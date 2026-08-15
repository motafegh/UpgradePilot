# B2 Cross-Responsibility Architecture — Tranche 1 Implementation Record

**Date:** 2026-08-15  
**Operation:** Phase E / Tranche 1 — static workflow architecture implementation and migration  
**Result classification:** OPEN / progressive implementation evidence record  
**Implementation baseline:** TO BE CAPTURED by Cluster 0 before source edits  

## 1. Purpose

Preserve the material implementation, debugging, findings, exact validation evidence, and cluster results produced while executing Tranche 1 of [`../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md`](../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md).

This record begins only after the preceding architecture reconciliation was formally closed. The accepted architecture is owned by [`../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md`](../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md); the detailed Phase-A–D reasoning remains historical in [`2026-08-14_B2-cross-responsibility-architecture-reconciliation-progress.md`](2026-08-14_B2-cross-responsibility-architecture-reconciliation-progress.md) and its [`2026-08-15_B2-cross-responsibility-architecture-reconciliation-phase-d-closure.md`](2026-08-15_B2-cross-responsibility-architecture-reconciliation-phase-d-closure.md).

This file is an implementation evidence trail, **not** the live-state owner and not a replacement for the plan. `../MEMORY.md` alone owns the exact current continuation.

## 2. Governing implementation owners

- [`../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md`](../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md) — accepted structural/parser architecture.
- [`../docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](../docs/architecture/ADR-0007-responsibility-based-python-subpackages.md) — source/package ownership baseline.
- [`../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md`](../plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md) — Tranche-1/2 sequence, proof obligations, and stop lines.
- [`../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md) — framework-independent proof-strength semantics.
- [`../SECURITY.md`](../SECURITY.md) — proportional untrusted structured-parser safety boundary.
- [`../MEMORY.md`](../MEMORY.md) — sole live project position and exact continuation.

## 3. Tranche-1 objective

Implement and validate the accepted static provider architecture without silently expanding into Tranche 2 or unrelated application architecture:

```text
exact baseline
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

This checklist mirrors the approved plan for convenience inside this dated implementation record. It does not replace the plan or `MEMORY.md`.

- [ ] **Cluster 0 — synchronize and validate baseline**
- [ ] **Cluster 1 — add PyYAML and prove parser dependency boundary**
- [ ] **Cluster 2 — implement bounded GitHub Actions static workflow IR**
- [ ] **Cluster 3 — implement shared direct-installation declaration observation**
- [ ] **Cluster 4 — migrate Target artifact-environment interpretation**
- [ ] **Cluster 5 — migrate CI static reading and narrow proof strength**
- [ ] **Cluster 6 — reconcile repository-path ownership drift**
- [ ] **Cluster 7 — Tranche-1 regression and acceptance gate**
- [ ] **Tranche-1 stop/review completed**

Do not check a cluster merely because code was written. A cluster is complete only when its bounded objective and applicable validation gate are satisfied or its remaining failure is explicitly classified.

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

Additional implementation rules:

- raw `RepositoryTextFile` remains authoritative source evidence;
- PyYAML parser/node objects remain internal syntax machinery, not UpgradePilot's public/domain IR;
- parser safety must be proportionate: safe/non-arbitrary-object parsing plus bounded malformed/recursive handling, without creating a generalized hostile-YAML framework;
- preserve readable dynamic/matrix/reusable/container structure even when current consumers remain unresolved;
- do not infer exact wheel tags from broad workflow labels;
- do not turn the shared direct-install primitive into a universal dependency-consumption tracer;
- if implementation materially contradicts ADR-0008, stop and classify the architecture conflict rather than silently changing the decision.

## 6. Recording convention for this tranche

For each material cluster, record only what is useful for reproducibility and diagnosis:

```text
EXPECTED
→ bounded objective / intended change

CHANGES
→ source/tests/dependency/contracts actually modified

OBSERVATIONS
→ exact relevant behavior/output

FINDINGS
→ implementation facts discovered; use T1-F### identifiers for durable tranche findings

FAILURES / DEBUGGING
→ meaningful failed approaches, diagnosis, repair

VALIDATION
→ exact commands + exact observed result

CLUSTER RESULT
→ COMPLETED / PARTIAL / BLOCKED / INVALID / SUPERSEDED
```

Small edits and every individual command do not need separate entries. Preserve material failures and changed understanding; avoid turning the record into a command diary.

## 7. Cluster 0 — synchronize and validate baseline

**Status:** PENDING  
**Source edits authorized before completion:** NO

### Expected

1. synchronize the implementation branch with current `main`;
2. verify the worktree is clean;
3. record the exact implementation baseline revision after documentation/setup commits are present;
4. run the focused regressions relevant to GitHub Actions/repository acquisition, CI dependency exercise, Target artifact environment, and repository-path behavior;
5. run the complete active deterministic product suite;
6. classify any pre-existing failure before changing source.

### Baseline identity

```text
revision: TO BE RECORDED
branch/worktree evidence: TO BE RECORDED
```

### Validation

```text
focused commands/results: PENDING
full suite command/result: PENDING
```

### Cluster result

`PENDING`

## 8. Cluster 1 — PyYAML dependency and parser boundary

**Status:** PENDING

Record the selected bounded version range, install/import proof, representation-node behavior, block scalars/source marks, duplicate-key visibility, malformed input behavior, and proportionate recursive/alias safety evidence required by the approved plan.

## 9. Cluster 2 — bounded GitHub Actions static workflow IR

**Status:** PENDING

Record the actual provider-owned module/types introduced, supported structural fields/variants, problem boundaries, tests, and any small implementation refinements to the ADR-0008 contract.

## 10. Cluster 3 — shared direct-installation declaration observation

**Status:** PENDING

Record the dependency-owned primitive, effective working-directory handling, admitted direct pip forms, proof-strength boundary, and focused tests.

## 11. Cluster 4 — Target migration

**Status:** PENDING

Record migration from the local shallow workflow parser to the shared IR, the replacement static declaration/configuration contract for the current runtime-sounding formation state, provenance preservation, unresolved behavior, and regression evidence.

## 12. Cluster 5 — CI migration

**Status:** PENDING

Record migration to the shared static IR/direct-install primitive, CI-specific package invocation/exercise handling, narrowed current proof claim/state, and regression evidence. Do not implement static↔runtime step correlation here.

## 13. Cluster 6 — repository-path ownership reconciliation

**Status:** PENDING

Record removal/reconciliation of the duplicate GitHub-local source-neutral repository-path validator and validation against the existing `repository_path.py` owner.

## 14. Cluster 7 — Tranche-1 acceptance gate

**Status:** PENDING

Required evidence is defined by the approved implementation plan and includes focused changed-responsibility tests, nearest GitHub/CI/Target/dependency regressions, installed/import smoke where the dependency/package surface changes, and the complete active deterministic product suite.

Transfer pressure should include the planned multi-job/matrix and optional-environment guards rather than relying only on synthetic happy paths.

## 15. Tranche-1 closure criteria

This record may be closed only when the selected Tranche-1 stop line is reached:

- shared static workflow IR implemented and migrated;
- Target static proof semantics corrected;
- CI current proof wording/state narrowed appropriately;
- direct-install declaration observation shared under the dependency boundary;
- repository-path drift reconciled;
- focused/nearest/full validation green or remaining failure explicitly classified;
- source/tests/docs/live memory synchronized.

Tranche 2 is **not** part of this record. If Tranche 1 is accepted and runtime correlation is still selected, create a separate dated Tranche-2 working record after explicit review.