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
A — IN PROGRESS — A1/A2 evidence pass complete; design acceptance pending Ali
B — NOT STARTED
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

Cycle 2 A is read-only with respect to product source/tests until its local migration decisions are resolved and Build is explicitly entered.

### Phase A progress — A1/A2 evidence pass

The first bounded A slice traced the current producer/consumer/orchestration path rather than choosing an API from the plan alone.

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

The current direct-exercise classifier then compares:

```text
(step_source_index, segment_index)
```

for supported consumption versus direct invocation. Runtime correlation, by contrast, already operates at the distinct outer location:

```text
(job_key, step_source_index)
```

This establishes that command occurrence identity is required for static composition *inside* one run step, while runtime-step identity remains a separate job/step proposition.

Current dependency unit tests also construct `RunStepDefinition` directly and test pip/uv domain semantics without workflow orchestration. That is useful separation pressure: migration should inject parser-neutral command analysis/occurrences into dependency observers rather than make those observers invoke shell parsing themselves.

#### A1 candidate decision — single analysis handoff seam

Evidence currently supports this direction:

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

The orchestration/composition seam should be the CI workflow-static interpretation path, because that layer already has workflow + job + step context and owns cross-evidence composition. GitHub continues to own shell syntax and the parser-neutral command IR. Dependency continues to own pip/uv meaning. CI continues to own package invocation and cross-evidence composition.

A consequence is that the current two-pass production shape (`derive_project_environment_consumptions(...)` followed later by `inspect_workflow_dependency_evidence(...)`) should not remain the final normal path if it causes the same workflow/run steps to be parsed/analyzed independently. Exact compatibility/refactor mechanics remain a Build decision after A closes.

This candidate is **not yet recorded as accepted**; Ali's reasoning/selection is still required.

#### A2 candidate decision — canonical static command identity

The evidence supports a layered identity rather than another flat ordinal.

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

Recommended representation: introduce one small provider-owned parser-neutral command-location value object derived from `StaticCommandOccurrence`, rather than copying raw span/order fields independently through every dependency/CI evidence type.

The value object's meaning must remain:

```text
exact static command occurrence location / source identity
```

and explicitly must **not** mean:

```text
runtime command identity
execution proof
success proof
same-path ordering proof
```

`source_order` may remain a derived deterministic ordering aid, but source span/occurrence identity is the canonical location. Downstream CI evidence combines the outer workflow/job/step identity with this inner location when a specific occurrence exists.

Important unresolved-state consequence: when parser/dependency interpretation is unresolved at step scope and no specific command occurrence can be justified, the evidence should not fabricate location `0` (the current `segment_index=0` placeholder pattern). The occurrence location should be absent or represented explicitly as step-scoped uncertainty; exact mechanics belong to A3/A4.

This candidate is **not yet recorded as accepted**; Ali's reasoning/selection is still required.

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

Cycle 2 must make shared occurrence source span/order the canonical static command identity. A derived source-order ordinal may remain only where an admitted contract truly needs it, and it must never imply runtime execution or same-path ordering.

---

## Cycle 2 A questions to resolve

A should answer these before Build:

### A1 — single analysis handoff seam

Where should one `RunStepDefinition` be analyzed exactly once?

Candidate direction to test against callers:

```text
workflow-level traversal
→ analyze_run_step_commands(workflow, job, step) once
→ pass StaticCommandAnalysis / relevant occurrences to dependency observers
```

This would prevent direct-install, project-environment, and CI invocation code from independently re-invoking parser logic or rebuilding identity.

The final seam must preserve ownership: GitHub owns command syntax; dependency modules own pip/uv meaning; CI owns cross-evidence composition.

### A2 — canonical static command location

Define the smallest cross-layer location/identity needed after `segment_index`.

Likely ingredients already proven by Cycle 1:

```text
step_source_index
+ occurrence.source_span
+ occurrence.source_order
```

Workflow path/revision and job key remain the outer CI/provider identity when evidence crosses workflow boundaries.

A must decide whether downstream evidence stores a dedicated location value object or the required fields directly.

### A3 — `segment_index` reconciliation

Trace every producer/consumer/test that still assumes segment ordinal. Classify each as:

```text
replace with canonical occurrence identity
retain only a derived source-order ordinal
remove because no longer justified
```

Do not preserve `segment_index` merely for compatibility with internal/private helpers.

### A4 — dependency observer interpretation

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
