# UpgradePilot Current Memory

**Last updated:** 2026-09-02  
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

Framework learning/comparison is allowed when attached to a real UpgradePilot responsibility. Product adoption remains a separate evidence-backed decision.

---

## Live position

- **Route:** B2/X1 — Product Agentic Investigation / Orchestration Evaluation.
- **Mode:** Learning-by-Doing / Building.
- **Selected implementation plan:** `plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`.
- **Selected R4 learning-depth companion:** `plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`.
- **Progress:** R0 PASS; R1 COMPLETE; R2 COMPLETE/PASS; R3 COMPLETE/PASS; **R4-A ordinary-Python reference/control ACTIVE**.
- **Completed/proven before A4:** R4-A1 model boundary/projection/parser; R4-A2 deterministic rebinding/admission; R4-A3 local-model request/response; real-product composition seam; first live real S001 A3 selection/admission.
- **Latest proven focused runtime family before A4:** **40/40 PASS** for A1+A2+A3+composition in the normal UpgradePilot WSL checkout.
- **Latest live A3 evidence:** real S001 → `ACTION_SELECTED` → `acquire_exact_target_python_declaration` → A2 `admitted_action`; capability execution deliberately stopped before A4.
- **R4-A4 design:** D1–D6 are now resolved sufficiently for the first bounded Build slice.
- **First R4-A4 source slice:** `experiments/b2_x1_evidence_gap_transition.py` implemented.
- **First R4-A4 focused tests:** `experiments/tests/test_b2_x1_evidence_gap_transition.py` added.
- **A4 runtime validation:** **PENDING**. The new source/tests were inspected after commit, but no GitHub commit status/check exists and the focused suite has not yet been executed in the normal UpgradePilot runtime. Do not claim A4 green yet.
- **Live next slice:** run the focused A4 transition tests; repair only evidence-backed failures; then connect the transition seam to the existing real S001 experiment path and execute one admitted S001 transition with trace/replay inspection.
- **Product runtime integration:** not authorized. New planner/orchestration work remains under `experiments/` through the R4 reference/framework-comparison period.
- **Post-experiment direction:** after plain-Python/LangGraph/LangChain experiment/comparison, perform a separate product-integration pass and move/refactor only responsibilities that earned adoption into `src/upgradepilot/`; do not blindly copy experiment scaffolding.
- **Persistence boundary:** in-memory typed state/trace is sufficient for the current experiment. No database/event-sourcing/checkpoint framework until a durable responsibility demonstrates the need.
- **Product-simulation:** prior capability/value research remains sufficient for current R4 design pressure; do not expand merely for case count.
- **Technical observation:** LM Studio previously emitted an `outdated gemma4 chat template` compatibility-workaround warning on successful calls; currently observational/non-blocking.

Current detailed owners:

- `plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`
- `plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`
- `working-memory/2026-09-01_B2-X1-R4A4-pre-implementation-design-and-lbd-entry.md`
- `working-memory/2026-09-01_2055_B2-X1-R4-real-flow-proof-and-live-A3.md`
- R4-A1/A2/A3 working memories remain supporting provenance.

Historical R2/E1–E5/v2/capability-research records remain provenance and are not mass-rewritten solely for newer vocabulary.

---

## Current responsibility vocabulary

### `EvidenceGapPlanner`

> Given one bounded UpgradePilot planning question, trusted proposition state, selected structured planning evidence, trusted consumed-investigation history, a bounded planning budget, and a closed set of currently admitted bounded actions, select one useful investigation action or explicitly decide why no action should execute now.

### `EvidenceGapDecision`

Untrusted structured model decision; never execution authority.

### `EvidenceGapDecisionKind`

```text
ACTION_SELECTED
QUESTION_SETTLED
KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

### No-action decision

Current umbrella vocabulary for the three valid planner outcomes where no investigation action executes:

```text
QUESTION_SETTLED
KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

`no-action decision` is descriptive vocabulary, not a fifth decision kind. Current R4 source/tests/active design use this term instead of generic `no-tool`; historical records may retain older wording.

### `PlanningEvidence`

Selected structured model-visible evidence whose bounded facts may change investigation value. Raw source/provider objects remain hidden by default.

### `BoundInvestigationAction`

Exact trusted executable action binding. The model sees only the smaller action descriptor and chooses `action_id`; repository/revision/path, preconditions, mutation policy, and result-family authority remain deterministic.

### `EvidenceGapAdmissionState`

Fresh T2 trusted state used by A2 immediately before execution. Separate from the T1 model-visible planner context.

### `LocalEvidenceGapPlanner`

R4-A3 local LM Studio structured-output boundary returning either `EvidenceGapDecision` or typed invocation problem. A successful decision still requires A2 admission.

### `EvidenceGapInvestigationState`

First R4-A4 experiment-owned evolving state:

```text
python_support_assessment
consumed_actions
remaining_investigations
continuation_status
```

Stable case facts/evidence remain outside the evolving state.

### `EvidenceGapTransitionTrace`

One in-memory immutable transition record containing actual before/after state, planner decision, admitted action when applicable, and either a valid semantic execution result or expected operational failure. No-action transitions contain no fake execution result.

---

## Frozen R2/R3 authority boundary

Model observation remains bounded to:

```text
planning_question
dependency_transition
propositions
planning_evidence
consumed_actions
planning_budget
allowed_actions
output_schema
```

Model-hidden authority includes:

```text
repository / pull number / immutable revision
raw source evidence
exact action locators and preconditions
mutation policy
exact result-family contract
provider/executor retry policy
full execution trace
```

Model wire shape:

```text
EvidenceGapDecision
    decision_kind
    action_id | null
    explanation
```

```text
ACTION_SELECTED
→ action_id required

all no-action kinds
→ action_id must be null
```

Selected actions still require fresh A2 checks for known/current action, consumed history, budget, source identity, proposition/evidence preconditions, and policy.

---

## R4-A4 accepted semantics

### D1 — state

```text
stable CaseContext
→ fixed case/revision facts and evidence

EvidenceGapInvestigationState
→ only evolving trusted values
```

State updates are immutable replacements so before/after remain inspectable.

### D2 — domain result

Do not reduce a completed investigation to an action ID. Preserve the real typed target result and let existing target-relevance/Python-support owners derive the new assessment.

### D3 — consumption and operational failure

```text
valid TargetPythonDeclaration
OR valid TargetPythonDeclarationProblem
→ semantic action consumed
→ budget spent
→ domain assessment updated
```

```text
operational failure before valid target result
→ budget spent
→ action NOT semantically consumed
→ domain assessment unchanged
→ failure recorded in trace
```

`not_found_or_inaccessible` is already converted by the repository owner into valid unavailable-file evidence and therefore becomes a typed target problem, not an operational failure.

### D4 — no-action transitions

All no-action decisions:

```text
no capability execution
→ budget unchanged
→ consumed history unchanged
→ domain assessment unchanged
→ continuation status changes
→ decision/explanation preserved in trace
```

Continuation states:

```text
ACTIVE
SETTLED
OUTSIDE_CURRENT_BOUNDARY
NO_JUSTIFIED_INVESTIGATION
```

The last three are terminal for the current bounded planner loop; only `SETTLED` means the bounded question itself is considered settled. Broader investigation work may remain for the other two.

### D5 — execution seam

First real action stays experiment-owned and directly reuses existing product owners:

```text
AdmittedInvestigationAction
→ GitHubRepositoryClient.get_exact_commit_text_file(...)
→ interpret_target_python_declaration(...)
→ evaluate_target_python_relevance(...)
→ evaluate_python_support_drop_impact(...)
→ next EvidenceGapInvestigationState
```

No generic executor registry is justified by the current one-action seam.

### D6 — trace/replay

Keep actual small immutable before/after states in the trace for now.

Replay means:

```text
recorded before_state
+ recorded decision/result/failure branch
+ same deterministic transition reduction
→ reconstructed after_state
```

Replay must not call LM Studio or GitHub. Re-calling external systems would be re-execution, not deterministic transition replay.

Proof target:

```text
replay(trace) == trace.after_state
```

---

## R4-A implemented route

```text
R4-A1 model boundary/types/projection/parser
→ COMPLETE / 10/10 focused PASS + real composition evidence

R4-A2 deterministic rebinding/admission
→ COMPLETE / 13/13 focused PASS + real S001 admission observed

R4-A3 local model request/response
→ COMPLETE / combined A1+A2+A3+composition 40/40 focused PASS
→ real S001 live selection PASS

R4-A4 transition/update/trace
→ FIRST SOURCE + TEST SLICE IMPLEMENTED
→ source/test inspection complete
→ focused runtime execution PENDING
→ real S001 A4 execution PENDING
```

R4-B LangGraph begins only after the ordinary-Python reference is coherent enough to be a real comparison baseline. R4-C LangChain follows at the bounded abstraction-learning level; R4-D compares implementations. Framework product adoption remains separate.

---

## Claim limits / stop lines

Current evidence does **not** yet prove:

- the new A4 tests pass in the normal runtime;
- real S001 capability execution/state update/trace correctness;
- multi-turn loop correctness;
- general live planner semantic quality beyond the first bounded S001 A3 slice;
- multi-action generality;
- durable persistence/database requirements;
- production reliability;
- general adaptive-planner superiority;
- product/framework adoption value;
- compatibility/safety/merge authority.

Do not:

- fabricate a second action;
- integrate planner/orchestrator code into `src/upgradepilot/` during the experiment phase;
- duplicate product-owned package/dependency/proposition/evidence/action authority in `experiments/`;
- add a generic executor registry before demonstrated multi-action pressure;
- add database/event-sourcing/rule-engine infrastructure before a durable need exists;
- begin automatic multi-turn looping before the first A4 transition is proven and understood;
- adopt/reject LangGraph or LangChain before real comparison evidence;
- let implementation outrun the understanding required for the next material decision.

---

## Immediate route

```text
A1/A2/A3 + real composition/live A3
→ COMPLETE for their bounded first-slice responsibilities

A4 D1–D6 design
→ CLOSED sufficiently for first Build slice

A4 source + focused tests
→ IMPLEMENTED

NEXT
→ execute focused A4 tests in normal UpgradePilot runtime
→ evidence-backed repair if needed
→ connect A4 to real S001 experiment path
→ execute one real admitted S001 action
→ inspect exact before/result/after trace + replay equivalence
→ stop before automatic multi-turn loop unless separately justified
→ then complete ordinary-Python reference/control
→ R4-B LangGraph
→ R4-C LangChain
→ R4-D comparison
→ R5 replay/development proof
→ R6 explicit X1 disposition
```
