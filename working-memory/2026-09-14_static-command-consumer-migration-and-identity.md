# Static Command Consumer Migration and Identity — Working Memory

**Date:** 2026-09-14  
**Session status:** ACTIVE  
**Primary mode:** Learning-by-Doing — Cycle 2  
**Selected parent plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Selected bounded implementation plan:** [`../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`](../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md)  
**Accepted architecture:** [`../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`](../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md)  
**Previous cycle closure:** [`2026-09-13_static-workflow-command-three-cycle-implementation.md`](2026-09-13_static-workflow-command-three-cycle-implementation.md)

## Three-cycle execution map

```text
Cycle 1 — parser, shell-context, shared command-analysis foundation — CLOSED ✅
Cycle 2 — static evidence consumer migration + command identity — CURRENT
Cycle 3 — runtime-strengthening correctness + consolidation + broad proof — PLANNED
```

Cycle 2 uses the normal top-level loop:

```text
A → B → C → D → E
```

This is not a sub-cycle of Cycle 1. Cycle 1 established the trustworthy producer. Cycle 2 now migrates static consumers onto that producer while preserving dependency/CI ownership boundaries.

---

## Cycle 2 responsibility

```text
shared StaticCommandAnalysis / StaticCommandOccurrence
→ direct requirements observation
→ project-environment selection
→ CI direct package invocation
→ canonical command identity / segment_index reconciliation
→ bounded same-step static ordering correction
```

Cycle 2 does **not** own runtime-strengthening eligibility. The proposition:

```text
static command exists
!= command executed
!= command succeeded
```

remains intact throughout this cycle.

## Current state

```text
A — IN PROGRESS — A1/A2/A3 RESOLVED; A4 NEXT
B — NOT STARTED
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

Cycle 2 A is read-only with respect to product source/tests until its local migration decisions are resolved and Build is explicitly entered.

---

## Phase A accepted decisions so far

### A1 — single analysis handoff seam — ACCEPTED

The evidence pass traced the current producer/consumer/orchestration path rather than choosing an API from the plan alone.

Observed current flow:

```text
investigation.py
→ acquire exact workflow definition source
→ derive_project_environment_consumptions(source, ...)
   → parse_workflow_definition(source)
   → walk jobs/steps
   → dependency project-environment observer

then

WorkflowDependencyCoverageInput
→ evaluate_dependency_ci_coverage(...)
→ inspect_workflow_dependency_evidence(source, ...)
   → parse_workflow_definition(source) again
   → walk jobs/steps again
   → direct-requirements observer
   → CI direct-package invocation scanner
   → validate precomposed project-environment evidence by re-splitting raw command text
```

The accepted migration direction is:

```text
one workflow-level CI traversal over one parsed WorkflowDefinition
→ for each RunStepDefinition:
     analyze_run_step_commands(definition, job, step) exactly once
→ pass that StaticCommandAnalysis / relevant StaticCommandOccurrence values to:
     direct requirements interpretation
     project-environment interpretation
     CI direct-package invocation interpretation
→ compose all resulting static evidence from the same occurrence identities
```

Ownership remains:

```text
GitHub/provider layer
→ effective shell semantics + shell syntax + parser-neutral command IR

Dependency layer
→ pip / uv / requirements / project-selection meaning

CI layer
→ workflow traversal + checkout provenance + cross-evidence composition
→ direct package invocation + bounded static ordering relations
```

The current two-pass production shape (`derive_project_environment_consumptions(...)` followed later by `inspect_workflow_dependency_evidence(...)`) should therefore not remain the final normal path if it causes the same workflow/run steps to be parsed/analyzed independently. Exact function compatibility/refactor mechanics remain Build decisions after A closes.

Ali's ownership reasoning matched the architecture: establish the reusable provider/IR fact once at the upper boundary instead of repeatedly reconstructing it in downstream consumers.

### A2 — canonical static command identity — ACCEPTED

The accepted model keeps two identity levels distinct.

Outer exact workflow/CI identity:

```text
workflow path
+ workflow revision
+ job key
+ step_source_index
```

Inner command occurrence identity within that exact run step:

```text
CommandSourceSpan
+ deterministic source_order
```

The preferred implementation direction is one small provider-owned parser-neutral command-location value object derived from `StaticCommandOccurrence`, conceptually:

```text
StaticCommandLocation
    source_span
    source_order
```

The exact class/field name remains a Build detail, but the semantic contract is accepted.

Its meaning is only:

```text
exact static command occurrence location / source identity
```

It does **not** mean:

```text
runtime command identity
execution proof
success proof
same-path ordering proof
```

Runtime static↔runtime correlation remains a separate job/step proposition. A command occurrence is the finer static identity inside that step. Neither identity level alone proves that the command executed.

`source_order` remains a deterministic source-order aid. Source span plus source order form the inner parser-neutral occurrence identity; downstream CI evidence combines the outer workflow/job/step identity with this inner location when a specific occurrence is established.

Ali delegated the technical selection for this identity boundary after establishing the A1 architectural reasoning; this two-level model is therefore the accepted Cycle 2 direction.

### A3 — `segment_index` reconciliation — ACCEPTED

The caller/test trace shows that the old integer is overloaded across three different responsibilities:

```text
1. occurrence identity / location
2. static ordering comparison
3. placeholder / validation convenience
```

Cycle 2 will split those responsibilities instead of renaming `segment_index` and preserving the overload.

#### A3.1 Direct requirements

Current:

```text
DirectInstallationObservation.matched_segment_index
```

Migration:

```text
replace with exact command occurrence location when one occurrence is established
```

The dependency observer must not retain a shell-segment ordinal contract. If the result is unresolved at step/analysis scope and no exact occurrence is justified, it must not manufacture location `0`.

#### A3.2 Project-environment declarations

Current:

```text
ProjectEnvironmentSelectionDeclaration.segment_index
```

Migration:

```text
replace with command occurrence location
```

A declaration interpreted from a real parsed occurrence carries that occurrence location. Multiple domain declarations derived from one occurrence may legitimately share the same command location. An unresolved observation that has not established a specific occurrence remains step/analysis scoped rather than receiving a fake location.

#### A3.3 CI consumption evidence

Current:

```text
StaticDependencyConsumptionEvidence.segment_index
```

Migration:

```text
specific-occurrence evidence → canonical command location
step-scoped unresolved evidence → no fabricated occurrence location
```

The precise optionality/type mechanics are a Build decision, but the semantic rule is fixed: absence of justified occurrence identity is represented as absence/unresolved state, not integer zero.

#### A3.4 Direct package invocation

Current:

```text
DirectPackageInvocationEvidence.segment_index
_first_package_invocation_segment_index(...)
_shell_segments(...)
```

Migration:

```text
real parsed StaticCommandOccurrence
→ CI-owned package-invocation interpretation
→ evidence carries canonical occurrence location
```

The private textual `_shell_segments(...)` owner and `_first_package_invocation_segment_index(...)` path should disappear from the normal migrated path once Build is proven.

#### A3.5 Project-environment evidence validation

Current validation re-splits `evidence.command`, checks `segment_index` bounds, and separately checks job/step/command text.

Migration:

```text
outer workflow/revision/job/step identity
+ exact analyzed occurrence location within that step
→ validate the supplied static command relationship
```

Do not re-derive command identity by splitting the raw command again.

#### A3.6 Static direct-exercise ordering

Current direct-exercise composition compares:

```text
(step_source_index, segment_index)
```

This raw tuple comparison must **not** mechanically become:

```text
(step_source_index, source_order)
```

Instead:

```text
different steps in the same static job
→ step_source_index may establish static step source order

same step
→ source_order is only an input to a bounded structural ordering relation
→ source_order alone does not establish same execution path
```

The exact same-step relation is deliberately deferred to A6. This prevents A3 from silently turning source order into control-flow proof.

Runtime correlation remains at:

```text
job_key + step_source_index
```

and does not require command occurrence identity until Cycle 3 defines a separate runtime-strengthening policy.

#### A3.7 Test migration pressure

Known current tests intentionally expose the old contract and therefore must change during Build rather than constrain the architecture:

- `tests/test_direct_install_declaration.py` asserts `matched_segment_index` values;
- `tests/test_project_environment_selection.py` asserts multiple static segment indices;
- `tests/test_workflow_dependency_evidence.py` manually constructs CI evidence with `segment_index=0`;
- `tests/test_ci_dependency_coverage.py` constructs project-environment declarations with `segment_index=0`, copies that field across identity-mismatch fixtures, and proves install-before-invocation versus invocation-before-install behavior inside one `run:` block;
- R6 workflow integration tests exercise the production seam and must continue proving that callers do not prebuild semantic evidence.

The semantic behavior worth retaining is the evidence proposition and ordering distinction, not the old integer field.

### A3 result

The accepted replacement rule is therefore:

```text
identity
→ canonical typed command occurrence location

ordering
→ explicit bounded ordering relation; source_order only as an input

placeholder / ordinal-bounds validation
→ remove
```

This closes A3 without deciding A6 prematurely.

---

## Established Cycle 1 handoff

Cycle 2 may rely on these proven foundation contracts:

- `resolve_effective_shell_context(...)` owns the effective static shell choice;
- `analyze_run_step_commands(...)` converts an admitted run step into parser-neutral command analysis;
- `StaticCommandOccurrence` is a real syntactic command occurrence, not a regex fragment;
- comments and quoted command-looking payloads do not become independent commands;
- source spans and deterministic source order are preserved;
- executable/argument atoms distinguish literal, dynamic, and unsupported meaning;
- structural context distinguishes straightforward top-level, linear-chain, short-circuit, conditional, loop, pipeline, function/block, and nested/subshell cases;
- parser/shell uncertainty remains explicit and does not fall back to textual splitting.

Cycle 1 proof horizon:

```text
parser characterization PASS
pip check PASS
34 focused + nearest-provider tests PASS
```

This does not prove any migrated Cycle 2 consumer yet.

---

## Current migration pressure discovered during Cycle 1 E

### 1. Direct requirements

`src/upgradepilot/dependency/direct_install.py` currently:

- calls `bounded_shell_segments(step.command.text)`;
- recognizes pip-install shape through regex over one text segment;
- finds requirements paths through regex inside that segment;
- returns `matched_segment_index` as its static location.

Its dependency-domain responsibility should remain:

```text
real static pip-install occurrence
+ independently established requirements source path
+ resolved working-directory context
→ direct installation declaration observation
```

The command-analysis layer must not become dependency-aware.

### 2. Project-environment selection

`src/upgradepilot/dependency/environment_selection.py` currently:

- calls the same textual segment splitter;
- identifies pip/uv candidates by regex;
- reparses candidate segments with `shlex`;
- stores `segment_index` in `ProjectEnvironmentSelectionDeclaration`;
- owns pip local-project and uv selector semantics.

The migration should preserve those dependency-domain semantics while sourcing executable/argument identity from shared parsed occurrences.

### 3. CI direct package invocation and composition

`src/upgradepilot/ci/workflow_commands.py` currently:

- has a separate private `_shell_segments(...)` implementation;
- detects direct package invocation by scanning those fragments;
- stores `segment_index` in `DirectPackageInvocationEvidence`;
- validates project-environment evidence by re-splitting the original command text and checking segment ordinal bounds;
- constructs direct-requirements consumption evidence from `matched_segment_index`.

This duplicate command-structure owner must disappear from the normal path once migration completes.

### 4. Cross-layer location contract

`src/upgradepilot/ci/consumption.py` currently stores:

```text
workflow path/revision
job key
step source index
segment_index
command text
```

in `StaticDependencyConsumptionEvidence`.

`segment_index` therefore has cross-layer migration pressure. It is not merely a private helper detail.

Cycle 2 makes shared occurrence source span/order the canonical static command identity. A derived source-order ordinal may remain only where an admitted relation truly needs it, and it must never imply runtime execution or same-path ordering.

---

## Remaining Cycle 2 A questions

### A4 — dependency observer interpretation — NEXT

Decide how `direct_install.py` and `environment_selection.py` consume:

```text
occurrence.executable
occurrence.arguments
literal/dynamic/unsupported atom states
structural context
```

while preserving their existing domain semantics and unresolved behavior.

Important question: which structural contexts are allowed to establish **static declaration presence** in Cycle 2? A command may be conditional or short-circuited yet still be a real static declaration. Cycle 2 must avoid importing Cycle 3 runtime-strengthening restrictions into static observation unnecessarily.

### A5 — direct package invocation

Move package invocation recognition onto real occurrences while keeping package-name/prefix meaning in CI, not in the GitHub parser layer.

The current admitted prefixes (`python -m`, `uv run`, `poetry run`, `pipenv run`, `coverage run -m`, direct invocation) need to be mapped to parsed atoms rather than raw text fragments.

### A6 — same-step static ordering boundary

Source order is available, but:

```text
source order
!= same execution path
```

Cycle 2 A must identify which current static direct-exercise composition can safely continue using order and which must become unresolved/not-established until Cycle 3 or a stronger structural relation is available.

Do not build a generic control-flow graph unless concrete implementation evidence proves the bounded structural tags insufficient.

---

## Cycle 2 stop line

Until A completes, do not:

- modify direct-install/project-environment/CI command consumers;
- remove old splitters;
- change runtime-strengthening/static↔runtime correlation policy;
- interpret successful runtime steps as command-level execution;
- expand into runtime logs/artifacts, matrix/reusable-workflow execution, Python/custom interpreter analysis, or maintainer-action enablement.

If A exposes a requirement for a broader command IR than Cycle 1 proved, return that specific gap to design rather than silently extending semantics inside consumers.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`
