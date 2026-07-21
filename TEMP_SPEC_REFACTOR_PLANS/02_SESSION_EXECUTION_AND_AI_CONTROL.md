# Temporary Work Package 02 — Session Execution and AI Control

**Status:** Blocked until Work Package 01 passes  
**Sequence:** 2 of 7  
**Primary repository:** Canonical `motafegh/Career`  
**Dependency:** Work Package 01  
**Stop boundary:** Finish the execution-mode and control-transfer rules before changing capability evidence schemas.

> This package preserves disciplined learning and evidence collection while making the amount of procedure proportional to the work and explicitly transferring technical control from AI to Ali as capability grows.

## 1. Outcome

After this package:

- small reversible work can use a lightweight continuation;
- normal learning work uses a standard learning loop;
- formal ceremony is reserved for consequential work;
- decision, exploration, execution and tangent handling are distinct;
- AI direction decreases as demonstrated depth increases;
- “one next action” controls execution without blocking legitimate technical comparison or challenge.

## 2. Files in scope

Primary:

- `governance/UPGRADEPILOT_LEARNING_AND_EXECUTION_CONTRACT.md`
- `governance/SESSION_AND_BLOCKER_PROTOCOL.md`

Supporting edits only where necessary:

- `governance/UPGRADEPILOT_LEARNING_PREFERENCES.md`
- `strategy/STRATEGY_AND_SCOPE.md`
- `governance/90_DAY_EXECUTION_CONTRACT.md`
- tracker schema references to assistance level, without implementing the full evidence redesign reserved for Work Package 03

## 3. Proportional execution modes

### 3.1 Lightweight continuation

Use for small, reversible work inside an already understood and authorized responsibility.

Minimum structure:

```text
Current responsibility:
Next observable result:
Prediction or risk when meaningful:
Action:
Proof:
Stop/continue condition:
```

A lightweight continuation does not require a complete session-start or session-end form unless meaningful state must be handed off.

### 3.2 Standard learning session

Use for a new concept, responsibility, or meaningful implementation increment.

Required flow:

```text
brief product orientation
→ prerequisite check
→ minimum-complete explanation
→ Ali prediction/reasoning
→ bounded action
→ inspect real evidence
→ correction or continuation
→ ownership-bearing change/check
→ concise evidence record
```

### 3.3 Formal session

Use when at least one of these applies:

- milestone or major responsibility transition;
- consequential design decision;
- material blocker;
- formal capability assessment;
- work requiring multi-conversation continuity;
- safety-, legal-, privacy-, cost-, credential-, untrusted-code-, or architecture-sensitive execution.

The existing full Session Order and Session End structures may remain for this mode after removing live project-state content.

### Selection rule

Choose the least ceremonial mode that still protects safety, continuity, learning, ownership and evidence quality.

### Escalation rule

Escalate lightweight or standard work when:

- a consequential decision appears;
- an assumption materially fails;
- the task crosses a responsibility boundary;
- assistance or ownership evidence becomes ambiguous;
- durable handoff state becomes necessary;
- risk or irreversibility materially increases.

## 4. Technical operating modes

### 4.1 Decision mode

Use when a consequential choice remains unresolved.

```text
responsibility and constraints
→ simplest credible baseline
→ two to four credible alternatives
→ trade-offs and failure modes
→ discriminating evidence needed
→ Ali challenges/selects
→ decision record when warranted
```

Alternatives must be explained enough for an informed choice. Do not ask Ali to choose among unfamiliar names without the required model.

### 4.2 Bounded exploration mode

Use when a technical question may affect the active responsibility but it is not yet clear whether a decision is required.

Every exploration must define:

- the exact question;
- relationship to the active responsibility;
- expected information gain;
- time and scope ceiling;
- evidence or observation sought;
- stop and return condition.

Exploration must not silently become permanent architecture or a new roadmap.

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

Record it briefly with a reconsideration trigger and return. Do not dismiss technically relevant questions without stating their relationship to the active work.

## 5. AI-assistance fading model

| Demonstrated depth | Default responsibility distribution |
|---|---|
| D0–D1 | AI may propose decomposition and next action; Ali must understand, predict where meaningful and challenge |
| D2 | AI presents bounded alternatives or prompts; Ali selects and explains the next action |
| D3 | Ali proposes decomposition, tests or diagnostics; AI reviews and corrects only as needed |
| D4 | Ali controls the technical sequence and evidence plan; AI acts mainly as reviewer, challenger or targeted assistant |
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

### Anti-regression rule

When evidence shows Ali cannot operate at the expected assistance level:

- reduce or narrow the capability claim;
- restore only the necessary scaffolding;
- record the actual assistance;
- do not preserve an optimistic depth label.

Scaffolding may increase temporarily for a new context without erasing established narrower capability. The record must distinguish new-context support from regression in an already-demonstrated responsibility.

## 6. Required contract changes

### Learning and Execution Contract

- make proportional modes mandatory;
- define decision/exploration/execution distinctions;
- establish assistance fading as part of capability growth;
- preserve prediction, evidence interpretation, direct correction and ownership requirements;
- state that AI must not complete all consequential decomposition by default after the relevant depth supports transfer.

### Session and Blocker Protocol

- remove active project/session state;
- present the three session modes;
- retain blocker and prerequisite workflows as reusable procedures;
- retain full formal templates only for formal mode;
- add escalation/de-escalation rules;
- avoid forcing a full administrative closeout for every small continuation.

### Learning Preferences

Retain only presentation consequences, such as:

- one minimum-complete chunk at a time;
- ask for reasoning when meaningful, not blind guesses;
- do not over-explain repeated safe material;
- respect justified challenges.

Do not duplicate mandatory execution procedures already owned by the contract/protocol.

## 7. Out of scope

Do not in this package:

- change capability depth definitions or tracker evidence fields beyond necessary references;
- change advanced-system requirements;
- alter workload hours or prerequisite time rules;
- modify technical specifications or ADRs;
- update UpgradePilot README, `AGENTS.md`, `MEMORY.md`, or snapshot files.

## 8. Validation scenarios

### Small validation change

A 15–30 minute reversible change can use lightweight mode. Its administrative work must remain materially smaller than its technical work.

### New unfamiliar contract behavior

Use standard mode: teach the minimum model, obtain a prediction, execute, inspect evidence and require one ownership-bearing change.

### Architecture-method challenge

Enter decision or bounded exploration mode. Do not reject the challenge merely because an action was previously selected.

### D3 debugging work

Ali proposes the first discriminating check. AI reviews rather than automatically selecting it.

### Safety-sensitive command

Escalate to formal mode regardless of task size.

## 9. Pass conditions

- [ ] Lightweight, standard and formal modes are defined once and used consistently.
- [ ] Selection and escalation rules are explicit.
- [ ] Decision, bounded exploration, execution and tangent modes are distinct.
- [ ] “One next action” no longer suppresses unresolved consequential comparison.
- [ ] Assistance fading is explicit from D0 through D5.
- [ ] AI control covers fewer central decisions as evidence grows.
- [ ] Existing safety, evidence and ownership protections remain.
- [ ] No live project state was reintroduced into the protocol.

## 10. Recommended commit boundary

Use one focused commit:

`Simplify Career session execution and transfer AI control`

After validation, stop and proceed to Work Package 03.