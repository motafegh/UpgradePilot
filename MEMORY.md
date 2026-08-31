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
- **Mode:** Learning-by-Doing / Building, with an active bounded ownership/learning re-entry before further implementation.
- **Selected implementation plan:** `plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`.
- **Selected R4 learning-depth companion:** `plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`.
- **Progress:** R0 PASS; R1 COMPLETE; R2 COMPLETE / PASS; R3 COMPLETE / PASS; **R4-A ordinary-Python reference/control ACTIVE**.
- **Completed R4-A increments:** **R4-A1 model boundary/projection/parser**, **R4-A2 deterministic action rebinding/admission**, and **R4-A3 bounded local model request/response seam**, all with focused mocked/runtime proof appropriate to their current boundaries.
- **Latest focused runtime proof:** **36/36 PASS** in the normal UpgradePilot WSL checkout — R4-A1 10/10, R4-A2 13/13, R4-A3 mocked provider/model seam 13/13.
- **Validation repair history:** two R4-A1 projection-test failures were diagnosed as test observation/representation defects and repaired without changing planner/admission source behavior. R4-A3 test-count bookkeeping was also corrected before the final 36/36 record.
- **Live next slice:** **ownership re-entry over the implemented ordinary-Python seam: bounded source walkthrough in runtime responsibility order A1 → A3 → A2.** Do not run the live LM Studio planner smoke until Ali can explain the minimum-complete end-to-end responsibility and the major syntax/control-flow mechanisms needed for that next material decision.
- **After ownership re-entry:** add or verify the smallest experiment-owned **real-flow composition seam** from actual UpgradePilot product outputs into `EvidenceGapPlannerContext`, then run the bounded live R4-A3 LM Studio inference smoke, inspect actual provider/model evidence, close the A3 LbD slice, and decide whether to continue to R4-A4.
- **Real-flow composition rule:** direct construction of A1/A2/A3 boundary objects remains valid for focused unit tests, but live/end-to-end R4 evidence must reuse the normal product flow and established product result types rather than reimplementing package normalization, dependency-transition truth, proposition truth, CI/reachability semantics, or action authority inside `experiments/`.
- **R4 execution rule:** each material slice must coordinate one bounded build target with the learning depth actually needed for that target, preserve deferred-depth re-entry triggers, inspect focused proof, include a proportional ownership/reasoning step, then explicitly continue/deepen/stop.
- **Product runtime integration:** not authorized; planner/framework work remains experiment-owned. A thin experiment-owned adapter that consumes product outputs is not product planner integration.
- **Technical blocker:** no source/test blocker. The current stop is a deliberate learning/ownership gate. Before live inference, the experiment must also be composed with real product outputs so the smoke exercises the actual architecture rather than hand-reconstructed S001 planner facts. Local LM Studio/provider/model freshness becomes material only when that live A3 smoke resumes and must then be checked narrowly.
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

For future live/end-to-end R4 evidence, these boundary objects must be populated from actual product outputs through a thin experiment-owned composition/projection seam. Focused unit tests may still construct them directly to isolate one contract.

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

The latest combined A1+A2+A3 focused run is recorded under R4-A3 below.

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

Ali ran the combined focused family in the normal UpgradePilot WSL checkout. Observed result:

```text
R4-A1 planner boundary
→ 10/10 PASS

R4-A2 deterministic admission
→ 13/13 PASS

R4-A3 mocked model/provider seam
→ 13/13 PASS

combined focused suite
→ 36/36 PASS
→ Ran 36 tests in 0.006s
→ OK
```

This establishes the focused mocked/source boundary behavior for A1+A2+A3. It does **not** establish live LM Studio reachability/current model availability, model semantic quality, capability execution/update, production reliability, general planner superiority, or product/framework adoption value.

### R4-A3 ownership state

The green run exposed a learning/ownership gap: the implemented source currently exceeds Ali's practical ability to explain the end-to-end flow and several syntax/control-flow mechanisms. The active cross-stage re-entry rule therefore pauses live inference and further implementation until a bounded source walkthrough restores the minimum-complete mental model.

Use runtime responsibility order:

```text
A1 `experiments/b2_x1_evidence_gap_planner.py`
→ model-visible state + decision contract

A3 `experiments/b2_x1_evidence_gap_model.py`
→ local provider/model invocation boundary

A2 `experiments/b2_x1_evidence_gap_admission.py`
→ trusted rebinding + execution authorization
```

During this ownership walkthrough, a real architecture refinement was identified: the current R4 boundary/unit tests can legitimately use direct planner fixtures, but the eventual live A3 smoke should not hand-reconstruct product facts. After re-entry, add or verify a thin experiment-owned composition seam from the real S001 product flow into A1 before live inference.

Tests should be learned after each owning mechanism rather than as 36 independent cases.

Detailed owners:

- `working-memory/2026-08-31_B2-X1-EvidenceGapPlanner-R4A3-local-model-request-response.md`
- `working-memory/2026-08-31_B2-X1-R4A3-mocked-proof-and-ownership-reentry.md`

---

## R4 route

### R4-A — ordinary-Python reference/control — ACTIVE

```text
R4-A1 model boundary/types/projection/parser
→ COMPLETE / FOCUSED RUNTIME PASS

R4-A2 deterministic action rebinding/admission
→ COMPLETE / FOCUSED RUNTIME PASS

R4-A3 bounded local model request/response seam
→ IMPLEMENTED / MOCKED FOCUSED PASS
→ LIVE LM STUDIO INFERENCE PENDING OWNERSHIP RE-ENTRY + REAL-FLOW COMPOSITION

real-flow composition seam
→ AFTER OWNERSHIP RE-ENTRY, BEFORE LIVE A3 SMOKE
→ consume normal UpgradePilot outputs
→ project into A1 planner context without duplicating product semantic owners

R4-A4 no-tool/action transition + execution/update + trace/replay seam
→ AFTER A3 OWNERSHIP RE-ENTRY + REAL-FLOW LIVE INFERENCE EVIDENCE/CLOSURE
```

Do not jump directly to A4 or a large orchestration loop. The active responsibility is now understanding and owning the implemented A1→A3→A2 seam well enough to make the next composition/live A3 evidence meaningful.

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

## R4-A3 immediate learning entry

The A3 implementation now exists. Learn it as part of the whole A1→A3→A2 runtime responsibility, not as a detached provider or Python course.

Required practical concepts before live inference:

```text
dataclass / frozen / slots at practical level
basic annotations, X | None, tuple[X, ...], Literal
__post_init__ invariants
explicit projection
JSON Schema vs Python parser
Mapping[str, Any] as an untrusted response view
JSON dumps vs loads
requests Session / POST / timeout at practical level
try/except and typed invocation problems
provider envelope vs model message content
runtime narrowing with isinstance
early-return guards
stable action-ID rebinding
TOCTOU
proposal != authorization
```

Central ownership model to preserve:

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

Do not yet study generic multi-provider abstraction, sophisticated retry libraries, deep prompt-optimization frameworks, requests internals, advanced Python typing internals, async/concurrency, or LangGraph/LangChain implementation mechanics; their recorded triggers have not fired.

---

## Claim limits / stop lines

Current evidence does **not** prove:

- live LM Studio reachability/current model behavior or planner semantic quality for R4-A3;
- real-flow planner composition has been implemented/proven yet;
- capability execution/state update;
- production reliability;
- general adaptive-planner superiority;
- product/framework adoption value;
- compatibility/safety/merge authority;
- learner mastery merely because AI-written source/tests exist or mocked tests pass.

Do not:

- fabricate a second action;
- begin `src/upgradepilot` planner integration merely because the experiment works;
- reimplement product-owned package normalization, dependency-transition truth, proposition truth, evidence semantics, or exact action authority inside `experiments/` merely to create planner input;
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
bounded A1 → A3 → A2 source ownership walkthrough
→ restore minimum-complete mental model and required practical syntax/control-flow understanding
→ add/verify thin experiment-owned real-flow composition from normal UpgradePilot outputs into A1
→ prove that composition without duplicating product semantic owners
→ bounded live R4-A3 LM Studio smoke
→ inspect provider/model evidence + A3 LbD closure
→ explicitly continue/deepen/stop
→ R4-A4 transition/update/trace seam when justified
→ complete ordinary-Python reference/control
→ R4-B LangGraph
→ R4-C LangChain learning slice
→ R4-D comparison
→ R5 bounded replay/development proof + ownership deepening
→ R6 explicit X1 disposition
```