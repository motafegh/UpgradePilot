# Session and Blocker Protocol

**Status:** Approved reusable operating protocol  
**Responsibility:** Session format, escalation, blockers, prerequisite repair, and continuation handoff  
**Live state:** The canonical tracker and current authorized session/work-package artifact control what is active. This protocol does not select a milestone, method, deliverable, or exact next action.

## 1. Governing principle

Use the least ceremonial mode that still protects:

- safety and legality;
- continuity;
- accurate learning;
- learner ownership;
- evidence quality;
- consequential decisions;
- costly or irreversible actions.

A small reversible action must not carry the same administrative burden as a milestone transition, architecture decision, formal assessment, or sensitive operation.

## 2. Session modes

### 2.1 Lightweight continuation

Use for a small, reversible action inside an already authorized and sufficiently understood responsibility.

Minimum structure:

```text
Current responsibility:
Next observable result:
Prediction or risk when meaningful:
Action:
Proof:
Stop/continue condition:
```

A lightweight continuation does not require a full start or end form unless material state must be handed off.

Typical examples:

- change one test case;
- inspect one validation error;
- rerun a known safe command;
- make one bounded implementation correction;
- confirm one invariant already understood.

### 2.2 Standard learning session

Use for a new concept, responsibility, or meaningful implementation increment.

Required flow:

```text
brief product orientation
→ prerequisite check
→ minimum-complete explanation
→ Ali prediction or reasoning
→ bounded action
→ inspect actual evidence
→ correct the model or continue
→ ownership-bearing change/check
→ concise evidence record
```

A standard session must name:

- the current product responsibility;
- the observable result sought;
- required prerequisite depth;
- the bounded action;
- proof and limitations;
- the stop or continuation condition.

### 2.3 Formal session

Use when at least one condition applies:

- milestone or major responsibility transition;
- consequential architecture, data, evaluation, security, or adoption decision;
- material blocker;
- formal capability assessment;
- work spanning conversations or requiring durable handoff;
- destructive, credential-sensitive, paid, externally mutating, privacy-sensitive, untrusted-code, or architecture-sensitive operation.

Formal start:

```text
SESSION START
Program date or review point:
Capacity mode:
Current controlled responsibility:
Current state and evidence:
First expected proof:
Material risks or constraints:
```

Formal order:

```text
SESSION ORDER
Deliverable:
Required output or behavior:
Why it is next:
Maximum investigation/work budget:
Required prerequisite depth:
Ali-owned action:
AI assistance permitted:
Files/components/sources allowed:
Execution sequence:
Proof commands/tests/evidence:
Expected evidence categories:
Stop line:
Pass condition:
Authorized continuation:
```

Formal close:

```text
SESSION END
Focused work:
Deliverables completed:
Evidence/commit:
Commands/tool actions/tests and results:
What Ali can explain, choose, modify, test, or diagnose:
Corrections received:
AI assistance used:
Capability evidence and transfer limit:
Unresolved blocker:
Next controlled responsibility:
```

## 3. Mode selection and escalation

Choose the least ceremonial adequate mode.

Escalate when:

- a consequential decision appears;
- an assumption materially fails;
- the task crosses a responsibility boundary;
- assistance or ownership evidence becomes ambiguous;
- durable handoff becomes necessary;
- risk, cost, privacy impact, external mutation, or irreversibility materially increases.

De-escalate after the consequential issue is resolved and the remaining work becomes small, reversible, and understood.

Do not continue formal ceremony merely because the session began formally.

## 4. Technical operating modes

Session mode describes how much process is required. Operating mode describes what kind of reasoning is occurring.

### 4.1 Decision mode

Use when a consequential choice remains unresolved.

```text
responsibility and constraints
→ simplest credible baseline
→ two to four credible alternatives
→ trade-offs and failure modes
→ discriminating evidence needed
→ Ali challenges, selects, or approves at the supported assistance level
→ ADR or decision record when warranted
```

Do not ask Ali to choose among unfamiliar names without the mental model needed to evaluate them.

### 4.2 Bounded exploration mode

Use when a technical question may materially affect the active responsibility but it is not yet clear whether a decision is required.

Record:

```text
Question:
Relationship to active responsibility:
Expected information gain:
Time/scope ceiling:
Evidence sought:
Stop and return condition:
```

Exploration must not silently become permanent architecture, a new roadmap, or an unrelated research campaign.

### 4.3 Execution mode

Use after a decision exists.

```text
one selected action
→ execute
→ inspect actual evidence
→ continue, repair, or reopen the decision only when evidence requires it
```

The one-next-action rule applies strongly here.

### 4.4 Tangent or diversion mode

Use when a question neither blocks nor materially affects the active responsibility.

Record briefly:

```text
Deferred question or idea:
Relationship to current work:
Reconsideration trigger:
```

Then return. Do not silently dismiss a relevant question, and do not expand it without a trigger.

## 5. Assistance fading during sessions

Use the capability depth demonstrated for the specific responsibility, not a broad topic label.

| Demonstrated depth | Default session responsibility |
|---|---|
| D0–D1 | AI may propose decomposition and next action; Ali understands, predicts where meaningful, and challenges |
| D2 | AI presents bounded alternatives or prompts; Ali selects and explains the next action |
| D3 | Ali proposes decomposition, tests, and diagnostic checks; AI reviews and corrects as needed |
| D4 | Ali controls technical sequence and evidence plan; AI acts mainly as reviewer or targeted assistant |
| D5 | Ali operates independently across changed cases and uses AI selectively |

Apply this transfer to:

- next-action selection;
- implementation decomposition;
- test design;
- diagnostic hypotheses;
- evidence selection;
- architecture comparison;
- stopping decisions;
- explanation and reproduction.

If evidence does not support the expected assistance level, narrow the claim or restore only the necessary scaffolding. Record the actual assistance.

## 6. Technical blocker protocol

### Step 1 — Observe

Before changing code, configuration, evidence interpretation, or decision logic, record:

```text
Expected:
Actual:
Error, symptom, or evidence conflict:
Last known working point:
Evidence inspected:
Strongest current hypothesis:
```

Inspect directly where safe and practical.

### Step 2 — Bound

Identify the likely affected layer, for example:

- external evidence/source;
- environment, network, process, file, or permission;
- acquisition or parsing;
- normalization or validation;
- persistence;
- analysis or recommendation;
- model/evaluation;
- test, packaging, or CI.

Do not change several layers simultaneously before a discriminating check.

### Step 3 — Diagnose

At D0–D2, AI may help identify the smallest discriminating action.

At D3 or higher for the responsibility, Ali proposes the first discriminating action and the AI reviews it.

The diagnostic cycle is:

```text
challenge hypothesis
→ request decisive evidence
→ run smallest safe check
→ interpret output categories
→ revise hypothesis
```

### Step 4 — Repair or correct the decision

Repair the smallest supported cause, or correct the smallest unsupported interpretation.

### Step 5 — Validate

Re-run or re-check:

- the failing or disputed case;
- a relevant success or unchanged case;
- the nearest integration or decision path when applicable.

Record what the repair proves and what remains unverified.

## 7. Missing-prerequisite protocol

A missing prerequisite does not authorize a detached course or new roadmap.

The initial repair budget is a **90-focused-minute review checkpoint**, not an automatic stop.

Before repair, state:

- exact missing concept;
- why it blocks the responsibility;
- required depth now;
- deeper material deferred;
- bounded teaching/practice action;
- one verification task;
- exact return point.

At the checkpoint determine:

1. Can Ali safely continue the active responsibility?
2. Is the remaining gap required now?
3. Can the responsibility be narrowed?
4. Should repair continue inside the same package?
5. Should remaining depth be developed through later changed cases?
6. Does the gap materially change route scope or sequence?

Formal replanning is required only for the final condition or another material program impact.

## 8. External evidence blocker

When public evidence is missing, inaccessible, stale, conflicting, invalid, or expired:

1. preserve the evidence state;
2. do not fabricate certainty;
3. try only lawful and proportionate alternatives;
4. narrow the claim, request a targeted check, defer, reject, or abstain;
5. record the effect on the report or evaluation.

An explicit limitation or abstention may be the correct result.

## 9. Environment blocker

When an environment blocker remains unresolved:

1. preserve state and evidence;
2. state whether the environment is required for the active gate;
3. choose the smallest safe workaround when one exists;
4. defer only the environment-specific part when safe;
5. register an explicit follow-up gate;
6. continue another authorized responsibility only when dependency order permits;
7. do not restart the project.

## 10. Command explanation level

### New or consequential

Explain name, purpose, key flags/operators, inputs/outputs, side effects, risks, failure categories, and what the result would and would not prove.

### Familiar but changed

Explain changed arguments, context, risk, and expected difference.

### Repeated and safe

Use a concise reminder or no repeated explanation unless requested, misunderstood, or used as capability evidence.

Always increase explanation for destructive, credential-sensitive, networked, paid, externally mutating, privacy-sensitive, or untrusted-code actions.

## 11. Session evidence and state

A session record may contain:

- what happened;
- actual outputs;
- Ali's reasoning or challenge;
- assistance used;
- local unresolved questions;
- evidence links.

The canonical tracker is updated only when a gate, blocker, material decision, capability claim, or controlled responsibility changes. It must not become a transcript.

A session record never becomes the authority for current program state merely because it is newer.

## 12. Completion judgments

Use:

- **Pass** — deliverable and required evidence completed;
- **Partial** — continue the same responsibility;
- **Blocked** — use the blocker protocol;
- **Invalid evidence** — rerun or repair;
- **Out of scope** — stop, revert, park, or discard;
- **Underloaded** — materially smaller than planned; record for calibration and continue only when quality and capacity support it.

Administrative completion is not capability completion. Successful execution is not ownership unless the required reasoning, modification, testing, diagnosis, transfer, and assistance conditions are met.

## 13. Maintenance

Change this protocol only when reusable session or blocker behavior changes. Do not add live milestone, method, exact-next-action, or session-specific implementation content.