# UpgradePilot Current Memory

**Last updated:** 2026-08-16  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Selected responsibility:** **Dependency Environment and CI Consumption Evidence** under [`plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md).
- **Progressive implementation record:** [`working-memory/2026-08-16_B2-dependency-environment-ci-consumption-implementation.md`](working-memory/2026-08-16_B2-dependency-environment-ci-consumption-implementation.md).
- **Current status:** Cluster 0 COMPLETE/GREEN; Cluster 1 COMPLETE/GREEN; **Cluster 2 IMPLEMENTED / VALIDATION PENDING**; Cluster 3 not started.
- **Fresh new-plan baseline:** `7444324e511b1e6fb49e6dba0bac371272bff7ba` — `435 tests / OK`, aligned, clean.
- **Validated Cluster-1 revision:** `ef8b4aa623bb53356b0969d099d2e32ee250b3e9` — `439 tests / OK`, aligned, clean.
- **Current Cluster-2 source/test implementation point before WM/live-state docs:** `78d0a8f22b7d3c2d9c630a9647a8854cbcdad6c5` — validation not yet observed.
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
!= static consumption declaration
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
→ Cluster 2 — exact pyproject optional-extra transition IMPLEMENTED / VALIDATION PENDING
  Cluster 3 — project-environment selection not started
  Cluster 4 — uv.lock membership/reachability not started
  Cluster 5 — CI consumption migration not started
  Cluster 6 — application/real-case integration not started
  Cluster 7 — resolver-satisfiability gate not started
  Cluster 8 — acceptance/STOP-REVIEW not started
```

## Cluster 1 accepted result

Stored dependency truth is now typed source context rather than the old format-specific `str | None` handoff:

```text
RequirementsFileDependencyContext
ConstraintsFileDependencyContext
UvLockDependencyContext
PyprojectOptionalExtraDependencyContext
PyprojectDependencyGroupContext
```

`direct_requirements_install_path` remains only as a derived compatibility projection until later CI migration.

S001 `uv.lock` evidence therefore survives as `UvLockDependencyContext(...)` instead of collapsing to an undifferentiated `None`.

## Cluster 2 implemented result — validation pending

The dependency-analysis layer now has a bounded exact `pyproject.toml` optional-extra source rule.

Real S011 pressure:

```text
dragfly/dictare PR #34
base 9921be73b4a55ba54b7b1f46ba424ada0d38aaa7
head 62d65da86f902d4b54a9d87e9ced5ff2e1f61e55
[project.optional-dependencies].mlx
numpy==1.26.4 → numpy==2.4.6
```

Implemented flow:

```text
modified pyproject.toml
→ exact base/head RepositoryTextFile
→ strong provenance validation
→ tomllib
→ packaging.Requirement for optional-dependency entries
→ conservative optional-extra comparison
→ ExtractedDependencyVersionChange + source-established extra
→ PR-wide DependencyVersionChange
→ PyprojectOptionalExtraDependencyContext(extra="mlx")
```

Important boundaries:

- unchanged general PEP 508 requirements may coexist with the changed exact pin;
- only one removed + one added requirement in the same extra is admitted;
- package/extras/marker/direct-reference identity must remain stable;
- changed pair must be exactly one non-wildcard `==version` on each side;
- multiple changes, cross-extra moves, marker/extras changes, direct references, repeated package records, malformed structures, and non-exact specifier changes abstain explicitly;
- unrelated `pyproject.toml` metadata edits are **neutral** to dependency comparison rather than false dependency failures;
- absence of an admitted PEP 621 optional-dependency surface is neutral; malformed present surfaces remain problems.

Cluster 2 does **not** establish workflow selection, environment formation, CI consumption, runtime exact-version observation, package exercise, or compatibility.

## Immediate project action

**Validate Cluster 2. Do not start Cluster 3 yet.**

Required next action:

1. synchronize local `main`;
2. run focused pyproject extractor/analysis/contract/topology tests;
3. run nearest dependency/CI/application regressions;
4. run the complete deterministic suite;
5. record exact HEAD/origin/worktree/test evidence in the progressive WM;
6. only after green validation mark Cluster 2 complete and enter Cluster 3.

## Continuation-critical guards

- `MEMORY.md` alone owns current continuation/latest verification;
- Cluster 1 remains validated at `ef8b4aa623bb53356b0969d099d2e32ee250b3e9` until Cluster 2 receives its own observed validation;
- current Cluster-2 implementation point is `78d0a8f22b7d3c2d9c630a9647a8854cbcdad6c5` before documentation commits;
- no Cluster-3 source mutation before Cluster-2 validation;
- Tranche 1 remains historical accepted work; do not retroactively enlarge it;
- Tranche 2 remains optional/separate/not selected;
- GitHub owns GitHub Actions structure; Dependency owns source/environment meaning; CI owns CI-specific composition; application owns sequencing;
- `dependency/direct_install.py` remains narrow;
- package present in `uv.lock` != selected environment membership;
- `.[dev]` != `.[mlx]`;
- static consumption declaration != runtime execution/success;
- dependency consumed != behavior exercised;
- resolver satisfiability != behavioral compatibility;
- missing/ambiguous evidence != negative fact;
- no generic package-manager/tox/shell/workflow engine without new evidence and explicit selection;
- new/materially modified source must carry proportional educational documentation.

## Learning state

Continue learning-by-building in small coherent blocks: explain the owned proposition/data flow, implement one bounded slice, validate, then append the same working-memory record. Passing AI-assisted code does not by itself establish mastery.
