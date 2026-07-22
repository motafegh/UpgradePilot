# Learning Artifacts

This directory preserves educational material produced while building
UpgradePilot. It is not a transcript archive, a second tracker, or a substitute
for source, tests, scenario evidence, plans, and working memory.

## Relationship to other areas

- `plans/` owns the project route and current bounded implementation work.
- `product-simulation/` owns current manual product-discovery execution.
- `working-memory/` records material execution and investigation evidence.
- `learning/` preserves reusable understanding, corrections, transfer,
  diagnosis, and ownership practice.
- source and tests own implemented behavior.
- `MEMORY.md` owns concise continuation.

Link across these areas; do not duplicate their complete contents.

## Current learning route

The controlling project route is
[`../plans/UPGRADEPILOT_90_DAY_PLAN.md`](../plans/UPGRADEPILOT_90_DAY_PLAN.md).

Current stage: **D1 — contrast closure; S004 complete, S005 remaining**.

Current learning entry point:

- [`product-simulation/`](product-simulation/) — complete runtime, artifact
  lifecycle, evidence authority, baseline comparison, causal attribution,
  sufficiency/stopping, cost, action divergence, and ownership exercises for
  S001–S005.

Current focused lesson:

- [`product-simulation/11_S004_BASELINE_SUFFICIENCY_AND_STOPPING.md`](product-simulation/11_S004_BASELINE_SUFFICIENCY_AND_STOPPING.md)
  — why a baseline can be sufficient only after its authority-critical assumptions
  are confirmed, and why declining deeper investigation is an affirmative technical
  decision.

Historical packages:

- [`m2-s02/`](m2-s02/) — closed semantic-extraction experiment and negative
  adoption evidence;
- [`m2-s03/`](m2-s03/) — superseded report-first implementation orientation,
  retained only for later B1 comparison.

Do not reactivate M2-S03. Future implementation learning will be organized around
the accepted B2 runtime responsibility after the D1/B1 gates.

## Create or update a learning artifact when

- a required-core concept was meaningfully taught;
- an important misconception was corrected;
- a reusable mental model was established;
- a concept was applied to real UpgradePilot behavior;
- the material supports later recall, transfer, diagnosis, or ownership;
- losing it would materially weaken future work.

Do not create one merely because a small clarification occurred or because a
polished document looks complete.

## Learning-by-building pattern

A central responsibility should normally produce:

```text
minimum accurate explanation
→ Ali prediction or challenge
→ bounded investigation or implementation
→ evidence inspection
→ diagnosis and correction
→ Ali-owned change or test
→ explanation of the complete path, stopping point, and limits
```

Record the actual depth:

- introduced;
- operationally understood with guidance;
- modified or tested with guidance;
- diagnosed with review;
- independently controlled at a stated scope.

Do not mark exposure, repetition, approval, or execution of AI-provided steps as
mastery.

## Organization

Create subdirectories only when a real learning responsibility requires them.
Prefer one focused note over a ceremonial package. A multi-file package is justified
when one file would collapse materially different concepts or ownership exercises.

A useful artifact normally states:

- concept or responsibility;
- depth covered;
- accurate mental model;
- relevant UpgradePilot example or failure;
- important boundaries and deferred depth;
- links to owning evidence, plan, source, test, or working record;
- a prediction, explanation, trace, diagnosis, stop decision, or modification task
  when useful.

## Maintenance

- update an existing note rather than create competing versions;
- preserve negative experiments and corrections;
- keep assistance and demonstrated depth honest;
- keep artifacts public-safe;
- reclassify packages when project authority changes;
- remove obsolete duplication while retaining the lesson that justified the
  correction.
