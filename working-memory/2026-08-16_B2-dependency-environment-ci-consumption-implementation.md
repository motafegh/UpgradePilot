# B2 Dependency Environment and CI Consumption Evidence — Implementation Record

**Date opened:** 2026-08-16  
**Operation:** bounded implementation of [`../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md)  
**Result classification:** IN PROGRESS — CLUSTER 5 ACTIVE / DESIGN FROZEN BEFORE SOURCE EDIT  
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
- [ ] Cluster 5 — CI migration to typed consumption evidence — ACTIVE
- [ ] Cluster 6 — ordinary application/CLI integration + S001/S011/S005 pressure
- [ ] Cluster 7 — AUDIT-004 resolver-satisfiability reassessment gate
- [ ] Cluster 8 — full acceptance / STOP-REVIEW

## 4. Accepted machinery through Cluster 4

### Cluster 1

Stored dependency truth is typed `DependencySourceContext`, not the old `direct_requirements_install_path: str | None`. Requirements, constraints, uv-lock, pyproject optional-extra, and pyproject dependency-group shapes are distinct. The old requirements path survives only as a compatibility projection.

### Cluster 2

Exact `pyproject.toml` base/head evidence can establish a conservative exact pin transition inside one `[project.optional-dependencies]` extra. S011 now yields:

```text
numpy 1.26.4 → 2.4.6
+ PyprojectOptionalExtraDependencyContext(extra="mlx")
```

Unrelated pyproject metadata changes are neutral rather than false dependency failures.

### Cluster 3

Dependency-owned static workflow interpretation can preserve explicit project selectors such as:

```text
pip install -e ".[dev]"      → OptionalExtraSelector("dev")
uv sync --group docs          → DependencyGroupSelector("docs")
uv sync --all-extras          → AllOptionalExtrasSelector()
```

Shared `dependency/workflow_context.py` owns effective working-directory precedence and bounded shell/path mechanics. Selection is static declaration evidence only.

### Cluster 4

Exact project metadata + exact `uv.lock` + one static uv selector can establish:

```text
member(direct|transitive) | not_established | unresolved
```

Positive membership requires an unconditional exact witness path. Universal-lock marker/fork ambiguity is not unioned. S001 is accepted through:

```text
selected group docs
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

`not_established` remains weaker than package absence. Cluster 4 does not establish lock currentness, runtime execution, install success, or behavior.

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

**Status:** ACTIVE — semantic/result contract frozen before source mutation

### 6.1 Problem in the accepted pre-Cluster-5 CI path

Current `ci/dependency_exercise.py` still accepts:

```text
dependency
+ workflow runtime/static inputs
+ direct_requirements_install_path: str | None
```

and `ci/workflow_commands.py` currently treats the bounded static path as one combined proposition:

```text
direct requirements install
BEFORE
direct changed-package invocation
→ supported static dependency path
```

It also rejects workflows with more than one static job because the old rule used one-job structure as a substitute for missing static↔runtime job correlation.

That is now too narrow for admitted evidence:

```text
S001
uv sync --group docs
+ exact lock-backed soupsieve membership
→ dependency consumption can be supported
→ direct soupsieve invocation is not required

S011
changed environment = mlx
workflow selects dev
→ successful CI exists
→ changed mlx environment consumption is not established
```

### 6.2 Cluster-5 owned proposition

> How should CI combine successful exact-head runtime authority with static dependency consumption evidence while preserving direct changed-package exercise as an independent stronger proposition?

The new path must represent three independent axes:

```text
RUNTIME AUTHORITY
successful exact-head workflow/job evidence?

STATIC CONSUMPTION
changed dependency is included by a statically declared CI dependency environment?

STATIC DIRECT EXERCISE
changed package is directly invoked after a supported consumption in the same static job?
```

### 6.3 Selected CI result semantics

Static consumption state:

```text
supported
not_established
unresolved
```

Static direct-exercise state:

```text
supported
not_established
unresolved
```

Workflow/aggregate CI coverage state retains the existing runtime/static guard:

```text
supported_not_correlated
no_successful_ci
unresolved
```

Meaning of strongest state after this migration:

```text
successful exact-head CI evidence exists
+
static changed-dependency consumption is supported
→ supported_not_correlated
```

It does **not** require direct package exercise and does **not** claim the exact static consuming step executed successfully.

### 6.4 CI-owned static consumption evidence contract

Introduce a small CI-specific evidence record for one static job/step/segment consumption proposition. It must preserve at least:

```text
state
mechanism = direct_requirements | project_environment
job_key
step_source_index
segment_index
command
reason/detail
optional source path
optional membership kind/witness path
```

For project-environment consumption, CI composes already-established dependency facts rather than parsing package-manager/project metadata itself:

```text
ProjectEnvironmentSelectionObservation
+ one ProjectEnvironmentSelectionDeclaration
+ UvSelectedEnvironmentMembership
→ CI static consumption evidence
```

Mapping:

```text
membership.member           → consumption.supported
membership.not_established  → consumption.not_established
membership.unresolved       → consumption.unresolved
```

The composition must validate that the declaration/selectors/source location actually correspond; internal mismatches are not silently accepted.

### 6.5 Requirements preservation

The new static workflow path continues to use dependency-owned `observe_direct_installation_declaration()` for each trusted `RequirementsFileDependencyContext`.

A visible direct requirements install is itself sufficient for:

```text
static dependency consumption = supported
```

A later direct package invocation is a separate stronger axis:

```text
requirements consumption supported
+
direct changed-package invocation later in same static job
→ direct exercise supported
```

Thus old successful install→invocation cases remain supported, while the new model can additionally preserve consumption even if direct exercise is absent.

Constraints contexts never become install evidence merely because a path exists.

### 6.6 Multiple static jobs

The new path will no longer reject an entire workflow solely because it contains several static jobs.

Instead:

```text
all readable static jobs
→ preserve per-job consumptions and direct invocations
→ compare ordering only within the same static job
```

Runtime workflow/job evidence remains separate. Because Cluster 5 still does not join a static job to a runtime `WorkflowJob`, any supported result remains `supported_not_correlated`.

This is not Tranche 2 by stealth; it is precisely the explicit non-correlation guard.

### 6.7 Workflow static inspection shape

Add a new static inspection entry alongside the legacy compatibility function. It should return:

```text
consumption evidence items
+ direct package invocation locations
+ structural problems that make an otherwise material path unresolved
```

Provider YAML parsing remains in `github.workflow_definition`; requirements semantics remain in `dependency.direct_install`; project environment semantics remain in dependency-owned Cluster-3/4 types.

CI only owns ordering and composition.

### 6.8 Transitional compatibility boundary

Cluster 5 may retain the old `evaluate_dependency_ci_exercise(... direct_requirements_install_path=...)` / `inspect_workflow_commands()` surface temporarily so ordinary `investigation.py` and CLI remain green until Cluster 6.

The **new CI path**, however, must use typed source contexts and typed consumption evidence rather than requiring the old string handoff.

Cluster 6 owns migration of ordinary application orchestration and end-to-end S001/S011 pressure. Do not pull exact project/lock acquisition into Cluster 5 merely to make application integration happen early.

### 6.9 Heterogeneous evidence preservation

Per-workflow results remain preserved even when one workflow supports coverage and another is weaker or has no successful CI. Aggregate success may select the strongest supported workflow but must not erase weaker workflow results.

### 6.10 Deliberate non-goals

Cluster 5 does not authorize:

```text
ordinary application acquisition of pyproject/uv.lock for S001
full S001/S011 CLI result migration
static↔runtime job/step correlation
runtime logs
exact installed-version witness
resolver execution or uv lock --check
package behavior inference from transitive consumption
final compatibility/action synthesis
```

### 6.11 Planned implementation slice

1. add CI-owned typed static consumption evidence + project-environment composition helper;
2. add new multi-job static workflow inspection using typed requirements contexts and external project-environment consumption evidence;
3. separate static consumption from direct package invocation/order;
4. add new CI coverage evaluator using typed source contexts while retaining exact-head runtime authority and `supported_not_correlated` guard;
5. preserve legacy API temporarily for Cluster-6 migration;
6. add focused tests for requirements consumption-with/without exercise, S001-shaped project-environment consumption, S011-shaped non-consumption, multiple jobs, heterogeneous workflows, unresolved evidence, and no-successful-CI precedence;
7. run nearest legacy regressions and full suite;
8. stop before Cluster 6.
