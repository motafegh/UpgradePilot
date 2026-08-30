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
- **Progress:** R0 PASS; R1 COMPLETE; R2 COMPLETE / PASS; **R3 COMPLETE / PASS**.
- **Live next stage:** **R4 — build and compare the coherent experiment-owned agent seam**.
- **R4 route:** R4-A ordinary-Python reference/control → R4-B LangGraph implementation → R4-C bounded LangChain learning slice → R4-D comparison.
- **Product runtime integration:** not authorized; planner/framework work remains experiment-owned.
- **Technical blocker:** none.
- **Product-simulation:** prior capability/value research complete; do not launch broad new simulation merely for case count.

Current detailed owners:

- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-model-visible-context.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-final-request-projection-proof.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R3-decision-semantics.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R3-wire-and-admission-contract.md`

Historical E1–E5/v2/capability-research detail remains in dated records and should not be duplicated here.

---

## Current responsibility vocabulary

### `EvidenceGapPlanner`

> Given one bounded UpgradePilot planning question, trusted proposition state, selected structured planning evidence, trusted consumed-investigation history, a bounded planning budget, and a closed set of currently admitted bounded actions, decide which material evidence gap should be addressed next by selecting one useful action, or explicitly decide why no action should execute now.

### `EvidenceGapDecision`

Untrusted structured model decision; never execution authority.

### `EvidenceGapDecisionKind` — R3 frozen semantics

```text
ACTION_SELECTED
QUESTION_SETTLED
KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

The rename from `KNOWN_INVESTIGATION_NOT_ADMITTED` is deliberate: `outside current boundary` describes a useful investigation that is not part of the planner's current action space without implying that deterministic action admission already rejected a concrete proposal.

### No-tool state

A **no-tool state** is a valid planner turn where no investigation action should execute now. It is an umbrella branch, not planner failure:

```text
QUESTION_SETTLED
→ bounded question is sufficiently settled

KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY
→ useful investigation is known but outside this planner's current admitted action/support boundary

NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
→ question remains non-final but no useful currently offered or specific outside-boundary investigation is identified
```

No-tool does not imply zero budget and does not mean UpgradePilot globally has no capabilities.

---

## R2 final model observation — PASS

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

output_schema / structured-output contract
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

R2 final synthesis used real S001 action state, real S004 settled/no-tool state, S001 Level-2 CI reachability/witness evidence, and a consumed-action repeat state.

### Planning budget

```text
planning_budget:
    remaining_investigations: int
```

Spend when fresh-admitted bounded execution actually begins. Provider-internal retries do not automatically spend extra semantic investigation units.

### `EvidenceGapActionDescriptor`

```text
action_id
purpose
target_proposition
evidence_yield
```

The model reasons about what evidence an action can contribute; deterministic code owns whether/how it may execute.

---

## R3 final decision/output contract — PASS

### Model wire shape

```text
EvidenceGapDecision
    decision_kind
    action_id | null
    explanation
```

Fixed three-field shape is preferred for the first seam.

Parser invariants:

```text
ACTION_SELECTED
→ action_id must be non-null

all no-tool kinds
→ action_id must be null

all kinds
→ explanation must be non-empty trimmed text
```

### Historical model echoes removed

Do not include in the new base output:

```text
target_proposition
expected_result_categories
limitations
```

Reasons:

- `action_id` rebinds to the trusted target proposition;
- exact result/problem families remain deterministic and are not model-owned;
- `limitations` overlaps explanation for the current seam and is not trusted evidence.

### Decision-processing layers

```text
JSON Schema
→ field/type shape

parser
→ cross-field semantic shape

no-tool decision
→ no capability execution; semantic correctness remains model/evaluation responsibility

ACTION_SELECTED
→ fresh deterministic action admission
```

### Fresh deterministic admission

For selected actions, re-check:

```text
action ID still known/currently offered
action not consumed
planning budget still permits execution
current proposition/evidence preconditions still hold
mutation/policy boundary still permits action
exact locator/arguments remain trusted and bound
state/action remain fresh immediately before execution
```

The model does not echo any of those authority fields.

Candidate admission problem responsibilities for R4:

```text
invalid_decision_shape
unknown_action
action_consumed
budget_exhausted
action_not_currently_actionable
action_not_allowed_by_policy
```

Do not mechanically retain historical `target_proposition_mismatch` / `expected_result_categories_mismatch`; those existed because the old model output echoed trusted metadata.

### Zero planning budget

`remaining_investigations <= 0` is a deterministic orchestration/resource gate, not a model decision kind. Orchestration should normally avoid an unnecessary planner action-selection call when no investigation can begin.

---

## R4 active route

R4 must use the active Build/LbD procedure before adding implementation/dependencies.

### R4-A — ordinary-Python reference/control

Implement the evidence-refined seam under `experiments/` / `experiments/tests/`:

```text
trusted state/context projection
→ local model request
→ EvidenceGapDecision parsing
→ no-tool handling OR action rebinding/admission
→ bounded execution/update seam as justified
→ deterministic trace/replay
```

This is a reference/control, not a predetermined winner.

### R4-B — LangGraph

Implement the **same responsibility** with LangGraph for real LbD comparison:

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

Learn persistence/checkpoints, interrupts/HITL concepts, freshness placement and graph observability only where they attach to the real flow.

### R4-C — LangChain

Bounded learning/integration slice for model/tool/agent/middleware abstractions and relationship to LangGraph runtime. Do not force custom EvidenceGapPlanner authority boundaries into a generic abstraction if it obscures them.

### R4-D — compare

Compare plain Python / LangGraph / relevant LangChain use on responsibility clarity, state transitions, authority preservation, context projection, freshness placement, replay/checkpoint value, failure/retry ownership, testability/debuggability, overhead, learning value, extensibility and provider integration friction.

Product framework adoption remains a later explicit architecture/build decision.

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
- begin `src/upgradepilot` planner integration merely because the experiment works;
- adopt LangGraph/LangChain merely because they are learned;
- reject them merely because plain Python can implement the flow;
- expose exact action authority/preconditions/result classes merely for model completeness;
- turn consumed history into free-form LLM memory;
- reuse historical v2 protected material as uncontaminated final evidence;
- continue product simulation merely for more cases.

---

## Immediate route

```text
R4-A ordinary-Python reference/control
→ R4-B same seam in LangGraph
→ R4-C bounded LangChain learning slice
→ R4-D comparison
→ R5 bounded replay/development proof
→ R6 explicit X1 disposition
```

Richer multi-action/multi-turn planner work reopens only when multiple independently justified actions naturally coexist and real state/history/budget/resource-dependent choice becomes materially non-trivial for a small deterministic policy.
