# Governance Redesign — Existing-Rule Traceability Gate

**Date:** 2026-08-23  
**Branch:** `governance/spec-governance-enhancement-refinement`  
**Role:** dated non-controlling audit/validation evidence for the rule-traceability gate inserted after Group 2 and before Group 3

## 1. Why this gate was added

The redesign originally audited canonical governance owners and the B2 learning package as a compatibility case, but it did not yet provide a rule-by-rule migration trace proving that strong existing local rules would be preserved, promoted, specialized, or deliberately left local.

The B2 package contains unusually mature rules created from real learning/building experience. A redesign that only followed file ownership could accidentally leave generally valuable behavior trapped inside that package or drop it while simplifying global files.

The correction was to add:

`plans/governance-spec-governance-enhancement-refinement/00_RULE_OWNERSHIP_PROMOTION_AND_REINFORCEMENT_MATRIX.md`

and make it a mandatory design input for Groups 3–7.

## 2. Sources inspected

The traceability pass inspected the current governance branch versions of:

- `AGENTS.md`;
- `OPERATING_GUIDE.md`;
- `plans/README.md`;
- `audits/README.md`;
- Core `JUST-*` invariants;
- Naming Clarity specification;
- existing repository-audit Skill;
- Learning-by-Doing Skill;
- governance case bank;
- prior agent-governance refinement/evaluation plan;
- B2 learning contract;
- B2 mastery/depth index;
- B2 Career ownership handoff;
- B2 learning package structure and learning-memory role;
- Groups 3–7 redesign plans.

## 3. Main classification result

Existing rules now have explicit dispositions:

```text
KEEP GLOBAL
PROMOTE GLOBAL
APPLY IN SKILL
DELIBERATE REINFORCEMENT
KEEP PACKAGE-LOCAL
PROMOTE PART / KEEP DETAIL LOCAL
```

This preserves one canonical semantic owner while allowing procedural Skills and high-salience reinforcement.

## 4. Immediate promotions applied

The traceability pass found several B2-proven rules broad enough to deserve stronger generic representation before Group 3.

`OPERATING_GUIDE.md` now explicitly owns:

1. current implementation fact vs rationale/failure mode vs engineering judgment vs authority boundary;
2. no invented rationale when evidence does not establish one;
3. structured `why is X needed?` reasoning:
   - proposition/design goal;
   - necessity class;
   - owner/layer;
   - evidence;
   - alternative/trade-off;
4. reasoning vocabulary:
   - proposition-essential;
   - current-implementation requirement;
   - defensive/boundary hardening;
   - uncertain/audit needed;
5. fair learner checkpoints only after the needed premises are established;
6. project-local justification for meaningful mastery/depth assignments;
7. material source-ownership connection to a meaningful focused test when one exists.

The necessity vocabulary is explicitly a reasoning/teaching aid. Core `JUST-*` remains the normative product-retention owner.

## 5. Learning-by-Doing Skill alignment

The Skill now operationalizes the promoted rules without copying the B2 contract:

- labels normal/failure/test-fixture/hypothetical/synthetic example classes when confusion would matter;
- does not ask checkpoints before their premises are known;
- gives a reason for meaningful learning depth;
- connects material source ownership to a focused test when one exists;
- applies `OPERATING_GUIDE.md` §4.3 for `why needed?` reasoning;
- explicitly forbids invented rationale and circular `the code uses it` explanations.

## 6. Rules deliberately kept local

The following remain in the B2/Career package because global promotion would add incorrect or unnecessary ceremony:

- exact S001 → S011 → S005 learning route;
- uv/pyproject/GitHub Actions/tox/BFS technology-depth assignments;
- exact A–N B2 chunk sequence and GREEN/YELLOW/RED package notation;
- B2 0–7 evidence-strength teaching labels;
- exact B2 plan/depth-map pairs and learning continuation;
- Career Day-30 evidence-class/reassessment requirements;
- Career-specific two-consecutive-session executable-contact drift breaker.

General ownership principles extracted from the Career overlay may be applied later by Build/Learning Skills, but Career-specific quotas/status do not become UpgradePilot technical authority.

## 7. Required later-group consumption

The matrix explicitly assigns rule IDs to:

- Group 3 Audit/Review;
- Group 4 Planning/Design;
- Group 5 Build/Implement;
- Group 6 Learning-Only;
- Group 7 Consistency/Validation/Cleanup.

Later groups fail traceability if a proven rule disappears, weakens, relocates without a canonical owner, or becomes globally mandatory despite being package-specific.

## 8. Bounded diff

Compared with the end-of-Group-2 commit `570b940a2b8ee9ee818429034061f1ebfb19f5f6`, the traceability work before this record changed only:

```text
plans/governance-spec-governance-enhancement-refinement/00_RULE_OWNERSHIP_PROMOTION_AND_REINFORCEMENT_MATRIX.md
plans/governance-spec-governance-enhancement-refinement/README.md
OPERATING_GUIDE.md
.agents/skills/upgradepilot-learning-by-doing/SKILL.md
```

The B2 learning package itself was not modified.

## 9. Main synchronization

During this audit, `main` advanced only in `MEMORY.md`. That live-state update was merged into the governance branch without changing the governance traceability decisions.

After synchronization, GitHub comparison reported:

```text
branch ahead of main: 28 commits
branch behind main: 0 commits
```

## 10. Behavioral-case disposition

The existing Group-2 cases `LBD-001` and `LBD-002` remain valid.

Additional behavior implied by this traceability audit is intentionally assigned to the operation groups that own it rather than adding every future case prematurely:

- circular / invented `why needed?` reasoning → Group 3 Audit and Group 4/5 application cases;
- misleading fixture/failure-as-normal teaching → Group 6 Learning-Only and Learning-by-Doing compatibility validation;
- pre-change model / post-change diff / source-test ownership → Group 5 Build cases.

Group 7 must verify that the most failure-prone promoted rules have representative regression cases.

## 11. Stop line

This gate does not implement Group 3.

The next authorized redesign step is still the Group-3 Audit/Review work, but Group 3 must now consume the applicable `RT-*` traceability rows before modifying the audit Skill or related governance surfaces.
