# LangGraph Bounded Evidence-Gap Planner Independent Design, Implementation, and Comparison Plan

**Status:** AUTHORIZED BOUNDED PLAN ARTIFACT — subordinate to the selected bounded evidence-gap planner implementation/comparison/evaluation plan; position-neutral; `MEMORY.md` alone owns live continuation  
**Date:** 2026-09-03  
**Revision:** corrected comparison boundary + API-paradigm gate + bounded-build / long-horizon architecture correction + semantic sequence naming  
**Parent plan:** `BOUNDED_EVIDENCE_GAP_PLANNER_IMPLEMENTATION_COMPARISON_AND_EVALUATION_PLAN.md`  
**Learning-depth owner:** `BOUNDED_EVIDENCE_GAP_PLANNER_IMPLEMENTATION_COMPARISON_LEARNING_DEPTH_AND_REENTRY_MAP.md`  
**Current corrected research evidence:** historical proposal at `../proposals/2026-09-03_B2_X1_R4B_CORRECTED_LANGGRAPH_INDEPENDENT_RESEARCH_AND_DESIGN_PROPOSAL.md`  
**Historical research evidence:** historical proposal at `../proposals/2026-09-02_B2_X1_R4B_LANGGRAPH_RESEARCH_AND_DESIGN_PROPOSAL.md`  
**Current correction provenance:** historical record at `../working-memory/2026-09-03_1804_B2-X1-R4B-comparison-boundary-reframe.md`  
**Responsibility:** independently design, learn, implement, prove, and compare the smallest credible LangGraph implementation of the same bounded `EvidenceGapPlanner` responsibility already explored in ordinary Python, while preserving accepted UpgradePilot semantics, allowing LangGraph to use an architecture natural to its own execution model, and judging that architecture against the credible larger UpgradePilot orchestration trajectory rather than only the first tiny experiment slice  
**Product runtime integration:** NOT authorized

Exact old proposal/working-memory filenames above are retained only as provenance. They are not current plan-step vocabulary.

---

## 1. Why this plan exists

The ordinary-Python bounded control produced a coherent reference implementation. That implementation is valuable because it exposed real engineering responsibilities, failure modes, authority boundaries, and testable semantics before framework adoption was considered.

The LangGraph experiment asks a different question:

> **If the same bounded UpgradePilot responsibility is designed competently with LangGraph rather than ordinary Python orchestration, what implementation architecture results, what does LangGraph materially improve or worsen, and what should that teach the eventual production architecture?**

An earlier refinement over-preserved ordinary-Python implementation structure. It treated several experiment-owned Python representations and old step boundaries as if LangGraph should mainly wrap or reproduce them. The Learning-by-Doing design review rejected that comparison method because it would measure how well LangGraph imitates the Python design rather than how well LangGraph implements the same responsibility.

A later corrected research proposal exposed a second bias: the route still leaned too quickly toward `StateGraph` and shared graph-state design before treating LangGraph's **Graph API** and **Functional API** as two first-class implementation paradigms.

A subsequent design review exposed a third risk: using the smallness of the first implementation slice as the dominant architecture criterion would optimize locally for one action/one bounded workflow even though the framework evaluation exists partly because UpgradePilot is expected to grow toward richer agentic orchestration. The first implementation should remain small; the architectural horizon should not be artificially small.

This plan therefore enforces four disciplines:

```text
SEMANTIC DISCIPLINE
→ accepted UpgradePilot behavior, trust, authority, failure, evidence, and investigation rules remain controlling

ARCHITECTURAL INDEPENDENCE
→ ordinary-Python implementation structure is evidence/reference, not automatic LangGraph architecture authority

FRAMEWORK-PARADIGM NEUTRALITY
→ do not assume Graph API / StateGraph is the only competent LangGraph-native implementation style
→ choose the API paradigm from the responsibility and evidence before freezing StateGraph-specific structure

BOUNDED BUILD / LONG-HORIZON ARCHITECTURE
→ implement only the smallest evidence-producing LangGraph slice
→ evaluate architecture against the credible intended UpgradePilot trajectory, including richer agent/orchestration responsibilities
→ do not choose a locally convenient architecture solely because the first graph currently has one action or one agent
→ future pressure informs architecture selection but does not authorize speculative implementation
```

The correction remains consistent with the project-wide retention rule:

```text
existing implementation
= evidence to inspect
!= authority to preserve unchanged
```

---

## 2. Owner split and authority

### Broader implementation-comparison authorization

`BOUNDED_EVIDENCE_GAP_PLANNER_IMPLEMENTATION_COMPARISON_AND_EVALUATION_PLAN.md`

Owns the broader ordinary-Python control → LangGraph experiment → LangChain bounded abstraction investigation → cross-implementation comparison route and later bounded-planner disposition.

### Stable framework-independent semantics

Use the applicable accepted owners rather than re-specifying them here:

- `../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`
- `../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`
- `../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`
- `../docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`

These own accepted trust/evidence/failure/authority/investigation/generalization semantics. They do not select LangGraph, Graph API, Functional API, or any internal workflow representation.

### This plan

Owns the bounded LangGraph route:

```text
comparison-boundary classification
→ LangGraph API-paradigm learning/comparison
→ selected-paradigm decision-critical learning
→ independent LangGraph architecture design
→ architecture freeze
→ smallest experiment implementation
→ controlled framework-neutral semantic proof
→ bounded real pydantic Python-support smoke
→ LangGraph framework value/cost findings
```

### Learning depth

`BOUNDED_EVIDENCE_GAP_PLANNER_IMPLEMENTATION_COMPARISON_LEARNING_DEPTH_AND_REENTRY_MAP.md`

Owns what Ali should understand before architecture decisions, what should be learned when first used materially, and what remains deferred.

### Ordinary-Python comparison evidence

Ordinary-Python source/tests/working memories are the comparison reference and engineering evidence. They are not a second specification and do not automatically constrain LangGraph representation.

### Corrected research proposal

`../proposals/2026-09-03_B2_X1_R4B_CORRECTED_LANGGRAPH_INDEPENDENT_RESEARCH_AND_DESIGN_PROPOSAL.md`

This exact historical filename identifies the strongest current non-controlling research/design evidence. It independently derives a four-stage Graph API candidate, evaluates a serious Functional API alternative, and records framework facts/trade-offs. Its recommendations are evidence for the decision gates below, not accepted architecture.

### Historical research proposal

`../proposals/2026-09-02_B2_X1_R4B_LANGGRAPH_RESEARCH_AND_DESIGN_PROPOSAL.md`

Remains unchanged historical evidence. Framework facts may remain useful; implementation-preserving recommendations do not control the current LangGraph design.

### Live continuation

`../MEMORY.md` alone selects the live responsibility. The active dated working memory preserves detailed reasoning and handoff.

---

## 3. Ordinary-Python comparison role

The ordinary-Python implementation remains a serious reference/control:

```text
bounded EvidenceGapPlanner responsibility
→ model-visible projection and structured decision contract
→ local model invocation
→ deterministic pre-execution authority/admission
→ bounded execution / interpretation / state consequences
→ trace / replay proof
```

The established evidence horizon remains:

```text
model-observation projection family: 10/10 PASS
deterministic authority family: 13/13 PASS
local model/provider family: 13/13 PASS
execution/transition family: 7/7 PASS
combined focused family: 47/47 PASS
real pydantic dependency-upgrade model selection/admission: PASS
real pydantic dependency-upgrade execution/update/trace/replay: PASS
```

Use the ordinary-Python implementation in four ways:

1. **reference implementation** — a coherent ordinary-Python solution to inspect and compare;
2. **engineering evidence** — reveals real failure modes, trust/authority needs, state consequences, and operational friction;
3. **learning evidence** — explains why certain responsibilities appeared during implementation;
4. **comparison result** — supplies observed complexity, clarity, proof surface, and growth pressure.

Do **not** use it as:

```text
mandatory LangGraph state schema
mandatory node decomposition
mandatory trace representation
mandatory class reuse boundary
mandatory mapping from old implementation steps to graph topology
```

A LangGraph implementation may independently converge on similar boundaries. When it does, the justification must come from the responsibility and LangGraph design rather than Python precedent.

---

## 4. Central LangGraph success question

Use:

> **Can a LangGraph-native implementation satisfy the same bounded UpgradePilot EvidenceGapPlanner responsibility and accepted framework-independent semantics while providing enough control-flow clarity, workflow-communication coherence, inspectability, test/debug leverage, runtime/orchestration burden reduction, and credible growth fitness to justify its dependency and framework machinery relative to the ordinary-Python reference?**

Evaluate at least four independent dimensions:

```text
SEMANTIC CORRECTNESS
→ does the implementation preserve accepted product/trust/authority/failure/investigation behavior?

ARCHITECTURAL QUALITY
→ is the LangGraph design coherent on its own terms rather than a mechanical translation of the ordinary-Python implementation?

FRAMEWORK VALUE
→ does LangGraph remove meaningful orchestration/runtime burden that UpgradePilot would otherwise have to own, rather than merely re-expressing Python branches/state with framework syntax?

TRAJECTORY FIT
→ does the design remain a credible foundation for the intended larger agentic/orchestration direction without pre-building unproven future machinery?
```

A workflow that merely runs fails the evaluation. A workflow that reproduces Python structure mechanically also provides weak evidence. A workflow that is elegant but weakens accepted semantics fails regardless of framework convenience.

A Graph API implementation that only turns ordinary Python `if` statements and dataclass state into nodes/edges/state has not, by that fact alone, justified LangGraph. The experiment should look for actual framework leverage such as executable workflow topology, standardized runtime observability, durable execution/persistence/recovery, interrupt/resume/human-in-the-loop support, richer branching/composition, or other orchestration infrastructure that would otherwise become UpgradePilot-owned burden. Not all of those features need to be implemented; some are legitimate architectural/value dimensions for the credible future system.

---

## 5. Common framework-neutral acceptance boundary

The LangGraph implementation must preserve the applicable accepted responsibility, not identical implementation objects.

The controlled comparison should include these common properties where the scenario makes them relevant:

```text
bounded model observation
→ the model receives only justified decision context

model result
→ proposal / semantic output
!= automatic external execution authority

pre-execution authority
→ action execution occurs only when sufficiently current trusted deterministic conditions permit it

rejection
→ denied/stale/consumed/disallowed action does not execute

no-action outcomes
→ remain explicit and semantically distinguishable

failure classes
→ semantic/domain result
!= expected operational/provider failure
!= unexpected implementation defect

investigation consequences
→ budget and action-consumption semantics remain correct

evidence/domain ownership
→ exact acquisition/identity/interpretation remains with the established owner where that responsibility already exists

external effects
→ required calls occur and forbidden calls do not

proof
→ final semantic consequences are testable against the accepted responsibility without hiding nondeterministic/external re-execution behind framework machinery
```

These are comparison/acceptance concerns. Exact concrete representations remain design questions unless an accepted specification/architecture decision already owns them.

---

## 6. Classification gate before LangGraph architecture

Before deciding workflow state, nodes/tasks, routing, or framework APIs, classify each material ordinary-Python concept into one of four buckets.

### Accepted framework-independent requirement

Examples may include:

- a model cannot grant its own execution authority;
- evidence/authority/failure distinctions must remain intact;
- current trusted execution conditions matter at the pre-execution boundary;
- investigation stopping and no-action semantics must remain honest.

These constrain every implementation.

### Reusable product-owned capability

Examples may include established exact repository acquisition, target declaration interpretation, target relevance, Python-support impact evaluation, and other product/domain facts already owned outside the experiment.

Reuse these when the LangGraph implementation needs the same responsibility. Independent framework design is not permission to duplicate product truth.

### Ordinary-Python engineering lesson/evidence

Examples:

- why an authority check became necessary;
- why semantic and operational failure needed separation;
- where trace/replay became useful;
- what test or live failure exposed a real problem.

These should pressure the LangGraph design but do not dictate its form.

### Ordinary-Python/Python-specific implementation choice

Examples may include:

- exact dataclass shape;
- exact `EvidenceGapInvestigationState` representation;
- old physical implementation decomposition;
- exact `EvidenceGapTransitionTrace` structure;
- helper/function/module boundaries chosen for ordinary Python.

These are open to independent redesign unless another owner establishes an implementation-independent need.

**Pass for this gate:** the important common requirements and reusable product capabilities are sufficiently clear that LangGraph design can proceed without treating ordinary-Python classes/topology as premises.

---

## 7. Independent LangGraph design principles

### Start from workflow responsibility, not Python classes or framework primitives

Ask:

```text
what does the workflow need from the caller?
what exact subset may the model observe?
what output may the model control?
what current trusted facts must be checked before any effect?
what operation performs external I/O?
what makes that I/O valid semantic evidence versus operational failure?
what deterministic consequences follow from each bounded outcome?
what information must communicate between those responsibilities?
what final result does the caller/comparison actually need?
```

Only then choose the LangGraph API paradigm and its representation/control-flow mechanisms.

### Reuse product capabilities, not experiment scaffolding by default

When an established product/domain callable already performs the exact same admitted responsibility, use it rather than reimplementing its semantics solely to make the framework look native.

Conversely, do not reuse an ordinary-Python experiment wrapper/type merely because it already exists if a simpler or more natural LangGraph representation satisfies the same responsibility.

### Let LangGraph earn its structure

Graph API/`StateGraph`, Functional API/`entrypoint`/`task`, conditional edges, `Command`, runtime context, checkpointers, interrupts, reducers, subgraphs, ToolNode, and other framework machinery are candidates only when the real responsibility or credible product trajectory makes them useful.

Do not add framework machinery for exposure, trend, pedagogy, or architectural appearance.

Also do not treat ordinary branching/state syntax as the framework's value proposition. If the experiment shows that LangGraph only relocates simple Python control flow without reducing a meaningful current or credible future orchestration burden, that is evidence against adoption.

### Avoid fake independence

A LangGraph implementation that merely duplicates all existing domain logic under new names is not an independent architecture; it is semantic duplication.

Independent design means freedom in **orchestration/representation**, not freedom to fork accepted product truth.

### Treat future growth as architectural pressure, not implementation authorization

Credible future additional agents, investigation actions/evidence families, bounded replanning, durable workflow execution/recovery, human approval/interrupt boundaries, richer branching/composition, and stronger runtime observability may materially influence whether one paradigm becomes an architectural dead end or avoids future UpgradePilot-owned orchestration burden.

That pressure must be considered when selecting the first architecture. It does **not** authorize generic dispatch, loops, subgraphs, persistence, human-in-the-loop behavior, or parallelism in the current implementation unless a present proof responsibility requires them.

### Bounded implementation scope does not imply bounded architectural horizon

Use:

```text
BUILD SMALL
→ implement the smallest real slice that can produce discriminating evidence

THINK AT PRODUCT HORIZON
→ choose boundaries/paradigms with the credible intended larger system in view

DO NOT SPECULATE
→ do not implement future machinery simply because it may someday be useful
```

Do not choose Functional API merely because the first workflow is small. Do not choose Graph API merely because future growth is imaginable. The selected paradigm should win because the current responsibility plus credible trajectory together make its structure/runtime value proportionate.

---

## 8. Decision-critical Learning-by-Doing before architecture freeze

Learn only enough to make the independent design choices correctly.

### LangGraph Graph API versus Functional API decision

Before assuming shared graph state or static topology, understand the two relevant first-class LangGraph styles at **design level**:

```text
GRAPH API
→ StateGraph
→ explicit nodes + edges/routing
→ explicit shared workflow communication/state
→ static visualization / inspectable topology
→ stronger fit when branching/state/control-flow structure itself is important

FUNCTIONAL API
→ @entrypoint + optional @task
→ ordinary Python control flow / local workflow values
→ LangGraph runtime without requiring an explicit shared StateGraph schema
→ lower ceremony for naturally procedural workflows
→ migration to Graph API remains possible if control-flow/state pressure later grows
```

The decision question is not "which API is more powerful?" It is:

> **Which paradigm gives the strongest foundation for the accepted current responsibility and credible UpgradePilot orchestration trajectory, while allowing the first evidence-producing implementation to remain small and proportionate?**

Current evidence makes Graph API the leading candidate, not because the first slice needs complex graph machinery, but because the ordinary-Python control exposed materially important planning/authority/effect boundaries and the intended larger system makes explicit topology/control-flow plus LangGraph runtime capabilities a meaningful hypothesis to test. Functional API remains a serious fallback because it can provide the same LangGraph runtime with less explicit topology/state ceremony; current workflow size alone must not decide the choice.

Do not build both by default.

**Pass:** Ali can explain what changes between Graph API and Functional API here, why either can preserve the same semantics, what engineering/runtime burden LangGraph must remove to justify itself over ordinary Python, why Graph API currently leads, and what evidence would favor Functional API or ordinary Python instead.

### Selected-paradigm decision-critical mechanics

After the API-paradigm gate is sufficiently understood, learn only the mechanics required by the leading/selected candidate.

If **Graph API** remains the selected candidate, learn proportionately:

```text
StateGraph execution model
START / END
node work vs routing work
shared workflow communication/state
partial state updates and overwrite/reducer implications
conditional edges
Command when update + routing are one cohesive responsibility
input schema vs internal state vs output schema
runtime context/resources vs evolving workflow facts
compile/invoke execution boundary
basic tracing/stream visibility
```

If **Functional API** becomes the selected candidate, learn proportionately:

```text
entrypoint lifecycle
ordinary Python control flow inside the workflow
local workflow values vs durable/runtime-managed task values
task boundaries only where they earn value
runtime context/dependency access
return/output boundary
basic tracing/observability
persistence/replay implications only enough to avoid semantic-proof confusion
```

For either paradigm, also understand:

```text
expected typed workflow outcome
!= unexpected programmer/framework exception

workflow recovery/history
!= deterministic semantic proof
```

Current Graph API learning has established these working distinctions:

```text
Graph State
→ evolving workflow communication needed across meaningful stages
→ current candidates: planner outcome, authority outcome, investigation outcome, final result

runtime context/resources
→ run-scoped capabilities such as model/provider and GitHub repository client

current authorization facts
→ derive/check at the pre-effect authority boundary when currentness matters
→ presence in Graph State does not itself make a value fresh, trusted, or authorized

routing
→ static edge when destination is unconditional
→ conditional edge when a separate routing function earns clarity
→ Command is a candidate when one node cohesively produces an outcome/state update and selects the next responsibility
```

Exact API syntax remains lookup-assisted until implementation.

### Important design questions after the premises are understood

```text
which LangGraph API paradigm best fits the current responsibility + credible product trajectory?
what meaningful orchestration/runtime burden should LangGraph remove compared with ordinary Python?
what values genuinely need to communicate between meaningful workflow stages?
which facts should be persisted/shared vs local/derived vs runtime resources?
what are the meaningful work/control-flow boundaries?
where should model observation/projection occur?
where and how should deterministic execution authority be enforced?
what routing is truly dynamic?
when does Command improve cohesion vs hide useful routing separation?
what belongs in final workflow output?
what domain/evidence capability should remain ordinary product code called by the workflow?
what effect boundaries matter for testability/retry/resume semantics even while those features remain deferred?
which locally convenient choices would create avoidable migration/coordination burden for the credible larger multi-agent/orchestration system?
```

Do not ask Ali to freeze StateGraph state/topology before the API-paradigm question is understood.

---

## 9. Architecture freeze gate

Freeze only what Build genuinely needs, but evaluate those choices against both current responsibility and credible system trajectory.

The architecture decision record in the active working memory should make these recoverable:

```text
1. LangGraph API paradigm selected for the first implementation and why
2. workflow responsibility and explicit non-responsibility
3. workflow input boundary
4. internal communication/value model
5. runtime resources/context
6. meaningful work/control-flow responsibilities
7. routing/termination model
8. deterministic authority placement
9. external effect boundary
10. final output / comparison projection
11. test/observability strategy
12. deliberately deferred LangGraph features
13. serious fallback/reassessment trigger, especially Functional API if Graph API ceremony dominates
14. long-horizon fit: which credible larger-system pressures the chosen boundaries anticipate without implementing them now
15. framework-value hypothesis: what orchestration/runtime burden LangGraph must demonstrably reduce to remain a serious product candidate
```

If Graph API is selected, this includes graph state/schema and node/edge design. If Functional API is selected, it instead includes the relevant entrypoint/task/local-value boundaries.

The freeze must not require identical ordinary-Python classes or topology.

**Pass:** a competent engineer could implement the selected LangGraph design without needing to reinterpret the comparison objective, silently inherit Python-specific structure, re-decide the API paradigm, or optimize solely for the current one-action slice.

---

## 10. Build preflight

After architecture freeze, hand off to Build/Implement.

Before source mutation:

- inspect experiment dependency configuration and current lock state;
- establish the smallest LangGraph dependency change actually needed;
- keep framework experiment code under `experiments/` / `experiments/tests/`;
- confirm product runtime imports do not depend on experiment code;
- do not add LangChain merely because LangGraph is used unless packaging/API reality makes that unavoidable and the consequence is understood;
- identify the narrow existing product/domain callables the LangGraph implementation will reuse;
- confirm the selected API paradigm and exact framework version/API surface against the installed/current dependency before coding.

---

## 11. Implementation boundary

Implement the smallest complete LangGraph architecture selected by the design gate.

Do not pre-authorize any mapping from historical ordinary-Python steps to Graph API topology.

The implementation may use new experiment-owned LangGraph-specific communication/types when they genuinely improve the selected design. It may also reuse an existing experiment type when independent reasoning shows that reuse is the simplest correct representation.

Either way:

```text
one source of accepted product/domain truth
+ one LangGraph orchestration design
```

not:

```text
Python semantics copied into a second LangGraph semantic implementation
```

Do **not** implement both Graph API and Functional API merely to complete a checklist. Reopen a second LangGraph implementation only if the first implementation leaves framework value ambiguous because API ceremony itself is the discriminating uncertainty.

The implementation remains deliberately smaller than the architectural horizon. Do not add persistence, human-in-the-loop interruption, subgraphs, or parallelism merely because they are part of LangGraph's future value proposition; preserve boundaries that allow those capabilities to remain plausible without paying their implementation cost now.

---

## 12. Framework-neutral comparison proof

### Controlled inputs

For semantic comparison, hold nondeterministic/external inputs constant where practical:

- same bounded starting case/knowledge;
- same model-visible responsibility/context at the semantic level;
- same controlled model decision/result when isolating orchestration;
- same current trusted execution conditions;
- same controlled repository/domain result or operational failure.

Internal input objects do not have to be identical when each implementation has a different representation. Build explicit adapters/projections for the **test comparison only** when necessary.

### Observable semantic projection

Define a small comparison projection/result for each scenario rather than asserting internal-state object equality.

Depending on the scenario, compare:

```text
planner/no-action/action outcome class
action identity selected/executed
whether current deterministic authority accepted/rejected execution
whether repository/external execution occurred
remaining investigation budget consequence
consumed-action consequence
final domain/applicability knowledge state
expected semantic result vs operational failure classification
continuation/stopping consequence
external call counts / forbidden calls
reproducible semantic consequence without model/repository re-execution when applicable
```

The comparison projection is evidence machinery, not a new product state model.

### Required bounded scenario family

At minimum preserve coverage for:

1. model invocation / structured-output problem;
2. each accepted no-action decision kind;
3. selected action rejected by current deterministic authority;
4. admitted action + valid semantic target declaration/result;
5. admitted action + typed target/domain problem that is still valid semantic evidence;
6. admitted action + expected operational acquisition/provider failure;
7. consumed/stale/budget/precondition authority cases needed to prove no forbidden execution;
8. unexpected programmer/framework defect remains distinguishable;
9. semantic consequence/reconstruction or equivalent deterministic proof without silently re-running model/GitHub I/O.

The exact LangGraph path/internal values may differ from the ordinary-Python control and may differ by LangGraph API paradigm.

### Proof limit

Passing controlled semantic comparison proves bounded responsibility equivalence for the exercised cases. It does not prove broad planner semantic quality, product reliability, multi-action generality, API-paradigm superiority, or framework adoption value.

---

## 13. Real pydantic Python-support LangGraph smoke

After deterministic comparison is green, run one bounded real LangGraph flow using `pydantic/pydantic` pull request `#13432`, comparable in responsibility to the real ordinary-Python smoke.

Use actual current product-owned evidence/capabilities rather than reconstructing fake planner facts when the live path requires those owners.

Record:

- workflow input boundary;
- model decision/output;
- deterministic authority result;
- exact external acquisition if executed;
- final semantic/domain outcome;
- relevant framework trace/observability evidence;
- framework/API-specific friction or benefit;
- proof limit.

Do not convert one green pydantic run into product reliability or framework superiority.

---

## 14. LangGraph framework value/cost findings for the later cross-implementation comparison

Capture evidence under dimensions such as:

```text
responsibility clarity
workflow-communication/state clarity
routing/control-flow clarity
trust/authority clarity
failure-model clarity
external-effect isolation
testability
observability/debuggability
semantic proof ergonomics
boilerplate/state or task plumbing
dependency/framework cost
learning/maintenance burden
change/locality characteristics
credible future multi-action/multi-agent/multi-turn growth fitness
durable execution/recovery fit
interrupt/human-in-the-loop fit where product trajectory makes it credible
workflow composition/subgraph/parallel growth fit where credible
provider/model integration friction
selected API-paradigm fit
```

Also record which ordinary-Python mechanisms:

```text
were independently rediscovered
were unnecessary in LangGraph
were replaced by a cleaner framework mechanism
remained better as ordinary product/domain code
revealed a weakness in one or both designs
```

The later cross-implementation comparison should compare the strongest competent versions, not score one implementation by how closely it resembles the other.

The comparison must distinguish:

```text
CURRENTLY EXERCISED VALUE
→ demonstrated by the bounded LangGraph implementation/tests/runtime evidence

CREDIBLE ARCHITECTURAL VALUE
→ framework capabilities relevant to the intended larger system but not yet exercised

SPECULATIVE VALUE
→ imagined future features without a concrete product trajectory or responsibility
```

Only the first two may materially support the later architecture decision, and they must not be conflated.

---

## 15. Learning/ownership expectations

Before Build, Ali should be able to explain proportionately:

- the difference between shared semantic requirements and ordinary-Python implementation choices;
- why ordinary Python is evidence/reference rather than LangGraph architectural authority;
- the difference between LangGraph Graph API and Functional API for this real responsibility;
- why the selected API paradigm currently wins and what evidence would reopen the alternative;
- what workflow communication, runtime context, routing/control flow, and output do in the selected design;
- where execution authority resides and why;
- what framework-specific structure LangGraph adds;
- what meaningful orchestration/runtime burden LangGraph could remove compared with ordinary Python;
- why small implementation slices should not force a small architectural horizon;
- what product/domain responsibilities remain ordinary owners rather than framework-owned semantics;
- how the comparison can be valid even when internal state/types/control flow differ;
- what the selected proof establishes and does not establish.

Exact API syntax may remain lookup-assisted until repeated use makes deeper fluency useful.

---

## 16. Explicitly deferred framework surface

The following features remain deferred from **current implementation/deep study** until a real trigger appears. They are not erased from architectural/value evaluation when the credible product trajectory makes them relevant.

```text
persistent checkpointing / durable workflow history
interrupts / human-in-the-loop
automatic retries / generalized error-handler policy
custom reducers beyond a real state-merge need
ToolNode / generic model-tool loop
create_agent
subgraphs
parallel fan-out / Send
automatic multi-turn back-edge
persistent Store / cross-thread memory
advanced streaming
LangSmith as required correctness proof
product-runtime integration
```

Also do not build a second LangGraph API implementation by default.

Reopen a Functional-vs-Graph second implementation only if:

- the first implementation's ceremony dominates the evaluation;
- the later cross-implementation comparison cannot determine LangGraph value without the lower/higher-structure alternative; or
- implementation friction directly suggests the API choice could reverse the conclusion.

---

## 17. Ordered semantic sequence

### Correct the comparison boundary

**Output:** corrected bounded plan, corrected LangGraph learning route, reconciled live memory, fresh active working memory.

**Pass:** no live owner treats ordinary-Python experiment structure as mandatory LangGraph architecture.

### Classify framework-neutral requirements and reusable capabilities

Classify the important ordinary-Python concepts using the classification gate in this plan.

**Pass:** requirements, reusable product capabilities, lessons/evidence, and Python-specific implementation choices are sufficiently separated.

### Decide between LangGraph Graph API and Functional API

Learn the API-paradigm comparison against current official framework documentation and the real UpgradePilot responsibility/credible trajectory.

**Pass:** Ali can explain Graph API vs Functional API trade-offs, what LangGraph must add beyond ordinary Python, and identify what evidence justifies the leading first-implementation paradigm without using current graph size as the sole criterion.

### Learn only the selected paradigm's decision-critical mechanics

Learn only the mechanics needed by the leading/selected API paradigm.

**Pass:** Ali can reason about the selected workflow design without inheriting ordinary-Python topology, unnecessary framework machinery, or a falsely narrow architectural horizon.

### Independently design and freeze the LangGraph architecture

Derive and record the architecture described in the architecture-freeze gate.

**Pass:** Build inputs are unambiguous, including API paradigm, long-horizon fit, framework-value hypothesis, and reassessment trigger.

### Establish the experiment dependency boundary

Perform the build preflight under Build/Implement.

### Implement the smallest complete LangGraph experiment

Use the implementation boundary in this plan.

### Prove framework-neutral semantic equivalence on controlled scenarios

Use the framework-neutral comparison proof before live model/provider proof.

### Run the real pydantic Python-support LangGraph smoke

Use the real public pydantic dependency-upgrade case and the smoke requirements above.

### Record LangGraph framework value/cost findings

Use the framework-value section and update only the appropriate evidence/live owners.

---

## 18. Pass condition

The bounded LangGraph responsibility passes when:

```text
same bounded responsibility is implemented competently in LangGraph
+ accepted framework-independent semantics are preserved on the required controlled cases
+ architecture is genuinely LangGraph-derived rather than a mechanical ordinary-Python translation
+ API paradigm was selected proportionately rather than assumed
+ bounded first-slice implementation did not become the sole architectural horizon
+ LangGraph framework value is assessed as burden reduction/runtime leverage, not mere graph-shaped Python branching
+ real pydantic Python-support smoke is inspected when available
+ framework value/cost evidence is recorded
+ learning ownership is sufficient for the decisions made
+ comparison evidence is ready for the bounded LangChain abstraction investigation and later cross-implementation comparison without product-adoption overclaim
```

---

## 19. Stop lines / prohibited scope

Do not:

- integrate LangGraph into product runtime during this bounded experiment;
- fabricate a second action merely to make orchestration richer;
- begin automatic multi-turn planning;
- treat ordinary-Python experiment classes/topology as mandatory LangGraph architecture;
- assume StateGraph/shared state is mandatory before the Graph-vs-Functional decision;
- duplicate established product/domain semantics to create artificial framework independence;
- require identical internal state, trace, task, or control-flow objects across implementations;
- add persistence/human-in-the-loop/retry/subgraph/parallel machinery without a real implementation trigger;
- ignore credible durable/multi-agent/orchestration trajectory merely because those features are not implemented in the first slice;
- choose or reject an API solely because the first experiment is small;
- implement both LangGraph APIs merely for exposure;
- use LangChain `create_agent` to consume the later bounded LangChain comparison prematurely;
- claim LangGraph adoption, superiority, production reliability, or broad planner quality from the bounded experiment.

Stop Planning/Design once the independent LangGraph architecture is unambiguous enough for Build. Stop the LangGraph bounded experiment once implementation/proof/comparison evidence is sufficient for the next authorized responsibility.

---

## 20. Provenance

This revision is informed by:

- the completed ordinary-Python control and its working-memory/test/runtime evidence;
- the historical 2026-09-02 non-controlling LangGraph research/design proposal;
- the corrected 2026-09-03 non-controlling independent LangGraph research/design proposal;
- the initial bounded LangGraph plan and learning-depth route;
- the subsequent Learning-by-Doing challenge that identified implementation-retention bias;
- the later proposal review that identified residual Graph-API-first learning bias;
- the 2026-09-04 Learning-by-Doing review that separated generic Python-capable orchestration concepts from LangGraph-specific runtime leverage and established **bounded implementation scope != bounded architectural horizon**;
- historical record `../working-memory/2026-09-03_1804_B2-X1-R4B-comparison-boundary-reframe.md`.

Exact historical filenames retain their old codes only as provenance.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`
