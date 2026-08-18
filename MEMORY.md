# UpgradePilot Current Memory

**Last updated:** 2026-08-18  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Selected responsibility:** **Dependency Environment and CI Consumption Evidence** under [`plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md).
- **Progressive implementation record:** [`working-memory/2026-08-16_B2-dependency-environment-ci-consumption-implementation.md`](working-memory/2026-08-16_B2-dependency-environment-ci-consumption-implementation.md).
- **Career Day-30 ownership handoff:** [`learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/CAREER_DAY30_OWNERSHIP_HANDOFF.md`](learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/CAREER_DAY30_OWNERSHIP_HANDOFF.md) is an active external evidence/ownership overlay; it does not change technical sequencing or authorize product work.
- **Current status:** Clusters 0–4 COMPLETE/GREEN; **Cluster 5 IMPLEMENTED / VALIDATION PENDING**; Cluster 6 not started.
- **Validated Cluster-0 baseline:** `7444324e511b1e6fb49e6dba0bac371272bff7ba` — `435 tests / OK`, aligned, clean.
- **Validated Cluster-1 revision:** `ef8b4aa623bb53356b0969d099d2e32ee250b3e9` — `439 tests / OK`, aligned, clean.
- **Validated Cluster-2 revision:** `f3e226a27216f75a689b73acbc4404cafb53f1c1` — `452 tests / OK`, aligned, clean.
- **Validated Cluster-3 revision:** `82fdf314e3361f90ab8fd3862247d4bd895a440d` — `476 tests / OK`, aligned, clean.
- **Validated Cluster-4 revision:** `cf2b4ca1a78c6cd008a9c55cb502ed5072647561` — `490 tests / OK`, aligned, clean.
- **Current Cluster-5 source/test implementation point before WM/live-state docs:** `f7fcd5e2dad98e3ab3ac59a1950cfb6d79cb0099` — validation not yet observed.
- **Tranche-1 historical accepted revision:** `ef4283db0a7ce3eec75a56ccc5c07354015fd2e3` — complete/green; not reopened.
- **Tranche 2:** NOT SELECTED / NOT AUTHORIZED.

## Selected responsibility

```text
trusted dependency change
+
exact dependency source/environment membership
+
static workflow environment selection / consumption declaration
+
separate exact-head runtime CI evidence
↓
bounded CI consumption/coverage evidence
↓
stronger exercise/runtime claims only when independently justified
```

Core proof ladder:

```text
dependency transition
!= environment membership
!= static environment selection
!= static dependency consumption
!= resolver satisfiability/currentness
!= runtime execution/success
!= exact-version witness
!= direct package exercise
!= behavioral compatibility/safety/action
```

Primary pressure:

```text
S001 — uv locked-environment positive consumption
S011 — pyproject optional-extra non-consumption under dev-only CI
S005 — tox/uv mediated lock-consumption transfer pressure
```

## New-plan implementation status

```text
✓ Cluster 0 — synchronized/frozen green baseline
✓ Cluster 1 — bounded dependency-environment evidence contract
✓ Cluster 2 — exact pyproject optional-extra transition evidence
✓ Cluster 3 — bounded project-environment selection semantics
✓ Cluster 4 — bounded uv.lock selected-environment membership/reachability
→ Cluster 5 — typed CI consumption/coverage IMPLEMENTED / VALIDATION PENDING
  Cluster 6 — application/real-case integration NOT STARTED / HOLD
  Cluster 7 — resolver-satisfiability gate not started
  Cluster 8 — acceptance/STOP-REVIEW not started
```

## Accepted capability through Cluster 4

UpgradePilot can separately establish:

```text
WHAT CHANGED / WHERE IT BELONGS
numpy 1.26.4 → 2.4.6
+ PyprojectOptionalExtraDependencyContext(extra="mlx")

WHAT STATIC WORKFLOW SELECTS
pip install -e ".[dev]" → OptionalExtraSelector("dev")
uv sync --group docs     → DependencyGroupSelector("docs")

WHETHER A UV-SELECTED ENVIRONMENT CONTAINS THE CHANGE
exact project metadata
+ exact uv.lock
+ explicit uv selector
→ member(direct|transitive) | not_established | unresolved
```

Accepted S001 witness:

```text
selected group docs
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

## Cluster 5 implemented result — validation pending

### CI semantic split

The new CI path no longer forces consumption and exercise into one proposition.

```text
STATIC CONSUMPTION
changed dependency is included by a statically declared CI dependency environment

STATIC DIRECT EXERCISE
changed package is directly invoked after supported consumption in the same static job

RUNTIME AUTHORITY
exact-head workflow/job evidence completed successfully
```

Strongest current coverage meaning:

```text
successful exact-head CI
+ supported static dependency consumption
→ supported_not_correlated
```

This does not require direct package exercise and does not correlate the consuming static job/step to runtime execution.

### New dependency-owned project environment membership

Created:

```text
src/upgradepilot/dependency/environment_membership.py
```

It keeps optional-extra/dependency-group comparison outside CI.

S011 guard now has a typed relation:

```text
affected extra = mlx
selected extra = dev
→ not_established
```

Matching explicit extra/group or all-extras/all-groups can establish membership; project-root mismatch is unresolved.

### New CI consumption evidence

Created:

```text
src/upgradepilot/ci/consumption.py
```

`StaticDependencyConsumptionEvidence` preserves:

```text
state
mechanism
normalized changed-package identity
exact workflow path/revision
static job/step/segment location
command
reason/detail
optional source path
optional direct/transitive witness path
```

Project-environment membership maps to CI consumption without adding runtime meaning.

### Exact rebinding guard

Externally composed project-environment consumption is accepted only if it matches:

```text
same changed normalized package
same exact workflow path
same exact workflow revision
same readable static job
same run-step source index
same command text
valid bounded segment index
```

Mismatch is preserved as an explicit static problem.

### New multi-job static workflow inspection

`ci/workflow_commands.py` now additionally provides:

```python
inspect_workflow_dependency_evidence(...)
```

The new path preserves all readable static jobs rather than rejecting a workflow solely for having multiple jobs.

It produces separately:

```text
consumption evidence
+ direct package invocation locations
+ static structure/source problems
```

Requirements consumption is admitted only from typed `RequirementsFileDependencyContext` and the dependency-owned direct-install observer. Constraints/uv-lock/pyproject paths do not become pip requirements evidence merely because they are paths.

### New coverage evaluator

`ci/dependency_exercise.py` now additionally provides:

```python
evaluate_dependency_ci_coverage(...)
```

Workflow results preserve:

```text
coverage state
consumption state/reason/detail
direct exercise state/reason/detail
selected commands
all consumption items
all invocation items
all static problems
```

Aggregate states remain:

```text
supported_not_correlated
no_successful_ci
unresolved
```

The legacy `evaluate_dependency_ci_exercise(... direct_requirements_install_path=...)` and legacy one-job `inspect_workflow_commands(...)` remain temporarily so ordinary application/CLI code stays unchanged until Cluster 6.

### S001 intended Cluster-5 result

Focused typed pressure represents:

```text
uv sync --group docs
+ docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve
+ successful exact-head CI
→ consumption supported
→ CI coverage supported_not_correlated
→ direct Soup Sieve exercise not_established
```

### S011 intended Cluster-5 result

```text
affected environment = mlx
workflow selects = dev
→ consumption not_established
+ successful exact-head CI
→ changed mlx CI coverage not established / unresolved
```

Green CI is therefore not promoted into changed-environment coverage.

### Requirements preservation

```text
pip install -r requirements-dev.txt
→ consumption supported

pip install -r requirements-dev.txt
then direct pytest invocation
→ consumption supported
→ direct exercise supported
```

The new path can now also preserve the weaker-but-useful first case without manufacturing exercise.

### Focused tests added

```text
tests/test_project_source_environment_membership.py
tests/test_ci_dependency_coverage.py
tests/test_workflow_dependency_evidence.py
```

`tests/test_source_topology.py` was updated for the new CI/dependency owners. Existing legacy CI tests remain unchanged and are part of the validation gate.

## Immediate project action

**Validate Cluster 5. Do not start Cluster 6 yet.**

Required next action:

1. synchronize local `main`;
2. run import smoke for new membership/consumption/coverage modules;
3. run focused Cluster-5 tests;
4. run legacy CI/workflow-command regressions;
5. run nearest dependency/environment/application regressions;
6. run the complete deterministic product suite;
7. record exact test count, HEAD/origin/worktree in the progressive WM;
8. only after green validation mark Cluster 5 complete and enter Cluster 6.

Use strict validation inside a subshell so shell options do not leak into the interactive VS Code zsh prompt.

## Continuation-critical guards

- `MEMORY.md` alone owns current continuation/latest verification;
- latest validated product point remains Cluster 4 at `cf2b4ca1a78c6cd008a9c55cb502ed5072647561` with `490 tests / OK` until Cluster 5 is validated;
- Cluster-5 source/test implementation point is `f7fcd5e2dad98e3ab3ac59a1950cfb6d79cb0099` before documentation commits;
- Cluster 6 is not started and no Cluster-6 source mutation is authorized before Cluster-5 validation;
- Tranche 2 remains optional/separate/not selected;
- static dependency consumption != direct package exercise;
- static evidence + successful CI != static↔runtime job/step correlation;
- successful CI != exact changed version observed;
- resolver satisfiability/currentness remains separate;
- missing/ambiguous evidence != negative fact;
- no generic package-manager/tox/shell/workflow engine without new evidence and explicit selection.

## Learning state

Continue learning-by-building in small coherent blocks: explain the proposition, implement one bounded slice, validate, then append the same working-memory record. Passing AI-assisted code does not by itself establish mastery.

For the active Career Day-30 ownership correction, use [`learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/CAREER_DAY30_OWNERSHIP_HANDOFF.md`](learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/CAREER_DAY30_OWNERSHIP_HANDOFF.md). It requires stronger project-local evidence of current-source understanding, representative test understanding, one legitimate ownership-bearing source/test change, and real failure diagnosis when such a failure naturally occurs. It also requires prediction/reconstruction before key AI answers or changes and changed-case transfer where useful.

This Career handoff **does not change the immediate project action**: Cluster 5 still must be validated before Cluster 6. It does not force artificial code changes or failures, does not require completion of every learning plan before legitimate building, and does not add SQL or any other Career-driven technology to B2.
