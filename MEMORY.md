# UpgradePilot Current Memory

**Last updated:** 2026-08-31  
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
- **Selected implementation plan:** `plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`.
- **Selected R4 learning-depth companion:** `plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`.
- **Progress:** R0 PASS; R1 COMPLETE; R2 COMPLETE / PASS; R3 COMPLETE / PASS; **R4-A ordinary-Python reference/control ACTIVE**.
- **Completed R4-A increment:** **R4-A1 — evidence-refined boundary types, explicit request projection, decision schema/parser, and focused tests landed.**
- **Latest refinement:** R4-A1 active evidence types renamed from `EvidenceGapPlanningEvidence` / `EvidenceGapPlanningEvidenceFact` to **`PlanningEvidence` / `PlanningEvidenceFact`** for clearer local source vocabulary; behavior/wire shape unchanged.
- **Live next slice:** **R4-A2 — fresh deterministic action rebinding/admission against trusted hidden action state.**
- **R4 execution rule:** each material slice must coordinate one bounded build target with the learning depth actually needed for that target, preserve deferred-depth re-entry triggers, inspect focused proof, include a proportional ownership/reasoning step, then explicitly continue/deepen/stop.
- **Product runtime integration:** not authorized; planner/framework work remains experiment-owned.
- **Technical blocker:** no design blocker. Focused R4-A1 runtime test execution remains pending because no GitHub workflow run appeared for the original test commit and the assistant execution environment could not resolve GitHub for a temporary clone.
- **Product-simulation:** prior capability/value research complete; do not launch broad new simulation merely for case count.

Current detailed owners:

- `plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-final-request-projection-proof.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R3-decision-semantics.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R3-wire-and-admission-contract.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R4A1-boundary-types-and-projection.md`
- `working-memory/2026-08-31_B2-X1-EvidenceGapPlanner-R4A1-planning-evidence-naming-refinement.md`

Historical R2/E1–E5/v2/capability-research records remain provenance and are not mass-rewritten solely for newer vocabulary.

---

## Current responsibility vocabulary

### `EvidenceGapPlanner`

> Given one bounded UpgradePilot planning question, trusted proposition state, selected structured planning evidence, trusted consumed-investigation history, a bounded planning budget, and a closed set of currently admitted bounded actions, decide which material evidence gap should be addressed next by selecting one useful action, or explicitly decide why no action should execute now.

### `EvidenceGapDecision`

Untrusted structured model decision; never execution authority.

### `EvidenceGapDecisionKind`

```text
ACTION_SELECTED
QUESTION_SETTLED
KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

### No-tool state

A valid planner turn where no investigation action should execute now:

```text
QUESTION_SETTLED
→ bounded question sufficiently settled

KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY
→ useful investigation known but outside current planner action/support boundary

NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
→ question remains non-final but no useful currently offered or specific outside-boundary investigation is identified
```

No-tool is not planner failure, does not imply zero budget, and does not mean UpgradePilot globally has no capabilities.

### `PlanningEvidence`

Current R4-A experiment type for selected structured evidence supplied to `EvidenceGapPlannerContext.planning_evidence` when mechanism/witness/limitation detail can change investigation value.

```text
PlanningEvidence
    evidence_kind
    summary
    facts: PlanningEvidenceFact[]

PlanningEvidenceFact
    name
    value
```

The former design labels `EvidenceGapPlanningEvidence` / `EvidenceGapPlanningEvidenceFact` remain only in historical R2 records where useful as provenance.

---

## Frozen R2 model observation, with active R4 naming

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
    detail

planning_evidence
    PlanningEvidence[]

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

output_schema / provider structured-output contract
```

Trusted but model-hidden by default:

```text
repository
pull_number
immutable revision
raw Level-3 evidence
exact action locators
exact action preconditions
mutation policy
exact result-family/class contract
provider/executor retry policy
full execution/audit trace
oracle/evaluator metadata
```

Consumed actions must not be offered in the current `allowed_actions` model projection. Deterministic admission still retains repeat protection as defense-in-depth against stale/concurrent state.

---

## Frozen R3 model output + admission responsibility

Model wire shape:

```text
EvidenceGapDecision
    decision_kind
    action_id | null
    explanation
```

Parser invariants:

```text
ACTION_SELECTED
→ action_id must be non-null

all no-tool kinds
→ action_id must be null

all kinds
→ explanation must be non-empty trimmed text
```

Historical model echoes are removed:

```text
target_proposition
expected_result_categories
limitations
```

For selected actions deterministic code must freshly re-check:

```text
action ID still known/currently offered
action not consumed
planning budget still permits execution
current proposition/evidence preconditions still hold
mutation/policy boundary still permits action
exact locator/arguments remain trusted and bound
state/action remain fresh immediately before execution
```

Candidate typed admission problem responsibilities:

```text
invalid_decision_shape
unknown_action
action_consumed
budget_exhausted
action_not_currently_actionable
action_not_allowed_by_policy
```

Zero planning budget is an orchestration/resource gate, not a model decision kind.

---

## R4 Learning-by-Doing execution contract

The selected implementation plan and R4 learning-depth companion are meant to be followed together.

For each material R4 slice, keep these aligned:

```text
BUILD TARGET
→ one smallest real implementation responsibility

LEARNING TARGET
→ code/syntax/concepts actually carrying that responsibility
→ required depth now

DEFERRED DEPTH
→ deeper/adjacent concepts intentionally postponed
→ explicit re-entry trigger

PROOF TARGET
→ focused source/test/runtime evidence
→ explicit stronger non-claim

OWNERSHIP POINT
→ proportional Ali prediction/explanation/challenge/selection/testing/diagnosis

AFTER EVIDENCE
→ continue
OR briefly deepen/repair a concept
OR repeat/practise a central mechanism
OR stop at the responsibility/proof boundary
```

Learning depth may increase later when real implementation, testing, debugging, comparison, or framework adoption makes deeper mechanics decision-relevant. Do not treat an earlier shallow/practical explanation as a permanent ceiling, and do not pre-study deeper mechanics without a trigger.

---

## R4-A1 implemented truth

Source:

`experiments/b2_x1_evidence_gap_planner.py`

Focused tests:

`experiments/tests/test_b2_x1_evidence_gap_planner.py`

Current implemented types/boundaries:

```text
EvidenceGapDependencyTransition
PlanningEvidenceFact
PlanningEvidence
EvidenceGapActionDescriptor
EvidenceGapPlanningBudget
EvidenceGapPlannerContext
EvidenceGapDecision
EVIDENCE_GAP_DECISION_JSON_SCHEMA
render_evidence_gap_planner_request(...)
evidence_gap_decision_from_mapping(...)
```

`render_evidence_gap_planner_request(...)` uses explicit field-by-field projection rather than wholesale dataclass/object serialization. A new trusted internal field therefore does not automatically become model-visible.

Current `PlanningEvidence` representation is experiment-owned, not a frozen product specification. It keeps bounded JSON-like fact values sufficient for current states/witness paths without admitting arbitrary nested source/provider objects.

### R4-A1 commits

```text
initial source
0ecbaf7d818ebf4ed5d1bf89a3ba17edf6892375

initial tests
c2c40e2cb77289cbf9c0c296281d78a689611a94

naming refinement source
b7cbda1be6e0f74cc806f88f5d054e82a361ba47

naming refinement tests
6e956005575c2e5cd133b5f52ac642a287ca2d1a

initial R4-A1 working memory
2cf9d1fc843042eac0aa8b317bde8cec3faa412a

naming refinement working memory
da81149234c98a0825d9283ae4e9fcd775e64396
```

### R4-A1 proof status

Static post-write source/test inspection has been performed. Focused tests exist for projection/exclusion, Level-2 witness evidence, context coherence, three-field decision parsing, and no-tool/action-ID invariants.

However:

```text
focused runtime test PASS
→ NOT YET ESTABLISHED
```

The naming refinement itself changes names/imports only; it does not add behavioral proof.

---

## R4 route

### R4-A — ordinary-Python reference/control — ACTIVE

```text
R4-A1 model boundary/types/projection/parser
→ COMPLETE (runtime validation pending)

R4-A1 naming refinement
→ COMPLETE

R4-A2 deterministic action rebinding/admission
→ NEXT

R4-A3 bounded local model request/response seam
→ AFTER A2 focused proof

R4-A4 no-tool/action transition + execution/update + trace/replay seam
→ AFTER A3
```

R4-A2 learning focus:

```text
stable-ID lookup/rebinding
typed admission result/problem
early-return guard flow
fresh-state/precondition validation
TOCTOU
proposal != authorization
defense in depth
```

Do not jump directly to a large orchestration loop.

### R4-B — LangGraph

Implement the same bounded responsibility for real comparison/LbD using State/StateGraph, planner node, deterministic admission/revalidation node or guard, execution node, state-update node, and conditional routing where those concepts map naturally.

Use the ordinary-Python seam as the learning/comparison anchor. Learn basic StateGraph/node/edge concepts on entry; deepen checkpointing, interrupts/HITL, reducers, streaming, tracing, or failure routing only when materially used.

### R4-C — LangChain

Bounded model/tool/agent/middleware learning slice and comparison with the lower-level controlled seam, after lower-level responsibilities are understood well enough to judge what the abstraction helps or obscures.

### R4-D — compare

Compare plain Python / LangGraph / relevant LangChain use on responsibility clarity, state transitions, authority preservation, context projection, freshness placement, replay/checkpoint value, failure/retry ownership, testability/debuggability, overhead, learning value, extensibility, and provider integration friction.

R4-D/R5 are also ownership-deepening stages for repeated concepts through real comparison, testing, replay, debugging, and evidence interpretation.

Framework learning/comparison is authorized. Product framework/dependency adoption remains a later explicit architecture/build decision.

---

## Claim limits / stop lines

Current evidence does **not** prove:

- R4-A1 focused tests pass at runtime;
- model/provider behavior;
- deterministic admission implementation correctness;
- capability execution/state update;
- production reliability;
- general adaptive-planner superiority;
- product/framework adoption value;
- compatibility/safety/merge authority;
- learner mastery merely because AI-written source/tests exist.

Do not:

- fabricate a second action;
- begin `src/upgradepilot` planner integration merely because the experiment works;
- adopt LangGraph/LangChain merely because they are learned;
- reject them merely because plain Python can implement the flow;
- expose hidden action authority fields merely for model completeness;
- turn consumed history into free-form LLM memory;
- reuse historical v2 protected material as uncontaminated final evidence;
- continue product simulation merely for more cases;
- let implementation materially outrun the understanding needed for the next engineering decision;
- turn every incidental syntax feature into a prerequisite course;
- forget deferred concepts by leaving them without re-entry triggers.

---

## Immediate route

```text
R4-A2 deterministic action rebinding/admission
→ focused proof + LbD closure
→ R4-A3 bounded local model request/response seam
→ R4-A4 transition/update/trace seam
→ complete ordinary-Python reference/control
→ R4-B LangGraph
→ R4-C LangChain learning slice
→ R4-D comparison
→ R5 bounded replay/development proof + ownership deepening
→ R6 explicit X1 disposition
```