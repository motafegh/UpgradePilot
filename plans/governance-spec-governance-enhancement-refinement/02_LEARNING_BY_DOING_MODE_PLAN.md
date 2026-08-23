# Group 2 — Learning-by-Doing Mode Plan

**Artifact role:** detailed redesign plan for UpgradePilot's default Learning-by-Doing operating philosophy  
**Primary owner to preserve:** `OPERATING_GUIDE.md`  
**Likely new procedural surface:** `.agents/skills/upgradepilot-learning-by-doing/SKILL.md`  
**Scope:** how substantive UpgradePilot work remains educational and ownership-building while still performing real project work

---

## 1. Objective

Make Learning-by-Doing explicit as the default UpgradePilot working philosophy without turning it into a giant always-on procedure.

The target is:

```text
PRIMARY OPERATION
Audit | Planning/Design | Build/Implement | Debug/Diagnose | Review | other bounded work

+ DEFAULT WORKING PHILOSOPHY
Learning by Doing
```

Learning-by-Doing is therefore not merely another mutually exclusive operation mode. It normally composes with the primary operation.

---

## 2. Why this group needs its own plan

The project goal is not only to produce working code/documents. Normal work should also progressively transfer understanding and technical ownership.

However, the present `OPERATING_GUIDE.md` mixes:

- universal Learning-by-Doing principles;
- detailed implementation procedure;
- detailed audit reasoning;
- source-clarity review;
- decision/planning behavior;
- debugging;
- learning-depth rules.

The redesign must keep the universal learning/ownership core highly visible while progressively disclosing detailed operation procedure through Skills.

---

## 3. Canonical responsibility

### `OPERATING_GUIDE.md` remains canonical for project-wide Learning-by-Doing principles

It should continue to own the rules that are expected during most substantive UpgradePilot sessions, including:

- real responsibility rather than detached tutorial topic;
- smallest blocking mental model;
- one minimum-complete chunk at a time;
- learner reasoning/prediction/challenge before or around action when useful;
- inspect actual evidence after action;
- distinguish observation, interpretation, uncertainty, and proof;
- explain what a result proves and does not prove;
- prerequisite repair only to the depth needed for the selected responsibility;
- assistance fading;
- no false ownership claims from AI-generated work or passing tests;
- proportionate teaching rather than line-by-line narration;
- handoff/continuity through repository owners rather than chat memory.

### Learning-by-Doing Skill owns reusable procedure/activation

The Skill should operationalize the above for an AI assistant and provide an explicit manual trigger when Ali wants the mode reinforced.

It must not become a separate semantic owner of the global learning philosophy.

---

## 4. Target Learning-by-Doing loop

Keep a compact high-salience loop in `OPERATING_GUIDE.md`:

```text
real project responsibility
→ identify minimum blocking concept/decision
→ build accurate mental model
→ Ali predicts/reasons/questions/challenges where useful
→ perform one bounded real action
→ inspect actual evidence
→ explain result + proof limit
→ Ali increasingly modifies/tests/diagnoses/explains
→ preserve only material continuity
→ continue or stop
```

The Skill may expand this with operation-sensitive instructions.

---

## 5. Composition with other operation Skills

### Audit + Learning by Doing

The audit procedure remains read-only unless separate change intent exists.

Learning contribution:

- explain the actual implementation/design responsibility being audited;
- teach only concepts needed to evaluate it;
- invite Ali to challenge necessity/ownership/evidence;
- preserve the distinction between understanding current implementation and endorsing its design.

### Planning/Design + Learning by Doing

Learning contribution:

- explain the responsibility before asking Ali to select among unfamiliar approaches;
- compare credible alternatives and tradeoffs;
- explain why a plan, ADR, specification, or simpler local action is appropriate;
- let Ali increasingly reason about sequence, evidence, and stop lines.

### Build/Implement + Learning by Doing

Learning contribution:

- orient source/data flow before or during material changes;
- explain high-value implementation mechanisms;
- use real tests/failures as teaching evidence;
- progressively transfer modification/testing/diagnosis responsibility.

### Debugging + Learning by Doing

Learning contribution:

- state hypothesis and discriminating check;
- explain why evidence changes confidence;
- identify the mental-model gap when a failure was not predicted;
- avoid random multi-layer edits.

### Learning Only

Learning-Only is a distinct action boundary, not just an intensified Learning-by-Doing session. Product mutation is paused and package-local learning contracts/memory may become the primary scoped procedure.

---

## 6. What should stay in `OPERATING_GUIDE.md`

Keep these as everyday/global rules:

### A. Learning objective and technical independence

The AI assistant should help Ali understand and own the work, but must not optimize for agreement. Claims from Ali, previous assistants, source comments, and current implementation are all subject to evidence.

### B. Minimum-complete teaching

Do not jump through several unfamiliar mechanisms in one explanation. Do not fragment so far that relationships disappear.

### C. Real evidence first

Use real UpgradePilot source/tests/plans/target evidence when available. Synthetic examples are secondary tools, not substitutes for existing project evidence.

### D. Background-first for genuinely new material

Give enough real-world meaning that a new term/tool/file is not used as an unexplained premise, but do not turn every prerequisite into a course.

### E. Evidence/proof distinction

Always preserve what a run/test/source fragment establishes and what stronger claim remains unsupported.

### F. Assistance fading

Retain D0–D5 or an equivalent compact progression because this is central to learner ownership.

### G. Ownership evidence

Typing AI-provided code, approving an AI design, or running generated tests is not independent mastery.

### H. Stopping and concentration

Stop or narrow when learning/diagnostic quality materially declines or the next action would begin an unauthorized responsibility.

---

## 7. What should move or become Skill-specific

Candidate details to remove from always-on guide and place in Skills:

- exact multi-step repository audit output format;
- exact plan-writing sequence and plan-size classification;
- exact Build preflight/source/test validation sequence;
- long Source Clarity completion checklist;
- package-specific Learning-Only route discovery;
- operation-specific handoff/checklists that are not relevant to most sessions.

Do not move universal concepts merely for file-size reduction.

---

## 8. Learning-by-Doing Skill design

Suggested Skill responsibility:

> Apply UpgradePilot's global Learning-by-Doing method during substantive project work, composing it with the selected primary operation while keeping explanations proportional and transferring ownership through real evidence and actions.

Suggested sections:

1. activation and non-controlling boundary;
2. identify primary operation and selected responsibility;
3. establish learner context only as needed;
4. minimum-complete orientation;
5. prediction/reasoning/challenge points;
6. real action/evidence cycle;
7. post-action explanation and proof limits;
8. assistance fading;
9. interruption/backtrack behavior;
10. relation to Learning-Only;
11. handoff/learning-memory routing.

### Manual trigger

Ali may explicitly request Learning-by-Doing reinforcement. The Skill should then be loaded even if the primary operation Skill is also active.

### Automatic trigger

For substantive UpgradePilot work, root routing should normally activate the philosophy without requiring Ali to say the words every session.

---

## 9. Relationship to package-local learning contracts

Global Learning-by-Doing rules must not overwrite specialized learning contracts.

Expected relationship:

```text
OPERATING_GUIDE.md
→ global Learning-by-Doing principles

Learning-by-Doing Skill
→ general operation composition

package-local learning contract
→ specialized learning invariants for that package

package plan/depth map
→ exact route and required depth

LEARNING_MEMORY.md
→ package learning continuity
```

When a package-local contract is active, the Skill should inherit and route rather than reproduce it.

---

## 10. Parallel audit behavior

Learning-by-Doing may include critical evaluation of what is being learned/built, but it should not automatically turn every session into a formal repository audit.

Rule:

```text
understand current mechanism
+ challenge material correctness/necessity/ownership when evidence warrants
+ invoke full Audit procedure only when the task becomes materially evaluative or Ali asks for it
```

This preserves technical independence without making routine learning excessively ceremonial.

---

## 11. Expected modifications

Likely files:

```text
OPERATING_GUIDE.md
AGENTS.md
.agents/skills/upgradepilot-learning-by-doing/SKILL.md
possibly tools/agent-governance/cases.json
```

Do not modify package-local learning contracts globally merely to mention the new Skill unless their routing actually becomes ambiguous.

The B2 package should be used as a validation case before any package-local edits are considered.

---

## 12. Validation scenarios

### Scenario A — design discussion

Ali asks to design the next implementation responsibility.

Expected:

- Planning/Design is primary operation;
- Learning-by-Doing also applies;
- unfamiliar alternatives are explained before selection;
- no Learning-Only package is created.

### Scenario B — ordinary coding

Ali explicitly asks to implement a bounded source change.

Expected:

- Build is primary operation;
- explanation focuses on material mechanisms/data flow;
- action proceeds rather than turning into a lecture;
- Ali gets meaningful reasoning/testing participation.

### Scenario C — user challenges a premise

Ali says the current design seems unnecessary.

Expected:

- stop advancing locally;
- evaluate the claim and implementation by evidence;
- do not agree merely to satisfy Ali;
- resume only after the local premise is resolved enough.

### Scenario D — tiny repetitive edit

Expected:

- Learning-by-Doing remains proportional;
- no unnecessary full concept lesson;
- only changed/new reasoning is explained.

### Scenario E — explicit “just learn this”

Expected:

- switch to Learning-Only procedure;
- product mutation paused;
- package/local learning continuity used when applicable.

---

## 13. Acceptance criteria

Group 2 passes when:

- `OPERATING_GUIDE.md` still clearly expresses the project's default Learning-by-Doing identity;
- a manual/automatic Learning-by-Doing Skill exists without becoming a second authority;
- the Skill composes cleanly with Audit, Planning, and Build;
- Learning-Only remains a distinct action boundary;
- explanations are proportional, real-evidence-based, and ownership-oriented;
- global teaching rules are not copied wholesale into every operation Skill;
- behavioral cases cover at least one composition scenario and one explicit Learning-Only switch.

---

## 14. Stop line

Do not use this group to design the complete Audit, Planning, Build, or Learning-Only procedure. Define only the composition contract they will inherit, validate it, then continue with the dedicated group plans.