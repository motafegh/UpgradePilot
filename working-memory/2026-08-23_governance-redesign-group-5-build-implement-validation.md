# Governance Redesign — Group 5 Build / Implement Validation

**Date:** 2026-08-23  
**Branch:** `governance/spec-governance-enhancement-refinement`  
**Role:** dated non-controlling implementation/validation record for Group 5 of the governance operating-model redesign

## 1. Scope executed

Group 5 implemented the planned reusable Build/Implement procedure only.

Created/changed:

```text
.agents/skills/upgradepilot-build-implement/SKILL.md
tools/agent-governance/build_cases.json
tools/agent-governance/README.md
```

No product source/tests, accepted specification semantics, ADR decisions, plan semantics, Naming Clarity semantics, or B2 package-local learning rules were changed.

## 2. Inputs audited before implementation

The Group-5 implementation was checked against:

- root `AGENTS.md` Build routing and mutation safeguards;
- `OPERATING_GUIDE.md` Learning-by-Doing, `JUST-*` application method, rationale/necessity reasoning, debugging, proof, Source Clarity outcomes, and handoff rules;
- `plans/governance-spec-governance-enhancement-refinement/05_BUILD_IMPLEMENT_MODE_PLAN.md`;
- `00_RULE_OWNERSHIP_PROMOTION_AND_REINFORCEMENT_MATRIX.md` Group-5 `RT-*` obligations;
- the pre-redesign `OPERATING_GUIDE.md` `SOURCE-CLARITY-001..022` contract on `main` as migration evidence;
- `docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`;
- current Learning-by-Doing, Planning/Design, and Audit Skills;
- current governance evaluation harness.

## 3. Canonical-owner result

No new semantic owner was introduced.

The Build Skill is procedural and applies:

```text
AGENTS.md
→ authorization / operation routing / persistent safeguards

OPERATING_GUIDE.md
→ Learning-by-Doing / proportionality / rationale / debugging / proof / Source Clarity outcomes

Core specification JUST-001..005
→ normative implementation-retention / end-to-end ownership constraints

Naming Clarity specification
→ naming / terminology quality

accepted specification
→ stable required behavior

accepted ADR
→ consequential durable method / structure

selected plan
→ bounded execution / proof / stop scope

source + tests + commands/outputs
→ implementation truth / proof

MEMORY.md
→ live continuation only
```

## 4. Traceability consumption

Group 5 explicitly operationalizes the required traceability families.

### Learning / ownership

- `RT-LBD-009` — AI use/manual typing/green tests do not prove learner ownership.
- Learning-by-Doing remains an overlay rather than mutation authorization.

### Engineering rationale / necessity

- `RT-ENG-001` — current fact, rationale/failure mode, engineering judgment, and authority are separated.
- `RT-ENG-002` — no invented rationale.
- `RT-ENG-003` — `why needed?` uses proposition → necessity → owner/layer → evidence → alternative/trade-off.
- `RT-ENG-004` — necessity labels remain reasoning aids, not product enums.

### Source / tests / mutation / debugging

- `RT-SRC-001` — material ownership requires executable reconstruction, not comments/AI summary alone.
- `RT-SRC-002` — material code-bearing responsibility connects to a meaningful focused test when one exists.
- `RT-SRC-003` — meaningful Learning-by-Doing mutation may use a pre-change model.
- `RT-SRC-004` — actual changed source/tests/diff/result are inspected after AI-assisted implementation and compared with the pre-change model when material.
- `RT-SRC-005` — real unexpected failures use hypothesis/discriminating-check diagnosis; failures are not manufactured for ownership evidence.
- `RT-SRC-006` — tests/callers/current use are regression/migration evidence, not retention authority.
- `RT-SRC-007` — producer → integration/composition → consumer trace and earliest sufficient owner are applied before material downstream duplication.

### Source clarity / naming

- `RT-CLR-001` — seven global Source Clarity outcomes remain canonical in the Operating Guide.
- `RT-CLR-002` — the useful detail from the former 22-rule contract is preserved as optional Build-time heuristics rather than restored as a universal checklist.
- `RT-CLR-003` — Naming Clarity remains the naming/terminology owner; comments do not compensate for vague names.

### Operation / context

- `RT-OPS-001` — primary operation controls authorization; explicit Learning-Only stops product mutation.
- `RT-OPS-004` — smallest sufficient context.
- `RT-OPS-005` — Build procedure lives in one scoped non-controlling Skill.
- `RT-OPS-006` — operation-specific behavioral regression cases added.

## 5. Source Clarity migration result

The former `SOURCE-CLARITY-001..022` contract was inspected from the pre-redesign Operating Guide.

Its valuable detailed lenses were not discarded. The Build Skill now preserves them as 17 proportional heuristic groups, including:

```text
reader independence / START-HERE orientation
bidirectional cross-file flow
project-local import roles
constants / literals / regex / sentinel meaning
decision-boundary why comments
layered explanation
semantic / proof transformations
callable IO + representative shapes
primary semantic API vs support APIs
structural grouping
type-state / narrowing meaning
guard clauses as evidence permissions
semantic algorithms / data structures
terminology collision handling
current / transitional / legacy surfaces
bounded clarity obligation when touching old code
comment/docstring maintenance
```

These heuristics are subordinate to the compact global acceptance question:

> Can a competent developer understand the component's responsibility, important data flow, non-obvious reasoning, ownership boundaries, and proof limits from the repository itself without relying on prior chat?

This preserves the rich source-writing intent while removing the old incentive to satisfy a 22-rule/21-question checklist mechanically.

## 6. Naming-standard audit

The Naming Clarity specification was inspected and remained coherent as the canonical naming owner.

No semantic edit was justified.

The Build Skill references/applies it and reinforces only procedural consequences such as responsibility-bearing names before comment compensation.

## 7. Build behavioral regression bank

Created:

`tools/agent-governance/build_cases.json`

Cases:

```text
BUILD-001 — authorized bounded implementation
BUILD-002 — callers/tests do not prove retention
BUILD-003 — trace before duplicate downstream validation
BUILD-004 — Source Clarity without comment inflation
BUILD-005 — specification/ADR/plan conflict stops implementation
BUILD-006 — Build + Learning-by-Doing pre/post ownership
BUILD-007 — explicit Learning-Only stops mutation
BUILD-008 — unexpected failure diagnosis before broad patching
BUILD-009 — static/source review != runtime validation
BUILD-010 — source ↔ focused-test coupling and proof limit
```

The bank uses the same schema shape as the base governance cases.

It is currently a behavioral/manual regression surface. `governance_doctor.py` still validates only `cases.json`; Group 7 owns scoped-bank consolidation or deterministic loading. No doctor PASS is claimed for `build_cases.json` merely because it exists.

## 8. Router / Operating Guide / plan-owner disposition

No additional Group-5 edit was made to `AGENTS.md`, `OPERATING_GUIDE.md`, `plans/README.md`, or the Naming Clarity specification.

Reason:

- root already routes Build/Implement to the admitted Build procedure **when present**;
- the procedure is now present under `.agents/skills/upgradepilot-build-implement/`;
- the Operating Guide already owns the required global behavior and explicitly delegates detailed Build-time Source Clarity application to operation Skills;
- the plan and naming owners are already correctly scoped.

Adding more always-on prose solely to repeat the new path would increase context without fixing an observed routing gap.

## 9. Group-5 bounded diff

Compared with the completed Group-4 validation commit:

`0bb68d32beefa09c6160ac7774df131c95747f45`

before this record, Group 5 changed exactly:

```text
.agents/skills/upgradepilot-build-implement/SKILL.md
tools/agent-governance/build_cases.json
tools/agent-governance/README.md
```

GitHub comparison reported 3 commits ahead of that Group-4 boundary and no other changed files.

## 10. Main synchronization

At the Group-5 acceptance check, GitHub reported:

```text
governance/spec-governance-enhancement-refinement
44 commits ahead of main
0 commits behind main
```

No synchronization merge was required during Group 5.

## 11. Validation limits

The GitHub connector supports repository inspection/writes but this environment does not provide a checked-out repository shell for executing `tools/agent-governance/governance_doctor.py` against the branch.

Therefore:

- Skill frontmatter/directory-name compatibility was inspected directly;
- scoped case schema/fields were inspected directly;
- canonical-owner and traceability relationships were semantically reviewed;
- exact branch diff and main relationship were checked through GitHub;
- no executed governance-doctor PASS is claimed.

Group 7 remains responsible for deterministic harness extension and final executable governance validation when the environment permits.

## 12. Acceptance conclusion

Group 5 satisfies its redesign acceptance boundary:

- Build has one admitted reusable procedure;
- mutation requires Build/change intent;
- active source/tests precede behavior edits;
- `JUST-*` and end-to-end ownership are operationalized;
- Source Clarity remains rich but becomes outcome-driven rather than comment-volume/checklist-driven;
- Naming Clarity remains the naming owner;
- tests are proof for exercised responsibility, not architecture authority;
- validation scales from narrow to broader evidence according to risk/claim;
- Learning-by-Doing has explicit pre-change/post-change ownership support;
- explicit Learning-Only stops Build mutation;
- no product semantics were changed for governance convenience.

## 13. Stop line

This record closes Group 5 only.

The next redesign dependency is **Group 6 — Learning Only**. It must consume the traceability matrix and integrate with existing package-local learning contracts/plans/`LEARNING_MEMORY.md` without replacing them or authorizing product mutation.
