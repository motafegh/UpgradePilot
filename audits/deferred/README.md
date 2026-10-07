# Deferred Audits

This folder is the **deferred lifecycle index** for validated audit questions or opportunities that remain useful but are not selected or scheduled for a specific implementation handoff.

Canonical audit records remain at stable paths directly under `audits/`; this index carries the lifecycle title/state without breaking the existing audit records' relative references.

Current deferred audits:

- [DEFERRED — AUDIT-004 — uv.lock Resolution-Satisfiability Evidence Boundary](../2026-08-16_AUDIT-004_uv-lock-resolution-satisfiability-evidence-boundary.md)

- [DEFERRED — AUDIT-010 — Hybrid Investigation Architecture Compatibility and Interface Delta](../2026-10-07_AUDIT-010_hybrid-investigation-architecture-compatibility.md)
  - Ali selected the hybrid direction. This lifecycle label applies to the unselected workspace/interface and implementation follow-ups, not to that direction decision.
  - Existing Core/Product Decision Model/ADR-0010/ADR-0011 semantics support the direction; no restatement ADR is needed. Re-enter concrete interface/method selection when the corresponding product responsibility is selected. No new Build plan or Investigator mechanism is selected by this review; `../../MEMORY.md` owns continuation.

Deferred does **not** mean rejected. Re-enter one only when its reassessment trigger becomes current, it is explicitly selected, or it is promoted into the scheduled lifecycle with a concrete activation trigger and owning plan. The audit remains non-controlling until the relevant responsibility owner is changed through the normal governance process.
