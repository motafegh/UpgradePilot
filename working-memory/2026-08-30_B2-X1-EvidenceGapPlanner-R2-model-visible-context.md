# B2/X1 EvidenceGapPlanner R2 — Model-Visible Context

**Date:** 2026-08-30  
**Status:** ACTIVE R2 WORKING MEMORY — field-level design complete; synthesis/projection proof next  
**Plan:** `../plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**Responsibility:** decide and justify the exact trusted context projected into the `EvidenceGapPlanner` model request without serializing whole product state, starving the model of discriminating evidence, or transferring deterministic authority.

## 1. R2 governing rule

For every candidate model-visible field ask:

```text
what reasoning does this enable?
is that reasoning part of EvidenceGapPlanner responsibility?
is the fact already trusted before the model?
is the same meaning represented better elsewhere?
does it add discriminating context or only duplicate trace/authority metadata?
what remains deterministic even if the model sees it?
```

Do not equate:

```text
important product state
=
model-visible state
```

and do not equate:

```text
safe bounded context
=
label-only context
```

## 2. Current evidence-refined model observation

```text
EvidenceGapPlannerContext

planning_question

dependency_transition
    normalized_package
    old_version
    proposed_version

propositions
    key
    state
    evidence_coverage
    evidence_owner
    bounded detail

planning_evidence
    EvidenceGapPlanningEvidence[]

consumed_actions
    action_id[]

planning_budget
    remaining_investigations

allowed_actions
    EvidenceGapActionDescriptor[]
        action_id
        purpose
        target_proposition
        evidence_yield

output_schema / structured-output contract
```

Trusted but model-hidden by default:

```text
repository
pull_number
immutable revision
exact action locators
exact action preconditions
mutation policy
exact result-family/class contract
provider/executor retry policy
full execution/audit trace
raw source/provider objects
oracle/evaluator metadata
```

## 3. Decided slices

### Planning question

One concise project-owned bounded question is model-visible.

It owns the uncertainty being advanced, not repository identity, evidence recap, expected action/disposition, or oracle hints.

Future question formulation may become a separate LLM/agent responsibility only when question selection itself becomes materially non-trivial.

Detailed owner: `2026-08-30_B2-X1-EvidenceGapPlanner-R2-planning-question.md`.

### Dependency transition

Pass:

```text
normalized_package
old_version
proposed_version
```

Use canonical normalized identity rather than source presentation spelling.

### Target/case identity

Keep repository / PR / immutable revision hidden from the current model observation. They remain trusted for acquisition, trace, binding, freshness, admission and replay.

### Proposition projection

Pass:

```text
key
state
evidence_coverage
evidence_owner
detail
```

Do not add experiment-only `origin` or `raw_external_text` to the base first-seam contract.

Detailed owner: `2026-08-30_B2-X1-EvidenceGapPlanner-R2-proposition-projection.md`.

### `EvidenceGapPlanningEvidence`

Propositions are the decision-state spine, not the whole reasoning input.

Use selected structured question-relevant evidence when mechanism/witness/limitation/reason/unresolved-condition detail can change which investigation is useful.

```text
Level 1 = proposition state
Level 2 = selected EvidenceGapPlanningEvidence
Level 3 = raw evidence

current model observation = Level 1 + selected Level 2
Level 3 stays outside by default
```

Examples may include bounded CI consumption/direct-exercise distinctions, reachability paths, environment conditions, target-Python interpretation, grounded upstream mechanism facts, structured change scope, and deterministically interpreted command semantics.

### Consumed-action history

Use:

```text
consumed_actions: [action_id]
```

Consumed means an admitted bounded investigation produced a trusted typed result/problem for the bounded state.

Admission rejection, pre-execution staleness and transient provider failures are not automatically consumed investigations.

Findings update propositions/planning evidence. Transport retries remain deterministic provider/executor policy.

Detailed owner: `2026-08-30_B2-X1-EvidenceGapPlanner-R2-action-history-and-retry-boundary.md`.

### Planning budget

Use:

```text
planning_budget:
    remaining_investigations: int
```

Spend one unit when fresh-admitted bounded execution actually begins.

Internal deterministic provider retries do not spend extra semantic investigation units.

Budget spend and consumed history are different dimensions:

```text
execution begins
→ budget spent

trusted typed result/problem
→ action consumed
```

Future time/cost/resource dimensions enter model-visible budget only after real competing actions, real bounds and trustworthy measurements make them decision-relevant.

Detailed owner: `2026-08-30_B2-X1-EvidenceGapPlanner-R2-planning-budget-envelope.md`.

### Allowed action descriptor

Use working planner-facing type:

```text
EvidenceGapActionDescriptor
    action_id
    purpose
    target_proposition
    evidence_yield
```

The planner sees enough to understand **which evidence gap the action advances and what useful evidence it can produce**.

Keep hidden:

```text
repository / revision / path
required proposition state/coverage
mutation_class
exact result_families / Python class names
current cost_class
provider/executor metadata
```

Deterministic catalog/admission owns current admissibility and exact execution binding.

`evidence_yield` is semantic planning vocabulary; exact result-class contract remains deterministic.

`cost_class` stays system-side until real multi-action resource trade-offs exist. Later prefer an earned `resource_profile` over blindly promoting the historical enum.

Keep `action_id` rather than generic `capability_id` because the current catalog entry is a pre-bound action instance.

Detailed owner: `2026-08-30_B2-X1-EvidenceGapPlanner-R2-capability-descriptor-boundary.md`.

## 4. Raw/default exclusions

Do not pass wholesale merely because UpgradePilot stores them:

- raw changelog/release-note prose;
- full GitHub Actions logs/payloads;
- full workflow YAML;
- whole diffs/source files;
- complete lockfiles/dependency graphs;
- whole nested domain/evidence objects;
- raw command text by default;
- evaluator/oracle/protected-set/grading metadata;
- exact provider/action locator data;
- verbose policy strings whose behavior is structurally enforced.

These are defaults, not permanent bans. A later responsibility may earn bounded raw/near-raw evidence explicitly.

## 5. Framework relationship

R2 remains framework-independent.

During R4:

```text
bounded model observation
→ same semantics in ordinary Python and LangGraph

trusted full action/state objects
→ deterministic control-plane / graph state
```

LangGraph/LangChain learning/comparison is explicitly planned. Framework convenience must not silently broaden model authority or erase the R2 projection boundary.

## 6. R2 final synthesis/projection proof — ACTIVE NEXT

Field-level design is sufficiently complete.

Next work:

1. create one final **field / trusted owner / model visibility / planning role / hidden authority** table;
2. construct representative evidence-refined request shapes for:
   - S001 action state;
   - a no-tool state;
   - a richer `EvidenceGapPlanningEvidence` state;
   - a consumed-action repeat state;
3. inspect for:
   - stale historical fields (`repository`, `attempted_actions`, `remaining_steps`, raw result families, hard-constraint echoes, etc.);
   - duplicated information;
   - authority leakage;
   - raw evidence leakage;
   - context starvation;
   - evaluator/oracle hints;
4. do not fabricate a multi-action budget-sensitive case merely to satisfy the proof; record that part as deferred until real competing actions exist;
5. reconcile any final contradiction;
6. if the projection passes, mark R2 complete and advance to R3.

## 7. R2 pass condition

Every model-visible field has an explicit planning role and authoritative non-model owner where appropriate. The request is rich enough for bounded evidence-gap reasoning without becoming a whole-state/raw-evidence dump or a label-only selector interface.

## 8. LbD concepts earned through R2

- canonical identity vs presentation spelling;
- full system state vs model observation;
- context engineering / projection;
- proposition state vs supporting planning evidence;
- information compression vs information loss;
- raw evidence vs interpreted evidence;
- action space vs execution authority;
- general capability vs pre-bound action instance;
- semantic evidence yield vs implementation result classes;
- model memory vs trusted consumed-action state;
- semantic retry vs transport retry;
- planning budget vs operational resource policy;
- telemetry before cost-aware optimization;
- framework-independent agent state design.
