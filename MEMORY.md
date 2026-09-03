# UpgradePilot Current Memory

**Last updated:** 2026-09-03  
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
- **Selected R4-B bounded plan:** `plans/B2_X1_R4B_LANGGRAPH_LBD_IMPLEMENTATION_AND_COMPARISON_PLAN.md`.
- **Selected R4 learning-depth companion:** `plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`.
- **Progress:** R0 PASS; R1 COMPLETE; R2 COMPLETE/PASS; R3 COMPLETE/PASS; **R4-A ordinary-Python reference/control COMPLETE; R4-B LangGraph research/design consolidated and decision-critical Learning-by-Doing ACTIVE; graph design not yet frozen**.
- **R4-A baseline disposition:** the ordinary-Python A1 → A3 → A2 → A4 seam is coherent enough to serve as the comparison control. This is a comparison-baseline decision, not product/framework adoption.
- **Completed/proven R4-A responsibility:** R4-A1 model boundary/projection/parser; R4-A2 deterministic rebinding/admission; R4-A3 local-model request/response; real-product composition seam; first live real S001 A3 selection/admission; bounded A4 execution/update/trace/replay; post-action Learning-by-Doing ownership closure.
- **Latest focused runtime family:** **47/47 PASS** for A1+A2+A3+composition+A4 in the normal UpgradePilot WSL checkout; the dedicated A4 family is **7/7 PASS**.
- **Latest live S001 evidence:** `ACTION_SELECTED` → `acquire_exact_target_python_declaration` → A2 `admitted_action` → A4 exact `pyproject.toml` read at head `aa2dc024d33f61cdef50bf1973ab5adf0a974f5a` → `requires-python = ">=3.10"` → applicability `unresolved → established_not_applicable`; budget `1 → 0`; action consumed; replay equivalent.
- **A4 runtime validation:** **PASS** for the bounded ordinary-Python transition seam. The first live diagnostic initially completed the semantic transition but failed only while serializing nested `packaging.version.Version` values; `default=str` currently remains acceptable for this disposable diagnostic boundary because typed replay equivalence is checked before rendering. Reopen only if JSON becomes a durable/machine-consumed contract, broad stringification hides a defect, or canonical serialized comparison becomes part of proof.
- **R4-B design consolidation:** current LangGraph/LangChain research proposal has been reviewed; accepted findings are promoted into the bounded R4-B plan and refined learning-depth map. The leading candidate is a minimal A3 → A2 → A4 LangGraph orchestration with A1 outside the graph, but A1 placement and the exact workflow-state/context/input-output design remain deliberately unresolved until the next LbD design closure.
- **R4-B non-negotiables:** preserve fresh T2 A2 admission after A3 proposal; keep `EvidenceGapInvestigationState` as canonical trusted domain state; wrap/reuse existing typed objects rather than duplicate graph-owned domain truth; keep `EvidenceGapTransitionTrace` + pure replay as semantic proof; framework tracing/checkpoint/time-travel is a different responsibility.
- **Live next slice:** decision-critical R4-B Learning-by-Doing: workflow state vs domain truth → partial state updates/runtime context → input/internal/output schema distinction as needed → expected outcome vs exception → T1/A3/T2 freshness → semantic replay vs framework replay; then jointly resolve the remaining graph design gates before Build. No LangGraph source implementation has started yet. Do not begin an automatic multi-turn loop.
- **Product runtime integration:** not authorized. New planner/orchestration work remains under `experiments/` through the R4 reference/framework-comparison period.
- **Post-experiment direction:** after plain-Python/LangGraph/LangChain experiment/comparison, perform a separate product-integration pass and move/refactor only responsibilities that earned adoption into `src/upgradepilot/`; do not blindly copy experiment scaffolding.
- **Persistence boundary:** in-memory typed state/trace is sufficient for the current experiment. No database/event-sourcing/checkpoint framework until a durable responsibility demonstrates the need.
- **Product-simulation:** prior capability/value research remains sufficient for current R4 design pressure; do not expand merely for case count.
- **Technical observation:** LM Studio previously emitted an `outdated gemma4 chat template` compatibility-workaround warning on successful calls; currently observational/non-blocking.

Current detailed owners:

- `plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`
- `plans/B2_X1_R4B_LANGGRAPH_LBD_IMPLEMENTATION_AND_COMPARISON_PLAN.md`
- `plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`
- `proposals/2026-09-02_B2_X1_R4B_LANGGRAPH_RESEARCH_AND_DESIGN_PROPOSAL.md` — non-controlling research/design evidence
- `working-memory/2026-09-02_B2-X1-R4B-langgraph-lbd-entry.md` — detailed current R4-B execution/learning owner
- `working-memory/2026-09-02_B2-X1-R4A4-runtime-lbd-and-reconciliation-closure.md`
- R4-A1/A2/A3/A4 working memories remain supporting provenance.

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
→ COMPLETE for the first bounded ordinary-Python baseline responsibility
→ 7/7 dedicated + 47/47 combined focused PASS
→ real S001 execution/update/trace/replay PASS
→ post-action Learning-by-Doing ownership closure PASS
```

**R4-A baseline disposition:** COMPLETE / accepted as a coherent comparison control. This does not select it as the product implementation.

**R4-B LangGraph:** research/design consolidated; decision-critical LbD design remains active and graph design is not yet frozen. R4-C LangChain follows at the bounded abstraction-learning level; R4-D compares implementations. Framework product adoption remains separate.

---

## Claim limits / stop lines

Current evidence does **not** yet prove:

- multi-turn loop correctness;
- general live planner semantic quality beyond the first bounded S001 A3/A4 slice;
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
- begin automatic multi-turn looping;
- adopt/reject LangGraph or LangChain before real comparison evidence;
- let implementation outrun the understanding required for the next material decision.

---

## Immediate route

```text
R4-A ordinary-Python reference/control
→ COMPLETE / coherent comparison baseline

R4-B LangGraph
→ RESEARCH/DESIGN CONSOLIDATED
→ DECISION-CRITICAL LBD ACTIVE
→ GRAPH NOT YET FROZEN

CURRENT BOUNDED PLAN
→ `plans/B2_X1_R4B_LANGGRAPH_LBD_IMPLEMENTATION_AND_COMPARISON_PLAN.md`

NEXT
→ learn workflow state vs trusted domain state
→ learn partial state updates + runtime context
→ learn input/internal/output schema distinction if it affects the graph boundary
→ consolidate expected typed outcome vs exception
→ preserve T1 observation → A3 proposal → fresh T2 A2 admission
→ consolidate UpgradePilot semantic replay vs framework checkpoint/time-travel replay
→ jointly resolve A1 placement, exact workflow state/input/output, T2 freshness mechanism, runtime context, routing representation, A4 cohesion, and naming
→ record the architecture decision in the current R4-B working memory
→ then hand off to Build/Implement for dependency/source/test preflight
→ implement the smallest experiment-owned LangGraph slice
→ controlled semantic-equivalence proof
→ real S001 LangGraph smoke
→ compare present value + credible near-future growth fitness

STOP LINES
→ no automatic multi-turn loop
→ no fabricated second action
→ no ToolNode/create_agent/checkpoint/retry/HITL/subgraph/parallelism machinery without its explicit trigger
→ no product runtime integration
→ no LangGraph/LangChain adoption claim before comparison evidence

LATER
→ R4-C LangChain
→ R4-D comparison
→ R5 replay/development proof
→ R6 explicit X1 disposition
```
