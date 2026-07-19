# Session and Blocker Protocol

## Current activation status

This protocol does not independently select work. It governs sessions authorized by active UpgradePilot plans.

- [`../UpgradePilot.md`](../UpgradePilot.md) is the governing project charter.
- [`../strategy/UPGRADEPILOT_CAPABILITY_AND_PREREQUISITE_SPECIFICATION.md`](../strategy/UPGRADEPILOT_CAPABILITY_AND_PREREQUISITE_SPECIFICATION.md) is the approved capability-control artifact.
- [`../governance/UPGRADEPILOT_LEARNING_AND_EXECUTION_CONTRACT.md`](../governance/UPGRADEPILOT_LEARNING_AND_EXECUTION_CONTRACT.md) is the approved operating contract.
- [`../plans/UPGRADEPILOT_90_DAY_MASTER_ROADMAP.md`](../plans/UPGRADEPILOT_90_DAY_MASTER_ROADMAP.md) is the approved master route.
- [`../plans/UPGRADEPILOT_STAGED_MILESTONE_PLAN.md`](../plans/UPGRADEPILOT_STAGED_MILESTONE_PLAN.md) is the approved milestone plan.
- [`../tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md`](../tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md) is the active tracker.
- [`../plans/UPGRADEPILOT_FIRST_SESSION_PLAN.md`](../plans/UPGRADEPILOT_FIRST_SESSION_PLAN.md) is the active session plan.
- R0 planning closure has passed.
- Technical execution is authorized for the bounded UP-S01 G1 session.
- Technical implementation has not started; UP-S01 is manual evidence work.
- The existing AegisLab current-week and daily routes are deferred and non-controlling.
- The exact next action is to start UP-S01.

## 1. Session-start message

Ali starts an authorized session with:

```text
START DAY <program day>
Actual date: YYYY-MM-DD
Mode: Green | Yellow | Red
Sleep/function: <public-safe summary>
Available focused minutes: <number>
Current deliverable: <artifact/behavior name>
Current state: <one sentence>
First expected proof: <file/test/command/output>
```

For UP-S01, use the exact start block in `../plans/UPGRADEPILOT_FIRST_SESSION_PLAN.md`.

Do not ask “What should I do?” The first incomplete deliverable in the current approved artifact is controlling. Deferred AegisLab files are never controlling.

## 2. Required AI Session Order

After the start message, the AI returns one order:

```text
SESSION ORDER

Deliverable:
Exact output path or behavior:
Why it is next:
Maximum time budget:
Required prerequisite depth:
Ali-owned action:
AI assistance allowed:
Files/components/sources allowed:

Execution sequence:
1.
2.
3.

Proof commands/tests/evidence:
Expected evidence:
Stop line:
Pass condition:
Next authorized deliverable if completed early:
```

Rules:

- one selected route;
- exact output before commands or tool actions;
- no unrelated alternatives;
- no future-phase expansion;
- no unexplained command dump;
- consequential commands are explained before execution;
- Ali predicts representative behavior;
- actual output is interpreted before continuation;
- identify what evidence proves and does not prove;
- time budgets are maxima, not targets to fill;
- continue only to the named next authorized deliverable;
- do not assign full sessions to administrative work that should take minutes;
- do not repeat demonstrated work merely to consume scheduled time;
- use the active tracker as the state record;
- do not create another planning artifact during active execution.

## 3. Session-end message

Ali closes every authorized focused session with:

```text
SESSION END
Focused minutes:
Deliverables completed:
Evidence/commit:
Commands/tool actions/tests and results:
What Ali can explain or modify:
Corrections received:
AI assistance used:
Capability evidence:
Unresolved blocker:
Exact next deliverable:
```

The AI judges:

- **Pass** — deliverable completed with sufficient evidence;
- **Partial** — continue the same deliverable;
- **Blocked** — invoke the blocker protocol;
- **Invalid evidence** — rerun or repair;
- **Out of scope** — stop, revert, park, or discard;
- **Underloaded** — materially smaller than planned; advance and record for calibration.

The active tracker must be updated from the actual session evidence.

## 4. Technical blocker protocol

### Step 1 — Observe

Before changing code, configuration, evidence interpretation, or recommendation logic, record:

```text
Expected:
Actual:
Error/symptom or evidence conflict:
Last known working point:
Evidence inspected:
Strongest current hypothesis:
```

Spend up to 15 minutes inspecting evidence personally where safe and practical.

### Step 2 — Bound

Identify the likely affected layer:

- external evidence/source;
- environment;
- network;
- process/service;
- file/permission;
- acquisition;
- parser;
- validation;
- persistence;
- analysis/recommendation;
- model/evaluation;
- test;
- packaging/CI.

Do not change multiple layers simultaneously.

### Step 3 — Guided diagnosis

AI help is initially capped at 45 minutes.

The AI should:

1. challenge the current hypothesis;
2. request only decisive evidence;
3. select the smallest safe diagnostic action;
4. explain expected output categories;
5. revise the hypothesis from actual output.

### Step 4 — Repair or decision correction

Repair the smallest supported cause, or correct the smallest unsupported evidence interpretation.

### Step 5 — Validate

Re-run or re-check:

- the failing or disputed case;
- a relevant success or unchanged case;
- the nearest integration or decision path when applicable.

Record what the repair proves and what remains unverified.

## 5. Missing prerequisite protocol

Initial repair cap: **90 focused minutes**, unless the active plan sets a smaller cap.

The AI must state:

- exact missing concept;
- why it blocks the current deliverable;
- required depth now;
- deferred depth;
- bounded teaching action;
- one verification task;
- exact return point.

After verification, return immediately to the blocked deliverable.

A prerequisite gap does not authorize a general course or new roadmap. A materially larger gap triggers formal sequence or scope review.

## 6. External evidence blocker

When public evidence is missing, inaccessible, stale, conflicting, invalid, or expired:

1. preserve the evidence state;
2. do not fabricate certainty;
3. try only lawful and proportionate alternatives;
4. narrow the claim, request a targeted check, defer, or abstain;
5. record the effect on the report or evaluation.

For UP-S01, inability to obtain one evidence source may lead to an explicit limitation or abstention rather than a new research campaign.

## 7. Environment blocker protocol

When an environment blocker becomes relevant in a later implementation stage and remains unresolved within one session:

1. preserve state and evidence;
2. state whether the environment is required for the current gate;
3. choose the smallest workaround when one exists;
4. defer only the environment-specific part when safe;
5. register an explicit follow-up gate;
6. continue another authorized deliverable when dependency order permits;
7. do not restart the project.

UP-S01 does not authorize repository-code execution or environment setup.

## 8. Planning-diversion protocol

When broad planning begins outside the authorized artifact, respond:

```text
This decision is already controlled by the 90-day system.
Current deliverable: <deliverable>
Next action: <action>
```

The current controlling deliverable is the **UP-S01 manual evidence report for `pydantic/pydantic#13432`**.

New roadmap, milestone, tracker, first-session, architecture, corpus, code, or advanced-system planning is out of scope until the active evidence creates a named need.

A brief clarification is allowed only when current files conflict, are materially underloaded, or lack a necessary decision.

## 9. New idea protocol

Record:

```text
Deferred idea:
Possible trigger:
```

Maximum discussion: five minutes.

No design, research campaign, repository, task list, or implementation is created outside the authorized artifact.
