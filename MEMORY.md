# UpgradePilot Current Memory

**Last updated:** 2026-08-30  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Controlling engineering rule

Existing implementation and historical design are evidence to inspect, not authority to preserve unchanged.

```text
real responsibility / proof need / material risk / learning value
→ identify the earliest sufficient owner
→ keep or grow mechanisms that add capability or learning value
→ refine redundant ownership/representation
→ avoid both over-engineering and under-engineering
```

New tools/frameworks are not prohibited merely because plain Python can implement the same behavior. Bounded learning/comparison is justified when attached to a real UpgradePilot responsibility and real baseline. Product adoption remains a separate evidence-backed decision.

---

## Live position

- **Route:** B2/X1 — Product Agentic Investigation / Orchestration Evaluation checkpoint.
- **Mode:** Learning-by-Doing / Building.
- **Selected plan:** `plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`.
- **Progress:** R0 PASS; R1 COMPLETE; R2 field-level context/action-space design complete.
- **Live next slice:** **R2 final synthesis / request-projection proof**.
- **Product runtime integration:** not authorized; planner/framework work remains experiment-owned.
- **Technical blocker:** none.
- **Product-simulation:** prior capability/value research complete; do not launch broad new simulation merely for case count.

Current R2 owners:

- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-model-visible-context.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-planning-question.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-proposition-projection.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-action-history-and-retry-boundary.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-planning-budget-envelope.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-capability-descriptor-boundary.md`

Historical E1–E5/v2/capability-research detail remains in dated records and should not be duplicated here.

---

## Current responsibility vocabulary

### `EvidenceGapPlanner`

> Given one bounded UpgradePilot planning question, trusted proposition state, selected structured planning evidence, trusted consumed-investigation history, a bounded planning budget, and a closed set of currently admitted bounded actions, decide which material evidence gap should be addressed next by selecting one useful action, or explicitly decide why no action should execute now.

### `EvidenceGapDecision`

Untrusted model proposal; never execution authority.

### `EvidenceGapDecisionKind`

```text
ACTION_SELECTED
QUESTION_SETTLED
KNOWN_INVESTIGATION_NOT_ADMITTED
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

R3 will freeze final structured/wire representation.

---

## R2 evidence-refined model observation

Current candidate:

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

### Planning question

One concise project-owned bounded question. It identifies the uncertainty being advanced without duplicating evidence or encoding the expected action/disposition.

Future question-formulation agent work remains separate and activates only when question selection itself becomes materially non-trivial.

### Dependency transition

Model-visible:

```text
normalized_package
old_version
proposed_version
```

Use canonical package identity, not presentation spelling.

### Case identity

Repository / PR / immutable revision remain trusted for trace, acquisition, binding, freshness and replay, but stay outside current model context.

### Proposition projection

Model-visible:

```text
key
state
evidence_coverage
evidence_owner
detail
```

Do not promote experiment-only `origin` / `raw_external_text` into the base first seam.

### `EvidenceGapPlanningEvidence`

Propositions are the state spine, not the full reasoning input.

```text
Level 1 = proposition state
Level 2 = selected EvidenceGapPlanningEvidence
Level 3 = raw evidence

current model context = Level 1 + selected Level 2
Level 3 excluded by default
```

Selected Level-2 evidence may expose bounded mechanism/witness/limitation/unresolved-condition information when it changes planning value.

### Consumed-action history

Use:

```text
consumed_actions: [action_id]
```

Consumed means an admitted bounded investigation produced a trusted typed result/problem for the bounded state.

Admission rejection, pre-execution staleness, and transient provider failures are not automatically consumed investigations.

Findings update propositions/planning evidence. Transport retries remain deterministic provider/executor policy.

### Planning budget

First seam:

```text
planning_budget:
    remaining_investigations: int
```

Spend one unit when fresh-admitted bounded execution actually begins—not when the model proposes or admission merely accepts.

Provider-internal retries do not automatically spend additional semantic investigation units.

```text
execution begins
→ budget spent

trusted typed result/problem
→ action consumed
```

Potential future time/cost/resource dimensions enter model-visible state only after real competing actions, real bounds and trustworthy measurements make them decision-relevant. Collect telemetry before inventing quantitative estimates.

### `EvidenceGapActionDescriptor`

First-seam model-visible action shape:

```text
action_id
purpose
target_proposition
evidence_yield
```

This gives the model enough information to reason about **which evidence gap the action advances and what useful evidence it can produce**.

Keep hidden:

```text
repository / revision / path
required proposition state/coverage
mutation_class
exact result_families / Python class names
current cost_class
provider/executor metadata
```

Deterministic catalog/admission owns current action applicability and exact execution binding.

`evidence_yield` is semantic planning vocabulary; exact result classes stay in the trusted execution/domain contract.

Keep `action_id` rather than generic `capability_id` because the current catalog entry is a pre-bound action instance.

---

## R2 final synthesis/projection proof — immediate continuation

Before implementation:

1. create the final **field / trusted owner / model visibility / planning role / hidden authority** table;
2. build evidence-refined request shapes for:
   - S001 action state;
   - one no-tool state;
   - one richer `EvidenceGapPlanningEvidence` state;
   - one consumed-action repeat state;
3. inspect for:
   - stale historical fields (`repository`, `attempted_actions`, `remaining_steps`, raw result-family echoes, etc.);
   - duplicated information;
   - authority leakage;
   - raw evidence leakage;
   - context starvation;
   - evaluator/oracle hints;
4. do not fabricate a budget-sensitive multi-action case merely to satisfy the proof; defer that proof until real competing actions exist;
5. if the projection passes, close R2 and advance to R3.

---

## R3 next responsibility after R2 PASS

Freeze the smallest `EvidenceGapDecision` + deterministic admission contract.

Current candidate:

```text
decision_kind
action_id | null
explanation
```

R3 must explicitly reconsider historical model echoes such as `target_proposition`, `expected_result_categories`, and `limitations`; do not retain them merely because v2 did.

Exact action binding, preconditions, mutation policy, result families, consumed-history guard, budget, and fresh-state revalidation remain deterministic.

---

## R4 framework/LbD route

Explicitly planned:

```text
R4-A
ordinary-Python reference/control implementation

R4-B
same bounded responsibility implemented with LangGraph

R4-C
smaller LangChain model/tool/agent/middleware learning slice

R4-D
compare real implementations against UpgradePilot responsibilities
```

Learning goals include LangGraph state/StateGraph/nodes/edges/routing, persistence/checkpoints, interrupts/HITL concepts, freshness/revalidation placement, and LangChain model/tool/middleware abstractions.

Framework learning/comparison is authorized. Product framework/dependency adoption remains a later explicit architecture/build decision.

---

## Claim limits / stop lines

Current evidence does **not** prove:

- production reliability;
- general adaptive-planner superiority;
- correct selection across several real actions;
- product/framework adoption value;
- compatibility/safety/merge authority;
- that raw evidence should never enter any future agent;
- that cost/time belong in current model state.

Do not:

- fabricate a second action;
- freeze v3 before a narrow claim and fresh holdouts exist;
- reuse historical v2 protected material as uncontaminated final evidence;
- begin `src/upgradepilot` planner integration merely because the experiment works;
- adopt LangGraph/LangChain merely because they are learned;
- reject them merely because plain Python can implement the flow;
- expose exact action authority/preconditions/result classes merely for model completeness;
- turn consumed history into free-form LLM memory;
- continue product simulation merely for more cases.

---

## Immediate route

```text
R2 final synthesis/projection proof
→ R2 PASS/repair
→ R3 EvidenceGapDecision + deterministic admission
→ R4 plain Python + LangGraph + LangChain learning/comparison
→ R5 bounded replay/development proof
→ R6 explicit X1 disposition
```

Richer multi-action/multi-turn planner work reopens only when multiple independently justified actions naturally coexist and real state/history/budget/resource-dependent choice becomes materially non-trivial for a small deterministic policy.
