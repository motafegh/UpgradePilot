# Governance Redesign — Group 8 Technical Specification Audit Validation

**Date:** 2026-08-23  
**Branch:** `governance/spec-governance-enhancement-refinement`  
**Group-8 baseline:** `b2f32e90bdb6d2393b035a6a4ba5ae5047fc83bd`  
**Role:** dated audit/refinement validation evidence  
**Controlling plan:** `plans/governance-spec-governance-enhancement-refinement/08_TECHNICAL_SPECIFICATION_SYSTEM_AUDIT_AND_REFINEMENT_PLAN.md`  
**Disposition matrix:** `plans/governance-spec-governance-enhancement-refinement/00_TECHNICAL_SPECIFICATION_AUDIT_AND_DISPOSITION_MATRIX.md`

## 1. Why Group 8 exists

Groups 1–7 redesigned and validated UpgradePilot's governance operating model and operation Skills. After the Group-7 doctor passed locally, Ali explicitly expanded the pre-merge scope to ask a separate question:

> Are the active files under `docs/specifications/` themselves still correctly scoped and optimized after the governance redesign, or were they only treated as authorities during that work?

Group 8 therefore audits the active specification system itself. It does not retroactively invalidate the Group-7 result; it extends the branch review before merge.

## 2. External corroboration used

Contemporary GitHub Spec Kit material was used as non-controlling corroboration for the ownership boundary:

```text
specification / intent
→ implementation plan
→ tasks / bounded execution
→ implementation
```

and for the living-spec concept where the specification remains the durable contract while execution artifacts evolve separately.

References recorded in the Group-8 plan:

- https://github.github.com/spec-kit/
- https://github.com/github/spec-kit/blob/main/docs/guides/evolving-specs.md
- https://github.com/github/spec-kit/blob/main/docs/concepts/spec-of-specs.md

UpgradePilot's own Charter/governance/specification owners remained authoritative.

## 3. Active specification dispositions

### Core Pipeline and Contract Specification

**Disposition: MODIFY — CLARIFY OWNER.**

Finding:

- `JUST-001..005` are already and intentionally canonical in the Core specification;
- §7 and §9 already describe implementation-retention discipline;
- the header/opening boundary previously described only admitted product behavior, understating the file's actual canonical responsibility.

Change:

- header Responsibility now explicitly includes implementation-retention and cross-layer ownership constraints;
- opening boundary describes both product/evidence invariants and framework-independent retention/ownership constraints;
- specialized-spec relationship description matches that owner.

Critical preservation:

- `JUST-001..005` requirement text was not rewritten;
- the redesign still treats Core as the only normative `JUST-*` semantic owner;
- AGENTS/Operating Guide/Skills remain reinforcement/application surfaces only.

### Product Decision Model Specification

**Disposition: MODIFY — TERMINOLOGY CLEANUP ONLY.**

Finding:

Active semantic prose still used historical labels:

- `Conversation-D/final maintainer-facing synthesis`;
- `Conversation-C investigation logic`.

The specification already has durable responsibility names for those concepts.

Change:

- active boundary now says `later maintainer-facing synthesis/policy`;
- investigation boundary now says `this investigation-selection responsibility`.

Historical provenance remains unchanged in spirit and continues to identify:

- Conversations A/B/C reconciliation;
- the post-conversation-C audit filename;
- C01/C203 pressure evidence.

No candidate/applicability/coverage/investigation/stopping semantic changed.

### Minimum Useful Generality Specification

**Disposition: KEEP UNCHANGED.**

The file already:

- owns one clear automated-capability acceptance responsibility;
- distinguishes supported-domain generality from universalization;
- rejects known-fixture/manual-interpretation substitution without mandating one architecture;
- keeps deterministic/model methods conditional and method-neutral;
- treats proof classes as conditional/proportional;
- keeps live activation outside the specification.

The branch blob remains:

`742aacfd050abaddf2a9f866e6cbffb44b409fd3`

which is the same blob audited before Group 8.

### Naming Clarity Engineering Standard

**Disposition: MODIFY — NARROW + REFERENCE.**

Finding:

The standard correctly owned naming/terminology quality but also duplicated learner-teaching semantics now owned by `OPERATING_GUIDE.md` and Learning procedures:

- first-use practical teaching/depth in `NAME-005`;
- `learning explanations` in `NAME-006`;
- the full Explanation Rule including depth now/deferred;
- Ali-specific recall-test wording.

Change:

- responsibility now targets competent-maintainer recoverability;
- boundary explicitly excludes learner-teaching procedure;
- `NAME-005` now requires project-specific/overloaded/non-obvious terms to be defined at the narrowest durable owner when ambiguity is material;
- `NAME-006` now applies to user-facing CLI/report terminology rather than learning explanations;
- `NAME-009` uses a competent-maintainer recall test;
- §3 is now an artifact-local terminology rule;
- learner-facing full-form/name-origin/depth teaching explicitly routes to `OPERATING_GUIDE.md` and applicable Learning procedures.

The naming quality bar was not weakened; competing teaching ownership was removed.

## 4. Specification-system/index changes

### `docs/specifications/README.md`

Added compact specification admission/quality guidance:

```text
one distinct durable semantic responsibility
→ why an existing owner cannot absorb it
→ implementation-neutral contract at owned level
→ owner relationships
→ proof/non-proof boundary
→ stable terminology/IDs when justified
→ change/reassessment boundary
```

It now explicitly excludes:

- live state;
- plan/Skill execution procedure;
- incidental current library/source-layout choices;
- historical conversation/session vocabulary from active semantics;
- copied requirements with another canonical owner;
- documentation-as-implementation-proof claims.

Navigation now identifies Core's implementation-retention ownership and Naming Clarity's non-teaching boundary.

### `docs/README.md`

The documentation map was updated only where the owner description changed:

- Core navigation includes implementation-retention/ownership constraints;
- promotion/specification descriptions allow explicitly owned framework-independent cross-implementation acceptance constraints;
- high-level specification map matches the audited surface.

No live state was added.

## 5. Behavioral regression protection

Group 8 did not create a seventh case bank.

Instead, `tools/agent-governance/consistency_cases.json` remains the cross-system bank and was extended from five to eight cases with:

- `CONSISTENCY-006` — current implementation/library/test success must not automatically become specification method;
- `CONSISTENCY-007` — durable active specification vocabulary versus historical conversation labels;
- `CONSISTENCY-008` — Naming Clarity terminology ownership versus learner-teaching procedure.

`tools/agent-governance/README.md` was updated to describe the Group-8 extension while keeping the doctor at six case banks.

## 6. Group-8 bounded diff

Immediately before this validation record, Group 8 was:

```text
10 commits ahead of baseline b2f32e90...
0 commits behind that baseline
```

and changed exactly ten files:

```text
docs/README.md
docs/specifications/README.md
docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md
docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md
docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md
plans/governance-spec-governance-enhancement-refinement/00_TECHNICAL_SPECIFICATION_AUDIT_AND_DISPOSITION_MATRIX.md
plans/governance-spec-governance-enhancement-refinement/08_TECHNICAL_SPECIFICATION_SYSTEM_AUDIT_AND_REFINEMENT_PLAN.md
plans/governance-spec-governance-enhancement-refinement/README.md
tools/agent-governance/README.md
tools/agent-governance/consistency_cases.json
```

Not changed by Group 8:

```text
docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md
AGENTS.md
OPERATING_GUIDE.md
SECURITY.md
ENVIRONMENT.md
MEMORY.md
docs/architecture/*
product plans outside this redesign family
src/upgradepilot/*
tests/*
```

This is a specification/governance refinement only, not product implementation work.

## 7. Semantic acceptance result

No P0/P1 specification conflict was found.

The final audited split is:

```text
PROJECT_CHARTER
→ mission / user / product boundary / evidence doctrine / claim limits

CORE SPECIFICATION
→ project-wide trust/evidence/representation/failure invariants
→ implementation-retention / earliest-sufficient-owner constraints

PRODUCT DECISION MODEL SPECIFICATION
→ candidate / applicability / coverage / investigation / stopping semantics

MINIMUM USEFUL GENERALITY SPECIFICATION
→ bounded generality acceptance for variable-input automated responsibilities

NAMING CLARITY ENGINEERING STANDARD
→ names and durable terminology clarity

OPERATING_GUIDE + Learning procedures
→ learner-facing explanation/depth/teaching method

ADRs
→ consequential method / structure

PLANS
→ bounded sequence / proof / stop line

SOURCE + TESTS + OBSERVED EVIDENCE
→ implementation truth

MEMORY.md
→ live continuation only
```

No new technical specification was justified.

## 8. Deterministic validation status

Connector-backed review found no objective defect in the changed surfaces:

- all changed internal repository-relative links resolve at reviewed paths;
- active specification stable-ID families remain distinct;
- no stable IDs were added/renamed by Group 8;
- `consistency_cases.json` retains the required schema fields and disjoint `CONSISTENCY-NNN` IDs;
- the doctor still has six configured case banks;
- the active specification set remains the same four registered files;
- `main` was still the merge base with the governance branch 0 commits behind at the final pre-record comparison.

However, the earlier executable doctor PASS at `542a7de2...` predates Group 8 and is **not** proof for this final branch state.

Required final executable proof:

```bash
python tools/agent-governance/governance_doctor.py
```

must be rerun locally after pulling the final Group-8 branch tip.

Until that PASS is observed and recorded, Group 8 is:

```text
planning/audit                 COMPLETE
specification refinement      COMPLETE
semantic validation           COMPLETE
connector objective review    COMPLETE / no defect found
executable doctor             PENDING on final Group-8 tip
merge                         NOT AUTHORIZED / NOT PERFORMED
```

## 9. Stop line

Do not merge yet.

After the final local doctor PASS is supplied, record that proof, recheck `main` freshness, and then make a separate explicit merge decision.
