# B2 Dependency Environment and CI Consumption Evidence — Implementation Record

**Date opened:** 2026-08-16  
**Operation:** bounded implementation of [`../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md)  
**Result classification:** IN PROGRESS — CLUSTER 4 ACTIVE / DESIGN FROZEN BEFORE SOURCE EDIT  
**Execution branch:** `main`  
**Validated Cluster-0 baseline:** `7444324e511b1e6fb49e6dba0bac371272bff7ba`  
**Validated Cluster-1 implementation revision:** `ef8b4aa623bb53356b0969d099d2e32ee250b3e9`  
**Validated Cluster-2 implementation revision:** `f3e226a27216f75a689b73acbc4404cafb53f1c1`  
**Validated Cluster-3 implementation revision:** `82fdf314e3361f90ab8fd3862247d4bd895a440d`

## 1. Purpose and operating mode

Preserve the single progressive implementation, debugging, validation, learning, and decision trail for the selected Dependency Environment and CI Consumption Evidence responsibility. `../MEMORY.md` remains the sole live-state/continuation owner.

Core proof ladder:

```text
trusted dependency transition
!= dependency-environment membership
!= static workflow environment selection/consumption
!= runtime execution/success
!= exact-version witness
!= package exercise
!= behavioral compatibility/safety/action
```

## 2. Learning-by-building / source-documentation mode

Before each material source change, record the exact responsibility/proof question; after it, record what changed, why, what the output means, what it deliberately does not mean, and the validation evidence.

New/materially modified source follows `../OPERATING_GUIDE.md`: meaningful docstrings/comments explain ownership, proof boundaries, invariants, abstention, and deliberate non-claims rather than narrating syntax.

## 3. Implementation checklist

- [x] **Cluster 0 — synchronize, freeze, and validate baseline**
- [x] **Cluster 1 — bounded dependency-environment evidence contract**
- [x] **Cluster 2 — exact `pyproject.toml` optional-extra transition evidence**
- [x] **Cluster 3 — bounded project-environment selection semantics**
- [ ] **Cluster 4 — bounded `uv.lock` selected-environment membership/reachability** — ACTIVE
- [ ] **Cluster 5 — CI migration to typed consumption evidence**
- [ ] **Cluster 6 — application/CLI integration + S001/S011/S005 pressure**
- [ ] **Cluster 7 — AUDIT-004 resolver-satisfiability reassessment gate**
- [ ] **Cluster 8 — regression, acceptance, STOP/REVIEW**

A checked cluster means code plus applicable focused/nearest/full validation is green. Code presence alone is insufficient.

## 4. Continuation-critical guards

```text
Tranche 1 remains accepted historical foundation; do not reopen it
Tranche 2 remains separate and not selected
GitHub owns GitHub Actions source structure
Dependency owns dependency/project selection meaning
CI owns CI-specific composition
Application owns sequencing

package present somewhere in uv.lock != member of every selected environment
.[dev] != .[mlx]
static environment selection != runtime environment formation
static selection != command execution/success
changed dependency consumed != changed package exercised
resolver-satisfiable != behavioral compatibility
missing/ambiguous evidence != negative fact
```

## 5. Cluster 0 — green baseline

**Status:** COMPLETED / GREEN  
**Validated baseline:** `7444324e511b1e6fb49e6dba0bac371272bff7ba`

```text
complete suite: 435 tests / OK
```

## 6. Cluster 1 — bounded dependency-environment evidence contract

**Status:** COMPLETED / GREEN  
**Validated revision:** `ef8b4aa623bb53356b0969d099d2e32ee250b3e9`

Stored truth became typed dependency source contexts. `direct_requirements_install_path` remains only as a derived compatibility projection.

```text
complete suite: 439 tests / OK
```

## 7. Cluster 2 — exact pyproject optional-extra transition evidence

**Status:** COMPLETED / GREEN  
**Validated revision:** `f3e226a27216f75a689b73acbc4404cafb53f1c1`

S011 can now produce:

```text
numpy 1.26.4 → 2.4.6
+
PyprojectOptionalExtraDependencyContext(extra="mlx")
```

using exact base/head source, strong provenance, `tomllib`, `packaging.Requirement`, conservative comparison, and neutral handling of unrelated pyproject metadata edits.

```text
complete suite: 452 tests / OK
```

## 8. Cluster 3 — bounded project-environment selection semantics

**Status:** COMPLETED / GREEN  
**Validated revision:** `82fdf314e3361f90ab8fd3862247d4bd895a440d`

Cluster 3 established only the static selection side of the later consumption proposition:

```text
RunStepDefinition
+ exact project file path
+ effective working-directory context
→ observed | not_observed | unresolved
→ typed project-environment selection declarations
```

Accepted examples:

```text
pip install -e ".[dev]"
→ OptionalExtraSelector("dev")

uv sync --group docs --all-extras
→ DependencyGroupSelector("docs")
→ AllOptionalExtrasSelector()
```

New shared `dependency/workflow_context.py` owns effective working-directory precedence, safe repository-relative path resolution, and bounded shell segmentation. `dependency/direct_install.py` consumes those helpers while preserving its narrow direct-requirements semantics.

Cluster 3 also preserves normalized environment-name identity, distinguishes uv options from `uv run` child-command arguments, binds literal project roots, and leaves dynamic/default/ambiguous selection unresolved.

User-observed validation:

```text
complete deterministic suite: 476 tests / OK
HEAD:                         82fdf314e3361f90ab8fd3862247d4bd895a440d
origin/main:                  same
worktree:                     clean
```

## 9. Cluster 4 — bounded uv selected-environment membership/reachability

**Status:** ACTIVE — design/proof rule frozen before source mutation

### 9.1 Owned proposition

Cluster 4 answers only:

> Given exact-head uv project metadata, exact-head `uv.lock`, one independently established changed package from `UvLockDependencyContext`, and one static uv project-environment selection declaration, can UpgradePilot establish that the changed package is directly or transitively reachable from an explicitly selected dependency group/optional extra?

Target result semantics:

```text
member
├─ direct | transitive
├─ selected root/group/extra evidence
└─ one exact normalized dependency path

not_established
→ bounded explicit selected roots were traversed completely without finding the target
  but this is NOT a repository/runtime absence claim

unresolved
→ source identity, project binding, lock structure, marker/fork ambiguity,
  selector semantics, or traversal safety is insufficient
```

The result remains static exact-source evidence. It does not establish resolver currentness, command execution, installation, or behavior.

### 9.2 Exact S001 pressure

Frozen evidence:

```text
repository: pydantic/pydantic
head: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
project: pyproject.toml
lock: uv.lock
workflow: .github/workflows/ci.yml
selected group: docs
changed package: soupsieve 2.6 → 2.8.4
```

Exact project metadata contains `[dependency-groups].docs`, including `mkdocs-llmstxt`. Exact lock evidence contains:

```text
workspace package pydantic
→ package.dev-dependencies.docs
→ mkdocs-llmstxt

mkdocs-llmstxt
→ beautifulsoup4

beautifulsoup4
→ soupsieve
```

Therefore the required proof path is genuinely transitive:

```text
docs
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

This is the concrete reason Cluster 4 cannot use repository-wide lock presence or direct-group string matching.

### 9.3 Exact source identity requirements

The first implementation will require all of the following before traversal:

1. `UvLockDependencyContext.repository` matches both exact source files;
2. `UvLockDependencyContext.revision` matches exact `pyproject.toml` and exact `uv.lock` revisions;
3. the supplied lock path matches the context source-evidence path;
4. project path is normalized repository-relative `pyproject.toml`;
5. declaration manager is `uv` and its bound `project_root` matches the supplied project path;
6. lock schema remains within the currently admitted uv schema boundary;
7. one exact workspace package record can be bound to the project root through its editable/virtual source path.

A source mismatch is unresolved, not silently repaired.

### 9.4 Project metadata versus lock responsibilities

Use both exact project and lock evidence, but keep their roles distinct:

```text
pyproject.toml
→ validates selected group/extra identity exists in exact project metadata

workspace package record in uv.lock
→ resolved group/extra root package entries

package dependency records in uv.lock
→ exact locked transitive edges
```

This avoids reimplementing full PEP 735 include-group expansion merely to recover roots already materialized by uv in `package.dev-dependencies`, while still requiring the selected environment identity to exist in the exact project metadata.

This cross-file consistency does **not** prove that the lock is freshly resolver-current against metadata. AUDIT-004 / Cluster 7 retains that separate question.

### 9.5 Initial admitted selectors

Membership evaluation will consume the explicit positive selectors already produced by Cluster 3:

```text
OptionalExtraSelector(name)
DependencyGroupSelector(name, mode=include|only)
AllOptionalExtrasSelector()
AllDependencyGroupsSelector()
```

Only explicitly represented positive selector roots are traversed.

Important consequence:

```text
uv sync --group docs
```

can prove positive reachability from `docs`, but failure to reach a package from the explicit `docs` roots is only `not_established`; it is not proof that uv's complete runtime environment excludes that package because default/base project semantics may add other roots.

### 9.6 Lock graph boundary

For each package record, the bounded graph uses only admitted `dependencies` entries. Dependency entries may identify a target by normalized package name and may carry marker/version/source/extra disambiguation metadata.

Universal-lock safety rule:

- an unmarked, uniquely identifiable edge can be traversed normally;
- a marked edge may establish a positive path only if the target is reached without needing to assert that the marker is true for an unknown runtime context; otherwise the branch remains conditional/unresolved;
- if a dependency name maps to several lock records and the edge does not deterministically identify one branch, do not union their outgoing dependencies;
- if every candidate repeated record has structurally equivalent outgoing dependency identity, traversal may safely continue through that common structure; otherwise the path is unresolved;
- package presence elsewhere in the universal lock is never sufficient.

The first implementation should prefer explicit unresolved over implementing a marker evaluator.

### 9.7 Direct versus transitive membership

Definitions for this bounded proof:

```text
direct
= changed normalized package is itself one explicit selected group/extra root

transitive
= changed normalized package is reached through >=1 locked package dependency edge
```

Preserve one deterministic witness path for explanation, for example:

```text
selected group docs
root mkdocs-llmstxt
path mkdocs-llmstxt → beautifulsoup4 → soupsieve
```

### 9.8 Traversal safety

The graph walker must be iterative/bounded and cycle-safe. Initial proportional guards:

```text
visited normalized/record states bounded
path depth bounded
cycle revisits skipped
```

Crossing a bound yields `unresolved`; it must not become a negative result.

### 9.9 Explicit non-goals

Cluster 4 does not authorize:

```text
executing uv
uv workspace metadata execution
uv lock --check
marker/platform/Python expression evaluation
resolver/SAT implementation
full workspace command semantics
full tox/nox interpretation
runtime environment inspection
exact installed-version witness
CI result migration
package behavior exercise
```

Current uv documentation explicitly describes `uv.lock` as a universal/cross-platform lock and states that syncing installs a subset of lock packages selected by project groups/extras. The lock format itself is uv-specific and not a stable external interchange contract, so UpgradePilot keeps this parser intentionally bounded to the admitted schema/source shapes rather than claiming general uv compatibility.

### 9.10 Planned source slice

1. add a dependency-owned `uv_membership.py` responsibility;
2. parse exact project metadata only far enough to validate optional-extra/dependency-group selector identities;
3. parse exact lock into a bounded workspace-package/root/dependency graph representation;
4. bind exact project root to one workspace package record;
5. derive explicit selected roots from lock `optional-dependencies` / `dev-dependencies`;
6. perform bounded direct/transitive reachability with fork/marker abstention;
7. add generic direct/transitive/negative/unresolved tests plus a real S001-shaped regression;
8. update source topology;
9. stop for focused + nearest + full validation before Cluster 5.

No CI consumer migration is authorized inside this cluster.
