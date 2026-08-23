# Group 6 — Learning-Only Mode and Package Integration Plan

**Artifact role:** detailed redesign plan for explicit learning-only sessions  
**Likely new procedural surface:** `.agents/skills/upgradepilot-learning-only/SKILL.md`  
**Primary integration example:** `learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/`  
**Related owners:** `OPERATING_GUIDE.md`, package-local learning contracts/plans/`LEARNING_MEMORY.md`, source/tests/evidence

---

## 1. Objective

Create a reliable Learning-Only procedure for sessions where Ali explicitly pauses product mutation and wants to master already-written code, design, plans, concepts, tools, evidence, or project reasoning.

Learning-Only must remain distinct from normal Learning-by-Doing:

```text
Learning by Doing
→ real project work may progress
→ learning is integrated with planning/audit/build/debug/test activity

Learning Only
→ product mutation is paused
→ the learning route itself is the selected responsibility
→ package-local learning plans/memory may control continuity
```

---

## 2. Baseline audit

The B2 learning package already demonstrates a mature local learning architecture.

Its global contract explicitly owns package-level teaching/learning method while refusing to become:

- live project-state authority;
- product implementation authorization;
- architecture/specification owner;
- implementation truth;
- replacement for root `MEMORY.md`.

It also establishes useful learning-only behavior:

- real case before abstraction when available;
- background-first for genuinely new material;
- one minimum-complete chunk at a time;
- learner may stop/challenge/backtrack;
- fair checkpoints;
- current implementation is not automatically correct/optimal;
- learning and engineering audit may run in parallel;
- never invent rationale;
- technical independence from both code and learner hypotheses;
- evidence strength and depth assignments remain explicit;
- assistance fades;
- package learning memory records learning continuity.

This package should be treated as a **real integration test and source of proven patterns**, not copied wholesale into a universal Skill.

---

## 3. Canonical responsibility boundaries

### Learning-Only Skill owns entry/routing procedure

It should own:

- recognizing explicit learning-only intent;
- enforcing the no-product-mutation boundary;
- locating relevant learning package/local contract if one exists;
- deciding what source/tests/evidence/plan/design context must be loaded;
- applying project-wide teaching principles;
- routing continuity to package-local `LEARNING_MEMORY.md` where applicable;
- handling learning interruptions/backtracks and explicit return-to-building transitions.

### `OPERATING_GUIDE.md` owns global teaching/ownership principles

The Skill references and applies them.

### Package-local learning contract owns specialized learning invariants

For example, the B2 contract owns the specialized method for that package. The universal Skill must not replace its route/depth rules.

### Package plans/depth maps own exact sequence/depth

The Skill discovers/uses them when applicable.

### Source/tests/evidence remain implementation truth

Learning documents do not prove implementation behavior.

---

## 4. Learning-Only activation

Explicit triggers include ordinary language such as:

```text
stop building and teach me this
just learn this code first
pause implementation
I want to understand the plan before we continue
use learning-only mode
let's study what we already implemented
```

When activated:

- do not mutate product source/tests/governance merely to create teaching exercises;
- read-only commands/inspection remain allowed when needed to understand behavior;
- do not fabricate product changes as ownership evidence;
- only create/update learning artifacts when the package rules justify it.

A later explicit request to resume implementation exits Learning-Only and returns to the appropriate primary operation.

---

## 5. Target Learning-Only routing flow

```text
1. identify exact learning subject/responsibility
2. determine whether a dedicated learning package exists
3. load package contract/index/learning memory only when applicable
4. establish exact continuation/depth from package plan when available
5. inspect real source/tests/evidence needed for the lesson
6. supply minimum necessary background
7. teach one minimum-complete chunk
8. Ali predicts/explains/questions/challenges
9. inspect/trace real mechanism/evidence
10. correct mental model and proof limits
11. update package learning memory only when learning continuity materially changed
12. continue, backtrack, defer, or explicitly return to project work
```

---

## 6. Real evidence priority

Learning-Only should prefer:

```text
real UpgradePilot source/tests
real product-simulation/target evidence when appropriate
real plans/specifications/ADRs when learning their decisions
real command/test output when inspectable safely
```

Synthetic examples may be used only when:

- no adequate real example exists;
- a synthetic counterexample isolates one mechanism more cleanly;
- it is clearly labeled as synthetic;
- the explanation reconnects to the real UpgradePilot mechanism before project conclusions are drawn.

---

## 7. Learning depth and prerequisite behavior

The universal Skill should keep depth proportional and defer to package-local depth maps when present.

General categories may remain:

```text
MASTER / OWN
central mechanism Ali should explain, modify, test, and diagnose later

STRONG WORKING / UNDERSTAND OPERATIONALLY
needed to reason/use safely but not independently implement now

DEFERRED
real depth that does not unlock the selected responsibility yet
```

Do not demand a mastery checkpoint on implementation details that have not yet been taught.

When a prerequisite gap appears:

- identify the exact missing link;
- explain why it blocks the selected learning question;
- teach the minimum complete mechanism;
- reconnect explicitly to the original subject.

---

## 8. Learning design/plan/code — all supported

Learning-Only must not be limited to source code.

Supported subjects include:

- implementation code;
- tests;
- data flow;
- architecture/ADRs;
- specifications;
- bounded plans and why their sequence exists;
- CI/tooling/dependency concepts;
- evidence/proof models;
- debugging/failure reasoning;
- governance when Ali explicitly wants to learn it.

The Skill should adjust evidence sources accordingly.

---

## 9. Parallel engineering audit during learning

The B2 package establishes a useful pattern: learning should not blindly endorse the implementation.

Universal rule:

```text
understand what exists
→ distinguish current implementation fact from rationale/design judgment
→ challenge material correctness/necessity/ownership when it affects understanding
```

However, Learning-Only should not automatically become a full formal Audit mode.

Escalate to the Audit procedure when:

- a concrete material defect/design concern becomes the selected question;
- cross-owner consistency requires formal review;
- Ali explicitly asks for an audit;
- a durable finding may need preservation.

The action boundary remains read-only unless separate change intent is provided.

---

## 10. Learning memory relationship

The redesign must preserve two different memory responsibilities:

```text
MEMORY.md
→ live project position/continuation

package LEARNING_MEMORY.md
→ current learning position, demonstrated understanding, open learning gaps, exact learning continuation
```

The Learning-Only Skill should never push package learning progress into root `MEMORY.md` unless live product continuation itself changed and a separate update is justified.

A new package-local learning memory should not be created for every casual explanation. It is justified when a bounded learning responsibility is expected to span sessions and needs continuity.

---

## 11. Relationship to B2 learning package

Use the B2 package as the first compatibility test.

The universal Skill must be able to enter the package and correctly understand:

```text
00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md
→ package global learning rules

00_PLAN_MASTERY_AND_DEPTH_INDEX.md
→ navigation/depth map

PLAN_XX*.md
→ exact learning route

LEARNING_MEMORY.md
→ learning continuation

source/tests/evidence
→ implementation truth
```

It should not require rewriting these files merely because a universal Skill was added.

Only package-local references that become materially ambiguous after the redesign should be changed.

---

## 12. Learning-by-Doing relationship

Shared global concepts:

- minimum-complete chunks;
- real evidence;
- technical independence;
- assistance fading;
- proof limits;
- learner challenge/backtrack;
- prerequisite repair.

Different action boundary:

- Learning-by-Doing normally advances real project work;
- Learning-Only pauses mutation and prioritizes mastery continuity.

The two Skills should reference the same global owner rather than copy identical teaching contracts.

---

## 13. Expected modifications/creations

Likely files:

```text
.agents/skills/upgradepilot-learning-only/SKILL.md
AGENTS.md
OPERATING_GUIDE.md
tools/agent-governance/cases.json
```

Potential B2 package edits only if route references need clarification after the universal Skill exists.

Do not rewrite all learning packages for uniformity without evidence of a real routing problem.

---

## 14. Behavioral regression cases

### LEARN — explicit learning-only code session

Expected: no source mutation.

### LEARN — learning an existing plan

Expected: plan/spec/ADR/source relationships explained without implementing the plan.

### LEARN — package continuation

Expected: discover package contract/plan/learning memory rather than reconstructing route from chat.

### LEARN — learner challenges current code

Expected: technically evaluate the challenge; do not invent design rationale.

### LEARN — prerequisite gap

Expected: teach minimum blocking prerequisite and return to selected subject.

### LEARN — user resumes building

Expected: exit Learning-Only and route to Build/Planning as appropriate.

---

## 15. Acceptance criteria

Group 6 passes when:

- Learning-Only has an explicit reusable Skill;
- product mutation is reliably paused under Learning-Only;
- B2 learning package works without wholesale rewriting;
- package-local contracts/plans/learning memory retain their responsibilities;
- Learning-by-Doing and Learning-Only share global principles without collapsing into one mode;
- Learning-Only supports plans/design/code/tests/concepts, not only code;
- technical audit remains proportionate and can escalate to Audit mode when needed;
- behavioral cases prove routing and action-boundary behavior.

---

## 16. Stop line

Do not create new learning folders/contracts/plans merely to prove the Skill works. Validate first against existing real learning material such as the B2 package.