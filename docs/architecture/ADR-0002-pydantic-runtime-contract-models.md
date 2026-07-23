# ADR-0002 — Pydantic for Runtime Contract Models

**Status:** Superseded  
**Original date:** 2026-07-21  
**Superseded:** 2026-07-23  
**Owner:** Ali Rajabi  
**Superseded by:** [`ADR-0003-clean-slate-b2-source-reset.md`](ADR-0003-clean-slate-b2-source-reset.md)

## Historical decision

M2 selected Pydantic v2 for strict boundary and trusted application contracts. The method
supported runtime validation, frozen typed models, structured errors, explicit adapters,
and machine-readable serialization for the then-active manual case/evidence/decision
slice.

The full original decision and its exact implementation remain available at:

```text
e7425dcfc20f093ac10c9a903f1c4ae50a8b2638
```

Archive record:

- [`../../archive/2026-07-23_PRE_B2_M2_IMPLEMENTATION.md`](../../archive/2026-07-23_PRE_B2_M2_IMPLEMENTATION.md)

## Why it no longer controls

D1 established a different first executable responsibility, and Ali directed the active
source to restart cleanly so that obsolete AI-generated classes, tests, and method choices
do not become the implicit B2 design or learning path.

Pydantic is therefore no longer an accepted B2 dependency or representation by inheritance.
It is not rejected. It may be reconsidered only after B1 freezes the new contract and
validation requirements and compares Pydantic with a simpler credible standard-library
baseline.

## Current authority

- ADR-0001 still controls the source/package layout.
- ADR-0003 controls the clean-slate source reset and archive boundary.
- The later accepted B1 responsibility and B2 plan will control new runtime contracts.

Historical passing tests and source code do not reactivate this ADR.