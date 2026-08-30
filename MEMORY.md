# UpgradePilot Current Memory

**Last updated:** 2026-08-30  
**Authority:** sole owner of the live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Controlling engineering rule

Existing implementation and historical design are evidence to inspect, not authority to preserve unchanged.

```text
real responsibility / proof need / material risk / learning value
→ identify the earliest sufficient owner
→ keep or grow mechanisms that add real capability or learning value
→ refine redundant ownership/representation
→ avoid both over-engineering and under-engineering
```

Complexity is welcome when it buys real product capability, stronger reasoning, useful failure handling, observability/replay, or meaningful engineering learning. New tools/frameworks are not prohibited merely because plain Python could implement the same behavior; bounded learning/comparison is justified when attached to a real UpgradePilot responsibility and a real baseline. Adoption remains a separate evidence-backed decision.

---

## Live position

- **Route:** B2/X1 — Product Agentic Investigation / Orchestration Evaluation checkpoint.
- **Mode:** Learning-by-Doing / Building.
- **Selected plan:** `plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`.
- **Progress:** R0 PASS; R1 COMPLETE; R2 active with planning-question, dependency-transition, case-identity, proposition, structured-planning-evidence, consumed-action-history, and planning-budget slices decided.
- **Live next slice:** **R2 — allowed capability descriptor / model-visible action-space boundary**.
- **Product runtime integration:** not authorized; current planner/framework work remains experiment-owned.
- **Technical blocker:** none.
- **Product-simulation:** prior capability/value research complete; no new broad simulation job merely for more cases.

Current detailed R2 owners:

- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-model-visible-context.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-planning-question.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-proposition-projection.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-action-history-and-retry-boundary.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-planning-budget-envelope.md`

Historical E1–E5 and capability-research detail remains in dated records; do not duplicate it here.

---

## Current responsibility vocabulary

### `EvidenceGapPlanner`

> Given one bounded UpgradePilot planning question, trusted typed proposition state, selected bounded structured planning evidence, trusted consumed-investigation history, a bounded planning budget, and a closed set of admitted bounded investigation capabilities, decide which material evidence gap should be addressed next by selecting one useful admitted capability, or explicitly decide why no capability should execute now.

### `EvidenceGapDecision`

Untrusted model proposal; never execution authority.

### `EvidenceGapDecisionKind`

```text
ACTION_SELECTED
QUESTION_SETTLED
KNOWN_INVESTIGATION_NOT_ADMITTED
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

R3 will freeze final structured/wire representation.

---

## R2 decisions already earned

### Model-visible dependency transition

```text
dependency_transition:
    normalized_package
    old_version
    proposed_version
```

Use canonical normalized package identity, not presentation spelling.

### Trusted but model-hidden case identity

```text
repository
pull_number
immutable revision
```

Retained for trace/acquisition/binding/freshness/admission/replay, not current model reasoning.

### Planning question

One concise project-owned bounded question. Do not duplicate structured evidence or encode expected action/oracle in the question.

A future question-formulation agent remains a separate hypothesis only when question selection itself becomes materially non-trivial.

### Proposition projection

Model-visible:

```text
key
state
evidence_coverage
evidence_owner
detail
```

Do not promote experiment-only `origin` / `raw_external_text` into the base first seam.

### `EvidenceGapPlanningEvidence`

Propositions are the decision-state spine, not the whole reasoning input.

Use selected structured question-relevant evidence when mechanism/witness/limitation/unresolved-condition detail can change which investigation is useful.

```text
Level 1 = proposition state
Level 2 = selected EvidenceGapPlanningEvidence
Level 3 = raw evidence

current model context = Level 1 + selected Level 2
Level 3 excluded by default
```

### Consumed-action history

Use:

```text
consumed_actions: [action_id]
```

rather than historical generic `attempted_actions[{action_id,outcome}]`.

Consumed means an admitted bounded investigation produced a trusted typed result/problem for the state. Rejected proposals, pre-execution stale actions, and transient provider failures are not automatically consumed investigations.

Findings update propositions/planning evidence. Transport retries remain deterministic provider/executor policy.

### Planning budget

First seam:

```text
planning_budget:
    remaining_investigations: int
```

Spend one investigation unit when fresh-admitted bounded execution actually begins, not when the model merely proposes or admission merely accepts.

Internal deterministic provider retries do not automatically spend additional planner investigation units.

Budget expenditure and consumed history are different dimensions:

```text
execution starts
→ budget spent

trusted typed result/problem
→ action consumed
```

Potential future budget envelope dimensions:

```text
remaining_time_seconds
remaining_external_cost
other measured resource constraints
```

Add them to model-visible state only when real competing actions, real bounds, and trustworthy resource profiles make them decision-relevant. Collect timing/resource telemetry before inventing precise planning estimates.

---

## R4 framework/LbD route — now explicitly planned

R4 is no longer "plain Python unless blocked."

```text
R4-A
ordinary-Python reference/control implementation

R4-B
same bounded EvidenceGapPlanner responsibility implemented with LangGraph

R4-C
smaller LangChain model/tool/agent/middleware learning slice

R4-D
compare real implementations against UpgradePilot responsibilities
```

Current framework-learning goals include:

- LangGraph State / StateGraph / nodes / edges / conditional routing;
- persistence/checkpoints and replay/fault-tolerance value;
- interrupts/HITL concepts where relevant;
- pre-execution revalidation placement;
- LangChain model/tool abstractions and middleware/lifecycle hooks;
- framework runtime vs UpgradePilot domain/control-plane ownership.

Learning/comparison is authorized by the current plan. Product dependency/framework adoption still requires a later explicit architecture/build decision.

---

## Evidence/claim limits retained

Current evidence does **not** prove:

- production reliability;
- general adaptive-planner superiority;
- correct selection across multiple real actions;
- product/framework adoption value;
- compatibility/safety/merge authority;
- that raw evidence should never enter any future agent;
- that every conceivable time/cost dimension belongs in model context.

Do not:

- fabricate a second action;
- freeze fresh v3 before the exact claim/holdout route is selected;
- reuse exposed v2 material as clean final evidence;
- silently integrate planner/framework into `src/upgradepilot/`;
- adopt LangGraph/LangChain merely because the learning slice succeeds;
- reject LangGraph/LangChain merely because plain Python can do the job;
- flatten provider retry attempts into semantic planner actions;
- invent fake latency/cost precision;
- continue product simulation merely for case count.

---

## Current learning route

```text
R2 context/state/budget/action-space design
→ context engineering, state projection, evidence representation,
  semantic history, resource budgeting

R3 decision/admission contract
→ structured outputs, authority, fresh-state validation

R4 plain Python + LangGraph + LangChain learning/comparison
→ StateGraph, nodes, edges, tools, middleware, checkpoints,
  framework-vs-domain ownership

R5 bounded replay/development proof
→ tracing, telemetry, failure separation, implementation comparison

R6 explicit X1 disposition
```

Richer multi-action/multi-turn planner work reopens only when independently justified capabilities naturally coexist and real state/evidence/history/time/cost-dependent selection becomes materially non-trivial for a small deterministic policy.

---

## Immediate continuation

Next R2 slice:

> **What exact information about each admitted capability should the model see in order to compare evidence value, preconditions and resource profile, and what action metadata must remain deterministic-only authority?**

Candidate fields to challenge rather than retain automatically:

```text
action_id
purpose
target proposition / gap
required proposition/evidence precondition
cost_class / future resource profile
mutation_class
result-family summary
exact locators
```

After that, build the final R2 field/owner/visibility table and rendered request examples. If those close cleanly, advance to R3.
