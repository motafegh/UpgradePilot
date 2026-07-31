# Learning Artifacts

This directory preserves reusable understanding produced while building UpgradePilot. It is
not a transcript archive, second tracker, project-status owner, substitute for source and
tests, or execution authority.

The sole live project position and continuation belong in [`../MEMORY.md`](../MEMORY.md).
Learning packages may preserve dated or commit-pinned snapshots, but this index must not
select the project stage, bounded plan, study order, or next action.

## Snapshot policy

A snapshot is a frozen educational record tied to:

- a date;
- an exact source/test commit;
- an observed proof state;
- the concepts and ownership depth covered at that moment.

When later implementation materially changes the responsibility or mechanism:

1. keep the existing snapshot as historical learning evidence;
2. create a new dated or clearly versioned snapshot only when separately justified;
3. do not silently rewrite the old snapshot merely to match later code.

Correct an existing snapshot only for a factual error, unsafe instruction, or broken
reference. Record the correction explicitly.

This preserves what was learned at each point without allowing an old package to redirect
present work.

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
- **operationally understood with guidance** — a bounded flow can be traced and used safely with support;
- **implementation-adjacent** — source and tests can be read and evaluated with guidance;
- **ownership practice** — one central behavior was predicted, modified or tested, executed, and explained;
- **independently demonstrated** — the responsibility is controlled across changed cases with limited assistance.

Approval, passive reading, execution of AI-written code, or passing tests alone is not
mastery.

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
- what must be mastered versus understood operationally or deferred within the snapshot;
- related source, tests, plan, evidence, and snapshot commit;
- one recall, transfer, modification, test, or diagnosis action.

Prefer several focused files with clear internal order over one document too long to use. Do
not create a ceremonial package when one focused note is sufficient.

## Relationship to other areas

- `learning/` — reusable understanding and frozen educational snapshots;
- `working-memory/` — dated records of material execution;
- `plans/` — position-neutral scope, proof, and stop conditions;
- source and tests — implemented truth and executable claims;
- `MEMORY.md` — sole live project position and continuation;
- `archive/` — immutable historical implementation references;
- `product-simulation/` — completed discovery evidence.

Link to owners rather than duplicating them.

## Existing learning packages

- [`2026-07-31-b2-evidence-pipeline-mastery/`](2026-07-31-b2-evidence-pipeline-mastery/) — branch-isolated, baseline-pinned plan for learning the active B2 evidence pipeline and later implementation deltas;
- [`2026-07-24-b2-public-pr-through-ci-authority/`](2026-07-24-b2-public-pr-through-ci-authority/) — dated snapshot pinned to its recorded source/test state;
- [`b2-pr-acquisition-and-pinned-extraction/`](b2-pr-acquisition-and-pinned-extraction/) — earlier bounded B2 snapshot;
- [`product-simulation/`](product-simulation/) — discovery lessons and ownership exercises from S001–S005;
- [`m2-s02/`](m2-s02/) — historical semantic-extraction and model-evaluation experiment;
- [`m2-s03/`](m2-s03/) — superseded report-first orientation;
- [`concepts/`](concepts/) — earlier concept notes retained for their historical scope.

Historical packages do not control implementation or continuation. Consult one only when
`MEMORY.md` or a selected responsibility names a precise comparison question.

## Safety and maintenance

- Keep learning artifacts public-safe.
- Do not include credentials, private logs, personal data, or unnecessary identifiers.
- Do not use learning notes to authorize implementation or override controlling plans.
- Do not claim safety, production readiness, recommendation correctness, or ownership beyond observed evidence.
- Remove obsolete live-state duplication while preserving material dated history.