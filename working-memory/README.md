# Working Memory

This directory contains detailed, public-safe records for individual UpgradePilot sessions, audits, investigations, major implementation responsibilities, and debugging steps.

## Relationship to other files

- `AGENTS.md` contains stable repository-wide AI operating instructions.
- `LEARNING-PREFERENCES.md` contains stable teaching, pacing, assessment, and learner-ownership preferences.
- `MEMORY.md` contains compact latest state and must remain below 200 lines.
- `working-memory/` preserves detailed progress, reasoning, evidence, and history.
- Canonical Career controls and trackers outrank all repository instruction and memory files.

## Naming

Use:

```text
YYYY-MM-DD_<session-or-step-id>_<short-topic>.md
```

Examples:

```text
2026-07-20_UP-S01_manual-evidence-investigation.md
2026-07-28_M2-S01_first-python-responsibility.md
2026-08-05_M3-S02_persistence-failure-diagnosis.md
```

## Start of work

Create or resume one record at the beginning of each meaningful work item. Include:

- date and session or step ID;
- status: `Active`;
- current route and milestone;
- authorized objective;
- starting repository and evidence state;
- expected output and pass condition;
- scope and stop line;
- relevant files and sources;
- Ali's initial prediction when required.

## During work

Update the record progressively with:

- concepts introduced and depth covered;
- decisions and rationale;
- commands, tool actions, and changed files;
- observed outputs and interpretations;
- failures, hypotheses, diagnoses, and corrections;
- tests, queries, comparisons, and evidence;
- assistance and ownership labels;
- blockers, deferred topics, and remaining uncertainty.

Do not rely on conversation context as the only record of material state. A short timely note is preferable to a reconstructed narrative after context is lost.

## Closure

Close the file as `Completed`, `Partial`, `Blocked`, `Invalid`, or `Superseded`.

Record:

- final result and pass-condition status;
- evidence, commit, or artifact references;
- demonstrated capability and depth;
- AI-generated or otherwise unowned work;
- remaining uncertainty or blocker;
- required canonical tracker update;
- `MEMORY.md` update;
- exact continuation or next action.

## Maintenance and safety

- Record observed events, decisions, and reasoning—not polished fictional summaries.
- Preserve failed, rejected, and superseded approaches when they materially explain the result.
- Reference canonical or large artifacts instead of duplicating them.
- Keep secrets, credentials, private data, medical or financial information, private logs, and unnecessary identifiers out of this public repository.
- Do not use working-memory records to authorize work or override a controlling artifact.
