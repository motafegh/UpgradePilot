---
name: upgradepilot-planning-design
description: Plan or design bounded UpgradePilot work proportionately by separating stable product semantics, durable architecture, execution coordination, implementation truth, and live state. Use when Ali asks to plan, design, think through architecture, compare implementation approaches, or write/update a bounded implementation or investigation plan.
---

# UpgradePilot Planning and Design

Use this Skill as the reusable procedure for materially planning or designing UpgradePilot work.

This Skill is **procedural and non-controlling**.

Root `AGENTS.md` owns authorization and operation routing. `plans/README.md` owns plan-artifact responsibility. Accepted specifications own stable framework-independent behavior/invariants. ADRs under `docs/architecture/` own accepted consequential implementation/structural methods. `OPERATING_GUIDE.md` owns project-wide Learning-by-Doing, proportionality, rationale/necessity reasoning, and evidence discipline. Active source/tests/commands/outputs establish implemented truth. `MEMORY.md` alone owns live project continuation.

A planning artifact or design conclusion does **not** prove implementation and does **not** authorize Build/Implement unless the user's request separately includes implementation.

## Activation and action boundary

Activate this Skill when the user asks to:

```text
plan this
write/update the implementation plan
design this responsibility
think through the architecture
compare implementation approaches
work out the sequence/proof/stop line before building
use planning/design mode
```

Do not force-load the full procedure for a tiny factual clarification or a trivial already-planned local edit whose execution route is unambiguous.

Planning/design normally means:

```text
inspect owners/evidence
→ reason/compare
→ optionally create/update the smallest justified planning artifact
→ STOP before implementation
```

An explicit request to create/update a plan authorizes only that bounded planning artifact and directly necessary planning references. It does not silently authorize source/test implementation.

If the same user request explicitly includes both planning and implementation, complete enough planning to remove material ambiguity, then hand off to the admitted Build/Implement procedure when available. Do not let this Skill itself become the implementation procedure.

## 1. Establish the exact responsibility and outcome

Start with the smallest complete planning question:

```text
what responsibility/outcome is being planned?
what is explicitly in scope?
what is explicitly out of scope?
what observable result/proof would make the responsibility complete?
what decisions are already owned elsewhere?
```

Do not begin from framework names, folder names, abstractions, or a desired technology. Define the real product/engineering responsibility first.

Load `MEMORY.md` only when live selection/continuation is material. A new plan can be designed without making it the live plan.

## 2. Load only the owners/evidence needed

Use the smallest useful chain:

```text
root authorization/routing
→ exact product/technical owner
→ accepted method owner when one exists
→ relevant existing plan when one exists
→ active source/tests/evidence when current implementation constrains the design question
```

Possible owners include:

- `PROJECT_CHARTER.md` for mission, supported decision, product boundary, evidence/claim doctrine;
- accepted specifications for stable behavior/invariants;
- ADRs for accepted durable method/structure;
- `plans/README.md` and selected/local plan-family rules for plan responsibility;
- active source/tests for implementation truth and migration pressure;
- `MEMORY.md` only for live continuation/selection;
- narrow audit/history/proposal evidence only for a precise unresolved design/provenance question.

Do not reconstruct accepted semantics from working-memory when their canonical specification/ADR already exists.

## 3. Separate already-decided semantics from unresolved design

Before proposing a solution, classify the planning inputs:

```text
ALREADY OWNED PRODUCT REQUIREMENT
what the system must guarantee
→ specification / Charter responsibility

ALREADY OWNED DURABLE METHOD
how a consequential cross-cutting method is already required to work
→ accepted ADR responsibility

CURRENT IMPLEMENTATION FACT
what active source/tests currently do/protect
→ implementation evidence, not automatic design authority

UNRESOLVED DESIGN QUESTION
what method/ownership/sequence/proof still requires a decision
→ Planning/Design work

EXECUTION COORDINATION
how accepted decisions will be implemented/proven/stopped
→ plan responsibility
```

If no real unresolved design question remains, do not manufacture alternatives merely to make planning look thorough.

If a proposed plan conflicts with an accepted specification or ADR inside that owner's responsibility, surface the conflict. Do not let the plan act as implicit supersession.

## 4. Decide how much planning is justified

Use one Skill at proportional depth.

### P0 — no durable plan

Use when:

- the change is tiny/reversible and already owned;
- one bounded diagnostic/check is enough;
- the sequence/proof is already unambiguous under an existing plan;
- only a clarification is needed.

Use a concise in-session action sequence. Do not create a repository artifact merely because planning occurred.

### P1 — compact bounded plan

Use when one responsibility needs several coordinated steps/files/tests, may span a session, or benefits from an explicit proof/pass/stop boundary.

Keep it compact and responsibility-specific.

### P2 — consequential plan

Use when work crosses important modules/owners, contains material design or migration pressure, depends on several proof layers, or wrong sequencing could create significant rework/drift.

Add only what is needed, such as:

- owner map;
- unresolved decisions;
- alternatives/trade-offs;
- dependency/order constraints;
- proof strategy;
- explicit stop/prohibited scope.

### P3 — staged plan family

Use only when several bounded responsibilities have genuinely different owners, gates, dependencies, or proof obligations and combining them into one plan would become ambiguous.

Do not create a plan family because the topic is large, because many files exist, or because multiple phases sound professional.

## 5. Use rationale and necessity correctly

Apply `OPERATING_GUIDE.md` §4.3 whenever the design depends on **why a mechanism is needed**.

For a material proposed or existing mechanism, reason through:

```text
1. proposition / design goal
2. necessity class
3. correct responsibility / owner / layer
4. evidence supporting the rationale
5. credible alternative / trade-off when one exists
```

Useful reasoning labels remain:

- proposition-essential;
- current-implementation requirement;
- defensive/boundary hardening;
- uncertain/audit needed.

Never invent a rationale because the current code contains a mechanism or because a plan would be easier to write if the rationale were assumed.

Current callers/tests/source are important migration/regression evidence. They are not automatic architectural authority.

## 6. Apply retention and end-to-end ownership before designing around legacy mechanisms

When planning refactors/extensions/migrations, apply Core `JUST-001` through `JUST-005` rather than treating current structures as mandatory design inputs.

For a material cross-layer field/check/transformation/metadata propagation, trace proportionately:

```text
exact proposition
→ normal producer
→ integration/composition boundary
→ earliest sufficient owner
→ downstream consumer
→ independently supported later boundary, if any
→ concrete proof/risk/compatibility reason for repetition
```

Then plan from the smallest justified responsibility boundary.

Do not preserve or introduce a mechanism solely because:

- current callers consume it;
- tests assert it;
- an internal function can be called directly;
- fixtures can fabricate inconsistent state;
- historical architecture used it;
- migration would require coordinated edits.

Migration cost matters to execution planning but does not create product necessity.

## 7. Establish the simplest credible baseline first

Apply the Ceremony Tax before adding durable complexity.

For a consequential proposed mechanism, ask:

```text
what capability / risk / obligation requires this?
what evidence makes that need real now?
what is the simplest mechanism that satisfies the responsibility and proof boundary?
what additional cost/maintenance/coordination does the larger option create?
what would justify the extra machinery?
```

Do not pre-create services, frameworks, abstractions, directories, compatibility layers, agent machinery, ADRs, plans, or approval/checklist process merely for possible future scale or generic best practice.

A simpler baseline must still satisfy the complete admitted responsibility. “Simple” is not permission to under-design the actual product boundary.

## 8. Compare alternatives only when a real decision remains

When several credible designs genuinely satisfy the admitted responsibility, compare only the material dimensions:

- correctness/proof fit;
- ownership/cohesion;
- failure/abstention behavior;
- complexity/maintenance;
- migration impact;
- generality pressure;
- testability/observability;
- reversibility;
- dependency/service/operational cost;
- security/privacy/credential implications when material.

Do not ask Ali to choose among unfamiliar names. Under Learning-by-Doing, first establish the minimum mental model needed to understand what each alternative changes.

Avoid fake choice: if one option is ruled out by accepted constraints, explain that rather than presenting it as an equally viable candidate.

If evidence is insufficient to choose, identify the **smallest discriminating investigation** and keep the decision open. Do not convert uncertainty into arbitrary preference.

## 9. Protect minimum useful generality

When the planned responsibility is automated and known fixtures/cases could distort the design, consult `docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`.

The plan should preserve the admitted responsibility across relevant variation rather than hardcoding the next example.

Use real cases as evidence/pressure, not as an excuse to define one rule per known fixture, one handcrafted parser per example, or caller-supplied interpretation that bypasses the responsibility being automated.

Do not broaden generality beyond the accepted product horizon merely for elegance.

## 10. Decide whether specification or ADR work is required

Use responsibility, not ceremony.

### Specification change/update is required when

The planned work changes or introduces an accepted stable framework-independent product invariant/behavior/decision semantic that must guide future implementations.

Do not hide that change only inside a plan.

### ADR creation/update is justified when

A durable consequential implementation/structural method is being selected, such as a material dependency/framework, source/package boundary, representation policy, persistence mechanism, service boundary, trust method, or comparable cross-cutting commitment.

Do not create an ADR for a routine local implementation choice, temporary experiment, exact next action, or detail already adequately owned by an accepted ADR.

### Plan is sufficient when

The stable behavior and consequential method are already decided and the remaining responsibility is bounded execution/investigation coordination, sequence, proof, stop condition, or migration.

## 11. Write/update the smallest adequate plan

When a durable plan is justified or explicitly requested, follow `plans/README.md` and include only applicable material:

```text
responsibility / bounded outcome
scope and exclusions
applicable owner references
entry evidence / prerequisites
unresolved decisions that genuinely block execution
allowed modification boundary
ordered implementation/investigation sequence
validation / proof obligations
pass condition
stop line
prohibited scope
reassessment/activation trigger only when material
```

### Reference, do not re-specify

If a specification/ADR already owns a rule, record only the execution consequence and reference the owner. A concise repeated phrase may be used when necessary for safe/unambiguous execution, but it is not a second semantic owner.

### Position neutrality

A reusable plan must not become the live-state owner. It may define durable activation conditions or its own artifact lifecycle status, but `MEMORY.md` alone selects what is live now.

### Source-layout hints are not architecture ownership

A plan may name expected files/modules as current execution hints. If active source or an accepted structural ADR has moved, reconcile the selected plan rather than recreating obsolete paths merely to satisfy old plan text.

## 12. Learning-by-Doing composition

Planning/design is a first-class Learning-by-Doing surface.

When the Learning-by-Doing overlay is active:

- orient Ali to the real responsibility before discussing implementations;
- explain unfamiliar design alternatives only to the depth needed for the current decision;
- state why the decision is necessary now;
- let Ali reason about ownership, proof, sequence, or trade-offs only after the required premises are established;
- challenge unsupported user/assistant assumptions by evidence;
- use the structured “why needed?” method rather than circular current-code explanations;
- do not infer ownership from Ali merely approving the assistant's preferred design;
- reduce assistance as the same design mechanism repeats across later work.

Use `.agents/skills/upgradepilot-learning-by-doing/SKILL.md` when the full learning/action composition cycle is explicitly invoked or materially useful.

Do not turn planning into a generic architecture course or make Ali manually fill every plan section as a proof of ownership.

## 13. Relationship to Audit / Review

Planning should critically evaluate design assumptions, but it does not need to become a formal audit every time.

Use `.agents/skills/upgradepilot-repository-audit/SKILL.md` when:

- the selected question is materially evaluative of an existing implementation/design;
- a cross-owner inconsistency needs formal classification;
- a retention/ownership question requires an explicit audit trace;
- a durable audit finding may need preservation;
- Ali explicitly asks for audit/review.

An audit finding may inform the plan; it does not by itself authorize the planned implementation.

## 14. Planning output discipline

A useful planning/design result should make the following recoverable without excess ceremony:

```text
what responsibility is being solved
what is already decided and by whom
what remains unresolved
why the selected design/baseline is justified
what alternatives were rejected and why, only when material
which owner/layer should carry each important responsibility
what sequence changes/investigations follow
what evidence will discriminate success
where execution must stop
what is explicitly not being done
```

If the user asked only for design discussion, a chat-level design result may be sufficient. Do not create a plan file unless requested or justified by the durable-plan criteria.

## 15. Completion and stop line

Planning/Design is complete when:

- the responsibility and boundaries are clear;
- applicable stable semantics/method owners are identified;
- material unresolved decisions are resolved or explicitly left open with discriminating evidence needs;
- planning depth is proportional;
- the smallest adequate design is selected or the comparison remains honestly unresolved;
- required specification/ADR work is identified at the correct owner;
- execution sequence/proof/pass/stop/prohibited scope are sufficient when a plan is needed;
- the result does not rely on invented rationale or current implementation inertia;
- the plan/design does not claim implementation proof or live continuation.

Then **stop before implementation** unless the user's request also explicitly authorizes Build/Implement.

## Anti-patterns

Do not:

- create a durable plan for every small task;
- create separate small/medium/large planning Skills;
- treat a detailed plan as implementation authorization;
- copy entire specifications/ADRs into a plan;
- make a plan the live-state owner;
- invent design rationale;
- preserve current code solely because callers/tests depend on it;
- design a downstream repeat without tracing the earlier owner;
- create alternatives when accepted constraints already decide the choice;
- ask Ali to choose unfamiliar technologies before teaching the required mental model;
- create an ADR merely because a plan contains a design choice;
- hide a stable behavior change only in a plan;
- hardcode known fixtures as the design horizon;
- introduce ceremony or durable machinery without a current admitted capability/risk/obligation;
- continue directly into implementation when only planning/design was requested.
