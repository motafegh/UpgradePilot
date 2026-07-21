# Temporary Work Package 03 — Capability, Ownership, and Operating Rules

**Status:** Blocked until Work Package 02 passes  
**Sequence:** 3 of 7  
**Primary repository:** Canonical `motafegh/Career`  
**Dependency:** Work Packages 01–02  
**Stop boundary:** Finish evidence-quality and operating-rule refinements before changing advanced-system targets.

> This package makes capability claims narrower, harder to satisfy performatively, and clearer about assistance, transfer limits, delayed recall and failure diagnosis.

## 1. Outcome

After this package:

- capability evidence is recorded for specific responsibilities rather than broad topic labels;
- ownership is evaluated by dimension;
- D3–D5 require stronger transfer and independence evidence;
- immediate repetition or executing AI-selected work cannot establish strong ownership by itself;
- prerequisite repair uses a review checkpoint rather than a rigid automatic stop;
- command explanation adapts to familiarity and risk;
- governance planning, technical decision records and execution sketches are distinguished;
- workload discipline does not force low-quality advancement merely to fill hours.

## 2. Files in scope

Primary:

- `strategy/UPGRADEPILOT_CAPABILITY_AND_PREREQUISITE_SPECIFICATION.md`
- `tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md`
- `governance/UPGRADEPILOT_LEARNING_AND_EXECUTION_CONTRACT.md`

Supporting edits where the rule is owned:

- `governance/SESSION_AND_BLOCKER_PROTOCOL.md`
- `governance/UPGRADEPILOT_LEARNING_PREFERENCES.md`
- `governance/90_DAY_EXECUTION_CONTRACT.md`

## 3. Atomic capability records

For material capability evidence, use fields equivalent to:

```text
Capability family:
Specific responsibility:
Depth:
Context:
Evidence:
Assistance level:
Ownership dimensions:
Changed-case evidence:
Failure evidence:
Delayed evidence:
Last demonstrated:
Breadth:
Confidence:
Transfer limit:
```

Example:

```text
Capability family: Python testing
Specific responsibility: Diagnose and repair strict Pydantic validation unit tests
Depth: D2 guided
Transfer limit: Does not establish integration-test design or general pytest ownership
```

### Rules

- A broad family name must not be used as the evidence scope when the demonstrated responsibility is narrower.
- Depth, breadth, freshness and confidence must remain distinguishable.
- A record must identify the context and assistance under which the evidence was produced.
- The tracker may summarize evidence, but must not become a full transcript.

## 4. Ownership vector

For central responsibilities, evaluate separately:

- problem understanding;
- design and trade-off selection;
- implementation;
- test design and repair;
- operation and evidence interpretation;
- diagnosis;
- explanation of system-wide effect;
- reduced-prompt reproduction.

The overall capability claim must not exceed the weakest dimension required for that responsibility.

A single artifact-level label such as “AI-assisted” may remain as a summary, but it must not hide materially different ownership across dimensions.

## 5. Evidence expectations by depth

### D0

No demonstrated capability. Exposure or generated artifacts may exist.

### D1

Require accurate recognition or explanation after teaching, with the evidence scope stated narrowly.

### D2

Require:

- guided application to the current case;
- correct interpretation of representative evidence;
- explicit assistance level.

### D3

Where the responsibility supports it, require:

- at least one changed case;
- one meaningful next action, test or diagnostic selected with limited prompting;
- one relevant failure diagnosis;
- one delayed recall or reconstruction check;
- one ownership-bearing modification or test;
- an explicit transfer limit.

### D4

Require:

- repeated evidence across sessions;
- changed-context transfer;
- design or challenge of the responsibility;
- implementation and test ownership;
- diagnosis of an unfamiliar failure;
- explanation of system-wide consequences;
- low-assistance reproduction.

### D5

Require sustained independent performance across materially different contexts, including recognition of limitations and appropriate use of assistance.

## 6. Performative-check prohibition

The following alone must not establish strong ownership or D3+ capability:

- repeating an explanation immediately after the AI;
- typing or applying an AI-provided change;
- approving an AI-selected design;
- successfully running a command;
- passing AI-generated tests;
- producing one guided artifact;
- explaining behavior while the answer remains visible;
- selecting an option after the AI has already eliminated all meaningful reasoning.

These actions may contribute evidence, but stronger claims require transfer, failure, delayed or reduced-assistance evidence appropriate to the depth.

## 7. Tracker design

The tracker remains the canonical state and capability-evidence owner.

It should record only decision-relevant conclusions:

- exact responsibility assessed;
- depth and assistance;
- evidence links;
- ownership dimensions that matter;
- limitations and transfer boundary;
- next required evidence.

Do not copy full session reasoning, command logs, or every ownership-vector field when none changed the conclusion.

Use compact structured entries or tables that remain maintainable.

## 8. Prerequisite-repair checkpoint

Change the 90-minute rule from an automatic ceiling into an initial review checkpoint.

At the checkpoint answer:

1. Can Ali safely and accurately continue the active responsibility?
2. Is the remaining gap required now?
3. Can the active responsibility be narrowed?
4. Should the repair continue inside the same work package?
5. Can remaining depth be distributed across later changed cases?
6. Does the gap materially change route scope, order or feasibility?

Formal replanning is required only for the final condition or another material program consequence. A prerequisite gap does not automatically authorize a general course.

## 9. Adaptive command explanation

### New or consequential command

Explain:

- command or tool name and practical meaning;
- important flags, operators and paths;
- inputs and expected output categories;
- side effects and risks;
- common failure categories;
- what the result proves and does not prove.

### Familiar but materially changed command

Explain only:

- changed arguments or context;
- changed risk or side effect;
- expected behavioral difference.

### Repeated and safe command

Use a concise reminder or no repeated explanation unless Ali requests it or evidence shows misunderstanding.

Increase explanation whenever the action is destructive, credential-sensitive, networked, privacy-sensitive, capability-evidence-bearing or unexpectedly behaves differently.

## 10. Planning categories

### Governance planning

Examples: roadmap redesign, milestone restructuring, program-policy changes.

Requires explicit authority and must remain rare during execution.

### Technical decision record

Examples: ADR, specification amendment, experiment protocol, threat model.

Allowed when a consequential technical decision genuinely needs durable reasoning.

### Execution sketch

A short current-step decomposition with actions, tests, evidence and stop line.

Normal engineering work. Anti-planning controls must not prohibit it or force it into a permanent document.

## 11. Workload and cognitive stop

Preserve capacity commitments and evidence gates, but add this rule:

> Do not begin a new consequential responsibility merely to fill remaining hours when concentration, comprehension or diagnostic quality has materially declined.

Safe remaining capacity may be used for:

- reviewing already-written code;
- replaying established behavior;
- organizing evidence;
- delayed recall;
- bounded cleanup;
- another already-authorized low-risk continuation.

Hours are a capacity target, not proof of capability or justification for poor-quality advancement.

## 12. Out of scope

Do not in this package:

- change the product mission or milestone sequence;
- alter advanced-system exposure targets;
- modify UpgradePilot technical specifications or ADRs;
- rewrite README, `AGENTS.md`, `MEMORY.md`, or snapshots;
- inflate or reduce existing capability conclusions without inspecting evidence.

## 13. Validation scenarios

### Immediate teach-back

May support D1 or D2 depending on the task. It cannot alone establish D3.

### Guided implementation with passing tests

Record the implementation and test assistance separately. Do not infer independent test design or diagnosis.

### Delayed changed case

If Ali reconstructs the mechanism and chooses an appropriate action after a gap, it may support D3 when other required evidence exists.

### Prerequisite repair exceeds 90 minutes

Perform the checkpoint and choose continue, narrow, distribute or escalate. Do not automatically create a new roadmap.

### Green-day work finishes early

Advance only when an authorized next item exists and cognitive quality remains sufficient. Do not pad work or start a consequential responsibility in a degraded state.

## 14. Pass conditions

- [ ] Capability entries identify a specific responsibility and transfer limit.
- [ ] Depth, breadth, freshness and confidence are not collapsed into one label.
- [ ] Ownership dimensions are available for central work.
- [ ] D3–D5 require changed-case, delayed, failure and reduced-assistance evidence where appropriate.
- [ ] Immediate repetition alone cannot establish strong capability.
- [ ] Tracker entries remain concise and evidence-linked.
- [ ] The 90-minute rule is a review checkpoint.
- [ ] Command explanation is adaptive.
- [ ] Planning categories are distinct.
- [ ] A cognitive stop rule prevents low-quality hour filling.

## 15. Recommended commit boundary

Use one or two focused commits:

1. `Strengthen Career capability and ownership evidence`
2. `Refine prerequisite command planning and workload controls`

After validation, stop and proceed to Work Package 04.