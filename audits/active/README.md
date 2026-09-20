# Active Audits

This folder is the **active lifecycle index** for validated audit findings selected as inputs to the current engineering responsibility.

Canonical audit records remain at stable paths directly under `audits/`. Existing audits contain relative references written from that location, so lifecycle classification is represented here instead of physically relocating those files and silently breaking their reproducibility links.

Current active audits:

- [ACTIVE — AUDIT-008 — Current System End-to-End Evidence-to-Action Audit](../2026-09-19_AUDIT-008_current-system-evidence-to-action-readiness.md)
  - selection basis: Ali explicitly redirected the main post-Cycle-3 workstream to the current-system evidence-to-action audit and the bounded execution/learning journey derived from it.
  - execution owners: `../../plans/END_TO_END_PRODUCT_FLOW_LEARNING_AND_EVIDENCE_TO_ACTION_EXECUTION_PLAN.md` and its parent `../../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`; `../../MEMORY.md` alone owns the exact live slice.
  - current coordination boundary (2026-09-20): F3 and F9 are closed at their bounded proof horizons; F11 reconciles audit lifecycle metadata before the plan's action-relative evidence-producer/reachability comparison. AUDIT-008 remains non-controlling evidence, not a source of independent implementation authorization.

AUDIT-005 was moved from ACTIVE to SCHEDULED through AUDIT-008-F11. Its earlier agentic-evaluation findings and approved B2/X1 checkpoint are preserved, but they are **not the selected current engineering workstream**. See `../scheduled/README.md` for the concrete future handoff and correct owning plan.

Active audits remain **non-controlling evidence**. The active plan, specifications/ADRs where applicable, source/tests, and `MEMORY.md` own execution, stable decisions, behavior, and live continuation.

When an active audit is dispositioned, remove it from this index and add it to the appropriate lifecycle index under `../scheduled/`, `../deferred/`, or `../absorbed/` with an updated title and explicit rationale under `audits/LIFECYCLE.md`.
