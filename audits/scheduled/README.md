# Scheduled Audits

This folder is the **scheduled lifecycle index** for validated audit questions or opportunities that are not the current implementation responsibility but have been explicitly selected for a concrete future activation trigger and owning execution plan.

Scheduled is stronger than deferred:

```text
deferred
→ valid but no guaranteed near-term execution point

scheduled
→ selected responsibility
→ explicit prerequisite / activation trigger
→ owning plan
→ non-skippable handoff when the trigger is satisfied
```

A scheduled audit is still non-controlling review evidence. Its owning plan defines execution and `MEMORY.md` owns live activation.

Current scheduled audits:

- [SCHEDULED — AUDIT-005 — Product AI / Agentic Orchestration and Sequencing Reassessment](../2026-08-21_AUDIT-005_product-ai-agentic-orchestration-sequencing.md)
  - findings retained: a bounded, read-only product-level investigation-planner evaluation is an explicitly selected but **undispositioned** B2/X1 checkpoint; neither adoption nor rejection is implied by this audit's scheduling.
  - correct owning plan: [`../../plans/BOUNDED_PRODUCT_AGENTIC_INVESTIGATION_PLANNER_AND_ORCHESTRATION_EVALUATION_PLAN.md`](../../plans/BOUNDED_PRODUCT_AGENTIC_INVESTIGATION_PLANNER_AND_ORCHESTRATION_EVALUATION_PLAN.md), with accepted protocol [`../../plans/B2_X1_PHASE3_EVALUATION_PROTOCOL.md`](../../plans/B2_X1_PHASE3_EVALUATION_PROTOCOL.md). The previous active index's `B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md` path is outdated and does not exist on current `main`.
  - prerequisite status: R7 deterministic acceptance already satisfied the original activation gate; the previously approved B2/X1 checkpoint remains open, with the next technical evaluation step historically at Phase 3B-1/4A. The plan's earlier activation is **not current live selection**.
  - **rescheduled handoff trigger (2026-09-20 F11):** when the currently selected evidence-to-action execution journey reaches its completion or an explicit stop/replanning decision, **before switching to ordinary B2 continuation**, revisit this still-open B2/X1 checkpoint. At that handoff, explicitly activate the owning evaluation plan or record an evidence-backed reschedule/defer/reject disposition in the appropriate owning plan and `MEMORY.md`; do not silently skip it.
  - current live route: AUDIT-008 evidence-to-action journey in `MEMORY.md`. Scheduling this audit does not start model calls, product-agentic implementation, or authorize adoption; an earlier Learning-Only pause is not silently ended by this index update.

If a scheduled trigger becomes invalid before activation, do not silently move on. Reassess the audit/plan and record an explicit reject/defer/reschedule disposition in the owning plan and `MEMORY.md`.
