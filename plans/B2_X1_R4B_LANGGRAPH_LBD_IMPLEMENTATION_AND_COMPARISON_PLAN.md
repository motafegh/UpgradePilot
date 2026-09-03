# B2/X1 R4-B LangGraph Learning-by-Doing Implementation and Comparison Plan

**Status:** AUTHORIZED BOUNDED PLAN ARTIFACT — subordinate to the selected B2/X1 post-research planner plan; position-neutral; `MEMORY.md` alone owns live continuation  
**Date:** 2026-09-03  
**Revision:** corrected comparison boundary after R4-B Learning-by-Doing design review  
**Parent plan:** `B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**Learning-depth owner:** `B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`  
**Research/design evidence:** `../proposals/2026-09-02_B2_X1_R4B_LANGGRAPH_RESEARCH_AND_DESIGN_PROPOSAL.md`  
**Current correction provenance:** `../working-memory/2026-09-03_1804_B2-X1-R4B-comparison-boundary-reframe.md`  
**Responsibility:** independently design, learn, implement, prove, and compare the smallest credible LangGraph implementation of the same bounded `EvidenceGapPlanner` responsibility already explored in ordinary Python, while preserving accepted UpgradePilot semantics and allowing LangGraph to use an architecture natural to its own execution model  
**Product runtime integration:** NOT authorized

---

## 1. Why this plan exists

R4-A produced a coherent ordinary-Python reference/control. That implementation is valuable because it exposed real engineering responsibilities, failure modes, authority boundaries, and testable semantics before framework adoption was considered.

R4-B exists to answer a different question:

> **If the same bounded UpgradePilot responsibility is designed competently with LangGraph rather than ordinary Python orchestration, what architecture results, what does LangGraph materially improve or worsen, and what should that teach the eventual production architecture?**

A previous refinement of this plan over-preserved the R4-A implementation structure. It treated several experiment-owned Python representations and A-number boundaries as if LangGraph should mainly wrap or reproduce them. The Learning-by-Doing design review rejected that comparison method because it would bias R4-B toward measuring how well LangGraph can imitate the Python design rather than how well LangGraph can implement the same responsibility.

This revised plan therefore enforces two simultaneous disciplines:

```text
SEMANTIC DISCIPLINE
→ accepted UpgradePilot behavior, trust, authority, failure, evidence, and investigation rules remain controlling

ARCHITECTURAL INDEPENDENCE
→ R4-A implementation structure is evidence/reference, not automatic R4-B architecture authority
```

The correction is consistent with the project-wide retention rule:

```text
existing implementation
= evidence to inspect
!= authority to preserve unchanged
```

---

## 2. Owner split and authority

### Broader route / authorization

`B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`

Owns the broader R4-A → R4-B → R4-C → R4-D experiment/comparison route and later disposition.

### Stable framework-independent semantics

Use the applicable accepted owners rather than re-specifying them here:

- `../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`
- `../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`
- `../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`
- `../docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`

These own accepted trust/evidence/failure/authority/investigation/generalization semantics. They do not select LangGraph or dictate its internal state/node structure.

### This plan

Owns the bounded R4-B route:

```text
comparison-boundary classification
→ decision-critical LangGraph learning
→ independent LangGraph architecture design
→ architecture freeze
→ smallest experiment implementation
→ controlled framework-neutral semantic proof
→ bounded real S001 smoke
→ LangGraph findings for R4-D
```

### Learning depth

`B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`

Owns what Ali should understand before architecture decisions, what should be learned when first used materially, and what remains deferred.

### R4-A evidence

R4-A source/tests/working memories are the ordinary-Python comparison reference and engineering evidence. They are not a second specification and do not automatically constrain R4-B representation.

### Research proposal

`../proposals/2026-09-02_B2_X1_R4B_LANGGRAPH_RESEARCH_AND_DESIGN_PROPOSAL.md`

Remains non-controlling research evidence. Some framework facts remain useful; architecture recommendations in that proposal must be re-evaluated under this corrected comparison boundary.

### Live continuation

`../MEMORY.md` alone selects the live step. The active dated working memory preserves detailed reasoning and handoff.

---

## 3. R4-A comparison role

R4-A remains a serious reference/control:

```text
ordinary-Python bounded EvidenceGapPlanner responsibility
→ model-visible projection and structured decision contract
→ local model invocation
→ deterministic pre-execution authority/admission
→ bounded execution / interpretation / state consequences
→ trace / replay proof
```

The current evidence horizon remains:

```text
A1 10/10 PASS
A2 13/13 PASS
A3 13/13 PASS
A4 7/7 PASS
combined focused family 47/47 PASS
real S001 model selection/admission PASS
real S001 execution/update/trace/replay PASS
```

Use R4-A in four ways:

1. **reference implementation** — a coherent ordinary-Python solution to inspect and compare;
2. **engineering evidence** — reveals real failure modes, trust/authority needs, state consequences, and operational friction;
3. **learning evidence** — explains why certain responsibilities appeared during implementation;
4. **comparison result** — supplies observed complexity, clarity, proof surface, and growth pressure.

Do **not** use R4-A as:

```text
mandatory LangGraph state schema
mandatory node decomposition
mandatory trace representation
mandatory class reuse boundary
mandatory A1/A2/A3/A4 topology
```

A LangGraph design may independently converge on similar boundaries. When it does, the justification must come from the responsibility and LangGraph design, not merely from Python precedent.

---

## 4. Central R4-B success question

Use:

> **Can a LangGraph-native implementation satisfy the same bounded UpgradePilot EvidenceGapPlanner responsibility and accepted framework-independent semantics while providing enough control-flow clarity, state/routing coherence, inspectability, test/debug leverage, and credible growth fitness to justify its dependency and framework machinery relative to the ordinary-Python reference?**

Evaluate at least three independent dimensions:

```text
SEMANTIC CORRECTNESS
→ does the implementation preserve the accepted product/trust/authority/failure/investigation behavior?

ARCHITECTURAL QUALITY
→ is the LangGraph design coherent on its own terms rather than a mechanical translation of R4-A?

FRAMEWORK VALUE
→ does LangGraph provide enough present or credible near-future value to pay for dependency, concepts, state plumbing, and failure surface?
```

A graph that merely compiles fails the evaluation. A graph that reproduces Python structure mechanically also provides weak evidence. A graph that is elegant but weakens accepted semantics fails regardless of framework convenience.

---

## 5. Common framework-neutral acceptance boundary

R4-B must preserve the applicable accepted responsibility, not identical implementation objects.

The controlled comparison should include these common properties where the scenario makes them relevant:

```text
bounded model observation
→ the model receives only justified decision context

model result
→ proposal / semantic output
!= automatic external execution authority

pre-execution authority
→ action execution occurs only when current trusted deterministic conditions permit it

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

These are comparison/acceptance concerns. Exact concrete representations remain design questions unless an accepted specification/ADR already owns them.

---

## 6. Classification gate before LangGraph architecture

Before deciding graph state, nodes, edges, or framework APIs, classify each material R4-A concept into one of four buckets.

### A. Accepted framework-independent requirement

Examples may include:

- a model cannot grant its own execution authority;
- evidence/authority/failure distinctions must remain intact;
- current trusted execution conditions matter at the pre-execution boundary;
- investigation stopping and no-action semantics must remain honest.

These constrain every implementation.

### B. Reusable product-owned capability

Examples may include established exact repository acquisition, target declaration interpretation, target relevance, Python-support impact evaluation, and other product/domain facts already owned outside the experiment.

Reuse these when the LangGraph implementation needs the same responsibility. Independent graph design is not permission to duplicate product truth.

### C. R4-A engineering lesson/evidence

Examples:

- why an authority check became necessary;
- why semantic and operational failure needed separation;
- where trace/replay became useful;
- what test or live failure exposed a real problem.

These should pressure the LangGraph design but do not dictate its form.

### D. R4-A/Python-specific implementation choice

Examples may include:

- exact dataclass shape;
- exact `EvidenceGapInvestigationState` representation;
- exact A1/A2/A3/A4 physical decomposition;
- exact `EvidenceGapTransitionTrace` structure;
- helper/function/module boundaries chosen for ordinary Python.

These are open to independent redesign unless another owner establishes an implementation-independent need.

**Pass for this gate:** the important common requirements and reusable product capabilities are sufficiently clear that LangGraph design can proceed without treating R4-A classes/topology as premises.

---

## 7. Independent LangGraph design principles

### 7.1 Start from workflow responsibility, not Python classes

Derive the graph by asking:

```text
what information must persist between meaningful workflow steps?
what work actually changes workflow/domain knowledge?
what decisions genuinely change control flow?
where are trusted/external effects performed?
what must remain outside model authority?
what result must the graph expose to callers/tests?
```

Then choose state, nodes, routing, runtime resources, and output representation.

### 7.2 Reuse product capabilities, not experiment scaffolding by default

When an established product/domain callable already performs the exact same admitted responsibility, use it rather than reimplementing its semantics solely to make the graph look native.

Conversely, do not reuse an R4-A experiment wrapper/type merely because it already exists if a simpler or more natural LangGraph representation satisfies the same responsibility.

### 7.3 Let LangGraph earn its structure

StateGraph, conditional edges, `Command`, runtime context, checkpointers, interrupts, reducers, subgraphs, ToolNode, and other framework machinery are candidates only when the real responsibility makes them useful.

Do not add framework machinery for exposure, trend, or architectural appearance.

### 7.4 Avoid fake independence

A LangGraph implementation that merely duplicates all existing domain logic under new names is not an independent architecture; it is semantic duplication.

Independent design means freedom in **orchestration/representation**, not freedom to fork accepted product truth.

---

## 8. Decision-critical Learning-by-Doing before architecture freeze

Learn only enough to make the independent design choices correctly.

Required practical concepts:

```text
StateGraph execution model
START / END
node work vs routing work
shared workflow state
partial state updates and overwrite/reducer implications
conditional edges
input schema vs internal state vs output schema
runtime context/resources vs persisted/shared workflow facts
expected typed workflow outcomes vs unexpected exceptions
compile/invoke execution boundary
framework tracing/stream visibility at practical level
checkpoint/replay semantics only enough to avoid confusing them with domain proof
```

Important design questions after those premises are understood:

```text
what should LangGraph state mean for this responsibility?
which facts should be state vs runtime resources vs derived values?
what are the meaningful nodes for a LangGraph-native flow?
where should model observation/projection occur?
where and how should deterministic execution authority be enforced?
what routing is truly dynamic?
what belongs in final graph output?
what domain/evidence capability should remain ordinary product code called from nodes?
what effect boundaries matter for retry/resume/checkpoint semantics even if those features remain deferred?
```

Do not ask Ali to choose APIs or graph topology before the necessary conceptual premises are established.

---

## 9. Architecture freeze gate

Freeze only what Build genuinely needs.

The architecture decision record in the active working memory should make these recoverable:

```text
1. graph responsibility and explicit non-responsibility
2. graph input boundary
3. internal workflow state model
4. runtime resources/context
5. meaningful node responsibilities
6. routing/termination model
7. deterministic authority placement
8. external effect boundary
9. final output / comparison projection
10. test/observability strategy
11. deliberately deferred LangGraph features
```

The freeze must not require identical R4-A classes or topology.

**Pass:** a competent engineer could implement the selected LangGraph design without needing to reinterpret the comparison objective or silently inherit Python-specific structure.

---

## 10. Build preflight

After architecture freeze, hand off to Build/Implement.

Before source mutation:

- inspect experiment dependency configuration and current lock state;
- establish the smallest LangGraph dependency change actually needed;
- keep framework experiment code under `experiments/` / `experiments/tests/`;
- confirm product runtime imports do not depend on experiment code;
- do not add LangChain simply because R4-B uses LangGraph unless packaging/API reality makes that unavoidable and the consequence is understood;
- identify the narrow existing product/domain callables the graph will reuse.

---

## 11. Implementation boundary

Implement the smallest complete LangGraph architecture selected by the design gate.

Do not pre-authorize any particular A-number mapping.

The implementation may use new experiment-owned LangGraph-specific types/state when they genuinely improve the graph design. It may also reuse an existing experiment type when independent reasoning shows that reuse is the simplest correct representation.

Either way:

```text
one source of accepted product/domain truth
+ one LangGraph orchestration design
```

not:

```text
Python semantics copied into a second LangGraph semantic implementation
```

---

## 12. Framework-neutral comparison proof

### 12.1 Controlled inputs

For semantic comparison, hold nondeterministic/external inputs constant where practical:

- same bounded starting case/knowledge;
- same model-visible responsibility/context at the semantic level;
- same controlled model decision/result when isolating orchestration;
- same current trusted execution conditions;
- same controlled repository/domain result or operational failure.

Internal input objects do not have to be identical when each implementation has a different representation. Build explicit adapters/projections for the **test comparison only** when necessary.

### 12.2 Observable semantic projection

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

### 12.3 Required bounded scenario family

At minimum preserve coverage for:

1. model invocation / structured-output problem;
2. each accepted no-action decision kind;
3. selected action rejected by current deterministic authority;
4. admitted action + valid semantic target declaration/result;
5. admitted action + typed target/domain problem that is still valid semantic evidence;
6. admitted action + expected operational acquisition/provider failure;
7. consumed/stale/budget/precondition authority cases needed to prove no forbidden execution;
8. semantic consequence/replay or equivalent deterministic proof without silently re-running model/GitHub I/O.

The exact LangGraph path and internal state for each scenario may differ from R4-A.

### 12.4 Proof limit

Passing controlled semantic comparison proves bounded responsibility equivalence for the exercised cases. It does not prove broad planner semantic quality, product reliability, multi-action generality, or framework adoption value.

---

## 13. Real S001 LangGraph smoke

After deterministic comparison is green, run one bounded real S001 LangGraph flow comparable in responsibility to the R4-A real smoke.

Use actual current product-owned evidence/capabilities rather than reconstructing fake planner facts when the live path requires those owners.

Record:

- graph input boundary;
- model decision/output;
- deterministic authority result;
- exact external acquisition if executed;
- final semantic/domain outcome;
- relevant graph trace/observability evidence;
- framework-specific friction or benefit;
- proof limit.

Do not convert one green S001 run into product reliability or framework superiority.

---

## 14. LangGraph comparison findings for R4-D

Capture evidence under dimensions such as:

```text
responsibility clarity
state-model clarity
routing/control-flow clarity
trust/authority clarity
failure-model clarity
external-effect isolation
testability
observability/debuggability
semantic proof ergonomics
boilerplate/state plumbing
dependency/framework cost
learning/maintenance burden
change/locality characteristics
credible future multi-action/multi-turn growth fitness
provider/model integration friction
```

Also record which R4-A mechanisms:

```text
were independently rediscovered
were unnecessary in LangGraph
were replaced by a cleaner framework mechanism
remained better as ordinary product/domain code
revealed a weakness in one or both designs
```

R4-D should compare the strongest competent versions, not score one implementation by how closely it resembles the other.

---

## 15. Learning/ownership expectations

Before Build, Ali should be able to explain proportionately:

- the difference between shared semantic requirements and R4-A implementation choices;
- why R4-A is evidence/reference rather than R4-B architectural authority;
- what LangGraph state/nodes/edges/context do in the selected design;
- where execution authority resides and why;
- what framework-specific structure LangGraph adds;
- what product/domain responsibilities remain outside or inside nodes without becoming framework-owned semantics;
- how the comparison can be valid even when internal state/types differ;
- what the selected proof establishes and does not establish.

Exact API syntax may remain lookup-assisted until repeated use makes deeper fluency useful.

---

## 16. Explicitly deferred framework surface

Remain deferred until a real trigger appears:

```text
persistent checkpointing / durable graph history
interrupts / HITL
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

Reopen only when the selected LangGraph architecture or later admitted product responsibility creates a concrete need.

---

## 17. Ordered R4-B sequence

### R4-B0 — comparison-boundary correction

**Output:** corrected bounded plan, corrected R4-B learning route, reconciled live memory, fresh active working memory.

**Pass:** no live owner treats R4-A experiment structure as mandatory LangGraph architecture.

### R4-B1 — framework-neutral responsibility classification

Classify the important R4-A concepts using §6.

**Pass:** requirements, reusable product capabilities, lessons/evidence, and Python-specific implementation choices are sufficiently separated.

### R4-B2 — decision-critical LangGraph learning

Learn the §8 concepts against current official framework documentation and the real UpgradePilot responsibility.

**Pass:** Ali can reason about graph design without inheriting R4-A topology by default.

### R4-B3 — independent LangGraph architecture design/freeze

Derive and record the architecture described in §9.

**Pass:** Build inputs are unambiguous.

### R4-B4 — Build preflight / dependency boundary

Perform §10 under Build/Implement.

### R4-B5 — implement smallest complete LangGraph experiment

Use §11.

### R4-B6 — deterministic framework-neutral semantic comparison

Use §12 before live model/provider proof.

### R4-B7 — bounded real S001 LangGraph smoke

Use §13.

### R4-B8 — LangGraph findings / R4-D handoff

Use §14 and update only the appropriate evidence/live owners.

---

## 18. Pass condition

R4-B passes when:

```text
same bounded responsibility is implemented competently in LangGraph
+ accepted framework-independent semantics are preserved on the required controlled cases
+ architecture is genuinely LangGraph-derived rather than a mechanical R4-A translation
+ real S001 bounded smoke is inspected when available
+ framework value/cost evidence is recorded
+ learning ownership is sufficient for the decisions made
+ comparison evidence is ready for R4-C/R4-D without product-adoption overclaim
```

---

## 19. Stop lines / prohibited scope

Do not:

- integrate LangGraph into product runtime during R4-B;
- fabricate a second action merely to make graph orchestration richer;
- begin automatic multi-turn planning;
- treat R4-A experiment classes/topology as mandatory LangGraph architecture;
- duplicate established product/domain semantics to create artificial framework independence;
- require identical internal state or trace objects across implementations;
- add persistence/HITL/retry/subgraph/parallel machinery without a real trigger;
- use LangChain `create_agent` to consume the later R4-C comparison prematurely;
- claim LangGraph adoption, superiority, production reliability, or broad planner quality from the bounded experiment.

Stop Planning/Design once the independent graph architecture is unambiguous enough for Build. Stop R4-B once the bounded implementation/proof/comparison evidence is sufficient for the next authorized route.

---

## 20. Provenance

This revision is informed by:

- the completed R4-A control and its working-memory/test/runtime evidence;
- the non-controlling LangGraph research/design proposal;
- the initial R4-B bounded plan and learning-depth route;
- the subsequent Learning-by-Doing challenge that identified implementation-retention bias;
- `../working-memory/2026-09-03_1804_B2-X1-R4B-comparison-boundary-reframe.md`.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`
