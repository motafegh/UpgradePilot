# B2/X1 Post-Research EvidenceGapPlanner Learning-by-Doing Implementation Plan

**Status:** AUTHORIZED PLAN ARTIFACT — position-neutral; `MEMORY.md` alone selects live activation  
**Date:** 2026-08-30  
**Revision:** evidence-refined after R0/R1 and progressive R2 design  
**Responsibility:** finish the post-E1–E5 B2/X1 planner decision by defining, building, comparing, and evaluating the smallest honest `EvidenceGapPlanner` experimental seam, then make an explicit X1 disposition without manufacturing multi-action value or prematurely integrating product runtime  
**Primary method:** Learning-by-Doing / Building  
**Product runtime integration:** NOT authorized by this plan itself

---

## 1. Why this plan exists

UpgradePilot has completed:

1. main-side E1–E5 evidence-first exploration; and
2. delegated product-simulation capability/value research.

Together they established:

```text
bounded typed-state reasoning works
closed action binding works
structured output and deterministic admission have distinct responsibilities
explicit no-tool semantics matter
real additional product capabilities exist
but a second capability is not yet justified for LLM-owned selection
general adaptive-planner advantage over a small deterministic policy is not proven
```

The next work must avoid both extremes:

```text
UNDER-ENGINEERING
→ dismiss the planner/agent work because the first S001 seam is simple

OVER-ENGINEERING
→ manufacture capabilities/framework machinery only to make the system look agentic
```

The project should instead build enough real agent-engineering surface to learn from and evaluate honestly, while keeping product authority and claims bounded by evidence.

---

## 2. Applicable owners and evidence

Use the smallest relevant chain for each slice.

### Controlling/procedural owners

- `../AGENTS.md`
- `../OPERATING_GUIDE.md`
- `.agents/skills/upgradepilot-planning-design/SKILL.md`
- `.agents/skills/upgradepilot-build-implement/SKILL.md`
- `.agents/skills/upgradepilot-learning-by-doing/SKILL.md`
- `README.md`

### Stable technical owners

- `../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`
- `../docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`
- `../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`
- `../docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md`

### Immediate continuity/evidence

- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-model-visible-context.md`
- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-planning-question.md`
- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-proposition-projection.md`
- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-action-history-and-retry-boundary.md`
- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R0-R1-responsibility-vocabulary.md`
- E1–E5 dated working memories
- `../working-memory/2026-08-28_B2-X1-product-simulation-capability-research-response.md`
- `B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md`
- historical `B2_X1_PHASE3_EVALUATION_PROTOCOL.md`

Do not re-open all historical material for every step.

---

## 3. Bounded outcome

This plan is complete when UpgradePilot has:

1. precise responsibility-oriented `EvidenceGapPlanner` / `EvidenceGapDecision` vocabulary;
2. an explicit model-visible context contract;
3. an explicit planning-budget contract;
4. an explicit model-visible capability/action descriptor boundary;
5. a coherent ordinary-Python experimental reference seam;
6. a bounded LangGraph implementation of the same responsibility for real comparison and learning;
7. a smaller LangChain learning/integration slice where its higher-level agent/tool/middleware abstractions intersect the same responsibility;
8. focused tests/replay evidence for the selected contracts;
9. an evidence-backed X1 disposition;
10. a decision on whether fresh v3 protected evaluation is justified;
11. a selected next independently useful AI/product capability direction or explicit defer;
12. a clear trigger for richer multi-action/multi-turn planning;
13. material LbD closure for the concepts actually encountered.

This plan does **not** require general adaptive-planner product adoption or framework adoption.

---

## 4. Responsibility being evaluated

Working component:

**`EvidenceGapPlanner`**

Working responsibility:

> Given one bounded UpgradePilot planning question, trusted typed proposition state, selected bounded structured planning evidence, trusted consumed-investigation history, a bounded planning budget, and a closed set of admitted bounded investigation capabilities, identify the material evidence gap that should be addressed next and select one useful admitted capability, or return an explicit no-tool disposition when no capability should execute.

The model does **not** own:

- repository/source authority;
- dependency identity/version truth;
- exact locator invention;
- action-catalog creation;
- execution authorization;
- evidence parsing/promotion;
- proposition truth/proof-strength composition;
- compatibility/safety/merge truth;
- maintainer action;
- target mutation;
- final trusted investigation state.

The accepted Product Decision Model already owns the framework-independent investigation semantics. `EvidenceGapPlanner` is a candidate implementation method for part of that responsibility.

---

## 5. Learning-by-Doing execution rule

Each substantive stage follows this loop proportionately:

```text
A. ORIENT
   establish only the concepts/dataflow/owners needed for the next real slice

B. USER REASONING
   learner predicts/challenges/selects/explains a material point when useful

C. REAL BOUNDED WORK
   design / implement / evaluate one actual slice

D. INSPECT ACTUAL EVIDENCE
   source/tests/model output/replay/result

E. CORRECT THE MENTAL MODEL
   observation vs interpretation vs remaining uncertainty

F. PRESERVE MATERIAL STATE
   working memory / MEMORY / plan only when continuation materially changes

G. TEACHING CLOSURE
   explain what changed, why, what concept was demonstrated, and what remains deferred
```

Do not turn every edit or command into ceremony.

### Framework/LbD rule

Do **not** interpret proportionality as a ban on new tools/frameworks.

```text
new tool only because it is fashionable
→ not justified

new tool because it gives meaningful learning exposure
AND is attached to a real project responsibility
AND can be compared against a real baseline
→ justified bounded experiment
```

Learning value is a legitimate project value. A framework does not need to be impossible to replace with plain Python before it can earn a bounded learning/comparison slice.

Adoption and learning/comparison remain different decisions.

---

# Stage R0 — Re-anchor baseline

**Status:** COMPLETE / PASS.

Confirm current live state without reopening completed E1–E5 or product-simulation research.

Stop line: no broad restart merely because a new session begins.

---

# Stage R1 — Responsibility vocabulary

**Status:** COMPLETE.

Current working vocabulary:

```text
EvidenceGapPlanner
EvidenceGapDecision
EvidenceGapDecisionKind
```

Preferred meanings:

```text
ACTION_SELECTED
QUESTION_SETTLED
KNOWN_INVESTIGATION_NOT_ADMITTED
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

Historical short names remain evidence only.

---

# Stage R2 — Freeze model-visible context contract

## R2 question

What exact trusted information should the `EvidenceGapPlanner` receive, and why does each field belong at the model boundary?

## Current candidate request

```text
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
    # later dimensions only when real evidence justifies them

allowed_actions
    planner-useful bounded capability descriptors

output_schema / structured-output contract
```

Trusted but hidden from the model by default:

```text
repository
pull_number
immutable revision
exact action locators
raw provider/source objects
full execution/audit trace
oracle/evaluator metadata
```

## R2.1 — planning question — DECIDED

One concise project-owned `planning_question` is model-visible.

It defines the bounded uncertainty being advanced. It must not smuggle structured evidence, repository identity, expected action, expected disposition, or oracle hints into prose.

A future question-formulation agent remains a separate hypothesis only when choosing the question itself becomes materially non-trivial.

## R2.2 — target/case identity — DECIDED

Do not pass repository / PR / revision to the current model request.

They remain trusted for trace, acquisition, binding, replay, freshness and admission.

## R2.3 — dependency transition — DECIDED

Pass:

```text
normalized_package
old_version
proposed_version
```

Use canonical normalized identity rather than source presentation spelling.

## R2.4 — proposition projection — DECIDED

Pass:

```text
key
state
evidence_coverage
evidence_owner
detail
```

Do not add experiment-only `origin` or `raw_external_text` fields to the base first-seam proposition contract.

`detail` is intentionally bounded/project-interpreted text, not arbitrary raw external prose.

## R2.5 — `EvidenceGapPlanningEvidence` — CONCEPT DECIDED

Propositions are the state spine, not the entire reasoning input.

`EvidenceGapPlanningEvidence` is selected structured evidence whose mechanism, witness, limitation, reason, or unresolved condition can change which investigation has the highest discriminating value.

Examples may include bounded structured CI consumption/direct-exercise distinctions, reachability/witness paths, target-Python interpretation, grounded upstream mechanism facts, environment conditions, structured change-scope facts, and deterministically interpreted command semantics.

Default:

```text
Level 1 = propositions
Level 2 = selected EvidenceGapPlanningEvidence
Level 3 = raw evidence

model receives Level 1 + selected Level 2
Level 3 remains outside by default
```

## R2.6 — planner-visible action history — DECIDED

Replace the historical generic concept:

```text
attempted_actions: [{action_id, outcome}]
```

with the first-seam working concept:

```text
consumed_actions: [action_id]
```

An investigation becomes consumed only after an admitted bounded execution yields a trusted typed result or typed domain/evidence problem for the bounded state.

Do not count as consumed:

- model proposal rejected by admission;
- pre-execution stale/pruned action;
- transient provider timeout/transport/rate-limit failure;
- untrusted provider response that never became valid domain evidence.

Material findings belong in updated propositions / planning evidence, not free-form history prose.

Transport retry remains deterministic executor/provider policy, not semantic replanning.

## R2.7 — planning budget — ACTIVE NEXT SLICE

Replace vague `remaining_steps` with a responsibility-oriented planning budget.

First-seam candidate:

```text
planning_budget:
    remaining_investigations: int
```

Starting lifecycle hypothesis to validate:

```text
model proposes action
→ no planning investigation spent

admission accepts
→ still not spent

fresh pre-execution validation passes
→ bounded investigation execution begins
→ spend one planning-investigation unit

internal deterministic provider retries
→ do not spend additional planner-investigation units
```

Do not treat all resources as one scalar.

Potential future budget dimensions include:

```text
remaining_time_seconds
remaining_external_cost
compute/network resource envelope
```

but add them to **model-visible planning state only when**:

1. the resource is actually bounded/measured;
2. alternative admitted actions materially differ on that resource;
3. the planner can use the value to make a better discriminating choice;
4. capability descriptors contain trustworthy enough cost/latency information to reason against it.

Keep executor/provider controls separate:

```text
request timeout
retry limit
backoff
rate-limit handling
provider-specific operational limits
```

These may consume real time/resources without automatically becoming additional semantic planner actions.

## R2.8 — allowed capability descriptors — PENDING

Planner-visible action information should explain what evidence a capability can obtain and what it requires, without transferring action definition/authority to the model.

Candidate fields:

```text
action_id
purpose
target proposition / evidence gap
required proposition/evidence precondition
cost / latency / resource class when trustworthy and planning-relevant
mutation class
result-family summary
```

Exact locator/authority metadata remains deterministic-only by default.

## R2 proof method

Before implementation, produce a final field/owner/why-visible/why-hidden table and render representative requests for:

- one S001 action state;
- one no-tool state;
- one richer Level-2 planning-evidence state;
- one consumed-action/repeat state;
- one budget-sensitive state when the admitted action space actually supports it.

## R2 pass condition

Every model-visible field has an explicit planning role and non-model authority where appropriate. The request is neither a raw-state dump nor a label-starved selector interface.

---

# Stage R3 — Freeze `EvidenceGapDecision` + deterministic admission contract

Question:

> What is the smallest model result that preserves useful planning semantics while trusted metadata/authorization stay deterministic?

Candidate:

```text
decision_kind
  ACTION_SELECTED
  QUESTION_SETTLED
  KNOWN_INVESTIGATION_NOT_ADMITTED
  NO_JUSTIFIED_INVESTIGATION_IDENTIFIED

action_id
  trusted ID | null

explanation
  non-empty bounded text
```

Trusted code must rebind/revalidate action catalog, exact locators, preconditions, mutation class, result families, current budget and current trusted state immediately before execution.

JSON/schema validity is not semantic correctness or execution authority.

---

# Stage R4 — Build and compare the coherent agent seam

## R4 question

Can the evidence-refined design exist as an understandable executable agent workflow, and what implementation method gives UpgradePilot the best combination of clarity, control, capability, learning value and future extensibility?

Product runtime remains untouched. Work stays under:

```text
experiments/
experiments/tests/
```

unless a later explicit product-integration decision changes that boundary.

## R4-A — ordinary-Python reference implementation

Build the smallest coherent reference seam using ordinary Python/direct local model integration.

It should own, at experiment level:

1. `EvidenceGapPlannerContext` projection;
2. dependency-transition/proposition/planning-evidence projection;
3. `consumed_actions` and planning-budget state;
4. model request/response boundary;
5. structured decision parsing;
6. trusted action lookup/rebinding;
7. deterministic admission/revalidation;
8. deterministic trace/replay output.

This is a **reference/control implementation**, not a predetermined winner.

## R4-B — LangGraph implementation/comparison — EXPLICITLY AUTHORIZED FOR LbD

Build the **same bounded responsibility** using LangGraph rather than inventing a different product capability.

Map the real UpgradePilot concepts to LangGraph concepts such as:

```text
trusted workflow state
→ State / state schema

planner invocation
→ planner node

deterministic admission/revalidation
→ admission node / transition guard

bounded capability execution
→ tool/execution node

domain interpretation + trusted update
→ evidence/state-update node

continue / stop / defer / unresolved routing
→ conditional edges

future multi-turn continuation
→ graph loop
```

Explore only features that attach to real current/future responsibilities, including where useful:

- `StateGraph` state/nodes/edges;
- conditional routing;
- persistence/checkpoints for replay/fault tolerance learning;
- interrupts/human-in-the-loop concept where it maps to authorization boundaries;
- pre-execution freshness/revalidation placement;
- graph tracing/state-transition observability.

Do not adopt persistence/checkpointing or other features merely because the framework offers them; **learn them against our real flow and compare their value**.

## R4-C — LangChain learning/integration slice

Add a smaller bounded LangChain slice to understand its higher-level abstractions relative to our lower-level controlled seam.

Focus on concepts that intersect UpgradePilot:

- standard model interface;
- `create_agent` / agent loop;
- tool definitions/calling;
- middleware hooks around model/tool execution;
- retries/fallback/early-stop/guardrail concepts;
- relationship to LangGraph runtime.

Do not force `EvidenceGapPlanner` into a generic prebuilt agent abstraction if doing so obscures its custom state/admission/evidence boundaries.

## R4-D — implementation comparison

Compare plain Python, LangGraph, and the relevant LangChain slice using real criteria:

```text
responsibility clarity
state-transition clarity
ability to preserve deterministic authority
context projection control
pre-execution revalidation placement
replay/checkpoint/observability value
failure/retry ownership clarity
testability
debuggability
implementation overhead
learning value
future multi-action/multi-turn extensibility
provider/model integration friction
```

The comparison may support:

```text
plain Python retained
LangGraph retained
hybrid use
framework deferred after learning slice
```

No result is predetermined.

### Important framework rule

```text
plain Python can implement it
!= framework has no value

framework is educational/powerful
!= framework should become product architecture
```

Framework **adoption** requires a later evidence-backed architecture/product decision. Framework **learning/comparison** is explicitly part of R4.

## R4 tests

Focused tests should prove the same semantics across implementations where applicable:

- intended model projection / excluded authority fields;
- normalized dependency transition;
- selected planning evidence without raw-object dumping;
- consumed action suppresses blind semantic repetition;
- rejected/stale proposal does not masquerade as consumed execution;
- planning budget semantics;
- output cannot redefine trusted action metadata;
- unknown/stale action rejection;
- experiment/product import direction;
- LangGraph state/edge routing preserves the same authority split rather than silently broadening it.

Do not create a generalized framework test platform before evidence requires one.

---

# Stage R5 — Bounded development/replay proof

Use development/consumed cases as development evidence only.

Minimum proof:

1. one action-selection case;
2. one no-tool case;
3. one structured planning-evidence case;
4. one consumed-action repeat suppression case;
5. one deterministic stale/unknown rejection case;
6. exact request/output/state-transition trace sufficient for replay;
7. plain-Python vs LangGraph behavior comparison on the same bounded cases;
8. LangChain learning slice findings where applicable.

Keep failure classes separate:

```text
model reasoning
structured-output/provider
projection bug
admission rejection
execution/acquisition
framework orchestration
replay/test harness
```

Do not turn development proof into reliability/generalization claims.

---

# Stage R6 — Explicit current X1 disposition

Serious outcomes:

### RETAIN AS LIMITED PILOT / CONTROL SEAM

Retain the bounded planning architecture/experiment because it is useful for learning, evaluation, reusable state/control mechanics or future expansion, while general adaptive-planner advantage remains unproven.

### DEFER RICHER X1

Defer richer product planning until independently justified capabilities create a genuine non-trivial selection/sequencing problem.

These may coexist:

```text
retain bounded pilot/control assets
+
defer richer product-planner expansion
```

### REJECT

Only if even the bounded seam/control/learning asset is not worth retaining.

General adaptive-planner ADOPT is not supported by current evidence alone.

The R6 record must also state which implementation method(s)—plain Python, LangGraph, LangChain-assisted/hybrid—were useful and why, without silently converting an experiment result into product architecture.

---

# Stage R7 — Conditional fresh v3 evaluation

Activate only if R6 determines the narrow pilot claim needs fresh planner-quality evidence.

Sequence:

```text
freeze exact claim + implementation being evaluated
→ screen/reserve fresh holdouts before deep analysis
→ freeze v3 protocol/model/config/prompt/schema
→ repeated protected evaluation
→ deterministic + human semantic scoring
→ final narrow disposition
```

Do not reuse exposed S001–S012 as untouched final holdouts.

---

# Stage R8 — Select next independently useful AI/product capability

Candidate directions include:

- broader upstream semantic mechanism discovery;
- exact-head resolver/currentness/satisfiability evidence;
- mediated CI/environment-consumption interpretation;
- richer target artifact/environment evidence;
- targeted behavioral differential reproduction;
- persisted-artifact provenance/history;
- repository-purpose/reproduction-context semantics.

Each must earn its own method based on recurring responsibility, proof need, strongest deterministic baseline, safe boundary, product value, AI value and learning value.

Do not add a capability merely to make the planner multi-action.

---

# Stage R9 — Richer EvidenceGapPlanner reactivation trigger

Reactivate richer planner work when evidence shows approximately:

```text
2+ independently admitted bounded capabilities
+
real states where several are plausibly useful
+
relative value/order changes with proposition state, planning evidence,
prerequisites, consumed history, failures, time/cost/resource budget
+
small fixed deterministic policy becomes materially brittle,
duplicated, combinatorial, or semantically contextual
```

Then the learning/build target becomes a real loop:

```text
trusted state
→ bounded model observation
→ EvidenceGapPlanner
→ choose action / no-tool disposition
→ fresh deterministic admission
→ execute
→ classify/interpret
→ update trusted state
→ re-plan
```

At that point, LangGraph persistence/checkpoints, richer graph routing, LangChain middleware/tool patterns, and other agent-runtime mechanisms can be reevaluated from much stronger product pressure.

---

## 10. Current planner-input decision table

| Field / concept | Current decision |
|---|---|
| `planning_question` | model-visible; bounded/project-owned |
| repository / PR / revision | deterministic-only |
| `dependency_transition.normalized_package/old_version/proposed_version` | model-visible |
| proposition `key/state/evidence_coverage/evidence_owner/detail` | model-visible |
| proposition `origin` | not in base first-seam contract |
| `EvidenceGapPlanningEvidence` | selectively model-visible |
| raw Level-3 evidence | excluded by default |
| `consumed_actions` | model-visible action IDs only for first seam |
| rejected proposal / provider retry trace | system/evaluator/executor only |
| `planning_budget.remaining_investigations` | candidate first-seam model-visible budget |
| time/cost/resource budget | add only when real bounded trade-offs exist |
| executor timeout/retry/backoff | deterministic operational policy |
| allowed action purpose/preconditions/resource profile | model-visible when useful |
| exact action locators | deterministic-only |
| evaluator/oracle metadata | excluded |

---

## 11. AI/agent-engineering learning map

### Directly learned through current route

- semantic extraction vs grounding;
- context engineering / model observation;
- typed proposition state;
- structured planning evidence;
- action spaces/capability catalogs;
- consumed-action history;
- semantic retry vs transport retry;
- planning budget vs execution resource policy;
- structured output / JSON Schema;
- deterministic admission/guardrails;
- TOCTOU / stale-plan revalidation;
- state transitions / loops;
- replay/reproducibility;
- failure taxonomy/observability;
- deterministic-baseline comparison.

### Explicit R4 framework learning

- LangGraph `StateGraph`, state, nodes, edges, conditional routing;
- persistence/checkpoints and their actual value/cost;
- interrupts/HITL concepts;
- LangChain agent/model/tool abstractions;
- LangChain middleware/lifecycle hooks;
- framework runtime vs domain responsibility;
- framework adoption vs framework learning.

### Later only when real responsibilities activate them

- richer checkpointing/persistence stores;
- model routing/fallbacks;
- LLM-as-a-judge;
- MCP;
- RAG;
- multi-agent/subagent systems;
- generalized middleware/orchestration infrastructure.

---

## 12. Modification boundary

Normally allowed while executing this plan:

- `experiments/`;
- `experiments/tests/`;
- this plan when a real ambiguity is discovered;
- dated `working-memory/`;
- `MEMORY.md` when live continuation changes.

R4 may add experiment-only LangGraph/LangChain dependencies/configuration needed for the bounded comparison, subject to the active Build/LbD procedure and without silently making them product runtime dependencies.

Separate product/architecture decision remains required for:

- `src/upgradepilot/` planner integration;
- accepted specifications/ADRs;
- product dependency/framework adoption;
- provider/security policy changes;
- broad product-simulation scope changes.

---

## 13. Proof hierarchy

```text
design/naming claim
→ responsibility trace + specs + recall test

context/budget projection claim
→ rendered request/state + focused deterministic tests

admission claim
→ deterministic tests + counterfactual rejection

framework learning/implementation claim
→ actual equivalent workflow implementation + traces/tests

model capability claim
→ actual local model behavior

reliability/generalization
→ repeated fresh protected evaluation

product behavior/adoption
→ product source/tests/runtime + explicit architecture/build decision
```

Plan text itself is never implementation proof.

---

## 14. Prohibited scope

Do not:

- fabricate a second action;
- claim general adaptive-planner value from S001;
- integrate product planner/framework runtime automatically after experiment success;
- collapse semantic discovery and planning;
- adopt LangGraph/LangChain merely because they were learned;
- reject LangGraph/LangChain merely because plain Python can implement the flow;
- pass whole evidence object graphs/raw external text without demonstrated need;
- reduce planner state permanently to labels when richer structured evidence is useful;
- let the model invent locators/authority;
- treat schema validity as semantic correctness;
- treat model proposal as execution authorization;
- treat rejected proposals or transient transport attempts as consumed investigations;
- let provider retries automatically consume multiple semantic planner actions;
- invent precise time/cost estimates with no trustworthy measurement;
- reuse contaminated v2 material as clean protected evidence;
- continue product simulation merely for more cases;
- create a new plan after every stage;
- turn history into free-form LLM memory;
- make compatibility/safety/maintainer claims from planner output.

---

## 15. Reassessment triggers

Reassess when:

1. a second independently justified capability creates real competing-action states;
2. richer upstream semantics materially expand planning state;
3. structured planning evidence still loses decision-critical information;
4. raw/near-raw evidence becomes demonstrably necessary;
5. framework comparison exposes a materially better/worse authority or orchestration fit;
6. reliable timing/cost/resource measurements become available and action choice depends on them;
7. local model/provider behavior changes materially;
8. a fresh real failure contradicts the current responsibility split;
9. planner value is consistently dominated by a smaller deterministic policy;
10. product/framework integration is explicitly selected.

---

## 16. Overall pass condition

The project can state with inspectable evidence:

```text
what EvidenceGapPlanner owns
what context it sees and why
what it does not see and why
what counts as consumed investigation history
what budget is planner-visible vs executor-owned
what decision it may propose
what deterministic code still owns
how ordinary Python implements the seam
how LangGraph implements the same seam
what LangChain abstractions teach/add/remove
which implementation is preferable for which responsibility
what current evidence proves and does not prove
whether the bounded seam is retained/rejected/deferred
whether fresh v3 is justified
what independent capability comes next
when richer planning reopens
```

And the learner can trace:

```text
trusted evidence
→ domain interpretation / grounding
→ propositions + selected planning evidence
→ bounded model observation
→ EvidenceGapPlanner
→ structured decision
→ deterministic admission/revalidation
→ bounded execution
→ domain result/problem interpretation
→ trusted state + consumed-action update
→ optional next turn
```

in both the framework-independent mental model and the concrete ordinary-Python/LangGraph implementations.

---

## 17. Final stop line

The end of this plan is **not** automatically product integration or framework adoption.

A valid result may be:

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

That is a successful evidence-backed LbD engineering outcome.
