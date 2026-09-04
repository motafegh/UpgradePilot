# B2/X1 R4-B — Graph API Architecture Freeze and Build Entry

**Date/time:** 2026-09-04 19:04 (+03:30)  
**Session status:** ACTIVE  
**Primary responsibility/mode:** R4-B LangGraph experiment / Learning-by-Doing + Build/Implement  
**Previous active reasoning:** `2026-09-03_1804_B2-X1-R4B-comparison-boundary-reframe.md`  
**Related bounded plan:** `../plans/B2_X1_R4B_LANGGRAPH_LBD_IMPLEMENTATION_AND_COMPARISON_PLAN.md`  
**Learning-depth owner:** `../plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`  
**Corrected research evidence:** `../proposals/2026-09-03_B2_X1_R4B_CORRECTED_LANGGRAPH_INDEPENDENT_RESEARCH_AND_DESIGN_PROPOSAL.md`  
**Product runtime integration:** not authorized

## 1. Operation boundary

The R4-B Planning/Design learning gate is complete enough for Build. The first LangGraph architecture is now frozen at the level required to implement and test it without continuing detached conceptual design.

The first implementation remains deliberately bounded, while architecture is judged against the credible larger UpgradePilot direction:

```text
BUILD SMALL
→ smallest real evidence-producing LangGraph slice

THINK AT PRODUCT HORIZON
→ more agent/orchestration responsibilities, richer branching, durable recovery, possible human approval/interrupts, stronger runtime observability

DO NOT SPECULATE
→ do not pre-build persistence/HITL/subgraphs/parallelism/multi-turn merely because they may later matter
```

LangGraph must earn itself by reducing meaningful orchestration/runtime burden or improving architectural leverage. Re-expressing ordinary Python `if` statements and state with framework syntax is not sufficient value.

## 2. API-paradigm decision

**Selected for first implementation:** LangGraph **Graph API / `StateGraph`**.

Why it wins this first implementation:

- R4-A exposed real planning → current authority → external effect → deterministic consequence boundaries;
- those boundaries are materially useful to make executable/inspectable rather than merely procedural;
- the intended larger UpgradePilot trajectory makes explicit topology/control-flow and LangGraph runtime leverage a meaningful hypothesis to test;
- the first graph can stay small without committing to speculative future machinery.

**Serious fallback:** Functional API remains live as a reassessment option if Graph API state/topology plumbing materially dominates, obscures the responsibility, creates many invalid combinations, or fails to provide useful orchestration/debugging leverage beyond plain Python.

This is an experiment architecture decision, not product-runtime adoption.

## 3. Routing decision

Use one routing mechanism per source node.

```text
START
  ↓ static
PLAN
  ├─ Command → AUTHORIZE   [action proposal]
  └─ Command → CONCLUDE    [no-action/provider problem]

AUTHORIZE
  ├─ Command → INVESTIGATE [authorized]
  └─ Command → CONCLUDE    [rejected]

INVESTIGATE
  ↓ static
CONCLUDE
  ↓ static
END
```

`Command` is selected for `PLAN` and `AUTHORIZE` because each node both:

1. establishes a new workflow outcome/state value; and
2. that exact newly established outcome determines the next responsibility.

A separate conditional router would currently reread/reclassify the value the node just produced without adding independent policy or proof value. If future routing policy becomes independently owned, shared across nodes/agents, or materially more complex than the producing node's outcome, extract a conditional router then.

Do not add an unconditional static outgoing edge from `PLAN` or `AUTHORIZE` alongside `Command` routing.

Routing remains distinct from authority: `PLAN → AUTHORIZE` only selects the authority responsibility; only `AUTHORIZE` can establish executable authority.

## 4. Frozen first architecture

### 4.1 Responsibility

One bounded `EvidenceGapPlanner` workflow turn:

```text
trusted starting product/evidence state
→ bounded model planning
→ sufficiently current deterministic authorization when an action is proposed
→ at most one admitted external investigation
→ pure deterministic final consequence
→ normalized R4-B result
```

### 4.2 Explicit non-responsibility

The first implementation does not own:

- automatic multi-turn planning;
- fabricated second action;
- persistence/checkpointing/time travel;
- interrupts/HITL;
- generalized retries/caching;
- parallel fan-out / `Send`;
- subgraphs;
- persistent Store/cross-thread memory;
- LangChain `create_agent` / ToolNode lifecycle;
- product runtime integration.

### 4.3 Graph input

Use a small trusted start-input value sufficient to derive the bounded planner observation and later current authority. It should represent/reference:

- real product investigation/candidate evidence state;
- bounded planning question;
- trusted consumed-action history;
- bounded investigation budget;
- current offered action semantics/selection required by this responsibility.

The caller is not required to construct R4-A's `EvidenceGapPlannerContext` as the graph's public input.

### 4.4 Internal Graph State

Use a small experiment-owned communication envelope, conceptually:

```text
start_input
planner_outcome
execution_authority_outcome
investigation_outcome
final_result
```

Rules:

- `TypedDict` is the leading envelope form unless Build shows a clearer supported equivalent;
- use small immutable/discriminated values for stage outcomes;
- one writer per stage field;
- ordinary overwrite semantics;
- no custom reducers;
- do not store service/client objects in State;
- do not carry raw repository content beyond immediate interpretation;
- do not mirror product/domain fields into graph fields without a routing/proof reason;
- a value in State is not automatically fresh, trusted, authoritative, or model-visible.

### 4.5 Runtime context/resources

Run-scoped dependencies belong outside evolving Graph State. Current candidates:

```text
bounded model/provider dependency
current trusted authority-state supplier/composition capability
GitHubRepositoryClient or narrower exact repository acquisition capability
```

Runtime-context placement is dependency injection only; it does not grant trust or authority.

### 4.6 `PLAN`

Owns:

- build the exact bounded model-facing projection immediately before invocation;
- call the controlled model/provider boundary;
- produce a typed planner outcome: action proposal, explicit no-action kind, or expected provider/structured-output problem;
- return `Command` to `AUTHORIZE` or `CONCLUDE`.

The model controls proposal/semantic output only; it does not control exact source identity, execution parameters, mutation policy, or authority.

### 4.7 `AUTHORIZE`

Owns the current deterministic pre-effect authority boundary.

After an action proposal exists, obtain/derive sufficiently current trusted T2 conditions and decide one exact authority outcome:

- selected action still exists in the current trusted set;
- not already consumed;
- budget remains;
- source identity/revision remains current;
- policy admits the action;
- current proposition/preconditions still make it actionable;
- executable repository/revision/path/result authority comes from trusted code/data rather than model echo.

Produces authorized exact action/capability information or a typed rejection. Returns `Command` to `INVESTIGATE` or `CONCLUDE`.

Build may reuse the existing bounded R4-A admission function behind a narrow adapter if that best holds authority semantics constant without forcing R4-A state/topology into graph architecture. Do not prematurely extract a new shared product abstraction merely for comparison symmetry.

### 4.8 `INVESTIGATE`

The only admitted external repository effect in the first slice.

It must:

- run only from an authorized outcome;
- execute the exact admitted read through the established product acquisition owner;
- immediately use established target/domain interpretation owners;
- produce either valid semantic observation/evidence or an expected operational/acquisition failure;
- let unexpected programmer/framework defects surface rather than normalize them as semantic outcomes.

Then follow the static edge to `CONCLUDE`.

### 4.9 `CONCLUDE`

Pure deterministic consequence stage. It must not call the model or GitHub.

It normalizes the final R4-B semantic result for:

- explicit no-action;
- model/provider problem;
- authority rejection;
- authorized semantic result;
- expected operational failure.

It owns the bounded budget/action-consumption/continuation consequence and product-domain update from already-valid semantic evidence. The exact final type is experiment-owned and smaller than the full internal graph state.

The pure boundary also supplies deterministic semantic reconstruction/proof without re-running model or repository I/O.

## 5. Proof strategy

First proof is controlled and framework-neutral, not a live model run.

Required evidence includes:

- graph compiles and invokes through intended routes;
- each no-action/provider-problem route skips authority/effect as appropriate;
- rejected/stale/consumed/budget/precondition cases cannot call the repository effect;
- authorized action reaches exactly one admitted external effect;
- semantic/domain result remains distinct from expected operational failure and unexpected defect;
- budget/consumption/continuation consequences match accepted semantics;
- final semantic consequence can be reconstructed/tested without model/GitHub re-execution;
- graph topology/trace/stream information is supporting observability evidence, not the semantic oracle.

After deterministic comparison is green, run the bounded real S001 smoke.

## 6. Framework-value hypothesis for R4-D

Evaluate separately:

```text
CURRENTLY EXERCISED VALUE
→ executable topology
→ explicit authority/effect routing
→ workflow state/context separation
→ tracing/stream/debug ergonomics actually observed during implementation/tests

CREDIBLE ARCHITECTURAL VALUE
→ durable execution/recovery
→ interrupt/resume/HITL
→ richer composition/branching/subgraphs
→ future multi-agent orchestration/runtime observability

SPECULATIVE VALUE
→ future mechanisms with no credible UpgradePilot responsibility
```

Do not score unexercised future capabilities as if R4-B proved them.

## 7. Build preflight started

Build/Implement procedure loaded.

Current repository facts:

- `pyproject.toml` currently declares `requests`, `packaging`, and `PyYAML`; no LangGraph dependency is declared;
- repository code search found no current `langgraph` usage;
- experiment tests already live under `experiments/tests/` and include the R4-A planner/admission/composition/model/transition families;
- R4-B source/test/dependency mutation is now authorized only inside the bounded experiment plan;
- product runtime integration remains prohibited.

## 8. Immediate Build route

```text
CURRENT — R4-B4
→ inspect lock/dependency state and exact current LangGraph package/API version
→ inspect only the R4-A/product source + tests needed for controlled reuse/proof
→ decide the smallest explicit LangGraph dependency change

THEN — R4-B5
→ first source increment: graph-owned input/state/context/outcome skeleton + compile/invoke proof
→ PLAN routing
→ AUTHORIZE boundary
→ INVESTIGATE effect
→ CONCLUDE pure consequence

THEN
→ R4-B6 controlled semantic comparison
→ R4-B7 real S001 smoke
→ R4-B8 value/cost findings for R4-D
```

Learning now moves primarily into implementation: exact `StateGraph`, `Command`, `Runtime`, typing, compile/invoke, testing, and observability mechanics are learned when the code first uses them.

## 9. Stop lines

Do not:

- integrate LangGraph into product runtime;
- add LangChain/create_agent merely because LangGraph is added;
- pre-build persistence/HITL/retry/subgraph/parallel/multi-turn machinery;
- manufacture a second action;
- duplicate established product/domain truth;
- claim framework superiority/adoption from the bounded experiment.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-build-implement`
