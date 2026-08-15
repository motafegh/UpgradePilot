# UpgradePilot Current Memory

**Last updated:** 2026-08-15  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Selected responsibility:** Phase E / Tranche 1 of [`plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md`](plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md).
- **Accepted architecture:** [`docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md`](docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md).
- **Current implementation evidence record:** [`working-memory/2026-08-15_B2-cross-responsibility-architecture-tranche-1-implementation.md`](working-memory/2026-08-15_B2-cross-responsibility-architecture-tranche-1-implementation.md).
- **Source ownership baseline:** [`docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](docs/architecture/ADR-0007-responsibility-based-python-subpackages.md).
- **Execution/learning/code-documentation rules:** [`OPERATING_GUIDE.md`](OPERATING_GUIDE.md).

### Current Phase-E status

```text
✓ Cluster 0 — synchronized green baseline
✓ Cluster 1 — PyYAML dependency/parser boundary
✓ Cluster 2 — typed static GitHub Actions workflow IR
✓ Cluster 3 — shared direct-install declaration observation
✓ Cluster 4 — Target migration / proof-strength correction
✓ Cluster 5 — CI migration / proof-claim narrowing
→ Cluster 6 — repository-path reconciliation: implementation written, validation pending
[ ] Cluster 7 — Tranche-1 acceptance gate
[ ] Tranche-1 stop/review
```

**Learning mode:** continue learning-by-doing/building. Deep mastery, full current-system walkthrough, and real end-to-end data-flow study remain deferred until a meaningful implementation milestone.

**Source documentation rule:** new/materially modified source should include useful docstrings/comments for responsibility, proof boundaries, invariants, precedence/abstention behavior, or other non-obvious reasoning. Avoid comments that merely restate syntax.

## Verification truth

```text
Cluster 0  92e6ea6...  403 tests / OK
Cluster 1  0d2c7f9...  green
Cluster 2  1e3027f...  416 tests / OK
Cluster 3  2980e229...  425 tests / OK
Cluster 4  f40e7348...  430 tests / OK
Cluster 5  10e07b37...  434 tests / OK
```

Latest validated implementation revision:

```text
10e07b37a72e6d457dfedd6766dfab23e5a27520
```

Cluster-5 validation reached the requested fail-fast completion marker. Final state was `main`, `HEAD == origin/main == 10e07b37...`, worktree clean.

## Current implementation truth — Cluster 6

Cluster 6 source/tests are written but **not yet runtime-validated**.

### Repository-path ownership

The source-neutral owner already exists:

```text
src/upgradepilot/repository_path.py
→ repository_relative_parts(...)
```

`src/upgradepilot/github/repository.py` previously contained a second private `_validate_repository_path(...)` implementation. That duplicate has now been removed.

GitHub repository acquisition delegates path structure to the shared owner, then retains only provider-specific responsibilities:

```text
repository-relative structural validation
→ GitHub URL encoding
→ immutable-revision acquisition
→ returned path / blob / byte-count / encoding / UTF-8 validation
```

### Small drift discovered during reconciliation

The old GitHub-local helper was not perfectly identical to the canonical contract:

- it stripped outer whitespace;
- it did not explicitly reject backslash separators;
- the canonical owner preserves exact spelling and rejects backslash, empty-component, `.` and `..` path forms.

Cluster 6 deliberately adopts the canonical source-neutral contract rather than preserving the duplicate drift.

### Regression protection

`tests/test_exact_commit_repository_files.py` now proves canonical invalid path forms are rejected before any network call, while existing `tests/test_identity_primitives.py` continues to protect the source-neutral path owner directly.

Current Cluster-6 source/test commits:

```text
69cb592b1a3125cc3bb66eebf6f763073c17e0c6
5f68006d6dad79ebb28b28ae661dd9eb33245ab5
```

No Cluster-7 acceptance work has started.

## Immediate project action

**Validate Cluster 6 before beginning Cluster 7.**

Required gate should cover:

```text
test_exact_commit_repository_files.py
+ test_identity_primitives.py
+ test_github_actions.py
+ test_github_workflow_definition.py
+ test_direct_install_declaration.py
+ test_target_artifact_environment.py
+ test_ci_dependency_exercise.py
+ test_source_topology.py
+ complete deterministic suite
+ clean aligned worktree
```

If green, close Cluster 6 and only then begin the Tranche-1 acceptance gate.

## Continuation-critical guards

- `MEMORY.md` alone owns current continuation/latest verification;
- latest validated implementation revision remains `10e07b37a72e6d457dfedd6766dfab23e5a27520` until Cluster 6 is validated;
- documentation/source commits after that revision do not themselves constitute validation;
- repository-relative structural validation has one source-neutral owner;
- provider-specific workflow path meaning remains with GitHub/consumer boundaries;
- static workflow structure remains separate from runtime evidence;
- `supported_not_correlated` must not be described as matched runtime command success;
- static↔runtime job/step correlation remains outside Tranche 1;
- Cluster 7 must not begin before Cluster 6 is green;
- Tranche 2 remains separately reviewed and must not start automatically.

## Learning state

Current demonstrated depth remains substantial guided implementation exposure with repeated evidence-driven reasoning/debugging; no formal mastery assessment. Deep system/data-flow learning remains intentionally deferred until a meaningful milestone selected with the user.
