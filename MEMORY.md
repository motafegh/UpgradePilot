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
- **Progress:** R0 PASS; R1 COMPLETE; R2 COMPLETE / PASS; R3 COMPLETE / PASS; **R4-A ordinary-Python reference/control ACTIVE**.
- **Completed R4-A increment:** **R4-A1 — evidence-refined boundary types, explicit request projection, decision schema/parser, and focused tests landed.**
- **Live next slice:** **R4-A2 — fresh deterministic action rebinding/admission against trusted hidden action state.**
- **Product runtime integration:** not authorized; planner/framework work remains experiment-owned.
- **Technical blocker:** no design blocker. Focused R4-A1 runtime test execution remains pending because no GitHub workflow run appeared for the commit and the assistant execution environment could not resolve GitHub for a temporary clone.
- **Product-simulation:** prior capability/value research complete; do not launch broad new simulation merely for case count.

Current detailed owners:

- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-final-request-projection-proof.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R3-decision-semantics.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R3-wire-and-admission-contract.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R4A1-boundary-types-and-projection.md`

Historical E1–E5/v2/capability-research detail remains in dated records and should not be duplicated here.

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

---

## Frozen R2 model observation

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

## R4-A1 implemented truth

New experiment source:

`experiments/b2_x1_evidence_gap_planner.py`

New focused tests:

`experiments/tests/test_b2_x1_evidence_gap_planner.py`

### Implemented types/boundaries

```text
EvidenceGapDependencyTransition
EvidenceGapPlanningEvidenceFact
EvidenceGapPlanningEvidence
EvidenceGapActionDescriptor
EvidenceGapPlanningBudget
EvidenceGapPlannerContext
EvidenceGapDecision
EVIDENCE_GAP_DECISION_JSON_SCHEMA
render_evidence_gap_planner_request(...)
evidence_gap_decision_from_mapping(...)
```

`render_evidence_gap_planner_request(...)` uses **explicit field-by-field projection**, not wholesale dataclass/object serialization. This preserves the model-observation authority boundary when trusted internal types later gain fields.

The first concrete `EvidenceGapPlanningEvidence` representation uses:

```text
evidence_kind
summary
facts[]
    name
    value
```

with bounded JSON-like fact values sufficient for current states/witness paths. It remains experiment representation, not a frozen product specification.

### R4-A1 commits

```text
source
0ecbaf7d818ebf4ed5d1bf89a3ba17edf6892375

tests
c2c40e2cb77289cbf9c0c296281d78a689611a94

working-memory record
2cf9d1fc843042eac0aa8b317bde8cec3faa412a
```

### R4-A1 proof status

Observed after write:

```text
source blob
2bf88bc1cb267c481183ac1bd563df7f24bb73a7

test blob
43d34193929bb9211e633e39b46eb5285df30cbc
```

Focused tests were written for projection/exclusion, Level-2 witness evidence, context coherence, three-field decision parsing, and no-tool/action-ID invariants.

However:

```text
source/test static inspection
→ completed

GitHub CI run for test commit
→ none observed

local project test execution
→ not obtained; temporary clone failed before checkout because the execution environment could not resolve github.com
```

Do not claim focused runtime PASS yet.

---

## R4 route

### R4-A — ordinary-Python reference/control — ACTIVE

Current sequence:

```text
R4-A1 model boundary/types/projection/parser
→ COMPLETE (runtime validation pending)

R4-A2 deterministic action rebinding/admission
→ NEXT

then bounded local model request/response seam
→ then no-tool/action transition + trace/replay as justified
```

Do not jump directly to a large orchestration loop.

### R4-B — LangGraph

Implement the **same bounded responsibility** for real comparison/LbD:

```text
trusted workflow state
→ State/StateGraph
planner
→ planner node
admission/revalidation
→ deterministic node/guard
execution
→ tool/execution node
interpretation/update
→ state-update node
continue/no-tool
→ conditional edges
```

### R4-C — LangChain

Bounded model/tool/agent/middleware learning slice and comparison with the lower-level controlled seam.

### R4-D — compare

Compare plain Python / LangGraph / relevant LangChain use on responsibility clarity, state transitions, authority preservation, context projection, freshness placement, replay/checkpoint value, failure/retry ownership, testability/debuggability, overhead, learning value, extensibility, and provider integration friction.

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
- compatibility/safety/merge authority.

Do not:

- fabricate a second action;
- begin `src/upgradepilot` planner integration merely because the experiment works;
- adopt LangGraph/LangChain merely because they are learned;
- reject them merely because plain Python can implement the flow;
- expose hidden action authority fields merely for model completeness;
- turn consumed history into free-form LLM memory;
- reuse historical v2 protected material as uncontaminated final evidence;
- continue product simulation merely for more cases.

---

## Immediate route

```text
R4-A2 deterministic action rebinding/admission
→ focused proof
→ bounded local model request/response seam
→ complete ordinary-Python reference/control
→ R4-B LangGraph
→ R4-C LangChain learning slice
→ R4-D comparison
→ R5 bounded replay/development proof
→ R6 explicit X1 disposition
```
