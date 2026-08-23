# Governance Redesign — Group 4 Planning / Design Validation

**Date:** 2026-08-23  
**Branch:** `governance/spec-governance-enhancement-refinement`  
**Role:** dated non-controlling implementation/validation evidence for Group 4 of the governance operating-model redesign

## 1. Scope executed

Group 4 implemented the bounded responsibility defined by:

`plans/governance-spec-governance-enhancement-refinement/04_PLANNING_DESIGN_MODE_PLAN.md`

with the existing-rule traceability gate:

`plans/governance-spec-governance-enhancement-refinement/00_RULE_OWNERSHIP_PROMOTION_AND_REINFORCEMENT_MATRIX.md`

as a mandatory design input.

No product source/tests, accepted product specification semantics, ADR semantics, live project position, B2 learning-package files, or unrelated governance groups were modified.

## 2. Exact Group-4 changes

Using Group-3 completion commit `069bdc35a5d5f8b54cb433e1cde90887244bda0b` as the bounded baseline, Group 4 changed only:

```text
.agents/skills/upgradepilot-planning-design/SKILL.md
tools/agent-governance/planning_cases.json
tools/agent-governance/README.md
```

No `AGENTS.md`, `OPERATING_GUIDE.md`, `plans/README.md`, specification, or ADR rewrite was required.

## 3. Why the permanent owners were not rewritten

The current permanent controls already contain the required routing/semantic boundaries:

- root `AGENTS.md` classifies `plan / design` as read-only reasoning by default, permits only bounded plan-artifact mutation when explicitly requested, and routes Planning/Design to the admitted procedure when present;
- root manual routing already recognizes `use planning/design mode`;
- `OPERATING_GUIDE.md` §5.4 routes Planning/Design through `plans/README.md` plus the admitted Planning/Design Skill when available;
- `plans/README.md` already correctly owns plan responsibility, position neutrality, reference-not-re-specify behavior, plan-creation justification, plan-family admission, and the minimum plan standard;
- `docs/architecture/README.md` already correctly owns ADR responsibility/proportionality and the specification → ADR → plan → implementation separation.

After `.agents/skills/upgradepilot-planning-design/SKILL.md` was created, those existing generic routing statements became fully satisfied. Adding more permanent prose or duplicate path strings was not required to establish a new semantic boundary and would have increased always-on context without correcting a real routing defect.

## 4. Planning/Design Skill result

The admitted Skill is procedural and non-controlling. It establishes one reusable flow that scales rather than separate small/medium/large planning Skills.

### Action boundary

Planning/design remains:

```text
inspect owners/evidence
→ reason/compare
→ optionally create/update the smallest justified planning artifact
→ STOP before implementation
```

A detailed plan does not authorize Build/Implement.

### Planning depth

The Skill operationalizes:

```text
P0 — no durable plan
P1 — compact bounded plan
P2 — consequential plan
P3 — staged plan family only when distinct responsibilities/gates/proof obligations justify it
```

Planning size is driven by responsibility ambiguity, owner/gate/proof structure, and continuation value—not raw word count or file count.

### Owner-first design

The Skill separates:

```text
stable required behavior
→ specification / Charter owner

accepted consequential durable method
→ ADR owner

current implementation fact
→ source/tests evidence, not automatic design authority

bounded execution/investigation coordination
→ plan owner

live selected continuation
→ MEMORY.md only
```

### Engineering-necessity discipline

The Skill consumes the traceability matrix's globally proven rules:

- `RT-ENG-001` — implementation fact vs rationale vs engineering judgment vs authority;
- `RT-ENG-002` — never invent rationale;
- `RT-ENG-003` — structured `why is X needed?` reasoning;
- `RT-ENG-004` — proposition-essential / current-implementation / defensive / uncertain reasoning vocabulary;
- `RT-SRC-006` — callers/tests/current code are migration/regression evidence, not automatic retention authority;
- `RT-SRC-007` — producer → integration/composition → consumer trace and earliest sufficient owner;
- `RT-OPS-002` — plan ownership and reference-not-re-specify boundary;
- `RT-OPS-004` — smallest sufficient context;
- `RT-OPS-005` — operation procedure belongs in a non-controlling Skill;
- applicable Learning-by-Doing rules including fair checkpoints, technical independence, and justified depth.

The Skill uses Core `JUST-001..005` as the normative retention owner rather than restating them as independent Planning semantics.

### Simplicity and generality

The Skill requires:

- simplest credible baseline first through Ceremony Tax;
- alternatives only when a real unresolved decision remains;
- no fake alternatives when accepted constraints already decide the choice;
- smallest discriminating investigation when evidence is insufficient;
- Minimum Useful Generality review when known fixtures could distort an automated design;
- no speculative framework/service/directory/agent/process machinery without an admitted current responsibility.

## 5. Behavioral regression bank

Created:

`tools/agent-governance/planning_cases.json`

Cases:

```text
PLAN-001  P0 — tiny/reversible work must not create a durable plan
PLAN-002  P1 — one bounded multi-file responsibility gets a compact plan
PLAN-003  P2 — consequential cross-cutting method uses the ADR boundary correctly
PLAN-004  current callers/tests do not become design authority
PLAN-005  design/plan-only request stops before implementation
PLAN-006  Planning + Learning-by-Doing composition
PLAN-007  plan/specification conflict is surfaced rather than silently followed
PLAN-008  Minimum Useful Generality prevents fixture hardcoding
PLAN-009  P3 — genuinely distinct responsibilities/gates justify a staged plan family
```

This covers both over-planning and under-planning pressure.

`tools/agent-governance/README.md` now registers the scoped planning bank and preserves the existing limitation that the deterministic doctor currently validates only base `cases.json`.

## 6. Deterministic doctor boundary

`governance_doctor.py` currently:

- auto-discovers every directory under `.agents/skills/`;
- requires each Skill to contain `SKILL.md`;
- parses frontmatter;
- requires non-empty `name` and `description`;
- requires the frontmatter `name` to match the Skill directory;
- validates only `tools/agent-governance/cases.json`, not scoped operation banks.

The new Skill satisfies the objective Skill schema:

```text
directory: upgradepilot-planning-design
frontmatter name: upgradepilot-planning-design
frontmatter description: present
SKILL.md: present
```

The scoped `planning_cases.json` is explicitly documented as behavioral/manual regression evidence until Group 7 extends or consolidates the deterministic case-bank validation.

The doctor was not executed in a repository-capable shell during this connector session. Therefore this record does **not** claim an executed doctor PASS. Relevant deterministic predicates were inspected directly from the current branch instead.

## 7. Group-4 acceptance check

### One proportional Skill

PASS — one Planning/Design Skill covers P0 through P3; no small/medium/large duplicate Skills were created.

### Small work avoids unnecessary artifacts

PASS — P0 explicitly selects no durable plan and `PLAN-001` protects it.

### Consequential work is not under-planned

PASS — P2/P3 are explicit and `PLAN-003` / `PLAN-009` protect consequential/staged cases.

### Planning/design-only requests remain non-mutating

PASS — root request boundary remains controlling; the Skill has an explicit stop-before-implementation rule; `PLAN-005` is critical.

### Specification / ADR / plan / implementation responsibilities remain distinct

PASS — Skill and cases distinguish them and reference existing canonical owners.

### Existing implementation is not design authority

PASS — `JUST-*`, rationale/necessity classification, and producer/integration/consumer tracing are operationalized; `PLAN-004` protects this behavior.

### Learning-by-Doing composition

PASS — unfamiliar choices are explained before learner selection and checkpoints require established premises; `PLAN-006` protects the composition.

### Generality pressure

PASS — the Skill explicitly invokes Minimum Useful Generality when known fixtures could distort automated design; `PLAN-008` protects this behavior.

### No unnecessary permanent-control expansion

PASS — no Group-4 rewrite of root/Guide/plan governance owners was needed once their existing generic routing was satisfied by the admitted Skill.

## 8. Validation limitations

No statistically controlled isolated agent-runner evaluation is available through the current GitHub connector workflow.

Therefore:

```text
Skill/schema and owner relationships
→ directly inspected

behavioral cases
→ explicit executable-quality/manual contract

statistical pass rate
→ NOT CLAIMED

governance_doctor execution
→ NOT CLAIMED
```

Group 7 remains responsible for final operation-bank consolidation/doctor extension and whole-system behavioral consistency.

## 9. Main synchronization

At Group-4 completion validation, GitHub comparison reported the governance branch as ahead of `main` and **0 commits behind**.

No parallel `main` change required synchronization during Group 4.

## 10. Stop line

Group 4 stops here.

Do not begin Group 5 Build/Implement work inside this validation record.

The next redesign group may consume the admitted Planning/Design Skill but must independently audit and implement the Build/Implement procedure using the traceability matrix and Group-5 plan.
