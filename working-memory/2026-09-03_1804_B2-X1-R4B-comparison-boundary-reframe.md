# B2/X1 R4-B — Comparison Boundary Reframe and Corrected Learning-by-Doing Entry

**Date/time:** 2026-09-03 18:04 (+03:30)  
**Last material update:** 2026-09-04 19:04 (+03:30)  
**Session status:** CONTINUED  
**Primary responsibility/mode:** R4-B LangGraph comparison/design / Learning-by-Doing + Planning/Design  
**Related parent plan:** `../plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**Related bounded plan:** `../plans/B2_X1_R4B_LANGGRAPH_LBD_IMPLEMENTATION_AND_COMPARISON_PLAN.md`  
**Learning-depth owner:** `../plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`  
**Current corrected research:** `../proposals/2026-09-03_B2_X1_R4B_CORRECTED_LANGGRAPH_INDEPENDENT_RESEARCH_AND_DESIGN_PROPOSAL.md`  
**Previous:** `2026-09-02_B2-X1-R4B-langgraph-lbd-entry.md`  
**Continued by:** `2026-09-04_1904_B2-X1-R4B-architecture-freeze-and-build-entry.md`  
**Product runtime integration:** not authorized

## 1. Session anchor

R4-A ordinary Python is complete and remains a valuable reference/control implementation and evidence source. The project then entered R4-B and produced a LangGraph research/design proposal, bounded R4-B plan, refined learning-depth route, and working-memory consolidation.

A subsequent Learning-by-Doing design discussion exposed a material comparison-design problem: the refined R4-B route had promoted too many R4-A experiment implementation choices into LangGraph architecture constraints. In particular, it increasingly treated the exact A1/A2/A3/A4 decomposition, `EvidenceGapInvestigationState`, `EvidenceGapTransitionTrace`, and related R4-A representations as structures R4-B should preserve or wrap rather than as evidence to inspect.

That pressure conflicts with UpgradePilot's existing retention discipline:

```text
existing implementation
= evidence to inspect
!= architectural authority to preserve
```

The corrected objective is therefore to compare competent implementations of the **same bounded UpgradePilot responsibility and framework-independent semantics**, while allowing each implementation approach to use an architecture natural to its own mechanism.

## 2. Accepted comparison reframe

Use this distinction going forward:

```text
R4-A
→ reference implementation
→ engineering evidence
→ lessons / failure modes / useful mechanisms
→ comparison result

R4-A
!= architectural specification for R4-B
```

R4-B should start from:

```text
accepted UpgradePilot framework-independent semantics
+ bounded EvidenceGapPlanner responsibility
+ trust / authority / failure / investigation constraints
+ real product-owned reusable capabilities
+ R4-A lessons and evidence
+ current LangGraph execution model
→ independently design the smallest proportionate LangGraph implementation
```

Do **not** start from:

```text
A1/A2/A3/A4 classes/functions
+ EvidenceGapInvestigationState
+ EvidenceGapTransitionTrace
→ find LangGraph containers/nodes that preserve those exact representations
```

This does not authorize redesign of accepted product semantics. It removes accidental implementation-retention constraints from the framework comparison.

## 3. What remains common across implementations

The cross-implementation comparison should preserve the applicable accepted semantics and observable responsibility, including where relevant:

- bounded model observation / no accidental authority leakage;
- model proposal does not itself authorize external action;
- action execution must be governed by sufficiently current trusted deterministic authority at the appropriate pre-execution point;
- rejected/unauthorized action does not execute;
- no-action outcomes remain explicit and semantically distinguishable;
- expected semantic/domain outcomes remain distinct from operational/provider failures and unexpected implementation defects;
- investigation budget and action-consumption consequences remain correct;
- exact evidence identity/scope and established product interpretation responsibilities remain owned by their normal product/domain owners;
- external effects/calls are observable and testable;
- semantic consequences can be tested/reconstructed without silently repeating nondeterministic/external work when that proof responsibility applies.

The exact Python classes, workflow-state representation, node/task boundaries, routing mechanism, internal trace shape, and framework observability representation are **not automatically shared invariants**.

## 4. Product-owned reuse boundary

Independent LangGraph design does not mean duplicating product/domain capabilities merely to be different.

Existing product-owned mechanisms such as exact repository acquisition, target declaration interpretation, target relevance, and Python-support impact evaluation should be reused when they still own the same product responsibility. R4-B is allowed to redesign experiment/orchestration structure around those capabilities; it is not authorized to create a second product truth implementation.

## 5. Correct comparison method

The comparison should no longer require identical internal representations such as:

```text
plain-Python EvidenceGapInvestigationState
==
LangGraph workflow state
```

Instead define common controlled cases and compare framework-neutral observable outcomes. Depending on the scenario, inspect matters such as:

```text
action selected / no action / rejected
whether execution occurred
whether required current authority was checked at the correct time
which exact action/evidence path executed
budget consequence
action-consumption consequence
final domain/applicability conclusion
expected semantic result vs operational failure behavior
forbidden external-call absence
reproducible/testable semantic consequence
```

Framework-specific state/local values, topology/control flow, trace, checkpoint, and observability evidence may also be compared as **value/overhead characteristics**, but they do not become the semantic oracle merely because one framework/API provides them.

## 6. Initial owner alignment completed

The repository owner chain was reconciled to the comparison correction:

1. **Parent R4 plan** — states that R4 compares competent implementations of the same bounded responsibility and that R4-A is evidence/reference rather than architectural authority for R4-B.
2. **Bounded R4-B plan** — reframed around framework-neutral responsibility classification → LangGraph learning → independent design → Build → normalized semantic comparison.
3. **R4 learning-depth map** — preserved R4-A learning while removing the old mandatory graph/state/A-number mapping.
4. **`MEMORY.md`** — selected the corrected live route and stated that LangGraph source implementation had not begun.
5. **Previous R4-B working memory** — marked historical/superseded and points to this record.
6. **2026-09-02 research/design proposal** — intentionally left unchanged as non-controlling historical research evidence.
7. **Specifications/ADRs** — no new specification or ADR was created because accepted framework-independent semantics already have owners and no product framework adoption has been selected.

That alignment established the correct comparison boundary but did not yet prove or select a LangGraph architecture.

## 7. Learning-by-Doing resumed — first classification slice

After the owner correction, Learning-by-Doing resumed against the real R4-A source.

The first focused slice examined **model observation vs execution authority** using:

- `experiments/b2_x1_evidence_gap_planner.py`;
- `experiments/b2_x1_evidence_gap_admission.py`.

### Classification established

Framework-independent requirements:

```text
model receives only justified bounded observation
model proposal does not self-authorize execution
sufficiently current deterministic authority must exist after proposal and before effect
rejected/unauthorized proposal must not execute
```

R4-A engineering lessons/evidence:

```text
explicit request projection prevents accidental context expansion
T1 observation vs T2 currentness exposes real TOCTOU/freshness pressure
stable action identity should not let the model redefine hidden execution authority
```

R4-A/Python-specific mechanisms, not automatic R4-B requirements:

```text
EvidenceGapPlannerContext
EvidenceGapAdmissionState
BoundInvestigationAction as this exact class
project_action_descriptor(...)
admit_selected_investigation_action(...) as this exact function
physical A1 / A2 decomposition
```

### Ali reasoning result

Ali correctly selected the framework-neutral interpretation:

```text
required:
current deterministic authorization after model proposal and before external effect

not established:
a dedicated authorization node is mandatory
```

Important refinement: this is not merely because R4-A evidence is limited. Even stronger evidence for the authorization responsibility would not by itself establish one mandatory physical node/function shape.

## 8. Corrected independent research proposal reviewed

A new research agent added:

`proposals/2026-09-03_B2_X1_R4B_CORRECTED_LANGGRAPH_INDEPENDENT_RESEARCH_AND_DESIGN_PROPOSAL.md`

Repository evidence horizon used by that proposal: `main@9bb534eda0ef68d701b031b5a19add432a52e910`.

The proposal is non-controlling and explicitly respects the corrected comparison boundary.

### Strong accepted research findings

The proposal materially improves the route in these areas:

1. **R4-A classification is treated as design evidence, not topology authority.**
2. **Workflow communication, product/domain truth, and runtime dependencies are separated explicitly.**
3. **Current authority should be obtained after the proposal rather than precomputed and carried as supposedly fresh state.**
4. **Framework-neutral comparison remains the semantic oracle.**
5. **Effect vs deterministic consequence is a real independent design question rather than an A4-preservation decision.**
6. **`Command` is a credible Graph API mechanism when update + dynamic routing are one cohesive responsibility; it is not mandatory.**
7. **Persistence/retry/HITL/ToolNode/subgraph/parallelism/multi-turn remain unjustified for the first slice.**
8. **Functional API is a first-class LangGraph alternative that the earlier route had not evaluated sufficiently.**

### Strongest researched Graph API candidate — not frozen

The proposal independently derives:

```text
START
→ PLAN
   → model problem / no-action → CONCLUDE
   → action proposal → AUTHORIZE
       → rejected → CONCLUDE
       → authorized → INVESTIGATE
           → CONCLUDE
→ END
```

Its rationale is responsibility-derived rather than A-number-derived:

- `plan` — bounded model observation + provider/model result;
- `authorize` — current deterministic pre-effect authority decision;
- `investigate` — admitted external investigation effect + product-owned interpretation;
- `conclude` — pure deterministic budget/consumption/domain/continuation consequence.

This is currently the strongest researched **candidate**, not accepted architecture.

### Serious Functional API alternative

The proposal correctly identifies LangGraph Functional API (`@entrypoint` + optional `@task`) as a serious fit.

Potential strength:

```text
ordinary Python control flow
+ lower explicit state/topology ceremony
+ LangGraph runtime
```

Potential weakness:

```text
less explicit static topology/state inspection
+ weaker discrimination of Graph API orchestration value
+ possible later migration if real action/state/branching complexity grows
```

The correct question became:

```text
which LangGraph API paradigm best implements the responsibility and credible product trajectory?
```

not:

```text
what should our StateGraph state fields be?
```

Do not build both APIs by default.

## 9. Owner alignment after proposal review

The proposal review produced a targeted owner refinement, not another plan family.

Updated:

1. **`plans/B2_X1_R4B_LANGGRAPH_LBD_IMPLEMENTATION_AND_COMPARISON_PLAN.md`**
   - adds explicit R4-B2A Graph API vs Functional API gate;
   - moves deep StateGraph mechanics to selected-paradigm learning;
   - keeps four-stage Graph API as research evidence, not frozen architecture;
   - records when a second API implementation may be reopened.

2. **`plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`**
   - teaches Graph API vs Functional API before StateGraph-specific design;
   - elevates workflow communication vs product truth vs runtime dependencies as the cross-API concept;
   - makes Graph API and Functional API mechanics conditional on selection;
   - keeps exact framework syntax lookup-assisted until Build.

3. **`MEMORY.md`**
   - selects the API-paradigm-aware live route;
   - records the proposal as non-controlling current research evidence;
   - records the first R4-B1 ownership result;
   - keeps LangGraph implementation stopped.

Not changed:

- accepted specifications;
- ADRs;
- parent R4 route materially;
- source/tests/dependencies;
- either research proposal.

No new plan or working-memory record was created because the responsibility remains the same R4-B session/design journey.

## 10. R4-B2A Learning-by-Doing result — why Graph API currently leads

The API-paradigm learning was continued against the real UpgradePilot responsibility rather than generic examples.

### Current architectural lean

Ali initially leaned toward the Graph API position because R4-A experience showed that these distinctions were materially important:

```text
model reasoning
!= trusted authorization
!= external effect
!= deterministic consequence
```

The accepted reasoning is **not**:

```text
R4-A had separate A1/A2/A4 pieces
→ LangGraph must have separate nodes
```

It is:

```text
R4-A exposed real trust/effect/debug/proof pressure
→ explicit workflow topology may provide material value
→ Graph API deserves to lead the first LangGraph design until evidence reverses it
```

Functional API remains a serious fallback rather than being rejected as "not real LangGraph."

### State / runtime context / freshness grounding

The real S001/R4-A code was used to attach new LangGraph vocabulary to already-learned engineering behavior.

Current mental model:

```text
Graph State
→ information produced by one meaningful workflow stage that a later stage needs
→ current candidates: planner_outcome, authority_outcome, investigation_outcome, final_result

runtime context/resources
→ capabilities used by graph work but not themselves evolving semantic workflow facts
→ current candidates: model/provider, GitHubRepositoryClient, possibly a current-authority acquisition/composition capability

fresh T2 authority facts
→ current repository/revision/propositions/consumption/budget/action bindings established where authorization needs them
→ they may remain local to AUTHORIZE if later stages do not need the raw facts
```

Critical retained distinction:

```text
value exists in Graph State
!= value is current
!= value is trusted
!= value is authorized
```

The T1→T2 R4-A admission design was explicitly connected to TOCTOU/currentness pressure. The example of another legitimate activity changing budget/revision/consumption between model observation and pre-effect authorization was clarified as a concurrency/staleness concern; it does **not** imply R4-B is implementing parallel graph actions.

### Routing mechanics learned

Decision-critical Graph API routing concepts were introduced:

```text
static edge
→ unconditional next responsibility

conditional edge
→ separate routing callable chooses destination from state/outcome

Command
→ node can cohesively return state update + dynamic next destination
```

Current strongest routing candidate remains:

```text
PLAN
├─ action proposal → AUTHORIZE
└─ no-action/provider problem → CONCLUDE

AUTHORIZE
├─ authorized → INVESTIGATE
└─ rejected → CONCLUDE

INVESTIGATE → CONCLUDE → END
```

`Command` currently looks proportionate for `PLAN` and `AUTHORIZE`; static edges look proportionate after `INVESTIGATE` and `CONCLUDE`. This is still a **candidate**, not frozen architecture. The final decision must test whether local routing cohesion is worth more than externally separated conditional routers.

## 11. Framework-value challenge — LangGraph must earn itself

Ali raised a material concern before architecture freeze: most concepts learned so far—state, branching, deterministic authorization, effect boundaries, typed outcomes—can already be implemented cleanly in ordinary Python, and R4-A proves that.

That concern is accepted and changes the R4-B evaluation standard.

### Technical conclusion

LangGraph does not give UpgradePilot a semantic/computational capability that Python fundamentally lacks. In particular:

```text
StateGraph state
conditional routing
node boundaries
if-like branching
```

are not sufficient adoption value by themselves.

If R4-B mainly translates ordinary Python state/branches into graph primitives, that is evidence that LangGraph has **not earned its dependency**.

### Where LangGraph can provide real leverage

The serious framework-value hypothesis is the orchestration/runtime infrastructure around the workflow, including credible capabilities such as:

```text
durable execution / checkpoint persistence / recovery
pause-resume and human-in-the-loop interrupts
standardized runtime streaming/events/observability
executable/inspectable workflow topology
richer branching/composition
subgraphs / larger workflow decomposition
parallel or multi-agent orchestration when actually required
```

Python can implement all of these, but doing so would progressively make UpgradePilot own more orchestration infrastructure. LangGraph is valuable only if its runtime removes enough of that burden while preserving the product's trust/authority/evidence semantics.

Current R4-A already has strong evidence for simple orchestration:

```text
explicit model/authority separation
typed outcomes/failures
immutable state consequences
trace/replay proof
47/47 focused tests
real S001 proof
```

Therefore LangGraph faces a high bar. The experiment should not claim victory because the graph looks cleaner.

### Current vs future value distinction

Most of LangGraph's strongest runtime advantages are **not required by the first one-action R4-B implementation**. This initially looked like a warning against the framework, but it exposed a more precise design requirement: the project is evaluating LangGraph partly because UpgradePilot is intended to grow toward richer agentic/orchestration responsibilities.

Use three evidence classes:

```text
CURRENTLY EXERCISED VALUE
→ demonstrated directly by R4-B implementation/tests/runtime

CREDIBLE ARCHITECTURAL VALUE
→ framework capability materially relevant to the intended larger UpgradePilot trajectory, even if not implemented in the first slice

SPECULATIVE VALUE
→ imagined future machinery without a concrete product trajectory/responsibility
```

Only the first two should influence the eventual framework decision, and they must remain visibly distinct.

## 12. Bounded build / long-horizon architecture correction

Ali explicitly established an important planning constraint:

> Build in small slices, but do not think only in the dimensions of the small slice.

The first R4-B implementation should remain deliberately bounded. However, choices must not be made solely because today's experiment has one action, one model turn, or one agent. That would drift from the purpose of evaluating a framework for the larger product direction.

Use:

```text
BUILD SMALL
→ no fabricated second action
→ no speculative multi-agent graph
→ no persistence/HITL/subgraphs/parallelism just for exposure

THINK AT PRODUCT HORIZON
→ consider credible additional agents/orchestration
→ consider durable execution/recovery burden
→ consider richer investigation branching/composition
→ consider human approval/interrupt needs if product direction earns them
→ consider observability/debugging burden as workflows grow

KEEP EVIDENCE DISCIPLINE
→ future pressure informs boundaries/paradigm
→ future pressure does not itself authorize implementation
```

This corrects an over-local optimization risk in the earlier wording "the current workflow is small, therefore Functional API may be enough." Current size remains relevant to ceremony cost but is **not** the sole or primary architectural horizon.

The bounded R4-B plan and `MEMORY.md` were updated on 2026-09-04 to preserve this rule.

## 13. Current route after the long-horizon correction

R4-B1 is sufficiently complete for the current architecture responsibility; reopen classification only if a new design question exposes an ownership ambiguity.

R4-B2A is materially advanced:

```text
Graph API
→ current leading first-implementation candidate

Functional API
→ serious fallback if explicit topology/state mainly relocates Python complexity

ordinary Python
→ remains a strong control and may still win R4-D if LangGraph does not remove enough burden
```

R4-B2B has covered enough State/context/freshness and routing concepts for the next decision. Do not start another broad LangGraph theory phase.

### Immediate next

```text
1. Resolve routing cohesion
   PLAN: Command vs separate conditional router
   AUTHORIZE: Command vs separate conditional router
   judge against current clarity/proof + credible larger workflow evolution

2. Enter R4-B3 architecture freeze
   record:
   - selected API paradigm + fallback trigger
   - input boundary
   - Graph State communication model
   - runtime context/resources
   - nodes/responsibilities
   - routing/termination
   - current deterministic authority placement
   - external effect boundary
   - deterministic conclusion/output
   - proof/observability strategy
   - deliberately deferred implementation features
   - long-horizon fit
   - explicit framework-value hypothesis

3. Hand off immediately to Build/Implement
   → dependency/lock preflight
   → smallest real LangGraph experiment
   → controlled semantic proof
   → bounded S001 smoke
```

## 14. Current stop lines

Remain stopped before LangGraph source/dependency implementation only until the final routing choice and architecture freeze are sufficiently clear for Build.

Still prohibited unless separately admitted:

- product runtime integration;
- fabricated second investigation action;
- automatic multi-turn planner loop;
- framework/API adoption claim;
- building both LangGraph APIs merely for exposure;
- implementing checkpoint/persistence/HITL/retry/subgraph/parallel machinery merely for future appearance;
- choosing/rejecting the architecture solely because the first slice is small;
- duplication of established product-owned semantics/capabilities.

Deferred framework capabilities may still be considered as **credible architectural value** when the intended product trajectory makes them relevant. They remain non-proof until actually exercised.

## 15. Evidence / non-proof

Established by the current planning/LbD work:

- the live owner chain describes one coherent corrected comparison method;
- R4-A remains a serious reference/control and evidence source without becoming R4-B architecture authority;
- model-proposal vs current deterministic authorization is classified at ownership level;
- Graph API and Functional API are both understood as first-class LangGraph paradigms;
- Graph API is the current leading candidate for the first implementation, but is not frozen;
- Graph State vs runtime context vs fresh authority facts is understood at the level needed for current architecture decisions;
- static/conditional/`Command` routing concepts are understood at decision level;
- LangGraph is not treated as valuable merely because it can express state/branches that Python already handles;
- the serious framework-value hypothesis is **orchestration/runtime burden reduction and credible larger-system fit**;
- bounded implementation scope is explicitly separated from architectural horizon;
- product/domain owner reuse and framework-independent semantic constraints remain protected.

Not established:

- any LangGraph source behavior;
- final `Command` vs conditional-edge routing choice;
- final graph state/type/node topology;
- semantic equivalence between Python and LangGraph;
- that four stages are better than a coarser Graph API flow;
- that LangGraph will actually reduce enough burden to justify adoption;
- product runtime readiness;
- multi-agent/multi-action/multi-turn product value;
- persistence/HITL/subgraph/parallel runtime value in UpgradePilot—their relevance is currently architectural hypothesis, not exercised evidence.

## 16. Provenance

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`