# UpgradePilot Operating Guide

**Status:** Controlling project-local operating guide  
**Owner:** Ali Rajabi  
**Responsibility:** Learning, execution, proportionality, blocker handling, assistance fading, evidence interpretation, and handoff inside UpgradePilot

## 1. Boundary

UpgradePilot owns its day-to-day operation.

Use this guide for:

- how Ali and AI reason, learn, decide, implement, test, diagnose, and preserve evidence;
- how much ceremony a task requires;
- how blockers and prerequisites are handled;
- how AI assistance decreases as Ali demonstrates capability;
- how execution stops or hands off.

Career does not control ordinary project steps. Consult or update Career only when Ali
explicitly requests a career review or reconsiders a durable program commitment.

This guide defines operating method, not live project state. `MEMORY.md` alone states the
selected stage, plan, latest verified behavior, blocker, and exact continuation.

## 2. Instruction and truth routing

### 2.1 Instruction precedence

When instructions conflict, use:

1. safety, legal, privacy, credential, financial, health, cost, and platform constraints;
2. Ali's explicit instruction;
3. nearest applicable `AGENTS.md`;
4. stable UpgradePilot controls, including `SECURITY.md` when applicable;
5. the position-neutral plan selected in `MEMORY.md`;
6. applicable technical specification and accepted ADR;
7. other project records;
8. AI suggestions.

A stale plan, memory entry, or historical record cannot override Ali's explicit instruction
unless the instruction would violate a higher constraint.

### 2.2 Stable requirements and decisions

Use:

- the project charter for mission, user, boundary, and claim limits;
- `SECURITY.md` for stable security, privacy, intentional credential-use, untrusted-evidence, and external-action rules;
- the 90-day route for stage sequence and gates;
- technical specifications for framework-independent behavior and invariants;
- ADRs for accepted consequential implementation methods;
- the selected bounded plan for scope, sequence, proof, and stop lines.

### 2.3 Actual implementation truth

Use the evidence owner appropriate to the responsibility:

- product runtime behavior → inspected `src/upgradepilot/`, active `tests/`, reproducible commands/outputs, and environment evidence;
- non-product experiment/evaluation behavior → inspected `experiments/`, `experiments/tests/`, reproducible experiment outputs, and dated evidence;
- developer diagnostic/live-proof behavior → inspected `tools/`, command output, and relevant environment/source evidence.

Do not collapse those proof classes. Passing experiment regression is not product regression; a live proof tool is not a substitute for deterministic product tests; documentation and accepted ADRs do not prove implementation.

Repository-wide artifact placement and dependency direction are controlled by the nearest `AGENTS.md` and ADR-0007.

### 2.4 Live continuation

Use `MEMORY.md` only for:

- selected stage and bounded plan;
- latest relevant repository and validated behavior commits;
- immediate action;
- live blocker, deferral, or stop condition;
- exact handoff.

A selected plan defines how work is bounded and proven but must not report progress.
Working-memory records preserve dated evidence and reasoning but must not become live status.

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
→ update MEMORY.md if live continuation changed
→ continue or stop
```

The unit of work is a real product responsibility, failure, evidence problem, or
consequential decision—not a detached technology topic.

## 4. Universal Ceremony Tax Rule

> **Ceremony is a tax. Pay it only when it unlocks a tangible capability, controls a
> material risk, or satisfies a real external obligation that a simpler mechanism cannot
> adequately address.**

Ceremony includes mandatory process, approval, review, meeting, handoff, checklist, document,
report, evidence record, abstraction, interface, framework, automation, infrastructure,
dashboard, compatibility layer, control, or coordination beyond the direct product or
learning action.

A tangible capability is observable and testable. Examples include:

- legal or regulatory compliance;
- security, privacy, access control, or destructive-action protection;
- auditability, provenance, or traceability required for a real decision;
- reproducibility needed for another person or environment;
- failure detection, recovery, rollback, or diagnosis;
- compatibility support for an actual boundary;
- coordination required by demonstrated scale;
- protection of supported behavior through a justified test or CI gate;
- ownership evidence required for a material capability claim;
- user-visible behavior that cannot be delivered safely without the control.

Before adding or retaining consequential ceremony, identify:

```text
Unlocked capability, controlled risk, or external obligation:
Evidence it is needed:
Simplest adequate mechanism:
Cost imposed:
Observable proof:
Removal or reassessment trigger:
```

For ordinary work, answer this through concise reasoning. Do not create a separate form or
approval merely to apply the rule.

Do not add ceremony when:

- no concrete capability, risk, or obligation can be named;
- the justification is only professionalism, best practice, completeness, possible future scale, or portfolio appearance;
- a cheaper mechanism is adequate;
- the need is hypothetical;
- an existing control already provides the capability;
- the process mainly proves that process was followed;
- cost materially slows delivery, learning, or diagnosis without compensating value.

Necessary ceremony must remain proportional, preferably reversible, and removable when its
reason disappears.

## 5. Session proportionality

Use the least ceremonial mode that protects safety, continuity, learning, ownership, and
evidence.

### 5.1 Lightweight continuation

Use for a small, reversible action inside an understood responsibility.

```text
Responsibility:
Observable result:
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

No separate start/end record is required unless material evidence would otherwise be lost.

### 5.2 Standard learning or implementation session

Use for a new concept, responsibility, or meaningful increment.

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

Name the responsibility, expected observable result, prerequisite depth, bounded action,
proof, limitations, and stop condition. Store live continuation only in `MEMORY.md`.

### 5.3 Formal session

Use only for:

- milestone or major responsibility transitions;
- consequential architecture, data, evaluation, security, or adoption decisions;
- material blockers;
- formal capability assessment;
- destructive, credential-sensitive, paid, externally mutating, privacy-sensitive, or
  untrusted-code work;
- durable handoff where `MEMORY.md` and a dated evidence record are both necessary.

De-escalate once the consequential issue is resolved.

## 6. Technical operating modes

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

Do not ask Ali to choose among unfamiliar names without first providing the mental model
needed to evaluate them.

Before comparing methods:

- name the complete product responsibility that owns the proof slice;
- distinguish the tested category from the method's required operating domain;
- reject methods based on accumulating known phrases, exact grammars, fixture rules, or one
  handcrafted interpreter per category when the responsibility is broader;
- explain how each candidate extends, abstains, and creates a replacement cliff.

Incremental delivery may limit what is implemented now. It must not silently reduce the
design horizon to the next fixture.

### Bounded exploration mode

Use when a question may materially affect the selected responsibility but it is unclear
whether a decision is required. Set a question, information goal, scope ceiling, evidence
sought, and return condition. Exploration must not silently become architecture or a new
route.

### Execution mode

Use after the decision exists.

```text
one selected action
→ execute
→ inspect evidence
→ continue, repair, or reopen the decision only when evidence requires it
```

### Tangent mode

Use when a question does not block or materially affect selected work. Record only the
relationship and a reconsideration trigger, then return.

## 7. Teaching and explanation

For an important new term, include when useful:

- full form and abbreviation;
- practical meaning;
- why the name makes sense;
- owning component or layer;
- inputs, outputs, state, and boundaries;
- relationship to the product flow;
- important failure modes and trade-offs;
- depth required for the selected responsibility and depth deferred.

Simplification may narrow scope but must not falsify mechanism. Analogies must reconnect to
the real system.

Teach one minimum-complete concept or responsibility at a time. Avoid monolithic lectures,
blind guessing, and fragments too small to preserve relationships.

### 7.1 Post-run review

After a meaningful implementation, test, command, or failure is observed, classify only
relevant material:

- **Must master** — central concepts, paths, failure boundaries, source behavior, syntax, or
  tools Ali must explain, modify, test, and diagnose for the selected responsibility;
- **Understand operationally** — material Ali must recognize and safely use without internal
  reproduction;
- **Deferred deliberately** — real depth that does not unlock the selected responsibility;
- **Ali-owned practice** — a meaningful prediction, explanation, modification, test, or
  diagnosis that transfers control of a central boundary.

Do not teach every line equally. A successful run triggers explanation of what was proved,
important source behavior, limitations, and the next ownership-bearing action. A failed run
also triggers failure localization, the revealed model gap, and the smallest justified
repair.

Update durable learning only for reusable understanding. Update `MEMORY.md` only when live
continuation changes.

## 8. Commands and tools

For a new or consequential operation, explain:

- command or tool purpose;
- important flags, paths, reads, writes, and side effects;
- credentials, network, cost, privacy, or destructive risk;
- expected output categories;
- what success would and would not prove.

For familiar changed operations, explain only changed arguments, context, risk, and expected
difference. For repeated safe operations, use a concise reminder unless misunderstanding or
capability evidence requires more.

Repository `tools/` contains developer-operated diagnostics, live proofs, explicit validation runners, and maintenance utilities. A tool may exercise product code and external sources, but tool success does not become product behavior unless the corresponding responsibility exists under `src/upgradepilot/` and is protected by product tests.

For public read-only validation, prefer anonymous access unless the selected proof explicitly requires authentication. Do not silently consume ambient credentials merely because they are available; follow `SECURITY.md` and keep authentication failure distinct from source/evidence/product failure.

Never execute untrusted public repository code merely to inspect it. Never expose secrets or
unnecessary private data.

## 9. Debugging

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

Do not change multiple layers before localizing the likely failure. When a failure was not
predicted, state that and identify the model gap it revealed.

## 10. Prerequisite repair

Classify encountered material as:

- **required core** — the selected responsibility directly depends on it;
- **supporting operational** — needed to work safely but not itself a target capability;
- **deferred core** — important later, but only an operational layer is needed now;
- **optional exploration** — not required for the dependency chain.

When blocked:

1. identify the exact missing link;
2. explain why it blocks selected work;
3. teach and practise the minimum complete mechanism;
4. verify through one meaningful action;
5. return explicitly to the original responsibility.

Ninety focused minutes is a review checkpoint, not an automatic new course or route.

## 11. Assistance fading

For project operation, use demonstrated depth of the specific responsibility:

- **D0–D1:** AI may propose decomposition; Ali understands, predicts, questions, and challenges.
- **D2:** AI presents bounded alternatives; Ali selects and explains the action.
- **D3:** Ali proposes decomposition, tests, and diagnostic checks; AI reviews and corrects.
- **D4:** Ali controls the technical sequence and evidence plan; AI acts mainly as reviewer.
- **D5:** Ali operates independently across changed contexts and uses AI selectively.

Do not infer ownership from immediate repetition, typing AI-provided code, approving an
AI-selected design, running a command, or passing AI-generated tests.

## 12. Evidence and ownership

Separate:

1. observed evidence;
2. execution and source context;
3. interpretation;
4. remaining uncertainty;
5. conclusion or next discriminating action.

Record assistance honestly as applicable:

- AI-generated;
- AI-assisted;
- Ali-directed;
- Ali-verified;
- Ali-owned at a stated narrow scope.

Use extended ownership assessment only for central milestone capabilities, disputed claims,
D3+ assessments, or explicit Career review.

## 13. Completion and stopping

Stop when:

- selected proof and ownership requirements are sufficient;
- the next action would begin an unauthorized responsibility;
- evidence requires a decision or blocker escalation;
- concentration, comprehension, or diagnostic quality materially declines;
- safety, legality, privacy, credentials, or cost make continuation inappropriate.

Do not begin consequential work merely to fill remaining hours.

## 14. Document updates

Update only the owner whose responsibility changed:

- live position, selected plan, latest verified behavior, blocker, or continuation → `MEMORY.md` only;
- stable security/privacy/credential/external-action rule → `SECURITY.md`;
- product runtime behavior → `src/upgradepilot/` and active `tests/` as required;
- experiment/evaluation behavior → `experiments/` and `experiments/tests/` as required;
- developer diagnostic/live-proof behavior → `tools/`;
- dated material execution or public-safe incident evidence → working-memory record;
- stable requirement → applicable specification;
- durable implementation or structural method → ADR;
- route sequence or gate → route plan;
- bounded scope, proof, or stop line → applicable plan;
- Career state → only during explicit Career review.

Do not propagate routine progress into README, `AGENTS.md`, specifications, ADRs, plans,
working records, and learning indexes simultaneously.
