# LangGraph Framework Value / Cost Findings

**Date/time:** 2026-09-06 18:10 +03:30  
**Session status:** CLOSED  
**Primary responsibility/mode:** Review/Evaluation + Learning-by-Doing  
**Related plan:** `../plans/LANGGRAPH_BOUNDED_EVIDENCE_GAP_PLANNER_INDEPENDENT_DESIGN_IMPLEMENTATION_AND_COMPARISON_PLAN.md`  
**Previous:** `2026-09-06_1752_real-s001-langgraph-executable-proof.md`

## 1. Evaluation anchor

The first bounded LangGraph implementation is now proven at three useful levels:

```text
focused native graph/adapter tests
→ 7/7 PASS before semantic rename

post-rename focused semantic family
→ 58/58 PASS

controlled ordinary-Python vs LangGraph semantic comparison
→ 4/4 PASS

real S001 LangGraph smoke
→ PASS
→ real model proposal
→ deterministic authority
→ exact GitHub target read
→ deterministic semantic conclusion
→ graph target/final assessment matches normal product path
```

The responsibility here is not to adopt or reject LangGraph. It is to record what the strongest current Graph API experiment actually bought and cost so the later ordinary-Python / LangGraph / LangChain comparison can use evidence rather than framework preference.

## 2. Currently exercised value

### Explicit executable topology — real positive value

The graph makes the meaningful control-flow responsibilities directly executable and inspectable:

```text
PLAN
→ AUTHORIZE
→ INVESTIGATE
→ CONCLUDE
```

Dynamic routing from PLAN and AUTHORIZE is represented through `Command`; unconditional progression uses static edges. This is not merely documentation: the real S001 smoke observed exactly `plan -> authorize -> investigate -> conclude` through LangGraph's updates stream.

This is a meaningful improvement in workflow visibility relative to ordinary Python because the orchestration topology is a first-class runtime construct rather than being recovered from nested function/branch execution.

### Runtime observability — real positive value

`stream_mode="updates"` exposed the node-by-node runtime path without adding a custom tracing system. This gave direct proof of which responsibilities executed in the real smoke.

The exercised value is currently modest but concrete: workflow-stage visibility came from the framework rather than a new UpgradePilot trace mechanism.

### Workflow state/context separation — useful but mixed

LangGraph gave a natural place to separate:

```text
Graph State
→ evolving workflow communication/results

Runtime Context
→ planner, authority supplier, authority evaluator, repository reader
```

This made dependency injection and workflow communication explicit. It was especially useful for controlled tests and the real smoke.

However, this benefit came with additional graph-owned state/result/port types. The conceptual separation is good; the amount of representation plumbing is a real cost in this small one-action slice.

### Routing / effect isolation — useful, but not uniquely framework-owned

The graph cleanly isolates:

```text
model proposal
!= deterministic authority
!= external effect
!= deterministic semantic conclusion
```

This boundary survived the real S001 run and is architecturally valuable.

But the important trust semantics were not created by LangGraph. The same proposal/authority/effect/conclusion separation had already been discovered and proven in the ordinary-Python control. LangGraph made the stages more explicit as workflow topology; it did not remove the need for those rules.

### Testing ergonomics — positive for orchestration, neutral for domain semantics

The graph's runtime context made it straightforward to inject controlled planner, authority, and repository capabilities and assert forbidden effects on no-action/rejection paths.

The controlled semantic comparison also showed that LangGraph can preserve the same accepted consequences without sharing ordinary-Python internals.

However, semantic proof still required framework-neutral projection and ordinary deterministic domain functions. LangGraph did not replace that proof work.

## 3. What LangGraph did not replace

The experiment shows clearly that the difficult UpgradePilot responsibilities remain ordinary code:

```text
model-visible context projection
structured model-output contract
current deterministic admission/authority semantics
exact repository identity and acquisition rules
target Python interpretation
target relevance evaluation
Python-support impact semantics
failure classification meaning
semantic comparison / proof boundary
```

These should remain ordinary product/domain or bounded experiment owners even if LangGraph is later adopted. Moving them into framework-specific nodes/tools merely for architectural uniformity would weaken ownership rather than improve it.

## 4. Current cost / friction

### Representation/state plumbing — material current cost

The Graph API implementation owns more workflow-specific types and schemas than the ordinary-Python transition path:

- start input;
- planner outcome variants;
- baseline;
- authority snapshot;
- authority result variants;
- operational failure;
- final result;
- planner/authority/repository protocols;
- runtime context;
- input/state/output schemas.

This structure is coherent and successfully protected the R4-B architecture from R4-A representation coupling, but it is real ceremony for the current one-action workflow.

### Comparison adapters — real experiment cost, not necessarily product cost

Because R4-B intentionally held proven planner/admission behavior constant, the experiment needs explicit ordinary-Python-to-LangGraph adapters. These were necessary for a fair comparison, but they are evaluation scaffolding rather than evidence that a future product implementation would need the same adapters.

Do not charge all adapter cost permanently against LangGraph product adoption; do count it as current experiment complexity and maintenance burden.

### Dependency/framework surface — real cost

LangGraph adds a dedicated experiment dependency and framework API surface (`StateGraph`, `Runtime`, `Command`, streaming semantics, schemas). This creates learning, upgrade, compatibility, and maintenance cost that plain Python does not have.

No currently exercised feature has yet demonstrated that this dependency removes an equivalent amount of custom runtime infrastructure.

### Change locality — mixed

A new orchestration stage or branch can become visually/locality clearer in the graph topology, but adding new workflow communication may require edits across state types, node contracts, routing, final result/projection, tests, and adapters.

For the present small workflow, ordinary Python remains locally cheaper. LangGraph's locality advantage is more credible when branching/composition pressure grows.

## 5. Ordinary-Python mechanisms independently rediscovered / retained

### Independently rediscovered because they are real requirements

These appeared in both implementations because the responsibility requires them, not because LangGraph copied Python:

```text
bounded model observation
deterministic post-model authority
semantic vs operational failure distinction
budget and consumed-action consequences
exact external-effect isolation
pure deterministic final consequence
```

### Better left as ordinary product/domain code

```text
GitHub repository acquisition
TargetPythonDeclaration interpretation
target relevance
Python-support impact evaluation
trusted proposition/product state
```

LangGraph should orchestrate these owners, not absorb them.

### Ordinary-Python trace/replay remains a stronger exercised proof asset today

The ordinary-Python control has an explicit immutable `EvidenceGapTransitionTrace` plus deterministic replay that reconstructs after-state without LM Studio/GitHub re-execution.

The current LangGraph experiment has final-result reconstruction and runtime update visibility, but we did not implement framework persistence/checkpoint/replay. Therefore LangGraph has not yet replaced the ordinary-Python trace/replay proof advantage.

This is not a defect requiring immediate framework persistence work; persistence/recovery remains deferred until a real responsibility needs it.

## 6. Credible architectural value not yet exercised

The intended UpgradePilot trajectory makes the following LangGraph capabilities credible future value rather than random feature speculation:

```text
richer explicit branching as investigation/action families grow
workflow composition when several agent/investigation responsibilities become independently admitted
durable execution / checkpoint / recovery if long-running orchestration becomes real
interrupt / HITL boundaries if human approval becomes a real product responsibility
stronger runtime tracing/inspection across multi-stage agent workflows
subgraph / parallel composition if independent branches later justify them
```

These may materially reduce UpgradePilot-owned orchestration infrastructure later, but current R4-B evidence has not exercised them. They must remain classified as architectural value, not current proof.

## 7. Speculative value to exclude from decision weight

Do not award LangGraph adoption credit today for:

```text
generic multi-agent swarms
automatic parallelism with no admitted independent branches
persistent memory with no product responsibility
multi-turn looping merely because the framework supports it
generic tool loops / ToolNode without a real capability set
HITL without an actual approval/interrupt requirement
```

These are possible framework features, not UpgradePilot evidence.

## 8. Graph API vs Functional API reassessment

Graph API ceremony is now an observed cost, but it has not dominated the experiment enough to justify building a second Functional API implementation.

Evidence supporting the current Graph API choice:

- the planning / authority / effect / conclusion boundaries are materially meaningful;
- explicit topology was visible in the real S001 runtime;
- runtime updates provided concrete stage observability;
- controlled tests benefited from explicit node/runtime-context boundaries;
- the design remains credible for richer branching/orchestration pressure.

Evidence against declaring Graph API an obvious winner:

- state/result/port representation plumbing is substantial for one action;
- ordinary Python remains simpler for the current bounded workflow;
- LangGraph has not yet exercised persistence/recovery/HITL/composition advantages;
- current semantic correctness depended primarily on ordinary deterministic/product owners rather than framework machinery.

Disposition for the API-paradigm gate:

```text
KEEP GRAPH API AS THE TESTED LANGGRAPH CANDIDATE
DO NOT BUILD FUNCTIONAL API NOW
REOPEN ONLY IF LATER R4-D COMPARISON CANNOT JUDGE LANGGRAPH FAIRLY BECAUSE GRAPH-API CEREMONY ITSELF REMAINS THE MATERIAL UNCERTAINTY
```

## 9. Current LangGraph disposition for later R4-D

Current evidence supports:

```text
VIABLE / SERIOUS CANDIDATE
+ real orchestration-topology and observability value
+ preserved accepted semantics
+ real S001 proof
- meaningful current state/type/dependency ceremony
- no demonstrated replacement yet for ordinary-Python replay or broader runtime infrastructure
```

Therefore:

- do not adopt LangGraph into product runtime yet;
- do not reject LangGraph;
- do not expand the Graph API experiment merely to demonstrate more features;
- carry these findings into the later R4-D implementation comparison;
- proceed to the bounded LangChain learning/integration slice required by the parent plan.

## 10. Handoff

LangGraph value/cost findings are sufficiently complete for the current bounded implementation. The next selected responsibility is the parent plan's **R4-C LangChain bounded learning/integration slice**.

That next slice should inspect only LangChain abstractions that materially intersect this same responsibility—model abstraction, agent/tool loop, tools, middleware/lifecycle hooks, and its relationship to LangGraph—and must not force the EvidenceGapPlanner into a generic tool-calling agent architecture merely for framework exposure.

Product runtime integration remains unauthorized.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
