# B2 Cross-Responsibility Architecture — Tranche 1 Implementation Record

**Date:** 2026-08-15  
**Operation:** Phase E / Tranche 1 — static workflow architecture implementation and migration  
**Result classification:** OPEN / progressive implementation evidence record  
**Validated product/source baseline:** `92e6ea6cb6dbfad7c50986d95e23de924a9b36c1` on `main`  
**Latest validated implementation revision:** `63190a9f9538966a6d3e53d3ae70cda21edbfc8c` on `main`

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
- [x] **Cluster 6 — reconcile repository-path ownership drift**
- [ ] **Cluster 7 — Tranche-1 regression and acceptance gate** — ready for consolidated validation
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
Complete suite: `434 tests / OK`.

CI now consumes the shared workflow IR and dependency install observer. The strongest active state is `supported_not_correlated`, explicitly preserving the missing static↔runtime command correlation. Static install-before-invocation ordering is checked without claiming runtime execution or success.

## 10. Cluster 6 — repository-path ownership reconciliation

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `63190a9f9538966a6d3e53d3ae70cda21edbfc8c`

### Changes

`src/upgradepilot/github/repository.py` no longer owns a second `_validate_repository_path(...)` implementation. It delegates source-neutral relative POSIX path structure to:

```text
src/upgradepilot/repository_path.py
→ repository_relative_parts(...)
```

GitHub retains provider-specific URL/acquisition/provenance behavior only.

The reconciliation intentionally adopts the canonical owner where the duplicate had drifted:

- no silent outer-whitespace normalization;
- backslash paths rejected;
- empty, `.`, `..`, and traversal components rejected;
- exact accepted spelling preserved.

`tests/test_exact_commit_repository_files.py` now protects rejection of invalid repository paths before network access, while `tests/test_identity_primitives.py` protects the source-neutral owner directly.

### Validation

User ran the requested fail-fast Cluster-6 gate. It covered repository acquisition/path identity plus nearest GitHub workflow, dependency observer, Target, CI, and topology regressions. The block reached its completion marker, so all focused/nearest commands passed.

Complete deterministic suite:

```text
Ran 435 tests in 0.088s
OK
```

Final state:

```text
branch: main
HEAD: 63190a9f9538966a6d3e53d3ae70cda21edbfc8c
origin/main: same revision
worktree: clean
```

### T1-F007 — repository path structure now has one active owner

The slight behavior drift in the duplicate GitHub helper validated the architectural reason for reconciliation: shared structural rules should not have parallel private implementations.

## 11. Cluster 7 — Tranche-1 regression and acceptance gate

**Status:** READY FOR CONSOLIDATED VALIDATION

No additional acceptance-only source/test code is currently justified. Existing focused suites already cover the required plan obligations, including:

- single/multi-job static workflow structure;
- `needs`, literal/dynamic runner, matrix without expansion, reusable jobs;
- ordered run/uses steps, `if`, `continue-on-error`, workflow/job/step run context;
- block/folded run YAML, duplicate identity, malformed/recursive/bounded YAML behavior;
- Target declaration-strength semantics and consumer-level limitations;
- CI narrowed `supported_not_correlated` proof semantics and install-before-invocation ordering;
- direct-install working-directory/path resolution;
- S004-style multi-job/matrix structural preservation;
- S011-style refusal to infer affected environment/exercise merely because workflow context exists;
- source-neutral repository-path ownership.

Cluster 7 therefore requires one consolidated focused/nearest/full acceptance run at a clean aligned revision. No new architecture or Tranche-2 correlation work is authorized inside this gate.

## 12. Remaining plan responsibility

- Cluster 7 acceptance validation: **PENDING USER-RUN GATE**
- Tranche-1 stop/review: **PENDING**

If Cluster 7 is green, Tranche 1 reaches its mandatory STOP / REVIEW line. Tranche 2 remains separately reviewed work and must not start automatically.
