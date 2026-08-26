# Working Memory — B2 R7 Acceptance, Cleanup, and Baseline Closure

**Date:** 2026-08-26  
**Status:** R7 SELECTED; R7.0 COMPLETE; R7.1 COMPLETE; R7.2 REMOTE ORCHESTRATION TRACE COMPLETE; R7.3 NEXT  
**Execution branch:** `main`  
**Current plan:** `../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`  
**Findings register:** `2026-08-26_B2-R7-findings-register.md`

## 1. Purpose and execution mode

This is the primary progressive execution record for R7. R7 closes the R1–R6 reconciliation; it is not another feature-expansion phase.

Remote-first execution remains controlling:

```text
R7.0–R7.8
→ work remotely against GitHub main
→ source/test/commit/diff/real-case/ownership/proof review
→ implement only later-dispositioned justified cleanup
→ NO local runtime acceptance claims

R7.9
→ after remote work is finished
→ pull exact frozen main candidate locally
→ run final validation bundle

R7.10
→ record accepted executable baseline + mandatory handoff
```

If R7.9 fails, preserve the exact output, return to the smallest owning remote slice, repair on GitHub, refreeze, and rerun the required local gate. Do not create an unrecorded local patch path.

Learning-by-Doing-and-Building remains proportionate:

```text
brief orientation
→ bounded remote work
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
REMOTE CANDIDATE REVISION
→ final code/test SHA after remote R7 review/cleanup
→ not runtime accepted yet

ACCEPTED EXECUTABLE REVISION
→ exact remote candidate after R7.9 local validation passes

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

## 9. Current R7 state

```text
R7.0 exact state re-anchor                                  COMPLETE
R7.1 remote focused R3–R6 source/test contract audit       COMPLETE
R7.2 remote normal investigation/CI orchestration trace     COMPLETE
R7.3 remote real-case GitHub evidence pressure              NEXT / NOT STARTED
R7.4 architecture/naming/retention review                   NOT STARTED
R7.5 bounded remote cleanup/finding disposition fixes       NOT STARTED
R7.6 remote post-cleanup source/diff + proof audit          NOT STARTED
R7.7 audit lifecycle reconciliation                        NOT STARTED
R7.8 final remote candidate + local bundle freeze           NOT STARTED
R7.9 final local pull + executable validation               DEFERRED UNTIL R7.8
R7.10 accepted baseline + mandatory handoff                 NOT STARTED
```

Queued findings now:

```text
F-001 mixed-segment granularity loss
→ conservative under-reporting

F-002 unavailable project-root evidence dropped
→ possible uncertainty erasure into not_established
→ high-priority final disposition

F-003 legacy CI compatibility surfaces
→ retention/naming cleanup pressure
```

## 10. R7.3 next bounded slice

Use the GitHub connector against retained real public cases, especially S001, rather than running local code.

For S001:

```text
Pydantic PR #13432
→ exact PR head identity
→ actual exact-head pull-request workflow runs
→ exact workflow definitions
→ exact pyproject.toml / uv.lock evidence
→ verify real command shapes and lock-root/path facts
→ compare real evidence against R3–R6 admitted contracts
```

R7.3 must specifically pressure:

- whether S001 still contains the expected `--all-packages --group docs` positive shape;
- whether exact lock facts still support `docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve` structurally;
- whether multiple relevant/non-relevant commands have the shapes our regressions claim;
- whether a real admitted workflow exposes F-001 mixed-segment behavior;
- whether real source acquisition exposes F-002 or another unavailability/identity edge;
- whether S011/S005 retained evidence still supports their boundary roles where useful.

Any new edge becomes F-004+ in the findings register. Do not implement queued findings merely because R7.3 provides more evidence; first gather and classify the complete remote picture unless a hard proof/normal-path blocker demands immediate action.

## 11. Final local validation principle

At R7.8, after all remote executable work is finished, freeze one exact candidate and one exact validation bundle. The user runs that bundle locally only in R7.9. The exact output becomes acceptance evidence; a failure reopens remote work.

## 12. Post-R7 mandatory handoff

Only successful R7.9 executable validation allows R7.10 to accept the baseline and activate:

```text
plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md
```

That checkpoint must reach an explicit evidence-backed disposition before old Cluster 6 or another ordinary B2 expansion becomes live work.
