# B2/X1 Post-Research EvidenceGapPlanner Learning-by-Doing Implementation Plan

**Status:** AUTHORIZED PLAN ARTIFACT — position-neutral; `MEMORY.md` selects live activation  
**Date:** 2026-08-30  
**Revision:** evidence-refined through R2 action-space design  
**Responsibility:** finish the post-E1–E5 B2/X1 planner decision by defining, building, comparing, and evaluating the smallest honest `EvidenceGapPlanner` experimental seam, then make an explicit X1 disposition without manufacturing multi-action value or prematurely integrating product runtime.  
**Primary method:** Learning-by-Doing / Building  
**Product runtime integration:** NOT authorized by this plan itself

---

## 1. Why this plan exists

Current evidence establishes that bounded typed-state LLM reasoning, closed action binding, structured output, deterministic admission, and explicit no-tool semantics can work. It also establishes an important limit:

```text
real additional product capabilities exist
but no second capability is yet justified for LLM-owned selection
general adaptive-planner advantage over a small deterministic policy is not proven
```

The route therefore avoids both:

```text
UNDER-ENGINEERING
→ discard useful planner/agent work because S001 is simple

OVER-ENGINEERING
→ manufacture capabilities/framework machinery merely to look agentic
```

The project should build enough real agent-engineering surface to learn from and evaluate honestly, while product authority and claims remain evidence-bounded.

---

## 2. Active owners

### Governance / procedure

- `../AGENTS.md`
- `../OPERATING_GUIDE.md`
- `.agents/skills/upgradepilot-planning-design/SKILL.md`
- `.agents/skills/upgradepilot-build-implement/SKILL.md`
- `.agents/skills/upgradepilot-learning-by-doing/SKILL.md`

### Stable technical owners

- `../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`
- `../docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`
- `../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`
- `../docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md`

### Immediate R2 evidence owners

- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-model-visible-context.md`
- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-planning-question.md`
- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-proposition-projection.md`
- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-action-history-and-retry-boundary.md`
- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-planning-budget-envelope.md`
- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-capability-descriptor-boundary.md`
- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R0-R1-responsibility-vocabulary.md`

Historical E1–E5, v2 and product-simulation research remain evidence. Do not re-open all of them for every slice.

---

## 3. Learning-by-Doing execution rule

Each substantive stage follows this loop proportionately:

```text
ORIENT
→ establish only the concepts/dataflow/owners needed now

USER REASONING
→ learner predicts/challenges/selects/explains a material point when useful

REAL BOUNDED WORK
→ design / implement / evaluate one actual slice

INSPECT ACTUAL EVIDENCE
→ source/tests/model output/replay/result

CORRECT THE MENTAL MODEL
→ observation vs interpretation vs remaining uncertainty

PRESERVE MATERIAL STATE
→ working memory / MEMORY / plan only when continuation changes

TEACHING CLOSURE
→ what changed, why, what concept was demonstrated, what remains deferred
```

Do not turn every edit or command into ceremony.

### Framework/LbD rule

Do not interpret proportionality as a ban on new tools/frameworks.

```text
new tool only because fashionable
→ not justified

new tool gives meaningful learning exposure
+ is attached to a real UpgradePilot responsibility
+ can be compared against a real baseline
→ justified bounded experiment
```

Learning/comparison and product adoption are separate decisions.

---

# Stage R0 — Re-anchor baseline

**Status:** COMPLETE / PASS.

Do not restart completed E1–E5 or product-simulation research without contradiction.

---

# Stage R1 — Responsibility vocabulary

**Status:** COMPLETE.

```text
component
→ EvidenceGapPlanner

model result
→ EvidenceGapDecision

decision kind
→ EvidenceGapDecisionKind
```

Preferred semantics:

```text
ACTION_SELECTED
QUESTION_SETTLED
KNOWN_INVESTIGATION_NOT_ADMITTED
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

---

# Stage R2 — Freeze model-visible context contract

## R2 question

> What exact trusted information should `EvidenceGapPlanner` receive, and why does each field belong at the model boundary?

## Current evidence-refined candidate

```text
EvidenceGapPlannerContext

planning_question

dependency_transition
    normalized_package
    old_version
    proposed_version

propositions
    key
    state
    evidence_coverage
    evidence_owner
    bounded detail

planning_evidence
    EvidenceGapPlanningEvidence[]

consumed_actions
    action_id[]

planning_budget
    remaining_investigations

allowed_actions
    EvidenceGapActionDescriptor[]
        action_id
        purpose
        target_proposition
        evidence_yield

output_schema / structured-output contract
```

Trusted but model-hidden by default:

```text
repository
pull_number
immutable revision
exact action locators
exact action preconditions
mutation policy
exact result-family/class contract
provider/executor retry policy
full execution/audit trace
raw provider/source objects
oracle/evaluator metadata
```

## R2.1 — planning question — DECIDED

One concise project-owned bounded `planning_question` is model-visible.

It defines which uncertainty the planner turn advances. It must not duplicate structured evidence or encode the expected action/disposition/oracle.

Future question-formulation LLM/agent work remains a separate hypothesis only when choosing the question itself becomes materially non-trivial.

## R2.2 — target/case identity — DECIDED

Repository / PR / revision remain trusted system state for acquisition, binding, freshness, trace and replay, but are omitted from the current model observation.

## R2.3 — dependency transition — DECIDED

Pass:

```text
normalized_package
old_version
proposed_version
```

Use canonical package identity rather than presentation spelling.

## R2.4 — proposition projection — DECIDED

Pass:

```text
key
state
evidence_coverage
evidence_owner
detail
```

Do not add experiment-only `origin` or `raw_external_text` to the base first-seam proposition contract.

`detail` is bounded/project-interpreted text, not arbitrary raw external prose.

## R2.5 — `EvidenceGapPlanningEvidence` — CONCEPT DECIDED

Propositions are the decision-state spine, not the complete reasoning input.

Use selected structured evidence whose mechanism, witness, limitation, reason, or unresolved condition can change which investigation has highest discriminating value.

```text
Level 1 = proposition state
Level 2 = selected EvidenceGapPlanningEvidence
Level 3 = raw evidence

current model observation = Level 1 + selected Level 2
Level 3 stays outside by default
```

Examples may include bounded CI consumption/direct-exercise distinctions, reachability/witness paths, target-Python interpretation, grounded upstream mechanism facts, environment conditions, structured change-scope facts, and deterministically interpreted command semantics.

## R2.6 — planner-visible history — DECIDED

Use:

```text
consumed_actions: [action_id]
```

rather than historical:

```text
attempted_actions: [{action_id, outcome}]
```

Consumed means an admitted bounded investigation produced a trusted typed result/problem for the bounded state.

Do not count as consumed:

- admission-rejected model proposals;
- pre-execution stale/pruned actions;
- transient provider timeout/transport/rate-limit failures;
- untrusted provider responses that never became valid domain evidence.

Findings update propositions/planning evidence. Transport retries remain deterministic provider/executor policy.

## R2.7 — planning budget — DECIDED

First seam:

```text
planning_budget:
    remaining_investigations: int
```

Spend one unit when a fresh-admitted bounded investigation execution actually begins.

```text
model proposal
→ no spend

admission
→ no spend

fresh pre-execution revalidation
→ no spend

execution begins
→ spend 1

internal deterministic provider retries
→ no additional planner-investigation spend
```

Budget expenditure and consumed history are different dimensions:

```text
execution starts
→ budget spent

trusted typed result/problem
→ action consumed
```

Future time/cost/resource dimensions enter model-visible budget only when real competing actions, real bounds and trustworthy measurements make them decision-relevant. R4/R5 should collect telemetry before quantitative estimates are invented.

## R2.8 — allowed action / capability descriptor — DECIDED

Use working planner-facing type:

**`EvidenceGapActionDescriptor`**

First-seam fields:

```text
action_id
purpose
target_proposition
evidence_yield
```

### Why these are visible

```text
action_id
→ stable trusted selection token; rebinds to exact hidden action

purpose
→ what bounded uncertainty the action is intended to advance

target_proposition
→ explicit semantic link to the evidence gap

evidence_yield
→ bounded project-authored description of what useful evidence the action may produce
```

The model needs to reason about **what it can learn**, not about how the action is authorized or executed.

### Hidden trusted action fields

Keep deterministic/system-only in the first seam:

```text
repository
revision
path / exact locator
required_proposition_state
required_evidence_coverage
mutation_class
exact result_families / Python class names
current cost_class
provider/executor metadata
```

Rationale:

- exact locators remain deterministic authority;
- current allowed catalog should already contain currently admissible candidates;
- admission re-checks preconditions immediately before execution;
- current X1 action space is read-only, so `mutation_class` adds no selection value;
- semantic `evidence_yield` is better planning vocabulary than Python result-class names;
- current one-action `cost_class` cannot affect selection.

Promote a richer `resource_profile` only when real multi-action cost/latency/resource trade-offs exist.

Keep `action_id` rather than `capability_id`: the current trusted entry is a pre-bound action instance, not merely a generic reusable operation definition.

Detailed owner: `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-capability-descriptor-boundary.md`.

## R2.9 — final synthesis / projection proof — ACTIVE NEXT SLICE

Field-level decisions are sufficiently complete. Before implementation:

1. build the final **field / trusted owner / model visibility / why / hidden-authority** table;
2. construct evidence-refined request shapes for:
   - S001 action state;
   - one no-tool state;
   - one richer Level-2 planning-evidence state;
   - one consumed-action/repeat state;
3. inspect them for:
   - duplicate information;
   - authority leakage;
   - stale v2 fields;
   - raw evidence leakage;
   - context starvation;
   - hidden oracle/evaluator hints;
4. do not fabricate a budget-sensitive multi-action example solely to satisfy the plan; note that proof as deferred until a real competing action space exists;
5. reconcile final contradictions;
6. if the projection passes, close R2 and advance to R3.

## R2 pass condition

Every model-visible field has an explicit planning role and a trusted non-model owner where applicable. The request is neither a whole-state/raw-evidence dump nor a label-starved selector interface.

---

# Stage R3 — Freeze `EvidenceGapDecision` + deterministic admission contract

## Question

> What is the smallest model output that preserves useful planning semantics while trusted metadata and execution authorization remain deterministic?

Current candidate:

```text
decision_kind
  ACTION_SELECTED
  QUESTION_SETTLED
  KNOWN_INVESTIGATION_NOT_ADMITTED
  NO_JUSTIFIED_INVESTIGATION_IDENTIFIED

action_id
  trusted action ID | null

explanation
  bounded non-empty text
```

R3 must explicitly reconsider historical model echoes such as:

```text
target_proposition
expected_result_categories
limitations
```

Do not retain them merely because v2 contained them. In particular, exact result families are trusted action metadata and should not need to be echoed by the model.

Deterministic admission/revalidation owns:

- action exists in current catalog;
- hidden exact binding;
- policy/mutation class;
- current preconditions;
- current budget;
- consumed-action repeat boundary;
- exact result contract;
- fresh state immediately before execution.

JSON/schema validity is not semantic correctness or execution authority.

---

# Stage R4 — Build and compare the coherent agent seam

Product runtime remains untouched. Experiment work belongs under:

```text
experiments/
experiments/tests/
```

## R4-A — ordinary-Python reference/control implementation

Implement the evidence-refined context, decision, admission and trace/replay seam using ordinary Python/direct local model integration.

This is a reference/control implementation, not a predetermined winner.

## R4-B — LangGraph implementation/comparison — EXPLICIT LbD SCOPE

Implement the same bounded responsibility with LangGraph and map real UpgradePilot concepts to:

```text
trusted workflow state
→ State / state schema

planner invocation
→ planner node

admission/revalidation
→ deterministic node / transition guard

bounded execution
→ tool/execution node

domain interpretation/state update
→ evidence-update node

continue / no-tool routing
→ conditional edges

future continuation
→ graph loop
```

Learn against real responsibilities: `StateGraph`, state/nodes/edges, conditional routing, persistence/checkpoints, interrupts/HITL concepts, freshness checks, tracing and state-transition observability.

Do not equate learning a feature with adopting it.

## R4-C — LangChain learning/integration slice

Use a smaller bounded slice to understand:

- standard model interfaces;
- agent/tool abstractions;
- tool calling;
- middleware around model/tool execution;
- retries/fallback/early-stop/guardrail concepts;
- relationship to LangGraph runtime.

Do not force the custom EvidenceGapPlanner authority boundary into a generic prebuilt abstraction if that obscures responsibility.

## R4-D — compare implementations

Compare against real criteria:

```text
responsibility clarity
state-transition clarity
deterministic-authority preservation
context projection control
fresh pre-execution validation placement
replay/checkpoint/observability value
failure/retry ownership
testability
debuggability
overhead
learning value
future multi-action/multi-turn extensibility
provider/model integration friction
```

Possible outcomes include plain Python, LangGraph, hybrid use, or framework defer after the learning slice. No result is predetermined.

### R4 proof pressure

Focused tests should prove, across implementations where applicable:

- exact intended model projection;
- normalized dependency transition;
- bounded planning evidence without raw-object dumping;
- `consumed_actions` repeat suppression;
- rejected/stale proposal does not masquerade as consumed execution;
- planning budget semantics;
- `EvidenceGapActionDescriptor` exposes only `action_id/purpose/target_proposition/evidence_yield`;
- hidden locators/preconditions/mutation/result classes remain deterministic;
- action ID rebinds to exact trusted action;
- unknown/stale action rejection;
- experiment/product import direction;
- LangGraph routing preserves the same authority split.

Collect timing/resource telemetry during R4/R5 for later cost-aware planning decisions; do not invent precise estimates beforehand.

---

# Stage R5 — Bounded development/replay proof

Use development/consumed cases as development evidence only.

Minimum proof:

1. one action-selection case;
2. one no-tool case;
3. one structured planning-evidence case;
4. one consumed-action repeat state;
5. one stale/unknown deterministic rejection;
6. exact request/output/state-transition trace for replay;
7. plain-Python vs LangGraph behavior comparison on the same bounded cases;
8. LangChain learning-slice findings where applicable.

Keep model, provider, projection, admission, execution, framework, and replay failure classes separate.

Do not turn development proof into reliability/generalization claims.

---

# Stage R6 — Explicit X1 disposition

Serious outcomes:

```text
RETAIN AS LIMITED PILOT / CONTROL SEAM
DEFER RICHER X1
REJECT
```

Retain + defer can coexist:

```text
retain useful bounded control/learning assets
+
defer richer product planner until real multi-action pressure
```

General adaptive-planner ADOPT is not supported by current evidence alone.

R6 must also state what plain Python / LangGraph / LangChain comparison actually taught or improved without silently converting experiment findings into product architecture.

---

# Stage R7 — Conditional fresh v3 evaluation

Activate only if R6 determines a narrow planner-quality claim needs fresh protected evidence.

```text
freeze exact claim + implementation
→ reserve fresh holdouts before deep analysis
→ freeze v3 protocol/model/config/prompt/schema
→ repeated protected evaluation
→ deterministic + human semantic scoring
→ final narrow disposition
```

Do not reuse exposed S001–S012 as untouched final holdouts.

---

# Stage R8 — Select next independently useful AI/product capability

Serious candidates include:

- broader upstream semantic mechanism discovery;
- exact-head resolver/currentness/satisfiability evidence;
- mediated CI/environment-consumption interpretation;
- richer target artifact/environment evidence;
- targeted behavioral differential reproduction;
- persisted-artifact provenance/history;
- repository-purpose/reproduction-context semantics.

Do not add a capability merely to make the planner multi-action.

---

# Stage R9 — Richer EvidenceGapPlanner reactivation trigger

Reactivate richer planner work when approximately:

```text
2+ independently admitted bounded actions
+
real states where several are plausibly useful
+
relative value/order changes with propositions, planning evidence,
prerequisites, consumed history, failures, time/cost/resource budget
+
small fixed deterministic policy becomes materially brittle,
duplicated, combinatorial or semantically contextual
```

Then build a real loop:

```text
trusted state
→ bounded model observation
→ EvidenceGapPlanner
→ action / no-tool disposition
→ fresh admission
→ execute
→ classify/interpret
→ trusted state update
→ re-plan
```

---

## 10. Current planner-input decision table

| Field / concept | Current decision |
|---|---|
| `planning_question` | model-visible; bounded/project-owned |
| repository / PR / revision | deterministic-only |
| `dependency_transition.normalized_package/old_version/proposed_version` | model-visible |
| proposition `key/state/evidence_coverage/evidence_owner/detail` | model-visible |
| proposition `origin` | not in base first seam |
| `EvidenceGapPlanningEvidence` | selectively model-visible |
| raw Level-3 evidence | excluded by default |
| `consumed_actions` | model-visible action IDs only |
| rejected proposal / provider retry trace | system/evaluator/executor only |
| `planning_budget.remaining_investigations` | model-visible semantic budget |
| time/cost/resource budget | add only when real bounded trade-offs exist |
| executor timeout/retry/backoff | deterministic operational policy |
| action `action_id/purpose/target_proposition/evidence_yield` | model-visible |
| action locators/preconditions/mutation/result-class contract | deterministic-only |
| current `cost_class` | trusted/system-side until real trade-off exists |
| evaluator/oracle metadata | excluded |

---

## 11. AI/agent-engineering learning map

### Direct current-route learning

- context engineering / model observation;
- semantic extraction vs grounding;
- proposition state;
- structured planning evidence;
- action space vs execution authority;
- general capability vs bound action instance;
- semantic evidence yield vs implementation result types;
- consumed-action history;
- semantic retry vs transport retry;
- planning budget vs execution policy;
- structured output / schema;
- deterministic admission;
- TOCTOU / stale-plan revalidation;
- state transitions / loops;
- replay / reproducibility;
- failure taxonomy / observability;
- deterministic-baseline comparison.

### Explicit R4 framework learning

- LangGraph StateGraph / state / nodes / edges / routing;
- persistence/checkpoint value and cost;
- interrupts/HITL concepts;
- LangChain model/tool/agent abstractions;
- middleware/lifecycle hooks;
- framework runtime vs UpgradePilot domain/control ownership;
- framework learning vs adoption.

---

## 12. Modification boundary

Normally allowed while executing this plan:

- `experiments/`;
- `experiments/tests/`;
- this plan when real execution evidence changes it;
- dated `working-memory/`;
- `MEMORY.md` when live continuation changes.

R4 may add experiment-only LangGraph/LangChain dependencies/configuration required for the bounded comparison, following the active Build/LbD procedure and without silently making them product runtime dependencies.

Separate explicit product/architecture ownership is required for:

- `src/upgradepilot/` planner integration;
- accepted specification/ADR changes;
- product framework/dependency adoption;
- provider/security policy changes;
- broad product-simulation scope changes.

---

## 13. Prohibited scope / claim limits

Do not:

- fabricate a second action;
- claim general adaptive-planner value from S001;
- integrate product planner/framework runtime automatically after experiment success;
- adopt LangGraph/LangChain merely because they were learned;
- reject them merely because plain Python can implement the flow;
- pass whole evidence object graphs/raw external text without demonstrated need;
- reduce planner state permanently to labels when richer structured evidence matters;
- let the model invent locators/authority;
- expose deterministic preconditions merely to make the model check them;
- require the model to echo exact result class families merely because v2 did;
- treat schema validity as semantic correctness;
- treat model proposal as execution authorization;
- treat rejected proposals/transient transport attempts as consumed investigations;
- let provider retries automatically consume multiple semantic planner actions;
- invent precise time/cost estimates without trustworthy measurement;
- reuse contaminated v2 material as clean protected evidence;
- continue product simulation merely for more cases;
- turn history into free-form LLM memory;
- make compatibility/safety/maintainer claims from planner output.

---

## 14. Overall pass condition

The project can state with inspectable evidence:

```text
what EvidenceGapPlanner owns
what exact model observation it receives and why
what full trusted state remains hidden and why
what counts as consumed investigation history
what planning budget means
what the action descriptor exposes and hides
what EvidenceGapDecision may propose
what deterministic admission/execution still owns
how ordinary Python implements the seam
how LangGraph implements the same seam
what LangChain abstractions add/remove/teach
which implementation fits which responsibility
what current evidence proves and does not prove
whether the bounded seam is retained/rejected/deferred
whether fresh v3 is justified
what independent capability comes next
when richer planning reopens
```

The learner should be able to trace:

```text
trusted evidence
→ domain interpretation / grounding
→ propositions + selected planning evidence
→ bounded model observation
→ EvidenceGapPlanner
→ structured decision
→ deterministic admission/revalidation
→ bounded execution
→ domain interpretation
→ trusted state + consumed-action update
→ optional next turn
```

without confusing framework concepts with product authority.

---

## 15. Final stop line

The end of this plan is **not** automatically product integration or framework adoption.

A successful result may be:

```text
bounded planner/control experiment retained
+
LangGraph/LangChain learned and compared against real UpgradePilot responsibilities
+
one implementation/hybrid preferred for future work, or framework adoption deferred
+
richer planner expansion deferred until genuine multi-action pressure
+
next independent capability selected
```
