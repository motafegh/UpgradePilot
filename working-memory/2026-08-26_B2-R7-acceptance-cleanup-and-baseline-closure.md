# Working Memory — B2 R7 Acceptance, Cleanup, and Baseline Closure

**Date:** 2026-08-26  
**Status:** R7 SELECTED; R7.0 COMPLETE; R7.1 COMPLETE; R7.2 REMOTE ORCHESTRATION TRACE COMPLETE; R7.3 REMOTE REAL-CASE PRESSURE COMPLETE; R7.4 COMPLETE; R7.5 COMPLETE LOCALLY; R7.6 NEXT
**Execution branch:** `main`  
**Current plan:** `../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`  
**Findings register:** `2026-08-26_B2-R7-findings-register.md`

## 1. Purpose and execution mode

This is the primary progressive execution record for R7. R7 closes the R1–R6 reconciliation; it is not another feature-expansion phase.

Ali explicitly superseded the earlier remote-first route before R7.5. R7.0–R7.4 retain their completed remote-depth status and are not reopened; remaining R7 work now proceeds from the exact local `main` checkout:

```text
R7.0–R7.4
→ completed remote source/test/orchestration/real-case/retention evidence
→ historical proof depth remains unchanged

R7.5–R7.8
→ work locally on main in bounded ownership-correct clusters
→ run focused and nearest relevant tests progressively
→ preserve exact commands/results without inflating their proof

R7.9
→ run the final broad deterministic validation bundle against the frozen local candidate

R7.10
→ record accepted executable baseline + mandatory handoff
```

If a local check fails, preserve the exact output, return to the smallest owning R7 slice, repair locally on `main`, and rerun the relevant focused proof before broadening. A final R7.9 failure still invalidates executable acceptance and requires a new frozen candidate after the bounded repair.

Learning-by-Doing-and-Building remains proportionate:

```text
brief orientation
→ bounded local work
→ actual evidence
→ material state/finding preservation
→ concise post-action learning/ownership closure
→ next slice
```

## 2. Revision semantics and R7 entry

R7 entry revision:

```text
fa12852598a8f687eac6827a296b87c66b7f932f
```

Latest source/test-changing revision entering R7:

```text
71df95cb60a0a476dce2ca090de504a77bde1d99
```

The later R7 preparation/recording commits before R7.2 changed planning/memory/working-memory only. Runtime acceptance of the R3–R6 executable candidate remains pending R7.9.

Revision meanings:

```text
EXECUTABLE CANDIDATE REVISION
→ final code/test SHA after local R7 review/cleanup
→ not broadly accepted until R7.9

ACCEPTED EXECUTABLE REVISION
→ exact executable candidate after R7.9 local validation passes

CLOSURE REVISION
→ possible later audit/memory/docs-only SHA
→ not newly execution-tested
```

## 3. R6 correction carried into R7

The post-R6 proof-preservation correction remains part of the candidate:

```text
R3 not_observed
→ no project-environment contribution

R3 unresolved
→ unresolved StaticDependencyConsumptionEvidence
→ preserve workflow/job/step/command + dependency-source identity
→ do not invoke R4/project-source membership/R5 positive-or-negative composition

R3 observed
→ dependency-domain relation → R5
```

The dynamic-selector regression uses:

```yaml
- run: uv sync --group "${{ matrix.group }}"
```

and protects the intended direction:

```text
R3 unresolved
→ unresolved CI consumption
→ unresolved coverage consumption state

NOT
→ evidence disappears
→ static_dependency_consumption_not_observed / not_established
```

Runtime execution remains pending R7.9.

## 4. Executable model under review

Normal product route under R7 is:

```text
public PR
→ dependency analysis + typed changed-dependency source context
→ exact admitted PR-head workflow runs/jobs
→ exact workflow definition for each admitted run
→ exact project/lock source bundle required by dependency context
→ ci/workflow_commands.py
   → every readable local run step
   → checkout/repository provenance admission owned by R6 composition
   → R3 project selection
   → R4 uv selected-root reachability OR project-source membership
   → R5 static CI consumption
   → preserve every resulting consumption
→ evaluate_dependency_ci_coverage(...)
→ PublicPullRequestInvestigation.ci_coverage_result
→ CLI / verifier / application consumers
```

Controlling proof boundaries remain:

```text
dependency transition
!= selected-root reachability
!= project-source membership
!= static selection
!= static consumption
!= direct exercise
!= runtime execution/success
!= resolver/currentness
!= behavioral compatibility/safety/action
```

## 5. R7.1 remote focused source/test contract audit

R7.1 inspected current R3–R6 source and focused tests together without executing them.

Disposition:

```text
REMOTE SOURCE/TEST CONTRACT AUDIT: PASS TO SOURCE/TEST-REVIEW DEPTH
RUNTIME EXECUTION: PENDING R7.9
SOURCE/TEST REPAIR REQUIRED BY R7.1: NO
```

The reviewed contract set coherently represents:

- R3 explicit selectors/package scope and dynamic/unsupported `unresolved`;
- R4 direct/transitive reachability, workspace negative-proof asymmetry, and conditional diagnostics;
- R5 non-strengthening CI-consumption mapping;
- R6 workflow-derived R3→R4/project-source→R5 integration;
- multiple supported command preservation;
- unresolved-selection preservation;
- S011 project-source separation;
- S005 mediated-tox non-promotion;
- workspace and marker pressure.

R7.1 discovered F-001, recorded separately in the findings register: mixed safe+unresolved shell segments in one `run:` block can conservatively suppress an independently safe declaration because R3 uncertainty is step-scoped while declarations are segment-indexed.

No implementation was performed; F-001 is queued for final R7 disposition.

## 6. R7.2 remote normal investigation/CI orchestration trace

R7.2 traced the actual ordinary product path end-to-end from current source/tests and searched repository-wide callers for legacy paths.

No code was executed. No runtime PASS is claimed.

### 6.1 Dependency producer binding

`dependency/analysis.py` establishes source contexts from the frozen PR identity and exact changed dependency evidence.

For each current dependency source context, the important relation is:

```text
repository = pull identity repository
revision = exact PR head SHA
normalized_package = canonical changed package
source_evidence = exact admitted changed source
```

For uv, this creates `UvLockDependencyContext`; it does not invent CI group/extra selection.

### 6.2 Provider-owned PR workflow admission is real, not assumed

`GitHubActionsClient.get_exact_head_workflow_runs(identity)` queries pull-request workflow runs bound to:

```text
event = pull_request
head_sha = identity.head_sha
```

Run parsing independently rejects mismatched event/head identity. Job acquisition also validates the frozen head relation.

`GitHubRepositoryClient.get_exact_head_workflow_file(identity, run)` revalidates:

```text
run id
workflow id
pull_request event
exact PR head SHA
workflow path under .github/workflows/
```

and then retrieves the workflow definition at the exact PR head revision.

Therefore:

```text
PR-head workflow admission
→ provider validation
→ only then workflow/dependency semantics
```

R3/R4/R5 do not search arbitrary repository workflows.

### 6.3 Normal `investigation.py` route is coverage-oriented

The ordinary dependency branch now does:

```text
analyze_dependency_change(...)
→ get_exact_head_workflow_runs(...)
→ get_workflow_jobs(...)
→ _acquire_project_environment_sources(...)
→ get_exact_head_workflow_file(...)
→ derive_project_environment_consumptions(...)
→ WorkflowDependencyExerciseInput(external_consumptions=...)
→ evaluate_dependency_ci_coverage(...)
→ ci_coverage_result
```

The normal path does not require a caller/test to supply a prebuilt selection declaration, reachability result, project-source membership result, or CI consumption.

The R6 normal-integration regression `tests/test_r6_investigation_ci_integration.py` protects that orchestration shape using controlled external clients while allowing the product code to derive R3→R4/R5 semantics itself.

### 6.4 Exact project/lock source acquisition

For `UvLockDependencyContext`, normal investigation acquires:

```text
exact sibling pyproject.toml at the lock/workspace root
+
exact uv.lock
```

The sibling project file supplies the existing R3 project-root binding. R4 still does not parse its content; the lock remains R4's semantic source.

For pyproject optional-extra/dependency-group contexts, the exact source pyproject is acquired and the separate project-source membership proposition remains in force.

Requirements/constraints remain on their direct-install/static path rather than being forced into uv/project-source semantics.

### 6.5 Coverage preserves the collection even when summaries select one item

`evaluate_dependency_ci_coverage(...)` and the workflow-scoped result retain:

```text
all static consumptions
all direct invocations
all static problems
```

Classification may select one representative supported/unresolved/not-established item for summary fields, but the returned workflow evidence keeps the full underlying collection.

Static-consumption classification order remains:

```text
supported
→ unresolved
→ structural/source problems as unresolved
→ not_established
→ fallback static_dependency_consumption_not_observed
```

This ordering is important to the proof-calibration findings below.

### 6.6 Application/CLI uses the current coverage result

`PublicPullRequestInvestigation` owns:

```text
ci_coverage_result: DependencyCICoverageResult | None
```

The CLI reads `ci_coverage_result` directly and renders all retained workflow consumptions/witnesses. It does not use the legacy evaluator as the ordinary product path.

The read-only `ci_exercise_result` property remains a transitional alias returning `ci_coverage_result`.

### 6.7 Legacy caller trace

Repository-wide search found no ordinary `investigation.py` or CLI caller of:

```text
evaluate_dependency_ci_exercise(...)
inspect_workflow_commands(...)
```

Those surfaces remain in source and legacy tests/history. `tests/test_source_topology.py` still deliberately imports the legacy evaluator alongside the current coverage evaluator.

The `ci_exercise_result` alias and `direct_requirements_install_path` compatibility surfaces also remain referenced by older tests/history despite no longer owning the ordinary coverage-oriented application route.

This is retention pressure, not automatic removal authority; it is recorded as F-003 for R7.4.

## 7. R7.2 findings

### F-002 — required project-root source unavailability can disappear

R7.2 confirmed a higher-priority proof-calibration edge:

```text
uv context
→ sibling pyproject.toml is UnavailableRepositoryFile
→ derive_project_environment_consumptions skips source because project_file is not RepositoryTextFile
→ no R3 observation / no unresolved project-environment evidence
→ coverage may fall through to static_dependency_consumption_not_observed / not_established
```

This can erase known uncertainty into negative-ish absence and therefore requires explicit disposition before R7.8 candidate freeze. It is recorded in detail in the findings register, with bounded repair direction and regression fixtures.

Per the agreed R7 method, it is **not implemented yet**; later R7 evidence may clarify the correct owning repair alongside other findings.

### F-003 — legacy CI compatibility/retention residue

The normal product route is migrated, but old evaluator/helper/alias/projection surfaces remain protected by legacy tests/topology. Their retention must be justified by a real supported compatibility responsibility, not test inertia.

F-003 is recorded for R7.4 KEEP/MOVE/NARROW/REMOVE disposition. No removal was performed in R7.2.

## 8. R7.2 disposition

```text
NORMAL PRODUCT ROUTE: ESTABLISHED TO REMOTE SOURCE/ORCHESTRATION-TRACE DEPTH
PR-CI ADMISSION BEFORE SEMANTICS: PROVIDER-ENFORCED
R3→R4/project-source→R5 IN NORMAL investigation.py PATH: YES
PREBUILT TEST-SIDE SEMANTIC OBJECTS REQUIRED BY NORMAL PATH: NO
MULTIPLE UNDERLYING CONSUMPTIONS PRESERVED: YES
CLI CONSUMES COVERAGE PATH: YES
LEGACY EVALUATOR IN NORMAL PRODUCT PATH: NO
RUNTIME EXECUTION: PENDING R7.9
NEW FINDINGS: F-002, F-003
EXECUTABLE REPAIR PERFORMED IN R7.2: NO
```

R7.2 is therefore complete as a remote orchestration/ownership trace. Its result does not claim executable success and does not resolve the queued findings.

## 9. R7.3 remote real-case GitHub evidence pressure

R7.3 used exact retained public cases, led by Pydantic S001 PR `#13432` at head `aa2dc024d33f61cdef50bf1973ab5adf0a974f5a`, to pressure the normal R3–R6 route against real GitHub workflow/source evidence.

Established S001 facts:

```text
PR changes only uv.lock
soupsieve 2.6 → 2.8.4

normal CI docs step:
uv sync --all-packages --group docs

exact lock witness:
docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve 2.8.4
```

The normal CI workflow checks Pydantic out at workspace root before that selector, so the intended positive witness remains sound. Codspeed also establishes the current repository at root before its selector and remains expected non-positive for SoupSieve under the current R4 graph evidence.

S001 did not trigger F-001: the positive docs selector is a standalone literal `run:` step rather than a safe+unresolved mixed command block. S001 also does not trigger F-002 because its exact sibling `pyproject.toml` and `uv.lock` are readable.

### F-004 hard blocker discovered and repaired

The admitted Pydantic `Third party tests` workflow exposed a provenance defect. Its jobs intentionally check another project such as Pandera out at `GITHUB_WORKSPACE` root and Pydantic into a subpath such as `pydantic-latest`. A root command like Pandera's:

```text
uv sync ... --group docs
```

belongs to Pandera, not Pydantic.

Pre-fix R6 did not track checkout ownership and could bind that external-project command to Pydantic's exact `pyproject.toml`/`uv.lock`, then find the real Pydantic docs→SoupSieve path and manufacture false supported Pydantic static consumption.

Because that is false support through authority/provenance conflation, F-004 met the R7 hard-blocker rule and interrupted R7.3 sampling.

The bounded repair keeps ownership in R6 orchestration rather than R3/R4 semantics:

```text
per-job workspace-root provenance
= not_established | current_repository | other_repository | unresolved

current_repository
→ repository-relative dependency semantics may proceed

other_repository
→ do not bind root commands to changed-repository evidence

not_established / unresolved
→ preserve unresolved checkout-provenance evidence
```

The same root cause was closed for the direct-requirements/direct-invocation branch so external-root `pip install -r ...` cannot be rebound to the changed repository either.

Primary production corrections:

```text
d14bb6d70c9bc34d0116d7c3abd56ea7bab9d6f5
R7 guard project selection with checkout provenance

e320ad64403360ff8b5c9c5a5e55e3c096bfee5a
R7 extend checkout provenance to direct CI evidence
```

Regression/verifier pressure is recorded in the findings register. Runtime execution remains pending R7.9.

Transfer checks retained the intended distinct boundaries:

```text
S011
→ real optional-extra path exists
→ inspected workflows install .[dev], not .[mlx]
→ no false MLX consumption

S005
→ tox/uv-venv-lock-runner mediated exact-lock use
→ not promoted into direct workflow uv-selection evidence
```

R7.3 disposition:

```text
REAL S001 SOURCE/WORKFLOW PRESSURE: COMPLETE TO REMOTE EVIDENCE DEPTH
INTENDED DOCS→SOUPSIEVE WITNESS: RETAINED
F-001: NOT TRIGGERED BY S001 / STILL QUEUED
F-002: NOT TRIGGERED BY S001 / STILL HIGH-PRIORITY QUEUED
F-004: HARD BLOCKER FOUND; REMOTE REPAIR IMPLEMENTED TO SOURCE/TEST-REVIEW DEPTH
S011/S005 TRANSFER BOUNDARIES: NO CONTRADICTION FOUND
RUNTIME ACCEPTANCE: PENDING R7.9
```

## 10. R7.4 architecture/naming/retention review — COMPLETE

R7.4 completed the required caller/responsibility/retention trace. Detailed decisions are recorded in:

```text
working-memory/2026-08-26_B2-R7-R7.4-architecture-naming-retention-disposition.md
```

Key dispositions selected for R7.5:

```text
REMOVE
→ evaluate_dependency_ci_exercise(...)
→ legacy exercise result types
→ inspect_workflow_commands(...)
→ WorkflowCommandEvidence
→ PublicPullRequestInvestigation.ci_exercise_result alias
→ direct_requirements_install_path compatibility projection/result field

NARROW / RENAME, responsibility retained
→ WorkflowDependencyExerciseInput → WorkflowDependencyCoverageInput
→ external_consumptions → project_environment_consumptions

KEEP
→ evaluate_dependency_ci_coverage(...)
→ inspect_workflow_dependency_evidence(...)
→ current coverage/static evidence types
→ ci/dependency_exercise.py module owner
→ current R6 checkout-provenance guard

REMOVE obsolete public contract after unique-test migration
→ evaluate_uv_selected_environment_membership(...)
→ legacy uv membership result/public types

MOVE, do not delete
→ current reachability-specific graph/projection helpers from uv_membership.py
→ into current R4 owner uv_reachability.py
```

The uv split is recorded as F-005: the legacy membership public surface has no production caller found, but its private graph/projection helpers still implement current R4 reachability. R7.5 must move current mechanics before retiring the obsolete public API and must migrate any unique current-proof tests first.

No product source or tests were changed by R7.4. No runtime PASS is claimed.

### 10.1 Operational hygiene note

During connector discovery after the F-004 repair, one temporary root file `noop-temp-should-not-create` was accidentally created and immediately deleted. It is absent from the current tree. The create/delete commits remain in history; do not rewrite history. No product source/test semantics were changed by that incident.

## 11. Current R7 state

```text
R7.0 exact state re-anchor                                  COMPLETE
R7.1 remote focused R3–R6 source/test contract audit       COMPLETE
R7.2 remote normal investigation/CI orchestration trace     COMPLETE
R7.3 remote real-case GitHub evidence pressure              COMPLETE TO REMOTE EVIDENCE DEPTH
R7.4 architecture/naming/retention review                   COMPLETE TO REMOTE DEPTH
R7.5 bounded local cleanup/finding disposition fixes        COMPLETE LOCALLY
R7.6 local post-cleanup source/diff + proof audit           NEXT
R7.7 audit lifecycle reconciliation                        NOT STARTED
R7.8 final local executable candidate + validation bundle   NOT STARTED
R7.9 final broad local executable validation                DEFERRED UNTIL R7.8
R7.10 accepted baseline + mandatory handoff                 NOT STARTED
```

Queued/active findings now:

```text
F-001 mixed-segment granularity loss
→ conservative under-reporting
→ ACCEPTED AS KNOWN BOUNDED LIMITATION in R7.5
→ reopen only on an admitted mixed safe+unresolved real-workflow trigger

F-002 unavailable project-root evidence dropped
→ possible uncertainty erasure into not_established
→ FIXED LOCALLY to focused/nearest-integration depth
→ final broad acceptance remains pending

F-003 legacy CI compatibility surfaces
→ R7.4 retention review COMPLETE
→ selected bounded REMOVE/NARROW actions COMPLETE LOCALLY
→ full standard suite passed at exact executable revision

F-004 checkout/repository provenance conflation
→ hard blocker discovered in R7.3
→ repair protected by local focused/full-standard R7.5 regression evidence
→ final executable acceptance pending R7.9

F-005 legacy uv membership API hosts current R4 mechanics
→ R7.4 ownership split established
→ MOVE current mechanics + REMOVE obsolete public surface COMPLETE LOCALLY
```

Current bounded continuation:

```text
R7.5 bounded cleanup/finding disposition
→ F-002 proof-calibration correction COMPLETE LOCALLY
→ F-003 legacy CI cleanup/naming COMPLETE LOCALLY
→ F-005 R4 owner move + legacy uv surface retirement COMPLETE LOCALLY
→ F-001 explicitly accepted as a trigger-based bounded limitation
→ F-004 post-cleanup source/diff + focused regression re-audit COMPLETE
→ R7.5 COMPLETE; R7.6 NEXT
```

## 12. R7.5 local F-002 proof-calibration cluster — COMPLETE

Starting point:

```text
branch: main
starting revision: 0ce34f153925a45fdb2ad50385faf69e751ce6de
implementation/evidence revision: 3f12283574c1e80ba92a1683ff575420dc9463ba
unrelated untracked state preserved: .codex/environments/environment.toml
```

Implemented boundary:

```text
typed unavailable required project-root source
+ exact visible project-selection command
+ changed-repository root checkout provenance
→ unresolved StaticDependencyConsumptionEvidence
→ reason = required_project_root_source_unavailable
→ preserve missing path + provider reason/detail
→ do not invoke R4 reachability or project-source membership
→ coverage cannot fall through to static_dependency_consumption_not_observed
```

The implementation uses the unavailable evidence's exact locator only to let R3 locate a
relevant static selector. It does not treat the unavailable file as an admitted project root.
R6 then stops before dependency-domain composition and preserves the source failure as
unresolved. This was smaller and more ownership-correct than duplicating command parsing in R6
or inventing a new dependency-domain state.

The new discriminating regression was run before the repair and failed as predicted:

```text
.venv/bin/python -m unittest \
  tests.test_r6_project_environment_workflow_integration.R6ProjectEnvironmentWorkflowIntegrationTests.test_unavailable_required_project_root_remains_unresolved_through_ci_coverage -v

Ran 1 test
FAILED (failures=1)
AssertionError: 0 != 1
```

After the repair, the same command passed:

```text
Ran 1 test
OK
```

Progressive post-change validation:

```text
.venv/bin/python -m unittest tests.test_r6_project_environment_workflow_integration -v
→ 7 tests / OK

.venv/bin/python -m unittest \
  tests.test_r6_investigation_ci_integration \
  tests.test_ci_dependency_coverage -v
→ 12 tests / OK

.venv/bin/python -m unittest \
  tests.test_r6_project_source_workflow_integration \
  tests.test_r6_s005_mediated_uv_boundary -v
→ 2 tests / OK

.venv/bin/python -m unittest \
  tests.test_workflow_dependency_evidence \
  tests.test_github_workflow_definition -v
→ 18 tests / OK

post-change focused/nearest-integration total
→ 39 tests / OK

.venv/bin/python -m compileall -q \
  src/upgradepilot/ci/workflow_commands.py \
  tests/test_r6_project_environment_workflow_integration.py
→ PASS

git diff --check
→ PASS
```

The first full R6 project-environment module run also exposed one stale S001 test key: the
workflow parser intentionally preserves the trailing newline from a YAML `run: |` block, while
the test indexed the exact command without that newline. The returned evidence and the parser's
own block-scalar contract agreed; the integration expectation was corrected by adding the
trailing newline. This was a test-only baseline correction, not a product normalization change.

Ruff result:

```text
.venv/bin/ruff check ...
→ NOT RUN
→ zsh:1: no such file or directory: .venv/bin/ruff
```

Proof boundary:

- the new regression establishes the exact F-002 current-root/readable-workflow/readable-lock/
  unavailable-project-root route;
- the surrounding suites protect current S001/S011/S005, coverage, normal investigation, YAML
  block-scalar, and nearest F-004 project-environment/direct-requirements behavior;
- no full deterministic suite or live GitHub verifier was run in this cluster;
- R7 executable acceptance therefore remains pending.

## 13. R7.5 local F-003 CI legacy cleanup/naming cluster — COMPLETE

Executable/test revision:

```text
0ff7b5d8613d521950e2b45006800f269b8597b3
Retire legacy CI exercise surfaces
```

Implemented dispositions:

```text
REMOVE
→ evaluate_dependency_ci_exercise(...)
→ WorkflowDependencyExerciseResult / DependencyCIExerciseResult
→ inspect_workflow_commands(...) / WorkflowCommandEvidence
→ PublicPullRequestInvestigation.ci_exercise_result
→ DependencyChangeAnalysis.direct_requirements_install_path
→ PublicPullRequestInvestigation.direct_requirements_install_path
→ tests/test_ci_dependency_exercise.py
→ tests/test_workflow_commands.py

NARROW / RENAME
→ WorkflowDependencyExerciseInput → WorkflowDependencyCoverageInput
→ external_consumptions → project_environment_consumptions
→ external_consumption_* diagnostics → project_environment_consumption_*

KEEP
→ evaluate_dependency_ci_coverage(...)
→ inspect_workflow_dependency_evidence(...)
→ typed RequirementsFileDependencyContext consumption
→ current direct-exercise axis and ci/dependency_exercise.py owner
```

Five cases with current coverage value migrated before the legacy tests were deleted:

```text
no workflow inputs
no successful job versus unavailable definition precedence
successful job with unavailable definition
successful job with unsuccessful run
direct invocation before supported consumption
```

The current multi-job, direct-requirements, constraints, aggregation, S001, S011, and S005
tests already protected the remaining admitted behavior more accurately than the removed
combined legacy API.

Validation:

```text
.venv/bin/python -m unittest \
  tests.test_ci_dependency_coverage \
  tests.test_workflow_dependency_evidence -v
→ 22 tests / OK

nearest application/CLI/dependency/R6/topology groups
→ 46 tests / OK

focused/nearest total
→ 68 tests / OK

.venv/bin/python -m unittest discover -s tests
→ 529 tests / OK

.venv/bin/python -m compileall -q src tests
→ PASS

git diff --check
→ PASS
```

F-004 re-audit for this cluster found no checkout-provenance guard change. Its current
project-environment and direct-requirements regression paths ran within the focused/full suites
and remained green. The executable diff was **220 insertions / 1006 deletions across 16 files**;
the large deletion is the explicitly authorized removal of legacy production/test surfaces.

Proof boundary:

- the exact F-003 executable revision passed the complete standard suite;
- later R7.5 executable changes will create a newer candidate, so this is not final R7
  executable acceptance;
- Ruff remained unavailable in the local virtual environment and was not claimed.

## 14. R7.5 local F-005 R4 ownership/legacy uv retirement cluster — COMPLETE

Executable/test revision:

```text
b50e4b1a656625c3215dd3fbf08c28012c6d18aa
Retire legacy uv membership API
```

The actual caller/dependency trace confirmed that the obsolete public selected-environment
membership API had no production caller, while current R4 imported its private graph mechanics.
R7.5 moved the complete reachability-specific projection dependency closure into the current
owner and removed only the obsolete surface:

```text
KEEP / MOVE TO uv_reachability.py
→ package/edge/root projection from admitted UvLockStructure
→ marker/extra parsing needed by that projection
→ deterministic repeated-record edge resolution
→ workspace-source path normalization
→ bounded traversal safety constants

REMOVE
→ src/upgradepilot/dependency/uv_membership.py
→ UvSelectedEnvironmentMembership and public evaluator/types
→ tests/test_uv_selected_environment_membership.py
→ tests/test_uv_membership_universal_lock_boundary.py
```

No generic graph layer was created. `uv_lock_structure.py` remains the shared external lock
admission owner; `uv_reachability.py` now owns the R4-specific interpretation and traversal.
The separate current project-source membership contract remains in `environment_membership.py`.

Unique current-proof cases were migrated before deletion: optional/all-extra roots, activated
dependency extras, repeated-record ambiguity and version discrimination, cycle safety, and
sound positive all-workspace evidence. The universal-lock marker boundary already had stronger
current R4 conditional-candidate coverage, and the shared-structure consumer regression was
rebound to R4.

Validation:

```text
.venv/bin/python -m unittest \
  tests.test_uv_selected_root_reachability \
  tests.test_uv_lock_structure
→ 21 tests / OK

.venv/bin/python -m unittest discover -s tests -p "test_uv*.py"
→ 43 tests / OK

.venv/bin/python -m unittest \
  tests.test_ci_dependency_coverage \
  tests.test_r6_project_environment_workflow_integration \
  tests.test_r6_project_source_workflow_integration \
  tests.test_source_topology
→ 27 tests / OK

.venv/bin/python -m unittest discover -s tests
→ 515 tests / OK

.venv/bin/python -m compileall -q src tests
→ PASS

git diff --check
→ PASS
```

The executable/test diff was **425 insertions / 1650 deletions across 8 files**. Ruff remained
unavailable in `.venv` and was not claimed. This exact revision has full standard-suite proof,
but R7.9 still owns final executable acceptance after the later R7 audit/freeze stages.

## 15. R7.5 final finding disposition and F-004 re-audit — COMPLETE

### F-001

**ACCEPT AS KNOWN BOUNDED LIMITATION.** Current step-level R3 uncertainty can suppress an
independently safe selector when another segment in the same `run:` block is unresolved. The
result is conservative under-reporting, not false support or uncertainty erasure. S001 did not
contain that shape, and no admitted current real workflow established the need for a durable
segment-result contract. No source/test change was made.

Reopen only when admitted real workflow evidence contains a safe literal selector and a
materially unresolved selector in one run block and UpgradePilot needs to preserve both. R3 must
then own per-segment safety; R6 must not guess from declarations retained by an unresolved step.

### F-004

The post-cleanup diff from `0ce34f153925a45fdb2ad50385faf69e751ce6de` through
`b50e4b1a656625c3215dd3fbf08c28012c6d18aa` retains the R6 per-job workspace-root checkout gate
before project-environment or direct-requirements evidence can bind to changed-repository source.
F-002 added an earlier unavailable-source stop, F-003 removed legacy CI surfaces without
weakening the gate, and F-005 did not touch workflow/coverage code.

Explicit post-cleanup regression command:

```text
.venv/bin/python -m unittest -v \
  tests.test_r6_project_environment_workflow_integration.R6ProjectEnvironmentWorkflowIntegrationTests.test_third_party_root_checkout_does_not_rebind_external_uv_selection_to_pydantic_lock \
  tests.test_r6_project_environment_workflow_integration.R6ProjectEnvironmentWorkflowIntegrationTests.test_dynamic_checkout_path_preserves_provenance_uncertainty \
  tests.test_r6_project_environment_workflow_integration.R6ProjectEnvironmentWorkflowIntegrationTests.test_other_repository_subpath_does_not_displace_current_root_checkout \
  tests.test_workflow_dependency_evidence.WorkflowDependencyEvidenceTests.test_other_repository_root_does_not_rebind_requirements_or_invocation \
  tests.test_workflow_dependency_evidence.WorkflowDependencyEvidenceTests.test_dynamic_root_checkout_preserves_requirements_uncertainty
→ 5 tests / OK
```

This establishes the discriminating local provenance regressions at the current R7.5 candidate.
It does not replace the final R7.9 validation bundle or live S001 verifier.

R7.5 is complete. The next bounded operation is R7.6 local post-cleanup source/diff and
proof-boundary audit; R7.0–R7.5 remain closed unless that audit finds a concrete blocker.

## 16. Final local validation principle

R7.5 onward now uses progressive local focused checks. At R7.8, after all executable cleanup/review is finished, freeze one exact candidate and one final validation bundle. R7.9 runs that broader bundle; its exact output becomes acceptance evidence, and a failure reopens the smallest owning local R7 slice.

## 17. Post-R7 mandatory handoff

Only successful R7.9 executable validation allows R7.10 to accept the baseline and activate:

```text
plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md
```

That checkpoint must reach an explicit evidence-backed disposition before old Cluster 6 or another ordinary B2 expansion becomes live work.
