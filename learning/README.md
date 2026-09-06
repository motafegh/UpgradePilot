# Learning Artifacts

This directory preserves reusable understanding produced while building UpgradePilot, including **AI-authored study/relearning material that Ali explicitly asks to create for later use**. It is not a transcript archive, second tracker, project-status owner, substitute for source and tests, or execution authority.

The sole live project position and continuation belong in [`../MEMORY.md`](../MEMORY.md). Learning packages may preserve dated or commit-pinned snapshots, but this index must not select the project stage, bounded plan, study order, or next action.

For the compact procedure that authors or materially revises reusable study/relearning artifacts, use [`../.agents/skills/upgradepilot-learning-artifact/SKILL.md`](../.agents/skills/upgradepilot-learning-artifact/SKILL.md). That Skill is a support/artifact-authoring procedure, not Learning-Only and not a new primary operation. Active interactive mastery remains governed by Learning-Only when Ali selects that mode.

## Snapshot policy

A snapshot is a frozen educational record tied to:

- a date;
- an exact source/test commit or otherwise explicit evidence horizon;
- an observed proof state;
- the concepts and ownership depth covered at that moment.

When later implementation materially changes the responsibility or mechanism:

1. keep the existing snapshot as historical learning evidence;
2. create a new dated or clearly versioned snapshot only when separately justified;
3. do not silently rewrite the old snapshot merely to match later code.

Correct an existing snapshot only for a factual error, unsafe instruction, or broken reference. Record the correction explicitly.

This preserves what was learned at each point without allowing an old package to redirect present work.

## Evidence-aware authoring

A learning artifact should teach the **best-supported current understanding**, not merely paraphrase whichever file is being studied.

For a material source/design/plan responsibility, use the smallest sufficient evidence chain:

```text
current canonical owner(s), when applicable
→ current source/tests/commands/evidence
→ directly relevant working-memory/history when it explains implementation path, meaningful engineering progression, errors, decisions, fixes, changed understanding, rejected alternatives, or deferrals
→ representative real UpgradePilot case/flow when available
→ learning artifact
```

Working-memory is historical/rationale evidence. It can preserve the meaningful engineering progression behind a responsibility—what was assumed or tried, what evidence or surprise appeared, what failed or changed, how understanding was corrected, and how the resulting mechanism/decision/proof state was reached. A learning artifact may selectively synthesize that progression when it materially improves understanding, but should extract the mechanism, reasoning transition, or lesson rather than reproduce the session chronology.

Working-memory does not override current source, accepted specifications/ADRs/plans, or newer evidence. Do not scan all working-memory reflexively; retrieve only records that materially help reconstruct the selected responsibility.

Keep these questions distinct when writing:

```text
WHAT THE PROJECT CURRENTLY DOES
WHY THE EVIDENCE SHOWS THAT
WHY IT WAS DESIGNED THAT WAY, when the rationale is actually evidenced
HOW THE ENGINEERING UNDERSTANDING EVOLVED, when that progression materially improves learning
WHETHER THE CURRENT DESIGN/IMPLEMENTATION IS CORRECT OR WELL-JUSTIFIED
WHAT CREDIBLE ALTERNATIVES / IMPROVEMENTS EXIST
```

Never invent a design rationale merely because current code needs an explanation. If the material appears defective, stale, contradictory, unnecessary, misleading, or otherwise questionable, inspect the relevant owners/evidence proportionately and say what is established versus uncertain. When the question becomes materially evaluative, compose the Repository-Audit procedure; authoring a learning artifact does **not** itself authorize product/source/test repair.

## Real-project teaching substrate

Use real UpgradePilot material by default:

- product-simulation cases and real repository/user scenarios;
- actual producer → transformation → consumer flows;
- real source objects/functions/types;
- real failure/debugging incidents;
- focused tests and their proof/non-proof boundaries;
- actual plan/design/ADR decisions and trade-offs.

A tiny toy example may be used as an explanatory microscope for isolated syntax/API behavior, but reconnect it immediately to the actual UpgradePilot mechanism. Do not replace an available real teaching substrate with a detached generic tutorial.

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

This pattern describes learning during real work; a requested learning artifact may be authored for later study without requiring an interactive lesson, quiz, learner response, or ownership demonstration in the authoring session.

## Depth labels and learning depth

Snapshot records may use these demonstrated-depth labels:

- **introduced** — terminology and broad mechanism recognized;
- **operationally understood with guidance** — a bounded flow can be traced and used safely with support;
- **implementation-adjacent** — source and tests can be read and evaluated with guidance;
- **ownership practice** — one central behavior was predicted, modified or tested, executed, and explained;
- **independently demonstrated** — the responsibility is controlled across changed cases with limited assistance.

Approval, passive reading, execution of AI-written code, or passing tests alone is not mastery.

When deciding **what depth the artifact itself should teach**, use the project-wide ownership model from `OPERATING_GUIDE.md` rather than inventing a competing taxonomy:

- **must master / own** — central engineering responsibility, mechanism, boundary, or decision;
- **understand operationally** — enough to read, reason about, modify, debug, review, or safely use the mechanism;
- **recognize / lookup-level** — understand what an incidental syntax/library/API construct is doing here and know how to recover exact details when needed;
- **deferred deliberately** — real depth that does not unlock the selected responsibility now.

Engineering ownership is not unaided source reproduction from memory.

## What belongs in a learning artifact

Create or update one only when it preserves a material:

- concept or mechanism;
- corrected misconception;
- transfer model;
- failure diagnosis;
- ownership exercise;
- explanation that would otherwise be lost and would weaken future work;
- requested study/relearning guide for a real project responsibility.

A useful artifact normally makes recoverable, as applicable:

- purpose, subject, and source/snapshot identity;
- the responsibility and non-responsibility boundary;
- the accurate big-picture mental model;
- one representative real UpgradePilot case, user flow, data flow, control flow, or failure path;
- important invariants, trust/authority boundaries, and trade-offs;
- material syntax/library/API mechanisms at the depth actually needed;
- current implementation fact versus evidenced rationale versus engineering judgment;
- tests/evidence and explicit non-claims;
- known issues, fixes, alternatives, or unresolved questions when materially useful;
- meaningful engineering progression/history when it materially explains how a mechanism, decision, correction, or lesson emerged;
- what must be mastered versus understood operationally, lookup-level, or deferred;
- related source, tests, plan/design/history/evidence anchors;
- a short **fast relearning route**;
- a few recall/transfer/modification/test/diagnosis prompts when they materially improve later study.

Adapt the shape to the subject. A source-code note, plan-learning guide, architecture/design note, concept/API companion, and end-to-end flow walkthrough do not need identical sections. Do not add a chronological-history section merely because relevant Working Memory exists.

## Size and package proportionality

Target the **smallest complete study artifact**:

```text
superficial summary
→ too little mechanism/context to learn from

minimum-complete focused note
→ preferred

exhaustive tutorial/document dump
→ too expensive to study or revisit
```

Prefer one focused file when one coherent responsibility can be learned usefully in one note. Prefer a small ordered package only when several genuinely distinct learning responsibilities would make one file difficult to study or revisit.

Do not create a package, contract, plan, depth map, learning memory, glossary, quiz set, or index merely for symmetry or professionalism. Existing package-local structures remain valid where their real continuity/learning responsibility justifies them.

A strong artifact should also support fast return weeks later. A useful relearning route is often:

```text
recall the core mental model
→ open 1–3 exact source/plan locations
→ trace one real representative flow
→ inspect one or two proof anchors
→ answer a few ownership questions
```

## Relationship to other areas

- `learning/` — reusable understanding and frozen educational snapshots;
- `working-memory/` — detailed dated engineering progression/session history, reasoning/evidence, discoveries, errors, decisions, corrections, and time-scoped handoff that may inform a learning artifact;
- `plans/` — position-neutral scope, proof, and stop conditions;
- source and tests — implemented truth and executable claims;
- specifications/ADRs — accepted stable semantics and consequential method/structure;
- `MEMORY.md` — sole live project position and continuation;
- `archive/` — immutable historical implementation references;
- `product-simulation/` — discovery evidence and real cases that may provide high-value learning substrates.

Link to owners rather than copying their full contracts.

## Existing learning packages

- [`2026-09-06-bounded-evidence-gap-planning-and-orchestration/`](2026-09-06-bounded-evidence-gap-planning-and-orchestration/) — two evidence-bounded learning snapshots completing the ordinary-Python execution/state/trace/replay responsibility, framework-neutral semantic comparison, independent LangGraph design and coupling correction, real pydantic proof, framework value/cost findings, and the current product-driven framework deferral/re-entry boundary at source/test horizon `d9c637b...`;
- [`2026-09-01-b2-x1-r4-evidence-gap-planner/`](2026-09-01-b2-x1-r4-evidence-gap-planner/) — two compact, commit-pinned study notes for A1→A3→A2 ownership and the real S001 composition/live-A3 flow at source snapshot `2467bf1...`;
- [`2026-08-15-tranche1-real-case-code-flows/01_S001_NORMAL_APPLICATION_END_TO_END.md`](2026-08-15-tranche1-real-case-code-flows/01_S001_NORMAL_APPLICATION_END_TO_END.md) — implementation-adjacent S001 walkthrough pinned to accepted Tranche-1 source `ef4283db...`, tracing the normal public-PR application path and the independent unresolved CI branch without turning it into a universal verdict;
- [`2026-08-15-tranche1-real-case-code-flows/02_S011_OPTIONAL_EXTRA_PROOF_BOUNDARY_END_TO_END.md`](2026-08-15-tranche1-real-case-code-flows/02_S011_OPTIONAL_EXTRA_PROOF_BOUNDARY_END_TO_END.md) — S011 workflow-evidence walkthrough pinned to the same accepted source, contrasting real optional-extra discovery evidence with current provider/consumer capabilities and explicit application gaps;
- [`2026-08-10-seven-concept-foundation-pre-a-c-implementation.md`](2026-08-10-seven-concept-foundation-pre-a-c-implementation.md) — focused study guide for the seven minimum concepts needed before implementation-adjacent A→C work: evidence/authority, completeness, logic, impact candidates, applicability, investigation selection, and deterministic/semantic responsibility;
- [`2026-08-10-product-decision-model-a-b-c-mastery-note.md`](2026-08-10-product-decision-model-a-b-c-mastery-note.md) — cumulative dated mastery/relearning snapshot of the product-decision-model journey through Conversation-C closure, pinned to reconciliation commit `7fedd79ecc97c71d025fd36bc4a0cfc31727a885`;
- [`2026-07-24-b2-public-pr-through-ci-authority/`](2026-07-24-b2-public-pr-through-ci-authority/) — dated snapshot pinned to its recorded source/test state;
- [`b2-pr-acquisition-and-pinned-extraction/`](b2-pr-acquisition-and-pinned-extraction/) — earlier bounded B2 snapshot;
- [`product-simulation/`](product-simulation/) — discovery lessons and ownership exercises from S001–S005;
- [`m2-s02/`](m2-s02/) — historical semantic-extraction and model-evaluation experiment;
- [`m2-s03/`](m2-s03/) — superseded report-first orientation;
- [`concepts/`](concepts/) — earlier concept notes retained for their historical scope.

Historical packages do not control implementation or continuation. Consult one only when `MEMORY.md` or a selected responsibility names a precise comparison question, or when Ali explicitly asks to study/relearn that historical material.

## Safety and maintenance

- Keep learning artifacts public-safe.
- Do not include credentials, private logs, personal data, or unnecessary identifiers.
- Do not use learning notes to authorize implementation or override controlling plans.
- Do not claim safety, production readiness, recommendation correctness, or ownership beyond observed evidence.
- Do not silently teach questionable current code as correct merely because it exists.
- Remove obsolete live-state duplication while preserving material dated history.