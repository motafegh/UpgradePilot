# Governance Redesign — Group 3 Audit / Review Validation

**Date:** 2026-08-23  
**Branch:** `governance/spec-governance-enhancement-refinement`  
**Role:** dated non-controlling implementation/validation evidence for Group 3  
**Plan:** `plans/governance-spec-governance-enhancement-refinement/03_AUDIT_REVIEW_MODE_PLAN.md`  
**Mandatory traceability input:** `plans/governance-spec-governance-enhancement-refinement/00_RULE_OWNERSHIP_PROMOTION_AND_REINFORCEMENT_MATRIX.md`

## 1. Group boundary

Group 3 refined the existing Audit/Review procedure only.

It did **not**:

- create a second audit Skill;
- change product behavior;
- modify product source/tests;
- change accepted specifications or ADRs;
- implement findings that an audit might discover;
- change B2 learning-package files;
- create a new audit record merely because the procedure was redesigned.

Audit remains read-only by default.

## 2. Latest-main synchronization

Before Group-3 implementation, `main` had advanced only in `MEMORY.md`.

That latest live-state content was merged into the governance branch before Group-3 edits. The governance redesign did not reinterpret or overwrite the B2 product continuation.

A temporary connector sync marker was created and removed immediately during low-level synchronization. It has no surviving tree content and no governance meaning.

The Group-3 synchronized baseline commit is:

```text
fc95ef9f5ef6a8c088353624be52d1de9a3d2f1f
```

## 3. Files changed by Group 3

Compared with the synchronized baseline above, Group 3 changed exactly:

```text
.agents/skills/upgradepilot-repository-audit/SKILL.md
tools/agent-governance/audit_cases.json
tools/agent-governance/README.md
```

GitHub comparison reported:

```text
3 commits ahead of Group-3 synchronized baseline
0 behind
```

No other controlling governance owner needed semantic modification for this group.

## 4. Why root/Operating Guide/audits README were not changed again

### `AGENTS.md`

Group 1 already provides the required route:

```text
Audit / Review
→ use the admitted repository-audit Skill for materially evaluative review
→ preserve read-only boundary unless change intent is separately explicit
```

Manual `use audit mode` routing is also already admitted. Repeating the exact Skill path again would add little value and would conflict with the redesign goal of keeping root high-signal.

### `OPERATING_GUIDE.md`

It already owns the global reasoning needed by Audit:

- Learning-by-Doing composition;
- implementation fact vs rationale vs engineering judgment;
- `why is X needed?` reasoning;
- necessity vocabulary;
- Ceremony Tax;
- `JUST-*` application method;
- producer → integration → consumer reasoning;
- evidence/proof discipline;
- compact Source Clarity outcomes.

Group 3 therefore **applies** these rules in the Skill rather than creating a second semantic owner.

### `audits/README.md`

It already owns the durable audit-record boundary, compact/formal modes, lifecycle, non-controlling status, and proportional record discipline. Group 3 only operationalizes those rules in the Skill.

No semantic defect was found that justified modifying that owner.

## 5. Rule-traceability consumption

Group 3 explicitly consumes these matrix families.

### Learning/technical independence

```text
RT-LBD-007
```

The Skill evaluates Ali's hypotheses, current code, prior assistant claims, and documents by the same evidence standard. Learning-by-Doing composition does not turn agreement into validation.

### Engineering rationale / necessity

```text
RT-ENG-001
RT-ENG-002
RT-ENG-003
RT-ENG-004
RT-ENG-005
RT-ENG-006
```

Implemented in the Skill as:

- current implementation fact vs rationale/failure mode vs engineering judgment vs authority boundary;
- explicit prohibition on invented rationale;
- proposition → necessity → owner/layer → evidence → alternative reasoning;
- proposition-essential/current-implementation/defensive/uncertain vocabulary;
- proportionate Audit + Learning-by-Doing composition;
- overlapping-evidence analysis.

### Source/retention ownership

```text
RT-SRC-006
RT-SRC-007
```

Implemented through direct `JUST-001..005` application and end-to-end producer → integration/composition → consumer analysis.

### Clarity / maintainability

```text
RT-CLR-001
RT-CLR-002
RT-CLR-003
```

The Skill uses the seven global Source Clarity outcomes and preserves detailed former Source-Clarity rules only as optional audit probes rather than restoring the old universal checklist.

Naming Clarity remains the naming owner.

### Operation / audit artifact discipline

```text
RT-OPS-003
RT-OPS-004
RT-OPS-005
RT-OPS-006
```

The Skill keeps audit records proportional, uses smallest-sufficient context, remains procedural/non-controlling, and is backed by behavioral regression cases.

## 6. Refined Audit procedure

The Audit Skill now scales across three depths:

```text
bounded review
cross-responsibility audit
governance-system audit
```

It provides one common flow:

```text
exact audit question
→ needed owners
→ independent observed/implementation truth
→ cross-owner relationship when material
→ relevant audit lenses
→ precise finding/uncertainty classification
→ smallest justified disposition
→ durable audit only when warranted
→ STOP without mutation
```

## 7. Cross-owner consistency model

The Skill now has a bounded semantic consistency walk:

```text
Charter / admitted product boundary, when material
→ specification
→ ADR, when one exists and matters
→ selected plan
→ active source/tests/evidence
→ live state only when continuation is part of the question
```

It explicitly does **not** require every layer to exist.

Disagreement is classified into the narrowest useful owner category, such as:

- requirement/specification drift;
- ADR/method drift;
- plan drift;
- implementation defect;
- test/proof gap;
- documentation drift;
- state leakage;
- unresolved conflict.

This avoids both universal document precedence and the false assumption that every mismatch is an implementation bug.

## 8. Retention and ownership model

The Skill explicitly rejects circular retention reasoning such as:

```text
keep X because Y consumes X
```

when Y's dependence is itself under review.

For material cross-layer mechanisms it now traces:

```text
proposition
→ producer
→ integration/composition
→ earliest sufficient owner
→ downstream repetition
→ independent later responsibility/risk, if any
→ concrete proof loss/failure without the repeat
→ KEEP / MOVE / NARROW / REMOVE
```

Direct internal callability and fabricated fixtures are not treated as production contracts unless explicitly admitted.

## 9. Overlapping-evidence correction

The Skill also guards against the opposite failure: deleting every duplicate-looking value.

When evidence branches overlap, Audit now asks:

```text
what each artifact directly establishes
where information overlaps
what is primary vs derived/duplicated
what implementation consumes
what none proves alone
what relation exists only when branches are combined
```

This is important for independently produced evidence branches where the **relationship** between otherwise valid objects is itself a real proposition.

## 10. Source clarity audit behavior

Group 3 does not restore the former 22-rule always-on Source Clarity contract.

Audit uses the compact global outcomes plus optional probes such as:

- START-HERE / primary semantic API;
- bidirectional flow;
- representative shapes;
- domain constants/regex/vocabulary;
- decision-boundary why-comments;
- guard permissions;
- meaningful algorithms/control flow;
- terminology collisions;
- current/transitional/legacy visibility.

The acceptance target remains recoverable responsibility/flow/reasoning/proof limits, not comment volume.

## 11. Behavioral regression bank

Created:

```text
tools/agent-governance/audit_cases.json
```

Cases:

```text
AUDIT-001 read-only audit boundary
AUDIT-002 callers/tests do not prove retention
AUDIT-003 end-to-end downstream validation ownership
AUDIT-004 cross-owner specification/ADR/plan/source consistency
AUDIT-005 no unnecessary durable audit record
AUDIT-006 Audit + Learning-by-Doing composition
AUDIT-007 overlapping evidence is not automatically redundant
```

These cases grade action/trajectory properties rather than exact prose.

## 12. Evaluation-bank decision

The Group-3 cases were added as a scoped operation bank instead of making the already broad base `cases.json` harder to navigate.

`tools/agent-governance/README.md` now explicitly states:

- `cases.json` remains the base bank;
- `audit_cases.json` is a scoped Group-3 behavioral extension;
- the current deterministic doctor validates the base bank only;
- scoped audit cases must **not** be reported as doctor-validated yet;
- Group 7 must decide whether to extend the doctor to scoped banks or consolidate the banks after all operation families exist.

This is an explicit limitation, not an implied PASS.

## 13. Validation performed

### Structural checks

Confirmed from the branch:

- `.agents/skills/upgradepilot-repository-audit/SKILL.md` exists;
- frontmatter name remains `upgradepilot-repository-audit` and matches the directory;
- Skill remains explicitly procedural/non-controlling;
- read-only audit boundary is explicit at activation and stop sections;
- seven `AUDIT-*` cases have unique IDs within the scoped bank;
- each scoped case contains action mode, owners, must-do/must-not-do, criticality, and rationale;
- governance-evaluation README registers the scoped bank and its doctor limitation;
- no B2 learning-package or product source/test file was changed by Group 3.

### Semantic scenario checks

The procedure was checked against the Group-3 plan scenarios:

1. **read-only implementation review** → inspect/report, no mutation;
2. **caller/test retention pressure** → trace independent admitted need, no retention by inertia;
3. **duplicate downstream validation** → producer/integration/consumer trace and earliest sufficient owner;
4. **spec/implementation mismatch** → classify which owner is actually inconsistent;
5. **small local observation** → no durable audit artifact unless future value exists;
6. **Audit + Learning-by-Doing** → explanation and learner challenge without changing audit authorization;
7. **overlapping evidence** → distinguish duplicated facts from a real cross-branch composition proposition.

All are explicitly represented in the refined Skill and scoped cases.

## 14. Deterministic-doctor limitation

The existing `governance_doctor.py` has not been changed in Group 3 and does not yet load `audit_cases.json`.

Therefore:

```text
base bank doctor coverage != scoped audit-bank doctor coverage
```

No executed doctor PASS is claimed for the scoped bank.

Group 7 owns the deterministic-harness extension/consolidation decision.

## 15. Group-3 acceptance result

Group 3 satisfies its planned functional acceptance:

- root routing already selects the admitted audit Skill;
- audit remains read-only by default;
- `JUST-*` and end-to-end ownership are explicitly operationalized;
- cross-owner consistency has a bounded procedure;
- durable audit recording remains proportional;
- Learning-by-Doing composition is explicit;
- observation, evidence, interpretation, uncertainty, finding, consequence, and disposition are separated;
- high-risk audit regressions have representative behavioral cases;
- proven B2/global rules identified by the traceability matrix were consumed rather than lost or copied blindly.

## 16. Stop line

Group 3 is complete.

Do not implement Group 4 Planning/Design inside this record. The next redesign group may rely on the refined Audit procedure and must again consume its applicable `RT-*` matrix rows before changing Planning/Design controls.
