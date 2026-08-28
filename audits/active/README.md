# Active Audits

This folder is the **active lifecycle index** for validated audit findings selected as inputs to the current engineering responsibility.

Canonical audit records remain at stable paths directly under `audits/`. Existing audits contain relative references written from that location, so lifecycle classification is represented here instead of physically relocating those files and silently breaking their reproducibility links.

Current active audits:

- [ACTIVE — AUDIT-005 — Product AI / Agentic Orchestration and Sequencing Reassessment](../2026-08-21_AUDIT-005_product-ai-agentic-orchestration-sequencing.md)
  - owning plan: `../../plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md`
  - activation basis: R7 deterministic acceptance completed successfully; the mandatory B2/X1 checkpoint is active.
  - current engineering route: Phase 3A protocol `b2-x1-phase3a-v2` is accepted. The calibrated checkpoint sequence is `Phase 3B-1 minimum model-ready deterministic boundary → Phase 4A early development-only local-model smoke → Phase 3B-2 protected-scoring machinery only if the smoke shows basic viability → Phase 4B protected pilot`.
  - current implementation state: the Phase-3B/4A model-ready development path is prepared under `experiments/` and `tools/`, including the oracle-isolating request renderer, `d-a1-smoke`, real `d-s004-stop`, the four-call LM Studio development runner, proxy-safe WSL wrapper, and offline-focused tests. Local WSL execution/compile evidence and LM Studio model behavior remain pending; no runtime/model PASS is claimed.
  - immediate selected action boundary: Ali explicitly paused implementation for Learning-Only mastery/review. Resume engineering only after that pause is explicitly ended. Ordinary B2 continuation remains blocked until the B2/X1 checkpoint reaches an evidence-backed disposition.

Active audits remain **non-controlling evidence**. The active plan, specifications/ADRs where applicable, source/tests, and `MEMORY.md` own execution, stable decisions, behavior, and live continuation.

When an active audit is dispositioned, remove it from this index and add it to either `../absorbed/README.md` or `../deferred/README.md` with an updated lifecycle title.
