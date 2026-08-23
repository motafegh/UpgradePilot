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
  - owning plan: `../../plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md`
  - activation trigger: successful R7 acceptance/validation of `../../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`
  - sequencing rule: this X1 checkpoint is entered before old Cluster 6 or another ordinary B2 continuation; the checkpoint itself must reach an evidence-backed proceed/adopt/pilot/reject/defer disposition rather than being silently skipped.

If a scheduled trigger becomes invalid before activation, do not silently move on. Reassess the audit/plan and record an explicit reject/defer/reschedule disposition in the owning plan and `MEMORY.md`.
