# Working Memory

`working-memory/` is UpgradePilot's **detailed, public-safe, dated operational memory** for sessions and bounded responsibilities.

Its main purpose is to preserve enough high-resolution context that Ali or a future AI assistant can recover what was being done, why decisions were made, what happened, what was deferred, and where that session stopped without replaying the whole chat.

It is not a raw transcript, a second specification, or the canonical live-state owner.

## Core preservation model

Working memory should progressively and accurately preserve the **meaningful engineering evolution of the active responsibility**.

Think in terms of the path by which the work changed state and understanding:

```text
starting state / assumptions / questions
→ decisions and reasoning
→ bounded actions / implementation / analysis
→ observations and evidence
→ discoveries, errors, failed approaches, or surprises
→ diagnosis, corrections, fixes, and changed understanding
→ alternatives or ideas considered
→ changed route / deferred work
→ resulting state, proof limits, and handoff
```

The goal is a **complete enough engineering story**, not a complete activity log:

```text
meaningful progression
!=
every message / command / edit / repeated run
```

Do not force each detail to prove in advance that it is architecturally critical, required for tomorrow's handoff, or certain to become a learning topic. A locally small but distinctive observation, failure, implementation detail, API/tool behavior, question, correction, or reasoning clue may be worth one concise sentence when it helps explain how the responsibility actually evolved or would be difficult to reconstruct later.

At the same time, do not turn this into continuous logging. Routine repetition, obvious mechanical edits, repeated safe commands, and large raw outputs should normally be summarized away unless they changed the engineering story.

This progression record can later provide historical/rationale evidence for audits, reviews, and Learning-Artifact authoring. Preserve enough context for those later consumers to reconstruct the real path accurately, but do **not** turn working memory itself into a tutorial or learning artifact.

## Relationship to other owners

- `MEMORY.md` is the **canonical compact current project position** and current continuation.
- `working-memory/` preserves detailed dated session/operation context, progressive reasoning/evidence, local session focus, and the handoff as understood at that session's stopping point.
- `plans/` own bounded position-neutral scope, sequence, proof, and stop conditions. A working record may restate the few plan steps selected for the current session as a convenience/focus aid; that does not create a second plan.
- accepted specifications/ADRs own stable accepted semantics/methods.
- `learning/` owns reusable understanding rather than the chronological work trail.
- source, tests, commands, outputs, and environment evidence establish implemented truth.

A working-memory handoff or `next` section is **time-scoped historical/session context**. It may be used to resume work after checking current `MEMORY.md` and any controlling owner, but it must not override newer live state, plans, specifications, ADRs, or user instructions.

For the compact operating procedure, use `.agents/skills/upgradepilot-working-memory/SKILL.md` when Ali asks to create/update session working memory or when a substantive session intentionally maintains one progressively. Load the procedure once for the active record/session; do not reload it for every append.

## Create, continue, or skip

### Create a new record when

- Ali asks for a new session/day/time working memory;
- a new session needs its own anchor and detailed handoff trail;
- responsibility or investigation changes enough that a separate record improves retrieval;
- the existing record has become too broad/long to remain a clear operational memory;
- a distinct material failure, decision, or evidence thread deserves its own record.

Multiple records on the same day are normal when there are distinct sessions or responsibilities.

### Continue an existing record when

- the same session/responsibility is still active;
- the same investigation or evidence question is continuing;
- another result, error, decision, discovery, correction, or learning-relevant step belongs naturally to that same progression.

### Skip when

No meaningful progression or useful future context would be lost and Ali has not asked for a record. Do not create a file merely for one trivial command, wording correction, or routine reversible edit.

## Naming and identity

Prefer new session records in this form:

```text
YYYY-MM-DD_HHMM_<scope-or-step>_<short-topic>.md
```

Use local 24-hour time when available. If exact time is not useful/available, the date-only form remains valid:

```text
YYYY-MM-DD_<scope-or-step>_<short-topic>.md
```

Choose retrieval-friendly scope/topic words that a future search is likely to find. Do not rename old records merely to match the newer convention.

At the top, keep lightweight identity when useful:

```text
Date/time:
Session status: ACTIVE | PAUSED | CLOSED | CONTINUED | SUPERSEDED
Primary responsibility/mode:
Related plan/owner:
Previous: <relative link, when useful>
Continued by: <relative link, when known>
```

These fields are aids, not a rigid schema; omit what adds no value.

## Lightweight record shape

Use only the sections the session needs. A strong default is:

### 1. Session anchor

Briefly preserve:

- the starting point inherited from `MEMORY.md` / the previous relevant record;
- today's/session's goals;
- the few selected plan steps or focus route for this session;
- temporary session-specific rules/boundaries Ali established.

### 2. Progressive record

Update at **meaningful progression points**, not after every message. Preserve the engineering path with enough fidelity that a future reader can understand how the responsibility reached its current state, including as relevant:

- decisions and rationale;
- implementation or analysis performed and what it established;
- important observations, commands/results, and proof limits;
- discoveries, errors, failed approaches, surprises, diagnosis, and repair;
- questions Ali raised and conclusions or corrected mental models reached;
- ideas and alternatives considered, including changes intentionally deferred for later;
- temporary/session-local rules;
- meaningful learning/ownership observations and useful implementation/API/tool details encountered in the real work;
- changed route, changed assumptions, or changed understanding.

Some apparently small details are worth keeping because they complete the engineering story or become useful retrieval/learning anchors later: exact names, files, error text, concepts, alternatives, a subtle behavior, or the clue needed to rediscover an old discussion.

Summarize rather than dump the chat or large logs. Reference canonical/large artifacts instead of copying them. The test is not “did we record everything?” but “can the meaningful progression be reconstructed accurately without replaying the session?”

### 3. Current session route

Keep a short, practical view of what the session is focusing on now. It may intentionally repeat selected plan steps.

If the route changes, update the current route so it does not mislead. Preserve the old route only when the change/reason is itself useful history.

### 4. Stop / handoff

When pausing or closing, preserve proportionately:

- what was actually completed or established;
- exact stopping point;
- unresolved questions, failures, deferred ideas, or unavailable validation;
- what the evidence proves and does not prove when material;
- the intended next steps **as of this stopping point**;
- links to the important plan/source/test/next working record when useful.

If the canonical live project position changed, update `MEMORY.md` separately and keep the working record as the detailed context behind that compact state.

## Links, continuation, and prior-record state

Use relative links between directly related records when they materially improve handoff/retrieval.

When a new record takes over from an older record:

- link the new record back to the relevant previous record;
- if the previous record still says `ACTIVE` or contains an unqualified handoff that could now mislead, make a **minimal** update such as `CONTINUED` / `SUPERSEDED` plus `Continued by: ...`;
- do not rewrite old reasoning, delete historical next steps, or edit every predecessor merely because a new session began;
- if the prior record is already clearly closed/time-scoped, a backlink update is optional.

This keeps chronology understandable without turning record maintenance into ceremony.

## Reading and retrieval

For normal continuation:

1. read current `MEMORY.md`;
2. read the selected plan/owner needed for the current responsibility;
3. read the latest directly relevant linked working record(s);
4. do not scan the full history speculatively.

When Ali remembers only a clue from an older discussion, search `working-memory/` by likely date, scope, filename, error text, concept, or keyword and follow nearby links as needed.

When a later Learning-Artifact task needs implementation history, rationale evidence, errors/fixes, rejected alternatives, or learning-relevant incidents, retrieve only the directly relevant working records and treat them as historical evidence rather than current authority.

## Authority, promotion, and safety

- Working memory records what was discussed/observed/decided in that dated context; it does not independently authorize new work.
- Temporary session rules remain local unless promoted to the correct durable owner.
- Stable accepted rules, semantics, or reusable decisions that should guide unrelated future sessions belong in their canonical owner; keep the working record as provenance.
- Preserve uncertainty and failed/rejected approaches when they materially explain the path.
- Keep secrets, credentials, private data, medical/financial information, private logs, and unnecessary identifiers out of this public repository.
