# B2/X1 R4-B — LangGraph Learning-by-Doing Entry

**Date:** 2026-09-02 / consolidated 2026-09-03  
**Mode:** Learning-by-Doing / Planning-Design leading into Build  
**Stage:** R4-B LangGraph implementation/comparison  
**State:** RESEARCH CONSOLIDATED / DESIGN-LEARNING ACTIVE / GRAPH NOT YET FROZEN  
**Product runtime integration:** not authorized

## 1. Continuity and evidence horizon

This record continues from:

`working-memory/2026-09-02_B2-X1-R4A4-runtime-lbd-and-reconciliation-closure.md`

The ordinary-Python R4-A reference/control is accepted as a coherent comparison baseline at its bounded scope:

```text
A1 model-visible projection / decision contract
→ A3 local-model request/response
→ A2 fresh deterministic rebinding/admission
→ A4 execution / domain interpretation / immutable state transition / trace / replay
```

Established proof carried into R4-B:

```text
A1 10/10 PASS
A2 13/13 PASS
A3 13/13 PASS
A4 7/7 PASS
combined A1+A2+A3+composition+A4 47/47 PASS
real S001 A3 selection/admission PASS
real S001 A4 execution/update/trace/replay PASS
post-action A4 Learning-by-Doing ownership closure PASS
```

This remains the semantic comparison anchor. It does not establish production reliability, broad planner quality, multi-action generality, product-runtime integration, or framework adoption value.

## 2. R4-B evidence added after entry

R4-B did not move directly from framework orientation into code. The current design horizon now includes:

```text
1. initial LangGraph mechanics orientation
2. coherent ordinary-Python R4-A control
3. current LangGraph/LangChain research + design proposal
4. post-research LbD discussion of architecture, authority, replay, growth fitness, and scope
5. evidence-refined bounded R4-B execution/comparison plan
6. refined R4 learning-depth / re-entry map
```

Research/design proposal:

`proposals/2026-09-02_B2_X1_R4B_LANGGRAPH_RESEARCH_AND_DESIGN_PROPOSAL.md`

New bounded execution/design owner:

`plans/B2_X1_R4B_LANGGRAPH_LBD_IMPLEMENTATION_AND_COMPARISON_PLAN.md`

The proposal remains non-controlling evidence. The bounded plan promotes only the findings judged useful enough to guide R4-B execution.

## 3. Selected R4-B success question

Use:

> Can the smallest semantically faithful LangGraph orchestration preserve all proven R4-A authority/state/replay semantics while providing enough control-flow clarity, inspectability, and credible growth fitness for UpgradePilot's expected investigation-system expansion to justify the framework's additional machinery?

Evaluate separately:

```text
PRESERVATION
→ are UpgradePilot-owned semantics and authority unchanged/provably equivalent?

VALUE
→ does LangGraph add enough clarity, inspectability, test/debug leverage, or growth fitness to pay for its dependency/plumbing/conceptual cost?
```

A graph that compiles/runs is not sufficient evidence.

## 4. Framework/domain conclusions now established for design

### LangGraph is orchestration, not a new domain owner

```text
UpgradePilot-owned
→ EvidenceGapPlannerContext
→ EvidenceGapDecision semantics
→ A2 fresh deterministic authority
→ EvidenceGapInvestigationState
→ semantic-result / operational-failure meaning
→ budget / action-consumption rules
→ EvidenceGapTransitionTrace
→ pure semantic replay

LangGraph-owned mechanism
→ workflow state carrier
→ nodes
→ edges / conditional routing
→ runtime context
→ compile/invoke execution
→ optional framework tracing/checkpoint machinery if ever separately justified
```

### Workflow state must not become domain truth

A future `EvidenceGapWorkflowState` should wrap/reuse existing typed UpgradePilot objects rather than duplicate canonical fields such as budget, consumed actions, or support assessment into graph-owned copies.

```text
LangGraph workflow state
!= EvidenceGapInvestigationState
```

The first is an orchestration envelope. The second remains trusted evolving investigation/domain state.

### Runtime resources are separate from evolving workflow facts

Current design direction is to keep run-scoped resources such as the planner/model dependency and `GitHubRepositoryClient` in LangGraph runtime context rather than shared graph state, subject to the exact API/design used by the first implementation.

### Graph-private/internal state is not the A1 security boundary

A1 remains the explicit model-observation projection. Framework internal/private channels or output filtering must not be treated as proof that hidden execution authority is unavailable to the model.

## 5. Authority and routing conclusions

### Planner branch

After A3 returns a valid parsed `EvidenceGapDecision`, routing is deterministic:

```text
ACTION_SELECTED
→ A2 admission

no-action decision
→ A4 no-action transition
```

Do not ask another LLM to decide the mechanical consequence of an already-established decision contract.

### Admission branch

A2 remains the actual authorization owner:

```text
AdmittedInvestigationAction
→ execution may proceed

EvidenceGapAdmissionProblem
→ execution must not begin
```

A conditional edge may route based on that result, but routing does not authorize.

### Freshness invariant

The T2 admission state must be established/read **after A3 produces its proposal**.

Do not:

```text
precompute EvidenceGapAdmissionState at T1
→ wait for model
→ later call the old value fresh
```

The graph design must preserve the real T1 → A3 → T2 time/authority boundary.

### Admission rejection

Admission rejection is an expected typed terminal workflow outcome, not an A4 transition and not automatically a framework exception:

```text
no repository execution
budget unchanged
consumed actions unchanged
domain assessment unchanged
```

This reinforces:

```text
workflow progress
!= trusted domain transition
```

## 6. A4 and replay conclusions

The research and LbD discussion currently support keeping A4 cohesive in the first baseline:

```text
freshly admitted action OR no-action decision
→ A4
→ execute if applicable
→ classify semantic result vs operational failure
→ apply correct budget/consumption/domain semantics
→ EvidenceGapTransitionTrace
→ END
```

Do not create a graph-level semantic-result vs operational-failure branch merely because the outcomes differ internally. Both currently end the bounded turn; no distinct next workflow responsibility exists yet.

Reopen A4 splitting only when real evidence creates a different downstream route, retry/resume boundary, effect-isolation requirement, or observability need that pays for the extra intermediate state/plumbing.

### Semantic replay remains UpgradePilot-owned

```text
replay_evidence_gap_transition(trace)
→ deterministic reconstruction from recorded semantic evidence
→ no model call
→ no GitHub call
```

LangGraph checkpoint/history/time-travel replay is a different operational mechanism and may re-execute downstream work. It must not replace `EvidenceGapTransitionTrace` or semantic replay proof.

## 7. Current leading graph candidate — not yet frozen

Current leading candidate is the minimal orchestration graph:

```text
existing trusted UpgradePilot evidence/state
        ↓
A1 explicit bounded projection — candidate outside graph
        ↓
START
        ↓
A3 model node
        ↓
planner-result router
├── model invocation problem → END
├── no-action → A4 transition → END
└── ACTION_SELECTED → A2 fresh-admission node
                         ↓
                    admission router
                    ├── admission problem → END
                    └── admitted → A4 transition → END
```

This is preferred over:

```text
one giant node calling the whole existing Python flow
→ too shallow to evaluate graph orchestration

mechanical one-node-per-helper/A-number rewrite
→ framework-shaped ceremony

duplicating A1/A2/A4 semantics inside LangGraph-specific implementations
→ two semantic sources of truth

splitting A4 before a real routing/operational need
→ extra intermediate invalid states/plumbing without current value
```

A1 placement remains a real design choice until the decision-critical learning is complete.

## 8. Near-future growth fitness criterion

R4-B should not be judged only on today's deliberately simple one-action path. UpgradePilot already has credible future pressure toward more investigation actions/evidence families and may later justify bounded multi-step/re-planning behavior.

Therefore R4-B comparison should ask whether the chosen graph has a clean extension path for **real future admitted growth**.

This does **not** authorize:

```text
fabricated second action
automatic multi-turn loop
parallel execution
subgraphs
checkpoint persistence
```

Growth fitness is an evaluation criterion, not an implementation target.

## 9. Explicitly deferred framework surface

Remain deferred until the triggers recorded in the bounded plan / learning map are met:

```text
checkpointing / persistence / time travel
interrupts / HITL
automatic retry / framework error-handler policy
custom reducers
Command routing
ToolNode
create_agent
subgraphs
parallelism / Send
automatic multi-turn / graph back-edge
persistent Store / cross-thread memory
advanced streaming
LangSmith as required correctness proof
product-runtime integration
```

Important specific reasons:

- retries can silently redefine attempt/budget/idempotency semantics;
- ToolNode/model-to-tool execution can obscure or bypass A2 if treated as authorization;
- `create_agent` would consume the higher-level LangChain comparison before R4-C;
- checkpoint replay is not semantic replay;
- parallel/multi-turn behavior has no currently admitted product responsibility.

## 10. Refined proof direction

The first LangGraph proof must hold model/external nondeterminism constant and compare UpgradePilot-owned semantics.

Required bounded scenario family:

```text
A3 invocation/structured-output problem
three no-action decision kinds
ACTION_SELECTED + A2 rejection
admitted + valid semantic result
admitted + typed target problem
admitted + operational acquisition/provider failure
pure semantic replay
```

When applicable compare:

```text
plain-Python final EvidenceGapInvestigationState
==
LangGraph final EvidenceGapInvestigationState

replay_evidence_gap_transition(graph_transition_trace)
== graph_transition_trace.after_state
```

Also prove call boundaries:

```text
no A2 on no-action
no repository call after A3 problem
no repository call after A2 rejection
exactly one expected repository call on admitted first action
zero model/repository calls during semantic replay
```

Semantic equivalence does **not** require identical internal LangGraph traces/super-steps/framework metadata.

After controlled equivalence is green, run one bounded real S001 LangGraph smoke comparable to the ordinary-Python reference.

## 11. Current decision gates before Build

The bounded plan now narrows the remaining design work to:

```text
D1 A1 placement
   outside graph vs explicit projection node

D2 exact workflow-state/input/internal/output shape

D3 exact T2 freshness mechanism used by A2 after A3 output

D4 exact runtime-context resources

D5 routing representation
   conditional edges preferred unless Command later proves more cohesive

D6 A4 cohesion
   cohesive by default; split only on demonstrated pressure

D7 naming
   EvidenceGapWorkflowState currently preferred to avoid collision with EvidenceGapInvestigationState
```

Do not open additional speculative architecture questions unless evidence creates them.

## 12. Immediate Learning-by-Doing continuation

Do **not** implement LangGraph yet.

Use the refined learning-depth map and bounded plan in this order:

```text
1. workflow state vs trusted domain state
2. partial state updates + runtime context
3. input/internal/output schema distinction if material to state design
4. expected typed outcome vs exception
5. T1 → A3 → fresh T2 admission placement
6. semantic replay vs checkpoint/time-travel replay
7. jointly resolve D1–D7
8. record the material architecture decision here
9. hand off to Build/Implement for dependency/source/test preflight
10. implement smallest experiment-owned graph
11. controlled semantic-equivalence proof
12. real S001 smoke
13. compare present value + near-future growth fitness
```

Required ownership before Build is proportional: Ali should be able to explain what LangGraph is adding structurally, what remains UpgradePilot-owned, why T2 freshness cannot be precomputed, why workflow state is not domain truth, and why semantic replay remains separate from framework replay/checkpoint machinery.

**Skill provenance:** `UP-SKILL:upgradepilot-learning-by-doing`; `UP-SKILL:upgradepilot-planning-design`.
