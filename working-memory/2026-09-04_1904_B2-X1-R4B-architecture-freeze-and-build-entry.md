# B2/X1 R4-B — Graph API Architecture Freeze and Build Entry

**Date/time:** 2026-09-04 19:04 (+03:30)  
**Last material update:** 2026-09-04 20:17 (+03:30)  
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

Build refinement after implementation preflight:

```text
authority_snapshot
→ also belongs in internal workflow communication for action branches
→ because CONCLUDE must apply consequences to the same fresh T2 baseline AUTHORIZE used
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

Run-scoped dependencies belong outside evolving Graph State. Current first implementation uses:

```text
bounded model/provider dependency
current trusted authority-snapshot supplier
exact repository-read capability
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

Build reuses the existing bounded R4-A deterministic admission function behind the graph node to hold authority semantics constant while testing orchestration. It does not reuse R4-A graph/state topology.

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

## 7. Build preflight and first implementation slice

Build/Implement and Learning-by-Doing procedures are active.

### Dependency boundary

`pyproject.toml` now declares:

```toml
[dependency-groups]
experiments = [
    "langgraph==1.2.11",
]
```

This is deliberate experiment-only dependency placement:

```text
R4-B may use LangGraph
!=
UpgradePilot product runtime depends on LangGraph
```

The normal `[project].dependencies` list remains unchanged. LangChain was not added, preserving the R4-B lower-level orchestration comparison and the later R4-C variable.

Commit:

`747149e6af3d4f5ed4c5823c159a6dbe62e6cd5f` — `Add LangGraph experiment dependency boundary`

No committed `uv.lock` exists in the current repository. A lockfile was not fabricated by hand; actual uv resolution/lock generation remains an executable WSL responsibility.

### First graph module

Added:

`experiments/b2_x1_evidence_gap_langgraph.py`

Commit:

`09b04ffbd8c9d031e8c3599c2c5a9bcb80a36df0` — `Implement first bounded LangGraph evidence-gap workflow`

The module currently contains:

- `EvidenceGapLangGraphStartInput` — caller-facing trusted turn input;
- `EvidenceGapLangGraphBaseline` — semantic consequence baseline;
- `EvidenceGapLangGraphAuthoritySnapshot` — coherent T2 admission state + consequence baseline;
- `EvidenceGapLangGraphRuntimeContext` — planner, fresh authority snapshot supplier, repository reader;
- `EvidenceGapLangGraphState` — graph communication channels;
- `EvidenceGapLangGraphResult` — normalized bounded output;
- `plan_evidence_gap` — T1 projection/provider + `Command` routing;
- `authorize_evidence_gap` — fresh T2 snapshot + deterministic admission + `Command` routing;
- `investigate_evidence_gap` — exact admitted read + immediate product-owned interpretation;
- `conclude_evidence_gap` / `derive_evidence_gap_langgraph_result` — pure deterministic consequence;
- `build_evidence_gap_langgraph` — `StateGraph` builder/compile boundary.

The graph uses explicit input/output schemas and runtime context. `PLAN` and `AUTHORIZE` have no unconditional static outgoing edge in addition to `Command`; `INVESTIGATE → CONCLUDE → END` remains static.

### First focused offline proof family

Added:

`experiments/tests/test_b2_x1_evidence_gap_langgraph.py`

Commit:

`ac852655c4bc0f472eb4aca5f5fd3d06f982ff6e` — `Add focused offline proof for first LangGraph workflow`

The initial four discriminating cases are:

1. no-action → direct conclusion; authority supplier and repository effect must not run;
2. T1 action offered but T2 already consumed → deterministic rejection; repository effect must not run; final result preserves the T2 baseline;
3. authorized exact target read → one repository call, semantic target interpretation, budget decrement, action consumption, applicability update;
4. expected repository timeout → budget decrement without action consumption or domain strengthening.

These are intentionally offline orchestration proofs; they do not contact LM Studio or GitHub.

## 8. Important Build/Learning discovery — T2 consequence coherence

Implementation exposed a gap in the earlier simplified model.

Earlier working assumption:

```text
AUTHORIZE gets fresh T2 facts
→ uses them locally
→ only authorization outcome needs to travel forward
```

That is insufficient for this responsibility.

If T1 says:

```text
remaining budget = 1
consumed = ()
```

but current T2 trusted state is different, `AUTHORIZE` must decide against T2. If it succeeds, `CONCLUDE` must also apply budget/consumption/domain consequences to the **same T2 semantic baseline**, not silently mutate the older T1 snapshot.

Therefore the first graph introduces:

```text
EvidenceGapLangGraphAuthoritySnapshot
    admission_state
    +
    baseline
```

and validates that the two agree on:

- consumed-action history;
- remaining investigation budget;
- proposition state derived from the current Python-support assessment.

This is a real implementation-derived refinement of Graph State responsibility:

```text
fresh facts do not belong in State merely because they are fresh
but
fresh information that a later node must use for correct consequences must cross the workflow boundary
```

The T2 snapshot remains acquired through runtime context; the resulting snapshot becomes workflow communication only after it has been obtained at the correct authority time boundary.

## 9. Evidence and proof limit after first slice

### Established by repository/source inspection

- experiment-only dependency placement is encoded in `pyproject.toml`;
- no LangChain dependency was introduced;
- the first Graph API module and test family exist under the correct experiment boundaries;
- the source topology matches the frozen routing design at text/source level;
- product repository acquisition and target/domain interpretation owners are reused rather than duplicated;
- R4-A deterministic admission semantics are reused as the controlled authority oracle;
- the first test family covers materially distinct no-action, T2 rejection, semantic success, and operational-failure responsibilities.

### Not yet established

- `uv` can resolve/install `langgraph==1.2.11` in the actual UpgradePilot WSL environment;
- the new module imports successfully in that environment;
- `StateGraph` compiles successfully against the installed package;
- the four focused tests pass;
- graph invocation/output filtering behaves exactly as intended at runtime;
- deterministic comparison against R4-A is green;
- real S001 LangGraph execution is green;
- LangGraph has earned product adoption.

Current assistant execution environment could not resolve `github.com`, so it could not clone/run the repository as a substitute for WSL. GitHub reported no Actions workflow runs for the new test commit. This is an environment/proof limitation, not evidence of a source failure.

## 10. Current route

```text
CURRENT — first R4-B5 source slice WRITTEN, execution proof pending
→ run uv dependency resolution/install in normal WSL control plane
→ run focused LangGraph test family
→ if failure: diagnose through hypothesis → discriminating evidence → minimal repair
→ if green: inspect actual graph/runtime behavior and source clarity

THEN
→ add any missing discriminating branch only if proof gap remains
→ controlled R4-A vs R4-B semantic comparison
→ bounded real S001 LangGraph smoke
→ R4-B framework value/cost findings for R4-D
```

Do not extend into persistence/HITL/subgraphs/parallelism or product integration before the current graph has executable proof.

## 11. Stop lines

Do not:

- integrate LangGraph into product runtime;
- add LangChain/create_agent merely because LangGraph is added;
- pre-build persistence/HITL/retry/subgraph/parallel/multi-turn machinery;
- manufacture a second action;
- duplicate established product/domain truth;
- claim framework superiority/adoption from the bounded experiment;
- treat written tests as passing tests.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-build-implement`
