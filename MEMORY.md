# UpgradePilot Current Memory

**Last updated:** 2026-08-16  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Selected responsibility:** **Dependency Environment and CI Consumption Evidence** under [`plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md).
- **Selection trigger:** Tranche-1 STOP/REVIEW learning against real S001/S011 evidence exposed that the direct-requirements-only CI rule cannot represent important real dependency-environment consumption paths.
- **Selected-plan status:** approved and selected; **implementation has not started yet**.
- **Tranche-1 status:** implementation and acceptance **COMPLETE / GREEN**; it remains historical accepted foundation and is not reopened by this selection.
- **Accepted GitHub Actions architecture:** [`docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md`](docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md).
- **Source ownership baseline:** [`docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](docs/architecture/ADR-0007-responsibility-based-python-subpackages.md).
- **Resolver-satisfiability review evidence:** [`audits/2026-08-16_AUDIT-004_uv-lock-resolution-satisfiability-evidence-boundary.md`](audits/2026-08-16_AUDIT-004_uv-lock-resolution-satisfiability-evidence-boundary.md).
- **Execution/learning/code-documentation rules:** [`OPERATING_GUIDE.md`](OPERATING_GUIDE.md).

### Selected post-Tranche-1 responsibility

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

Initial admitted pressure surface:

```text
requirements files
+
uv.lock / uv project groups and extras
+
pyproject.toml optional dependencies / dependency groups
```

Primary real cases:

```text
S001 — positive uv locked-environment consumption pressure
S011 — optional-extra non-formation/non-consumption pressure
S005 — transfer pressure for lock consumption mediated by tox/uv runner
```

Core evidence ladder remains:

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

## Phase-E / Tranche-1 historical status

```text
✓ Cluster 0 — synchronized green baseline
✓ Cluster 1 — PyYAML dependency/parser boundary
✓ Cluster 2 — typed static GitHub Actions workflow IR
✓ Cluster 3 — shared direct-install declaration observation
✓ Cluster 4 — Target migration / proof-strength correction
✓ Cluster 5 — CI migration / proof-claim narrowing
✓ Cluster 6 — repository-path reconciliation
✓ Cluster 7 — Tranche-1 acceptance gate
✓ Tranche-1 implementation / acceptance complete
✓ STOP / REVIEW milestone performed sufficiently to select the next responsibility

Tranche 2 — NOT SELECTED / NOT AUTHORIZED
```

The new selected responsibility solves a different problem from optional Tranche 2:

```text
NEW PLAN
Can UpgradePilot recognize the relevant dependency environment and establish a static consumption path?

TRANCHE 2
Can UpgradePilot correlate an already-identified static job/step to runtime job/step evidence?
```

Do not substitute one for the other and do not start Tranche 2 automatically.

## Final Tranche-1 verification truth

Accepted implementation revision:

```text
ef4283db0a7ce3eec75a56ccc5c07354015fd2e3
```

The user ran the requested fail-fast Tranche-1 acceptance gate. Because it reached its final acceptance marker, the environment/import smoke and every focused/nearest acceptance command passed before the complete-suite result.

Complete deterministic suite:

```text
Ran 435 tests in 0.090s
OK
```

Final accepted repository state:

```text
branch: main
HEAD: ef4283db0a7ce3eec75a56ccc5c07354015fd2e3
origin/main: ef4283db0a7ce3eec75a56ccc5c07354015fd2e3
worktree: clean

TRANCHE 1 ACCEPTANCE COMPLETE
ACCEPTED REVISION: ef4283db0a7ce3eec75a56ccc5c07354015fd2e3
```

Documentation, learning, audit, and plan commits after that accepted revision may advance `main`; they do not replace the accepted runtime/source validation point until the selected new implementation runs its own Cluster-0 baseline validation.

## Accepted Tranche-1 implementation foundation

```text
RepositoryTextFile
        ↓
bounded PyYAML parser boundary
        ↓
typed provider-owned GitHub Actions static workflow IR
        ↓
dependency-owned direct-install declaration observation
        ↓
   ┌───────────────┐
   ▼               ▼
Target            CI
static            static package path
configuration     + separate exact-head
interpretation    runtime run/job evidence
```

The evidence classes remain deliberately separate:

```text
static declaration != runtime execution != runtime success
```

### Target result

Target no longer owns a second workflow parser or generic direct-install matcher. Static workflow evidence reports declaration/configuration strength rather than claiming runtime environment formation.

### CI result

CI no longer owns a second workflow parser or direct-install matcher. Its strongest current pre-new-plan state is:

```text
supported_not_correlated
```

meaning:

```text
successful exact-head runtime workflow/job evidence
+
ordered exact-head static install→package-invocation path
!= matched static commands observed executing/succeeding at runtime
```

The new plan may broaden **static dependency-environment consumption recognition** while preserving this non-correlation guard.

### Repository path result

Repository-relative structural validation has one source-neutral active owner in `repository_path.py`. GitHub repository acquisition retains provider-specific URL/acquisition/provenance behavior rather than duplicating path structure rules.

## Why the new responsibility was selected

### S001 pressure

The canonical dependency change is established from exact base/head `uv.lock` evidence, but the current CI evaluator receives:

```text
direct_requirements_install_path = None
```

and stops before it can reason about `uv` project/group consumption. A useful product needs a bounded way to distinguish:

```text
package merely appears somewhere in uv.lock
```

from:

```text
this exact selected uv environment includes the changed package
```

including transitive membership where exact project/lock evidence supports it.

### S011 pressure

The real change is inside `pyproject.toml` `[project.optional-dependencies].mlx`, while ordinary workflows install `.[dev]`. The current normal dependency-analysis path does not admit that source format, and workflow context must not be interpreted as formation/consumption of the affected optional extra.

### S005 transfer pressure

Historical simulation evidence shows lock consumption can be mediated through tox + `uv-venv-lock-runner`. The new implementation must not encode `uv.lock consumption == direct uv sync only`; it may explicitly defer tox interpretation if that is a materially separate mechanism.

### AUDIT-004 pressure

Successful/current uv resolution can be useful evidence of declared dependency-constraint satisfiability, but:

```text
resolver-satisfiable != behavioral compatibility
```

The selected plan contains a later resolver-satisfiability **reassessment gate**, not automatic resolver execution.

## Remaining intentionally unresolved / separately deferred work

These are not defects merely because they remain unresolved:

```text
static↔runtime GitHub Actions job/step correlation
runtime log interpretation
matrix static-job ↔ runtime-instance mapping
reusable-workflow execution semantics
exact proposed dependency version runtime witness
generic shell/dependency tracing
generic tox/nox/task-runner interpretation
package managers outside the new plan's admitted first families
final compatibility/safety/recommendation synthesis
```

## Immediate project action

**Begin the selected plan, but do not skip its setup gate.**

Next action:

1. create **one** working-memory record for `B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`;
2. run **Cluster 0** synchronization/baseline validation on current `main`;
3. record exact branch/HEAD/origin/worktree/test evidence;
4. only after a classified green baseline, enter Cluster 1 contract work.

Do not create per-cluster working-memory files. Append the same implementation record unless a materially separate later responsibility is explicitly selected.

## Continuation-critical guards

- `MEMORY.md` alone owns current continuation/latest verification;
- accepted Tranche-1 implementation revision remains `ef4283db0a7ce3eec75a56ccc5c07354015fd2e3` until the new plan establishes its own validated baseline/source revisions;
- Tranche 1 is complete and must not be retroactively enlarged;
- the selected new plan is a separate post-Tranche-1 responsibility;
- Tranche 2 remains optional, separate, and not selected;
- GitHub owns GitHub Actions source structure, not dependency/package-manager semantics;
- Dependency owns dependency-source/environment membership and broader consumption semantics;
- CI owns CI-specific composition with exact-head runtime evidence;
- `dependency/direct_install.py` must remain narrow rather than becoming a universal dependency-consumption abstraction;
- package present in `uv.lock` != package selected in every environment;
- `.[dev]` != `.[mlx]`;
- static consumption declaration != execution/success;
- dependency consumed != package behavior exercised;
- resolver satisfiability != API/runtime compatibility;
- `not_observed` != absent without justified completeness;
- no generic package-manager/tox/shell/workflow engine without new evidence and explicit selection;
- resolver execution must pass the selected plan's security/value gate before implementation.

## Learning state

Tranche-1 milestone onboarding produced enough real-case understanding to select the next implementation responsibility from evidence rather than chronology. The current demonstrated depth remains guided implementation-adjacent learning; no formal mastery claim is made.

Learning should continue alongside implementation in small coherent blocks, especially around dependency-source identity, environment membership, lock reachability, project selectors, static/runtime proof separation, and CI consumption-versus-exercise semantics.