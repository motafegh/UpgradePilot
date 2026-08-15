# B2 Cross-Responsibility Architecture — Tranche 1 Implementation Record

**Date:** 2026-08-15  
**Operation:** Phase E / Tranche 1 — static workflow architecture implementation and migration  
**Result classification:** OPEN / progressive implementation evidence record  
**Validated product/source baseline:** `92e6ea6cb6dbfad7c50986d95e23de924a9b36c1` on `main`  
**Latest validated implementation revision:** `10e07b37a72e6d457dfedd6766dfab23e5a27520` on `main`

## 1. Purpose and operating mode

Preserve material implementation, debugging, findings, exact validation evidence, and cluster results while executing Tranche 1 of [`../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md`](../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md).

This is an evidence trail, not the live-state owner. `../MEMORY.md` alone owns current continuation.

Accepted durable architecture remains [`../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md`](../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md).

### Learning / source-documentation mode

The user selected learning-by-doing/building and deferred broad mastery/system/data-flow teaching until a meaningful implementation milestone. New/materially modified source should include useful docstrings/comments for responsibility, proof boundaries, invariants, precedence/abstention logic, and non-obvious reasoning without restating syntax; the stable rule is owned by [`../OPERATING_GUIDE.md`](../OPERATING_GUIDE.md).

## 2. Tranche-1 checklist

- [x] **Cluster 0 — synchronize and validate baseline**
- [x] **Cluster 1 — add PyYAML and prove parser dependency boundary**
- [x] **Cluster 2 — implement bounded GitHub Actions static workflow IR**
- [x] **Cluster 3 — implement shared direct-installation declaration observation**
- [x] **Cluster 4 — migrate Target artifact-environment interpretation**
- [x] **Cluster 5 — migrate CI static reading and narrow proof strength**
- [ ] **Cluster 6 — reconcile repository-path ownership drift** — implementation written, validation pending
- [ ] **Cluster 7 — Tranche-1 regression and acceptance gate**
- [ ] **Tranche-1 stop/review completed**

A checked cluster means its bounded objective and applicable validation were satisfied; code presence alone is insufficient.

## 3. Continuation-critical guards

```text
static declaration != execution != success
consumer unresolved != parser failure
multiple jobs / needs / source order != runtime environment continuity
workflow evidence != complete Target context
direct-install declaration != generic dependency consumption
package invocation/exercise remains CI-specific
static Actions evidence != runtime Actions evidence
Tranche 1 != automatic authorization for Tranche 2
```

## 4. Cluster 0 — green baseline

**Status:** COMPLETED / GREEN BASELINE  
Validated baseline `92e6ea6cb6dbfad7c50986d95e23de924a9b36c1`; complete suite: `403 tests / OK`.

## 5. Cluster 1 — PyYAML dependency/parser boundary

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `0d2c7f9eba08bd3c80f1b128d5b223b4e10a9667`

PyYAML runtime dependency + private bounded representation-node parsing were established and validated. A stale exact dependency-contract expectation correctly failed after PyYAML was added, then was deliberately updated and revalidated.

## 6. Cluster 2 — bounded static GitHub Actions workflow IR

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `1e3027f87fa5b187c7d333472fe849aa6a49b049`  
Complete suite: `416 tests / OK`.

The provider-owned typed static IR is independently green before consumer migration.

## 7. Cluster 3 — shared direct-install declaration observation

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `2980e22994216c069b2f4fb36dc31ea80398367f`  
Complete suite: `425 tests / OK`.

`upgradepilot.dependency` owns direct requirements-install declaration observation with step > job > workflow > repository-root working-directory precedence and `observed | not_observed | unresolved` declaration-strength semantics.

## 8. Cluster 4 — Target migration and proof-strength correction

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `f40e7348a38966e7e30b462846a4962a116a9e80`  
Complete suite: `430 tests / OK`.

Target now consumes the shared workflow IR + direct-install observer. Static workflow source no longer claims runtime environment formation; active Target evidence uses declaration-strength `observed | not_observed | unresolved` semantics.

## 9. Cluster 5 — CI migration and proof-claim narrowing

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `10e07b37a72e6d457dfedd6766dfab23e5a27520`

### Changes

`src/upgradepilot/ci/workflow_commands.py` now consumes:

```text
parse_workflow_definition(...)
observe_direct_installation_declaration(...)
```

rather than owning another indentation/regex workflow reader and pip requirements matcher. CI retains package-invocation recognition, the bounded one-static-job rule, and static install-before-invocation ordering.

The dependency observer exposes `matched_segment_index` only as a bounded static shell-segment locator so CI can compare declaration order without duplicating install parsing:

```text
static segment ordinal != runtime command/step identity
```

`src/upgradepilot/ci/dependency_exercise.py` replaced the old strongest state `proven` with:

```text
supported_not_correlated
```

meaning:

```text
successful exact-head workflow/run + successful runtime job evidence
+
exact-head static ordered install→package-invocation path
!= matched static commands observed executing/succeeding at runtime
```

Static↔runtime job/step correlation remains outside Tranche 1.

### Validation

User ran the requested fail-fast Cluster-5 gate covering:

```text
test_workflow_commands.py
test_ci_dependency_exercise.py
test_direct_install_declaration.py
test_github_workflow_definition.py
test_target_artifact_environment.py
test_source_topology.py
test_investigation.py
test_cli.py
test_step7f_end_to_end.py
```

The block reached its completion marker, so all focused/nearest commands passed. Complete deterministic suite:

```text
Ran 434 tests in 0.092s
OK
```

Final state:

```text
branch: main
HEAD: 10e07b37a72e6d457dfedd6766dfab23e5a27520
origin/main: same revision
worktree: clean
```

### T1-F006 — CI now preserves the missing static↔runtime link explicitly

The migration removes duplicated workflow/install parsing while deliberately refusing to describe successful runtime CI + static declaration evidence as correlated command success.

## 10. Cluster 6 — repository-path ownership reconciliation

**Status:** IMPLEMENTATION WRITTEN / VALIDATION PENDING

### Expected

Remove the duplicate private repository-path validator from `src/upgradepilot/github/repository.py` and use the existing source-neutral owner:

```text
src/upgradepilot/repository_path.py
→ repository_relative_parts(...)
```

No new ADR is required because this executes ADR-0007 ownership rather than introducing a new architecture.

### Finding

The duplicate GitHub helper had drifted slightly from the canonical structural rule:

- it stripped outer whitespace before validation;
- it did not explicitly reject backslash separators;
- the canonical source-neutral owner preserves exact spelling and rejects non-POSIX/backslash, empty-component, `.` and `..` forms.

Cluster 6 intentionally adopts the canonical contract instead of preserving the duplicate behavior.

### Changes

`src/upgradepilot/github/repository.py` now imports and delegates structural validation to `repository_relative_parts(...)`. The local `_validate_repository_path(...)` implementation is removed.

The GitHub owner retains only provider concerns:

```text
shared repository-relative structural validation
→ GitHub URL encoding
→ exact revision acquisition
→ exact returned-path / byte-count / encoding / UTF-8 provenance checks
```

The touched source now documents this ownership boundary and the fact that path spelling is preserved rather than silently rewritten.

`tests/test_exact_commit_repository_files.py` adds a focused boundary regression proving that canonical invalid path forms are rejected before any network call:

```text
absolute path
backslash path
double separator
./ component
../ traversal
empty path
```

### Source/test commits

```text
69cb592b1a3125cc3bb66eebf6f763073c17e0c6
→ Use shared repository path validation

5f68006d6dad79ebb28b28ae661dd9eb33245ab5
→ Protect shared repository path ownership
```

### Validation

Pending user-run focused/nearest/full gate.

### Cluster result

`PARTIAL / IMPLEMENTATION WRITTEN / VALIDATION PENDING`

Cluster 7 must not begin until Cluster 6 is validated and explicitly closed.

## 11. Remaining plan responsibilities

- Cluster 7 — Tranche-1 regression and acceptance gate: **PENDING**
- Tranche-1 stop/review: **PENDING**

Tranche 2 remains separately reviewed work and must not start automatically.
