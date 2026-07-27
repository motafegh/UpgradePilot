# Working Memory

This directory contains detailed, public-safe, dated records for material UpgradePilot
audits, investigations, implementation responsibilities, and debugging work.

Working memory preserves evidence and reasoning. It is not a second tracker, live status
owner, or reason to turn every interaction into ceremony.

## Relationship to other files

- `AGENTS.md` contains stable repository-wide AI operating instructions.
- `MEMORY.md` is the sole live project position and exact continuation.
- `working-memory/` records dated observations, decisions, commands, outputs, and closed or
  partial results.
- `learning/` records reusable understanding and frozen educational snapshots.
- `plans/` defines position-neutral scope, sequence, proof, and stop conditions.
- source, tests, commands, outputs, and environment establish implemented truth.

A working record may say what happened on a stated date or during a named operation. It must
not claim to be the present project stage, selected plan, latest commit, blocker, handoff, or
next action.

## Decide: create, reuse, or skip

### Create one record when

- a material responsibility or investigation needs an evidence trail;
- work spans several coordinated actions or competing hypotheses;
- a consequential product, architecture, dependency, security, or evidence decision must be
  preserved;
- losing the reasoning trail would materially damage diagnosis, reproducibility, or auditability;
- a significant result, failure, or rejected method needs a dated record.

### Append to an existing dated record when

- continuing the same named investigation or evidence question;
- adding another result to the same bounded responsibility;
- diagnosing a focused failure inside the same operation;
- preserving a correction to the same historical account.

Do not create one record per concept, command, error, chat, or small edit.

### Skip working memory when

- answering a small explanation or clarification;
- discussing an idea without a material decision;
- explaining one line of code or one command without consequential execution;
- making a small reversible edit;
- correcting wording or formatting;
- no material evidence or reasoning would be lost.

## Reading discipline

Use this order:

1. read `MEMORY.md`;
2. read the position-neutral plan selected there;
3. read a dated working record only when `MEMORY.md`, provenance, or the precise question
   points to it;
4. do not scan every historical record speculatively.

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

## Record structure

Include only what the evidence needs:

- date and operation or responsibility identifier;
- objective or question investigated;
- repository revision or input identity relevant to the observation;
- commands or tool actions that materially affected the result;
- observed outputs;
- interpretation and uncertainty separated from observation;
- decisions and rationale;
- failures, competing hypotheses, diagnosis, and repair;
- checks performed and checks unavailable;
- final result classification such as completed, partial, blocked, invalid, or superseded;
- stable artifact, commit, or source references.

A result classification is local to the dated record. It must not be presented as the live
project position.

## Closure

At closure, record:

- whether the stated objective or pass condition was met;
- the evidence that supports that conclusion;
- remaining uncertainty specific to that operation;
- which stable owner, if any, changed because of the result.

When live project position changes, update `MEMORY.md`; do not copy its continuation back
into the working record.

## Maintenance and safety

- Record observed events, decisions, and reasoning—not polished fictional summaries.
- Preserve failed, rejected, and superseded approaches when they materially explain the result.
- Reference canonical or large artifacts instead of duplicating them.
- Keep secrets, credentials, private data, medical or financial information, private logs,
  and unnecessary identifiers out of this public repository.
- Do not use working-memory records to authorize work or override a controlling artifact.