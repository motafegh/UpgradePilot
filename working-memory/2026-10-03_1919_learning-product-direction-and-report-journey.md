# Learning Session — Product Direction, Hybrid Reporting, and Maintainer Utility

**Date/time:** 2026-10-03 19:19 Asia/Tehran
**Session status:** ACTIVE
**Primary responsibility/mode:** Learning/discussion only; no `main` mutation
**Branch:** `learning/product-direction-report-2026-10-03`
**Base:** `main@9b281229d8ac9094aec7c3315003267bdd8f6938`
**Related plan:** [Product Direction and Maintainer Utility Investigation](../plans/PRODUCT_DIRECTION_AND_MAINTAINER_UTILITY_INVESTIGATION_PLAN.md)
**Current live owner remains:** [MEMORY.md](../MEMORY.md)
**Procedure:** UP-SKILL:upgradepilot-working-memory

## Session anchor

Ali explicitly asked to keep the ongoing `main` work untouched and use this separate branch for learning, discussion, discovery, and durable notes that may be useful later.

This record is deliberately non-controlling. It may preserve hypotheses, questions, useful discoveries, and candidate implications, but it does not change the live project position, accepted semantics, selected implementation responsibility, or authorization on `main`.

## Current learning model

### Report is not merely a saved file

The report direction is understood as a product-facing decision-support layer:

```text
internal evidence / findings / uncertainty
        ↓
faithful projection
        ↓
maintainer-readable explanation
        ↓
decision-relevant unknowns
        ↓
justified next checks
        ↓
action or abstention when independently supported
```

Saving a report, preserving raw evidence, replaying analysis, rerunning acquisition, and recovering interrupted execution are separate promises.

### Hybrid direction hypothesis

Ali's current intuition is that action-led alone is unattractive because UpgradePilot cannot always justify a strong action, while hybrid allows useful assistance under uncertainty.

Refined engineering interpretation:

> Advisory usefulness and action permission have different evidence thresholds.

Hybrid should mean: provide the strongest useful decision-support output the evidence truthfully supports, while independently controlling whether a stronger action claim has been earned.

### Evidence strength ladder

```text
observed evidence
      ↓
supported interpretation
      ↓
material unresolved proposition
      ↓
justified discriminating check
      ↓
positively supported maintainer action
```

## Real-case learning anchors

### S014 — already satisfied vs installed by command

- Successful exact requirement execution may support "exact version satisfied/present at command completion."
- It does not necessarily support "this command installed the version."
- Later persistence, later exercise, compatibility, and merge safety remain separate propositions.

### S015 — marker-scoped applicability

- Changed requirements file consumed != changed exact requirement applies in this environment.
- A green sibling matrix row cannot establish a changed marker-scoped dependency when the marker does not apply there.
- Current normal product extraction does not support marker-bearing exact pins.
- Research knowledge must not be projected as current automated product output.

General rule:

```text
useful information exists in reality
        !=
UpgradePilot can currently acquire/derive it
        !=
UpgradePilot can currently present it
```

## Candidate discoveries worth carrying forward

1. Usefulness should be graded by claim strength, not binary action success.
2. Report projection should be decision-relevant rather than evidence-complete.
3. A good abstention should still identify the exact blocker and, when supported, a useful discriminating check.
4. A justified next check is a substantive product outcome and must not degrade into generic "run more tests."
5. Research-case insight and normal product capability must remain separate.
6. User-facing output likely benefits from layered presentation: concise decision support first, deeper provenance/evidence on inspection.

## Refinement — decision-driving prioritization and progressive disclosure

Current plans/specifications already require material, decision-relevant, discriminating output. The new learning is therefore a refinement rather than a missing product direction.

Possible refinement:

> The primary maintainer-facing layer should prioritize the smallest set of decision-driving findings, uncertainties, and next steps needed to make progress on the exact update, while supporting evidence/provenance remains inspectable through progressive disclosure rather than competing for equal prominence.

Open questions:

- How should multiple material findings be ordered?
- What belongs on the primary surface versus supporting detail?
- Can a fact be materially true but not currently decision-driving?
- What stable rule can prioritize content without opaque scoring or hiding relevant uncertainty?

## Learning — requirement declarations are a semantic family

S015 exposed that `package==version` is only the simplest dependency declaration form.

Marker support is already considered: S015 records it as a real future source-support question and freezes this invariant:

```text
package/version + marker + selected runtime environment
        ↓
applicable / non-applicable / unresolved
```

It is not the currently selected Build responsibility. Re-enter when a real finding, check, or action is blocked by the missing capability.

Adjacent forms that may matter:

1. bare exact pin: `pytest==9.0.3`;
2. marker-bearing pin: `pytest==9.0.3 ; python_version == "3.8"`;
3. extras: optional dependency selections such as `requests[security]`;
4. non-exact/range specifiers: `>=`, `<`, `~=`, `!=`, wildcards and compound ranges;
5. direct URL/VCS/archive references, where source/revision/artifact identity becomes part of the proposition;
6. requirements-file composition via included requirements and constraints;
7. editable/local/path forms and install options that affect source, selection, or resolver behavior.

Adjacent applicability/selection pressures outside one requirement line include:

- selected extras/groups/roots, already validated by S016;
- package Python-version compatibility metadata;
- wheel/artifact/platform compatibility;
- exact index/source/binary/hash policy;
- transitive dependency metadata with its own markers/extras.

Important conceptual decomposition:

```text
DECLARED DEPENDENCY PROPOSITION
identity + version constraint/direct source + extras + marker
        ↓
APPLICABILITY / SELECTION
runtime environment + selected extras/groups/roots
        ↓
RESOLUTION CONTEXT
index/source/binary/hash/configuration policy
        ↓
RESOLVED / OBSERVED PACKAGE STATE
exact artifact/version/environment/runtime evidence
```

Syntax recognition is not semantic support. Do not solve this by merely widening one regex.

Current evidence suggests a demand-driven priority:
marker applicability → extras/groups/selected roots → constraints/includes → non-exact ranges → direct references/local/editable forms → resolver/index/binary/hash policy as concrete decision pressure appears.

This taxonomy is a learning hypothesis, not implementation authorization or a new plan.

## Current route

Continue learning/discussion without changing `main`.

Near-term topics:
- distinguish a genuinely useful next check from generic/speculative advice;
- understand which dependency-declaration/applicability forms deserve future support based on real decision pressure;
- preserve any useful refinements here for later promotion through the correct owner if selected.


## Discovery — dependency propositions are context-composed, not source-line facts

### Status

**Learning discovery / candidate architectural principle.**
This is not yet an accepted `main` semantic change, implementation authorization, or roadmap commitment.

### Discovery

The S015 marker case and S016 selector/extra case expose the same deeper invariant from different mechanisms:

```text
source identity alone
!=
effective dependency proposition
```

A dependency declaration becomes meaningful only after the conditions that determine where and how it applies are composed with it.

A stronger conceptual model is:

```text
DECLARATION
package/distribution identity
+ version constraint or direct source
+ optional extras
+ optional environment marker
        ↓
APPLICABILITY / SELECTION
runtime/environment facts
+ selected extras/groups/roots
+ target/repository context
        ↓
RESOLUTION CONTEXT
constraints/includes
+ index/source configuration
+ binary/source/hash policy
+ other resolver-affecting configuration
        ↓
RESOLVED / OBSERVED STATE
exact selected version
+ artifact/source identity
+ selected environment
+ observed command/runtime state
        ↓
LATER USE / BEHAVIOR
whether the resolved dependency was actually exercised
+ relevant behavioral outcome
```

Each layer answers a different proposition. Evidence from one layer must not silently be promoted into a stronger claim owned by a later layer.

### Why this matters to UpgradePilot

UpgradePilot started from a deliberately narrow and useful form:

```text
package==version
```

That form collapses several dimensions because the package identity and requested version are explicit, with no marker, extra, or direct source reference.

Real Python dependency updates show that those simplifications do not always hold.

#### S015 — environment-marker pressure

```text
pytest==9.0.3 ; python_full_version == "3.8.*"
```

The same changed file can be consumed by multiple CI rows while the changed requirement applies only to some of them.

```text
file consumed
!=
changed requirement applicable
```

#### S016 — selector/extra/group pressure

The same `uv.lock` participates in multiple successful commands, but different extras/groups select different dependency sets.

```text
lock contains package
!=
selected environment contains package
```

Together:

```text
source + exact environment/selection context
→ effective dependency proposition
```

### Adjacent forms that can create similar semantic pressure

The project should recognize these as distinct possible capability families rather than variants to flatten into one parser rule:

1. **Bare exact pins** — example: `pytest==9.0.3`; strongest/simple current declaration form.
2. **Marker-bearing requirements** — example: `pytest==9.0.3 ; python_version == "3.8"`; requires applicability proof against the selected environment.
3. **Extras / optional dependency selection** — example: `requests[security]`; selected extras can change reachable transitive dependencies.
4. **Non-exact version constraints** — examples: `>=2,<3`, `~=2.1`, `!=2.1.4`, `==2.1.*`; declaration identifies an allowed set, not one exact installed version.
5. **Direct references** — URL/archive/VCS/revision forms; source/revision/artifact identity becomes part of the dependency proposition.
6. **Requirements-file composition** — included requirement files and constraints; source/provenance becomes relational rather than one-line/one-file.
7. **Editable/local/path/install-option forms** — can affect source identity, installation semantics, resolver behavior, and reproducibility.
8. **Package/runtime compatibility metadata** — Python-version compatibility and platform/wheel availability can make a syntactically valid declaration unresolved for a target environment.
9. **Resolver/source policy** — indexes, binary-vs-source policy, hashes, configuration and ambient resolver inputs can change what is obtainable without changing the declaration.
10. **Transitive dependency conditions** — dependency metadata can itself contain markers/extras/constraints that alter the effective graph.

### Architectural consequence

Do **not** solve these pressures by widening `_PINNED_REQUIREMENT_PATTERN` into a universal parser and then continuing to emit the same old proposition.

The important question is not:

> Can UpgradePilot parse this line?

It is:

> Which proposition can UpgradePilot truthfully establish from this declaration in this exact environment and resolution context?

Syntax recognition and semantic support are separate responsibilities.

A future implementation should preserve the dimensions needed downstream rather than normalize them away prematurely.

### Decision/proof consequence

When downstream reasoning uses dependency evidence, it should be able to distinguish at least conceptually:

```text
declared
applicable
selected/reachable
resolvable
resolved/present
later exercised
behaviorally successful
```

These states are not interchangeable.

Examples of prohibited collapses:

```text
declared         -> present
file consumed    -> requirement applied
lock membership  -> selected environment membership
command success  -> exact package installed
resolved/present -> later exercised
later exercised  -> behavior compatible/safe
```

### Priority rule

Do not pre-build universal Python packaging support.

Prefer:

```text
real maintainer-facing limitation
        ↓
identify exact missing proposition
        ↓
find which declaration/applicability/resolution dimension owns it
        ↓
test with contrasting real cases
        ↓
admit the smallest semantically complete capability
```

Current evidence-backed priority pressure:

1. marker applicability — real unsupported case in S015;
2. extras/groups/root selection — real case in S016 and partly modeled already;
3. constraints/includes when real source-provenance pressure appears;
4. non-exact ranges when exact-transition/state assumptions become limiting;
5. direct URL/VCS/local/editable identity when encountered;
6. broader resolver/index/binary/hash policy when it becomes decision-critical.

This ordering is provisional and may change with stronger real-case or user-value evidence.

### Relationship to current product direction

This discovery reinforces the hybrid/report discussion.

A useful maintainer report must not simply expose a parsed dependency line. It should expose the strongest supported meaning after applicability/selection and evidence limitations are accounted for.

For example, `pytest 9.0.3 appears in the changed file` is weaker than `pytest 9.0.3 applies to the Python 3.8 row, was attempted there, and resolution failed`.

The report should preserve that proof ladder rather than flattening all dependency evidence into one generic `dependency changed` statement.

### Re-entry / promotion condition

Promote this discovery into a durable `main` owner only when one of these becomes true:

- current report/evaluation work shows that missing declaration/applicability semantics materially blocks useful maintainer output;
- a selected implementation responsibility must support one of these forms;
- an accepted stable invariant needs to constrain multiple producers/consumers.

Until then:

- preserve the discovery here;
- do not create a new broad plan;
- do not expand the Charter/supported surface automatically;
- do not implement a universal requirement parser;
- do not treat S015/S016 research conclusions as normal product-produced facts.


## Current capability map — context-composed dependency proposition

Fresh source inspection of current `main` mapped the learning model against implemented producers and report projection.

### Layer 1 — declaration / source transition

**Supported, bounded:**
- conventional requirements/constraints files with exactly one bare `package==version` transition;
- exact `uv.lock` textual version transition under conservative structural comparison;
- one exact-version transition inside an existing `[project.optional-dependencies]` extra, using exact base/head `pyproject.toml` evidence.

**Partial / important boundary:**
- the pyproject optional-extra parser uses `packaging.Requirement` and retains extras/marker/url internally while comparing base/head, rejects marker changes, repeated marker forks, direct references and non-exact pins;
- however the successful output retains only package/version plus the containing extra. Marker applicability is not represented in `PyprojectOptionalExtraDependencyContext`.

**Unsupported in the normal conventional-requirements extractor:**
- marker-bearing pins such as `pytest==9.0.3 ; python_version == "3.8"`;
- non-exact/range transitions;
- direct URL/reference transitions;
- multiple simultaneous exact-pin transitions under the first rule.

Dependency-group context types exist, but current source inspection did not find a normal pyproject dependency-group extraction producer; do not describe the context type itself as current source capability.

### Layer 2 — applicability / selection

**Supported, bounded:**
- optional-extra selection/membership against explicit project-environment selectors;
- uv extras/groups/root selection plus selected-root reachability;
- source/project-root identity checks and explicit unresolved/not-established states.

**Missing / partial:**
- PEP 508 environment-marker truth against the exact selected runtime/matrix environment is not a first-class applicability proposition;
- selected extra/group membership therefore must not be confused with marker applicability.

### Layer 3 — resolution / package-manager context

**Supported, bounded for admitted pip paths:**
- package-manager operation declaration;
- manager environment selection;
- installation destination;
- mutation mode including dry-run pressure;
- direct-requirement handling;
- selected process-environment/persistent-config evidence and explicit unresolved states.

**Not a generic resolver model:**
- no universal index/source/hash/binary-policy/constraint/include semantics;
- no universal uv runtime package-state proof;
- ambient configuration is modeled only where current semantic dimensions require it.

### Layer 4 — resolved / observed package state

**Supported for first admitted Route-A family:**

```text
exact requirements source/applicability
+ supported direct-requirements consumption
+ admitted pip semantics
+ exact successful runtime command
→ RequirementSatisfiedAtCommandCompletion
```

This proves only exact proposed direct-requirement satisfaction at that successful command-completion boundary.

It explicitly does not prove:
- fresh installation causality;
- wheel/sdist/artifact identity;
- persistence after command completion;
- later use;
- behavioral compatibility;
- maintainer-action permission.

Other mechanisms such as uv selected environments do not automatically receive this package-state proof.

### Layer 5 — later use / behavior

**Supported, bounded:**
- static direct package invocation ordered after supported consumption;
- bounded correlation of that invocation to successful runtime execution.

This is still not:
- proof that the exact proposed version was the one exercised;
- broad affected-behavior coverage;
- compatibility/safety;
- maintainer-action permission.

Mechanism-specific impact/applicability owners can establish stronger scoped propositions separately; no generic behavioral-compatibility layer exists.

### Current report claim ladder

Current report projection already preserves much of this separation:

```text
exact source transition
→ "one supported exact version transition"
  NOT installation/compatibility

selection/consumption evidence
→ selected/reachable/static consumption
  NOT changed-version use

runtime-correlated consumption
→ exact command execution support
  NOT package-state truth by itself

RequirementSatisfiedAtCommandCompletion
→ exact proposed direct requirement satisfied at command completion
  NOT fresh install / persistence / later use / behavior

direct exercise correlation
→ bounded later invocation/execution evidence
  NOT general compatibility

mechanism-specific impact/applicability
→ scoped technical finding
  NOT maintainer-action authority
```

This strongly aligns the implemented report with the newly articulated context-composed proposition model.

### New candidate correctness gap — pyproject marker propagation

Source inspection exposed a credible gap requiring a focused reproducer before calling it a confirmed product defect.

Current chain:

1. `pyproject.py` parses PEP 508 markers and includes the marker in its internal comparison identity.
2. It rejects a **changed marker** and repeated same-package marker forks.
3. If only the exact version changes while the marker remains unchanged, the source logic appears able to admit the transition.
4. The successful result returns `ExtractedDependencyVersionChange + extra`; it does not retain the marker.
5. `PyprojectOptionalExtraDependencyContext` retains the extra but no marker.
6. `evaluate_project_source_environment_membership(...)` checks project root + extra/group selector membership only; it does not evaluate marker truth.

Potential consequence:

```text
changed optional-extra requirement:
numpy==1.0; python_version < "3.12"
→
numpy==2.0; python_version < "3.12"

selected extra on Python 3.12
        ↓
extra membership may be established
        ↓
marker non-applicability is not represented
```

If the full normal composition indeed admits that case, static dependency-consumption/report evidence could become stronger than justified.

**Status:** credible source-grounded concern, not yet a proven normal-path bug. Required next proof is one focused end-to-end or composition-level reproducer using an unchanged-marker version transition and a runtime/environment where the marker is false.

This is exactly the type of discovery the learning branch exists to preserve. Do not repair on this branch unless Ali explicitly authorizes it; first prove the normal-path behavior and determine the correct semantic owner.


### Freshness note for capability map

This capability map was reconciled against current `main@7edb33c7869c92c527d8f282c998f4710f3326d2` (2026-10-03), after the learning branch was originally created. The learning branch remains intentionally separate; this note records the source baseline used for the analysis rather than rebasing or changing `main`.
