# B2 Cross-Responsibility Architecture — Tranche 1 Implementation Record

**Date:** 2026-08-15  
**Operation:** Phase E / Tranche 1 — static workflow architecture implementation and migration  
**Result classification:** OPEN / progressive implementation evidence record  
**Validated product/source baseline:** `92e6ea6cb6dbfad7c50986d95e23de924a9b36c1` on `main`  
**Latest validated implementation revision:** `0d2c7f9eba08bd3c80f1b128d5b223b4e10a9667` on `main`  

## 1. Purpose

Preserve material implementation, debugging, findings, exact validation evidence, and cluster results while executing Tranche 1 of [`../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md`](../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md).

This file is an implementation evidence trail, not the live-state owner and not a replacement for the plan. `../MEMORY.md` alone owns current continuation.

Accepted durable architecture remains [`../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md`](../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md). Historical Phase-A–D reasoning remains in the closed reconciliation records and must not be continued here.

## 2. Governing implementation owners

- [`../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md`](../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md) — static GitHub Actions architecture and parser method.
- [`../docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](../docs/architecture/ADR-0007-responsibility-based-python-subpackages.md) — package/source ownership baseline.
- [`../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md`](../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md) — tranche/cluster order, proof obligations, stop lines.
- [`../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md) — proof-strength semantics.
- [`../SECURITY.md`](../SECURITY.md) — proportional untrusted structured-parser safety.
- [`../MEMORY.md`](../MEMORY.md) — sole live position/continuation owner.

## 3. Tranche-1 objective

```text
exact green baseline
↓
PyYAML dependency/parser boundary
↓
bounded github-owned static workflow IR
↓
dependency-owned direct-install declaration observation
↓
Target migration + static proof-semantic correction
↓
CI migration + current proof-claim narrowing
↓
repository-path ownership reconciliation
↓
focused + nearest + full validation
↓
STOP / REVIEW
```

## 4. Local execution checklist

- [x] **Cluster 0 — synchronize and validate baseline**
- [x] **Cluster 1 — add PyYAML and prove parser dependency boundary**
- [ ] **Cluster 2 — implement bounded GitHub Actions static workflow IR**
- [ ] **Cluster 3 — implement shared direct-installation declaration observation**
- [ ] **Cluster 4 — migrate Target artifact-environment interpretation**
- [ ] **Cluster 5 — migrate CI static reading and narrow proof strength**
- [ ] **Cluster 6 — reconcile repository-path ownership drift**
- [ ] **Cluster 7 — Tranche-1 regression and acceptance gate**
- [ ] **Tranche-1 stop/review completed**

A checked cluster means its bounded objective and applicable validation were satisfied; code presence alone is insufficient.

## 5. Continuation-critical implementation guards

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

Additional guards:

- `RepositoryTextFile` remains authoritative raw source evidence;
- PyYAML nodes remain private parser machinery, not UpgradePilot domain/evidence contracts;
- parser safety remains proportionate rather than becoming a generalized hostile-YAML framework;
- dynamic/matrix/reusable/container source structure must not become parser failure merely because a consumer cannot interpret it;
- no exact wheel-tag inference from broad workflow labels;
- no universal dependency-consumption tracer;
- material contradiction of ADR-0008 requires classification rather than silent architecture drift.

## 6. Cluster 0 — synchronize and validate baseline

**Status:** COMPLETED / GREEN BASELINE  
**Source edits before completion:** NONE

### Baseline identity

User-run WSL preflight established:

```text
branch: main
HEAD: 92e6ea6cb6dbfad7c50986d95e23de924a9b36c1
origin/main: 92e6ea6cb6dbfad7c50986d95e23de924a9b36c1
worktree: clean
```

The fail-fast focused baseline covered:

```text
tests/test_github_actions.py
tests/test_exact_commit_repository_files.py
tests/test_ci_dependency_exercise.py
tests/test_target_artifact_environment.py
tests/test_identity_primitives.py
tests/test_source_topology.py
```

All focused commands passed.

Complete deterministic suite:

```text
Ran 403 tests in 0.256s
OK
```

Final worktree remained clean.

### T1-F001 — Phase-E started from a clean, reproduced source baseline

```text
92e6ea6cb6dbfad7c50986d95e23de924a9b36c1
→ focused migration-relevant regressions pass
→ complete deterministic suite: 403 tests, OK
→ worktree clean
```

Documentation commits after this validation do not alter the product/source baseline proved above.

## 7. Cluster 1 — PyYAML dependency and parser boundary

**Status:** COMPLETED / GREEN  
**Validated implementation revision:** `0d2c7f9eba08bd3c80f1b128d5b223b4e10a9667`

### Changes

`pyproject.toml` now declares:

```text
PyYAML>=6.0.3,<7
```

`src/upgradepilot/github/workflow_definition.py` now provides the private first parser boundary:

```text
untrusted workflow text
→ yaml.compose(..., Loader=yaml.BaseLoader)
→ PyYAML representation nodes
→ controlled parse failure
→ bounded recursive-alias / depth / node-visit validation
```

This module intentionally does **not** yet implement the typed GitHub Actions job/step IR. PyYAML nodes remain internal syntax machinery.

`tests/test_github_workflow_definition.py` covers:

- BaseLoader textual scalar preservation;
- scalar/sequence/mapping node shapes;
- literal/folded block-scalar decoding;
- source marks;
- duplicate mapping-pair visibility before ordinary dict collapse;
- malformed YAML controlled failure;
- recursive alias rejection;
- bounded depth/node traversal.

`tests/test_runtime_dependency_contract.py` now explicitly protects the approved runtime dependency surface and verifies installed PyYAML satisfies `>=6.0.3,<7`.

### Failure / diagnosis / repair

The first post-change full-suite run exposed one failure:

```text
test_packaging_dependency_uses_the_accepted_26x_bound

Ran 409 tests in 0.311s
FAILED (failures=1)
```

Observed cause: the runtime dependency contract test still asserted the pre-Cluster-1 exact dependency list:

```text
requests>=2.32,<3
packaging>=26.2,<27
```

while `pyproject.toml` now correctly also contained:

```text
PyYAML>=6.0.3,<7
```

The failure was classified as a stale explicit dependency-contract expectation, not a parser/architecture defect.

Repair commit:

```text
0d2c7f9eba08bd3c80f1b128d5b223b4e10a9667
Update runtime dependency contract for PyYAML
```

The repair did not weaken the test. It made the dependency contract explicitly require all three approved runtime dependencies and added an installed-PyYAML version-bound assertion.

### T1-F002 — explicit dependency-surface tests correctly detect intentional runtime dependency changes

The regression demonstrated a useful repository invariant:

```text
approved dependency change
→ exact dependency contract fails
→ contract must be deliberately updated
→ change cannot silently enter runtime dependency surface
```

This is expected protective behavior, not test brittleness to remove.

### Validation after repair

User reran the requested post-repair validation in WSL:

```text
runtime dependency contract tests
+ focused Cluster-1 parser-boundary tests
+ complete deterministic product suite
```

User reported all commands green/passed.

No exact post-repair test count or timing is inferred because those final numeric lines were not supplied. The reported successful completion is recorded at that precision only.

### Cluster result

`COMPLETED / GREEN`

The bounded Cluster-1 responsibility is therefore established:

```text
accepted PyYAML runtime dependency
+
private non-object-constructing node composition boundary
+
proportionate graph guards
+
focused parser/dependency contract coverage
+
post-repair full-suite green
```

## 8. Current handoff / deliberate pause

Implementation is deliberately paused after Cluster 1 for user onboarding and understanding of the full current point.

No Cluster-2 source work has begun. No later cluster is selected for execution merely because it appears next in the approved plan.

The plan continues to define the remaining Tranche-1 sequence, but `MEMORY.md` owns whether/when implementation resumes after the onboarding checkpoint.

## 9. Remaining plan sections — not yet executed

- Cluster 2 — bounded GitHub Actions static workflow IR: **PENDING**
- Cluster 3 — shared direct-install declaration observation: **PENDING**
- Cluster 4 — Target migration: **PENDING**
- Cluster 5 — CI migration: **PENDING**
- Cluster 6 — repository-path ownership reconciliation: **PENDING**
- Cluster 7 — Tranche-1 acceptance gate: **PENDING**
- Tranche-1 stop/review: **PENDING**

Tranche 2 is outside this record and remains separately reviewed work.