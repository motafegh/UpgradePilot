# Learning Artifacts

This directory preserves reusable understanding produced while building UpgradePilot. It is not a transcript archive, second tracker, or substitute for source, tests, plans, implementation evidence, or working memory.

## Current learning route

The controlling project route is [`../plans/UPGRADEPILOT_90_DAY_PLAN.md`](../plans/UPGRADEPILOT_90_DAY_PLAN.md).

Current stage:

> **B2 — Public PR vertical slice**

Current bounded plan:

- [`../plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](../plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- [`../working-memory/B2_TECHNICAL_PROGRESS.md`](../working-memory/B2_TECHNICAL_PROGRESS.md)
- active source, tests, commands, outputs, and environment for implemented truth.

## Current study snapshot

- [`b2-pr-acquisition-and-pinned-extraction/`](b2-pr-acquisition-and-pinned-extraction/) — the validated B2 path from public PR input through complete changed-file acquisition and one exact pinned dependency update.

This snapshot prepares the remaining Ali-owned normalized-package test before exact-head CI acquisition begins.

## Stage-snapshot policy

A stage snapshot is a frozen educational record tied to:

- a date;
- an exact source/test commit;
- an observed proof state;
- the concepts and ownership depth required at that moment.

When later implementation materially changes the responsibility or mechanism:

1. keep the existing snapshot as historical learning evidence;
2. create a new dated or clearly versioned snapshot;
3. link the new snapshot from this index;
4. do not silently rewrite the old snapshot merely to match current code.

Correct an existing snapshot only for a factual error, unsafe instruction, or broken reference. Record the correction explicitly.

This preserves what was learned at each stage and prevents later implementation from making older study material appear more advanced than it really was.

## Learning-by-building pattern

```text
minimum accurate explanation
→ Ali prediction or challenge
→ fresh bounded implementation or test
→ evidence inspection
→ diagnosis and correction
→ Ali-owned change or test
→ explanation of the complete path and limits
```

Teach through the real product responsibility. Do not study every source line equally.

## Depth labels

Record only the depth demonstrated:

- **introduced** — terminology and broad mechanism recognized;
- **operationally understood with guidance** — current flow can be traced and used safely with support;
- **implementation-adjacent** — source and tests can be read and evaluated with guidance;
- **ownership practice** — one central behavior was predicted, modified or tested, executed, and explained;
- **independently demonstrated** — the responsibility is controlled across changed cases with limited assistance.

Approval, passive reading, execution of AI-written code, or passing tests alone is not mastery.

## What belongs in a learning artifact

Create or update one only when it preserves a material:

- concept or mechanism;
- corrected misconception;
- transfer model;
- failure diagnosis;
- ownership exercise;
- explanation that would otherwise be lost and would weaken future work.

A useful artifact normally states:

- the responsibility and exact depth covered;
- the accurate mental model;
- one UpgradePilot example or failure mode;
- important invariants, boundaries, and trade-offs;
- what must be mastered now versus understood operationally or deferred;
- related source, tests, plan, evidence, and snapshot commit;
- one recall, transfer, modification, test, or diagnosis action.

Prefer several focused files with clear study order over one document too long to use. Do not create a ceremonial package when one focused note is sufficient.

## Relationship to other areas

- `learning/` — what should be understood and remembered;
- `working-memory/` — what materially happened during execution;
- `plans/` — authorized scope, proof, and stop conditions;
- source and tests — implemented truth and executable claims;
- `MEMORY.md` — concise current continuation;
- `archive/` — immutable historical implementation references;
- `product-simulation/` — completed discovery evidence.

Link to owners rather than duplicating them.

## Existing learning packages

- [`product-simulation/`](product-simulation/) — discovery lessons and ownership exercises from S001–S005;
- [`m2-s02/`](m2-s02/) — historical semantic-extraction and model-evaluation experiment;
- [`m2-s03/`](m2-s03/) — superseded report-first orientation;
- [`concepts/`](concepts/) — earlier concept notes retained for their historical scope.

Historical packages do not control current implementation or learning order. Consult them only when an active responsibility names a precise comparison question.

## Safety and maintenance

- Keep learning artifacts public-safe.
- Do not include credentials, private logs, personal data, or unnecessary identifiers.
- Do not use learning notes to authorize implementation or override controlling plans.
- Do not claim safety, production readiness, recommendation correctness, or ownership beyond observed evidence.
- Remove obsolete duplication, but preserve material corrections and stage history.