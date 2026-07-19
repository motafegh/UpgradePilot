# Working Memory

This directory contains detailed, public-safe records for formal UpgradePilot sessions, audits, investigations, major implementation responsibilities, and material debugging work.

Working memory preserves continuity and evidence. It must not turn every small interaction into ceremony.

## Relationship to other files

- `AGENTS.md` contains stable repository-wide AI operating instructions.
- `LEARNING-PREFERENCES.md` contains stable teaching, pacing, assessment, and learner-ownership preferences.
- `MEMORY.md` contains compact latest state and must remain below 200 lines.
- `working-memory/` records what happened during material work.
- `learning/` records what should be understood and remembered afterward.
- `plans/` coordinates future detailed technical work when a plan is justified.
- Canonical Career controls and trackers outrank all repository instruction and memory files.

## Decide: create, reuse, or skip

### Create one record when

- a new formal session or authorized responsibility begins;
- work is likely to continue across conversations;
- accepted repository behavior or state may change;
- a material product, architecture, dependency, security, or evidence decision must be preserved;
- an investigation has several steps or competing hypotheses;
- capability, assistance, or ownership will be assessed;
- a milestone, gate, blocker, or exact next action may change;
- losing the reasoning trail would materially damage continuity or auditability.

### Reuse the active record when

- continuing the same session or responsibility;
- teaching another concept chunk within the active plan;
- adding a localized test or implementation step;
- diagnosing a focused failure inside the same investigation;
- making an Ali-directed change already covered by the active boundary.

Do not create a new record per concept, command, error, chat, or small edit.

### Skip working memory when

- answering a small explanation or clarification;
- discussing an idea without making a material decision;
- explaining one line of code or one command without consequential execution;
- making a small reversible edit already covered by active work;
- correcting wording or formatting;
- no persistent state, evidence, ownership, gate, blocker, or continuation changes.

If a lightweight interaction unexpectedly becomes material, create or activate a record at that point and capture the relevant context. Do not reconstruct unnecessary detail from the beginning.

## Reading discipline

Use this order:

1. read `MEMORY.md`;
2. read the active working-memory record, if one exists;
3. read the controlling plan and directly relevant files;
4. open historical records only when `MEMORY.md`, the active record, provenance, or the current question points to them.

Do not scan every historical record speculatively.

## Naming

Use:

```text
YYYY-MM-DD_<session-or-step-id>_<short-topic>.md
```

Examples:

```text
2026-07-20_M2-S01_case-identity-normalization.md
2026-08-05_M3-S02_persistence-failure-diagnosis.md
```

## Start of formal work

Create or resume one record and include only what is needed:

- date and session or step ID;
- status: `Active`;
- current route and milestone;
- authorized objective;
- starting repository and evidence state;
- expected output and pass condition;
- scope and stop line;
- relevant plans, files, and sources;
- Ali's initial prediction when required.

## During work

Update progressively with material events:

- concepts introduced and depth covered;
- decisions and rationale;
- consequential commands, tool actions, and changed files;
- observed outputs and interpretations;
- failures, hypotheses, diagnoses, and corrections;
- tests, comparisons, and evidence;
- assistance and ownership labels;
- blockers, deferred topics, and remaining uncertainty.

Do not log every conversational turn or copy full artifacts. A short timely record is preferable to a polished reconstruction after context is lost.

## Closure

Close the file as `Completed`, `Partial`, `Blocked`, `Invalid`, or `Superseded`.

Record:

- final result and pass-condition status;
- evidence, commit, or artifact references;
- demonstrated capability and depth;
- AI-generated or otherwise unowned work;
- remaining uncertainty or blocker;
- required canonical tracker update;
- `MEMORY.md` update, when current state changed;
- exact continuation or next action.

## Maintenance and safety

- Record observed events, decisions, and reasoning—not polished fictional summaries.
- Preserve failed, rejected, and superseded approaches when they materially explain the result.
- Reference canonical or large artifacts instead of duplicating them.
- Keep secrets, credentials, private data, medical or financial information, private logs, and unnecessary identifiers out of this public repository.
- Do not use working-memory records to authorize work or override a controlling artifact.