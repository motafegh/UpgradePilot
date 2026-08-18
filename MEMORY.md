# UpgradePilot Current Memory

**Last updated:** 2026-08-18  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Selected responsibility:** **Dependency Environment and CI Consumption Evidence** under [`plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md).
- **Progressive implementation record:** [`working-memory/2026-08-16_B2-dependency-environment-ci-consumption-implementation.md`](working-memory/2026-08-16_B2-dependency-environment-ci-consumption-implementation.md).
- **Career Day-30 ownership handoff:** [`learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/CAREER_DAY30_OWNERSHIP_HANDOFF.md`](learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/CAREER_DAY30_OWNERSHIP_HANDOFF.md) is an active external evidence/ownership overlay; it does not change technical sequencing or authorize product work.
- **Current status:** Clusters 0–5 COMPLETE/GREEN; Cluster 6 not started.
- **Validated Cluster-0 baseline:** `7444324e511b1e6fb49e6dba0bac371272bff7ba` — `435 tests / OK`, aligned, clean.
- **Validated Cluster-1 revision:** `ef8b4aa623bb53356b0969d099d2e32ee250b3e9` — `439 tests / OK`, aligned, clean.
- **Validated Cluster-2 revision:** `f3e226a27216f75a689b73acbc4404cafb53f1c1` — `452 tests / OK`, aligned, clean.
- **Validated Cluster-3 revision:** `82fdf314e3361f90ab8fd3862247d4bd895a440d` — `476 tests / OK`, aligned, clean.
- **Validated Cluster-4 revision:** `cf2b4ca1a78c6cd008a9c55cb502ed5072647561` — `490 tests / OK`, aligned, clean.
- **Validated Cluster-5 revision:** `bfdfd4257574f85cc3a2d094bf46a37ad6373dea` — `508 tests / OK`, `HEAD == origin/main`, clean worktree.
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
✓ Cluster 5 — typed CI consumption/coverage COMPLETE/GREEN
  Cluster 6 — application/real-case integration NOT STARTED
  Cluster 7 — resolver-satisfiability gate not started
  Cluster 8 — acceptance/STOP-REVIEW not started
```

## Accepted capability through Cluster 5

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

WHAT CI CAN CLAIM FROM STATIC CONSUMPTION + RUNTIME AUTHORITY
successful exact-head CI
+ supported static dependency consumption
→ supported_not_correlated
```

Accepted S001 witness:

```text
selected group docs
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

## Cluster 5 accepted result

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

`ci/workflow_commands.py` additionally provides:

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

`ci/dependency_exercise.py` additionally provides:

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

### S001 accepted Cluster-5 pressure

Focused typed pressure represents:

```text
uv sync --group docs
+ docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve
+ successful exact-head CI
→ consumption supported
→ CI coverage supported_not_correlated
→ direct Soup Sieve exercise not_established
```

### S011 accepted Cluster-5 pressure

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

The new path can also preserve the weaker-but-useful first case without manufacturing exercise.

### Validation evidence

On 2026-08-18 the documented strict Cluster-5 validation sequence ran on synchronized `main` after the source-clarity calibration work:

```text
Ran 508 tests in 0.096s
OK

HEAD        bfdfd4257574f85cc3a2d094bf46a37ad6373dea
origin/main bfdfd4257574f85cc3a2d094bf46a37ad6373dea
worktree    clean
```

The progressive implementation record owns the detailed validation sequence and implementation journey.

## Immediate project action

**Perform the user-selected bounded source-clarity/refactoring pass on already accepted code before starting Cluster 6.**

Current calibration direction:

```text
comments/docstrings only
→ naming/type-expression improvement where ambiguity materially drops
→ small structural cleanup only when justified
→ behavioral/design refactor only when separately identified and validated
```

Preferred next source order begins with:

```text
dependency/change.py
→ dependency/analysis.py
→ dependency/environment.py
→ dependency/environment_membership.py
→ ci/consumption.py
→ ci/workflow_commands.py
→ ci/dependency_exercise.py
→ dependency/environment_selection.py
→ dependency/uv_membership.py
```

Do not treat every file as requiring behavioral refactoring. Apply the `NON-NEGOTIABLE SOURCE CLARITY CONTRACT` and naming specification, preserving accepted semantics unless a separate defect/design issue is established.

Cluster 6 is authorized by the completed validation gate but is **not started or selected as the immediate action** while this bounded clarity pass is active.

## Continuation-critical guards

- `MEMORY.md` alone owns current continuation/latest verification;
- latest validated product point is Cluster 5 at `bfdfd4257574f85cc3a2d094bf46a37ad6373dea` with `508 tests / OK`, aligned and clean;
- Cluster 6 remains not started; source-clarity work must not silently become Cluster-6 application migration;
- source/comment/naming/type cleanups must preserve accepted behavior unless a separately justified refactor is identified;
- Tranche 2 remains optional/separate/not selected;
- static dependency consumption != direct package exercise;
- static evidence + successful CI != static↔runtime job/step correlation;
- successful CI != exact changed version observed;
- resolver satisfiability/currentness remains separate;
- missing/ambiguous evidence != negative fact;
- no generic package-manager/tox/shell/workflow engine without new evidence and explicit selection.

## Learning state

Continue learning-by-building in small coherent blocks: explain the proposition, inspect the real source/data flow, improve one bounded responsibility, validate proportionately, then continue. Passing AI-assisted code does not by itself establish mastery.

For the active Career Day-30 ownership correction, use [`learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/CAREER_DAY30_OWNERSHIP_HANDOFF.md`](learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/CAREER_DAY30_OWNERSHIP_HANDOFF.md). It requires stronger project-local evidence of current-source understanding, representative test understanding, one legitimate ownership-bearing source/test change, and real failure diagnosis when such a failure naturally occurs. It also requires prediction/reconstruction before key AI answers or changes and changed-case transfer where useful.

Cluster-5 validation is complete. The current user-selected continuation is the bounded source-clarity/refactoring pass before ordinary Cluster-6 application integration; this does not force artificial behavioral changes or failures.
