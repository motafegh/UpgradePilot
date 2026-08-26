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
- **Plan position:** **R0 COMPLETE; R1 COMPLETE; R2 COMPLETE; R3 IMPLEMENTED / RUNTIME ACCEPTANCE PENDING R7; R4 IMPLEMENTED TO STATIC/SOURCE-REVIEW DEPTH / RUNTIME ACCEPTANCE PENDING R7; R5 IMPLEMENTED TO STATIC/SOURCE-REVIEW DEPTH / RUNTIME ACCEPTANCE PENDING R7; R6 IMPLEMENTED TO STATIC/SOURCE-REVIEW DEPTH / RUNTIME ACCEPTANCE PENDING R7; R7 ACTIVE — R7.0 COMPLETE / R7.1 NEXT**.
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
- **R7 entry revision:** `fa12852598a8f687eac6827a296b87c66b7f932f` — R7 plan refinement HEAD when R7 was selected.
- **Pending executable candidate source/test revision:** `71df95cb60a0a476dce2ca090de504a77bde1d99`. The later R6 proof-preservation working-memory commit and R7 plan-refinement commit changed no executable source/tests, so this is the same executable tree entering R7; it is **not yet accepted**.
- **Current bounded continuation:** execute **R7.1 focused R3–R6 executable acceptance**. Load only current environment/test-command facts needed for reproducible execution, run the narrowest meaningful R3/R4/R5/R6 checks, record exact commands/counts/results, and stop broad progression on any focused failure until diagnosed and repaired. No R3/R4/R5/R6 runtime PASS is claimed yet.
- Learning-by-Doing-and-Building remains the normal execution loop, applied proportionately: brief orientation → real bounded work → actual evidence → material state preservation → concise post-action learning/ownership closure → next bounded slice. Avoid ceremony for routine repeated checks; spend depth on failures, proof boundaries, ownership, and cleanup decisions.
- Dedicated B2 mastery learning package remains paused while this reconciliation plan is active.
- Previous dependency-environment/CI plan remains deferred at completed Cluster 5; do not start old Cluster 6.
- **AUDIT-005 / product AI-agentic orchestration remains SCHEDULED.** Successful R7 acceptance activates `plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md` before ordinary B2 continuation.

## R7 acceptance entry state

R7.0 established exact state only; it did not execute validation.

```text
R7 entry HEAD
fa12852598a8f687eac6827a296b87c66b7f932f

latest source/test-changing revision
71df95cb60a0a476dce2ca090de504a77bde1d99

71df95cb... → fa128525...
only:
- R6 proof-preservation working-memory record
- R7 plan refinement

therefore executable source/test tree unchanged across those later documentation/planning commits
```

The post-R6 proof-preservation correction is part of the pending R7 executable candidate:

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

and must protect:

```text
R3 unresolved
→ unresolved CI consumption
→ unresolved coverage consumption state

NOT
→ evidence disappearance
→ static_dependency_consumption_not_observed / not_established
```

R7 revision semantics are now explicit:

```text
R7 ENTRY REVISION
→ repository HEAD when R7 is selected

ACCEPTED EXECUTABLE REVISION
→ exact final post-cleanup code/test revision that receives final deterministic validation

CLOSURE REVISION
→ possible later audit/memory/docs-only revision
→ not newly execution-tested merely because it is later
```

Current R7 acceptance status:

```text
R7.0 exact state re-anchor                            COMPLETE
R7.1 focused R3–R6 executable acceptance            NEXT / NOT STARTED
R7.2 normal investigation/CI integration acceptance  NOT STARTED
R7.3 live S001 external verification                  NOT STARTED
R7.4 full deterministic suite                         NOT STARTED
R7.5 architecture/naming/retention review             NOT STARTED
R7.6 bounded cleanup if justified                     NOT STARTED
R7.7 final post-cleanup executable validation         NOT STARTED
R7.8 proof-boundary audit                             NOT STARTED
R7.9 audit lifecycle reconciliation                   NOT STARTED
R7.10 deterministic baseline freeze + handoff         NOT STARTED
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

The bounded local-model path remains:

```text
authoritative deterministic source
→ bounded model semantic candidate
→ deterministic source reconstruction / admission
→ grounded claim
```

The model does not own source authority, target relevance, compatibility, safety, or action.

## R2 accepted uv.lock structural ownership

R2 goal from the active plan was:

> Introduce one bounded uv-specific structural lock model so external `uv.lock` structural truth is established once and separate semantic consumers use that admitted structure.

Starting pressure was:

```text
uv_lock.py transition parser
+
uv_membership.py reachability parser
→ overlapping structural truth
→ demonstrated versionless-record drift
```

R2 selected and implemented the smallest shared owner:

```text
exact uv.lock text
→ uv_lock_structure.py
   - TOML admission
   - schema/revision admission
   - core package-record name/version/source admission
   - versionless editable/virtual boundary
   - repeated normalized-name preservation
→ admitted UvLockStructure
   ├── uv_lock.py transition semantics
   └── reachability-specific projection/traversal
```

Important design boundary:

```text
SHARED STRUCTURAL FACT
schema/revision/core package record/version/source/repeated-record structure

!=

TRANSITION SEMANTICS
base/head pairing, artifact-only canonical comparison, exact version transition

!=

REACHABILITY SEMANTICS
project/root binding, selected roots, edge markers/extras, deterministic edge resolution, traversal
```

The known versionless-record disagreement is removed structurally: a package with no textual version now enters either consumer only when the shared parser admits an exact one-key editable/virtual local source. The shared parser also closes the former membership-only `version = true` schema-admission bug by requiring exact integer type.

Product-code implementation/test milestone:

```text
77575e3558c6425066047b5e3201e61f8665d0d9
```

Accepted locally tested R2 branch head before closure-only documentation:

```text
9da2ebe6d4073bfde3f58aee7111004e71ad9cc2
```

No product code changed between those two SHAs; the later commits reinforced governance/learning/live-state documentation.

Focused regression:

```text
tests/test_uv_lock_structure.py
```

Accepted R2 runtime evidence:

```text
shared structural regression                  5 tests / OK
existing uv-focused regression discovery      user reported green
complete standard suite                       507 tests / OK
compileall src/tests                          PASS
local worktree after validation               clean
final connector ownership/diff review         PASS
```

Final review found no unexplained structural drift and no accidental R3 workspace-scope implementation, R4 proposition/naming redesign, generic dependency graph abstraction, or resolver/runtime proof.

Real S001 learning/ownership trace used during closure:

```text
base/head uv.lock
→ UvLockStructure
→ uv_lock.py
→ soupsieve 2.6 → 2.8.4

head uv.lock + selected docs roots
→ reachability-specific consumer
→ docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve
→ transitive selected-root witness
```

**R2 disposition: COMPLETE / ACCEPTED.** Closure details are in `working-memory/2026-08-25_B2-R2-runtime-acceptance-and-main-promotion.md`.

## R3 package-scope reconciliation

R3 goal from the active plan is:

> Preserve the minimum real uv command scope required by current evidence, beginning with S001 `--all-packages`, so positive and negative-ish reachability semantics remain sound.

Pre-R3 loss:

```text
real command
uv sync --all-packages --group docs

old declaration
manager=uv
operation=sync
selectors=(docs,)
project_root=...

--all-packages
→ discarded
```

The R3 implementation adds one bounded producer-owned fact:

```text
ProjectEnvironmentSelectionDeclaration
└── package_scope
    ├── bound_project
    └── all_workspace_packages
```

`environment_selection.py` now preserves literal `--all-packages` as `all_workspace_packages`. Ordinary pip/uv declarations remain `bound_project`. Unsupported package-targeting scope such as `--package`, `--directory`, and `--no-project` remains unresolved and does not emit a misleading bound-project declaration.

The consumer applies the proof asymmetry explicitly:

```text
all_workspace_packages
+ one unconditional bound-project selected-root witness
→ positive reachability

all_workspace_packages
+ no bound-project witness
+ complete workspace roots not modeled/exhausted
→ unresolved

NOT
→ not_established
```

This deliberately does not enumerate guessed workspace members from editable/virtual lock records. Complete workspace discovery/member/config semantics, defaults, exclusions, conflicts, package targeting, and complete `--only-group` environment formation are not introduced in R3.

Focused R3 tests cover:

```text
S001-shaped --all-packages scope preservation
ordinary bound-project scope
uv run option-prefix scope preservation
unsupported --package targeting → unresolved/no false declaration
S001 positive witness under all-workspace scope
no-witness all-workspace → unresolved
explicit [tool.uv.workspace] multi-member producer→consumer regression
```

R3 source/test candidate before memory-only state recording:

```text
4b6714aef29c57682c96e3c0b243bb1b93268181
```

Current R3 verification status:

```text
static producer→consumer responsibility review    PASS to current depth
focused R3 runtime tests                          PENDING R7.1
uv-focused regression discovery                  PENDING R7.1/R7.2 as selected
complete standard suite                          PENDING R7.4
compileall src/tests                              PENDING current accepted verification procedure
```

R3 runtime acceptance is not claimed. R7 now owns the deferred executable acceptance.

## R4 selected-root reachability reconciliation

R4 goal from the active plan is:

> Align names, inputs, comments, tests, and output semantics with explicit selected-root reachability rather than complete uv environment formation.

New preferred contract:

```text
UvLockDependencyContext
+ ProjectEnvironmentSelectionDeclaration
+ exact uv.lock
→ evaluate_uv_selected_root_reachability(...)
→ UvSelectedRootReachability
```

Public state semantics:

```text
reachable
→ at least one admitted explicit selected root has one unconditional deterministic lock-backed path to the changed package

not_established
→ the complete root domain represented by this bounded result was exhausted without a witness

unresolved
→ evidence/scope/ambiguity prevents either sound conclusion
```

The new lock-backed reachability evaluator no longer requires exact `pyproject.toml` content. The declaration already supplies `project_root`, selectors, and package scope; the admitted lock supplies local editable/virtual package source paths, selected optional/dev roots, and dependency edges. The bound project is now selected by exact project-root ↔ lock local-source-path relation rather than project-name/content corroboration.

Important separation retained:

```text
lock-backed selected-root reachability
!= pyproject-source optional-extra/dependency-group evidence
!= project/lock coherence/currentness
```

R4 keeps direct/transitive witness paths and the R3 completeness asymmetry. It does not build complete workspace enumeration or a complete uv selected-environment interpreter.

New preferred source/test surfaces:

```text
src/upgradepilot/dependency/uv_reachability.py
tests/test_uv_selected_root_reachability.py
```

`tests/test_source_topology.py` now imports the new evaluator as the preferred responsibility owner.

Transitional boundary after R5:

```text
uv_membership.py
→ no longer the CI consumption contract
→ still temporarily supplies legacy/private reachability projection helpers to uv_reachability.py

ci/consumption.py
→ now consumes UvSelectedRootReachability directly
```

Current R4 verification status:

```text
plan/audit/source responsibility trace          COMPLETE
new R4 source contract                          IMPLEMENTED
focused R4 tests                                IMPLEMENTED
preferred source-topology import                UPDATED
post-write connector source inspection          PASS to static review depth
local focused runtime                           PENDING R7.1
uv-focused regression discovery                 PENDING R7.1/R7.2 as selected
complete standard suite                         PENDING R7.4
compileall                                      PENDING current accepted verification procedure
```

No R4 runtime PASS is claimed. Detailed implementation record: `working-memory/2026-08-25_B2-R4-selected-root-reachability-implementation.md`.

## R5 CI-consumption reachability rebind

R5 goal from the active plan is:

> Ensure Cluster-5 CI composition consumes the narrowed dependency evidence without regressing the split between static consumption, direct exercise, and runtime authority.

The active CI composition now uses:

```text
ProjectSourceEnvironmentMembership
| UvSelectedRootReachability
        ↓
compose_project_environment_consumption(...)
        ↓
StaticDependencyConsumptionEvidence
```

The uv mapping is explicit:

```text
reachable
→ supported
→ reason = selected_uv_roots_reach_changed_dependency
→ preserve reachability_kind + unconditional witness_path
→ source_path = uv.lock

not_established
→ not_established
→ admitted only for bound_project scope

unresolved
→ unresolved
→ preserve dependency-owned reason/detail
→ preserve conditional_candidate_path + unresolved_conditions when present
```

A conditional candidate therefore remains diagnostic evidence only:

```text
conditional structural path
!= supported static consumption
```

The former generic adapter could fall back to the command observation's `pyproject.toml` path for uv evidence. R5 removes that ambiguity: uv reachability is attributed to its exact lock source, while S011-style `ProjectSourceEnvironmentMembership` remains attributed to `pyproject.toml`.

The R3 proof asymmetry is protected at the composition boundary: a synthetic/bounded `not_established` reachability result cannot be rebound to an `all_workspace_packages` declaration. Positive reachability remains existential and is safe when the same bound-project witness sits inside the broader all-workspace command scope.

The CI coverage boundary remains unchanged:

```text
successful exact-head CI
+ supported static dependency consumption
→ supported_not_correlated
```

and still does not establish direct package exercise, command execution, installation success, runtime lock/version use, or behavioral coverage.

R5 changed active source/tests:

```text
src/upgradepilot/ci/consumption.py
tests/test_ci_dependency_coverage.py
tests/test_workflow_dependency_evidence.py
```

Executable/source-test commits:

```text
b72d52e461862ba10a4851b687761c2469237b1f
bdc2672d9b73bdfb67afe95740baf2777b43c5d0
0f35860b66608901c665670240eafb4a9ef0bce0
```

Current R5 verification status:

```text
R5 source/consumer ownership trace                 COMPLETE
legacy uv membership import removed from CI       IMPLEMENTED
explicit uv vs project-source mapping              IMPLEMENTED
S001/S011 focused regression updates               IMPLEMENTED
conditional diagnostic non-promotion regression   IMPLEMENTED
all-workspace negative-scope guard regression      IMPLEMENTED
post-write connector source inspection             PASS to static review depth
R4→R5 changed-file comparison                      PASS / intended executable-test files only
local focused runtime                              PENDING R7.1
nearest dependency/CI integration runtime          PENDING R7.2
complete standard suite                            PENDING R7.4
compileall                                         PENDING current accepted verification procedure
```

No R5 runtime PASS is claimed. Detailed implementation record: `working-memory/2026-08-25_B2-R5-ci-consumption-reachability-rebind.md`.

## R6 real-workflow reachability integration

R6 goal is to prove the reconciled responsibility split against real-case flow rather than keep R3→R4→R5 as a manual/test-side composition.

Selected production seam:

```text
exact admitted PR-head workflow definition
→ ci/workflow_commands.py
→ every readable local RunStepDefinition
→ R3 observe_project_environment_selection(...)
→ dependency-domain relation
   - uv: R4 evaluate_uv_selected_root_reachability(...)
   - project source: evaluate_project_source_environment_membership(...)
→ R5 compose_project_environment_consumption(...)
→ preserve every StaticDependencyConsumptionEvidence
→ evaluate_dependency_ci_coverage(...)
```

The normal `investigation.py` path is migrated in R6, not deferred. This is required because the old dependency-environment plan's Cluster 6 remains blocked while the active reconciliation is running; deferring application migration would allow R7 to freeze a test-only R3→R4→R5 baseline.

Normal orchestration now acquires exact source bundles only after exact PR-head workflow-run admission:

```text
PullRequestIdentity.head_sha
→ pull_request workflow runs at exact head
→ exact workflow file for each admitted run
→ exact project/lock source bundle(s)
→ workflow-derived project-environment consumptions
→ coverage-oriented CI evaluation
```

For uv contexts the exact changed `uv.lock` remains the R4 semantic source. The exact sibling `pyproject.toml` supplies the existing R3 project-root path binding; its content is not reintroduced as an R4 reachability input.

S001 pressure now has three layers:

```text
focused seam regression
→ tests/test_r6_project_environment_workflow_integration.py

normal application regression
→ tests/test_r6_investigation_ci_integration.py

complete-real-source verifier through normal production acquisition
→ tools/verification/2026-08-25_r6_s001_real_ci_reachability.py
```

The live verifier supplies only `pydantic/pydantic` PR `#13432`. It must discover SoupSieve, the exact admitted PR workflows, exact head `uv.lock`, selectors, reachability, and consumption. It does not assert one unique "correct" command; all supported matches are preserved.

Real S001 positive command remains:

```text
uv sync --all-packages --group docs
→ docs selected roots
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
→ R4 reachable / transitive
→ R5 supported
```

Other commands are evaluated independently and stay non-positive unless their own selected roots reach SoupSieve. The real successful `codspeed` PR workflow, for example, selects `testing-extra + email`; relevance is not inherited from the docs workflow.

R6 transfer boundaries also remain explicit:

```text
S011
project-source affected environment + real selector
→ project-source membership path
→ no uv reachability substitution

S005
tox command → uv-venv-lock-runner → exact-lock execution pressure
→ mediated proposition
→ direct R3/R4 uv command seam must not manufacture support

all-workspace no-witness
→ incomplete workspace root exhaustion
→ unresolved
→ never false not_established
```

Focused transfer regressions:

```text
tests/test_r6_project_source_workflow_integration.py
tests/test_r6_s005_mediated_uv_boundary.py
tests/test_uv_package_scope.py
```

Presentation now exposes all retained consumption commands/witnesses through `ci_coverage_result`. A transitional read-only `ci_exercise_result` alias remains for pre-R6 assertions and is an explicit R7 cleanup candidate.

### Post-R6 proof-preservation correction

A bounded review after the main R6 integration found that `derive_project_environment_consumptions()` dropped every R3 observation whose state was not `observed`. Because R3 intentionally uses `unresolved` for material uncertainty, that could erase uncertainty and later allow CI classification to fall through to `not_established`.

The smallest correction is now implemented at the R6 seam:

```text
not_observed
→ no project-environment contribution

unresolved
→ preserve unresolved StaticDependencyConsumptionEvidence
→ do not strengthen through R4/project-source membership/R5

observed
→ unchanged dependency-domain + R5 flow
```

The focused dynamic-selector regression is implemented in `tests/test_r6_project_environment_workflow_integration.py`, but remains pending R7.1 runtime validation.

Current R6 verification status:

```text
production ownership/orchestration trace                 COMPLETE
workflow-derived R3→R4/R5 production seam               IMPLEMENTED
normal investigation migration                           IMPLEMENTED
all supported matching consumption preservation          IMPLEMENTED
PR-head workflow admission boundary                      PRESERVED
S001 focused seam regression                             IMPLEMENTED
S001 normal-application regression                       IMPLEMENTED
S001 complete-real-source verifier                       IMPLEMENTED / NOT RUN
S011 source-membership transfer                          IMPLEMENTED
S005 mediated tox boundary                               IMPLEMENTED
workspace R4 negative-proof guard                        IMPLEMENTED
R3 unresolved-selection preservation                     IMPLEMENTED
post-write connector source/diff review                  PASS to static/source-review depth
local focused runtime                                    PENDING R7.1
real S001 verifier runtime                               PENDING R7.3
nearest integration/runtime suites                       PENDING R7.2
complete standard suite                                  PENDING R7.4
compileall                                               PENDING current accepted verification procedure
```

No R6 runtime PASS is claimed. Detailed records:

- `working-memory/2026-08-25_B2-R6-real-workflow-reachability-integration.md`
- `working-memory/2026-08-25_B2-R6-unresolved-selection-proof-preservation-fix.md`

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
accepted executable revision != later documentation-only closure revision
live external verification != deterministic baseline
```
