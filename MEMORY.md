# UpgradePilot Current Memory

**Last updated:** 2026-08-16  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Selected responsibility:** **Dependency Environment and CI Consumption Evidence** under [`plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md).
- **Progressive implementation record:** [`working-memory/2026-08-16_B2-dependency-environment-ci-consumption-implementation.md`](working-memory/2026-08-16_B2-dependency-environment-ci-consumption-implementation.md).
- **Current status:** Clusters 0–3 COMPLETE/GREEN; **Cluster 4 IMPLEMENTED / VALIDATION PENDING**; Cluster 5 not started.
- **Fresh new-plan baseline:** `7444324e511b1e6fb49e6dba0bac371272bff7ba` — `435 tests / OK`, aligned, clean.
- **Validated Cluster-1 revision:** `ef8b4aa623bb53356b0969d099d2e32ee250b3e9` — `439 tests / OK`, aligned, clean.
- **Validated Cluster-2 revision:** `f3e226a27216f75a689b73acbc4404cafb53f1c1` — `452 tests / OK`, aligned, clean.
- **Validated Cluster-3 revision:** `82fdf314e3361f90ab8fd3862247d4bd895a440d` — `476 tests / OK`, aligned, clean.
- **Current Cluster-4 source/test implementation point before WM/live-state docs:** `9348a1094e040568a1ac9883e85953dc552133fe` — validation not yet observed.
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
!= static environment selection/consumption
!= resolver satisfiability
!= runtime execution/success
!= exact-version witness
!= package exercise
!= behavioral compatibility/safety/action
```

Primary pressure:

```text
S001 — uv locked-environment positive consumption
S011 — pyproject optional-extra non-formation/non-consumption
S005 — tox/uv mediated lock-consumption transfer pressure
```

## New-plan implementation status

```text
✓ Cluster 0 — synchronized/frozen green baseline
✓ Cluster 1 — bounded dependency-environment evidence contract
✓ Cluster 2 — exact pyproject optional-extra transition evidence
✓ Cluster 3 — bounded project-environment selection semantics
→ Cluster 4 — uv.lock membership/reachability IMPLEMENTED / VALIDATION PENDING
  Cluster 5 — CI consumption migration not started
  Cluster 6 — application/real-case integration not started
  Cluster 7 — resolver-satisfiability gate not started
  Cluster 8 — acceptance/STOP-REVIEW not started
```

## Accepted capability through Cluster 3

UpgradePilot can separately preserve:

```text
WHAT CHANGED / WHERE IT BELONGS
numpy 1.26.4 → 2.4.6
+ PyprojectOptionalExtraDependencyContext(extra="mlx")

WHAT STATIC WORKFLOW SELECTS
pip install -e ".[dev]"
→ OptionalExtraSelector("dev")

uv sync --group docs
→ DependencyGroupSelector("docs")
```

Cluster 3 does not itself establish package membership in those selected environments.

## Cluster 4 implemented result — validation pending

New dependency-owned source:

```text
src/upgradepilot/dependency/uv_membership.py
```

Main proposition:

```text
UvLockDependencyContext(changed package)
+
exact project metadata
+
exact uv.lock from same repository/revision
+
static uv selection declaration
↓
member(direct|transitive) | not_established | unresolved
```

### Real S001 structure

Exact S001 evidence at `aa2dc024d33f61cdef50bf1973ab5adf0a974f5a` provides:

```text
workflow:
uv sync --all-packages --group docs

project group docs contains:
mkdocs-llmstxt

lock-backed path:
mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve 2.8.4
```

So the intended S001 membership witness is transitive, not direct.

### Source and project binding

Before traversal, Cluster 4 validates:

- exact project/lock availability and normalized paths;
- repository/revision equality with `UvLockDependencyContext`;
- lock path/revision/blob/byte count against the exact source evidence that established the dependency transition;
- declaration project root against exact `pyproject.toml`;
- project `[project].name` and selected optional-extra/dependency-group names;
- one exact workspace package record bound through normalized project name plus editable/virtual source path relative to the lock workspace root.

### Selected roots and graph

Exact project metadata validates environment identity. The bound workspace record's:

```text
package.optional-dependencies
package.dev-dependencies
```

provides uv-materialized selected roots. Package `dependencies` provide transitive edges.

The graph preserves dependency-edge activated extras, because selecting a dependency such as `package[imaging]` can add outgoing optional-dependency roots.

### Universal-lock safety

Positive membership requires one unconditional witness path.

```text
marked dependency edge
OR package record with resolution-markers
OR unresolved repeated package record
→ conditional/ambiguous branch
→ do not union or assume active
```

If another unconditional path reaches the target, positive membership is still allowed. If no unconditional witness exists and any selected branch is conditional/ambiguous, the result is `unresolved`.

Only a complete explicit-root traversal without ambiguity can return `not_established`, and that state is not repository/runtime absence.

Traversal is iterative/cycle-safe and bounded by:

```text
10,000 visited package+activated-extra states
100 path depth
```

Crossing a bound yields `unresolved`.

### Tests added

Cluster-4 test pressure covers:

- S001-shaped transitive docs path;
- direct membership;
- `not_established` proof boundary;
- marker-dependent branches;
- package-level `resolution-markers`;
- activated extras;
- optional-extra/group/all-category roots;
- repeated-record ambiguity and version disambiguation;
- cycle safety;
- nested workspace binding;
- lock blob/source mismatch;
- source-topology ownership.

Cluster 4 still does **not** establish lock freshness/currentness, resolver satisfiability, runtime execution/success, exact installed version, behavioral exercise, CI coverage/exercise, or static↔runtime correlation.

## Immediate project action

**Validate Cluster 4. Do not start Cluster 5 yet.**

Required next action:

1. synchronize local `main`;
2. run Cluster-4 import smoke and focused uv membership/universal-lock/topology tests;
3. run nearest uv-lock/environment-selection/dependency/CI/application regressions;
4. run complete deterministic product suite;
5. record exact HEAD/origin/worktree/test evidence in progressive WM;
6. only after green validation mark Cluster 4 complete and enter Cluster 5.

Use strict validation inside a subshell so `set -u` remains isolated from the interactive VS Code zsh prompt.

## Continuation-critical guards

- `MEMORY.md` alone owns current continuation/latest verification;
- Cluster 3 remains latest validated product point at `82fdf314e3361f90ab8fd3862247d4bd895a440d` until Cluster 4 receives observed validation;
- Cluster-4 implementation point is `9348a1094e040568a1ac9883e85953dc552133fe` before documentation commits;
- no Cluster-5 source mutation before Cluster-4 validation;
- Tranche 1 remains historical accepted work;
- Tranche 2 remains optional/separate/not selected;
- GitHub owns GitHub Actions structure; Dependency owns source/environment meaning; CI owns CI-specific composition; application owns sequencing;
- package present anywhere in `uv.lock` != selected-environment membership;
- static selection/consumption declaration != runtime execution/success;
- dependency consumed != behavior exercised;
- resolver satisfiability/currentness remains separate;
- missing/ambiguous evidence != negative fact;
- no generic package-manager/tox/shell/workflow engine without new evidence and explicit selection;
- new/materially modified source must carry proportional educational documentation.

## Learning state

Continue learning-by-building in small coherent blocks: explain the owned proposition/data flow, implement one bounded slice, validate, then append the same working-memory record. Passing AI-assisted code does not by itself establish mastery.
