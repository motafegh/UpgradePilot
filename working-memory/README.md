# Working Memory

This directory contains detailed, public-safe records for individual UpgradePilot sessions, audits, investigations, major implementation responsibilities, and debugging steps.

## Relationship to other files

- `AGENTS.md` contains stable AI operating instructions.
- `MEMORY.md` contains compact latest state and must remain below 200 lines.
- `working-memory/` preserves detailed progress and history.
- Canonical Career controls and trackers outrank all memory files.

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
- blockers and remaining uncertainty.

Do not rely on the conversation context as the only record of material state.

## Closure

Close the file as `Completed`, `Partial`, `Blocked`, `Invalid`, or `Superseded`. Record the result, evidence or commit, demonstrated capability, unowned work, remaining uncertainty, required tracker update, `MEMORY.md` update, and exact next action.

## Maintenance and safety

- Record observed events, not polished fictional summaries.
- Preserve failed and rejected approaches when they matter.
- Keep secrets, private data, medical or financial information, private logs, and unnecessary identifiers out of this public repository.
- Reference large or canonical artifacts instead of duplicating them.
