---
name: upgradepilot-learning-by-doing
description: Apply UpgradePilot's Learning-by-Doing overlay during substantive real project work by composing teaching, reasoning, bounded action, evidence review, and ownership transfer with the selected primary operation. Use when Ali explicitly asks to learn while doing/building/designing/auditing/debugging, or when progressing non-trivial project work materially benefits from the full learning/action cycle. Do not use merely for standalone Learning-Only mastery sessions where product mutation is paused and learning itself is the primary responsibility.
---

# UpgradePilot Learning by Doing

Use this Skill to **operationalize** the project-wide Learning-by-Doing method during real UpgradePilot work.

This Skill is procedural and non-controlling. `OPERATING_GUIDE.md` remains the canonical owner of the project-wide Learning-by-Doing philosophy and rules. Root `AGENTS.md`, the selected responsibility owners, and current user authorization remain authoritative.

This Skill does not authorize implementation, planning artifacts, external actions, or product mutation by itself.

## Activation

Activate this Skill when either condition holds:

1. Ali explicitly requests Learning-by-Doing, asks to learn while doing/building/designing/auditing/debugging, or asks to use Learning-by-Doing mode with a real primary operation; or
2. substantive UpgradePilot project work that is progressing or materially clarifying a primary operation would benefit from the full reasoning → action → evidence → ownership-transfer cycle.

Do **not** activate this Skill merely because a standalone Learning-Only session is substantive. When mastery/understanding is the selected responsibility and product mutation is paused, use the admitted Learning-Only procedure; it already applies the shared teaching principles from `OPERATING_GUIDE.md` without requiring this overlay.

Do **not** force-load the full procedure for a tiny repetitive edit, one familiar safe command, or a narrow factual lookup when the compact rules already present in `OPERATING_GUIDE.md` are sufficient.

Learning-by-Doing is normally an **overlay**, not the primary authorization mode.

```text
primary operation
Audit | Planning/Design | Build/Implement | Debug/Diagnose | Review | other bounded work

+
Learning-by-Doing procedure
```

The primary operation still controls action boundaries and detailed execution procedure.

## Procedure

### 1. Identify the real responsibility and primary operation

State or infer the smallest real responsibility/question/failure being worked on and the primary operation that owns the action.

Do not replace the real task with a detached tutorial topic.

If live continuation is material, use `MEMORY.md`. Otherwise do not load live state reflexively.

### 2. Establish only the learner context needed now

Use the current conversation and applicable learning continuity before asking Ali to repeat prior understanding.

Load package-local learning contract/plan/depth map/`LEARNING_MEMORY.md` only when that package is actually active or the task depends on its learning state.

Determine only what is necessary to answer:

```text
what must Ali understand before this action is meaningful?
what can safely remain operational or deferred?
what mechanism is genuinely new versus already repeated?
```

Do not create a broad prerequisite inventory unless the primary responsibility requires it.

### 3. Give a minimum-complete orientation

Before using an unfamiliar concept/tool/file/mechanism as a premise, establish enough accurate context to connect it to the real UpgradePilot responsibility.

Prefer this compact shape when useful:

```text
what it is
→ what job it does here
→ where it sits in the real flow
→ why it matters to the current decision/action
→ depth needed now versus deferred
```

Use real source/tests/plans/target evidence when available. Synthetic examples are secondary and should be labeled when used.

When an example's status could materially change the learner's model, distinguish the relevant class rather than presenting every example as normal operation:

```text
normal / expected path
failure / invalid input
purpose-built test fixture
hypothetical design case
synthetic teaching example
```

A defensive failure state or intentionally inconsistent fixture must not be taught as though it is the normal admitted product flow.

Do not explain every line, import, command, or technology equally.

If a meaningful mastery/ownership depth is being assigned, briefly state the project-local reason for that depth. Do not create deeper learning obligations merely because a file or technology is large or interesting.

### 4. Create a meaningful reasoning point

When prerequisites are available and the step is material, give Ali a real opportunity to predict, choose, explain, challenge, or diagnose before or around the action.

Examples:

- predict what a transformation should preserve;
- choose between understood design alternatives;
- explain why a test discriminates one hypothesis;
- challenge whether a field/check belongs at the current layer;
- identify what evidence would strengthen or weaken a claim.

A reasoning point is not a quiz gate. Do not stall useful project work merely to manufacture learner participation, and do not ask for implementation detail that has not yet been taught or established as a premise.

If Ali challenges the premise, stop advancing that local proposition and evaluate the claim, current implementation, and prior assistant claims by the same evidence standard. Do not agree merely for conversational satisfaction and do not defend current code merely because it exists.

### 5. Perform the real bounded action

Proceed according to the **primary operation's** authorization and procedure.

Learning-by-Doing must not turn implementation into a lecture, turn review into implementation, or turn planning into unauthorized building.

Use the smallest real action that can produce useful evidence:

```text
one design decision
one bounded implementation increment
one discriminating diagnostic
one source/test trace
one relevant command/test
one evidence interpretation step
```

### 6. Inspect actual evidence and correct the model

After a meaningful action, inspect the strongest available evidence appropriate to the claim.

Keep distinct:

```text
observation
→ source/execution context
→ interpretation
→ remaining uncertainty
→ supported conclusion / next discriminating action
```

Explicitly state what the result proves and what stronger claim it does **not** prove when that boundary is material.

If the result contradicts the prediction or prior model, identify the exact model gap rather than hiding the mismatch.

For a material source-ownership block, connect the executable responsibility to a meaningful focused test when one exists and make clear what that test protects and does not prove. If no meaningful focused test exists, state that instead of implying test understanding was demonstrated.

### 7. Transfer ownership proportionately

Use the assistance-fading model in `OPERATING_GUIDE.md` for the specific responsibility.

As a mechanism repeats, shift progressively toward Ali:

```text
AI decomposition/explanation
→ Ali prediction/selection
→ Ali proposes checks or decomposition
→ Ali controls technical sequence/evidence plan
```

Do not claim ownership/mastery from typing AI-provided code, approving an AI-selected design, running commands, immediate repetition, or passing AI-generated tests.

When an already-taught mechanism naturally reappears in later real project work, and the required premises are still available, prefer a brief fair retrieval/reconstruction before replaying the earlier explanation when that helps judge retained understanding. Use the result to reduce or restore support under the Operating Guide's assistance-fading rule. Do not manufacture a project task or quiz every recurrence for this purpose.

For a tiny familiar step, one concise explanation may be enough. For a central new mechanism, require more meaningful reasoning, modification, testing, diagnosis, or explanation over time.

### 8. Backtrack and repair prerequisites locally

Ali may interrupt, question, or backtrack at any point.

When a prerequisite gap appears:

```text
identify exact missing link
→ explain why it blocks the current responsibility
→ teach/practise the minimum complete mechanism
→ verify once meaningfully
→ return explicitly to the original task
```

Do not silently let prerequisite repair become a new course or project route.

## Composition with primary operations

### Audit / Review

Learning-by-Doing adds explanation, learner reasoning, and critical understanding; the Audit procedure remains read-only unless separate change intent exists.

Understanding current behavior does not imply endorsing its correctness, necessity, ownership, or architecture.

Invoke the full Audit Skill only when the task is materially evaluative or Ali asks for audit/review—not merely because Learning-by-Doing encourages critical thinking.

### Planning / Design

Explain the responsibility and unfamiliar alternatives before asking Ali to choose among them. Make trade-offs, evidence needs, proof/stop lines, and artifact choice understandable.

The Planning/Design operation still decides whether no durable plan, one compact plan, or a larger plan family is justified.

### Build / Implement

Orient the important source/data flow, explain high-value mechanisms, use real tests/failures as evidence, and progressively transfer modification/testing/diagnosis responsibility.

The Build operation still owns source/test preflight, mutation scope, source-clarity application, and validation sequence.

### Debug / Diagnose

Use hypothesis → discriminating check → evidence → model correction. Avoid random multi-layer edits. A surprising failure should produce an explicit model correction.

## Parallel engineering judgment

Normal Learning-by-Doing includes technical independence:

- current source/tests establish implementation truth, not automatic design correctness;
- Ali's hypothesis, an earlier assistant's claim, comments, and current design all remain challengeable;
- when material, ask whether a mechanism is correct, necessary, proportionate, and owned by the right layer;
- use `OPERATING_GUIDE.md` §4.3 when the question is **why a mechanism is needed**: proposition/design goal → necessity class → owner/layer → evidence → alternative/trade-off;
- never invent a rationale that the inspected evidence does not establish;
- use the canonical `JUST-*` / end-to-end ownership rules when retention or cross-layer responsibility is actually at issue.

Do not turn every routine step into a formal architecture or repository audit.

## Learning-Only boundary

If Ali says to stop building and **just learn**, switch to Learning-Only behavior:

```text
product mutation paused
→ existing real code/design/plan/evidence becomes learning material
→ package-local learning contract/plan/memory used when applicable
```

Do not continue Build/Implement merely because Learning-by-Doing was active earlier.

Use `.agents/skills/upgradepilot-learning-only/SKILL.md` as the admitted Learning-Only procedure, together with root `AGENTS.md`, `OPERATING_GUIDE.md`, and applicable package-local learning owners.

## Continuity and records

Do not create a learning artifact merely because learning occurred.

Route durable information by responsibility:

- reusable understanding → `learning/` or the active package's learning owner when justified;
- package learning position/depth/gaps → `LEARNING_MEMORY.md` when that package uses one;
- dated material execution/validation reasoning → `working-memory/` when it has handoff value;
- live project continuation → `MEMORY.md` only.

Preserve only information that will materially improve future continuation, understanding, or ownership evidence.

## Anti-patterns

Do not:

- replace real project work with generic lectures;
- ask Ali to choose among unexplained names/technologies;
- use fictional examples when adequate real project evidence already answers the question;
- present a failure-only/test-fixture/hypothetical state as normal product operation;
- manufacture failures, mutations, or exercises solely to create ownership evidence;
- require a prediction before every trivial step or before its premises are known;
- explain every line equally;
- infer correctness from existence or tests from necessity;
- answer “why do we need this?” with only “because the current code uses it”;
- invent an original/design rationale that cannot be established;
- let learning concerns authorize work outside the primary operation's scope;
- copy package-local learning contracts into this Skill;
- layer Learning-by-Doing onto a standalone Learning-Only session merely because learning is substantive;
- turn Learning-by-Doing into Learning-Only unless Ali explicitly pauses building or the active learning contract requires that boundary.

## Completion check

Before ending a substantive Learning-by-Doing cycle, confirm proportionately:

```text
real responsibility advanced or clarified
+ important new mechanism understood at the required and justified depth
+ actual evidence inspected
+ proof limit stated when material
+ source/test relationship understood when source ownership was a material target and a meaningful test exists
+ Ali had a meaningful ownership-bearing reasoning/action opportunity when useful
+ next continuation routed to the correct owner
```

Do not add ceremony merely to complete this check.