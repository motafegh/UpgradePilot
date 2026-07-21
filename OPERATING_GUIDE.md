# UpgradePilot Operating Guide

**Status:** Controlling project-local operating guide  
**Owner:** Ali Rajabi  
**Responsibility:** Learning, execution, session proportionality, blocker handling, assistance fading, evidence interpretation, and handoff inside UpgradePilot

## 1. Boundary

UpgradePilot owns its own day-to-day operation.

Use this guide for:

- how Ali and AI reason, learn, decide, implement, test, diagnose, and preserve evidence;
- how much ceremony a task requires;
- how blockers and prerequisites are handled;
- how AI assistance decreases as Ali demonstrates capability;
- how current work is handed off.

Career does **not** control ordinary project steps. Career is updated only when Ali explicitly requests a career review or when a major career/program decision is being reconsidered.

## 2. Instruction and truth routing

### 2.1 Instruction precedence

When instructions conflict, use:

1. safety, legal, privacy, credential, financial, health, cost, and platform constraints;
2. Ali's explicit current instruction;
3. stable UpgradePilot project controls;
4. the current authorized project plan;
5. applicable technical specification and accepted ADR;
6. other project records;
7. AI suggestions.

A stale plan, memory entry, or historical record cannot override Ali's current instruction unless the instruction would violate a higher safety or platform constraint.

### 2.2 Required behavior

Use:

- the project charter and 90-day plan for product and milestone requirements;
- technical specifications for framework-independent behavior and invariants;
- ADRs for accepted consequential implementation methods.

### 2.3 Actual implementation truth

Use:

- inspected source;
- reproducible commands and outputs;
- relevant tests;
- current environment evidence.

Documentation and accepted ADRs do not prove implementation.

### 2.4 Current project continuation

Use:

- `MEMORY.md` for concise current responsibility and continuation;
- the current project plan for bounded scope, proof, and stop conditions;
- `working-memory/` for detailed session evidence and reasoning.

## 3. Core working loop

```text
real product responsibility
→ identify the smallest blocking concept or decision
→ build the minimum accurate mental model
→ Ali predicts, reasons, questions, or challenges
→ perform one bounded action
→ inspect actual evidence
→ separate observation, interpretation, and uncertainty
→ diagnose or revise
→ Ali modifies, tests, selects, or explains
→ preserve only material evidence and assistance
→ continue or stop
```

The learning unit is a real product responsibility, failure, evidence problem, or consequential decision—not a detached technology topic.

### 3.1 Universal Ceremony Tax Rule

> **Ceremony is a tax. Pay it only when it unlocks a tangible capability, controls a material risk, or satisfies a real external obligation that a simpler mechanism cannot adequately address. If it does not, it is excessive.**

Ceremony includes any mandatory process, approval, review, meeting, handoff, checklist, document, report, evidence record, abstraction, interface, framework, automation, infrastructure layer, dashboard, compatibility layer, control, or coordination step that adds work beyond the direct product or learning action.

A tangible capability is observable and testable. Examples include:

- legal or regulatory compliance;
- security, privacy, access control, or destructive-action protection;
- auditability, provenance, or traceability required for a real decision;
- reproducibility needed for another person or environment;
- failure detection, recovery, rollback, or operational diagnosis;
- compatibility or migration support for an actual boundary, such as a real multi-cloud migration;
- coordination required by demonstrated team, service, or workload scale;
- protection of supported behavior through a justified test or CI gate;
- learner ownership evidence required for a material capability claim;
- user-visible product behavior that cannot be delivered safely or reliably without the control.

Before adding or retaining ceremony, identify:

```text
Unlocked capability, controlled risk, or external obligation:
Evidence that it is needed now:
Simplest adequate mechanism:
Cost imposed:
Observable proof that it works:
Reassessment or removal trigger:
```

For ordinary work, this may be answered in one concise sentence or through the immediate reasoning. **Do not create a separate form, document, meeting, or approval merely to apply this rule.** Record the justification durably only when the ceremony is itself consequential, cross-cutting, costly, externally required, or likely to persist.

The default is **do not add the ceremony** when:

- no concrete capability, material risk, or external obligation can be named;
- the justification is only “professionalism,” “best practice,” “completeness,” possible future scale, or portfolio appearance;
- a cheaper mechanism provides adequate protection;
- the need is hypothetical rather than evidenced now;
- an existing control already provides the same capability;
- the process mainly proves that a process was followed;
- the cost materially slows delivery, learning, diagnosis, or ownership without compensating value;
- the original need has disappeared but the ceremony remains.

Necessary ceremony must remain proportional. Use the smallest control that buys the required capability. Prefer reversible and temporary controls when the need may change. Name reassessment or removal triggers for costly or persistent controls, and simplify or remove them when they no longer pay for themselves.

Apply this rule across the whole journey, including:

- planning and governance;
- sessions, reviews, approvals, and handoffs;
- documentation, evidence, and reporting;
- testing and quality gates;
- abstractions, interfaces, and package structure;
- dependencies, frameworks, and tools;
- automation, dashboards, and observability;
- infrastructure, services, queues, cloud, migration, and operational controls;
- capability assessment and portfolio evidence.

This rule does not weaken required safety, legal, privacy, security, evidence, or external compliance controls. It requires those controls to have a concrete purpose, proportional implementation, observable proof, and a defined reason to persist.

## 4. Session proportionality

Use the least ceremonial mode that protects safety, continuity, learning, ownership, and evidence.

### 4.1 Lightweight continuation

Use for a small, reversible action inside an understood responsibility.

Minimum structure:

```text
Current responsibility:
Next observable result:
Action:
Proof:
Stop or continue condition:
```

Examples:

- change one test case;
- inspect one validation error;
- rerun a known safe command;
- make one bounded implementation correction;
- confirm one invariant already understood.

No separate start/end record is required unless material state must be handed off.

### 4.2 Standard learning session

Use for a new concept, responsibility, or meaningful implementation increment.

```text
brief orientation
→ prerequisite check
→ minimum-complete explanation
→ Ali reasoning or prediction
→ bounded action
→ inspect evidence
→ correct the model
→ ownership-bearing change or check
→ concise evidence update
```

Name:

- current responsibility;
- expected observable result;
- required prerequisite depth;
- bounded action;
- proof and limitations;
- stop or continuation condition.

### 4.3 Formal session

Use only for:

- milestone or major responsibility transitions;
- consequential architecture, data, evaluation, security, or adoption decisions;
- material blockers;
- formal capability assessment;
- destructive, credential-sensitive, paid, externally mutating, privacy-sensitive, or untrusted-code work;
- durable handoff spanning conversations where concise memory is insufficient.

Formal sessions may record expanded risks, allowed files, proof, ownership actions, assistance, and continuation. De-escalate once the consequential issue is resolved.

## 5. Technical operating modes

### Decision mode

Use when a consequential choice remains unresolved.

```text
responsibility and constraints
→ simplest credible baseline
→ credible alternatives
→ trade-offs and failure modes
→ discriminating evidence
→ Ali challenges, selects, or approves
→ ADR only when the decision is durable and cross-cutting
```

Do not ask Ali to choose among unfamiliar names without first providing the mental model needed to evaluate them.

### Bounded exploration mode

Use when a question may materially affect the active responsibility but it is not yet clear whether a decision is required.

Set a question, information goal, scope/time ceiling, evidence sought, and return condition. Exploration must not silently become architecture or a new roadmap.

### Execution mode

Use after the decision exists.

```text
one selected action
→ execute
→ inspect evidence
→ continue, repair, or reopen the decision only when evidence requires it
```

### Tangent mode

Use when a question does not block or materially affect active work. Record only the relationship and a reconsideration trigger, then return.

## 6. Teaching and explanation

For an important new term, include when useful:

- full form and abbreviation;
- practical meaning;
- why the name makes sense;
- owning component or layer;
- inputs, outputs, state, and boundaries;
- relationship to the current product flow;
- important failure modes and trade-offs;
- depth required now and depth intentionally deferred.

Simplification may narrow scope but must not falsify the mechanism. Analogies must reconnect to the real system.

Teach one minimum-complete concept or responsibility at a time. Avoid monolithic lectures, blind guessing, and fragments so small that relationships disappear.

## 7. Commands and tools

### New or consequential operation

Explain:

- command/tool name and purpose;
- important flags, paths, reads, writes, and side effects;
- credentials, network, cost, privacy, or destructive risk;
- expected output categories;
- what success would and would not prove.

### Familiar but changed operation

Explain only the changed arguments, context, risk, and expected difference.

### Repeated safe operation

Use a concise reminder or no repeated explanation unless requested, misunderstood, or needed for capability evidence.

Never execute untrusted public repository code merely to inspect it. Never expose secrets or unnecessary private data.

## 8. Debugging

Use:

```text
symptom
→ affected boundary
→ strongest supported hypothesis
→ discriminating check
→ root cause
→ smallest repair
→ failing case
→ relevant unchanged case
→ nearest integration proof
```

Do not change multiple layers before localizing the likely failure. When a failure was not predicted, state that clearly and identify the model gap it revealed.

## 9. Prerequisite repair

Classify encountered material as:

- **required core** — active responsibility directly depends on it;
- **supporting operational** — needed to perform work safely but not itself a target capability;
- **deferred core** — important later, but only the accurate operational layer is needed now;
- **optional exploration** — not required for the dependency chain.

When blocked:

1. identify the exact missing link;
2. explain why it blocks current work;
3. teach and practice only the minimum complete mechanism;
4. verify through one meaningful action;
5. return explicitly to the original responsibility.

Ninety focused minutes is a review checkpoint, not an automatic new course or roadmap. Continue, narrow, distribute later depth, or replan only when the gap materially changes scope or sequence.

## 10. Assistance fading

Capability depth is defined by the Career capability model when a formal career assessment is requested. For project operation, use the demonstrated depth of the specific responsibility:

- **D0–D1:** AI may propose decomposition; Ali understands, predicts where meaningful, questions, and challenges.
- **D2:** AI presents bounded alternatives or prompts; Ali selects and explains the next action.
- **D3:** Ali proposes decomposition, tests, and diagnostic checks; AI reviews and corrects.
- **D4:** Ali controls the technical sequence and evidence plan; AI acts mainly as reviewer or targeted assistant.
- **D5:** Ali operates independently across changed contexts and uses AI selectively.

Do not infer ownership from immediate repetition, typing AI-provided code, approving an AI-selected design, running a command, or passing AI-generated tests.

## 11. Evidence and ownership

Separate:

1. observed evidence;
2. execution/source context;
3. interpretation;
4. remaining uncertainty;
5. conclusion or next discriminating action.

Record assistance honestly as applicable:

- AI-generated;
- AI-assisted;
- Ali-directed;
- Ali-verified;
- Ali-owned at a stated narrow scope.

For ordinary project evidence, record only what is necessary. Use an extended ownership assessment only for central milestone capabilities, disputed claims, D3+ assessments, or explicit Career review.

## 12. Completion and stopping

Stop when:

- the active proof and ownership requirement are sufficient;
- the next action would begin an unauthorized responsibility;
- evidence requires a decision or blocker escalation;
- concentration, comprehension, or diagnostic quality has materially declined;
- safety, legality, privacy, credentials, or cost make continuation inappropriate.

Do not begin new consequential work merely to fill remaining hours. Safe remaining capacity may be used for reviewing code, reproducing evidence, improving one test, concise documentation derived from behavior, or stopping.

## 13. Document updates

A normal technical event updates only the artifacts whose responsibilities changed.

- Source/test change: source, tests, and material working evidence.
- Continuation change: `MEMORY.md`.
- Requirement change: applicable specification.
- Durable implementation-method change: ADR.
- Project-plan boundary or gate change: current project plan.
- Career state or capability update: only when Ali explicitly requests a Career review.

Do not propagate routine project progress into Career, README, `AGENTS.md`, specifications, ADRs, and plans simultaneously.