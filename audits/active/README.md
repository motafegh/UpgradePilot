# Active Audits

This folder is the **active lifecycle index** for validated audit findings selected as inputs to the current engineering responsibility.

Canonical audit records remain at stable paths directly under `audits/`. Existing audits contain relative references written from that location, so lifecycle classification is represented here instead of physically relocating those files and silently breaking their reproducibility links.

Current active audits:

- [ACTIVE — AUDIT-018 — Cross-domain Remediation Priorities and Dependency Order](../2026-10-20_AUDIT-018_cross-domain-remediation-priorities.md)
  - selection basis: the dedicated project-wide audit/correction branch completed governance, product-value, architecture, proof and Investigator-methodology passes and consolidated their surviving findings into one remediation order.
  - execution owner: [Project-wide Technical Audit and Correction Program Plan](../../plans/PROJECT_WIDE_TECHNICAL_AUDIT_AND_CORRECTION_PROGRAM_PLAN.md). The current selected responsibility is Wave 1 truth/lifecycle/governance correction on `audit/project-wide-system-audit-2026-10-20`; later proof, Workspace-cutover and semantic-experiment waves remain gated by their named prerequisites.
  - latest reconciled upstream horizon: `main@bfcc8b916fc33523a535f7c5a994d118d09552b8`. Main's parallel product-value plan revision is convergent input that still requires semantic reconciliation before final integration.

AUDIT-009, AUDIT-010 and AUDIT-011 are no longer current engineering inputs and have been moved to ABSORBED. Their dated evidence remains immutable and continues to support the later architecture/experiment conclusions. AUDIT-012 through AUDIT-017 are also ABSORBED into AUDIT-018 for lifecycle purposes; they remain the detailed stage evidence behind the consolidated disposition.

AUDIT-005 remains SCHEDULED and is not the selected current engineering workstream unless its activation condition is separately re-established by the live owner.

Active audits remain **non-controlling evidence**. The active plan, specifications/ADRs where applicable, source/tests, and `MEMORY.md` own execution, stable decisions, behavior, and live continuation.

When an active audit is dispositioned, remove it from this index and add it to the appropriate lifecycle index under `../scheduled/`, `../deferred/`, or `../absorbed/` with an updated title and explicit rationale under `audits/LIFECYCLE.md`.
