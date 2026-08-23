# Group 8 — Technical Specification System Audit and Refinement Plan

**Artifact role:** bounded audit/refinement plan for UpgradePilot's active technical-specification surface after the governance operating-model redesign  
**Branch:** `governance/spec-governance-enhancement-refinement`  
**Primary owners under audit:** `docs/specifications/README.md` and the four registered active specification/engineering-standard files  
**Predecessor:** Group 7 governance consistency/validation  
**Merge boundary:** this group does not authorize merge to `main`

---

## 1. Objective

Audit the active specification system itself rather than assuming that successful governance routing automatically means every specification is still optimally scoped.

The target question is:

> Does each active technical specification/engineering standard still own one clear durable semantic responsibility, remain implementation-neutral at the correct level, avoid procedural/live-state leakage, preserve exact proof and authority boundaries, and compose cleanly with Charter → specification → ADR → plan → source/tests/evidence?

The default disposition is **KEEP**. A file changes only when the audit finds an evidence-backed semantic, ownership, terminology, or maintenance defect.

This group is not a rewrite exercise and is not permission to create new specifications merely for symmetry.

---

## 2. Active surface in scope

Audit as one system:

```text
docs/specifications/README.md

docs/specifications/
  UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md
  UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md
  UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md
  UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md
```

Use the surrounding owners only as discriminating evidence:

```text
PROJECT_CHARTER.md
AGENTS.md
OPERATING_GUIDE.md
docs/README.md
docs/architecture/README.md
relevant accepted ADRs
selected representative plans
representative active source/tests
operation Skills
```

Do not reopen unrelated product design or implementation merely because a specification references it.

---

## 3. Authority and responsibility model

The intended durable chain remains:

```text
PROJECT_CHARTER
→ mission / user / product boundary / claim limits

TECHNICAL SPECIFICATION
→ framework-independent required behavior / semantic invariant / acceptance boundary

ENGINEERING STANDARD
→ cross-cutting engineering quality constraint such as naming clarity

ADR
→ consequential implementation / structural method

PLAN
→ bounded sequence / proof / stop line

SOURCE + TESTS + OBSERVED EVIDENCE
→ implemented truth at the exercised scope

MEMORY.md
→ live project continuation only
```

A specification may constrain implementations strongly without selecting an incidental current mechanism.

A plan/ADR/source fact must not become a specification requirement merely because it is current.

A specification must not become an operation Skill, teaching contract, live-state register, or historical conversation transcript.

---

## 4. External corroboration, not authority

Current spec-driven-development practice provides useful corroborating pressure:

- GitHub Spec Kit separates **specification → implementation plan → tasks → implementation** rather than treating those as one artifact;
- its living-spec model treats the specification as the durable contract while plan/tasks remain derived execution artifacts;
- its guidance recommends decomposing only when complexity justifies the additional overhead.

References:

- <https://github.github.com/spec-kit/>
- <https://github.com/github/spec-kit/blob/main/docs/guides/evolving-specs.md>
- <https://github.com/github/spec-kit/blob/main/docs/concepts/spec-of-specs.md>

These sources are external evidence only. UpgradePilot's own Charter/governance/specification ownership remains controlling.

---

## 5. Audit lenses applied to every file

For each specification/standard, answer proportionately:

### 5.1 Responsibility integrity

- Can its durable responsibility be stated in one sentence?
- Does the body stay inside that responsibility?
- Is a rule actually owned by Charter, Operating Guide, Security, ADR, plan, Skill, source/test, or live memory instead?
- Does another active specification already own the same semantic proposition?

### 5.2 Framework/implementation neutrality

- Is the requirement stated as behavior/meaning/acceptance rather than today's Python class, package layout, provider API, library, or fixture?
- Where implementation techniques are excluded, is the exclusion itself necessary to protect the owned proposition rather than an arbitrary method preference?

### 5.3 Activation and state discipline

- Does the specification avoid claiming that a responsibility is currently active merely because the requirement exists?
- Does it keep live selection/continuation in `MEMORY.md` and bounded activation in the selected plan?
- Are dated incidents/conversation labels kept as provenance rather than active vocabulary?

### 5.4 Proof and authority discipline

- Does it distinguish specification intent from implementation proof?
- Are static/configuration/runtime/model/deterministic evidence strengths separated where material?
- Does it avoid upgrading source/model/schema validity into semantic truth?

### 5.5 Normative precision

- Are MUST/MUST NOT/SHOULD/MAY statements testable or auditable at the owned semantic boundary?
- Are stable IDs necessary, unique, understandable, and still correctly scoped?
- Are examples explanatory rather than accidental contracts?

### 5.6 Terminology and cognitive load

- Are active terms durable rather than historical conversation/session labels?
- Does terminology satisfy the Naming Clarity standard?
- Are learner-teaching procedures accidentally duplicated inside a technical engineering standard?

### 5.7 Proportionality and maintainability

- Can anything be removed/narrowed without losing a real invariant?
- Is a cross-reference better than duplicated semantic prose?
- Would adding a new specification create more ceremony than responsibility value?

---

## 6. Per-file audit routes

### 6.1 Core Pipeline and Contract Specification

Audit especially:

- whether the declared responsibility accurately covers the existing `JUST-001..005` implementation-retention invariants;
- whether `JUST-*` remains the correct canonical owner versus Operating Guide/Skills merely applying it;
- whether product/evidence/trust/failure invariants remain distinct from project-operation procedure;
- whether the specialized-spec relationship is accurate and complete;
- whether any rule is accidentally current-implementation specific.

Initial pressure identified before implementation:

> The body explicitly owns implementation-retention discipline through `JUST-*`, while the header/navigation description currently emphasizes admitted product behavior only. The audit must decide whether to clarify the declared responsibility rather than relocate proven `JUST-*` semantics.

### 6.2 Product Decision Model Specification

Audit especially:

- candidate/applicability/coverage/investigation/stopping semantics versus implementation/planner method;
- static/configuration/runtime evidence strength;
- open-world/negative-evidence boundaries;
- later synthesis boundary;
- historical conversation labels still present in the active semantic surface;
- whether provenance remains historical without leaking old names into current requirements.

Initial pressure:

> Active prose still contains `Conversation-C` / `Conversation-D` labels even though the durable responsibility now has concrete names. These are candidates for terminology cleanup if no semantic meaning depends on them.

### 6.3 Minimum Useful Generality Specification

Audit especially:

- whether it remains an acceptance standard rather than an architecture prescription;
- whether fixture/known-answer rejection is correctly bounded to the owning automated responsibility;
- whether deterministic and model-based methods remain method-neutral when they genuinely satisfy the responsibility;
- whether representative proof classes are proportional rather than universal mandatory test matrices;
- whether selected-plan references add activation detail without turning the specification into live state.

Initial disposition hypothesis:

> **KEEP unless deeper audit finds a concrete defect.** The current file already strongly separates bounded supported-domain generality from speculative universalization and keeps method choice neutral.

### 6.4 Naming Clarity Engineering Standard

Audit especially:

- naming/terminology engineering responsibility versus learner-teaching procedure;
- whether `NAME-005`, `NAME-006`, and the current Explanation Rule duplicate `OPERATING_GUIDE.md` teaching responsibilities;
- whether the recall test should evaluate a competent maintainer rather than use Ali as the engineering-standard subject;
- whether user-facing terminology remains appropriately covered;
- whether implementation-specific examples remain non-binding.

Initial pressure:

> The post-redesign architecture gives `OPERATING_GUIDE.md` and Learning Skills explicit ownership of teaching depth, first-use explanations, and learner context. Naming Clarity should constrain names/terms without becoming a second teaching contract.

---

## 7. Disposition vocabulary

For every audited rule/file use one of:

```text
KEEP
→ responsibility and semantics are already correct

CLARIFY OWNER
→ keep the rule but make its canonical responsibility/boundary explicit

NARROW
→ remove accidental overreach while preserving the valid invariant

MOVE / REFERENCE
→ semantic owner is elsewhere; replace duplicate contract with a precise reference

RENAME / TERMINOLOGY CLEANUP
→ preserve semantics while removing historical/ambiguous vocabulary

ADD MISSING INVARIANT
→ only when a durable cross-implementation requirement is already independently justified

NO NEW SPEC
→ a proposed split/addition does not earn its ceremony cost
```

Every modification must state the concrete defect it fixes.

---

## 8. Expected artifacts

Required planning/audit evidence:

```text
08_TECHNICAL_SPECIFICATION_SYSTEM_AUDIT_AND_REFINEMENT_PLAN.md
00_TECHNICAL_SPECIFICATION_AUDIT_AND_DISPOSITION_MATRIX.md
```

Implementation may modify only evidence-backed owners, expected to be a subset of:

```text
docs/specifications/README.md
UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md
UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md
UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md
UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md
```

Directly required reference surfaces may change only when their ownership/navigation becomes inaccurate.

A dated Group-8 validation/decision record should be written after implementation/review.

Do not create four formal `audits/AUDIT-*` records merely because four files were reviewed. Promote accepted fixes directly to the canonical owners and use one bounded dated validation record unless an independently valuable future reassessment responsibility appears.

---

## 9. Validation sequence

After evidence-backed edits:

```text
1. re-read every active specification as one system
2. verify Charter → specification → ADR → plan → source/test responsibility boundaries
3. verify no active historical conversation/session vocabulary remains where a durable term exists
4. verify no learner-teaching contract remains duplicated in Naming Clarity
5. verify `JUST-*` still has one unambiguous canonical owner
6. verify Minimum Useful Generality remains method-neutral and bounded
7. verify specification README accurately describes each owner
8. run governance_doctor.py
9. inspect changed internal links and stable normative IDs
10. compare branch against main and confirm product source/tests remain untouched by this governance/specification refinement
```

A deterministic doctor PASS proves only the objective relationships it checks. The semantic specification audit remains necessary.

---

## 10. Acceptance criteria

Group 8 passes when:

- all four active specification/standard files have an explicit audited disposition;
- every modification fixes a named semantic/ownership/terminology defect;
- no current implementation detail is promoted merely because it exists;
- no new specification is created without a distinct durable responsibility;
- specification/ADR/plan/source/live-state responsibilities remain separated;
- the Core `JUST-*` owner is explicit and preserved;
- Product Decision Model active vocabulary is durable rather than conversation-derived;
- Naming Clarity no longer competes with project-wide teaching procedure;
- Minimum Useful Generality is either evidence-backed modified or explicitly retained unchanged;
- `docs/specifications/README.md` remains an accurate low-cost entry point;
- deterministic governance validation passes after the final branch state is materialized locally;
- the branch is again ready for a separate explicit merge decision.

---

## 11. Stop line

Do not merge automatically.

Do not modify product source/tests merely to make specification prose look aligned. If the audit discovers real source/spec drift, classify it and stop that product change behind its own authorization/plan rather than hiding it inside Group 8.
