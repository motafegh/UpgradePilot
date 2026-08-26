# UpgradePilot Current Memory

**Last updated:** 2026-08-26  
**Authority:** sole owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Controlling engineering rule

Existing implementation is evidence to inspect, not authority to preserve.

```text
current use / tests / comments / historical design
!= retention justification

trace admitted responsibility / proof need / material risk / real compatibility obligation
→ locate earliest sufficient owner
→ keep the smallest adequate mechanism
→ otherwise move, narrow, or remove
```

For cross-layer mechanisms, trace normal producer → integration/orchestration → consumer before deciding local ownership. Direct callability, historical fixtures, or diagnostic convenience are not retention authority unless the alternate route is an explicitly supported product boundary.

Canonical governance owners: `AGENTS.md`, `OPERATING_GUIDE.md` §4.1–4.2, and `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md` (`JUST-001` through `JUST-005`).

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Current plan:** `plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`.
- **Plan position:** **R0 COMPLETE; R1 COMPLETE; R2 COMPLETE; R3 IMPLEMENTED / FINAL ACCEPTANCE PENDING LOCAL R7.9; R4 IMPLEMENTED / FINAL ACCEPTANCE PENDING LOCAL R7.9; R5 IMPLEMENTED / FINAL ACCEPTANCE PENDING LOCAL R7.9; R6 IMPLEMENTED / FINAL ACCEPTANCE PENDING LOCAL R7.9; R7 ACTIVE — R7.0 COMPLETE; R7.1 COMPLETE; R7.2 REMOTE ORCHESTRATION TRACE COMPLETE; R7.3 REMOTE REAL-CASE PRESSURE COMPLETE; R7.4 COMPLETE; R7.5 COMPLETE LOCALLY; R7.6 COMPLETE LOCALLY; R7.7 COMPLETE; R7.8 COMPLETE; R7.9 NEXT**.
- **R1 static closure record:** `working-memory/2026-08-23_B2-R1-static-closure-audit.md`.
- **R1 Gate-A/reconciliation record:** `working-memory/2026-08-23_B2-R1-gate-a-runtime-and-main-reconciliation.md`.
- **R1 completion record:** `working-memory/2026-08-24_B2-R1-completion-and-main-acceptance.md`.
- **R2 initial structural-owner record:** `working-memory/2026-08-24_B2-R2-uv-lock-structural-model-initial-slice.md`.
- **R2 acceptance/promotion record:** `working-memory/2026-08-25_B2-R2-runtime-acceptance-and-main-promotion.md`.
- **R3 implementation record:** `working-memory/2026-08-25_B2-R3-uv-package-scope-implementation.md`.
- **R4 implementation record:** `working-memory/2026-08-25_B2-R4-selected-root-reachability-implementation.md`.
- **R5 implementation record:** `working-memory/2026-08-25_B2-R5-ci-consumption-reachability-rebind.md`.
- **R6 implementation record:** `working-memory/2026-08-25_B2-R6-real-workflow-reachability-integration.md`.
- **R6 proof-preservation correction:** `working-memory/2026-08-25_B2-R6-unresolved-selection-proof-preservation-fix.md`.
- **R7 progressive acceptance record:** `working-memory/2026-08-26_B2-R7-acceptance-cleanup-and-baseline-closure.md`.
- **R7 findings register:** `working-memory/2026-08-26_B2-R7-findings-register.md`.
- **R7.4 retention disposition record:** `working-memory/2026-08-26_B2-R7-R7.4-architecture-naming-retention-disposition.md`.
- **R7.7 audit lifecycle reconciliation record:** `working-memory/2026-08-26_B2-R7-R7.7-audit-lifecycle-reconciliation.md`.
- **R7.8 executable candidate / validation freeze record:** `working-memory/2026-08-26_B2-R7-R7.8-executable-candidate-and-validation-bundle-freeze.md`.
- **Learning-by-Building loop reinforcement record:** `working-memory/2026-08-24_LEARNING_BY_BUILDING_LOOP_REINFORCEMENT.md`.
- **R7 entry revision:** `fa12852598a8f687eac6827a296b87c66b7f932f` — R7 plan-refinement HEAD when R7 was first selected.
- **Frozen R7 executable candidate:** `b50e4b1a656625c3215dd3fbf08c28012c6d18aa` (tree `6fa6c6dfe9135990bb56eb786ecb7299ea99ac30`). Later R7.6–R7.8 commits are audit/memory/lifecycle records only; R7.8 direct comparison confirmed no later change under `src/`, `tests/`, or the retained S001 verifier.
- **R7 execution mode override before R7.5:** Ali explicitly superseded the earlier remote-first-through-R7.8 route. R7.0–R7.4 remain completed remote-depth evidence and are not reopened. Starting from exact local `main` revision `0ce34f153925a45fdb2ad50385faf69e751ce6de`, R7.5 onward proceeds locally in bounded clusters with focused tests run progressively; R7.9 remains the final broad deterministic acceptance gate rather than the first local execution point.
- **R7.1 result:** **PASS TO REMOTE SOURCE/TEST-REVIEW DEPTH.** Current R3–R6 source and focused tests coherently represent the required selector/scope, reachability, consumption, workflow derivation, multiple-match, unresolved-preservation, S011, S005, workspace, and conditional proof boundaries. No R7.1 source/test repair was required. Runtime remains pending R7.9.
- **R7.2 result:** **NORMAL PRODUCT ROUTE ESTABLISHED TO REMOTE SOURCE/ORCHESTRATION-TRACE DEPTH.** Provider code enforces exact PR-head workflow admission before R3/R4/R5; normal `investigation.py` derives project-environment consumptions itself, calls `evaluate_dependency_ci_coverage(...)`, preserves all underlying consumption evidence, and exposes `ci_coverage_result` to the CLI/application. The legacy evaluator is not on the ordinary product route. No executable repair was performed in R7.2; runtime remains pending R7.9.
- **R7.3 result:** **REAL-CASE GITHUB EVIDENCE PRESSURE COMPLETE TO REMOTE DEPTH.** Pydantic S001 still provides the intended standalone `uv sync --all-packages --group docs` command and exact lock witness `docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve 2.8.4`. S011 and S005 retain their distinct non-direct-uv boundary roles. R7.3 discovered `F-004`, a real workflow checkout-provenance false-support path, and therefore interrupted sampling for an immediate bounded repair.
- **F-004 repair:** R6 now guards repository-relative project-environment and direct-requirements/direct-invocation evidence with per-job workspace-root checkout provenance. Explicit current-repository root checkout permits changed-repository binding; explicit other-repository root checkout prevents rebinding; unresolved/not-established checkout provenance is preserved as unresolved rather than guessed. Primary production corrections: `d14bb6d70c9bc34d0116d7c3abd56ea7bab9d6f5` and `e320ad64403360ff8b5c9c5a5e55e3c096bfee5a`. Local R7.5 regression evidence now protects the repair; final executable acceptance remains pending R7.9.
- **R7.4 result:** **ARCHITECTURE/NAMING/RETENTION REVIEW COMPLETE TO REMOTE DEPTH.** The normal coverage owners are retained; the legacy CI evaluator/helper/alias/direct-requirements compatibility projection are selected for removal in R7.5; the current coverage input/consumption names are selected for bounded narrowing; the obsolete public uv selected-environment membership API is selected for retirement after unique current-proof test migration; and the private reachability mechanics still used by R4 are selected to move into `uv_reachability.py`. No product source/test change was made by R7.4.
- **R7.5 F-002 result:** **COMPLETE TO LOCAL FOCUSED/NEAREST-INTEGRATION DEPTH at `3f12283574c1e80ba92a1683ff575420dc9463ba`.** R6 now uses typed unavailable project-root evidence to locate a relevant static selector, then preserves `required_project_root_source_unavailable` as unresolved before R4/R5. The new regression first failed with `0 != 1`, then passed after the repair. Four focused module runs executed **39 tests / OK** across the F-002 route, normal investigation, coverage, S001, S011, S005, workflow parsing, and F-004 checkout provenance. Targeted `compileall` and `git diff --check` passed. Ruff was not executed because `.venv/bin/ruff` is absent. Full deterministic acceptance remains pending later R7.
- **R7.5 F-003 result:** **COMPLETE LOCALLY at executable/test revision `0ff7b5d8613d521950e2b45006800f269b8597b3`.** The obsolete CI exercise evaluator/result types, combined workflow-command helper/evidence, investigation alias, and direct-requirements compatibility projection/result field were removed. The retained current input is now `WorkflowDependencyCoverageInput`, and `project_environment_consumptions` plus matching diagnostics replace broad `external_consumptions` language. Five still-current legacy proof cases moved to coverage tests; two legacy-only test modules were removed. Focused/nearest suites executed **68 tests / OK**; complete standard discovery executed **529 tests / OK**; `compileall src tests` and `git diff --check` passed.
- **R7.5 F-005 result:** **COMPLETE LOCALLY at executable/test revision `b50e4b1a656625c3215dd3fbf08c28012c6d18aa`.** Reachability-specific lock projection, edge resolution, and traversal support now live in `uv_reachability.py`; the obsolete public `uv_membership.py` API and its legacy-only tests were removed after unique current R4 cases migrated. Uv-focused tests executed **43 tests / OK**, nearest CI/integration/topology tests executed **27 tests / OK**, complete standard discovery executed **515 tests / OK**, and `compileall src tests` plus `git diff --check` passed.
- **R7.5 finding closure:** `F-001` is **ACCEPTED AS A KNOWN BOUNDED LIMITATION** because it only conservatively under-reports, no admitted real workflow currently requires mixed safe+unresolved segment preservation, and a segment-level contract lacks a present product trigger. `F-002`, `F-003`, and `F-005` are complete to their recorded local proof depths. `F-004` remains repaired; the post-cleanup source/diff re-audit found no checkout-state bypass and its five discriminating provenance tests passed at the F-005 candidate. Final executable acceptance remains pending R7.9.
- **R7.6 result:** **PASS LOCALLY AT READ-ONLY SOURCE/DIFF + FOCUSED PROOF-BOUNDARY DEPTH** against executable candidate `b50e4b1a656625c3215dd3fbf08c28012c6d18aa` (tree `6fa6c6dfe9135990bb56eb786ecb7299ea99ac30`). The complete R7.5 executable diff has no unexplained source/test change, stale live transitional symbol, proof strengthening, uncertainty erasure, or checkout-authority bypass. The normal investigation route remains independently integrated rather than established only by injected unit-test evidence. The focused R3–R6/R4/investigation audit bundle executed **40 tests / OK** and range `git diff --check` passed. No product source/test mutation was required.
- **R7.7 result:** **AUDIT LIFECYCLE RECONCILIATION COMPLETE.** AUDIT-001, AUDIT-006, and AUDIT-007 moved from active to absorbed because their material conclusions are now incorporated into stronger accepted owners and completed R1–R7 work; AUDIT-004 remains deferred; AUDIT-005 remains scheduled behind successful R7.9/R7.10 acceptance; AUDIT-002/003 remain absorbed. No executable blocker or product source/test change was introduced.
- **R7.8 result:** **EXECUTABLE CANDIDATE + FINAL VALIDATION BUNDLE FROZEN.** The exact executable candidate remains `b50e4b1a656625c3215dd3fbf08c28012c6d18aa`. The R7-entry→candidate source/test change surface, final finding/retention dispositions, real S001/S011/S005 pressure, proof boundaries, exact focused R3→R6 bundle, complete standard suite, compile/diff checks, and live S001 normal-path verifier procedure are recorded in the R7.8 working-memory record. No new executable work was required.
- **Current bounded continuation:** execute **R7.9 final local validation** in the normal WSL project checkout against synchronized current `main`, first proving `src/` + `tests/` + retained S001 verifier are identical to frozen executable candidate `b50e4b1...`. Record exact checkout HEAD, tracked/untracked status, interpreter, commands, counts, and PASS/FAIL. Do not patch a failure only locally.
- **Runtime claim boundary:** the earlier R7.0–R7.4 remote reviews remain non-runtime evidence. From R7.5 onward, record only the exact focused/local checks actually run for each cluster; no cluster-level pass substitutes for the final focused + integration + full deterministic R7.9 acceptance gate.
- Learning-by-Doing-and-Building remains the normal execution loop, applied proportionately: brief orientation → real bounded work → actual evidence → material state preservation → concise post-action learning/ownership closure → next bounded slice.
- Dedicated B2 mastery learning package remains paused while this reconciliation plan is active.
- Previous dependency-environment/CI plan remains deferred at completed Cluster 5; do not start old Cluster 6.
- **AUDIT-005 / product AI-agentic orchestration remains SCHEDULED.** It activates only after final R7.9 local deterministic acceptance succeeds and R7.10 freezes the accepted baseline.

## R7 acceptance state after local-continuation override

```text
R7.0 exact state re-anchor                                  COMPLETE
R7.1 remote focused R3–R6 source/test contract audit       COMPLETE
R7.2 remote normal investigation/CI orchestration trace     COMPLETE
R7.3 remote real-case GitHub evidence pressure              COMPLETE TO REMOTE EVIDENCE DEPTH
R7.4 architecture/naming/retention review                   COMPLETE TO REMOTE DEPTH
R7.5 bounded local cleanup/finding disposition fixes        COMPLETE LOCALLY
R7.6 local post-cleanup source/diff + proof audit           COMPLETE LOCALLY
R7.7 audit lifecycle reconciliation                        COMPLETE
R7.8 final local executable candidate + validation bundle   COMPLETE
R7.9 final broad local executable validation                NEXT
R7.10 accepted baseline + mandatory handoff                 NOT STARTED
```

Revision semantics:

```text
R7 ENTRY REVISION
→ exact HEAD when R7 began

EXECUTABLE CANDIDATE REVISION
→ final code/test SHA after all local R7 cleanup/review
→ not broadly accepted until R7.9

ACCEPTED EXECUTABLE REVISION
→ exact executable candidate SHA after R7.9 local validation passes

CLOSURE REVISION
→ possible later audit/memory/docs-only SHA
→ not newly execution-tested
```

The post-R6 proof-preservation correction remains part of the pending executable candidate:

```text
R3 not_observed
→ no project-environment evidence

R3 unresolved
→ unresolved StaticDependencyConsumptionEvidence
→ preserve workflow/job/step/command + dependency-source identity
→ do not invoke R4/project-source membership/R5 positive-or-negative composition

R3 observed
→ existing R3 → dependency-domain relation → R5 flow
```

The focused regression uses:

```yaml
- run: uv sync --group "${{ matrix.group }}"
```

and protects by source/test intent:

```text
R3 unresolved
→ unresolved CI consumption
→ unresolved coverage consumption state

NOT
→ evidence disappearance
→ static_dependency_consumption_not_observed / not_established
```

## R1 accepted runtime authority

Accepted executable commit:

```text
9fb19dd483f568a459a0680527a8b00683334359
```

Local environment:

```text
Python 3.12.3
/home/motafeq/projects/UpgradePilot/.venv/bin/python
```

Gate A before main reconciliation:

```text
structural contract assertions               PASS
focused R1 regression suite                  272 tests / OK
experiment suite                              27 tests / OK
compileall src/tests/tools/experiments       PASS
complete standard suite                      502 tests / OK
```

Gate B after current `main` was merged into the same R1 branch:

```text
complete standard suite                      502 tests / OK
experiment suite                              27 tests / OK
```

`main` was then fast-forwarded non-destructively to the exact Gate-B-tested commit `9fb19dd483f568a459a0680527a8b00683334359`. At promotion time GitHub reported `main` and `agent/r1-exact-file-contract-migration` identical.

Any later commits that only record R1 completion/live state are documentation-only and do not supersede the executable acceptance SHA.

The old pre-fix result:

```text
507 tests
FAILED (failures=5, errors=51)
```

is historical migration-pressure evidence only and is fully superseded by the accepted R1 runtime results above.

## R1 accepted exact-file ownership

Successful exact repository text:

```text
RepositoryTextFile
├── repository
├── path
├── revision
└── content
```

Typed unavailability:

```text
UnavailableRepositoryFile
├── repository
├── path
├── revision
├── reason
└── detail
```

Not retained as durable exact-file evidence:

```text
returned_path
reported_byte_count
decoded_byte_count
blob_sha
retrieved_at
```

Important distinction:

```text
retired as durable evidence field
!= forbidden as provider-local validation state
```

The GitHub provider still validates returned-path equality, regular-file type, supported/strict base64, actual encoded/decoded bounds, UTF-8, and exact repository/path/revision identity before constructing successful evidence.

## Current ownership map retained for later work

```text
GitHubRepositoryClient
→ external acquisition truth + provider admission

RepositoryTextFile / UnavailableRepositoryFile
→ intrinsic exact locator/content state

dependency/analysis.py
→ PR source admission + exact base/head orchestration + source-context rebinding

environment_selection.py
→ static project selector observation + bounded command package-scope preservation

uv_lock_structure.py
→ shared bounded uv.lock schema/core package-record structural admission

uv_lock.py / pyproject.py
→ source-format transition semantics after admitted source structure

uv_reachability.py
→ R4 public contract and implementation owner for scope-calibrated explicit selected-root lock reachability, including the reachability-specific lock projection and edge-resolution mechanics moved here during R7.5

ci/consumption.py
→ compose dependency-owned project-source membership or uv selected-root reachability into static CI dependency-consumption evidence; does not own dependency semantics, direct exercise, or runtime authority

ci/workflow_commands.py
→ R6 production seam over an exact admitted workflow: iterate readable local steps in source order; maintain bounded changed-repository workspace-root checkout provenance; only bind repository-relative commands to changed-repository dependency evidence when that provenance is sound; invoke R3 selection and the appropriate dependency-domain relation (R4 uv reachability or project-source membership); retain every R5 consumption result; preserve unresolved selection/provenance instead of strengthening it

ci/dependency_exercise.py
→ aggregate exact-head runtime authority + static dependency-consumption evidence into coverage while preserving consumption/direct-exercise/runtime separation; current coverage responsibility retained after R7.5 legacy evaluator/type removal and input naming narrowing

target/artifact_environment.py
→ bounded Target workflow semantics + minimal source provenance

target/python.py
→ exact pyproject.toml requires-python semantics

upstream tagged-changelog chain
→ exact immutable source + bounded semantic source window

investigation.py
→ cross-object application sequencing and exact PR/target identity binding; R6 acquires exact project/lock source bundles and routes normal PR CI through coverage-oriented R3→R4/project-source→R5 composition; provider-admitted exact PR-head workflows precede those semantics; R7.5 removed the transitional CI alias/direct-requirements projection selected by R7.4

CLI / tests / tools
→ consume current product contracts; CLI reads `ci_coverage_result`; tests/tools do not enlarge evidence contracts for convenience
```

Final reduced dependency source provenance:

```text
DependencyChangeSourceEvidence
├── path
├── file_format
└── extraction_method
```

Final Target Python evidence:

```text
TargetPythonDeclaration
├── path
├── revision
└── requires_python
```

Final tagged changelog evidence:

```text
TaggedChangelogEvidence
├── repository
├── interval
├── resolved_commit_sha
├── path
└── content
```

## Stable proof guards

```text
dependency transition
!= explicit selected-root reachability evidence
!= project-source environment membership evidence
!= static environment selection
!= static dependency consumption
!= resolver satisfiability/currentness
!= runtime execution/success
!= exact-version witness
!= direct package exercise
!= behavioral compatibility/safety/action
```

and:

```text
observation != interpretation != evidence quality != decision
```

remain controlling.

## R2 accepted uv.lock structural ownership

R2 introduced one bounded uv-specific structural lock owner and has accepted runtime evidence. Detailed acceptance remains in `working-memory/2026-08-25_B2-R2-runtime-acceptance-and-main-promotion.md`.

## R3 package-scope reconciliation

R3 preserves `bound_project` versus `all_workspace_packages`, explicit selectors, and unresolved unsupported/dynamic scope. Current verification status:

```text
static producer→consumer responsibility review    PASS to prior depth
R7.1 remote source/test contract audit            PASS
R7.2 normal-path producer/orchestration trace     PASS to remote trace depth
R7.3 S001 real-case source pressure               PASS TO REMOTE EVIDENCE DEPTH
focused runtime tests                             PENDING R7.9
complete standard suite                           PENDING R7.9
compileall src/tests                              PENDING R7.9 as required
```

## R4 selected-root reachability reconciliation

Preferred contract remains `evaluate_uv_selected_root_reachability(...) → UvSelectedRootReachability`. Current verification status:

```text
source contract / focused tests                  IMPLEMENTED
post-write connector source inspection           PASS to static review depth
R7.1 remote source/test contract audit            PASS
R7.2 normal-path orchestration trace               PASS to remote trace depth
R7.3 S001 docs→SoupSieve source pressure          PASS TO REMOTE EVIDENCE DEPTH
R7.4 legacy uv membership/helper ownership         COMPLETE — CURRENT MECHANICS MOVED / LEGACY PUBLIC SURFACE REMOVED IN R7.5
local focused runtime                            PENDING R7.9
complete standard suite                          PENDING R7.9
compileall                                       PENDING R7.9 as required
```

## R5 CI-consumption reachability rebind

R5 maps `ProjectSourceEnvironmentMembership | UvSelectedRootReachability` into `StaticDependencyConsumptionEvidence` without strengthening proof. Current verification status:

```text
source/consumer ownership trace                  COMPLETE
explicit uv vs project-source mapping            IMPLEMENTED
conditional/non-workspace proof guards            IMPLEMENTED
post-write source inspection                     PASS to static review depth
R7.1 remote source/test contract audit            PASS
R7.2 normal-path orchestration trace               PASS to remote trace depth
R7.3 real-case source pressure                     PASS TO REMOTE EVIDENCE DEPTH
local focused/runtime integration                PENDING R7.9
complete standard suite                          PENDING R7.9
compileall                                       PENDING R7.9 as required
```

## R6 real-workflow reachability integration

Normal R6 production seam remains:

```text
exact admitted PR-head workflow definition
→ ci/workflow_commands.py
→ source-ordered workflow steps
→ bounded workspace-root checkout provenance
→ every readable local run step
→ R3
→ R4 uv reachability OR project-source membership
→ R5 consumption
→ preserve all evidence
→ CI coverage
```

The normal `investigation.py` path is migrated; S001/S011/S005/workspace/unresolved-preservation regressions are implemented. R7.3 additionally repaired checkout/repository provenance for both project-environment and direct-requirements/direct-invocation evidence. Current verification status:

```text
production ownership/orchestration trace                 COMPLETE
workflow-derived R3→R4/R5 production seam               IMPLEMENTED
normal investigation migration                           IMPLEMENTED
all supported matching consumption preservation          IMPLEMENTED
PR-head workflow admission boundary                      PROVIDER-ENFORCED / R7.2 CONFIRMED
S001/S011/S005/workspace regressions                      IMPLEMENTED
R3 unresolved-selection preservation                     IMPLEMENTED
checkout/repository provenance guard                      IMPLEMENTED REMOTELY IN R7.3
R7.1 remote source/test contract audit                   PASS
R7.2 normal-path remote trace                             PASS TO REMOTE SOURCE/ORCHESTRATION-TRACE DEPTH
R7.3 real-case GitHub evidence pressure                   COMPLETE TO REMOTE EVIDENCE DEPTH
F-004 source/test-review repair                           COMPLETE REMOTELY / RUNTIME PENDING
local executable validation                              PENDING R7.9
```

No R3/R4/R5/R6/F-004 final R7 runtime acceptance is claimed before R7.9.

## Learning state to retain

```text
current code uses X != product requires X
provider returns X != durable evidence needs X
construction invariant != external-provider truth
provenance != transport metadata
valid object != valid relationship
real proposition != local ownership
orchestration context != semantic input
controlled composition != independent evidence-branch composition
test fixture mismatch != reason to restore deleted production fields
diagnostic convenience != evidence-retention requirement
test suite responsibility != duplicate every lower-layer mechanism
resource protection should bind actual processed data, not merely provider-reported metadata
retired durable field != forbidden provider-local variable
runtime green != proof of every later compatibility/safety proposition
Git history divergence != content conflict
same commit SHA under two refs = same executable tree
closure documentation != new executable authority
shared structural parsing != shared semantic interpretation
one external format != permission to build a generic package-manager abstraction
pre-action orientation != post-action learning closure
pending local validation != reason to defer learning closure for already-established work
file-level dependency transition != PR-wide trusted dependency transition
lock structural truth != dependency-transition truth != selected-root reachability truth
positive reachability witness requires one sound path != not_established requires complete claimed scope exhaustion
preserved command scope != complete command/environment interpretation
selected-root reachability != complete selected-environment membership
pyproject source evidence != automatically required input to lock-backed reachability
project-root/lock-source binding != project/lock currentness proof
conditional candidate path != supported static consumption
uv reachability source = uv.lock != project-source membership source = pyproject.toml
static dependency consumption != static direct exercise != runtime authority
changed package != hardcoded relevant CI group
one changed package may have zero, one, or multiple supported CI selection commands
PR workflow admission happens before command/dependency semantics
workflow command visible in changed-repository workflow != command operates on changed repository checkout
repository-relative command + changed-repository dependency evidence requires compatible checkout provenance
aggregate existential support != discard other supported matching commands
summary representative item != erase underlying evidence collection
R3 unresolved != absent evidence != not_established
required exact source unavailable != evidence absent != not_established
normal-path migration != legacy-surface retention justification
legacy public API absent from production route != private implementation mechanics are unused
remote source/test/orchestration review != runtime PASS
final broad local validation should validate the frozen executable candidate, not be conflated with narrower progressive checks
accepted executable revision != later documentation-only closure revision
live external verification != deterministic baseline
historical audit mentions a future question != audit must remain active
absorbed audit != future trigger can never create a new review
current main HEAD may be newer than the executable candidate when later commits change only audit/memory/docs
current-main validation can establish the frozen candidate only after executable/test/verifier identity to that candidate is proven
```
