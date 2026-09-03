# B2/X1 R4-B LangGraph Learning-by-Doing Implementation and Comparison Plan

**Status:** AUTHORIZED BOUNDED PLAN ARTIFACT — subordinate to the selected B2/X1 post-research planner plan; position-neutral; `MEMORY.md` alone owns live continuation  
**Date:** 2026-09-03  
**Parent plan:** `B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**Learning-depth owner:** `B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`  
**Research/design evidence:** `../proposals/2026-09-02_B2_X1_R4B_LANGGRAPH_RESEARCH_AND_DESIGN_PROPOSAL.md`  
**Responsibility:** design, learn, implement, prove, and compare the smallest semantically faithful LangGraph orchestration of the already-proven bounded `EvidenceGapPlanner` responsibility without redesigning UpgradePilot domain semantics or pre-building future agent capabilities  
**Product runtime integration:** NOT authorized

---

## 1. Why this bounded R4-B plan now exists

The parent plan correctly authorized a LangGraph comparison once the ordinary-Python R4-A seam became coherent. At R4-B entry, however, exact graph design was intentionally left open so framework structure would not be chosen before the real responsibility and baseline were understood.

That evidence now exists through four complementary inputs:

```text
pre-initial framework impressions
→ coherent ordinary-Python R4-A implementation/control
→ current LangGraph/LangChain research + design proposal
→ post-research Learning-by-Doing discussion and engineering guardrails
```

The result is enough new design evidence to justify a more precise R4-B execution route, but **not** enough to justify framework adoption, product integration, automatic multi-turn planning, fabricated actions, or the larger LangGraph/LangChain feature surface.

This plan prevents two opposite failures:

```text
UNDER-EVALUATION
→ prove only that a StateGraph compiles around today's one-action seam
→ learn little about whether LangGraph is a useful orchestration foundation

FRAMEWORK-DRIVEN OVERBUILD
→ redesign domain semantics or add checkpoints/tools/loops/retries because LangGraph exposes them
```

The experiment must preserve the existing UpgradePilot responsibility and make LangGraph earn any claimed value through evidence.

---

## 2. Owner split and authority

### Overall route / authorization

`B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`

Owns the broader post-research planner route, R4-A/R4-B/R4-C/R4-D ordering, later disposition, and overall stop boundaries.

### This plan

Owns only the bounded R4-B LangGraph sequence:

```text
remaining design-critical learning
→ graph architecture freeze
→ smallest experiment implementation
→ semantic-equivalence proof
→ real S001 graph smoke
→ LangGraph-vs-Python comparison
→ handoff evidence for R4-C/R4-D
```

### Learning depth

`B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`

Owns what Ali should understand now, what should deepen on first material use, and what remains deferred behind explicit triggers.

### Research evidence

`../proposals/2026-09-02_B2_X1_R4B_LANGGRAPH_RESEARCH_AND_DESIGN_PROPOSAL.md`

Is non-controlling evidence. Its recommendations may inform this plan but do not become architecture merely because they were researched.

### Live continuation

`../MEMORY.md` alone owns the exact live stage/action. Dated R4-B working memory preserves detailed execution/learning handoff evidence.

---

## 3. Comparison anchor already established

The ordinary-Python R4-A control provides the semantic baseline:

```text
trusted UpgradePilot product evidence/state
→ A1 bounded model-observation projection
→ A3 local structured model invocation
→ EvidenceGapDecision                    # untrusted proposal
→ A2 fresh deterministic T2 admission
→ AdmittedInvestigationAction            # exact authorization
→ A4 execute / interpret / immutable transition / trace / pure replay
```

The current committed evidence horizon records:

```text
A1 10/10 PASS
A2 13/13 PASS
A3 13/13 PASS
A4 7/7 PASS
combined focused family 47/47 PASS
real S001 A3 selection/admission PASS
real S001 A4 execution/update/trace/replay PASS
A4 post-action LbD ownership closure PASS
```

R4-B must compare against these semantics; it must not silently redefine them to fit framework conventions.

---

## 4. R4-B success question

Use this as the central evaluation question:

> **Can the smallest semantically faithful LangGraph orchestration preserve all proven R4-A authority/state/replay semantics while providing enough control-flow clarity, inspectability, and growth fitness for the investigation-system expansion UpgradePilot already expects to justify the framework's additional machinery?**

Evaluate two independent dimensions:

```text
PRESERVATION
Does LangGraph preserve the UpgradePilot-owned semantics and authority boundaries?

VALUE
Does LangGraph provide enough present clarity/inspectability and credible near-future growth leverage to pay for its dependency, state plumbing, concepts, and failure surface?
```

A graph that runs but weakens semantics fails. A graph that preserves semantics but adds no material value is valid evidence against further LangGraph use for this responsibility.

---

## 5. Non-negotiable semantic invariants

Unless a later accepted semantic/architecture decision explicitly changes them, R4-B must preserve:

```text
EvidenceGapPlannerContext
= explicit bounded model observation

EvidenceGapDecision
= untrusted model proposal, never execution authority

A2 admission
= deterministic authorization against fresh T2 trusted state

T2 freshness
= established/read after A3 has produced its proposal
!= precomputed before A3 and later called fresh

AdmittedInvestigationAction
= exact authorization token into A4

EvidenceGapInvestigationState
= canonical trusted evolving investigation/domain state

LangGraph workflow state
= orchestration carrier, not a second source of domain truth

semantic result
!= operational failure

budget spent
!= action consumed

admission rejection
= no execution and no fabricated A4/domain transition

EvidenceGapTransitionTrace + replay_evidence_gap_transition(...)
= authoritative semantic transition/replay proof

LangGraph trace/checkpoint/time-travel
!= UpgradePilot semantic trace/replay
```

Unexpected programmer/framework exceptions must not be flattened into expected domain/control outcomes merely to use framework error machinery.

---

## 6. Current leading architecture — candidate until design freeze

The evidence currently favors the **minimal orchestration graph**, but implementation must wait until the remaining design questions in §8 are understood and resolved.

Conceptual candidate:

```text
existing trusted UpgradePilot evidence/state
        ↓
A1 bounded projection (UpgradePilot-owned; candidate placement outside graph)
        ↓
START
        ↓
A3 planner/model node
        ↓
planner-result routing
├── EvidenceGapModelInvocationProblem → END
├── no-action decision → A4 transition node → END
└── ACTION_SELECTED → A2 fresh-admission node
                         ↓
                     admission routing
                     ├── EvidenceGapAdmissionProblem → END
                     └── admitted action → A4 transition node → END
```

Current rationale:

- A3 is a meaningful stochastic/external workflow boundary whose typed result controls routing.
- A2 is a meaningful authority boundary and should remain structurally explicit.
- A4 is already a cohesive proven owner; semantic-result vs operational-failure currently has no different downstream destination, so splitting it would add ceremony without present control value.
- A1's durable property is the explicit model-observation projection, not its graph placement. Keeping it outside is currently the smallest candidate; an explicit A1 node remains a credible alternative if its graph-visible observability/learning value justifies the extra state plumbing.

Do not treat this section as implementation freeze. §8 owns the remaining decisions.

---

## 7. State / context philosophy

### 7.1 Wrap existing typed objects; do not flatten domain truth

The graph-specific state should be a small orchestration envelope around existing UpgradePilot values, conceptually:

```text
EvidenceGapWorkflowState
├── planner_context: EvidenceGapPlannerContext
├── investigation_state: EvidenceGapInvestigationState
├── planner_result: EvidenceGapDecision | EvidenceGapModelInvocationProblem | unset
├── admission_result: AdmittedInvestigationAction | EvidenceGapAdmissionProblem | unset
└── transition_trace: EvidenceGapTransitionTrace | unset
```

Exact fields, optionality, input/output schemas, and naming are not frozen by this sketch.

Do **not** duplicate canonical domain fields such as:

```text
remaining budget
consumed actions
Python-support/domain assessment
exact action authority
```

as separate graph-owned truths beside their UpgradePilot owners.

### 7.2 Runtime dependencies are not evolving workflow facts

Run-scoped resources should normally enter through LangGraph runtime context rather than graph state when current framework behavior supports it, including candidates such as:

```text
local model/planner dependency
GitHubRepositoryClient
narrow current-state access/composition capability needed by A2 at T2
```

Do not put provider sessions, clients, raw repository content, prompt templates, or exact hidden execution authority into shared graph state merely because a node needs access to them.

### 7.3 Graph privacy is not model-observation authority

LangGraph internal/private state or output filtering must never replace A1's explicit projection. Model visibility is proved at the A1/A3 request boundary, not inferred from graph-channel names or output schemas.

---

## 8. Remaining design gates before Build

Resolve only these material questions before implementation. Do not manufacture additional alternatives.

### D1 — A1 placement

Choose between:

```text
A1 outside graph
→ smallest graph; preserves current explicit model boundary without extra state plumbing

A1 as explicit graph node
→ stronger graph-level visibility of the projection step, but requires more trusted input inside graph and adds ceremony
```

Current leading candidate: **outside graph**.

### D2 — exact workflow-state / input / output shape

Decide:

- smallest `EvidenceGapWorkflowState` representation;
- which values are graph inputs;
- which intermediate values remain internal;
- what final output is necessary for direct comparison/testing;
- whether an explicit output schema should hide planner/admission intermediates from normal callers while focused tests can inspect them.

### D3 — T2 freshness mechanism

Identify the smallest existing/narrow owner the A2 node will use **after A3 output exists** to establish/read fresh `EvidenceGapAdmissionState`.

Do not invent a general repository/service abstraction merely to satisfy framework dependency injection.

### D4 — runtime-context shape

Choose only the run-scoped resources actually needed by A3/A2/A4 and confirm they cannot become model-visible authority accidentally.

### D5 — routing representation

Baseline preference:

```text
node returns typed partial state update
→ small pure conditional router chooses next node
```

Prefer conditional edges over `Command` while routing-only functions remain clearer. Reopen `Command` only if update+goto genuinely becomes one cohesive responsibility and separate routers become duplication.

### D6 — A4 cohesion

Keep A4 cohesive unless current evidence shows a different downstream route, retry/resume boundary, effect-isolation requirement, or observability problem that pays for splitting execution from reduction.

### D7 — naming

Use terminology that prevents the framework envelope from being confused with trusted domain state. `EvidenceGapWorkflowState` is the current leading name; exact final name remains a small implementation-design choice.

Once D1–D7 are resolved sufficiently for implementation, stop Planning/Design and hand off to the active Build/Implement procedure.

---

## 9. Ordered R4-B sequence

### R4-B0 — research/design consolidation

**Purpose:** convert the new proposal/research and post-research discussion into controlling execution/learning guidance without treating the proposal as authority.

**Output:** this plan + refined learning-depth route + active working-memory checkpoint.

**Proof limit:** planning evidence only; no LangGraph implementation claim.

### R4-B1 — decision-critical Learning-by-Doing

Learn only the concepts necessary to resolve §8:

```text
LangGraph workflow state vs UpgradePilot domain truth
partial state updates / overwrite semantics at practical level
runtime context vs workflow state
input vs internal vs output state schemas
conditional routing vs node work
expected typed outcome vs exception
T1 observation vs T2 fresh admission placement
semantic replay vs checkpoint/time-travel replay
```

Use current official framework documentation when API behavior matters. Do not turn this into a broad LangGraph course.

**Ownership target:** Ali can explain what belongs in graph state, what remains UpgradePilot-owned, why A2 freshness occurs after A3, and why framework replay/checkpoints solve a different problem from A4 semantic replay.

### R4-B2 — graph architecture freeze

Resolve D1–D7 using the minimum-complete learning from R4-B1 and the real R4-A source/test baseline.

Record the material decisions and rationale in the active R4-B working memory. Update this plan or the learning map only if a durable route/depth decision actually changes.

**Pass:** exact graph boundary, state/context philosophy, routing, freshness placement, and proof target are unambiguous enough for Build.

### R4-B3 — Build preflight and dependency boundary

Under Build/Implement:

- inspect current experiment dependency configuration (`pyproject.toml` / lock state as applicable);
- determine the smallest experiment-appropriate LangGraph dependency change if not already present;
- verify source/test modification boundaries;
- confirm no product-runtime import/adoption is introduced.

Do not add LangChain merely because R4-B uses LangGraph unless the current dependency packaging makes that unavoidable and the consequence is explicitly understood.

### R4-B4 — implement the smallest graph

Expected first implementation responsibility:

```text
small typed workflow state
+ runtime context
+ A3 node
+ A2 fresh-admission node
+ cohesive A4 transition node
+ pure routers / edges
+ compile/invoke seam
```

Reuse existing R4-A domain types/functions/owners wherever doing so preserves one source of semantic truth.

Do not wrap the entire plain-Python orchestration as one giant graph node; that would provide little graph-comparison evidence. Do not duplicate A1/A2/A4 domain semantics inside framework-specific versions either.

### R4-B5 — deterministic semantic-equivalence proof

Hold nondeterminism constant before any live model smoke.

For each scenario, provide the same controlled planner result, fresh admission conditions, and repository result/failure to the ordinary-Python and LangGraph paths and compare UpgradePilot-owned outcomes.

Required scenario family:

| Scenario | Required graph behavior | Required invariant |
|---|---|---|
| A3 invocation/structured-output problem | A3 → END | no A2/A4 execution; no domain transition |
| `QUESTION_SETTLED` | A3 → A4 no-action → END | continuation-only update |
| `KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY` | A3 → A4 no-action → END | current no-action semantics preserved |
| `NO_JUSTIFIED_INVESTIGATION_IDENTIFIED` | A3 → A4 no-action → END | current no-action semantics preserved |
| ACTION_SELECTED + fresh A2 rejection | A3 → A2 → END | exact rejection; no repository call; no A4/domain transition |
| admitted + valid declaration | A3 → A2 → A4 → END | budget spent; consumed; domain updated; replay equal |
| admitted + typed target problem | A3 → A2 → A4 → END | semantic result; budget spent; consumed; domain semantics preserved |
| admitted + acquisition/provider operational failure | A3 → A2 → A4 → END | budget spent; not consumed; domain unchanged; replay equal |

At minimum assert when relevant:

```text
plain-Python final EvidenceGapInvestigationState
==
LangGraph final EvidenceGapInvestigationState

replay_evidence_gap_transition(graph_transition_trace)
== graph_transition_trace.after_state
```

Also prove external-call behavior:

```text
no model-dependent execution after typed A3 problem
no A2 execution on no-action decision
no repository call on A2 rejection
exactly one expected repository call on admitted first-seam action
zero model/repository calls during UpgradePilot semantic replay
```

Semantic equivalence does **not** require identical internal LangGraph traces, super-steps, or framework metadata.

### R4-B6 — bounded real S001 LangGraph smoke

Only after controlled equivalence is green:

```text
real UpgradePilot S001 product evidence
→ existing A1 projection
→ LangGraph A3/A2/A4 orchestration
→ exact target result / trusted state transition
→ EvidenceGapTransitionTrace
→ pure replay equivalence
```

The live local-model result proves runtime composition only. It does not replace deterministic equivalence tests or prove broad planner quality.

### R4-B7 — LangGraph comparison / disposition evidence

Compare ordinary Python and LangGraph on:

```text
semantic preservation
authority-boundary clarity
workflow/state clarity
branch readability
T2 freshness visibility
testability/debuggability
observability value
extra state/dependency/plumbing
framework-specific failure surface
terminology/replay burden
learning value
near-future growth fitness
```

Growth fitness is an evaluation criterion, not an implementation mandate. Judge how the chosen graph would accommodate **real future** investigation actions, evidence families, and bounded re-planning/multi-step investigation if/when admitted, without adding those capabilities now.

R4-B ends with evidence for R4-D/R4-C, not a product-framework adoption decision.

---

## 10. Learning-depth contract for R4-B

The detailed depth owner remains `B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`.

### Understand before architecture freeze

```text
workflow state vs domain truth
partial node updates
runtime context vs state
input/internal/output state distinction
nodes vs routers/edges
expected result vs exception
A2 T2 freshness placement
semantic replay vs framework checkpoint/time-travel replay
```

### Learn when first used materially

```text
exact StateGraph schema typing used by our code
Runtime/context_schema API used by our nodes
conditional-edge/router typing used by our graph
compile/invoke behavior used by our tests
basic graph trace/debug visibility needed for comparison
```

### Master through repeated implementation/comparison

```text
framework orchestration vs domain ownership
model proposal vs deterministic authorization
state-transition reasoning
semantic-equivalence testing
framework cost vs benefit judgment
```

### Deferred until explicit trigger

See §12. No feature should be adopted solely for educational exposure.

---

## 11. Near-future growth fitness without pre-building it

UpgradePilot already has credible product pressure toward more investigation capabilities/evidence families and may later justify bounded re-planning or multi-step investigation. R4-B should therefore ask whether its architecture has a clean extension path, but must not fabricate proof pressure.

Evaluate questions such as:

```text
if a second real investigation action is later admitted,
can routing grow without duplicating authority?

if different evidence families require distinct effect owners,
can graph topology express that without flattening domain semantics?

if another bounded planning turn is later justified,
can a deliberate back-edge/continuation rule be added with explicit budget/anti-repeat/stop semantics?
```

Do **not** implement any of those scenarios until real product evidence admits them.

---

## 12. Explicitly deferred framework surface and reopening triggers

| Feature | Defer because | Reopen only when |
|---|---|---|
| Checkpointer / persistent history | no current long-running/resume/thread responsibility; terminology collides with semantic replay | real crash/restart, pause/resume, thread continuity, or checkpoint-debug requirement |
| LangGraph time travel | downstream nodes may be re-executed; not semantic replay | workflow debugging/forking is needed alongside—not instead of—semantic replay |
| Interrupts / HITL | no current human approval/input responsibility | a real action requires human approval/edit/input before continuation |
| Automatic retry/error-handler policy | retries change attempt/external-call/budget/idempotency semantics | explicit retry classes, idempotency, and budget accounting are defined |
| Custom reducers | current seam has sequential singleton writers | parallel writers or real accumulation semantics appear |
| `Command` routing | conditional edges keep update vs route ownership clearer | update+goto genuinely becomes one cohesive responsibility |
| ToolNode | normal tool loops can obscure/bypass A2; belongs to later tool/agent comparison | R4-C explicitly evaluates tool calling while preserving/retesting A2 |
| `create_agent` | introduces LangChain-style model/tool loop and contaminates R4-B | R4-C after lower-level LangGraph comparison |
| Subgraphs | no reusable nested/multi-agent responsibility | a real reusable nested/separately-owned workflow appears |
| Parallelism / `Send` | one sequential admitted action; concurrency creates freshness/reducer/race semantics | multiple independent admitted actions have defined concurrency benefit/authority |
| Automatic multi-turn loop | no admitted second turn/action; risks repeated investigation | explicit continuation, budget, anti-repeat, second-action, and stopping semantics exist |
| Persistent Store / cross-thread memory | no cross-run agent-memory responsibility | real cross-thread/user/application memory requirement |
| Advanced streaming | no current user-facing progressive-output need; may expose internal state | concrete UX/diagnostic streaming requirement + explicit redaction/output policy |
| LangSmith as correctness dependency | tracing is not semantic proof | observability/evaluation value justifies service use; tests remain authoritative |

---

## 13. R4-C boundary preserved intentionally

Do not consume the later LangChain comparison inside R4-B.

Leave these questions available for R4-C:

```text
direct local provider adapter vs LangChain model abstraction
current strict structured-output seam vs LangChain structured-output mechanisms
action descriptor + A2 vs LangChain tool schema/tool-call lifecycle
explicit bounded graph vs create_agent agent loop
explicit control vs middleware/guardrail/retry abstractions
```

A clean first R4-C slice may replace only A3's provider/model abstraction while A1/A2/A4 remain unchanged, then evaluate higher-level agent/tool abstractions separately if justified.

---

## 14. Pass condition

R4-B passes only when:

1. the selected LangGraph topology is small and explicitly justified;
2. A2 T2 freshness and deterministic authorization are preserved;
3. graph workflow state does not become a duplicate owner of domain truth;
4. existing typed UpgradePilot responsibilities remain the semantic source of truth unless a deliberate accepted redesign says otherwise;
5. controlled tests demonstrate semantic equivalence with the ordinary-Python baseline across the required branch/outcome matrix;
6. `EvidenceGapTransitionTrace` and pure semantic replay remain valid and external-I/O-free;
7. one bounded real S001 LangGraph smoke composes successfully after controlled proof;
8. framework benefits and costs are compared explicitly, including credible near-future growth fitness;
9. Ali has practical ownership of the decision-critical LangGraph/agent-engineering concepts actually used;
10. no deferred framework feature or product integration is smuggled into the baseline.

A technically working graph that cannot demonstrate meaningful value beyond extra machinery is still a valid R4-B result; record that evidence rather than expanding the graph until the framework appears useful.

---

## 15. Stop line / prohibited scope

This plan does **not** authorize:

- product-runtime imports/integration;
- general LangGraph/LangChain adoption;
- automatic multi-turn investigation;
- fabricated second actions or evidence families;
- model-direct execution authority;
- bypassing or hiding A2 deterministic admission;
- duplicated graph-owned domain truth;
- checkpoints/persistence/time-travel as replacement for semantic trace/replay;
- retries without explicit attempt/idempotency/budget semantics;
- ToolNode / `create_agent` inside the first R4-B baseline;
- HITL/subgraphs/parallelism merely for framework exposure;
- broad agent-platform architecture.

After R4-B comparison evidence is complete, stop and hand the evidence to the parent R4 route for R4-C/R4-D. Any product adoption of LangGraph/LangChain remains a later explicit consequential architecture/build decision and may require an ADR at that time.

---

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`
