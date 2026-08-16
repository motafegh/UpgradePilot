# UpgradePilot Current Memory

**Last updated:** 2026-08-16  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Selected responsibility:** **Dependency Environment and CI Consumption Evidence** under [`plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md).
- **Selected-plan status:** implementation **STARTED**; **Cluster 0 COMPLETE / GREEN; Cluster 1 ACTIVE**.
- **Progressive implementation record:** [`working-memory/2026-08-16_B2-dependency-environment-ci-consumption-implementation.md`](working-memory/2026-08-16_B2-dependency-environment-ci-consumption-implementation.md).
- **Fresh new-plan baseline:** `7444324e511b1e6fb49e6dba0bac371272bff7ba` — local fail-fast baseline green, `435 tests / OK`, HEAD==origin/main, clean worktree.
- **Tranche-1 status:** implementation and acceptance **COMPLETE / GREEN** at `ef4283db0a7ce3eec75a56ccc5c07354015fd2e3`; historical accepted foundation, not reopened.
- **Accepted GitHub Actions architecture:** [`docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md`](docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md).
- **Source ownership baseline:** [`docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](docs/architecture/ADR-0007-responsibility-based-python-subpackages.md).
- **Resolver-satisfiability review evidence:** [`audits/2026-08-16_AUDIT-004_uv-lock-resolution-satisfiability-evidence-boundary.md`](audits/2026-08-16_AUDIT-004_uv-lock-resolution-satisfiability-evidence-boundary.md).
- **Execution/learning/code-documentation rules:** [`OPERATING_GUIDE.md`](OPERATING_GUIDE.md).

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

Initial admitted pressure surface:

```text
requirements files
+
uv.lock / uv project groups and extras
+
pyproject.toml optional dependencies / dependency groups
```

Primary real pressure:

```text
S001 — positive uv locked-environment consumption
S011 — optional-extra non-formation/non-consumption
S005 — transfer pressure for tox/uv mediated lock consumption
```

Core evidence ladder:

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

## New-plan implementation status

```text
✓ Cluster 0 — synchronized/frozen green baseline
→ Cluster 1 — bounded dependency-environment evidence contract ACTIVE
  Cluster 2 — pyproject optional-extra transition not started
  Cluster 3 — project-environment selection not started
  Cluster 4 — uv.lock membership/reachability not started
  Cluster 5 — CI consumption migration not started
  Cluster 6 — application/real-case integration not started
  Cluster 7 — resolver-satisfiability gate not started
  Cluster 8 — acceptance/STOP-REVIEW not started
```

### Cluster-0 validation truth

The user ran the documented fail-fast baseline after synchronizing `main`. The block reached its final markers under `set -euo pipefail`, therefore repository identity, import smoke, focused dependency/workflow/CI tests, and nearest application tests all passed before the complete suite.

Visible nearest application result:

```text
Ran 13 tests in 0.011s
OK
```

Complete deterministic product suite:

```text
Ran 435 tests in 0.080s
OK
```

Final state:

```text
branch      : main
HEAD        : 7444324e511b1e6fb49e6dba0bac371272bff7ba
origin/main : 7444324e511b1e6fb49e6dba0bac371272bff7ba
worktree    : clean
```

The trailing `__vsc_update_prompt:6: RPROMPT: parameter not set` was classified as a local shell prompt-hook issue after the validation block, not an UpgradePilot failure.

## Cluster 1 current question

Before coding, inspect the current format-specific handoff:

```text
direct_requirements_install_path: str | None
```

and design the smallest dependency-owned typed evidence contract that can represent:

```text
exact requirements source
uv project/lock context
pyproject optional-extra context
pyproject dependency-group context
```

while preserving exact provenance and normalized changed-package identity and **without** encoding workflow selection, runtime execution, resolver success, or a universal environment graph.

The contract must preserve current requirements behavior and create the correct dependency→CI boundary for later S001/S011 work.

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
✓ STOP / REVIEW milestone produced the selected next responsibility

Tranche 2 — NOT SELECTED / NOT AUTHORIZED
```

The responsibilities remain distinct:

```text
CURRENT PLAN
recognize relevant dependency environment + static consumption path

OPTIONAL TRANCHE 2
correlate an already-identified static job/step with runtime job/step evidence
```

## Accepted Tranche-1 foundation

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

Strongest pre-new-plan CI state remains `supported_not_correlated`:

```text
successful exact-head runtime workflow/job evidence
+
ordered exact-head static install→package-invocation path
!= matched static commands observed executing/succeeding at runtime
```

## Continuation-critical guards

- `MEMORY.md` alone owns current continuation/latest verification;
- Cluster-0 baseline for the new plan is green at `7444324e511b1e6fb49e6dba0bac371272bff7ba`;
- Tranche 1 remains historical accepted work; do not retroactively enlarge it;
- Tranche 2 remains optional, separate, and not selected;
- GitHub owns GitHub Actions source structure, not package-manager semantics;
- Dependency owns dependency-source/environment membership and broader consumption semantics;
- CI owns CI-specific composition with exact-head runtime evidence;
- application owns sequencing, not source semantics;
- `dependency/direct_install.py` remains narrow rather than becoming universal dependency consumption;
- package present in `uv.lock` != package selected in every environment;
- `.[dev]` != `.[mlx]`;
- static consumption declaration != execution/success;
- dependency consumed != package behavior exercised;
- resolver satisfiability != API/runtime compatibility;
- `not_observed` != absent without justified completeness;
- no generic package-manager/tox/shell/workflow engine without new evidence and explicit selection;
- resolver execution must pass the selected plan's security/value gate before implementation;
- new/materially modified source must carry proportional educational docstrings/comments explaining responsibility, proof boundaries, invariants, abstention, and deliberate non-claims.

## Learning state

Continue learning-by-building in small coherent blocks. For each material implementation step, first explain the owned question and data flow, then implement, validate, and append the same progressive working-memory record. No mastery claim is inferred from passing AI-assisted code.
