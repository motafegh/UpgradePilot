# Dependency applicability and marker propagation — handoff to main

Date: 2026-10-03 (Asia/Tehran).  
Status: non-controlling handoff from `learning/product-direction-report-2026-10-03`; no source/spec/ADR/plan acceptance by this file.  
Main baseline reviewed: `0839e79a5307e09405800ce305d40e699428c428`.  
Relevant active main cycle: [Upstream API changes and target context — design cycle](2026-10-03_2023_upstream-api-and-target-context-design_lbd-cycle.md).  
Relevant current draft: [Upstream API changes and target context — design draft](../proposals/2026-10-03_UPSTREAM_API_CHANGE_AND_TARGET_CONTEXT_DESIGN_DRAFT.md).  
Relevant real-case evidence: [S015 marker-scoped applicability](../product-simulation/S015_POST_CASE_SYNTHESIS.md), [S016 selector/root reachability](../product-simulation/S016_POST_CASE_SYNTHESIS.md).

## Purpose

The parallel learning branch independently investigated report usefulness, marker-bearing requirements, dependency declaration forms and the current producer/report capability boundary. After reconciling those findings against current `main`, two items are worth handing to the active design review:

1. a design refinement directly relevant to target/dependency context;
2. a likely existing-product marker-propagation correctness defect that should be reproduced before repair.

Do not merge the learning branch wholesale. The rest of its exploratory taxonomy and report-presentation ideas remain useful background, not selected main work.

## 1. Design refinement — dependency relationships are context-composed

S015 and S016 expose the same higher-level rule through different mechanisms:

```text
source/declaration identity alone
!=
effective dependency proposition
```

A dependency relationship becomes decision-meaningful only after the conditions that define where/how it applies are preserved and composed.

Useful conceptual decomposition:

```text
DECLARATION
distribution identity
+ version constraint or direct source
+ extras
+ environment marker
        ↓
APPLICABILITY / SELECTION
runtime/target environment
+ selected extras/groups/roots
+ repository/project scope
        ↓
RESOLUTION CONTEXT
constraints/includes
+ index/source/binary/hash/configuration policy
        ↓
RESOLVED / OBSERVED STATE
exact selected version/artifact/environment
+ command/runtime evidence
        ↓
LATER USE / BEHAVIOR
exercise and mechanism-specific outcome
```

These are distinct propositions. Evidence from an earlier layer must not silently be promoted into a later-layer claim.

Examples of prohibited collapses:

```text
file consumed       -> changed requirement applies
extra selected      -> every requirement in that extra applies
lock membership     -> selected-environment membership
declared range      -> exact resolved version
command success     -> exact package freshly installed
resolved/present    -> later exercised
later exercised     -> compatible/safe
```

### Relevance to the active upstream-API/target-context draft

The current draft already preserves several of these distinctions correctly:

- declared dependency constraints versus actual resolution;
- target imports/static relationships versus runtime execution;
- upstream source change versus target applicability;
- candidate formulation versus action authority.

The handoff recommends making one additional invariant explicit during D/E review:

> **Normally acquired target/dependency relationship evidence must preserve the conditions that define applicability—especially extras, environment markers and version constraints—and must not flatten a conditional relationship into an unconditional dependency edge.**

This does **not** require implementing universal marker/range/resolver support in the first API-impact trial. Unsupported dimensions may remain explicit unknowns. The requirement is that existing conditions are not discarded and then treated as proven.

This matters immediately to the current HTTPX design evidence:

- distribution metadata already contains marker- and extra-conditioned `Requires-Dist` entries;
- the target path includes `fastapi[standard]`;
- the draft intentionally preserves unresolved framework/adapter version relationships.

Therefore the correct first-trial posture is:

```text
preserve conditional declaration
→ establish only the applicability/selection facts actually owned
→ keep unresolved conditions explicit
→ formulate only the strongest justified target-exposure proposition
```

## 2. Existing-product correctness concern — pyproject marker propagation

Fresh source tracing on current `main` indicates a likely normal-path semantic hole for an unchanged environment marker attached to a changed exact dependency inside a `pyproject.toml` optional extra.

### Current source path

#### Extraction

[src/upgradepilot/dependency/pyproject.py](../src/upgradepilot/dependency/pyproject.py):

- parses optional-dependency strings with `packaging.Requirement`;
- internal `_RequirementRecord` retains:
  - package identity;
  - dependency extras;
  - specifier;
  - marker;
  - URL;
- marker identity participates in conservative base/head comparison;
- changed markers are rejected;
- repeated same-package records that may encode marker forks are rejected;
- direct references and non-exact changed pins are rejected.

However, when only the exact version changes and the marker is unchanged, the successful result is reduced to:

```text
ExtractedDependencyVersionChange
+ containing optional-extra name
```

The marker itself is not retained in the downstream source context.

#### Source context

[src/upgradepilot/dependency/environment.py](../src/upgradepilot/dependency/environment.py):

`PyprojectOptionalExtraDependencyContext` retains repository, revision, package, source evidence and extra name, but no requirement marker/applicability condition.

#### Normal orchestration

[src/upgradepilot/investigation.py](../src/upgradepilot/investigation.py):

`_acquire_project_environment_sources(...)` passes this optional-extra context into normal workflow project-environment acquisition.

[src/upgradepilot/ci/workflow_commands.py](../src/upgradepilot/ci/workflow_commands.py):

for non-`uv.lock` project contexts, normal composition calls:

`evaluate_project_source_environment_membership(context, declaration)`

and then:

`compose_project_environment_consumption(...)`.

#### Membership

[src/upgradepilot/dependency/environment_membership.py](../src/upgradepilot/dependency/environment_membership.py):

optional-extra membership currently checks:

- project root alignment;
- whether the affected optional extra/all extras is selected.

It does not evaluate the changed requirement's PEP 508 environment marker against the exact selected runtime/matrix environment.

### Concrete risk shape

```text
base:
numpy==1.0 ; python_version < "3.12"

head:
numpy==2.0 ; python_version < "3.12"

workflow/environment:
Python 3.12
+ affected extra selected
```

The changed requirement is not applicable on Python 3.12.

But the current downstream context no longer carries the marker, so normal source-environment membership can potentially establish:

```text
selected_project_environment_contains_changed_dependency
```

from extra selection alone.

That would violate the S015 invariant:

```text
source/extra consumed or selected
!=
exact changed requirement applicable
```

### Current confidence

This is stronger than a speculative architecture concern because the normal composition path has been traced end to end and no later marker-applicability gate was found.

However, do **not** repair solely from static inspection. The correct next proof is one focused normal-path/composition-level regression reproducer.

Suggested reproducer:

```text
exact base/head pyproject.toml:
  same optional extra
  same marker: python_version < "3.12"
  exact pin changes 1.0 -> 2.0

exact workflow:
  selects that extra
  represents/targets Python 3.12

question:
  does UpgradePilot emit supported project-environment consumption for the
  changed dependency despite the marker being false?
```

Pass expectation for safe behavior:

- either marker-aware applicability prevents positive consumption;
- or the case remains explicitly unresolved/not established because exact marker truth is not owned.

Failure signal:

- positive changed-dependency consumption is established solely from extra membership while the marker condition is false/unrepresented.

If reproduced, the repair belongs upstream of reporting, in dependency source/applicability composition. Do not patch the report to hide the stronger incorrect producer claim.

## 3. Recommended disposition for current main D/E review

Carry these two items into the active design discussion:

### A. Add/confirm the design invariant

The first upstream-API/target-context trial must preserve conditional dependency semantics. Extras, markers and version constraints should remain distinguishable from actual applicability/resolution.

This is a **design constraint**, not authorization for universal Python-packaging support.

### B. Run one focused marker-propagation reproducer before admitting broader target-context implementation

The reproducer is proportionate because it tests a potential existing correctness problem in current product evidence, not a speculative future feature.

If it reproduces:

1. identify the earliest adequate semantic owner;
2. preserve marker provenance/applicability rather than strip it;
3. evaluate it only against justified environment evidence;
4. keep matrix/environment uncertainty explicit when variables are not bound;
5. add regression coverage;
6. then reassess what the report is allowed to project.

If it does not reproduce, record the actual protecting boundary and retire/narrow the concern.

## 4. Non-goals

This handoff does **not** recommend:

- merging the learning branch into `main`;
- building a universal requirement parser;
- adding all PEP 508/440 forms now;
- implementing general resolver simulation;
- broad VCS/path/index/hash support;
- changing maintainer-action permission;
- weakening source-authority checks;
- treating S015/S016 manual/research conclusions as normal product-produced facts;
- changing report prose to compensate for missing or incorrect producer semantics.

Other discovered declaration families—ranges, direct references, includes/constraints, local/editable sources, broader resolver policy and transitive conditions—remain demand-driven future pressures unless a real user-facing proposition is blocked.

## 5. Relationship to report/product-direction learning

The parallel branch also refined a report principle:

> primary maintainer output should prioritize decision-driving findings/unknowns/next steps, with supporting provenance available through deeper inspection.

That remains useful, but it is not the immediate blocker exposed by current main development cases. The current main work correctly shows that missing semantic evidence cannot be repaired by rendering.

Re-enter presentation prioritization during report-usefulness evaluation after the producer-side evidence is sufficient for the selected cases.

## Handoff summary

```text
CURRENT MAIN DESIGN
upstream change meaning
+ exact target context
+ unresolved resolution/activation
        ↓

ADD THIS CONSTRAINT
conditional dependency declarations must retain
extras/markers/version constraints as applicability conditions
        ↓

EXISTING PRODUCT CHECK
prove whether pyproject optional-extra marker information
is currently lost before environment-membership composition
        ↓

ONLY THEN
admit/fix the smallest semantically complete owner
without broad parser/resolver expansion
```

This handoff changes no live selection by itself. `MEMORY.md` and the active design cycle remain authoritative for the next admitted responsibility.
