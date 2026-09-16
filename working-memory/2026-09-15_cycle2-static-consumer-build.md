# Cycle 2 Static Consumer Build — Working Memory

**Date:** 2026-09-15 → 2026-09-16  
**Session status:** ACTIVE — Phase B implementation complete; executable proof gate still open  
**Primary mode:** Learning-by-Doing — Cycle 2 / Phase B Build  
**Selected parent plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Selected bounded implementation plan:** [`../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`](../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md)  
**Accepted architecture:** [`../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md`](../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md)  
**Phase A decision owner:** [`2026-09-14_static-command-consumer-migration-and-identity.md`](2026-09-14_static-command-consumer-migration-and-identity.md)

## Current Cycle 2 state

```text
A — COMPLETE
B — IN PROGRESS
    implementation: COMPLETE through B1+B2+B3+B4+B5
    executable proof: PENDING / currently unavailable from this runtime
C — NOT STARTED formally
D — NOT STARTED
E — NOT STARTED
```

Phase B is not called closed yet because the accepted proof requirement includes executable focused/nearby validation. Progressive state preservation has been performed throughout B, but formal Phase C is not entered while the Phase-B proof gate remains open.

Learning cadence agreed with Ali:

```text
each bounded Build slice
→ brief what / why / remaining-transition checkpoint

Phase B final implementation + executable validation
→ one proper integrated implementation-learning session over the stable code
```

Ali explicitly asked on 2026-09-16 that the implementation journey, problems, surprises, corrections, and proof limits from every Phase-B section be preserved so the later learning session can use this record together with the final source/tests. This working memory therefore keeps the meaningful engineering progression rather than only the resulting code state.

---

## Phase A contract implemented by B

Phase B implements only the accepted A1–A6 migration contract:

```text
A1  one workflow traversal + one StaticCommandAnalysis per run step
A2  outer workflow/job/step identity + inner StaticCommandLocation
A3  remove segment_index identity/ordering/placeholder overload
A4  dependency observers interpret typed parser-neutral atoms
A5  package invocation comes from real parsed command occurrences
A6  CI owns explicit ordered_after | not_after | unresolved relation
```

Persistent boundary:

```text
static command occurrence
!= command execution
!= command success
```

Cycle 3 runtime-strengthening policy remains out of scope throughout this record.

---

# B1 — provider command location + direct-install parser-backed seam

**State:** IMPLEMENTED; execution proof deferred to the Phase-B final proof gate.

### Why B1 was the first slice

The migration needed a provider-owned parser-neutral identity before downstream dependency/CI contracts could stop using textual segment ordinals. The smallest safe first seam was therefore:

```text
StaticCommandOccurrence
→ StaticCommandLocation
→ direct-install observer accepts StaticCommandAnalysis
```

This deliberately avoided changing the larger CI composition surface before the dependency-facing contract was real.

### Implemented

Added:

`src/upgradepilot/github/workflow_command_location.py`

with:

```text
StaticCommandLocation
    source_span
    source_order
```

Its meaning is exact static source occurrence/location only; it is not runtime identity or execution proof.

Updated:

`src/upgradepilot/dependency/direct_install.py`

The direct-install observer now:

- consumes `StaticCommandAnalysis` and typed `StaticCommandAtom` values;
- recognizes the existing bounded `pip`/`pip3` and `python`/`python3 -m pip install` forms;
- reads `-r` / `--requirement` paths from typed atoms rather than shell text splitting;
- leaves working-directory/path resolution dependency-owned;
- returns unresolved on analysis failure or material token/path uncertainty;
- permits a matching literal requirements path to survive unrelated dynamic arguments when sound;
- accepts a real static occurrence even inside path-dependent structure because declaration presence is not execution proof;
- carries canonical `command_location` when a specific occurrence is established.

Focused tests in `tests/test_direct_install_declaration.py` were rebuilt around parser-neutral `StaticCommandAnalysis` fixtures so dependency-domain tests do not own a Tree-sitter parser.

### Important reasoning / learning pressure

The key ownership lesson was that a dependency observer should know pip semantics, not shell grammar. Parser nodes therefore remain private to the GitHub/provider layer; the dependency boundary receives UpgradePilot-owned typed atoms and occurrence identity.

### Commits

```text
a5d372b525ee0e7b2c23bb8e17755fd6a01e2a93  feat: add static command location identity
6566de0603c532653040ea42860502aaed044529  feat: consume parsed command analysis for direct installs
527a4c9234607654f8be3da9b672a73758c22c88  test: prove parser-backed direct install observation
c6006285e5860809d798a3177a9c4c6a9424cd49  docs: preserve cycle 2 build slice one
```

### Proof boundary at B1

```text
implementation committed
+ focused proof assets written
+ connector source/diff inspection
!= focused tests executed
!= production CI direct-requirements migration complete
```

---

# B2 — production direct requirements + parsed package invocation + bounded ordering

**State:** IMPLEMENTED; execution proof deferred to the Phase-B final proof gate.

Commit:

```text
328e0b2eee3652e6a552a7b1cfbfda3c46b4c44a
feat: migrate direct CI command evidence to parsed identity
```

### Why B2 became a coupled slice

Once direct-requirements evidence stopped using the old ordinal, the existing direct-exercise classifier could no longer safely compare:

```text
(step_source_index, segment_index)
```

Fabricating a replacement integer merely to preserve the classifier would have violated A3/A6. The smallest coherent Build slice therefore had to migrate the coupled chain together:

```text
shared run-step analysis
→ direct requirements
→ direct package invocation
→ canonical locations + structure
→ explicit CI ordering relation
```

This was an important implementation discovery: a field that looked local was actually carrying several cross-module propositions.

### Production handoff

For each readable run step in the normal CI evidence path:

```python
command_analysis = analyze_run_step_commands(definition, job, entry)
```

is established once and reused by direct requirements and package invocation.

### Direct-install compatibility removed

The B1 temporary regex/text-split compatibility route was removed. `direct_install.py` requires caller-supplied `StaticCommandAnalysis`; no textual positive-evidence fallback remains for this migrated consumer.

### Package invocation migrated

CI package invocation now interprets real parsed occurrences and preserves only the accepted bounded shapes:

```text
<package>
python/python3 -m <package>
uv run <package>
poetry run <package>
pipenv run <package>
coverage run -m <package>
```

A recognized wrapper/prefix with a material dynamic or unsupported target remains typed `unresolved` evidence rather than being erased as absence.

### Explicit static-order owner

Added:

`src/upgradepilot/ci/static_command_order.py`

with the bounded relation:

```text
ordered_after | not_after | unresolved
```

Implemented boundary:

- different job → `not_after`;
- later user-defined step in the same job → `ordered_after`;
- earlier step → `not_after`;
- same-step parsed occurrence must have strictly greater `source_order`;
- later source order under short-circuit / conditional / loop / pipeline / function-or-block / nested-or-subshell structure → `unresolved`;
- same/earlier occurrence → `not_after`;
- temporary parsed/legacy identity mixing did not guess an ordering.

Even `ordered_after` is a static composition statement, not runtime execution evidence.

### Test/proof assets introduced or reconciled

```text
tests/test_static_command_order.py
tests/test_parser_backed_ci_command_evidence.py
tests/test_ci_static_direct_exercise_order.py
tests/test_workflow_dependency_evidence.py
tests/test_ci_dependency_coverage.py
```

These preserve clean same-step order, before-consumption order, short-circuit unresolved behavior, parser-backed consumption/invocation identity, quoted payload false-positive protection, repository-checkout provenance, and shell-context uncertainty.

Synthetic CI tests were corrected to state Bash explicitly when their responsibility is CI composition rather than shell selection. This preserved the provider rule that an omitted/unknown runner cannot be guessed into a default shell.

### B2 proof issue encountered

GitHub reported zero workflow runs for the B2 commit. `.github/workflows/product-verification.yml` is intentionally `workflow_dispatch` only, so push did not produce hosted execution proof.

B2 therefore remained source/diff-audited but not executable-proven.

---

# B3 — project-environment selection migration

**State:** IMPLEMENTED.

Commit:

```text
7cb7820bf284b3f1fd2a62e0623a23917f9b2790
feat: migrate project environment selection to parsed commands
```

Files materially involved:

```text
src/upgradepilot/dependency/environment_selection.py
src/upgradepilot/dependency/pip_command.py        (new shared pip-prefix helper)
src/upgradepilot/dependency/direct_install.py
src/upgradepilot/ci/consumption.py
src/upgradepilot/ci/workflow_commands.py
tests/test_project_environment_selection.py
```

### Why B3 existed

After B2, project-environment selection was the last semantic consumer still reconstructing command segments with textual splitting / regex / `shlex` and carrying a real `segment_index`. That meant Cycle 2 still had two command-meaning systems.

B3 moved pip local-project and uv project-selection semantics onto the same `StaticCommandAnalysis` and `StaticCommandOccurrence` IR as direct requirements and package invocation.

### Project-environment observer migration

`observe_project_environment_selection(...)` now receives caller-supplied `StaticCommandAnalysis` and interprets typed atoms.

Preserved bounded semantics include:

```text
pip local project / editable project
explicit optional extras
uv sync / uv run
--extra / --group / --only-group
--all-extras / --all-groups
--project
--all-packages package scope
material negative / project-targeting flags remaining conservative
```

No scope was added merely because parser atoms made broader CLI interpretation possible.

Each concrete declaration now carries:

```text
command_location
structural_context
```

Real conditional/short-circuit/etc. occurrences may still establish static declaration presence; they do not gain execution authority.

### Shared pip-prefix helper discovered during implementation

Both direct-install and project-environment observers needed the same typed recognition of:

```text
pip/pip3 install ...
python/python3 -m pip install ...
```

Keeping two separate typed-prefix implementations would have recreated duplication immediately after removing textual duplication. The smallest independent shared dependency-domain responsibility was extracted to:

`src/upgradepilot/dependency/pip_command.py`

This helper identifies the pip-install command shape only; direct requirements and local-project semantics remain owned by their respective observers.

### Unresolved evidence identity correction

The legacy path had fabricated `segment_index=0` when project-environment uncertainty was step-scoped and no exact command occurrence had been established.

B3 stopped manufacturing that identity. For unresolved project-environment evidence, CI preserves a canonical location/structure only when one unique declaration occurrence actually exists; otherwise location remains absent.

This is an important evidence-model lesson for later learning:

```text
"we know the step is relevant/unresolved"
!=
"we know which inner command occurrence it is"
```

### What intentionally remained after B3

B3 migrated command semantics and identity, but the normal investigation still did:

```text
derive_project_environment_consumptions(...)
→ parse/walk workflow

then later

inspect_workflow_dependency_evidence(...)
→ parse/walk same workflow again
```

So B3 was semantically migrated but A1 was not fully realized at the workflow orchestration level. This became the explicit B4 pressure rather than being hidden as acceptable final architecture.

### B3 proof assets

`tests/test_project_environment_selection.py` was rebuilt around parser-neutral analysis fixtures and canonical locations, including dynamic/material uncertainty, uv child-command option boundaries, package scope, multiple occurrence locations, and parse-failure behavior.

Existing real R6 project-environment integration remained the production seam to protect rather than inventing a second integration harness.

### B3 proof boundary

The source/diff contract was audited. Executable tests remained unavailable for the same environment/workflow reasons already present in B2.

---

# B4 — one workflow traversal / one run-step analysis in the normal product path

**State:** IMPLEMENTED.

Commit:

```text
069e61c2c65a282ba21472b361035ecbc4223eae
feat: consolidate static workflow evidence traversal
```

Primary files:

```text
src/upgradepilot/ci/workflow_commands.py
src/upgradepilot/ci/dependency_exercise.py
src/upgradepilot/investigation.py
tests/test_single_pass_workflow_static_evidence.py
```

### Why B4 existed

B3 removed duplicate command parsers, but normal application orchestration still duplicated the entire workflow parse/traversal. That contradicted accepted A1 even though both traversals used the correct parser.

The exact problem was:

```text
investigation.py
→ derive_project_environment_consumptions(...)
→ parse + jobs/steps walk + command analyses

later coverage evaluation
→ inspect_workflow_dependency_evidence(...)
→ parse + jobs/steps walk + command analyses again
```

The correction was not another parser change. It was an ownership/orchestration change.

### Final production handoff shape

The normal application now acquires exact project-environment **source bundles**, not precomputed project-environment consumptions, and passes them into CI coverage input.

`inspect_workflow_dependency_evidence(...)` is the single production static workflow traversal:

```text
one WorkflowDefinition
→ one job/step walk
→ analyze_run_step_commands(...) once per RunStepDefinition
→ same StaticCommandAnalysis reused for:
     direct requirements
     project environment
     package invocation
```

This is the concrete implementation of A1.

### Compatibility/test wrapper retained deliberately

`derive_project_environment_consumptions(...)` was not deleted blindly. Existing R6 integration tests and focused dependency→CI transfer tests still benefit from a standalone entry seam.

Instead, it became a thin wrapper over the same internal collector. It no longer owns a second implementation or production traversal.

This distinction is useful for later learning:

```text
multiple callable entry points
!=
multiple implementations / multiple semantic authorities
```

### Focused architecture regression

Added:

`tests/test_single_pass_workflow_static_evidence.py`

The key regression patches the CI-owned `analyze_run_step_commands` function and asserts one call for one project-selection run step while real project-environment consumption is derived. It protects the single-analysis architecture rather than an incidental helper implementation.

### B4 audit result

The commit touched only the unified static collector, coverage handoff, investigation orchestration, and the single-pass regression. Runtime-strengthening semantics were not changed.

Hosted checks still did not exist for the commit.

---

# B5 — remove obsolete ordinal compatibility and audit migration residue

**State:** IMPLEMENTED on `main`; executable proof still pending.

Commit:

```text
5d783df4e8ab899178df1597e3554d8c39d42509
refactor: remove legacy static command ordinals
```

### Why B5 was necessary

After B4, the production architecture was correct, but transitional fields/checks still allowed the repository to express both old and new identity models. Leaving that scaffolding would make the later learning session teach a migration state rather than the intended architecture and would violate A3 / plan §6.10.

B5 therefore removed the obsolete ordinal model rather than treating `None` values as permanent design.

Removed from active contracts:

```text
DirectInstallDeclarationObservation.matched_segment_index
ProjectEnvironmentSelectionDeclaration.segment_index
StaticDependencyConsumptionEvidence.segment_index
DirectPackageInvocationEvidence.segment_index
legacy same-step segment ordering
legacy project-environment shell-segment validation
```

Same-step CI ordering is now canonical-location-only:

```text
step_source_index
+ StaticCommandLocation.source_order
+ structural_context
→ ordered_after | not_after | unresolved
```

If canonical inner-command identity is absent for same-step comparison, the result is unresolved rather than guessed.

### Precomposed project-environment test seam retained but strengthened

Focused tests may still inject a precomposed `StaticDependencyConsumptionEvidence` so lower composition behavior can be tested without rebuilding upstream dependency semantics every time.

That seam no longer accepts a legacy segment ordinal. It must preserve canonical parsed command identity and structure, and CI validates that identity against the exact parsed run-step occurrence.

This keeps test layering without keeping obsolete architecture.

### Tests were changed to prove the positive architecture

Tests stopped asserting things like:

```text
segment_index is None
matched_segment_index is None
```

because those assertions preserve knowledge of a deleted design.

They now assert the actual contract:

```text
canonical command location exists when earned
source_order is correct
missing same-step canonical identity is unresolved
project-environment injected evidence matches exact parsed occurrence
```

Dependency-domain membership/reachability unit fixtures simply stopped supplying an ordinal because those tests do not own CI source identity.

### Regression found during B5 audit

`tests/test_uv_package_scope.py` still called `observe_project_environment_selection(...)` using its pre-B3 API and did not supply `command_analysis`.

This stale test was discovered because B5 deliberately audited manual constructors/callers rather than only deleting fields from source. The test was repaired with a parser-neutral `StaticCommandAnalysis` fixture and now also asserts that the resulting declaration has canonical command location.

This was a real migration residue; it is part of the learning record, not noise.

### Atomic Git-object failure and recovery

The first B5 atomic tree attempt failed before moving `main` because one prepared unreferenced blob SHA was no longer a valid Git blob:

```text
tree.sha ... is not a valid blob
HTTP 422
```

Important consequence:

```text
main remained at 069e61c2...
no partial source/test update was published
```

The correction was to validate the prepared blob objects against their intended files, recreate the missing/stale objects, rebuild the tree from the unchanged base tree, create one commit, and fast-forward `main` only after the complete tree existed.

The successful final atomic tree changed 15 files: five production modules and ten focused/nearby tests.

### B5 post-commit audit

`069e61c2... → 5d783df4...` is exactly one commit and only the expected cleanup/test files changed. No Cycle-3 runtime policy, target evidence, maintainer-action logic, or unrelated product responsibility was modified.

---

# Final Phase-B implementation shape

After B1–B5, the static command consumer architecture is:

```text
exact GitHub Actions WorkflowDefinition
        ↓
one CI-owned workflow traversal
        ↓
for each RunStepDefinition:
    analyze_run_step_commands(...) exactly once
        ↓
    StaticCommandAnalysis
      + StaticCommandOccurrence
      + StaticCommandLocation
      + structural_context
        ↓
    ┌───────────────────────────────┬──────────────────────────────┬──────────────────────────┐
    │                               │                              │
    ▼                               ▼                              ▼
direct requirements          project environment            package invocation
(dependency semantics)       (dependency semantics)         (CI semantics)
    │                               │                              │
    └────────────── canonical static occurrence identity ─────────┘
                                    ↓
                        CI bounded static ordering
                                    ↓
                     ordered_after / not_after / unresolved
```

Ownership after migration:

```text
GitHub/provider
→ shell context + syntax parsing + parser-neutral command IR/identity

dependency
→ pip requirements meaning + local project/extra/group/uv selection + reachability/membership

CI
→ one workflow traversal + checkout provenance + changed-package invocation
  + cross-evidence composition + static ordering

Cycle 3 (not started)
→ runtime-strengthening eligibility and final static↔runtime correction
```

No Tree-sitter node is exposed as a dependency/CI contract. No migrated consumer reconstructs shell command identity through regex/text splitting as positive fallback.

---

# Executable proof status and exact blockage

Phase B implementation is complete, but Phase B remains formally open because executable proof has not yet been obtained.

Evidence currently available:

```text
B1–B5 source committed
+ actual commit/diff audits through GitHub connector
+ focused/nearby proof assets written/reconciled
+ B4 single-pass architectural regression written
+ final B5 migration-residue audit performed
!= focused tests executed against final 5d783df4...
!= nearby suites executed against final 5d783df4...
!= full deterministic suite executed against final 5d783df4...
```

### Hosted proof attempt

For final commit:

```text
5d783df4e8ab899178df1597e3554d8c39d42509
```

GitHub combined status currently has no statuses/checks.

Repository workflow:

`.github/workflows/product-verification.yml`

is intentionally:

```yaml
on:
  workflow_dispatch:
```

and its own comment states that enabling push/PR checks is a separate decision after a hosted run is reviewed.

The available GitHub connector exposes workflow reads and reruns of existing jobs/runs, but no action to initiate a new `workflow_dispatch` run. Changing the workflow trigger merely to manufacture proof would be a separate CI-policy responsibility and is outside this Build slice.

### Local exact-SHA execution attempt

A read-only clone was attempted solely for test execution at the exact final commit. The runtime failed before repository acquisition with:

```text
fatal: unable to access 'https://github.com/motafegh/UpgradePilot.git/':
Could not resolve host: github.com
```

This is an execution-environment/network limitation, not evidence that the product tests failed.

Do not report Phase-B tests as passing until a real execution environment runs them.

---

# Phase-B integrated learning map for the later Learning-by-Doing session

When executable proof closes B, use the final source/tests plus this record to learn the implementation in this order rather than by commit chronology alone:

### 1. Why source identity had to change

Follow:

```text
old segment_index overload
→ identity + ordering + placeholder roles
→ StaticCommandLocation
→ explicit CI ordering relation
```

Primary files:

```text
src/upgradepilot/github/workflow_command_location.py
src/upgradepilot/ci/static_command_order.py
```

### 2. Provider IR versus dependency semantics

Follow one real `pip install -r ...` and one real `uv sync ...` from:

```text
workflow definition
→ StaticCommandAnalysis / atoms
→ dependency observer
→ domain evidence
```

Primary files:

```text
src/upgradepilot/github/workflow_command_analysis.py
src/upgradepilot/dependency/pip_command.py
src/upgradepilot/dependency/direct_install.py
src/upgradepilot/dependency/environment_selection.py
```

### 3. Static presence versus execution-path meaning

Use clean linear commands and short-circuit/conditional examples to understand why:

```text
real parsed command exists
```

can be positive static evidence while:

```text
invocation definitely happened after consumption
```

remains unresolved.

Primary proof files:

```text
tests/test_static_command_order.py
tests/test_ci_static_direct_exercise_order.py
tests/test_github_workflow_command_analysis.py
```

### 4. One-analysis handoff and cross-layer composition

Trace the final production seam:

```text
investigation.py
→ WorkflowDependencyCoverageInput(project_environment_sources=...)
→ inspect_workflow_dependency_evidence(...)
→ one RunStepDefinition analysis
→ all three consumers
```

Primary files:

```text
src/upgradepilot/investigation.py
src/upgradepilot/ci/dependency_exercise.py
src/upgradepilot/ci/workflow_commands.py
tests/test_single_pass_workflow_static_evidence.py
```

### 5. Project-environment evidence composition

Use S001-style uv and S011-style pyproject examples to distinguish:

```text
visible project selection
→ dependency-domain membership/reachability
→ CI consumption evidence
```

without turning it into execution or installed-version proof.

Primary proof files:

```text
tests/test_project_environment_selection.py
tests/test_uv_selected_root_reachability.py
tests/test_project_source_environment_membership.py
tests/test_r6_project_environment_workflow_integration.py
tests/test_r6_project_source_workflow_integration.py
```

### 6. Why compatibility scaffolding was removed

Review B5 and compare the final dataclasses/tests against the transitional B2/B3 state. The learning point is not “delete old fields”; it is:

```text
migration scaffold can be useful temporarily
but it must not become accidental permanent architecture
```

### 7. Proof discipline

Use the current blocked proof as a concrete example of:

```text
source inspection + tests written
!= tests executed
```

and why environment/tooling failure must be recorded separately from product failure.

---

# Current route / exact next action

Do not start Cycle 3 and do not yet perform the full integrated implementation-learning session.

Next required step:

```text
obtain executable Phase-B proof on final commit 5d783df4...
```

Preferred proof progression, consistent with the accepted plan:

```text
focused parser/dependency/CI suites
→ nearest R6/investigation/runtime-correlation suites
→ full deterministic repository suite
```

The existing `Product verification` workflow already installs the package in a fresh Python 3.12 environment, runs `pip check`, verifies CLI entry points, runs focused investigation composition, and then runs the full deterministic `unittest` suite. A manual dispatch against the final revision is therefore the cleanest currently-defined hosted proof route when dispatch is available.

Once executable proof is green:

1. record exact commands/run URL/counts and any repair if needed;
2. close Phase B and reconcile formal state preservation;
3. perform Ali's requested integrated implementation-learning session over the final B1–B5 architecture using the map above;
4. repair any ownership gap exposed by that learning check;
5. only then enter Cycle 3 runtime-strengthening work.

If executable proof fails, diagnose the exact failing responsibility; do not start learning from or advance beyond a knowingly unstable final implementation.

---

# Stop line

Until Phase B executable proof closes:

- do not change Cycle 3 runtime-strengthening eligibility;
- do not treat static source order as execution proof;
- do not broaden pip/uv/package-wrapper semantics;
- do not reintroduce textual shell splitting as a positive-evidence fallback;
- do not introduce general control-flow simulation;
- do not change CI trigger policy merely to manufacture proof without separate authorization;
- do not absorb runtime logs/artifacts, matrix/reusable-workflow execution, Python/custom-interpreter analysis, Target redesign, exact installed-version/wheel evidence, or maintainer-action enablement.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
