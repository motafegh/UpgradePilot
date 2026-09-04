# UpgradePilot Current Memory

**Last updated:** 2026-09-04  
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

For framework architecture work, keep this additional discipline:

```text
bounded implementation slice
!= bounded architectural horizon

build only what current evidence needs
+ evaluate boundaries against the credible intended larger system
+ do not pre-build speculative future machinery
```

---

## Live position

- **Route:** B2/X1 — Product Agentic Investigation / Orchestration Evaluation.
- **Mode:** Learning-by-Doing + **Build/Implement**.
- **Selected implementation plan:** `plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`.
- **Selected R4-B bounded plan:** `plans/B2_X1_R4B_LANGGRAPH_LBD_IMPLEMENTATION_AND_COMPARISON_PLAN.md`.
- **Selected R4 learning-depth companion:** `plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`.
- **Progress:** R0 PASS; R1 COMPLETE; R2 COMPLETE/PASS; R3 COMPLETE/PASS; **R4-A ordinary-Python reference/control COMPLETE; R4-B comparison-boundary correction COMPLETE; corrected independent LangGraph research reviewed; R4-B2A API-paradigm decision COMPLETE; R4-B2B decision-critical Graph API learning COMPLETE enough for Build; R4-B3 Graph API architecture FROZEN; R4-B4 Build preflight ACTIVE**.
- **Current active working memory:** `working-memory/2026-09-04_1904_B2-X1-R4B-architecture-freeze-and-build-entry.md` — architecture decision + Build handoff.
- **Previous detailed reasoning:** `working-memory/2026-09-03_1804_B2-X1-R4B-comparison-boundary-reframe.md` — comparison reframe, API-paradigm learning, framework-value challenge, and design provenance.
- **R4-A baseline disposition:** the ordinary-Python A1 → A3 → A2 → A4 seam is coherent enough to serve as a real reference/control. This is a comparison-baseline decision, not product/framework adoption and not architectural authority over R4-B.
- **Completed/proven R4-A responsibility:** R4-A1 model boundary/projection/parser; R4-A2 deterministic rebinding/admission; R4-A3 local-model request/response; real-product composition seam; first live real S001 A3 selection/admission; bounded A4 execution/update/trace/replay; post-action Learning-by-Doing ownership closure.
- **Latest focused runtime family:** **47/47 PASS** for A1+A2+A3+composition+A4 in the normal UpgradePilot WSL checkout; the dedicated A4 family is **7/7 PASS**.
- **Latest live S001 evidence:** `ACTION_SELECTED` → `acquire_exact_target_python_declaration` → current R4-A A2 admission → exact `pyproject.toml` read at head `aa2dc024d33f61cdef50bf1973ab5adf0a974f5a` → `requires-python = ">=3.10"` → applicability `unresolved → established_not_applicable`; budget `1 → 0`; action consumed; R4-A replay equivalent.
- **A4 runtime validation:** PASS for the bounded ordinary-Python transition seam. `default=str` remains accepted only for the current disposable diagnostic JSON boundary because typed semantic comparison occurs before rendering; reopen if serialized JSON becomes durable/machine-consumed, broad stringification hides a defect, or canonical serialization becomes part of proof.
- **R4-B comparison correction:** R4-A serves as **reference implementation + engineering/learning evidence**, not as the architectural specification for LangGraph. Do not mechanically translate A1/A2/A3/A4 or require existing R4-A state/trace classes to define R4-B.
- **R4-B bounded-build / long-horizon rule:** keep the first implementation deliberately small, but do **not** select architecture merely because the first graph has one action/one agent. Evaluate boundaries against the credible larger UpgradePilot direction: more agent/orchestration responsibilities, richer investigation paths, durable execution/recovery, possible human approval/interrupt boundaries, stronger runtime observability, and other real growth pressures. Those pressures inform design; they do not authorize building those features now.
- **R4-B API-paradigm decision:** **Graph API / `StateGraph` is selected for the first implementation.** It wins because R4-A exposed materially important planning/authority/effect/consequence boundaries and the intended larger system makes explicit executable topology/control-flow plus LangGraph runtime leverage a meaningful hypothesis to test. This is an experiment architecture decision, not product adoption.
- **Serious API fallback:** Functional API remains the explicit reassessment option if Graph API state/topology plumbing materially dominates, creates invalid-state pressure, obscures responsibility, or fails to provide useful orchestration/debugging leverage beyond ordinary Python.
- **R4-B framework-value rule:** LangGraph does not justify itself merely by expressing state and `if`-style branching with framework primitives; ordinary Python can already do that. The experiment must look for meaningful orchestration/runtime burden reduction or architectural leverage—executable topology, standardized runtime observability, durable execution/persistence/recovery, interrupt/resume/HITL support, richer composition/branching, and related framework infrastructure UpgradePilot would otherwise have to own. Distinguish currently exercised value from credible-but-unexercised architectural value.
- **R4-B frozen topology:** `START → PLAN`; `PLAN` uses `Command` to `AUTHORIZE` for action proposals or `CONCLUDE` for no-action/provider problems; `AUTHORIZE` uses `Command` to `INVESTIGATE` when authorized or `CONCLUDE` when rejected; static `INVESTIGATE → CONCLUDE → END` thereafter. Do not mix unconditional static edges with dynamic `Command` routing from `PLAN`/`AUTHORIZE`.
- **Routing rationale:** `PLAN` and `AUTHORIZE` each create a new stage outcome and that exact outcome determines the next responsibility. Separate conditional routers would currently duplicate the just-produced classification without an independent routing policy. Extract separate routing only if future routing policy gains its own responsibility, shared ownership, or materially different proof value.
- **R4-B frozen State/context model:** use a small experiment-owned graph communication envelope, conceptually `start_input`, `planner_outcome`, `execution_authority_outcome`, `investigation_outcome`, `final_result`; one writer per stage field; overwrite semantics; no custom reducers. Model/provider, current-authority composition/supply capability, and `GitHubRepositoryClient`/narrow acquisition capability belong in runtime context/resources rather than evolving graph State. A value in State is not automatically current, trusted, authorized, or model-visible.
- **R4-B frozen responsibility boundaries:** `PLAN` owns explicit bounded model projection + provider call; `AUTHORIZE` obtains sufficiently current T2 trusted facts after proposal and owns deterministic pre-effect authority; `INVESTIGATE` is the only admitted external repository effect and reuses product acquisition/target/domain owners; `CONCLUDE` is pure deterministic consequence with no model/GitHub I/O and owns normalized budget/consumption/continuation/final-result consequences.
- **R4-B proof model:** first prove controlled framework-neutral scenarios and forbidden-call absence; use pure conclusion reconstruction for deterministic semantic proof without model/GitHub re-execution; use graph topology/trace/stream evidence only as supporting observability. Run real S001 only after controlled proof is green.
- **R4-B reuse rule:** established product/domain capabilities remain the truth owners. Build may reuse the bounded R4-A admission function or provider seam behind narrow adapters where that holds semantic variables constant without forcing R4-A state/topology into graph architecture. Do not prematurely create a shared abstraction merely for symmetry.
- **R4-B Build preflight facts:** Build/Implement procedure is loaded; `pyproject.toml` currently declares only `requests`, `packaging`, and `PyYAML`; repository code search found no current `langgraph` usage; established experiment tests already live under `experiments/tests/`. No LangGraph dependency/source mutation has occurred yet.
- **Live next slice:** **R4-B4 Build preflight** — inspect `uv.lock`/dependency state and exact current LangGraph package/API surface; inspect only the R4-A/product source/tests required for controlled reuse/proof; choose the smallest explicit dependency change. Then begin R4-B5 with graph-owned input/state/context/outcome skeleton + compile/invoke proof and learn exact framework syntax through implementation.
- **LangGraph implementation:** NOT STARTED. Source/dependency mutation is now authorized only inside the bounded R4-B experiment plan after the remaining Build preflight checks.
- **Product runtime integration:** not authorized. Planner/orchestration framework work remains under `experiments/` through the R4 reference/framework-comparison period.
- **Post-experiment direction:** after ordinary-Python/LangGraph/LangChain comparison, perform a separate product-integration/architecture decision. Move/refactor only responsibilities that earn adoption; do not blindly copy any experiment implementation wholesale.
- **Persistence boundary:** checkpointing/durable execution is **not authorized for the first R4-B implementation** merely for exposure. It remains an important LangGraph architectural-value dimension for the credible larger system because it could remove future workflow recovery/resume infrastructure from UpgradePilot ownership. Reopen implementation only when a real responsibility/proof trigger appears.
- **Product-simulation:** existing capability/value research remains sufficient for current design pressure; do not expand merely for case count.
- **Technical observation:** LM Studio previously emitted an `outdated gemma4 chat template` compatibility-workaround warning on successful calls; currently observational/non-blocking.

Current detailed owners/evidence:

- `plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`
- `plans/B2_X1_R4B_LANGGRAPH_LBD_IMPLEMENTATION_AND_COMPARISON_PLAN.md`
- `plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`
- `working-memory/2026-09-04_1904_B2-X1-R4B-architecture-freeze-and-build-entry.md` — current active architecture/Build owner
- `working-memory/2026-09-03_1804_B2-X1-R4B-comparison-boundary-reframe.md` — detailed predecessor/provenance
- `proposals/2026-09-03_B2_X1_R4B_CORRECTED_LANGGRAPH_INDEPENDENT_RESEARCH_AND_DESIGN_PROPOSAL.md` — corrected non-controlling research/design evidence
- `working-memory/2026-09-02_B2-X1-R4B-langgraph-lbd-entry.md` — superseded earlier R4-B design-consolidation provenance
- `proposals/2026-09-02_B2_X1_R4B_LANGGRAPH_RESEARCH_AND_DESIGN_PROPOSAL.md` — historical non-controlling research evidence; implementation-preserving architecture recommendations are superseded
- `working-memory/2026-09-02_B2-X1-R4A4-runtime-lbd-and-reconciliation-closure.md`
- R4-A1/A2/A3/A4 working memories remain supporting provenance.

Historical R2/E1–E5/v2/capability-research records remain provenance and are not mass-rewritten solely for newer vocabulary.

---

## Current responsibility vocabulary

### `EvidenceGapPlanner`

> Given one bounded UpgradePilot planning question, trusted proposition state, selected structured planning evidence, trusted consumed-investigation history, a bounded planning budget, and a closed set of currently admitted bounded actions, select one useful investigation action or explicitly decide why no action should execute now.

This is a framework-independent bounded responsibility. R4-A and R4-B may represent its internal implementation differently.

### `EvidenceGapDecision`

Current R4-A untrusted structured model decision representation; never execution authority.

The **semantic rule** that model output does not self-authorize execution is shared. The exact `EvidenceGapDecision` class remains an R4-A implementation representation unless independently selected for R4-B.

### `EvidenceGapDecisionKind`

Current accepted first-seam planner semantic outcomes:

```text
ACTION_SELECTED
QUESTION_SETTLED
KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

### No-action decision

Umbrella vocabulary for the three valid planner outcomes where no investigation action executes:

```text
QUESTION_SETTLED
KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

`no-action decision` is descriptive vocabulary, not a fifth decision kind.

### `PlanningEvidence`

Current structured model-visible evidence representation used by R4-A. Its underlying requirement is selected bounded evidence that may change investigation value while raw/privileged authority remains outside model control.

### `BoundInvestigationAction`

Current trusted exact executable action binding used in the ordinary-Python experiment. The broader authority rule remains that model-visible action descriptors/IDs do not carry exact execution authority by themselves.

### `EvidenceGapAdmissionState`

Current R4-A representation of fresh trusted pre-execution conditions. The shared requirement is sufficiently current deterministic execution authority after the model proposal and before the effect; R4-B may represent that responsibility differently.

### `LocalEvidenceGapPlanner`

R4-A3 local LM Studio structured-output boundary returning either the current structured decision or a typed invocation problem.

### `EvidenceGapInvestigationState`

R4-A4 experiment-owned evolving state representation:

```text
python_support_assessment
consumed_actions
remaining_investigations
continuation_status
```

This remains part of the R4-A reference. It is **not** a mandatory LangGraph state/domain-wrapper requirement.

### `EvidenceGapTransitionTrace`

R4-A4 immutable transition record used for bounded semantic proof/replay. It remains valid R4-A comparison evidence. R4-B preserves the required semantic/proof behavior through its independently selected pure-conclusion/proof design rather than requiring the same trace representation.

### Graph API / `StateGraph`

Selected R4-B first-implementation LangGraph paradigm using explicit shared workflow state, nodes, and edges/routing. Selection is bounded to the experiment; it is not product-runtime adoption.

### Functional API

Current R4-B fallback/reassessment paradigm using `@entrypoint`, optional `@task`, and ordinary Python control flow/local workflow values on the LangGraph runtime. Reopen if Graph API ceremony materially drives a negative or ambiguous result.

### Runtime context

Run-scoped dependencies/resources needed by graph work but not themselves evolving semantic workflow facts. Current candidates include model/provider, current-authority supplier/composer, and `GitHubRepositoryClient`/narrow acquisition capability; placement does not itself establish trust or authorization.

### Graph State

For the selected Graph API experiment, the evolving workflow communication snapshot needed across meaningful stages. A value being present in Graph State does not by itself make it current, trusted, authoritative, or appropriate for model observation.

### `Command`

Selected R4-B dynamic-routing mechanism for `PLAN` and `AUTHORIZE` when a node both records the stage outcome and routes based on that same newly established outcome. It is not execution authority and is not required for unconditional transitions.

---

## Frozen / accepted framework-independent boundaries relevant to R4

### Model authority

```text
model observation
→ bounded to the admitted decision context

model output
→ proposal / semantic result
!= automatic trusted source truth
!= automatic execution authority
```

### Deterministic execution authority

A selected action may execute only after the applicable sufficiently current trusted deterministic conditions are established at the pre-execution boundary. In the selected R4-B architecture, `AUTHORIZE` owns that boundary.

### Product/domain ownership

Experiment isolation does not authorize duplicate ownership of established product facts/capabilities. Reuse the normal owners when the same responsibility is required.

### Evidence/failure discipline

Keep materially different classes distinct where applicable:

```text
semantic/domain result
expected external/provider/operational failure
unexpected programmer/framework defect
```

Do not turn missing/unavailable/error states into stronger semantic conclusions merely for orchestration convenience.

### Investigation semantics

Preserve explicit no-action/stopping outcomes and honest unresolved states. Do not manufacture a second action or multi-turn loop merely to exercise framework features.

---

## R4-A evidence retained for comparison

```text
A1
→ bounded model observation / strict decision representation

A3
→ bounded local model invocation / provider failure classification

A2
→ current deterministic pre-execution authority

A4
→ bounded effect / interpretation / state consequence / trace-replay proof
```

These labels are useful for discussing the R4-A implementation and its lessons. They are not mandatory LangGraph node/task names or architecture layers.

The real S001 R4-A path remains a comparison reference:

```text
current product evidence
→ bounded model context
→ ACTION_SELECTED
→ deterministic pre-execution admission
→ exact target declaration acquisition
→ requires-python >=3.10
→ applicability unresolved → established_not_applicable
→ remaining investigation budget 1 → 0
→ selected action consumed
→ semantic replay equivalent without re-running model/GitHub I/O
```

---

## Corrected R4-B Learning-by-Doing route

### R4-B1 — comparison-boundary classification — COMPLETE enough for Build

Important concepts remain classified as:

```text
accepted framework-independent requirement
reusable product-owned capability
R4-A engineering lesson/evidence
R4-A/Python-specific implementation choice
```

Reopen only if Build exposes a real ownership ambiguity.

### R4-B2A — LangGraph API-paradigm decision — COMPLETE

Selected:

```text
Graph API / StateGraph
→ explicit topology + shared workflow state + nodes/edges/routing
```

Functional API remains the reassessment fallback. The selection is based on current responsibility **plus credible product trajectory**, not current graph size alone.

### R4-B2B — selected-paradigm decision-critical learning — COMPLETE enough for Build

Grounded concepts:

```text
StateGraph mental model
Graph State vs runtime context/resources
fresh T1 → T2 authority/currentness distinction
node work vs routing work
static edges
conditional routing
Command for cohesive state-update + dynamic routing
input/internal/output separation
compile/invoke and observability remain implementation-time learning
```

Exact syntax is now intentionally learned through Build.

### R4-B3 — independent Graph API architecture freeze — COMPLETE

Frozen first topology:

```text
START → PLAN
PLAN --Command(action)--> AUTHORIZE
PLAN --Command(no-action/problem)--> CONCLUDE
AUTHORIZE --Command(authorized)--> INVESTIGATE
AUTHORIZE --Command(rejected)--> CONCLUDE
INVESTIGATE → CONCLUDE → END
```

Frozen responsibilities and boundaries are recorded in the current active working memory.

### R4-B4 — Build preflight — ACTIVE

Use the substantive Build/Implement procedure.

```text
inspect lock/dependency state + current LangGraph package/API
→ inspect only needed R4-A/product source/tests
→ choose smallest explicit dependency change
→ begin implementation
```

### R4-B5+ — implementation and proof

```text
smallest complete Graph API experiment
→ controlled framework-neutral semantic comparison
→ bounded real S001 smoke
→ framework value/cost findings for R4-D
```

Do not implement the Functional API as a checklist. Reopen it only if Graph API implementation evidence makes API ceremony a material confounder.

---

## Current common comparison projection

The comparison remains framework-neutral and small. Candidate observable fields/responsibilities include:

```text
planner/action/no-action/rejection outcome
selected/executed action identity when applicable
pre-execution trusted authority accepted/rejected
external execution occurred? / forbidden calls absent?
remaining investigation budget consequence
consumed-action consequence
final domain/applicability conclusion
semantic result vs operational failure classification
continuation/stopping consequence
semantic consequence reproducible/testable without model/repository re-execution when applicable
```

This comparison projection is evaluation evidence, not a new canonical product state model.

Framework-value evidence additionally distinguishes:

```text
currently exercised value
→ demonstrated by R4-B implementation/tests/runtime

credible architectural value
→ framework capability relevant to the intended larger system but not yet exercised

speculative value
→ imagined future without a concrete product responsibility/trajectory
```

---

## Deliberately deferred R4-B surface

Do not pre-build or deeply study without a real implementation trigger:

```text
persistent checkpointing / time travel
interrupts / HITL
automatic generalized retries
custom reducers without merge pressure
ToolNode / generic model-tool execution
create_agent before R4-C
subgraphs
parallelism / Send
automatic multi-turn back-edge
persistent Store / cross-thread memory
advanced streaming
LangSmith as required correctness proof
product-runtime integration
```

Deferred implementation does not make credible future framework capabilities invisible to architecture/value evaluation.

---

## Immediate route

```text
PLANNING / DESIGN
→ R4-B1 COMPLETE enough
→ R4-B2A COMPLETE
→ R4-B2B COMPLETE enough
→ R4-B3 ARCHITECTURE FROZEN

CURRENT — R4-B4 BUILD PREFLIGHT
→ inspect uv.lock/dependency state
→ confirm exact current LangGraph package/API/version surface
→ inspect only required existing source/tests for controlled reuse
→ choose smallest dependency mutation

NEXT — R4-B5 BUILD
→ graph input/state/context/outcome skeleton
→ compile/invoke proof
→ PLAN
→ AUTHORIZE
→ INVESTIGATE
→ CONCLUDE

THEN
→ R4-B6 controlled semantic comparison
→ R4-B7 real S001 smoke
→ R4-B8 R4-D handoff evidence

STOP
→ no product runtime integration
→ no speculative persistence/HITL/subgraph/parallel/multi-turn machinery
→ no LangChain/create_agent consumption before R4-C
→ no framework/product adoption claim
```

---

## Provenance

Current active detailed reasoning / Build handoff:

`working-memory/2026-09-04_1904_B2-X1-R4B-architecture-freeze-and-build-entry.md`

Previous detailed planning/learning provenance:

`working-memory/2026-09-03_1804_B2-X1-R4B-comparison-boundary-reframe.md`

Current corrected research evidence:

`proposals/2026-09-03_B2_X1_R4B_CORRECTED_LANGGRAPH_INDEPENDENT_RESEARCH_AND_DESIGN_PROPOSAL.md`

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-build-implement`
