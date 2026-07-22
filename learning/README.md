# Learning Artifacts

This directory is the durable home for educational material created while building UpgradePilot.

It is not a transcript archive, a second tracker, or a substitute for working code and tests. Store only material that is useful for later understanding, recall, transfer, diagnosis, or ownership.

## Relationship to other areas

- `working-memory/` records what happened during a session or investigation.
- `learning/` records what should be understood and remembered afterward.
- `plans/` defines bounded project-local technical work.
- `docs/` contains product, technical, architecture, and user-facing documentation.
- source and tests contain accepted executable behavior and verification.
- `MEMORY.md` contains compact current state and exact continuation.

A working-memory record and a learning note may link to each other, but should not duplicate each other.

## Branch policy

Accepted learning artifacts belong on `main` beside the project behavior and evidence they explain.

Do not create a permanent learning branch. Use a short-lived session, feature, experiment, or repair branch only when the related work is unfinished or needs review. Merge the learning artifact with the relevant code, test, or evidence when they form one coherent change.

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
- the result would only duplicate chat or working memory.

## Optional organization

Create subdirectories only when a real artifact requires them. Suggested categories are:

- `concepts/` — durable concept and mechanism notes;
- `session-notes/` — consolidated educational outcomes from a formal session;
- `mistakes/` — corrected misconceptions worth revisiting;
- `recall/` — reusable recall and transfer prompts;
- `diagrams/` — durable learning diagrams and data flows.

Do not pre-create empty directory trees.

## Minimum useful content

A learning artifact should normally state:

- the concept or responsibility;
- the depth actually covered;
- the accurate mental model;
- one relevant UpgradePilot example or failure mode;
- important boundaries or trade-offs;
- what remains deferred;
- links to the related plan, working memory, code, tests, or evidence.

Use the smallest format that preserves the learning value. A short focused note is preferable to a polished document with no additional utility.

## Current learning packages

- [`m2-s02/`](m2-s02/) — closed semantic-extraction experiment and engineering retrospective. It teaches attributed evidence claims, mechanical grounding, model-derived authority, decision-effect evaluation, rejected controls, model failures, and the reasoning that led to a negative adoption result.
- [`m2-s03/`](m2-s03/) — current evidence-to-report orientation. It distinguishes foundations that already exist from report composition and rendering behavior that remains planned.

## Maintenance

- Update an existing note instead of creating competing versions for the same concept.
- Keep assistance and demonstrated depth honest.
- Do not mark exposure as mastery.
- Keep all learning artifacts public-safe.
- Preserve negative experiments and material corrections; do not rewrite the learning history to make the path look cleaner than it was.
- Remove obsolete duplication while retaining the lesson that made the correction necessary.
