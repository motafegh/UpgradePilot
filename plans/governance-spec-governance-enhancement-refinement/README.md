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

The initial redesign is defined in [`GOVERNANCE_OPERATING_MODEL_REDESIGN_PLAN.md`](GOVERNANCE_OPERATING_MODEL_REDESIGN_PLAN.md).
