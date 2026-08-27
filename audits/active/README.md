# Active Audits

This folder is the **active lifecycle index** for validated audit findings selected as inputs to the current engineering responsibility.

Canonical audit records remain at stable paths directly under `audits/`. Existing audits contain relative references written from that location, so lifecycle classification is represented here instead of physically relocating those files and silently breaking their reproducibility links.

Current active audits:

- [ACTIVE — AUDIT-005 — Product AI / Agentic Orchestration and Sequencing Reassessment](../2026-08-21_AUDIT-005_product-ai-agentic-orchestration-sequencing.md)
  - owning plan: `../../plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md`
  - activation basis: R7 deterministic acceptance completed successfully; the mandatory B2/X1 checkpoint is active.
  - current responsibility: Phase 3A protocol `b2-x1-phase3a-v2` is accepted; build the deterministic experiment-owned Phase-3B planner-request/manifest/replay/baseline/grading harness and focused tests without any model/provider call. Phase 4 model scoring remains blocked until the Phase-3B deterministic gate passes and its separate model/configuration gate is satisfied.

Active audits remain **non-controlling evidence**. The active plan, specifications/ADRs where applicable, source/tests, and `MEMORY.md` own execution, stable decisions, behavior, and live continuation.

When an active audit is dispositioned, remove it from this index and add it to either `../absorbed/README.md` or `../deferred/README.md` with an updated lifecycle title.
