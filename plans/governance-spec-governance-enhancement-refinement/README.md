# Governance + Specification Enhancement and Refinement Plans

This directory owns the bounded planning work for refining UpgradePilot's governance/specification operating system without prematurely changing its controlling artifacts.

The work is concerned with how durable controls are organized, loaded, reinforced, validated, and specialized for recurring operating modes such as audit, planning/design, implementation, learning-by-doing, and learning-only sessions.

It does **not** itself redefine project governance. Root `../../AGENTS.md`, the project charter, accepted specifications/ADRs, and other responsibility owners remain controlling until an approved change is actually made to those owners.

## Responsibility

Plans in this directory may coordinate:

- refinement of always-on governance context;
- deliberate reinforcement of critical rules without ambiguous ownership;
- operation-specific Agent Skills and routing;
- reduction of unnecessary persistent context and oversized mixed-responsibility sections;
- cross-owner consistency analysis and deterministic governance checks;
- proportionate simplification of security/trust controls;
- migration of existing procedures into better-scoped owners;
- validation and merge criteria for the resulting governance redesign.

They must preserve the distinction between:

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

## Change boundary

Creating or revising plans in this directory does not authorize the planned governance edits by itself.

A redesign plan should expose unresolved design choices before implementation, prefer migration/refinement over uncontrolled new-file growth, and identify which existing files can be reduced or absorbed when a new scoped procedure is introduced.

---

## Planning set

### Master redesign

[`GOVERNANCE_OPERATING_MODEL_REDESIGN_PLAN.md`](GOVERNANCE_OPERATING_MODEL_REDESIGN_PLAN.md)

Defines the overall target operating model, redesign principles, migration intent, major decision points, validation philosophy, and merge criteria.

### Cross-group audit and dependency map

[`00_GROUP_AUDIT_AND_DEPENDENCY_MAP.md`](00_GROUP_AUDIT_AND_DEPENDENCY_MAP.md)

Audits the present governance relationships and defines the seven redesign groups, canonical-owner/reinforcement model, cross-group dependencies, operation composition, and group acceptance rule.

### Group 1 — Core Router + Operating Guide Boundary

[`01_CORE_ROUTER_AND_OPERATING_GUIDE_PLAN.md`](01_CORE_ROUTER_AND_OPERATING_GUIDE_PLAN.md)

Plans the refinement of root routing, `OPERATING_GUIDE.md` boundaries, deliberate reinforcement policy, security/trust disposition, and cleanup of durable governance indexes.

### Group 2 — Learning by Doing

[`02_LEARNING_BY_DOING_MODE_PLAN.md`](02_LEARNING_BY_DOING_MODE_PLAN.md)

Plans preservation of Learning-by-Doing as UpgradePilot's default working philosophy while adding a reusable/manual Skill that composes with Audit, Planning, Build, Debugging, and other substantive work.

### Group 3 — Audit / Review

[`03_AUDIT_REVIEW_MODE_PLAN.md`](03_AUDIT_REVIEW_MODE_PLAN.md)

Plans refinement of the existing repository-audit Skill into the standard critical-review procedure, including `JUST-*`, producer → integration → consumer analysis, cross-owner consistency, and proportional audit records.

### Group 4 — Planning / Design

[`04_PLANNING_DESIGN_MODE_PLAN.md`](04_PLANNING_DESIGN_MODE_PLAN.md)

Plans one proportional Planning/Design Skill covering no-plan, compact-plan, consequential-plan, and staged-plan-family cases without turning plans into specifications/ADRs or silently authorizing implementation.

### Group 5 — Build / Implement

[`05_BUILD_IMPLEMENT_MODE_PLAN.md`](05_BUILD_IMPLEMENT_MODE_PLAN.md)

Plans the authorized implementation procedure, source/test preflight, `JUST-*` application, source/naming clarity, narrow-to-broad validation, Learning-by-Doing composition, and handoff discipline.

### Group 6 — Learning Only

[`06_LEARNING_ONLY_MODE_PLAN.md`](06_LEARNING_ONLY_MODE_PLAN.md)

Plans the explicit no-product-mutation learning procedure and integration with existing package-local contracts, plans, depth maps, and `LEARNING_MEMORY.md`, using the B2 mastery package as the primary compatibility case.

### Group 7 — Governance Consistency + Validation + Cleanup

[`07_GOVERNANCE_CONSISTENCY_VALIDATION_AND_CLEANUP_PLAN.md`](07_GOVERNANCE_CONSISTENCY_VALIDATION_AND_CLEANUP_PLAN.md)

Plans deterministic governance-doctor improvements, behavioral routing cases, cross-owner semantic audit, lifecycle/index cleanup, security disposition re-check, final branch validation, and merge readiness.

---

## Dependency order

The planned dependency order is:

```text
Group 1 — Core Router + Operating Guide Boundary
→ Group 2 — Learning by Doing
→ Group 3 — Audit / Review
→ Group 4 — Planning / Design
→ Group 5 — Build / Implement
→ Group 6 — Learning Only
→ Group 7 — Consistency / Validation / Cleanup
```

This is an execution dependency encoded by the planning family, not live project-position authority. `../../MEMORY.md` remains the sole live project-continuation owner.

Each group should be audited against its detailed plan, implemented as a bounded change, and validated before the next group is allowed to rely on its result.

## Core design decisions already represented by the planning set

The plans deliberately encode these provisional redesign conclusions for implementation testing:

1. operation families should normally be Agent Skills/procedures rather than new product specifications;
2. `OPERATING_GUIDE.md` should remain a substantial owner of everyday Learning-by-Doing principles;
3. Learning-by-Doing is normally an overlay/default philosophy, not a mutually exclusive competitor to Audit/Planning/Build;
4. Learning-Only is a distinct action boundary where product mutation is paused;
5. critical rules may be deliberately reinforced across execution surfaces when one canonical semantic owner remains explicit;
6. source clarity should first be simplified into compact global outcomes plus detailed Build/Audit application rather than immediately creating another permanent specification;
7. security/trust rules should survive only to the extent their concrete UpgradePilot responsibility remains justified, with the standalone-file decision made after routing is redesigned;
8. deterministic tooling should check objective relationships, while semantic cross-owner consistency remains an Audit responsibility.

These are planning conclusions, not yet controlling changes to the existing governance artifacts.

## Implementation discipline

When implementation begins:

- do not rewrite all governance files at once;
- modify only the group currently being executed and any directly required reference/validation surfaces;
- preserve deliberate reinforcement until its replacement is proven at least as reliable;
- do not create broken intermediate Skill/owner references;
- run focused governance validation after each group;
- record a design change back into the relevant plan if implementation evidence materially invalidates an assumption;
- stop at each group's explicit stop line before progressing.

The full planning set is intended to make the redesign reviewable and reversible before any final merge into `main`.