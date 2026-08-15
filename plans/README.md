# Project-Local Plans

This directory is the canonical home for bounded UpgradePilot execution plans.

The project charter owns stable product scope. The route owns stage sequence/gates. `MEMORY.md` alone selects the live position and bounded plan.

For repository-wide durable knowledge ownership and decision-promotion rules, see [`../docs/README.md`](../docs/README.md).

## Plan responsibility

A plan owns:

- one authorized responsibility or investigation question;
- execution sequence;
- entry prerequisites/evidence;
- allowed modification boundary;
- proof obligations;
- pass/stop conditions;
- prohibited scope.

A plan does **not** normally own:

- stable product mission/boundary;
- live project position;
- framework-independent product invariants or accepted product-decision semantics;
- durable architecture/method decisions already owned by an ADR;
- actual implemented behavior.

Those responsibilities belong to their normal owners.

## Position-neutral rule

A plan must not state which stage/increment is currently active, passed, pending, blocked, or next; the latest commit/test result; an immediate blocker/handoff; or the exact live continuation.

Those facts belong only in `../MEMORY.md`. A plan may cite dated evidence as entry context without turning it into present status.

## Reference, do not re-specify

When a specification or ADR already owns a rule, the plan should normally state the execution consequence and link the owner rather than reproduce the full decision.

Preferred pattern:

```text
accepted requirement/method owner
→ execution consequence for this bounded responsibility
→ sequence
→ proof
→ stop line
```

Avoid:

```text
plan
→ recopies the whole specification/ADR
→ later drifts from the owner
```

A plan may repeat the minimum detail required to execute safely or unambiguously, but that repetition is a working summary, not a new source of authority.

If a plan and its linked specification/ADR differ inside the latter's responsibility, fix the plan or surface the conflict; do not treat the plan as an implicit supersession.

For the B2 reasoning responsibility, accepted candidate/applicability/investigation/stopping semantics are owned by [`../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md). Dated A/B/C working-memory and audits remain rationale/provenance, not the normal semantic owner.

## Source-layout hints

A plan may name expected files as bounded modification hints, but it does not permanently own directory hierarchy.

When a selected older plan names stale paths:

1. compare them with accepted structural ADRs and active source;
2. update the selected plan when needed for unambiguous execution;
3. preserve the responsibility/proof/stop line unless separately changed;
4. do not recreate deleted compatibility paths merely to satisfy an old filename;
5. do not mass-rewrite unselected historical plans solely for vocabulary/path consistency.

Root `../AGENTS.md` owns repository-wide artifact routing. ADR-0007 owns the responsibility-based Python source/product-test/experiment/tool structure.

## When a plan is justified

Create or update one when work:

- begins a new authorized responsibility;
- requires several coordinated steps/files/tests/decisions;
- is likely to span conversations;
- needs an explicit pass condition, stop line, or comparison method;
- could materially change accepted behavior, architecture, dependencies, or evidence.

Do not create another plan for:

- a small explanation/clarification;
- a minor reversible edit already covered by the selected plan;
- one localized check/diagnosis inside an understood responsibility;
- work whose sequence/gate is already defined adequately;
- speculative work that has not been admitted.

## Plans versus proposals, specifications, ADRs, and experiments

- `proposals/` → substantial unadmitted ideas and non-controlling horizons.
- `docs/specifications/` → accepted framework-independent behavior/invariants and product-decision semantics.
- `docs/architecture/` → accepted consequential methods/structures.
- `plans/` → admitted bounded execution/investigation coordination.
- `experiments/` → executable non-product research/evaluation machinery.
- source/tests → actual implemented product behavior.

A proposal may inform a plan but is not authorization. A plan may execute an ADR but does not become architecture. An experiment plan under `plans/` is not executable experiment code.

## B2 architecture-reconciliation plan family

The following files have related names but different responsibilities and lifecycle states.

### Current reusable B2 reasoning responsibility

[`B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md)

Owns the bounded technical-impact → applicability → investigation/feedback → architecture-pressure → synthesis-handoff responsibility. It contains an explicit gate to reconcile shared architecture when a second real mechanism/source consumer exposes demonstrated overlap or proof-strength ambiguity.

### Cross-responsibility architecture checkpoint

[`B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md`](B2_CROSS_RESPONSIBILITY_ARCHITECTURE_RECONCILIATION_PLAN.md)

Owns the bounded design/inspection checkpoint for the currently exposed cross-responsibility seams, including:

```text
GitHub Actions workflow structure
static definition vs runtime execution evidence
CI-specific vs Target-specific interpretation
shared installation/configuration observation
multiple-job structural preservation
heterogeneous impact orchestration
dependency direction / ADR disposition
```

This plan does not pre-authorize source refactoring; it must first produce an evidence-backed architecture decision and implementation handoff.

### Completed historical source-topology reconciliation

[`B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md`](B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md) is **COMPLETED / HISTORICAL PRECEDENT**, not the plan for the new cross-responsibility checkpoint.

Its accepted result was the August 4 transition from the earlier flat/transition-era package into responsibility-based subpackages and true shared primitives. Final behavior validation is recorded in [`../working-memory/2026-08-04_B2-source-structure-reconciliation-final-acceptance.md`](../working-memory/2026-08-04_B2-source-structure-reconciliation-final-acceptance.md), and the durable source-ownership decision is ADR-0007.

Use that completed plan for historical rationale and proven reconciliation principles such as:

```text
share a primitive only when its meaning is genuinely identical across callers
```

Do **not** reactivate its old migration map or Step-7 handoff as the answer to the newer CI/Target/workflow/orchestration question.

## Organization

Create plan subdirectories only when real volume/responsibility justifies them. Do not pre-create empty `implementation/`, `experiments/`, `debugging/`, or `completed/` hierarchies merely for appearance.

Git history and dated evidence preserve plan history. Completed plans may remain in `plans/` when they continue to provide useful execution provenance or architectural precedent, but their completed/historical status must be unambiguous from plan navigation and accepted evidence.

## Plan standard

Use the smallest plan that makes execution unambiguous. A consequential plan should normally identify:

- responsibility and bounded user-visible/evaluation outcome;
- applicable specifications and accepted decisions by reference;
- entry evidence/prerequisites;
- unresolved decisions that genuinely block execution;
- allowed modification/responsibility boundary;
- execution sequence;
- proof/tests;
- pass condition and stop line;
- prohibited scope;
- maintenance/reassessment conditions when material.

Do not add sections merely to satisfy a template. If one compact plan can own the work, reuse/update it rather than creating an overlapping plan.

`MEMORY.md` selects the plan and states the exact live action.