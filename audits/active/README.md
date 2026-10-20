# Active Audits

This folder is the **active lifecycle index** for validated audit findings selected as inputs to the current engineering responsibility.

Canonical audit records remain at stable paths directly under `audits/`. Existing audits contain relative references written from that location, so lifecycle classification is represented here instead of physically relocating those files and silently breaking their reproducibility links.

Current active audits:

- [ACTIVE — AUDIT-019 — Phase-B Product-Value Reconciliation and Audit-Program Reprioritization](../2026-10-20_AUDIT-019_phase-b-product-value-reconciliation-and-audit-program-reprioritization.md)
  - selection basis: main completed the bounded product-value feasibility Phase B at `cbba2c88`, establishing a credible finite S002/S004 retained-native-CI versus transparent-baseline component comparison before more architecture or semantic investment. AUDIT-019 reconciles that new evidence with the project-wide audit/correction program.
  - execution owner: [Project-wide Technical Audit and Correction Program Plan](../../plans/PROJECT_WIDE_TECHNICAL_AUDIT_AND_CORRECTION_PROGRAM_PLAN.md), with current branch progression in [Stage 7 remediation](../../working-memory/2026-10-20_stage7-remediation-progress.md). Workspace closure design is parked behind the comparison result; only comparison-independent governance/proof corrections continue meanwhile.
  - latest reconciled upstream horizon: `main@3344982c10e75863b4f4b922984e3b10b63f3b80`. The later AI-native/career horizon proposal is explicitly non-controlling and does not supersede the Phase-B product handoff in `MEMORY.md`.

AUDIT-018 is now ABSORBED as the predecessor cross-domain remediation order; AUDIT-019 supersedes it only for current sequencing/latest-main reconciliation and carries its still-valid findings forward. AUDIT-009 through AUDIT-017 remain absorbed historical/detail evidence.

AUDIT-005 remains SCHEDULED and is not the selected current engineering workstream unless its activation condition is separately re-established by the live owner.

Active audits remain **non-controlling evidence**. The active plan, specifications/ADRs where applicable, source/tests, and `MEMORY.md` own execution, stable decisions, behavior, and live continuation.

When an active audit is dispositioned, remove it from this index and add it to the appropriate lifecycle index under `../scheduled/`, `../deferred/`, or `../absorbed/` with an updated title and explicit rationale under `audits/LIFECYCLE.md`.
