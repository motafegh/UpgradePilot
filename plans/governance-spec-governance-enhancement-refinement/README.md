# Governance + Specification Enhancement and Refinement Plans

This directory owns the bounded planning and provenance for refining UpgradePilot's governance/specification operating system.

The work concerns how durable controls are organized, loaded, reinforced, validated, and specialized for recurring operating modes such as audit, planning/design, implementation, learning-by-doing, and learning-only sessions.

The planning family was executed sequentially on branch `governance/spec-governance-enhancement-refinement` through Groups 1–7. That is **plan-family lifecycle/provenance**, not live project-position authority and not evidence that the redesign has been merged into `main`. Root `../../AGENTS.md`, the project charter, accepted specifications/ADRs, and other responsibility owners control according to the repository revision actually being used; `../../MEMORY.md` remains the sole live project-continuation owner.

## Responsibility

Plans in this directory coordinate and preserve the rationale for:

- refinement of always-on governance context;
- deliberate reinforcement of critical rules without ambiguous ownership;
- operation-specific Agent Skills and routing;
- reduction of unnecessary persistent context and oversized mixed-responsibility sections;
- cross-owner consistency analysis and deterministic governance checks;
- proportionate simplification of security/trust controls;
- migration of existing procedures into better-scoped owners;
- validation and merge criteria for the resulting governance redesign.

They preserve the distinction between:

```text
canonical durable owner
→ authoritative semantic rule

operation-specific skill/procedure
→ reusable way to apply the owners for one kind of work

working memory / learning memory
→ continuity and dated state/evidence

source/tests/commands
→ implementation truth and proof appropriate to the claim
```

## Change and merge boundary

A plan does not authorize its own implementation. The Groups 1–7 changes described here were implemented only after separate user authorization during the bounded redesign branch work.

Likewise, completing and validating this plan family does **not** authorize merging the branch into `main`. Merge remains a separate explicit decision after Group-7 merge-readiness review.

---

## Planning set

### Master redesign

[`GOVERNANCE_OPERATING_MODEL_REDESIGN_PLAN.md`](GOVERNANCE_OPERATING_MODEL_REDESIGN_PLAN.md)

Defines the overall target operating model, redesign principles, migration intent, major decision points, validation philosophy, and merge criteria.

### Cross-group audit and dependency map

[`00_GROUP_AUDIT_AND_DEPENDENCY_MAP.md`](00_GROUP_AUDIT_AND_DEPENDENCY_MAP.md)

Audits the governance relationships and defines the seven redesign groups, canonical-owner/reinforcement model, cross-group dependencies, operation composition, and group acceptance rule.

### Mandatory existing-rule traceability gate

[`00_RULE_OWNERSHIP_PROMOTION_AND_REINFORCEMENT_MATRIX.md`](00_RULE_OWNERSHIP_PROMOTION_AND_REINFORCEMENT_MATRIX.md)

Traces high-value rules distributed across root governance, specifications, existing Skills, the earlier agent-governance refinement, and the rich B2 learning/ownership package. It classifies each reusable rule as global ownership, operation-Skill application, deliberate reinforcement, partial promotion, or package-local specialization.

Groups 3–7 used this matrix as a mandatory migration input so proven rules were not silently weakened, lost, or generalized beyond their responsibility.

### Group 1 — Core Router + Operating Guide Boundary

[`01_CORE_ROUTER_AND_OPERATING_GUIDE_PLAN.md`](01_CORE_ROUTER_AND_OPERATING_GUIDE_PLAN.md)

Refined root routing, `OPERATING_GUIDE.md` boundaries, deliberate reinforcement policy, security/trust disposition, and durable governance indexes.

### Group 2 — Learning by Doing

[`02_LEARNING_BY_DOING_MODE_PLAN.md`](02_LEARNING_BY_DOING_MODE_PLAN.md)

Preserved Learning-by-Doing as UpgradePilot's default working philosophy and added the reusable composition Skill.

### Group 3 — Audit / Review

[`03_AUDIT_REVIEW_MODE_PLAN.md`](03_AUDIT_REVIEW_MODE_PLAN.md)

Refined the repository-audit Skill into the standard critical-review procedure, including `JUST-*`, producer → integration → consumer analysis, cross-owner consistency, and proportional audit records.

### Group 4 — Planning / Design

[`04_PLANNING_DESIGN_MODE_PLAN.md`](04_PLANNING_DESIGN_MODE_PLAN.md)

Added one proportional Planning/Design Skill covering no-plan, compact-plan, consequential-plan, and staged-plan-family cases without turning plans into specifications/ADRs or silently authorizing implementation.

### Group 5 — Build / Implement

[`05_BUILD_IMPLEMENT_MODE_PLAN.md`](05_BUILD_IMPLEMENT_MODE_PLAN.md)

Added the authorized implementation procedure, source/test preflight, `JUST-*` application, source/naming clarity, narrow-to-broad validation, Learning-by-Doing composition, and handoff discipline.

### Group 6 — Learning Only

[`06_LEARNING_ONLY_MODE_PLAN.md`](06_LEARNING_ONLY_MODE_PLAN.md)

Added the explicit no-product-mutation Learning-Only procedure and integrated it with existing package-local contracts, plans, depth maps, and `LEARNING_MEMORY.md`, using the B2 mastery package as the primary compatibility case.

### Group 7 — Governance Consistency + Validation + Cleanup

[`07_GOVERNANCE_CONSISTENCY_VALIDATION_AND_CLEANUP_PLAN.md`](07_GOVERNANCE_CONSISTENCY_VALIDATION_AND_CLEANUP_PLAN.md)

Owns deterministic governance-doctor improvements, cross-operation behavioral cases, cross-owner semantic audit, lifecycle/index cleanup, final security disposition, final branch validation, and merge readiness.

---

## Dependency order

The executed dependency order was:

```text
Group 1 — Core Router + Operating Guide Boundary
→ Group 2 — Learning by Doing
→ EXISTING-RULE TRACEABILITY GATE
   00_RULE_OWNERSHIP_PROMOTION_AND_REINFORCEMENT_MATRIX.md
→ Group 3 — Audit / Review
→ Group 4 — Planning / Design
→ Group 5 — Build / Implement
→ Group 6 — Learning Only
→ Group 7 — Consistency / Validation / Cleanup
```

This is redesign-plan dependency/provenance, not live project-position authority. `../../MEMORY.md` remains the sole live project-continuation owner.

Each group was audited against its detailed plan and the applicable traceability-matrix rule IDs, implemented as a bounded change, and validated before the next group relied on it.

## Implemented design conclusions on this branch

The branch implementation now embodies these redesign conclusions:

1. recurring operation families are Agent Skills/procedures rather than new product specifications;
2. `OPERATING_GUIDE.md` remains the substantial owner of everyday Learning-by-Doing principles;
3. Learning-by-Doing is normally an overlay/default philosophy, not a mutually exclusive competitor to Audit/Planning/Build;
4. Learning-Only is a distinct action boundary where product mutation is paused;
5. critical rules may be deliberately reinforced across execution surfaces when one canonical semantic owner remains explicit;
6. Source Clarity uses compact global outcomes plus detailed Build/Audit application instead of the former universal 22-rule checklist;
7. `SECURITY.md` remains as a compact distinct owner for secrets/private data, untrusted evidence, unknown-code/external-action, credential, and transport boundaries;
8. deterministic tooling checks objective relationships, while semantic cross-owner consistency remains an Audit responsibility;
9. rich package-local rules are promoted globally only when their responsibility is genuinely cross-project; package-specific routes, evidence vocabularies, technology depth, and Career overlays remain local unless independently justified.

These conclusions control only where the corresponding changed owner/Skill exists in the checked-out revision. This plan-family index is provenance, not a substitute for those owners.

## Implementation discipline retained for future maintenance

Future governance maintenance should preserve the lessons from this redesign:

- modify only the responsibility actually changing and directly required reference/validation surfaces;
- consult canonical owners before removing, compressing, or relocating an existing rule family;
- preserve deliberate reinforcement when repeated failures or material risk still justify it;
- do not create broken Skill/owner references;
- run focused deterministic and semantic validation after material governance changes;
- update the relevant durable owner when a conclusion changes rather than accumulating dated competing contracts;
- stop before merge/external publication when that action has not been separately authorized.

The full planning set remains as redesign provenance and a reviewable record of why the final operating model took this shape.
