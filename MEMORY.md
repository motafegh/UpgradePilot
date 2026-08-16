# UpgradePilot Current Memory

**Last updated:** 2026-08-16  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Selected responsibility:** **Dependency Environment and CI Consumption Evidence** under [`plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md).
- **Progressive implementation record:** [`working-memory/2026-08-16_B2-dependency-environment-ci-consumption-implementation.md`](working-memory/2026-08-16_B2-dependency-environment-ci-consumption-implementation.md).
- **Current status:** Cluster 0 COMPLETE/GREEN; Cluster 1 COMPLETE/GREEN; Cluster 2 COMPLETE/GREEN; **Cluster 3 COMPLETE/GREEN**; **Cluster 4 NOT STARTED / HOLD**.
- **Fresh new-plan baseline:** `7444324e511b1e6fb49e6dba0bac371272bff7ba` — `435 tests / OK`, aligned, clean.
- **Validated Cluster-1 revision:** `ef8b4aa623bb53356b0969d099d2e32ee250b3e9` — `439 tests / OK`, aligned, clean.
- **Validated Cluster-2 revision:** `f3e226a27216f75a689b73acbc4404cafb53f1c1` — `452 tests / OK`, aligned, clean.
- **Validated Cluster-3 revision:** `82fdf314e3361f90ab8fd3862247d4bd895a440d` — `476 tests / OK`, aligned, clean.
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

Primary real pressure:

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
  Cluster 4 — uv.lock membership/reachability NOT STARTED / HOLD
  Cluster 5 — CI consumption migration not started
  Cluster 6 — application/real-case integration not started
  Cluster 7 — resolver-satisfiability gate not started
  Cluster 8 — acceptance/STOP-REVIEW not started
```

## Accepted capability through Cluster 3

The dependency-analysis side can establish and preserve exact dependency-source/environment identity, including S011:

```text
numpy 1.26.4 → 2.4.6
+
PyprojectOptionalExtraDependencyContext(extra="mlx")
```

The new project-environment selection observer can separately establish visible static workflow selectors, including:

```text
pip install -e ".[dev]"
→ OptionalExtraSelector("dev")

uv sync --group docs --all-extras
→ DependencyGroupSelector("docs")
→ AllOptionalExtrasSelector()
```

Shared dependency-side workflow context now owns the reusable static working-directory/path mechanics so the direct-requirements observer and project-environment observer use one precedence/path-resolution rule.

Environment/selector spelling is preserved while normalized identities are exposed for later matching. `uv run` interpretation stops at uv's own option prefix; child-command flags are not uv selectors. Dynamic/ambiguous path/selector state remains unresolved rather than becoming a negative fact.

### Cluster-3 validation truth

The user ran the strict Cluster-3 validation in a subshell after synchronizing `main`. The block reached the complete-suite/final-state markers, therefore import smoke, focused tests, and nearest regressions passed.

```text
complete deterministic suite: 476 tests / OK
HEAD:                         82fdf314e3361f90ab8fd3862247d4bd895a440d
origin/main:                  same
worktree:                     clean
```

The prior VS Code/zsh `RPROMPT` warning did not recur; the subshell wrapper successfully kept `set -u` from leaking into the parent interactive shell.

Cluster 3 still does **not** establish selected-environment membership, uv lock reachability, resolver satisfiability, runtime execution/success, exact installed version, package exercise, or CI coverage/exercise.

## Immediate project action

**HOLD. Do not start Cluster 4 yet.**

When the user explicitly resumes, Cluster 4 will address only bounded `uv.lock` selected-environment membership/reachability.

Before source mutation, onboard the user on:

1. the exact S001 membership proposition;
2. what exact-head project metadata provides environment roots;
3. what exact-head `uv.lock` provides dependency edges;
4. direct versus transitive membership;
5. universal-lock marker/platform/Python fork ambiguity;
6. why package presence anywhere in the lock is insufficient;
7. traversal bounds/cycle safety and explicit unresolved conditions.

## Continuation-critical guards

- `MEMORY.md` alone owns current continuation/latest verification;
- Cluster 3 is validated green at `82fdf314e3361f90ab8fd3862247d4bd895a440d` with `476 tests / OK`;
- Cluster 4 is **not started** and no Cluster-4 source mutation is authorized until the user resumes;
- Tranche 1 remains historical accepted work; do not retroactively enlarge it;
- Tranche 2 remains optional/separate/not selected;
- GitHub owns GitHub Actions structure; Dependency owns source/environment meaning; CI owns CI-specific composition; application owns sequencing;
- `dependency/direct_install.py` remains narrow;
- package present in `uv.lock` != selected environment membership;
- `.[dev]` != `.[mlx]`;
- static selection/consumption declaration != runtime execution/success;
- dependency consumed != behavior exercised;
- resolver satisfiability != behavioral compatibility;
- missing/ambiguous evidence != negative fact;
- no generic package-manager/tox/shell/workflow engine without new evidence and explicit selection;
- new/materially modified source must carry proportional educational documentation.

## Learning state

Continue learning-by-building in small coherent blocks: explain the owned proposition/data flow, implement one bounded slice, validate, then append the same working-memory record. Passing AI-assisted code does not by itself establish mastery.
