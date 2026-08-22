# Active Audits

This folder is the **active lifecycle index** for validated audit findings selected as inputs to the current engineering responsibility.

Canonical audit records remain at stable paths directly under `audits/`. Existing audits contain relative references written from that location, so lifecycle classification is represented here instead of physically relocating those files and silently breaking their reproducibility links.

Current active audits:

- [ACTIVE — AUDIT-001 — Exact PR File Acquisition Evidence Contract](../2026-08-01_AUDIT-001_exact-pr-file-acquisition-evidence-contract.md)
- [ACTIVE — AUDIT-006 — Internal Evidence Type Strength and Revalidation Boundaries](../2026-08-21_AUDIT-006_internal-evidence-type-strength-and-revalidation-boundaries.md)
- [ACTIVE — AUDIT-007 — uv Membership Proposition and Lock-Model Boundaries](../2026-08-22_AUDIT-007_uv-membership-proposition-and-lock-model-boundaries.md)

These remain **non-controlling evidence**. The active plan, specifications/ADRs where applicable, source/tests, and `MEMORY.md` own execution, stable decisions, behavior, and live continuation.

When an active audit is dispositioned, remove it from this index and add it to either `../absorbed/README.md` or `../deferred/README.md` with an updated lifecycle title.
