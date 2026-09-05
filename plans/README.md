# Project-Local Plans

This directory is the canonical home for bounded UpgradePilot execution and investigation plans.

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

## Plan naming

Plan filenames and primary titles follow the accepted Naming Clarity standard in [`../docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md).

Use the complete semantic responsibility as the primary identity:

```text
BOUNDED_EVIDENCE_GAP_PLANNER_IMPLEMENTATION_COMPARISON_AND_EVALUATION_PLAN.md
```

rather than making a reader decode execution history first:

```text
B2_X1_R4B_..._LBD_..._PLAN.md
```

High-level route coordinates may remain as secondary plan metadata when they materially improve navigation. Execution-local stage/step labels remain useful inside a bounded sequence or historical provenance, but should not become the filename/title vocabulary for unrelated artifacts. Prefer full descriptive words over project-local abbreviations when expansion prevents misunderstanding. A longer filename is acceptable when the extra wording materially clarifies responsibility or scope.

Historical plans are not mass-renamed merely to satisfy the current convention. Apply this rule first to newly created plans and selected active plans, then to older active plans when they are materially touched or obstruct comprehension.

## Position-neutral rule

A reusable plan must not claim which stage/increment is currently active, passed, pending, blocked, or next; the latest commit/test result; an immediate blocker/handoff; or the exact live continuation.

Those facts belong only in `../MEMORY.md`. A plan may contain explicit lifecycle/status metadata about **the plan artifact itself** (for example approved, scheduled, completed, historical) when that metadata is part of the plan's durable activation/interpretation contract; it must not replace `MEMORY.md` as the owner of what work is live now.

A plan may cite dated evidence as entry context without turning that evidence into present continuation.

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

## Source-layout hints

A plan may name expected files as bounded modification hints, but it does not permanently own directory hierarchy.

When a selected older plan names stale paths:

1. compare them with accepted structural ADRs and active source;
2. update the selected plan when needed for unambiguous execution;
3. preserve the responsibility/proof/stop line unless separately changed;
4. do not recreate deleted compatibility paths merely to satisfy an old filename;
5. do not mass-rewrite unselected historical plans solely for vocabulary/path consistency.

Root `../AGENTS.md` owns repository-wide artifact routing. Accepted structural ADRs own durable source-layout decisions.

## When a plan is justified

Create or update one when work:

- begins a new authorized responsibility;
- requires several coordinated steps/files/tests/decisions;
- is likely to span conversations;
- needs an explicit pass condition, stop line, comparison method, or activation trigger;
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

## Plan families and local indexes

Create a plan subdirectory only when several plans genuinely share one bounded redesign/program responsibility and a local index reduces ambiguity.

A local plan-family `README.md` may describe:

- each plan's responsibility;
- dependency/order relationships among those plans;
- durable activation or stop conditions;
- historical/completed interpretation when needed to prevent accidental reuse.

It must not claim that a plan is the live continuation unless `MEMORY.md` independently selects it. Do not use the root `plans/README.md` as a changing catalog of whichever project-specific plan family happens to be important at the moment.

Git history and dated evidence preserve plan history. Completed plans may remain in `plans/` when they continue to provide useful execution provenance or architectural precedent, but their historical interpretation must be unambiguous from the plan/family itself or accepted evidence.

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