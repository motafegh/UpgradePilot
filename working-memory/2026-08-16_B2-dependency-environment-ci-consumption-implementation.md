# B2 Dependency Environment and CI Consumption Evidence — Implementation Record

**Date opened:** 2026-08-16  
**Operation:** bounded implementation of [`../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md)  
**Result classification:** IN PROGRESS — CLUSTER 5 IMPLEMENTED / VALIDATION PENDING  
**Execution branch:** `main`

## 1. Validation history

```text
Cluster 0  7444324e511b1e6fb49e6dba0bac371272bff7ba   435 tests / OK
Cluster 1  ef8b4aa623bb53356b0969d099d2e32ee250b3e9   439 tests / OK
Cluster 2  f3e226a27216f75a689b73acbc4404cafb53f1c1   452 tests / OK
Cluster 3  82fdf314e3361f90ab8fd3862247d4bd895a440d   476 tests / OK
Cluster 4  cf2b4ca1a78c6cd008a9c55cb502ed5072647561   490 tests / OK
```

Each accepted point was observed on synchronized `main` with `HEAD == origin/main` and a clean worktree.

## 2. Core proof ladder

```text
trusted dependency transition
!= dependency environment/source membership
!= static workflow environment selection
!= static dependency consumption
!= resolver satisfiability/currentness
!= runtime command execution
!= environment/install success
!= exact proposed runtime version witness
!= direct changed-package exercise
!= behavioral compatibility/safety/action
```

`MEMORY.md` remains the sole live continuation owner. This working memory preserves implementation design, findings, and validation provenance.

## 3. Implementation checklist

- [x] Cluster 0 — synchronized green baseline
- [x] Cluster 1 — typed dependency source/environment contract
- [x] Cluster 2 — exact pyproject optional-extra transition evidence
- [x] Cluster 3 — bounded project-environment selection semantics
- [x] Cluster 4 — bounded uv.lock selected-environment membership/reachability
- [ ] Cluster 5 — CI migration to typed consumption evidence — IMPLEMENTED / VALIDATION PENDING
- [ ] Cluster 6 — ordinary application/CLI integration + S001/S011/S005 pressure
- [ ] Cluster 7 — AUDIT-004 resolver-satisfiability reassessment gate
- [ ] Cluster 8 — full acceptance / STOP-REVIEW

## 4. Accepted machinery through Cluster 4

```text
Cluster 1
DependencyChangeAnalysis.source_contexts becomes stored truth.

Cluster 2
S011:
numpy 1.26.4 → 2.4.6
+ PyprojectOptionalExtraDependencyContext(extra="mlx")

Cluster 3
pip install -e ".[dev]" → OptionalExtraSelector("dev")
uv sync --group docs     → DependencyGroupSelector("docs")

Cluster 4
S001 exact lock-backed witness:
docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve
```

Cluster 4 establishes static selected-environment membership only. It does not establish runtime execution, resolver currentness, install success, or package behavior.

## 5. Continuation-critical guards

```text
Tranche 1 remains historical accepted work
Tranche 2 remains separate / optional / NOT selected
GitHub owns Actions structure
Dependency owns source/environment/selection/membership meaning
CI owns CI-specific composition
Application owns sequencing

package present somewhere in uv.lock != selected-environment membership
.[dev] != .[mlx]
static dependency consumption != direct package exercise
static evidence + successful workflow != static↔runtime step correlation
successful CI != exact changed version observed
resolver satisfiability != behavioral compatibility
missing/ambiguous evidence != negative fact
```

## 6. Cluster 5 — CI migration to typed consumption evidence

**Status:** IMPLEMENTED / VALIDATION PENDING  
**Source/test implementation point before this WM update:** `f7fcd5e2dad98e3ab3ac59a1950cfb6d79cb0099`

### 6.1 Owned proposition

Cluster 5 answers:

> How should CI combine successful exact-head runtime authority with static changed-dependency consumption while preserving direct changed-package exercise as an independent stronger proposition?

The new path preserves three axes:

```text
RUNTIME AUTHORITY
successful exact-head workflow/job evidence?

STATIC CONSUMPTION
changed dependency belongs to a statically declared CI dependency environment?

STATIC DIRECT EXERCISE
direct package invocation occurs after supported consumption in the same static job?
```

### 6.2 New dependency-side S011 comparison primitive

Created:

```text
src/upgradepilot/dependency/environment_membership.py
```

This keeps extras/groups semantics out of CI. It compares source-established project environment identity with Cluster-3 selectors:

```text
affected extra mlx + selected mlx       → member
affected extra mlx + --all-extras       → member
affected extra mlx + selected dev       → not_established
project-root mismatch                    → unresolved
```

Equivalent dependency-group comparisons are supported by normalized group identity.

`not_established` is not runtime absence; it means the visible selector does not establish selection of the affected environment.

### 6.3 New CI static consumption contract

Created:

```text
src/upgradepilot/ci/consumption.py
```

`StaticDependencyConsumptionEvidence` preserves:

```text
state = supported | not_established | unresolved
mechanism = direct_requirements | project_environment
normalized changed-package identity
exact workflow path/revision
job key
step source index
segment index
command
reason/detail
optional dependency/project source path
optional membership kind/witness path
```

`compose_project_environment_consumption(...)` maps dependency-owned membership into CI meaning:

```text
membership.member           → consumption.supported
membership.not_established  → consumption.not_established
membership.unresolved       → consumption.unresolved
```

The helper validates that the declaration belongs to the supplied observed selection and that selectors/package identity are coherent. It does not claim runtime execution.

### 6.4 Exact external-consumption rebinding

Implementation review exposed a critical provenance rule: externally composed project-environment evidence cannot be accepted merely because it names a familiar job.

The new static inspector therefore rebinds each external consumption to:

```text
same normalized changed package
same exact workflow path
same exact workflow revision
same readable static job key
same run-step source index
same command text
valid bounded segment index
```

Mismatch becomes an explicit static problem rather than silently attaching the evidence elsewhere.

### 6.5 New multi-job static CI inspection

`ci/workflow_commands.py` now provides:

```python
inspect_workflow_dependency_evidence(...)
```

while retaining legacy `inspect_workflow_commands(...)` temporarily for Cluster-6 migration.

The new path parses the accepted GitHub workflow IR and preserves across all readable local steps jobs:

```text
consumption evidence items
+ direct package invocation source locations
+ structural/source problems
```

It no longer rejects a workflow solely because several static jobs exist.

Requirements behavior uses only typed `RequirementsFileDependencyContext` values and the existing dependency-owned direct-install observer. Constraints/uv-lock/pyproject paths are never promoted into requirements installation evidence merely because they are file paths.

Typed requirements contexts are also checked against exact workflow head revision and normalized changed-package identity before use.

### 6.6 Consumption versus direct exercise

The new semantics deliberately change the old combined proposition:

```text
OLD
requirements install BEFORE direct package invocation
→ one combined supported path
```

into:

```text
NEW
requirements install
→ static consumption supported

supported consumption
+ later direct package invocation in same static job
→ direct exercise supported
```

Therefore:

```text
requirements install only
→ consumption supported
→ direct exercise not_established
```

This is a semantic clarification, not weaker evidence.

### 6.7 New CI coverage evaluator

`ci/dependency_exercise.py` now additionally provides:

```python
evaluate_dependency_ci_coverage(...)
```

and new coverage result types while retaining the old `evaluate_dependency_ci_exercise(...)` contract unchanged for temporary application compatibility.

Workflow result separates:

```text
coverage state
consumption state/reason/detail
 direct exercise state/reason/detail
selected consumption/execution commands
all consumption evidence
all invocation evidence
all static problems
```

Aggregate coverage state remains:

```text
supported_not_correlated
no_successful_ci
unresolved
```

Strongest Cluster-5 meaning:

```text
successful exact-head CI
+ supported static dependency consumption
→ supported_not_correlated
```

Direct package exercise is **not required** for CI dependency coverage.

### 6.8 Static↔runtime boundary remains intact

Multiple static jobs are now preserved rather than rejected, but no static job is joined to a runtime `WorkflowJob`.

Thus:

```text
supported static consumption
+ successful exact-head runtime workflow
!= exact consuming static step ran successfully
```

The strongest result remains explicitly `supported_not_correlated`. Static↔runtime job/step correlation remains optional Tranche 2 and is not implemented here.

### 6.9 S001 pressure encoded in focused tests

S001-shaped typed evidence now supports:

```text
uv sync --group docs
+ exact membership witness
  mkdocs-llmstxt → beautifulsoup4 → soupsieve
+ successful exact-head CI
→ consumption supported
→ CI coverage supported_not_correlated
→ direct Soup Sieve exercise not_established
```

This is the intended result: transitive environment consumption does not manufacture a direct Soup Sieve invocation claim.

### 6.10 S011 pressure encoded in focused tests

S011-shaped evidence now preserves:

```text
affected environment = mlx
workflow selects = dev
→ membership not_established
→ project-environment consumption not_established
+ successful exact-head CI
→ CI coverage unresolved / not established
```

Green CI therefore does not become evidence that the changed `mlx` environment was consumed.

### 6.11 Requirements compatibility and added generality

Focused tests preserve the accepted old case:

```text
pip install -r requirements-dev.txt
then pytest
→ consumption supported
→ direct exercise supported
```

and add the newly representable weaker-but-useful case:

```text
pip install -r requirements-dev.txt
without direct changed-package invocation
→ consumption supported
→ direct exercise not_established
```

Multiple static jobs are preserved, constraints are not promoted to install evidence, and supported workflows do not erase weaker workflow results/problems.

### 6.12 Test surface added

New focused tests:

```text
tests/test_project_source_environment_membership.py
tests/test_ci_dependency_coverage.py
tests/test_workflow_dependency_evidence.py
```

Updated:

```text
tests/test_source_topology.py
```

Pressure includes:

- matching/mismatching optional extras and dependency groups;
- S011 `dev != mlx`;
- requirements consumption with and without direct exercise;
- multi-job static workflows;
- S001-shaped transitive environment consumption;
- no-successful-CI precedence;
- exact external workflow-revision/step binding;
- constraints non-promotion;
- heterogeneous workflow evidence preservation;
- source-topology ownership.

### 6.13 Transitional compatibility boundary

Cluster 5 intentionally leaves the ordinary application on the legacy evaluator for now:

```text
investigation.py
→ direct_requirements_install_path
→ evaluate_dependency_ci_exercise(...)
```

The new typed CI path is implemented and tested independently. Cluster 6 owns migration of ordinary orchestration/CLI plus actual S001/S011/S005 end-to-end pressure.

This separation prevents Cluster 5 from pulling repository acquisition/application sequencing into a CI contract migration.

### 6.14 Deliberate non-claims

Cluster 5 still does not establish:

```text
static job ↔ runtime job correlation
static step ↔ runtime step correlation
consuming command actually executed
installation/environment formation succeeded
exact proposed version was installed or imported
transitive dependency behavior was exercised
resolver currentness/satisfiability
compatibility/safety/action
```

### 6.15 Validation gate

Cluster 5 is not complete until the following are observed green on synchronized `main`:

1. import smoke for new dependency/CI modules;
2. focused project-membership / static-consumption / coverage tests;
3. legacy requirements CI tests;
4. nearest dependency selection/membership/workflow/application regressions;
5. complete deterministic product suite;
6. aligned `HEAD == origin/main` and clean worktree.

**Do not start Cluster 6 before this validation is recorded.**
