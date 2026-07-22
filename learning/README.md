# Learning Artifacts

This directory is the durable home for educational material created while building UpgradePilot.

It is not a transcript archive, a second tracker, or a substitute for working code, tests, scenario evidence, and exact project sources. Store only material that is useful for later understanding, recall, transfer, diagnosis, or ownership.

## Relationship to other areas

- `working-memory/` records what happened during a session or investigation.
- `learning/` records what should be understood and remembered afterward.
- `plans/` defines bounded project-local technical work.
- `product-simulation/` performs and preserves the current manual product-discovery runtime.
- `docs/` contains product, technical, architecture, and user-facing documentation.
- source and tests contain accepted executable behavior and verification.
- `MEMORY.md` contains compact current state and exact continuation.

A project source, working-memory record, and learning note may link to each other, but should not duplicate each other.

## Branch policy

Accepted learning artifacts belong on `main` beside the project behavior and evidence they explain.

Do not create a permanent learning branch. Use a short-lived session, feature, experiment, or repair branch only when the related work is unfinished or needs review. Merge the learning artifact with the relevant code, test, scenario, or evidence when they form one coherent change.

## Create or update a learning artifact when

- a required-core concept was meaningfully taught;
- an important misconception was corrected;
- a reusable mental model or terminology connection was established;
- a concept was applied to real UpgradePilot behavior;
- the material supports later recall, transfer, diagnosis, or ownership evidence;
- losing the explanation would materially weaken future work.

## Do not create a learning artifact merely because

- a small clarification was answered;
- one incidental supporting detail was mentioned;
- the material already exists accurately elsewhere;
- no durable understanding, correction, or reusable connection was produced;
- the result would only duplicate chat, project sources, or working memory.

## Organization

Create subdirectories only when a real learning responsibility requires them.

Current package styles include:

- milestone/session packages such as `m2-s02/`;
- separately governed domain packages such as `product-simulation/`;
- focused concept, mistake, recall, session, or diagram artifacts when they add durable value.

Do not force the current product-simulation learning into the paused M2-S03 package. Its authority, runtime scope, artifacts, cases, and ownership exercises form a separate learning domain.

Do not pre-create empty directory trees.

## Minimum useful content

A learning artifact should normally state:

- the concept or responsibility;
- the depth actually covered;
- the accurate mental model;
- one relevant UpgradePilot example or failure mode;
- important boundaries or trade-offs;
- what remains deferred;
- links to the related plan, source, case, test, working memory, or evidence;
- an explanation, trace, prediction, or ownership task when active practice is useful.

Use the smallest format that preserves the learning value. A short focused note is preferable to a polished document with no additional utility. A multi-file package is justified only when one file would collapse materially different learning responsibilities.

## Current learning packages

- [`product-simulation/`](product-simulation/) — **current separately governed learning domain.** It teaches the complete manual runtime, artifact lifecycle, evidence lineage and states, honest progressive execution, transparent baseline, decision/report/follow-up behavior, S001 and S002 case reasoning, cross-case synthesis, S003 causal-failure preparation, and ownership practice.
- [`m2-s02/`](m2-s02/) — closed semantic-extraction experiment and engineering retrospective. It teaches attributed evidence claims, mechanical grounding, model-derived authority, decision-effect evaluation, rejected controls, model failures, and the negative adoption result.
- [`m2-s03/`](m2-s03/) — paused evidence-to-report implementation orientation retained for later comparison. It is not the current learning entry point while manual product simulation controls project work.

## Depth and ownership discipline

- Exposure is not operational understanding.
- Operational understanding is not independent execution.
- Project ownership or artifact approval is not capability proof.
- AI-generated exercises and answers do not establish Ali-owned capability.
- Record the exact task scope, assistance, errors, correction, and demonstrated depth.
- Use the learning package's own stated depth scale where one exists.

## Maintenance

- Update an existing note instead of creating competing versions for the same concept.
- Keep assistance and demonstrated depth honest.
- Do not mark exposure as mastery.
- Keep all learning artifacts public-safe.
- Preserve negative experiments and material corrections; do not rewrite the learning history to make the path look cleaner than it was.
- Remove obsolete duplication while retaining the lesson that made the correction necessary.
- Reclassify a package when project authority changes instead of leaving a stale “current” entry point.
