# Group 4 — Planning / Design Mode Plan

**Artifact role:** detailed redesign plan for proportional planning and design procedure  
**Likely new procedural surface:** `.agents/skills/upgradepilot-planning-design/SKILL.md`  
**Related owners:** `plans/README.md`, root `AGENTS.md`, `OPERATING_GUIDE.md`, `PROJECT_CHARTER.md`, accepted specifications/ADRs, `MEMORY.md` only when live selection matters

---

## 1. Objective

Create one reusable Planning/Design procedure that scales from a tiny bounded change to a multi-stage implementation responsibility without forcing unnecessary plan artifacts or duplicating specification/ADR semantics.

The Skill should answer:

```text
Does this work need a durable plan at all?
If yes, how much planning depth is justified?
Which decisions are already owned elsewhere?
What remains unresolved?
What is the bounded execution route, proof, stop line, and prohibited scope?
```

---

## 2. Baseline audit

`plans/README.md` already has strong core rules:

- a plan owns one bounded responsibility/investigation;
- plans own sequence, prerequisites/evidence, modification boundary, proof, pass/stop conditions, prohibited scope;
- plans do not own stable mission, live state, framework-independent product invariants, durable architecture already owned by ADR, or implementation truth;
- plans should reference rather than re-specify accepted specifications/ADRs;
- plan creation must be justified and proportional;
- stale paths should be reconciled against active source/accepted architecture rather than recreated blindly.

Weaknesses to address operationally:

1. these rules are conventions, but there is no reusable Skill that reliably applies them when Ali asks for planning/design;
2. planning/design method remains mixed into `OPERATING_GUIDE.md` decision/exploration material;
3. assistants can over-plan small work or under-plan cross-responsibility work;
4. design discussion can silently become implementation authorization;
5. plans can become mini-specifications or mini-ADRs when the assistant restates stable semantics/method decisions;
6. planning under Learning-by-Doing needs an explicit teaching/decision procedure.

---

## 3. Canonical responsibility boundary

### Planning/Design Skill owns procedure

It should own:

- classify planning need and scale;
- inspect relevant owners before inventing design;
- identify unresolved decisions;
- compare alternatives when needed;
- determine whether a specification/ADR update is required before execution;
- write/update the smallest adequate plan when authorized/requested;
- define proof/pass/stop/prohibited scope;
- preserve design discussion vs implementation boundary.

### `plans/README.md` remains canonical for plan artifact responsibility

The Skill operationalizes it, not replaces it.

### Specifications own stable behavior

If planning reveals that accepted behavior itself must change, update/supersede the specification through the proper bounded work. Do not encode the new invariant only in a plan.

### ADRs own consequential method

If a durable cross-cutting implementation method is selected, use an ADR when justified. Do not create an ADR merely because a plan contains a design choice.

---

## 4. Planning-depth model

One Skill should scale. Do not create micro/medium/big planning Skills.

### Level P0 — no durable plan

Use for:

- tiny reversible edits;
- one bounded diagnostic check;
- simple clarification/explanation;
- work already unambiguously covered by an existing selected plan.

Use a concise internal/response-level action sequence only.

### Level P1 — compact bounded plan

Use for:

- several coordinated steps/files/tests;
- one responsibility likely to span a session or conversation;
- work needing explicit proof/pass/stop conditions.

Keep it compact.

### Level P2 — consequential plan

Use for:

- cross-module responsibility;
- behavior/architecture pressure;
- multiple proof layers;
- material dependencies or migration;
- work where wrong sequencing can cause rework or drift.

Include owner map, unresolved decisions, evidence/proof strategy, and explicit stop lines.

### Level P3 — staged plan family

Use only when one plan would become ambiguous because several bounded responsibilities have distinct gates/owners/proof obligations.

Do not create a plan family merely because the work is large in word count.

---

## 5. Target Planning/Design flow

```text
1. establish exact desired outcome/responsibility
2. inspect applicable Charter/spec/ADR/plan/source evidence
3. separate already-decided semantics from unresolved design
4. determine whether a durable plan is justified
5. establish simplest credible baseline
6. compare credible alternatives only when a real decision remains
7. identify ownership implications
8. define bounded sequence
9. define proof/pass/stop/prohibited scope
10. write/update plan only at the justified depth
11. stop before implementation unless implementation is also explicitly authorized
```

---

## 6. Design reasoning rules

### 6.1 Do not design from names alone

Before selecting frameworks/abstractions/patterns, define the complete responsibility and evidence/proof need.

### 6.2 Simplest credible baseline first

Apply Ceremony Tax before adding persistent machinery.

### 6.3 Existing implementation is evidence, not design authority

When planning refactors or extensions, apply `JUST-*` to existing mechanisms. Migration impact matters, but current use does not automatically establish architectural necessity.

### 6.4 Trace responsibility before adding cross-layer fields/checks

If the plan proposes a material cross-layer mechanism, identify producer → integration → consumer ownership before committing to the design.

### 6.5 Preserve design horizon without fixture hardcoding

Use the Minimum Useful Generality specification when automated behavior could be overfit to known examples.

### 6.6 Separate behavior decision from method decision

```text
what the system must guarantee
→ specification responsibility

how a consequential mechanism will achieve it
→ ADR responsibility

how bounded work will implement/prove it
→ plan responsibility
```

---

## 7. Learning-by-Doing composition

Planning/design is one of the most important learning surfaces.

The Skill should:

- provide the mental model before asking Ali to choose unfamiliar technologies/architectures;
- explain why a decision is necessary now;
- identify alternatives and tradeoffs proportionately;
- ask Ali to reason about sequence/proof/ownership when prerequisites are available;
- challenge unsupported user or assistant assumptions;
- avoid fake choice when only one option actually satisfies admitted constraints.

Do not require Ali to manually author every plan section for ownership evidence.

---

## 8. Plan-writing behavior

When a plan artifact is justified/requested, include only applicable sections:

- responsibility and outcome;
- scope/exclusions;
- applicable owner references;
- entry evidence/prerequisites;
- unresolved decisions that genuinely block execution;
- modification boundary;
- execution sequence;
- validation/proof;
- pass condition;
- stop line;
- prohibited scope;
- reassessment trigger only when material.

Do not add ceremonial headings that carry no decision value.

### Reference, do not re-specify

If a specification/ADR already owns a rule, the plan should record its execution consequence and link it.

### Position-neutrality

The plan must not become live-state owner. `MEMORY.md` selects the active continuation separately.

---

## 9. Explicit design-only boundary

Prompts such as:

```text
plan this
design this
think through the architecture
write the implementation plan
```

are read/design operations unless the user also authorizes implementation.

The Skill must not infer mutation merely because the plan is detailed enough to execute.

This is important for governance redesign work like this branch, where planning intentionally precedes modification.

---

## 10. Expected modifications/creations

Likely files:

```text
.agents/skills/upgradepilot-planning-design/SKILL.md
AGENTS.md
OPERATING_GUIDE.md
plans/README.md
tools/agent-governance/cases.json
```

Potential plan-index cleanup occurs under Group 1/7 and should not be duplicated here.

---

## 11. Behavioral regression cases

### PLAN — tiny localized edit

Expected: no unnecessary durable plan.

### PLAN — multi-file bounded responsibility

Expected: compact plan with proof/stop line.

### PLAN — consequential architecture choice

Expected: inspect spec/ADR ownership, compare alternatives, create/update ADR only if durable consequential method warrants it.

### PLAN — existing implementation pressure

Expected: current code/callers/tests treated as evidence/migration pressure, not automatic design authority.

### PLAN — user asks for plan only

Expected: no implementation mutation.

### PLAN + Learning-by-Doing

Expected: explain unfamiliar design alternatives before asking Ali to select.

### PLAN — plan/spec conflict

Expected: surface/fix conflict rather than treating plan as implicit supersession.

---

## 12. Acceptance criteria

Group 4 passes when:

- one Planning/Design Skill scales proportionately across plan sizes;
- small work does not generate unnecessary artifacts;
- design-only requests remain non-mutating;
- specification/ADR/plan/source responsibilities remain distinct;
- plan artifacts reference rather than copy accepted semantics;
- Learning-by-Doing composition is explicit;
- `JUST-*`, Ceremony Tax, and generality pressure are applied when relevant;
- behavioral governance cases cover over-planning, under-planning, plan-only boundary, and owner conflicts.

---

## 13. Stop line

Do not use Planning/Design to pre-authorize implementation. Once a plan/design is complete enough for execution and no planning question remains, stop unless Build/Implement work is also explicitly requested.