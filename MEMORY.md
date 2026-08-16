# UpgradePilot Current Memory

**Last updated:** 2026-08-16  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Selected responsibility:** **Dependency Environment and CI Consumption Evidence** under [`plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md).
- **Progressive implementation record:** [`working-memory/2026-08-16_B2-dependency-environment-ci-consumption-implementation.md`](working-memory/2026-08-16_B2-dependency-environment-ci-consumption-implementation.md).
- **Current status:** Cluster 0 COMPLETE/GREEN; Cluster 1 COMPLETE/GREEN; Cluster 2 COMPLETE/GREEN; **Cluster 3 IMPLEMENTED / VALIDATION PENDING**; Cluster 4 not started.
- **Fresh new-plan baseline:** `7444324e511b1e6fb49e6dba0bac371272bff7ba` — `435 tests / OK`, aligned, clean.
- **Validated Cluster-1 revision:** `ef8b4aa623bb53356b0969d099d2e32ee250b3e9` — `439 tests / OK`, aligned, clean.
- **Validated Cluster-2 revision:** `f3e226a27216f75a689b73acbc4404cafb53f1c1` — `452 tests / OK`, aligned, clean.
- **Current Cluster-3 source/test implementation point before WM/live-state docs:** `47b3098616146ddc63a5dd83650cbac94b08f92d` — validation not yet observed.
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
→ Cluster 3 — bounded project-environment selection IMPLEMENTED / VALIDATION PENDING
  Cluster 4 — uv.lock membership/reachability not started
  Cluster 5 — CI consumption migration not started
  Cluster 6 — application/real-case integration not started
  Cluster 7 — resolver-satisfiability gate not started
  Cluster 8 — acceptance/STOP-REVIEW not started
```

## Cluster 1 accepted result

Stored dependency truth is typed source context rather than the old format-specific `str | None` handoff. `direct_requirements_install_path` remains only as a derived compatibility projection until later CI migration.

## Cluster 2 accepted result

The dependency-analysis layer admits a bounded exact `pyproject.toml` optional-extra transition from complete exact base/head evidence.

S011 now reaches:

```text
numpy 1.26.4 → 2.4.6
+
PyprojectOptionalExtraDependencyContext(extra="mlx")
```

without claiming workflow selection, runtime formation, consumption, exercise, or compatibility.

### Cluster-2 validation truth

```text
complete deterministic suite: 452 tests / OK
HEAD:                         f3e226a27216f75a689b73acbc4404cafb53f1c1
origin/main:                  same
worktree:                     clean
```

## Cluster 3 implemented result — validation pending

Cluster 3 adds bounded **static project-environment selection** without crossing into membership or runtime evidence.

New shared dependency-side workflow context:

```text
src/upgradepilot/dependency/workflow_context.py
```

owns reusable static mechanics only:

```text
step > job defaults.run > workflow defaults.run > repository root
safe repository-relative path resolution
bounded shell-segment splitting
```

`dependency/direct_install.py` now consumes those helpers while preserving its old narrow direct-requirements semantics.

New observer:

```text
src/upgradepilot/dependency/environment_selection.py
```

Main result shape:

```text
RunStepDefinition
+ exact project file path
+ effective working-directory context
→ observed | not_observed | unresolved
→ typed static project-environment declarations
```

Admitted explicit selectors:

```text
OptionalExtraSelector(name)
DependencyGroupSelector(name, mode=include|only)
AllOptionalExtrasSelector()
AllDependencyGroupsSelector()
```

Real pressure currently represented:

```text
S011:
pip install -e ".[dev]"
→ selected optional extra = dev

S001-style:
uv sync --group docs --all-extras
→ selected group = docs
→ all optional extras explicitly selected
```

Important semantics/boundaries:

- local pip project paths must bind to the independently established project root;
- literal `uv --project` may bind a subproject safely;
- parent/nested uv project discovery is unresolved rather than guessed;
- dynamic project path/group/extra or dynamic effective working directory is unresolved;
- a bound uv command with no explicit extra/group selector is unresolved, not negative, because default-group semantics need project/config evidence;
- material negative/target-changing uv selectors are conservatively unresolved in this first rule;
- for `uv run`, only uv's option prefix before the child command is interpreted;
- extras/groups preserve source spelling and expose normalized comparison identity;
- static shell-segment index is source ordering only, not runtime command identity.

Cluster 3 does **not** establish:

```text
selected environment contains changed dependency
uv.lock membership/reachability
resolver satisfiability
runtime execution/success
environment formation
exact proposed version installed
package exercise
CI coverage/exercise result
```

## Immediate project action

**Validate Cluster 3. Do not start Cluster 4 yet.**

Required next action:

1. synchronize local `main`;
2. run Cluster-3 import smoke and focused selector/shared-context/direct-install tests;
3. run nearest dependency/CI/application regressions;
4. run the complete deterministic suite;
5. record exact HEAD/origin/worktree/test evidence in the progressive WM;
6. only after green validation mark Cluster 3 complete and consider Cluster 4.

Use strict validation inside a subshell so `set -u` does not leak into the interactive VS Code zsh prompt and trigger the unrelated `RPROMPT` hook warning.

## Continuation-critical guards

- `MEMORY.md` alone owns current continuation/latest verification;
- Cluster 2 remains the latest validated product point at `f3e226a27216f75a689b73acbc4404cafb53f1c1` until Cluster 3 receives observed validation;
- Cluster-3 implementation point is `47b3098616146ddc63a5dd83650cbac94b08f92d` before documentation commits;
- no Cluster-4 source mutation before Cluster-3 validation;
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
