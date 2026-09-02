# Governance + Specification Enhancement and Refinement Plans

This directory owns the bounded planning and provenance for refining UpgradePilot's governance/specification operating system.

The work concerns how durable controls are organized, loaded, reinforced, validated, and specialized for recurring operating modes such as audit, planning/design, implementation, learning-by-doing, and learning-only sessions; support/composition workflows such as Working-Memory and Learning-Artifact authoring; the quality/ownership review of the active technical-specification surface; and later behavioral refinements based on real agent usage.

Groups 1–7 were executed sequentially on branch `governance/spec-governance-enhancement-refinement`. After Group 7 reached merge-review readiness and the deterministic doctor later passed locally, Ali explicitly expanded the redesign scope to include a specification-by-specification audit before merge. Group 8 therefore extended the branch review rather than rewriting the history of Groups 1–7. Group 9 was a later behavioral-refinement extension created after a blind agent trial showed that primary governance discovery/routing was strong while some secondary/conditional owner loading was weaker. Group 10 was later designed and implemented on `governance/learning-artifact-skill-2026-09-01`, then admitted to `main` after separate authorization and a real learning-artifact trial.

That is **plan-family lifecycle/provenance**, not live project-position authority. Root `../../AGENTS.md`, the project charter, accepted specifications/ADRs, and other responsibility owners control according to the repository revision actually being used; `../../MEMORY.md` remains the sole live project-continuation owner.

## Responsibility

Plans in this directory coordinate and preserve the rationale for:

- refinement of always-on governance context;
- deliberate reinforcement of critical rules without ambiguous ownership;
- operation-specific Agent Skills and routing;
- support/composition Skills for recurring artifact workflows when justified;
- reduction of unnecessary persistent context and oversized mixed-responsibility sections;
- cross-owner consistency analysis and deterministic governance checks;
- proportionate simplification of security/trust controls;
- migration of existing procedures into better-scoped owners;
- active technical-specification ownership/semantic audit after the operating-model redesign;
- behavioral evaluation of actual agent routing/use;
- low-noise Skill-use provenance and secondary/conditional owner-discovery refinement;
- validation and merge criteria for the resulting governance/specification system.

They preserve the distinction between:

```text
canonical durable owner
→ authoritative semantic rule

operation-specific skill/procedure
→ reusable way to apply the owners for one primary kind of work

support/composition skill
→ reusable artifact/workflow procedure that composes with a primary operation without becoming one

working memory / learning memory
→ continuity and dated state/evidence

source/tests/commands
→ implementation truth and proof appropriate to the claim
```

## Change and merge boundary

A plan does not authorize its own implementation. Groups 1–10 were implemented only after separate user authorization for their bounded work. Group-10 implementation authorization was granted after its planning-only stop point; admitting the resulting Skill to `main` was also a separate explicit decision.

Completing and validating a future refinement plan does **not** automatically authorize merging its branch into `main`. Merge remains a separate explicit user decision when a branch-based workflow is selected.

---

## Planning set

### Master redesign

[`GOVERNANCE_OPERATING_MODEL_REDESIGN_PLAN.md`](GOVERNANCE_OPERATING_MODEL_REDESIGN_PLAN.md)

Defines the original target operating model, redesign principles, migration intent, major decision points, validation philosophy, and merge criteria for Groups 1–7. Later groups are explicit extensions governed by their own evidence and planning history.

### Cross-group audit and dependency map

[`00_GROUP_AUDIT_AND_DEPENDENCY_MAP.md`](00_GROUP_AUDIT_AND_DEPENDENCY_MAP.md)

Audits the governance relationships and defines the original seven redesign groups, canonical-owner/reinforcement model, cross-group dependencies, operation composition, and group acceptance rule.

### Mandatory existing-rule traceability gate

[`00_RULE_OWNERSHIP_PROMOTION_AND_REINFORCEMENT_MATRIX.md`](00_RULE_OWNERSHIP_PROMOTION_AND_REINFORCEMENT_MATRIX.md)

Traces high-value rules distributed across root governance, specifications, existing Skills, the earlier agent-governance refinement, and the rich B2 learning/ownership package. It classifies each reusable rule as global ownership, operation-Skill application, deliberate reinforcement, partial promotion, or package-local specialization.

Groups 3–7 used this matrix as a mandatory migration input so proven rules were not silently weakened, lost, or generalized beyond their responsibility. Group 8 used it as provenance during specification audit. Group 9 preserved the same canonical-owner/reinforcement discipline while improving observability and conditional routing. Group 10 likewise reused the existing learning/depth/evidence doctrine rather than introducing a competing learning taxonomy.

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

Owns deterministic governance-doctor improvements, cross-operation behavioral cases, cross-owner semantic audit, lifecycle/index cleanup, final security disposition, branch validation, and the first merge-readiness review.

### Group 8 — Technical Specification System Audit + Refinement

[`08_TECHNICAL_SPECIFICATION_SYSTEM_AUDIT_AND_REFINEMENT_PLAN.md`](08_TECHNICAL_SPECIFICATION_SYSTEM_AUDIT_AND_REFINEMENT_PLAN.md)

Audits `docs/specifications/README.md` plus all four active specification/engineering-standard owners after the operating-model redesign. It requires an explicit KEEP/MODIFY disposition for each file, corrects only evidence-backed ownership/semantic/terminology defects, and validates Charter → specification → ADR → plan → implementation boundaries.

The supporting audit/disposition matrix is:

[`00_TECHNICAL_SPECIFICATION_AUDIT_AND_DISPOSITION_MATRIX.md`](00_TECHNICAL_SPECIFICATION_AUDIT_AND_DISPOSITION_MATRIX.md)

### Group 9 — Agent Usage Provenance + Dynamic Routing Refinement

[`09_AGENT_USAGE_PROVENANCE_AND_DYNAMIC_ROUTING_REFINEMENT_PLAN.md`](09_AGENT_USAGE_PROVENANCE_AND_DYNAMIC_ROUTING_REFINEMENT_PLAN.md)

Uses blind behavioral-test evidence to refine two practical weaknesses without reopening the whole governance redesign: make actual full-Skill activation more observable through stable low-noise provenance markers, and strengthen re-evaluation/loading of secondary or conditional owners when a material condition appears during execution. It also clarifies mixed Build/Planning routing and extends deterministic/behavioral regression coverage while preserving smallest-sufficient-context discipline.

### Group 10 — Learning-Artifact Authoring Support Skill

Group 10 introduced the admitted `.agents/skills/upgradepilot-learning-artifact/SKILL.md` support procedure and the corresponding `learning/README.md` authoring model. Its detailed planning artifact and implementation trial were developed on branch `governance/learning-artifact-skill-2026-09-01`; the planning file itself was deliberately left in branch/Git history rather than copied to `main` with stale planning-only lifecycle wording.

The admitted capability preserves these boundaries:

```text
current truth / accepted owners first
→ directly relevant working-memory history when useful
→ bounded Audit composition for questionable material
→ real UpgradePilot case/flow as default teaching substrate
→ proportional must-own / operational / lookup / deferred depth
→ smallest complete study artifact
→ no automatic product repair
```

It remains a support/composition Skill, not a sixth primary operation.

---

## Dependency order

The redesign/refinement provenance is now:

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
→ Group 8 — Technical Specification System Audit + Refinement
→ BLIND BEHAVIORAL AGENT TRIAL
   primary routing strong; secondary/conditional owner loading weaker
→ Group 9 — Agent Usage Provenance + Dynamic Routing Refinement
→ Group 10 — Learning-Artifact Authoring Support Skill
→ focused structural/behavioral + real-artifact validation
→ separate explicit admission to main
```

This is plan-family dependency/provenance, not live project-position authority. `../../MEMORY.md` remains the sole live project-continuation owner.

Groups 1–10 remain historical redesign/audit/refinement provenance. They do not select the current product stage or restart completed project work.

## Implemented design conclusions to preserve

Future refinements must preserve these operating-model conclusions unless new evidence justifies an owning change:

1. recurring operation families are Agent Skills/procedures rather than new product specifications;
2. `OPERATING_GUIDE.md` remains the substantial owner of everyday Learning-by-Doing principles;
3. Learning-by-Doing is normally an overlay/default philosophy, not a mutually exclusive competitor to Audit/Planning/Build;
4. Learning-Only is a distinct action boundary where product mutation is paused;
5. critical rules may be deliberately reinforced across execution surfaces when one canonical semantic owner remains explicit;
6. Source Clarity uses compact global outcomes plus detailed conditional Build/Audit application rather than a universal checklist;
7. `SECURITY.md` remains the compact distinct owner for secrets/private data, untrusted evidence, unknown-code/external-action, credential, and transport boundaries;
8. `ENVIRONMENT.md` remains the durable owner of reusable runtime/topology facts and re-check rules rather than being copied into operation Skills;
9. deterministic tooling checks objective relationships, while semantic cross-owner consistency and actual agent behavior remain behavioral/Audit responsibilities;
10. rich package-local rules are promoted globally only when their responsibility is genuinely cross-project;
11. smallest-sufficient-context and responsibility-level Skill inheritance remain important constraints against procedural/context inflation;
12. support/composition Skills may own frequent reusable workflows without being promoted into primary operation modes.

## Implementation discipline retained for future maintenance

Future governance/specification maintenance should preserve the lessons from this redesign and later evidence:

- modify only the responsibility actually changing and directly required reference/validation surfaces;
- consult canonical owners before removing, compressing, or relocating an existing rule family;
- preserve deliberate reinforcement when repeated failures or material risk still justify it;
- keep specification semantics separate from ADR method, plan sequence, Skill procedure, implementation truth, and live state;
- distinguish Skill-use observability from proof of behavioral compliance;
- re-evaluate conditional owners when a material new execution condition appears, but do not re-route on every micro-step;
- keep support/composition Skills outside the primary-operation set unless their responsibility genuinely becomes a primary action mode;
- do not create broken Skill/owner/reference paths;
- run focused deterministic and semantic/behavioral validation after material governance changes;
- update the relevant durable owner when a conclusion changes rather than accumulating dated competing contracts;
- stop before merge/external publication when that action has not been separately authorized.

The full planning set remains redesign/refinement provenance and a reviewable record of why the operating/specification model took its current shape.