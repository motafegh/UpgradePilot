# Active Audits

This folder is the **active lifecycle index** for validated audit findings selected as inputs to the current engineering responsibility.

Canonical audit records remain at stable paths directly under `audits/`. Existing audits contain relative references written from that location, so lifecycle classification is represented here instead of physically relocating those files and silently breaking their reproducibility links.

Current active audits:

- [ACTIVE — AUDIT-009 — Post-Runtime-State Delta Readiness Audit](../2026-10-02_AUDIT-009_post-runtime-state-delta-readiness.md)
  - selection basis: Ali requested a full post-runtime-state delta audit and then authorized reconciliation of stale current-facing records before the next action-relative reachability comparison.
  - execution owners: `../../plans/END_TO_END_PRODUCT_FLOW_LEARNING_AND_EVIDENCE_TO_ACTION_EXECUTION_PLAN.md` and its parent `../../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`; `../../MEMORY.md` alone owns the exact live slice.
  - current coordination boundary (2026-10-02): Runtime Dependency-State Cycle 1 is closed and Product Verification #17 remains the product proof anchor. The next selected responsibility is the parent action-relative reachability comparison. AUDIT-009 is the current delta-readiness input; it does not authorize F5/F7, Runtime-State Cycle 2, AI activation, or maintainer-action implementation.

AUDIT-008 has been moved to ABSORBED because AUDIT-009 and the completed F3/F4/F9/F11/F6 records now carry its current conclusions forward. AUDIT-008 remains the historical baseline and source of finding provenance. AUDIT-005 remains SCHEDULED and is not the selected current engineering workstream.

Active audits remain **non-controlling evidence**. The active plan, specifications/ADRs where applicable, source/tests, and `MEMORY.md` own execution, stable decisions, behavior, and live continuation.

When an active audit is dispositioned, remove it from this index and add it to the appropriate lifecycle index under `../scheduled/`, `../deferred/`, or `../absorbed/` with an updated title and explicit rationale under `audits/LIFECYCLE.md`.
