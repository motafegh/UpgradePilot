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
- **Plan position:** **R0 COMPLETE; R1 COMPLETE; R2 COMPLETE; R3 IMPLEMENTED / RUNTIME ACCEPTANCE PENDING FINAL R7 LOCAL GATE; R4 IMPLEMENTED TO STATIC/SOURCE-REVIEW DEPTH / RUNTIME ACCEPTANCE PENDING FINAL R7 LOCAL GATE; R5 IMPLEMENTED TO STATIC/SOURCE-REVIEW DEPTH / RUNTIME ACCEPTANCE PENDING FINAL R7 LOCAL GATE; R6 IMPLEMENTED TO STATIC/SOURCE-REVIEW DEPTH / RUNTIME ACCEPTANCE PENDING FINAL R7 LOCAL GATE; R7 ACTIVE — R7.0 COMPLETE; R7.1 REMOTE SOURCE/TEST AUDIT COMPLETE; R7.2 NEXT**.
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
- **Learning-by-Building loop reinforcement record:** `working-memory/2026-08-24_LEARNING_BY_BUILDING_LOOP_REINFORCEMENT.md`.
- **R7 entry revision:** `fa12852598a8f687eac6827a296b87c66b7f932f` — R7 plan-refinement HEAD when R7 was first selected.
- **Remote-first R7 execution mode:** GitHub-only work through R7.8. Local checkout/testing is deferred to **R7.9**, after all remote review/cleanup is complete and one exact final remote candidate is frozen. Local execution is validation only; any failure returns to the smallest owning remote R7 slice for a GitHub-side repair and refreeze.
- **R7.1 result:** **PASS TO REMOTE SOURCE/TEST-REVIEW DEPTH.** Current R3–R6 source and focused tests coherently represent the required selector/scope, reachability, consumption, workflow derivation, multiple-match, unresolved-preservation, S011, S005, workspace, and conditional proof boundaries. No R7.1 source/test repair was required. Runtime remains pending R7.9.
- **R7.1 non-blocking review note:** step-scoped R3 uncertainty can conservatively suppress retained declarations when a hypothetical run step mixes one independently safe uv shell segment with another material unresolved segment. No current admitted R6 real case or selected requirement establishes the need to solve this now; it is conservative under-reporting, not false support. Revisit only if real evidence/product responsibility requires independent mixed-segment preservation.
- **Current bounded continuation:** execute **R7.2 remote normal investigation/CI orchestration trace** from current source/tests: exact PR/change → `investigation.py` → admitted exact-head workflows/source bundle → `derive_project_environment_consumptions(...)` → CI coverage → application/CLI result. Confirm this is the normal product route, not test-side composition; preserve PR-CI admission and all evidence items; identify whether any legacy path still participates in ordinary operation.
- **Runtime claim boundary:** no R3/R4/R5/R6 runtime PASS is claimed during R7.0–R7.8. Final local focused + integration + full deterministic validation is concentrated in R7.9 after the final remote candidate is frozen.
- Learning-by-Doing-and-Building remains the normal execution loop, applied proportionately: brief orientation → real bounded work → actual evidence → material state preservation → concise post-action learning/ownership closure → next bounded slice.
- Dedicated B2 mastery learning package remains paused while this reconciliation plan is active.
- Previous dependency-environment/CI plan remains deferred at completed Cluster 5; do not start old Cluster 6.
- **AUDIT-005 / product AI-agentic orchestration remains SCHEDULED.** It activates only after final R7.9 local deterministic acceptance succeeds and R7.10 freezes the accepted baseline.

## R7 remote-first acceptance state

```text
R7.0 exact state re-anchor                                  COMPLETE
R7.1 remote focused R3–R6 source/test contract audit       COMPLETE
R7.2 remote normal investigation/CI orchestration trace     NEXT / NOT STARTED
R7.3 remote real-case GitHub evidence pressure              NOT STARTED
R7.4 architecture/naming/retention review                   NOT STARTED
R7.5 bounded remote cleanup                                 NOT STARTED
R7.6 remote post-cleanup source/diff + proof audit          NOT STARTED
R7.7 audit lifecycle reconciliation                        NOT STARTED
R7.8 final remote candidate + local bundle freeze           NOT STARTED
R7.9 final local pull + executable validation               DEFERRED UNTIL R7.8
R7.10 accepted baseline + mandatory handoff                 NOT STARTED
```

Revision semantics:

```text
R7 ENTRY REVISION
→ exact HEAD when R7 began

REMOTE CANDIDATE REVISION
→ final code/test SHA after all remote R7 cleanup/review
→ not yet runtime accepted

ACCEPTED EXECUTABLE REVISION
→ exact remote candidate SHA after R7.9 local validation passes

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
→ preferred R4 public contract for scope-calibrated explicit selected-root lock reachability

uv_membership.py
→ legacy/transitional reachability implementation support + private projection helpers still reused by uv_reachability.py; no longer the CI consumption contract

ci/consumption.py
→ compose dependency-owned project-source membership or uv selected-root reachability into static CI dependency-consumption evidence; does not own dependency semantics, direct exercise, or runtime authority

ci/workflow_commands.py
→ R6 production seam over an exact admitted workflow: iterate every readable local run step, invoke R3 selection, invoke the appropriate dependency-domain relation (R4 uv reachability or project-source membership), and retain every R5 consumption result; does not choose a preferred command; material R3 `unresolved` is preserved as unresolved CI-consumption evidence rather than discarded

ci/dependency_exercise.py
→ aggregate exact-head runtime authority + static dependency-consumption evidence into coverage while preserving consumption/direct-exercise/runtime separation

target/artifact_environment.py
→ bounded Target workflow semantics + minimal source provenance

target/python.py
→ exact pyproject.toml requires-python semantics

upstream tagged-changelog chain
→ exact immutable source + bounded semantic source window

investigation.py
→ cross-object application sequencing and exact PR/target identity binding; R6 now acquires exact project/lock source bundles and routes normal PR CI through coverage-oriented R3→R4/R5 composition instead of the legacy direct-requirements exercise evaluator

CLI / tests / tools
→ consume current product contracts; they do not enlarge evidence contracts for convenience
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
local focused/runtime integration                PENDING R7.9
complete standard suite                          PENDING R7.9
compileall                                       PENDING R7.9 as required
```

## R6 real-workflow reachability integration

Normal R6 production seam remains:

```text
exact admitted PR-head workflow definition
→ ci/workflow_commands.py
→ every readable local run step
→ R3
→ R4 uv reachability OR project-source membership
→ R5 consumption
→ preserve all evidence
→ CI coverage
```

The normal `investigation.py` path is migrated; S001/S011/S005/workspace/unresolved-preservation regressions are implemented. Current verification status:

```text
production ownership/orchestration trace                 COMPLETE
workflow-derived R3→R4/R5 production seam               IMPLEMENTED
normal investigation migration                           IMPLEMENTED
all supported matching consumption preservation          IMPLEMENTED
PR-head workflow admission boundary                      PRESERVED
S001/S011/S005/workspace regressions                      IMPLEMENTED
R3 unresolved-selection preservation                     IMPLEMENTED
R7.1 remote source/test contract audit                   PASS
R7.2 normal-path remote trace                            NEXT
local executable validation                              PENDING R7.9
```

No R3/R4/R5/R6 runtime PASS is claimed.

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
aggregate existential support != discard other supported matching commands
R3 unresolved != absent evidence != not_established
remote source/test review != runtime PASS
final local validation should validate the frozen remote candidate, not become a parallel implementation path
accepted executable revision != later documentation-only closure revision
live external verification != deterministic baseline
```
