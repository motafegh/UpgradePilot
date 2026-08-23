# Governance Redesign Group 2 — Learning-by-Doing Validation

**Date:** 2026-08-23  
**Branch:** `governance/spec-governance-enhancement-refinement`  
**Group plan:** `plans/governance-spec-governance-enhancement-refinement/02_LEARNING_BY_DOING_MODE_PLAN.md`  
**Artifact role:** dated non-controlling implementation/validation evidence; not live project-position authority

## 1. Bounded Group-2 result

Group 2 admits one new procedural surface:

```text
.agents/skills/upgradepilot-learning-by-doing/SKILL.md
```

and makes only the minimum permanent-control/evaluation changes needed to activate and test it:

```text
AGENTS.md
OPERATING_GUIDE.md
tools/agent-governance/cases.json
```

The B2 package-local learning contract/plans/`LEARNING_MEMORY.md`, product source/tests, accepted product specifications, ADRs, `SECURITY.md`, `ENVIRONMENT.md`, and plan/audit governance were not rewritten by the Group-2 implementation.

`MEMORY.md` changed on this branch only through merges from advancing `main`; Group 2 did not claim or replace live project state.

## 2. Canonical-owner result

The responsibility split is now explicit:

```text
OPERATING_GUIDE.md
→ canonical project-wide Learning-by-Doing philosophy and durable rules

upgradepilot-learning-by-doing Skill
→ reusable activation/composition procedure

primary operation
→ actual action boundary and detailed Audit / Planning / Build / Debug procedure

package-local learning contract
→ specialized learning invariants when that package is active
```

The Skill is deliberately non-controlling and states that it does not authorize implementation, planning artifacts, external actions, or product mutation by itself.

## 3. Activation result

The Skill is activated when:

1. Ali explicitly requests Learning-by-Doing or asks to learn while doing/building/designing/auditing/debugging; or
2. substantive UpgradePilot work materially benefits from the full reasoning → action → evidence → ownership-transfer cycle.

The Skill is not force-loaded for tiny repetitive edits, familiar safe commands, or narrow factual lookups when `OPERATING_GUIDE.md` already provides enough method.

This preserves:

```text
high-value automatic Learning-by-Doing
+
explicit manual reinforcement
+
proportional context loading
```

## 4. Composition behavior

Learning-by-Doing is represented as an overlay:

```text
PRIMARY OPERATION
Audit | Planning/Design | Build/Implement | Debug/Diagnose | Review | other bounded work

+
LEARNING-BY-DOING
orientation → reasoning → real action → evidence → model correction → ownership transfer
```

The primary operation remains responsible for authorization and detailed action procedure.

### Audit / Review

Learning adds explanation, reasoning, and critical understanding. Audit remains read-only unless separate change intent exists.

### Planning / Design

Learning makes the responsibility, alternatives, trade-offs, evidence needs, and artifact choice understandable before Ali is expected to select among them. Planning still does not authorize implementation.

### Build / Implement

Learning adds source/data-flow orientation, high-value mechanism explanation, evidence review, and progressive ownership transfer. Build remains responsible for mutation scope and validation.

### Debug / Diagnose

Learning uses hypothesis → discriminating check → evidence → model correction and explicitly records surprising failures as model gaps rather than hiding them.

## 5. Technical-independence result

The Skill preserves the project rule that learning does not mean endorsing the current implementation.

When Ali challenges a premise, the procedure requires stopping advancement of that local proposition and evaluating:

```text
Ali's claim
current implementation
prior assistant claim
comments/tests/design
```

by the same evidence standard.

The Skill also routes material retention/ownership questions back to the canonical `JUST-*` and end-to-end responsibility rules without turning every learning step into a formal repository audit.

## 6. Learning-Only boundary

The new Skill explicitly handles the transition:

```text
Learning-by-Doing active
+ Ali says stop building / just learn
→ product mutation paused
→ Learning-Only behavior
→ existing code/design/plan/evidence becomes learning material
→ package-local learning contract/plan/memory used when applicable
```

A dedicated Learning-Only Skill remains Group 6 work. Its absence does not weaken the current no-product-mutation boundary.

## 7. B2 package compatibility

The existing B2 mastery contract already defines:

```text
OPERATING_GUIDE.md
→ project-wide learning/execution rules

package contract
→ global teaching/learning rules for the package

PLAN_XX
→ local route/gates

LEARNING_MEMORY.md
→ package learning continuity

source/tests
→ implementation truth
```

Group 2 preserves this architecture. No package-local edit was needed merely to mention the new general Skill.

The new Skill explicitly says to load package-local contract/plan/depth map/`LEARNING_MEMORY.md` only when that package is active or the task depends on its learning state.

## 8. Behavioral regression cases

Two cases were added to `tools/agent-governance/cases.json`.

### `LBD-001` — composition

Tests that a request to design/implement while learning:

- identifies the primary operation;
- activates Learning-by-Doing as an overlay;
- uses real project action/evidence rather than a detached tutorial;
- keeps explanation proportional;
- creates meaningful ownership-bearing reasoning/action opportunities;
- does not let learning silently broaden scope.

### `LBD-002` — Learning-Only switch

Tests that an explicit `stop building; just learn` request:

- pauses product mutation;
- leaves Build as inactive mutation procedure;
- uses existing code/design/evidence as learning material;
- routes to package-local learning continuity when applicable;
- does not create a duplicate learning package.

Both case IDs are new/unique and use existing case-bank fields and allowed `high` criticality.

## 9. Group-plan scenario review

### Scenario A — design discussion

Represented correctly:

```text
Planning/Design primary
+ Learning-by-Doing overlay
+ unfamiliar alternatives explained before selection
```

No Learning-Only package is created.

### Scenario B — ordinary coding

Represented correctly:

```text
Build primary
+ material source/data-flow explanation
+ real action/evidence
+ meaningful Ali reasoning/testing participation
```

The Skill explicitly rejects turning implementation into a lecture.

### Scenario C — challenge to a premise

Represented correctly: stop advancing the challenged local proposition, test the claim and implementation by evidence, then resume only when the premise is sufficiently resolved.

### Scenario D — tiny repetitive edit

Represented correctly: the full Skill need not be loaded; Learning-by-Doing remains proportional through the Operating Guide.

### Scenario E — explicit just-learn request

Represented correctly: product mutation pauses and the route switches to Learning-Only/package-local learning behavior.

## 10. Governance-doctor validation boundary

A direct clone/run of:

```text
python tools/agent-governance/governance_doctor.py
```

could not be executed in the available assistant-side runtime because DNS resolution for `github.com` failed during clone.

This is **not** an executed PASS.

The unchanged doctor's relevant deterministic predicates were checked against branch evidence instead:

- `.agents/skills/` exists and now contains `upgradepilot-repository-audit` and `upgradepilot-learning-by-doing`;
- the new directory contains `SKILL.md`;
- frontmatter contains non-empty `name` and `description`;
- frontmatter `name: upgradepilot-learning-by-doing` exactly matches the directory name;
- `cases.json` still contains the required schema fields and critical-case references;
- `LBD-001` and `LBD-002` are unique IDs, use list-valued owner/must fields, and use allowed `high` criticality;
- required core governance files remain present;
- Group 2 introduced no new Markdown link whose target must be resolved by the doctor.

An actual doctor execution remains required when a repository-capable shell is available.

## 11. Group-2 stop line

Group 2 does not design or implement the full Audit, Planning/Design, Build/Implement, or Learning-Only procedures.

Those remain Groups 3–6.

The next redesign group may rely on this composition contract but must not copy the full Learning-by-Doing philosophy into its own Skill.

This record is dated execution/validation evidence only. `MEMORY.md` remains the sole live project-continuation owner.