# UpgradePilot Current Memory

**Last updated:** 2026-08-16  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Selected responsibility:** **Dependency Environment and CI Consumption Evidence** under [`plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md).
- **Progressive implementation record:** [`working-memory/2026-08-16_B2-dependency-environment-ci-consumption-implementation.md`](working-memory/2026-08-16_B2-dependency-environment-ci-consumption-implementation.md).
- **Current status:** Clusters 0–4 COMPLETE/GREEN; **Cluster 5 NOT STARTED / HOLD**.
- **Fresh new-plan baseline:** `7444324e511b1e6fb49e6dba0bac371272bff7ba` — `435 tests / OK`, aligned, clean.
- **Validated Cluster-1 revision:** `ef8b4aa623bb53356b0969d099d2e32ee250b3e9` — `439 tests / OK`, aligned, clean.
- **Validated Cluster-2 revision:** `f3e226a27216f75a689b73acbc4404cafb53f1c1` — `452 tests / OK`, aligned, clean.
- **Validated Cluster-3 revision:** `82fdf314e3361f90ab8fd3862247d4bd895a440d` — `476 tests / OK`, aligned, clean.
- **Validated Cluster-4 revision:** `cf2b4ca1a78c6cd008a9c55cb502ed5072647561` — `490 tests / OK`, aligned, clean.
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
✓ Cluster 4 — bounded uv.lock selected-environment membership/reachability
  Cluster 5 — CI consumption migration NOT STARTED / HOLD
  Cluster 6 — application/real-case integration not started
  Cluster 7 — resolver-satisfiability gate not started
  Cluster 8 — acceptance/STOP-REVIEW not started
```

## Accepted capability through Cluster 4

UpgradePilot can now preserve and separately establish:

```text
WHAT CHANGED / WHERE IT BELONGS
numpy 1.26.4 → 2.4.6
+ PyprojectOptionalExtraDependencyContext(extra="mlx")

WHAT STATIC WORKFLOW SELECTS
pip install -e ".[dev]"
→ OptionalExtraSelector("dev")

uv sync --group docs
→ DependencyGroupSelector("docs")

WHETHER A UV-SELECTED ENVIRONMENT CONTAINS THE CHANGED PACKAGE
exact project metadata
+ exact uv.lock
+ selected uv group/extra
→ member(direct|transitive) | not_established | unresolved
```

### Cluster-4 accepted S001 result

Exact S001 structure at the admitted head supports the transitive witness:

```text
selected group docs
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

So Soup Sieve is not merely present somewhere in the universal lock; it is reachable from one explicit selected `docs` root through exact lock-backed dependency edges.

### Cluster-4 proof boundary

Positive membership requires one unconditional exact witness path. Marker-scoped edges, package-level `resolution-markers`, ambiguous repeated package records, source/project mismatches, or traversal-bound pressure remain `unresolved` unless another unconditional path already proves membership.

`not_established` means only that the bounded explicit roots were completely traversed without a witness. It is not proof that the package is absent from the repository, complete uv environment, or runtime installation.

Cluster 4 still does **not** establish lock freshness/currentness, resolver satisfiability, command execution, successful environment formation, exact installed version, behavioral exercise, CI coverage/exercise, or static↔runtime correlation.

### Cluster-4 validation truth

The user ran the strict Cluster-4 validation on synchronized `main`; the block reached complete-suite/final-state markers, so focused and nearest validation passed before the visible final result.

```text
complete deterministic suite: 490 tests / OK
HEAD:                         cf2b4ca1a78c6cd008a9c55cb502ed5072647561
origin/main:                  same
worktree:                     clean
```

## Immediate project action

**HOLD. Do not start Cluster 5 yet.**

When the user explicitly resumes, Cluster 5 will migrate CI away from the direct-requirements-only handoff and compose the typed evidence produced by Clusters 1–4.

Before source mutation, onboard the user on the CI distinction:

```text
static dependency consumption
!= static direct package exercise
!= runtime CI success
!= exact installed-version witness
```

Cluster 5 should preserve existing requirements behavior while adding source-aware environment consumption, heterogeneous weaker results, and explicit separation between consumption and package exercise.

## Continuation-critical guards

- `MEMORY.md` alone owns current continuation/latest verification;
- Cluster 4 is validated green at `cf2b4ca1a78c6cd008a9c55cb502ed5072647561` with `490 tests / OK`;
- Cluster 5 is **not started** and no Cluster-5 source mutation is authorized until the user resumes;
- Tranche 1 remains historical accepted work;
- Tranche 2 remains optional/separate/not selected;
- GitHub owns GitHub Actions structure; Dependency owns source/environment meaning; CI owns CI-specific composition; application owns sequencing;
- package present anywhere in `uv.lock` != selected-environment membership;
- static environment selection/consumption != runtime execution/success;
- dependency consumed != changed package behavior exercised;
- resolver satisfiability/currentness remains separate;
- missing/ambiguous evidence != negative fact;
- no generic package-manager/tox/shell/workflow engine without new evidence and explicit selection;
- new/materially modified source must carry proportional educational documentation.

## Learning state

Continue learning-by-building in small coherent blocks: explain the owned proposition/data flow, implement one bounded slice, validate, then append the same working-memory record. Passing AI-assisted code does not by itself establish mastery.
