# B2 Dependency Environment and CI Consumption Evidence — Implementation Record

**Date opened:** 2026-08-16  
**Operation:** bounded implementation of [`../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md)  
**Result classification:** IN PROGRESS — CLUSTER 5 COMPLETE/GREEN; CLUSTER 6 NOT STARTED  
**Execution branch:** `main`

## 1. Validation history

```text
Cluster 0  7444324e511b1e6fb49e6dba0bac371272bff7ba   435 tests / OK
Cluster 1  ef8b4aa623bb53356b0969d099d2e32ee250b3e9   439 tests / OK
Cluster 2  f3e226a27216f75a689b73acbc4404cafb53f1c1   452 tests / OK
Cluster 3  82fdf314e3361f90ab8fd3862247d4bd895a440d   476 tests / OK
Cluster 4  cf2b4ca1a78c6cd008a9c55cb502ed5072647561   490 tests / OK
Cluster 5  bfdfd4257574f85cc3a2d094bf46a37ad6373dea   508 tests / OK
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
- [x] Cluster 5 — CI migration to typed consumption evidence — COMPLETE/GREEN
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

**Status:** COMPLETE / GREEN  
**Source/test implementation point before this WM update:** `f7fcd5e2dad98e3ab3ac59a1950cfb6d79cb0099`  
**Validated current-main point:** `bfdfd4257574f85cc3a2d094bf46a37ad6373dea` — `508 tests / OK`, `HEAD == origin/main`, clean worktree

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

### 6.15 Validation result — GREEN

On 2026-08-18 the documented strict validation block was run on synchronized `main` after the source-clarity calibration work. The sequence covered:

1. import smoke for the new dependency/CI modules;
2. focused project-membership / static-consumption / coverage tests;
3. legacy CI/workflow-command regressions;
4. nearest dependency selection/membership/workflow/application regressions;
5. the complete deterministic product suite;
6. final repository alignment/cleanliness.

Observed final evidence:

```text
Ran 508 tests in 0.096s
OK

HEAD        bfdfd4257574f85cc3a2d094bf46a37ad6373dea
origin/main bfdfd4257574f85cc3a2d094bf46a37ad6373dea
worktree    clean (`git status --short` emitted no entries)
```

No validation failure was observed. Cluster 5 is therefore accepted COMPLETE/GREEN at this revision. This authorizes later Cluster-6 work when selected, but does not itself start or implement Cluster 6.

### 6.16 Cluster-5 implementation journey and material findings

This subsection preserves the chronological engineering/reasoning trail that led to the final Cluster-5 design. These are not additional product claims; they explain why the implementation has its current boundaries.

#### Step A — old CI contract inspected before mutation

The starting CI contract was confirmed to be structurally tied to:

```text
direct_requirements_install_path: str | None
+
one static workflow job
+
direct requirements install before direct package invocation
```

The key finding was that the old result did not merely have a narrow input; it **collapsed two different propositions** into one supported path:

```text
changed dependency consumed
+
changed package directly invoked
```

That made a direct extension to uv/project environments unsafe because S001 can support consumption without a direct Soup Sieve invocation.

Decision:

```text
do not stretch the old combined result
→ introduce a parallel typed coverage path
→ retain legacy API until Cluster 6 migrates callers
```

#### Step B — one-job restriction identified as legacy, not a new invariant

`inspect_workflow_commands(...)` rejected any workflow with zero/multiple jobs because Tranche 1 lacked static↔runtime job correlation.

During Cluster-5 design this was classified as an artifact of the **legacy combined exercise rule**, not a reason to discard static evidence from real multi-job workflows such as S001.

Decision:

```text
new static inspector preserves all readable local steps jobs
+
records unreadable/reusable jobs as problems
+
does NOT correlate any static job to runtime
```

Therefore multi-job support does not secretly implement Tranche 2; strongest runtime/static result remains `supported_not_correlated`.

#### Step C — S011 exposed a missing dependency-domain relation

Clusters 2 and 3 independently provided:

```text
affected optional extra = mlx
selected optional extra = dev
```

but no typed primitive yet compared those two dependency-owned identities.

Putting `dev != mlx` logic directly inside CI would have violated ownership.

Decision:

```text
create dependency/environment_membership.py
→ compare affected source environment with selected environment
→ CI consumes only the resulting member/not_established/unresolved fact
```

This was a discovered prerequisite inside Cluster 5, not permission to build a general environment graph.

#### Step D — CI consumption became its own typed evidence object

Once consumption and exercise were separated, a bare Boolean/state was insufficient. CI needed to preserve the source location and proof provenance of the consuming declaration.

Decision:

```text
StaticDependencyConsumptionEvidence
```

with mechanism, package identity, workflow identity, job/step/segment location, command, source path, and optional membership witness.

This allows a later learner/debugger to answer **why** CI called something consumption rather than seeing only a final aggregate state.

#### Step E — exact external-evidence rebinding issue caught in pre-validation review

Project-environment consumption is composed from dependency-owned selection/membership evidence before CI static aggregation. Initial design pressure showed that accepting such an item merely because it named `job_key="docs"` would be unsafe:

```text
valid evidence from workflow A
+
workflow B also has job "docs"
→ must NOT attach automatically
```

The contract was tightened before validation to require exact rebinding to:

```text
changed normalized package
workflow path
workflow revision
job key
run-step source index
command text
segment index
```

This was a proof-integrity correction found during implementation review, not a user-test failure.

#### Step F — package-identity drift guard added after rebinding review

A second rebinding issue was identified after workflow identity was protected: evidence for one changed package could theoretically be reused while CI was evaluating another package unless normalized package identity travelled with the consumption record.

Decision:

```text
StaticDependencyConsumptionEvidence.normalized_package
```

is mandatory, and the static workflow inspector validates it against the current `DependencyVersionChange.normalized_package`.

Again, this was caught before the validation run; it should not be recorded later as a runtime/test regression.

#### Step G — exact static step/command rebinding added

Matching only workflow path/revision + job key was still not sufficient because several run steps in the same job may select different environments.

The inspector therefore verifies that the external consumption points to the same parsed `RunStepDefinition` and command text, with a bounded valid segment index.

This protects against accidentally moving a legitimate `docs` selection witness onto a different command in the same job.

#### Step H — heterogeneous evidence preservation corrected

During the semantic pass, another issue was identified:

```text
one job has supported consumption
another job is reusable/unreadable
```

If aggregate support simply selected the strongest item and discarded static problems, later learning/debugging would lose material weaker evidence.

Decision:

```text
WorkflowDependencyCoverageResult
preserves all consumptions
+ all invocations
+ all static problems
```

while aggregate state may still be `supported_not_correlated` when one valid supported path exists.

This follows the project rule that stronger evidence should not erase heterogeneous weaker evidence.

#### Step I — requirements compatibility protected through typed context, not raw path fallback

The legacy path previously accepted `direct_requirements_install_path`. In the new inspector, requirements consumption is derived only from:

```text
RequirementsFileDependencyContext
```

and the existing `observe_direct_installation_declaration(...)` primitive.

The implementation explicitly avoids treating these as installable requirements merely because they have paths:

```text
ConstraintsFileDependencyContext
UvLockDependencyContext
PyprojectOptionalExtraDependencyContext
```

A focused constraint non-promotion test was added for this reason.

#### Step J — direct exercise made dependent on source ordering, not on consumption existence alone

After separating the axes, direct invocation evidence is collected independently. It becomes `direct_exercise=supported` only when:

```text
same static job
+
supported consumption location
< later direct changed-package invocation location
```

A visible invocation before consumption, in another job, or without supported consumption does not become direct exercise.

This preserves the useful ordering semantics of the old rule without forcing exercise to be a prerequisite for consumption.

#### Step K — no-successful-CI precedence preserved independently

A workflow may have strong static consumption evidence while runtime CI failed or no successful exact-head job exists.

Cluster-5 tests explicitly preserve:

```text
static consumption = supported
runtime CI = not successful
→ aggregate CI state = no_successful_ci
```

The static fact remains visible in the workflow result instead of being erased.

#### Step L — S001 and S011 used as opposite semantic pressure

The implementation was intentionally tested against two opposite cases:

```text
S001
selected docs + transitive Soup Sieve membership
→ consumption supported
→ direct exercise not_established

S011
changed extra mlx + selected extra dev
→ consumption not_established
→ green CI does not upgrade it
```

These cases validate that the new contract is not simply a more permissive version of the old requirements rule; it can support a positive environment-consumption case and preserve a meaningful non-consumption case.

#### Step M — implementation stopped before ordinary application migration

A final scope check confirmed that `investigation.py` still projects dependency analysis back down to `direct_requirements_install_path` and calls the legacy evaluator.

This is intentional at the Cluster-5 boundary:

```text
Cluster 5
new CI contract + typed static/runtime composition exists independently

Cluster 6
ordinary orchestration acquires/composes real selection/membership evidence
and routes it into the new coverage evaluator
```

No application/CLI migration was pulled forward merely to make Cluster-5 unit tests look end-to-end.

### 6.17 Validation classification

The documented user validation gate has now run and passed without an observed product regression.

The corrections in Steps A–M were found during source/design consistency review before validation and remain classified as:

```text
implementation/design findings
NOT observed product regressions
NOT validation failures
```

Accepted state after validation:

```text
Cluster 5 = COMPLETE / GREEN at bfdfd4257574f85cc3a2d094bf46a37ad6373dea
Cluster 6 = NOT STARTED
```
