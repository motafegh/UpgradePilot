# Learning Artifacts

This directory preserves reusable understanding produced while building UpgradePilot. It is
not a transcript archive, second tracker, or substitute for source, tests, plans, scenario
evidence, or working memory.

## Current learning route

The controlling project route is
[`../plans/UPGRADEPILOT_90_DAY_PLAN.md`](../plans/UPGRADEPILOT_90_DAY_PLAN.md).

Current stage:

> **B1 — Clean-slate implementation responsibility freeze**

D1 was accepted on 2026-07-23. The S001–S005 package remains the evidence foundation, but
no additional simulation lesson is required merely to continue.

Current B1 sources:

- [`../plans/D1_ACCEPTANCE_AND_B1_ACTIVATION.md`](../plans/D1_ACCEPTANCE_AND_B1_ACTIVATION.md)
- [`../plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md`](../plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md)
- [`../plans/B1_CURRENT_SOURCE_AND_TEST_RECONCILIATION.md`](../plans/B1_CURRENT_SOURCE_AND_TEST_RECONCILIATION.md)
- [`../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md`](../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md)
- active `pyproject.toml`, `src/upgradepilot/__init__.py`, and `tests/README.md`.

## Current learning responsibility

The old M2 source is not the teaching baseline. It is archived because reverse-engineering
and modifying substantially AI-generated code would blur the new responsibility and Ali's
learning.

Current learning proceeds from the product responsibility:

```text
understand one complete blocking concept
→ predict the required behavior
→ define the smallest contract or invariant
→ write a fresh bounded implementation
→ write or modify a meaningful test
→ run and inspect evidence
→ diagnose a defect
→ explain authority, stopping, and limits
```

Before B2 code begins, Ali should understand and challenge:

- why invocation and frozen case identity differ;
- why run identity and record identity are needed;
- what evidence states and provenance must preserve;
- why observations, interpretations, findings, and decisions must not collapse;
- what the transparent baseline owns;
- why conditional responsibilities must be inactive when unnecessary;
- why reports are projections of accepted state rather than independent truth;
- what replay fixtures may prepare and what runtime behavior must remain deterministic;
- why no dependency or class structure is inherited from M2;
- why the selected B2 responsibility is complete but still the smallest credible core.

## Clean-source ownership rule

The exact pre-reset implementation remains at commit
`e7425dcfc20f093ac10c9a903f1c4ae50a8b2638` and is indexed by
[`../archive/2026-07-23_PRE_B2_M2_IMPLEMENTATION.md`](../archive/2026-07-23_PRE_B2_M2_IMPLEMENTATION.md).

Do not:

- use archived modules as examples during ordinary implementation;
- copy archived tests;
- inherit Pydantic, OpenAI, model clients, class names, or file boundaries;
- treat old passing tests as evidence of current skill or coverage.

Consult an archived lesson only when the current responsibility names a precise comparison
question.

## Product-simulation package

[`product-simulation/`](product-simulation/) preserves:

- the complete runtime and artifact lifecycle;
- evidence identity, lineage, states, and authority;
- CI responsibility and causal attribution;
- baseline sufficiency and wrong-action behavior;
- stopping and conditional-stage behavior;
- ownership exercises for S001–S005.

Its demonstrated depth remains primarily AI-produced and implementation-adjacent. Ali's D1
acceptance is a planning decision, not proof of mastery.

## Historical packages

- [`m2-s02/`](m2-s02/) — archived semantic-extraction and model-evaluation experiment;
- [`m2-s03/`](m2-s03/) — superseded report-first orientation.

Neither package controls current implementation or learning order.

## Learning-by-building pattern

```text
minimum accurate explanation
→ Ali prediction or challenge
→ fresh bounded implementation
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

Create or update a learning artifact only when it preserves a material concept, correction,
transfer, diagnosis, or ownership exercise that would otherwise be lost. Prefer one focused
note over a ceremonial package. Link to owning plans, evidence, active source, and active
tests rather than duplicating them.