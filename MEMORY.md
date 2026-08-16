# UpgradePilot Current Memory

**Last updated:** 2026-08-16  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Selected responsibility:** **Dependency Environment and CI Consumption Evidence** under [`plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN.md).
- **Selected-plan status:** implementation **IN PROGRESS**; **Cluster 0 COMPLETE / GREEN; Cluster 1 COMPLETE / GREEN; Cluster 2 NOT STARTED / HOLD**.
- **Progressive implementation record:** [`working-memory/2026-08-16_B2-dependency-environment-ci-consumption-implementation.md`](working-memory/2026-08-16_B2-dependency-environment-ci-consumption-implementation.md).
- **Fresh new-plan baseline:** `7444324e511b1e6fb49e6dba0bac371272bff7ba` — local fail-fast baseline green, `435 tests / OK`, aligned HEAD/origin, clean worktree.
- **Validated Cluster-1 implementation revision:** `ef8b4aa623bb53356b0969d099d2e32ee250b3e9` — local validation green, `439 tests / OK`, aligned HEAD/origin, clean worktree.
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
✓ Cluster 1 — bounded dependency-environment evidence contract
  Cluster 2 — exact pyproject optional-extra transition NOT STARTED / HOLD
  Cluster 3 — project-environment selection not started
  Cluster 4 — uv.lock membership/reachability not started
  Cluster 5 — CI consumption migration not started
  Cluster 6 — application/real-case integration not started
  Cluster 7 — resolver-satisfiability gate not started
  Cluster 8 — acceptance/STOP-REVIEW not started
```

### Cluster-0 validation truth

The user ran the documented fail-fast baseline after synchronizing `main`.

```text
nearest application: 13 tests / OK
complete suite:       435 tests / OK
HEAD:                 7444324e511b1e6fb49e6dba0bac371272bff7ba
origin/main:          same
worktree:             clean
```

### Cluster-1 implementation/result

Cluster 1 replaced the format-specific stored handoff:

```text
direct_requirements_install_path: str | None
```

with dependency-owned typed source contexts as the stored truth:

```text
RequirementsFileDependencyContext
ConstraintsFileDependencyContext
UvLockDependencyContext
PyprojectOptionalExtraDependencyContext
PyprojectDependencyGroupContext
```

Current trusted analysis populates requirements, constraints, and uv-lock contexts. The pyproject variants are contract surface only until Cluster 2 supplies exact source extraction.

The old direct requirements path remains temporarily as a **derived compatibility projection** for existing CI/application consumers; it is no longer duplicated stored truth.

S001-style `uv.lock` evidence is therefore now preserved as:

```text
UvLockDependencyContext(...)
```

instead of collapsing downstream to an undifferentiated `None`, while CI behavior is deliberately unchanged at this stage.

Cluster 1 does **not** establish group/extra selection, selected-environment membership, CI consumption, command execution/success, runtime exact-version witness, or package exercise.

### Cluster-1 validation truth

The user ran the documented fail-fast Cluster-1 validation after synchronizing `main`. Reaching the complete-suite/final-state markers means focused contract and nearest consumer regressions passed before the visible final result.

```text
complete deterministic suite: 439 tests / OK
HEAD:                         ef8b4aa623bb53356b0969d099d2e32ee250b3e9
origin/main:                  same
worktree:                     clean
```

The recurring trailing `__vsc_update_prompt:6: RPROMPT: parameter not set` is a local shell prompt-hook issue after validation, not an UpgradePilot failure.

Documentation/live-state commits after the validated implementation revision may advance `main`; they do not replace `ef8b4aa623bb53356b0969d099d2e32ee250b3e9` as the current validated product/source point until further source changes are validated.

## Immediate project action

**HOLD. Do not start Cluster 2 yet.**

When the user explicitly resumes implementation, the next bounded responsibility is Cluster 2:

```text
exact modified pyproject.toml
+ exact base/head repository evidence
+ [project.optional-dependencies]
→ conservative exact-pin transition extraction
→ DependencyVersionChange
+ PyprojectOptionalExtraDependencyContext(extra=<source-established name>)
```

Before touching source, onboard the user on the exact Cluster-2 proposition, expected source flow, ambiguity/abstention boundaries, and why optional-extra identity is dependency evidence rather than CI selection evidence.

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

## Continuation-critical guards

- `MEMORY.md` alone owns current continuation/latest verification;
- new-plan Cluster-0 baseline is green at `7444324e511b1e6fb49e6dba0bac371272bff7ba`;
- Cluster-1 implementation is validated green at `ef8b4aa623bb53356b0969d099d2e32ee250b3e9` with `439 tests / OK`;
- Cluster 2 is **not started** and no further source mutation is authorized until the user resumes;
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
