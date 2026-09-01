# UpgradePilot Current Memory

**Last updated:** 2026-09-01  
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
- **Mode:** Learning-by-Doing / Building; R4-A ordinary-Python reference/control remains active, with the first live real-flow A3 slice now closed and A4 pre-implementation design next.
- **Selected implementation plan:** `plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`.
- **Selected R4 learning-depth companion:** `plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`.
- **Progress:** R0 PASS; R1 COMPLETE; R2 COMPLETE / PASS; R3 COMPLETE / PASS; **R4-A ordinary-Python reference/control ACTIVE**.
- **Completed R4-A increments:** **R4-A1 model boundary/projection/parser**, **R4-A2 deterministic action rebinding/admission**, **R4-A3 bounded local model request/response seam**, plus the thin experiment-owned **real-product composition seam** required for meaningful live evidence.
- **Latest focused runtime proof:** **40/40 PASS** in the normal UpgradePilot WSL checkout across the current A1/A2/A3/composition focused family.
- **Latest real-flow proof:** public S001 normal product flow successfully produced the expected dependency transition, the current three product-owned Python-support propositions, supported CI-consumption witness evidence, and the current action descriptor without leaking repository/revision/path/command/action authority into the A1 request.
- **Latest live A3 proof:** `gemma-4-e4b-it-ud` received the real composed `EvidenceGapPlannerContext`, returned a technically valid `ACTION_SELECTED` decision for `acquire_exact_target_python_declaration`, gave reasoning aligned with the unresolved target-declaration proposition, and A2 admitted the selected ID against fresh trusted state. The smoke deliberately executed no capability.
- **A3 closure:** the first S001 real-flow A3 request/response slice is **COMPLETE / PASS** for its bounded purpose. This does not establish general planner quality, production reliability, multi-case generality, execution/update correctness, or framework/product adoption value.
- **Live next slice:** **R4-A4 pre-implementation design** — define the smallest ordinary-Python state/transition responsibility for no-tool/action routing, execution result handling, trusted state update, consumed-action/budget update, and trace/replay. Before implementation, revisit the proposition-production/generalization and persistence questions only against this concrete A4 responsibility.
- **Persistence boundary:** do not adopt a database, event-sourcing architecture, generic rule engine, or durable workflow framework merely because those ideas are attractive. The current learning-depth owner defers full workflow persistence/event sourcing until replay/checkpoint needs become durable product responsibilities; an in-memory experiment trace may be sufficient initially.
- **Real-flow composition rule:** direct construction of A1/A2/A3 boundary objects remains valid for focused unit tests, but live/end-to-end R4 evidence must reuse the normal product flow and established product result types rather than reimplementing package normalization, dependency-transition truth, proposition truth, CI/reachability semantics, or action authority inside `experiments/`.
- **R4 execution rule:** each material slice must coordinate one bounded build target with the learning depth actually needed for that target, preserve deferred-depth re-entry triggers, inspect focused proof, include a proportional ownership/reasoning step, then explicitly continue/deepen/stop.
- **Product runtime integration:** not authorized; planner/framework work remains experiment-owned. A thin experiment-owned adapter that consumes product outputs is not product planner integration.
- **Technical blocker:** no source/test/runtime blocker. LM Studio emitted an `outdated gemma4 chat template` compatibility-workaround warning on the successful semantic-extractor and planner calls; current classification is observational/non-blocking and should be reopened only if later behavior/reliability evidence makes it material.
- **Product-simulation:** prior capability/value research complete; do not launch broad new simulation merely for case count.
- **Governance merge note:** Group 9 merge `973387c` changed governance/procedure and governance-evaluation surfaces only; it did not change product source, product tests, or experiment implementation behavior, so ongoing B2/X1 R4 build progress is unaffected.

Current detailed owners:

- `plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-final-request-projection-proof.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R3-decision-semantics.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R3-wire-and-admission-contract.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R4A1-boundary-types-and-projection.md`
- `working-memory/2026-08-31_B2-X1-EvidenceGapPlanner-R4A1-planning-evidence-naming-refinement.md`
- `working-memory/2026-08-31_B2-X1-EvidenceGapPlanner-R4A2-deterministic-action-admission.md`
- `working-memory/2026-08-31_B2-X1-EvidenceGapPlanner-R4A2-focused-runtime-failure-and-test-repair.md`
- `working-memory/2026-08-31_B2-X1-EvidenceGapPlanner-R4A3-local-model-request-response.md`
- `working-memory/2026-08-31_B2-X1-R4A3-mocked-proof-and-ownership-reentry.md`
- `working-memory/2026-09-01_B2-X1-R4-ownership-reentry-and-next-route.md`
- `working-memory/2026-09-01_2055_B2-X1-R4-real-flow-proof-and-live-A3.md`

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

### `BoundInvestigationAction`

Current R4-A experiment type for one exact trusted executable action binding. The model may see a smaller `EvidenceGapActionDescriptor` projection and choose only `action_id`; repository/revision/path, exact preconditions, mutation policy, and result-family contract remain deterministic authority.

### `EvidenceGapAdmissionState`

Latest trusted deterministic state used immediately before selected-action execution. It is deliberately separate from the T1 model-visible `EvidenceGapPlannerContext` so consumed history, budget, source identity, proposition state, and the current catalog can be rechecked at T2.

### `LocalEvidenceGapPlanner`

Current R4-A3 experiment boundary for one bounded local LM Studio/OpenAI-compatible structured-output invocation. It accepts only an `EvidenceGapPlannerContext`, serializes the existing explicit model-visible projection, validates the provider envelope and structured model content, and returns either an untrusted `EvidenceGapDecision` or a typed `EvidenceGapModelInvocationProblem`.

A successful model decision is still not execution authority and still requires the R4-A2 deterministic admission boundary.

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

Current R4-A2 typed admission problem reasons are:

```text
unknown_action
action_consumed
budget_exhausted
action_identity_stale
action_not_allowed_by_policy
action_not_currently_actionable
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

The R4-A1 validation cycle adds one practical cross-stage rule:

```text
red test
→ identify the exact failed proposition
→ distinguish implementation defect vs fixture/setup vs observation/assertion defect vs mental-model defect
→ repair the correct owner
```

The R4-A3 ownership re-entry adds another:

```text
implementation proof green
+
learner cannot accurately explain the mechanism needed for the next material decision
→ pause further implementation/live inference briefly
→ restore the minimum-complete mental model against the real source
→ resume only when the next step is meaningful
```

That re-entry gate was satisfied before the real-flow composition/live A3 proof. Apply the same proportional rule again if A4 implementation begins to outrun the understanding needed for its next material decision.

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

The planner-facing dataclasses are **boundary representations**, not new owners of product semantics. In the normal product flow, package normalization, exact dependency-transition validity, proposition truth, and evidence semantics are established earlier by their owning product components. Local A1 `__post_init__` checks may protect the planner object from obviously malformed direct construction, but they do not replace or redefine those upstream responsibilities.

Live/end-to-end R4 evidence now uses `experiments/b2_x1_evidence_gap_composition.py` to populate these boundary objects from actual `PublicPullRequestInvestigation` outputs. Focused unit tests may still construct them directly to isolate one contract.

### R4-A1 proof status

Static post-write source/test inspection was followed by actual focused execution in the normal UpgradePilot WSL checkout.

The projection-boundary test exposed two test-design defects during validation:

```text
1. substring search treated `witness_path` as if exact hidden key `path` leaked
2. repaired key-set assertion then incorrectly treated `witness_path` value as a mapping key
```

Both were repaired in the test observation model without changing planner source behavior. Current observed A1 result remains:

```text
10/10 PASS
```

The separate structured-evidence test remains the owner of proving the `witness_path` fact survives projection; the boundary test owns exact hidden-key exclusion.

The real S001 composition probe additionally proves that actual product-owned transition/proposition/CI-consumption state reaches the A1 context while hidden source/action authority stays out of the rendered request.

---

## R4-A2 implemented truth

Source:

`experiments/b2_x1_evidence_gap_admission.py`

Focused tests:

`experiments/tests/test_b2_x1_evidence_gap_admission.py`

Current implemented types/boundaries:

```text
BoundInvestigationAction
EvidenceGapAdmissionState
AdmittedInvestigationAction
EvidenceGapAdmissionProblem
EvidenceGapAdmissionResult
build_target_python_declaration_action(...)
project_action_descriptor(...)
admit_selected_investigation_action(...)
```

Core flow:

```text
T1 model decision: ACTION_SELECTED + action_id
→ T2 current bound-action lookup
→ consumed-history guard
→ remaining-investigation guard
→ repository/revision freshness guard
→ read-only policy guard
→ current proposition state/coverage guard
→ exact admitted action OR typed problem
```

The real A1 ID is construction-bound to the exact target proposition, `pyproject.toml`, unresolved/insufficient preconditions, read-only policy, and exact target-declaration result-family contract. The model explanation remains trace-only and cannot redefine hidden authority.

R4-A2 also makes the TOCTOU distinction executable:

```text
valid at planning time T1
!= permanently authorized at execution time T2
```

### R4-A2 learning depth reached

Practical understanding now required:

```text
stable-ID lookup/rebinding
typed admitted-result vs typed problem result
early-return guard flow
Literal reason vocabulary
Python 3.12 `type Alias = A | B` union alias
fresh-state/precondition validation
TOCTOU
proposal != authorization
defense in depth
```

Advanced generic typing, policy/rule engines, async/concurrency, and framework machinery remain deferred behind the learning-depth map triggers.

### R4-A2 proof status

Current observed focused execution in the normal UpgradePilot WSL checkout:

```text
R4-A2 admission tests
→ 13/13 PASS
```

The latest real-flow A3 smoke additionally observed the expected selected action being rebound and admitted against current trusted S001 state without capability execution.

---

## R4-A3 implemented truth

Source:

`experiments/b2_x1_evidence_gap_model.py`

Focused tests:

`experiments/tests/test_b2_x1_evidence_gap_model.py`

Current boundary:

```text
EvidenceGapPlannerContext
→ existing explicit model-visible projection
→ one LM Studio/OpenAI-compatible structured-output request
→ provider envelope validation
→ strict EvidenceGapDecision parser
→ EvidenceGapDecision OR EvidenceGapModelInvocationProblem
```

Current typed invocation-problem reasons:

```text
provider_request_failed
provider_http_error
provider_response_malformed
completion_truncated
structured_output_invalid
```

The implementation uses a loopback `requests.Session` with `trust_env = False`, a bounded 180-second timeout, no automatic retry, strict JSON-Schema structured output, and the already-deployed local model ID `gemma-4-e4b-it-ud`. These are experiment choices; they do not extend product planner/framework adoption authority.

### R4-A3 proof status

Latest combined focused family in the normal UpgradePilot WSL checkout:

```text
A1 + A2 + A3 + real-state composition focused tests
→ 40/40 PASS
→ Ran 40 tests in 0.006s
→ OK
```

Real S001 live smoke:

```text
real public S001 product flow
→ real product-owned transition/propositions/CI evidence
→ composition seam
→ EvidenceGapPlannerContext
→ LocalEvidenceGapPlanner.decide(...)
→ ACTION_SELECTED: acquire_exact_target_python_declaration
→ basic expectation match: True
→ A2 admitted_action
→ capability_executed: False
```

Observed planner call:

```text
model: gemma-4-e4b-it-ud
schema: upgradepilot_evidence_gap_decision_v1
prompt tokens: 695
completion tokens: 419
reasoning tokens: 324
finish_reason: stop
truncated: false
```

The model explanation correctly identified the unresolved exact-target-declaration proposition as the missing evidence needed before the range-intersection proposition can be resolved.

This establishes the first real S001 A3 request/response seam. It does **not** establish general model quality, production reliability, multi-case planner correctness, capability execution/update, or product/framework adoption value.

### R4-A3 ownership state

The bounded ownership re-entry is closed for the material concepts needed to run and interpret this first live slice. The real-flow composition and live A3 evidence now make the next A4 state/transition discussion meaningful.

The current trust path is:

```text
real trusted UpgradePilot product state
→ thin experiment-owned composition/projection
→ EvidenceGapPlannerContext
→ explicitly rendered model observation
→ provider transport
→ untrusted model response
→ strict parse to EvidenceGapDecision
→ no-tool branch OR fresh deterministic admission
```

The next learning step is not more provider syntax. It is the A4 transition/update responsibility: what happens after a no-tool decision or admitted action, how execution/domain results update trusted state, and what trace/replay information is actually needed.

---

## R4 route

### R4-A — ordinary-Python reference/control — ACTIVE

```text
R4-A1 model boundary/types/projection/parser
→ COMPLETE / FOCUSED + REAL-COMPOSITION PROOF PASS

R4-A2 deterministic action rebinding/admission
→ COMPLETE / FOCUSED PASS + REAL LIVE ADMISSION OBSERVED

R4-A3 bounded local model request/response seam
→ COMPLETE / MOCKED FOCUSED + REAL S001 LIVE PASS

real-flow composition seam
→ IMPLEMENTED / FOCUSED + REAL S001 PROOF PASS
→ consumes normal UpgradePilot outputs
→ projects into A1 planner context without duplicating product semantic owners

R4-A4 no-tool/action transition + execution/update + trace/replay seam
→ NEXT: PRE-IMPLEMENTATION DESIGN
→ define smallest state/transition ownership
→ revisit proposition production + persistence only against concrete A4 needs
```

Do not jump directly to a large orchestration loop, database, event-sourcing architecture, LangGraph, or LangChain. First design the smallest ordinary-Python A4 state/transition seam that can serve as the comparison baseline.

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

## R4-A4 immediate learning/design entry

The A3 live gate is closed. The next bounded responsibility is A4, not additional provider study.

Learn/design when materially used:

```text
state machine / transition model
planner state vs execution state
budget decrement timing
consumed-action update timing
immutable-state replacement/update patterns
execution result → domain interpretation → trusted state update
trace/event record design
replay and deterministic comparison
operational failure vs domain/evidence result
```

Two architecture questions must now be considered against that exact responsibility:

```text
1. proposition production/generalization
→ domain owners produce trusted proposition state
→ composition/state layer selects and carries it
→ planner must not become truth owner

2. persistence/durability
→ determine what A4 actually needs for state transition, trace, replay, resume
→ prefer the smallest adequate mechanism
→ in-memory typed state/trace first unless durable product responsibility is demonstrated
```

Full event sourcing/workflow persistence remains deferred until replay/checkpoint requirements become durable product responsibilities. Async/concurrency remains deferred until real parallelism or race/freshness complexity appears.

---

## Claim limits / stop lines

Current evidence does **not** prove:

- general live planner semantic quality beyond the first bounded real S001 slice;
- multi-case proposition/action generality;
- capability execution/state update;
- durable investigation-state persistence requirements or database choice;
- production reliability;
- general adaptive-planner superiority;
- product/framework adoption value;
- compatibility/safety/merge authority;
- learner mastery merely because AI-written source/tests exist or one live result matched expectation.

Do not:

- fabricate a second action;
- begin `src/upgradepilot` planner integration merely because the experiment works;
- reimplement product-owned package normalization, dependency-transition truth, proposition truth, evidence semantics, or exact action authority inside `experiments/` merely to create planner input;
- adopt a database/event-sourcing/rule-engine architecture before A4 demonstrates the requirement;
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
A1/A2/A3 ownership re-entry → COMPLETE
→ real-product composition seam → IMPLEMENTED / PROVEN
→ bounded live R4-A3 LM Studio smoke → PASS / A3 FIRST REAL SLICE CLOSED
→ A4 pre-implementation state/transition design
→ revisit proposition-production + persistence questions against concrete A4 responsibility
→ implement/prove smallest no-tool/action execution/update/trace seam
→ complete ordinary-Python reference/control when coherent
→ R4-B LangGraph
→ R4-C LangChain learning slice
→ R4-D comparison
→ R5 bounded replay/development proof + ownership deepening
→ R6 explicit X1 disposition
```
