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
A — COMPLETE
B — NEXT / NOT STARTED
C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

Phase A changed only design/state documentation. Product source/tests remain untouched. Build must be explicitly entered before consumer migration begins.

---

# Phase A accepted migration contract

## A1 — single analysis handoff seam — ACCEPTED

The evidence pass traced the current producer/consumer/orchestration path and found two independent workflow-static paths that currently parse/walk the same exact workflow source.

Accepted migration direction:

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

The current two-pass production shape (`derive_project_environment_consumptions(...)` followed later by `inspect_workflow_dependency_evidence(...)`) should not remain the final normal path if it causes the same workflow/run steps to be parsed/analyzed independently. Exact function compatibility/refactor mechanics remain Build decisions.

Ali's ownership reasoning matched this architecture: establish the reusable provider/IR fact once at the upper boundary instead of repeatedly reconstructing it in downstream consumers.

## A2 — canonical static command identity — ACCEPTED

Two identity levels remain distinct.

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

Preferred implementation direction: one small provider-owned parser-neutral command-location value object derived from `StaticCommandOccurrence`, conceptually:

```text
StaticCommandLocation
    source_span
    source_order
```

Exact class/field spelling remains a Build detail; the semantic contract is fixed.

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

Runtime static↔runtime correlation remains a separate job/step proposition. Neither identity level alone proves that an internal command executed.

## A3 — `segment_index` reconciliation — ACCEPTED

The old integer is overloaded across three responsibilities:

```text
1. occurrence identity / location
2. static ordering comparison
3. placeholder / validation convenience
```

Cycle 2 splits these responsibilities instead of renaming the integer.

### Direct requirements

```text
DirectInstallationObservation.matched_segment_index
→ replace with exact command occurrence location when one is established
```

No exact occurrence means no fabricated `0` location.

### Project-environment declarations

```text
ProjectEnvironmentSelectionDeclaration.segment_index
→ replace with command occurrence location
```

Multiple domain declarations derived from one occurrence may share one location.

### CI consumption evidence

```text
StaticDependencyConsumptionEvidence.segment_index
→ specific-occurrence evidence carries canonical location
→ step-scoped unresolved evidence carries no fabricated occurrence identity
```

### Direct package invocation

```text
DirectPackageInvocationEvidence.segment_index
_first_package_invocation_segment_index(...)
_shell_segments(...)
```

migrates to real parsed occurrences and canonical occurrence location. The duplicate textual CI command-structure path should disappear after migrated proof is green.

### Project-environment evidence validation

Replace raw-command re-splitting/segment-bounds validation with:

```text
outer workflow/revision/job/step identity
+ exact analyzed occurrence location
→ validate supplied static command relationship
```

### Ordering

Raw tuple comparison:

```text
(step_source_index, segment_index)
```

must not mechanically become:

```text
(step_source_index, source_order)
```

Identity, ordering, and unresolved/placeholder state are separate responsibilities.

Known tests that encode the old integer contract are migration pressure rather than retention authority, including direct-install, project-environment, workflow dependency evidence, and CI coverage fixtures.

Accepted A3 rule:

```text
identity
→ canonical typed command occurrence location

ordering
→ explicit bounded CI ordering relation; source_order only as an input

placeholder / ordinal-bounds validation
→ remove
```

## A4 — dependency observer interpretation — ACCEPTED

Dependency observers should receive the provider-owned `StaticCommandAnalysis` for the run step in addition to the existing step/default/path context. Passing the whole analysis preserves both real occurrences and analysis-level failure state without making dependency code invoke the parser.

Conceptual seam:

```text
RunStepDefinition
+ StaticCommandAnalysis
+ dependency-owned target/path context
→ dependency-domain observation
```

### Analysis-level state

```text
analysis.state == analyzable
→ inspect real occurrences

analysis unresolved / unsupported / parse_error
→ dependency observation remains unresolved where the command proposition cannot be decided
→ no textual/regex fallback
```

### Occurrence-level token policy

Dependency code consumes:

```text
occurrence.executable
occurrence.arguments
```

through their typed atom states.

```text
literal atom
→ may participate in admitted pip/uv interpretation

dynamic / unsupported atom in a material recognized command position
→ preserve unresolved

unrelated uncertainty
→ must not erase an already established positive static fact
```

Do not reconstruct raw command text and run `shlex`, regex shell segmentation, or another lexical parser to recover the same command identity.

A completely unrelated literal occurrence is ignored. A nonliteral/unanchored executable does not become positive pip/uv evidence merely because it could theoretically expand to anything; unresolved is preserved when a partially established/relevant pip/uv shape has material uncertainty.

### Direct requirements semantics retained

Admitted positive shapes remain the current bounded forms such as:

```text
pip / pip3 install -r ...
python / python3 -m pip install -r ...
```

Requirements options/paths are interpreted from typed argument atoms. Working-directory/path resolution remains dependency-owned through the existing context resolver.

A literal matching requirements path can establish the static declaration even if an unrelated argument elsewhere is dynamic. If the material requirements path/prefix cannot be decided, the result is unresolved rather than guessed.

### Project-environment semantics retained

Pip local-project and uv selector/package-scope meaning stays in `dependency/environment_selection.py`, but its input becomes parsed atoms rather than textual segments + `shlex`.

Current bounded domain rules remain, including:

- pip local-project path/extras;
- uv `sync` / `run` positive extras/groups;
- explicit package scope such as `--all-packages`;
- project-path and effective-working-directory binding;
- material negative/targeting flags remaining unresolved where required;
- positive selectors surviving unrelated uncertainty where sound.

### Structural-context rule for Cycle 2

All real parser-established command occurrences may participate in **static declaration presence** regardless of whether their structural context is straightforward, linear, short-circuit, conditional, loop, pipeline, function/block, or nested/subshell.

Those tags do not prove execution. They are preserved for CI ordering and Cycle 3 runtime-strengthening decisions.

Therefore:

```text
real conditional pip/uv command
→ may be a static declaration

real conditional pip/uv command
!= executed command
!= runtime-strengthening eligible command
```

## A5 — direct package invocation — ACCEPTED

CI continues to own the meaning “this real static command occurrence directly invokes the changed package.” GitHub command analysis remains package-agnostic.

Recognition moves from raw fragments to typed occurrence atoms.

The first migrated rule preserves the **currently admitted wrapper shapes** rather than opportunistically broadening CLI semantics:

```text
<package>
python -m <package>
python3 -m <package>
uv run <package>
poetry run <package>
pipenv run <package>
coverage run -m <package>
```

Package identity continues to use the current package / normalized-package candidate boundary. Exact comparison/helper spelling remains a Build detail.

A positive invocation carries the occurrence's canonical command location.

If a literal admitted wrapper/prefix is established but a material target/prefix atom is dynamic or unsupported, retain a typed unresolved invocation candidate rather than silently converting it to absence. A completely unrelated occurrence remains irrelevant.

This likely requires the migrated CI invocation contract to preserve observed versus unresolved invocation state rather than treating the tuple as positive-only. Exact class naming is a Build decision.

No new general uv/poetry/pipenv command-line parser is authorized by A5. Broader wrapper-option traversal is deferred unless concrete current evidence makes it necessary.

## A6 — same-step static ordering boundary — ACCEPTED

Replace direct tuple comparison with one CI-owned bounded relation whose semantic result is conceptually:

```text
ordered_after
not_after
unresolved
```

No generic control-flow graph is required.

### Different run steps in the same static job

Retain the currently admitted static step-order proposition from `step_source_index`:

```text
invocation step_source_index > consumption step_source_index
→ statically ordered after at the user-defined step level
```

This remains a static relation only; runtime execution/success is separate.

### Distinct occurrences inside the same run step

A same-step positive ordering relation is admitted only when:

1. both identities resolve to distinct real occurrences from the same shared analysis;
2. `consumption.source_order < invocation.source_order`;
3. the relevant occurrences are in a clean top-level linear-chain context; and
4. neither occurrence carries path-dependent/ambiguous structure such as:
   - `short_circuit`;
   - `conditional`;
   - `loop`;
   - `pipeline`;
   - `function_or_block`;
   - `nested_or_subshell`.

This preserves ordinary top-level newline/semicolon-style static ordering without pretending all source order is same-path structure.

### Unsupported/path-dependent same-step relation

If an invocation appears later in source but the structural relation is path-dependent/unsupported, keep the static invocation visible but classify the direct-exercise ordering proposition as **unresolved**, not supported.

If the invocation is definitely before the consumption, classify it as **not after / not established**.

### Same occurrence

A consumption and invocation mapped to the same command occurrence do not satisfy the strict “invocation after consumption” relation in Cycle 2. No wrapper-internal execution model is introduced here.

### Short-circuit correction

The current parser tag intentionally groups `&&` and `||` under `short_circuit`. Because those operators imply materially different path relationships, Cycle 2 does not infer same-step direct-exercise ordering from either form merely from source order. If future evidence requires that distinction, it must be added explicitly rather than guessed.

### Runtime boundary retained

Even `ordered_after` means only the bounded static composition relation. It does not establish that either command executed or succeeded. Cycle 3 owns command-level runtime-strengthening eligibility.

---

## Phase A closure result

All six pre-Build questions are resolved:

```text
A1 single analysis seam            → accepted
A2 canonical command identity      → accepted
A3 segment_index reconciliation    → accepted
A4 dependency atom interpretation  → accepted
A5 parsed package invocation       → accepted
A6 bounded static ordering         → accepted
```

No broader IR/ADR reassessment is required by the Phase A evidence. The Cycle 1 command IR is sufficient for the bounded Cycle 2 migration contract.

The next phase may now enter Build, subject to the normal explicit Build transition.

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
python -m pip check → PASS
34 focused + nearest-provider tests → PASS
```

This does not prove any migrated Cycle 2 consumer yet.

---

## Current migration pressure / Build targets

### Direct requirements

`src/upgradepilot/dependency/direct_install.py` still uses `bounded_shell_segments(...)`, regex command recognition, and `matched_segment_index`.

### Project-environment selection

`src/upgradepilot/dependency/environment_selection.py` still uses textual segmentation plus regex/`shlex` parsing and stores `segment_index`.

### CI command composition

`src/upgradepilot/ci/workflow_commands.py` still owns a second `_shell_segments(...)`, fragment-based package invocation, raw-command revalidation, and segment-index composition.

### Cross-layer evidence

`src/upgradepilot/ci/consumption.py` still exposes `segment_index`, and `src/upgradepilot/ci/dependency_exercise.py` still uses tuple ordering.

These are expected Build targets, not evidence that Phase A is incomplete.

---

## Cycle 2 Build stop line

When Build is explicitly entered:

- implement only the accepted A1–A6 migration contract;
- do not change Cycle 3 runtime-strengthening policy;
- do not introduce runtime logs/artifacts, matrix/reusable-workflow execution, Python/custom-interpreter analysis, exact installed-version/wheel evidence, Target redesign, or maintainer-action enablement;
- do not retain old textual splitters as positive-evidence fallback paths;
- if implementation evidence shows the Cycle 1 IR cannot express an accepted A1–A6 requirement, stop and return that exact gap to design rather than extending semantics ad hoc.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`
