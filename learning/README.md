# Learning Artifacts

This directory preserves reusable understanding produced while building UpgradePilot.
It is not a transcript archive, second tracker, or substitute for source, tests, plans,
scenario evidence, or working memory.

## Current learning route

The controlling project route is
[`../plans/UPGRADEPILOT_90_DAY_PLAN.md`](../plans/UPGRADEPILOT_90_DAY_PLAN.md).

Current stage:

> **B1 — Implementation responsibility freeze**

D1 was accepted on 2026-07-23. The S001–S005 package remains the evidence and learning
foundation for B1, but no additional simulation lesson is required merely to continue.

Current B1 sources:

- [`../plans/D1_ACCEPTANCE_AND_B1_ACTIVATION.md`](../plans/D1_ACCEPTANCE_AND_B1_ACTIVATION.md)
- [`../plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md`](../plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md)
- [`../product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](../product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md)
- current source and tests.

## Current learning responsibility

B1 learning should occur through actual implemented-truth inspection:

```text
inspect current behavior
→ predict what the code should own
→ trace source and tests
→ identify mismatch with accepted runtime responsibilities
→ classify retain/correct/supersede/experimental
→ explain the smallest credible executable boundary
→ define tests and ownership work
```

The current learning objective is not to memorize the five cases. It is to transfer their
principles into a bounded implementation responsibility.

Ali should practise:

- tracing one current input-to-output path in the existing code;
- identifying where semantics are caller-supplied or missing;
- distinguishing current implemented truth from old plans;
- deciding whether a component should be retained, corrected, or superseded;
- explaining universal versus conditional runtime behavior;
- defining what replay input may prepare versus what B2 must execute;
- challenging premature schema, persistence, model, service, or architecture choices;
- defining meaningful B2 tests and a central Ali-owned change.

## Product-simulation package

[`product-simulation/`](product-simulation/) preserves:

- the complete runtime and artifact lifecycle;
- evidence identity, lineage, states, and authority;
- CI responsibility and causal attribution;
- baseline sufficiency and wrong-action behavior;
- stopping and conditional-stage behavior;
- ownership exercises for S001–S005.

Its demonstrated depth remains primarily AI-produced and implementation-adjacent. Ali's
D1 acceptance is a planning decision, not proof of mastery.

## Historical packages

- [`m2-s02/`](m2-s02/) — closed semantic-extraction experiment and negative adoption
  evidence;
- [`m2-s03/`](m2-s03/) — superseded report-first implementation orientation, retained
  only for B1 comparison.

Do not reactivate M2-S03.

## Learning-by-building pattern

```text
minimum accurate explanation
→ Ali prediction or challenge
→ bounded investigation or implementation
→ evidence inspection
→ diagnosis and correction
→ Ali-owned change or test
→ explanation of the complete path and limits
```

Record actual depth:

- introduced;
- operationally understood with guidance;
- modified or tested with guidance;
- diagnosed with review;
- independently controlled at a stated scope.

Approval or execution of AI-provided work is not mastery.

## Artifact rules

Create or update a learning artifact only when it preserves a material concept,
correction, transfer, diagnosis, or ownership exercise that would otherwise be lost.

Prefer one focused note over a ceremonial package. Link to owning plans, evidence, source,
and tests rather than duplicating them.
