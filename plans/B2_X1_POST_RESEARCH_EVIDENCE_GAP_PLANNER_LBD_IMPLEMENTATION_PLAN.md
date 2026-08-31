# B2/X1 Post-Research EvidenceGapPlanner Learning-by-Doing Implementation Plan

**Status:** AUTHORIZED PLAN ARTIFACT — position-neutral; `MEMORY.md` alone selects live activation  
**Date:** 2026-08-30  
**Revision:** R4-A1/A2 focused-runtime proven; R4-A3 bounded local model seam next  
**Responsibility:** finish the post-E1–E5 B2/X1 planner decision by defining, building, comparing, learning, and evaluating the smallest honest `EvidenceGapPlanner` experimental seam, then make an explicit X1 disposition without manufacturing multi-action value or prematurely integrating product runtime  
**Primary method:** Learning-by-Doing / Building  
**Product runtime integration:** NOT authorized by this plan itself

---

## 1. Why this plan exists

UpgradePilot has established through E1–E5 and delegated capability research that bounded typed-state reasoning, closed action binding, structured output, deterministic admission, and explicit no-tool semantics are useful. It also established that the current one-action seam does **not** prove general adaptive-planner superiority and that no second action should be fabricated merely to make the system look agentic.

The route therefore avoids both:

```text
UNDER-ENGINEERING
→ dismiss useful planner/agent work because the first seam is simple

OVER-ENGINEERING
→ manufacture capabilities/framework machinery for appearance rather than responsibility
```

The project should build enough real agent-engineering surface to learn from and evaluate honestly while keeping authority and claims bounded by evidence.

Learning and implementation are one coordinated journey here. The plan must therefore prevent both:

```text
BUILD DRIFT
→ implementation outruns Ali's understanding/ownership

LEARNING DRIFT
→ detached theory delays the real implementation without helping the next decision
```

---

## 2. Applicable owners

Use the smallest relevant chain for each slice.

### Controlling/procedural

- `../AGENTS.md`
- `../OPERATING_GUIDE.md`
- `.agents/skills/upgradepilot-planning-design/SKILL.md`
- `.agents/skills/upgradepilot-build-implement/SKILL.md`
- `.agents/skills/upgradepilot-learning-by-doing/SKILL.md`
- `README.md`

### Stable technical

- `../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`
- `../docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`
- `../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`
- `../docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md`

### R4 learning-depth companion

- `B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`

This selected implementation plan owns **what is built, in what sequence, with what proof and stop line**. The R4 learning-depth companion owns **what Ali should understand now, what is learned when first used materially, what remains deferred, and what concrete trigger reopens deeper study**. Neither replaces the project-wide LbD method in `AGENTS.md` / `OPERATING_GUIDE.md`.

### Immediate continuity

- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R0-R1-responsibility-vocabulary.md`
- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-model-visible-context.md`
- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-final-request-projection-proof.md`
- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R3-decision-semantics.md`
- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R3-wire-and-admission-contract.md`
- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R4A1-boundary-types-and-projection.md`
- `../working-memory/2026-08-31_B2-X1-EvidenceGapPlanner-R4A1-planning-evidence-naming-refinement.md`
- `../working-memory/2026-08-31_B2-X1-EvidenceGapPlanner-R4A2-deterministic-action-admission.md`
- `../working-memory/2026-08-31_B2-X1-EvidenceGapPlanner-R4A2-focused-runtime-failure-and-test-repair.md`
- E1–E5 dated working memories
- `../working-memory/2026-08-28_B2-X1-product-simulation-capability-research-response.md`
- historical `B2_X1_PHASE3_EVALUATION_PROTOCOL.md`

Do not reopen all historical material for every step.

---

## 3. Bounded outcome

This plan is complete when UpgradePilot has:

1. precise `EvidenceGapPlanner` / `EvidenceGapDecision` responsibility vocabulary;
2. an explicit model-visible input contract;
3. an explicit planning-budget and action-space contract;
4. a frozen `EvidenceGapDecision` semantic/wire contract;
5. a frozen deterministic admission contract;
6. a coherent ordinary-Python experiment reference/control seam;
7. the same bounded responsibility implemented with LangGraph for real comparison/LbD;
8. a smaller LangChain agent/tool/middleware learning slice;
9. focused tests/replay evidence;
10. an evidence-backed X1 disposition;
11. a decision on whether fresh v3 protected evaluation is justified;
12. a selected next independently useful AI/product capability direction or explicit defer;
13. a clear trigger for richer multi-action/multi-turn planning;
14. material LbD closure for concepts actually encountered;
15. a traceable learning-depth path showing what was understood at practical depth, what deepened through repeated use, and what remained correctly deferred behind explicit re-entry triggers.

This plan does **not** require general adaptive-planner product adoption or framework adoption.

---

## 4. Candidate responsibility

**`EvidenceGapPlanner`**

> Given one bounded UpgradePilot planning question, trusted typed proposition state, selected bounded structured planning evidence, trusted consumed-investigation history, a bounded planning budget, and a closed set of currently admitted bounded investigation actions, identify the material evidence gap that should be addressed next and select one useful action, or explicitly decide why no action should execute now.

The model does **not** own repository/source authority, dependency truth, exact locators, action-catalog creation, execution authorization, evidence promotion, proposition truth, proof strength, compatibility/safety/merge truth, maintainer action, target mutation, or final trusted investigation state.

---

## 5. Learning-by-Doing execution rule

Each substantive stage follows proportionately:

```text
ORIENT
→ USER REASONING
→ REAL BOUNDED WORK
→ INSPECT ACTUAL EVIDENCE
→ CORRECT THE MENTAL MODEL
→ PRESERVE MATERIAL STATE
→ TEACHING CLOSURE
→ CONTINUE / DEEPEN / STOP
```

Do not turn every edit/command into ceremony.

### R4 dual-track slice contract

For every material R4 implementation increment, establish proportionately before or around the action:

```text
BUILD TARGET
What one real responsibility changes in this slice?

LEARNING TARGET
Which code/syntax/concepts actually carry that responsibility?
What depth is required now?

DEFERRED DEPTH
Which nearby concepts are intentionally not being learned deeply yet?
What concrete trigger would reopen them?

PROOF TARGET
What focused source/test/runtime evidence should this slice produce?
What stronger claim will it not prove?

OWNERSHIP POINT
What should Ali be able to predict, explain, challenge, select, modify,
test, or diagnose after the needed premises exist?

STOP / CONTINUE
After inspecting real evidence, should we:
- continue to the next bounded implementation slice;
- pause briefly to deepen/repair one concept because it now affects correctness,
  authority, debugging, or design choice;
- repeat/practise a central mechanism for stronger ownership;
- or stop because the selected responsibility/proof is complete?
```

The full depth/re-entry mapping for R4 is owned by `B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`. Do not rely on chat memory to remember deferred topics.

### Learning depth is allowed to change over time

A concept does not receive one permanent depth assignment.

```text
first real use
→ minimum-complete practical understanding

repeated central use
→ stronger independent ownership

later implementation makes internals decision-relevant
→ deliberately deepen the same concept

no material trigger
→ keep deeper mechanics deferred
```

Do not block progress for incidental syntax. Do pause when misunderstanding a mechanism would affect the next material engineering decision or proof.

### Framework/LbD rule

```text
new tool only because fashionable
→ not justified

new tool because meaningful learning attaches to a real UpgradePilot responsibility
AND it can be compared against a real baseline
→ justified bounded experiment
```

Learning/comparison and product adoption remain separate decisions.

---

# Stage R0 — Baseline

**Status:** COMPLETE / PASS.

---

# Stage R1 — Responsibility vocabulary

**Status:** COMPLETE.

Working names:

```text
EvidenceGapPlanner
EvidenceGapDecision
EvidenceGapDecisionKind
```

---

# Stage R2 — Model-visible context contract

**Status:** COMPLETE / PASS.

Detailed proof:

`../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-final-request-projection-proof.md`

Final model observation, using the current active R4 type name for the structured evidence representation:

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
    detail

planning_evidence
    PlanningEvidence[]

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

output_schema / provider structured-output contract
```

Historical R2 records may still use the earlier design label `EvidenceGapPlanningEvidence`; active R4 source/tests use `PlanningEvidence`. The semantic boundary is unchanged.

Trusted but model-hidden by default:

```text
repository
pull_number
immutable revision
raw Level-3 evidence
exact action locators
exact action preconditions
mutation policy
exact result-family/class contract
provider/executor retry policy
full execution/audit trace
oracle/evaluator metadata
```

### Key R2 decisions

- canonical `normalized_package + old_version + proposed_version` transition;
- proposition `key/state/evidence_coverage/evidence_owner/detail`;
- selected structured `PlanningEvidence` rather than raw evidence dumping or label starvation;
- `consumed_actions: [action_id]` rather than generic attempt/outcome history;
- `planning_budget.remaining_investigations`, spent when fresh-admitted execution actually begins;
- `EvidenceGapActionDescriptor(action_id, purpose, target_proposition, evidence_yield)`;
- real time/cost/resource dimensions deferred until measured competing-action trade-offs exist.

No fabricated multi-action cost case was created.

---

# Stage R3 — EvidenceGapDecision semantics + admission

**Status:** COMPLETE / PASS.

Detailed owners:

- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R3-decision-semantics.md`
- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R3-wire-and-admission-contract.md`

## R3 decision semantics

Use:

```text
ACTION_SELECTED
QUESTION_SETTLED
KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

The rename from `KNOWN_INVESTIGATION_NOT_ADMITTED` avoids collision with the separate deterministic action-admission lifecycle.

### No-tool umbrella

```text
NO-TOOL
├── QUESTION_SETTLED
├── KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY
└── NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

Historical `stop` is intentionally **not** mapped one-to-one:

```text
historical stop + truly settled question
→ QUESTION_SETTLED

historical stop + unresolved state + consumed/no useful remaining action
→ NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

Budget exhaustion and provider failures are control/execution states, not model decision kinds.

## R3 wire shape

First seam:

```text
EvidenceGapDecision
    decision_kind
    action_id | null
    explanation
```

Parser invariants:

```text
ACTION_SELECTED
→ non-null action_id

all no-tool kinds
→ null action_id

all kinds
→ non-empty trimmed explanation
```

Historical model echoes removed:

```text
target_proposition
expected_result_categories
limitations
```

The action ID rebinds to trusted target proposition/result contract; exact result classes are deterministic; untrusted limitations do not need a separate base field.

## R3 processing layers

```text
JSON Schema
→ basic field/type shape

parser
→ cross-field semantic shape

no-tool decision
→ no capability execution; semantic correctness remains model/evaluation responsibility

ACTION_SELECTED
→ fresh deterministic action admission
```

## Fresh admission responsibilities

Re-check at least:

```text
action ID still known/currently offered
action not consumed
planning budget still permits execution
current proposition/evidence preconditions still hold
mutation/policy boundary still permits action
exact locators/arguments remain trusted and bound
state/action remain fresh immediately before execution
```

Candidate first-seam admission-problem responsibilities:

```text
invalid_decision_shape
unknown_action
action_consumed
budget_exhausted
action_not_currently_actionable
action_not_allowed_by_policy
```

Do not mechanically retain historical mismatch checks that existed only because the model echoed trusted metadata.

---

# Stage R4 — Build and compare the coherent agent seam

**Status:** ACTIVE.

Use the active Build/LbD procedure and the R4 learning-depth companion while adding source/dependencies. Product runtime remains untouched; work stays under `experiments/` / `experiments/tests/` unless a later explicit product-integration decision changes that boundary.

## R4-A — ordinary-Python reference/control implementation

Build the smallest coherent reference seam:

```text
trusted context projection
→ local model request
→ EvidenceGapDecision parser
→ no-tool handling OR fresh action rebinding/admission
→ bounded execution/update seam as justified
→ deterministic trace/replay
```

Implement only what R2/R3 require. Historical experiment code is evidence, not retention authority.

The ordinary-Python seam is a **reference/control**, not a predetermined product winner.

### R4-A1 — model boundary/types/projection/parser

**Status:** COMPLETE / FOCUSED RUNTIME PASS.

Implemented:

```text
EvidenceGapPlannerContext
EvidenceGapDependencyTransition
PlanningEvidence / PlanningEvidenceFact
EvidenceGapActionDescriptor
EvidenceGapPlanningBudget
EvidenceGapDecision
explicit request projection
strict decision parser/schema
```

Learning depth for these mechanisms is owned by the R4 learning-depth companion: practical dataclass/type/Literal/`__post_init__`/comprehension/projection/schema-vs-parser understanding now; deeper internals only on trigger.

Focused validation ultimately passed 10/10 A1 tests. Two earlier failures in the projection-boundary test were diagnosed as test-observation/representation defects rather than model-authority leakage: first an over-broad serialized substring assertion, then a key-vs-value misunderstanding. The repaired focused proof separates exact hidden-key exclusion from preservation of the structured `witness_path` fact.

### R4-A2 — deterministic action rebinding/admission

**Status:** COMPLETE / FOCUSED RUNTIME PASS.

Implemented:

```text
EvidenceGapDecision.ACTION_SELECTED(action_id)
→ trusted current action lookup/rebinding
→ consumed-history check
→ budget check
→ latest proposition/evidence precondition check
→ policy/mutation check
→ exact hidden locator remains trusted
→ admitted action OR typed admission problem
```

Learned at practical ownership depth:

```text
stable-ID lookup/rebinding
typed admission result/problem
early-return guard flow
fresh-state validation
TOCTOU
proposal/recommendation != authorization
defense in depth
Python 3.12 union type-alias syntax
```

Focused validation passed 13/13 A2 tests. Combined R4-A1 + R4-A2 focused runtime result in the normal UpgradePilot WSL checkout:

```text
Ran 23 tests in 0.004s
OK
```

### R4-A3 — bounded local model request/response seam

**Status:** NEXT.

Build:

```text
explicit planner request
→ local model/provider call
→ schema-constrained response
→ strict parse to EvidenceGapDecision
→ provider/model failure remains distinct from semantic decision/admission
```

Learn when materially used:

```text
Mapping[str, Any] as untrusted input boundary
runtime narrowing
JSON serialization/deserialization
LM Studio/OpenAI-compatible request shape actually used
structured outputs
provider response parsing
timeout/retry boundary
prompt/context engineering for this exact responsibility
```

Do not turn this into a broad provider API course.

### R4-A4 — transition/update/trace seam

**Status:** AFTER A3.

Build only enough to make the ordinary-Python control coherent:

```text
no-tool OR admitted action
→ bounded execution/result seam
→ domain interpretation/update
→ budget/consumed-action state update
→ deterministic trace/replay
→ optional next turn when justified
```

Learn when materially used:

```text
state-machine/transition model
planner state vs execution state
budget decrement timing
consumed-action update timing
immutable state update/replacement
trace/event record design
replay
operational failure vs domain/evidence result
```

Async/concurrency, event sourcing, and generalized workflow persistence remain deferred until their recorded triggers are reached.

## R4-B — LangGraph implementation/comparison

**Explicitly authorized for LbD after the ordinary-Python reference is coherent enough to serve as a real baseline.**

Implement the same bounded responsibility and map real concepts:

```text
trusted workflow state
→ State / state schema

planner invocation
→ planner node

admission/revalidation
→ deterministic node / transition guard

bounded execution
→ execution/tool node

domain interpretation + update
→ evidence/state-update node

continue/no-tool routing
→ conditional edges
```

Learn against the real UpgradePilot flow where useful:

- `StateGraph`;
- nodes/edges/conditional routing;
- persistence/checkpoints when materially useful;
- interrupts/HITL concepts when materially useful;
- pre-execution freshness placement;
- graph tracing/state-transition observability.

Do not adopt or deeply study every framework feature merely because it exists. Use the learning-depth companion's trigger rules.

## R4-C — LangChain bounded learning/integration slice

Explore abstractions intersecting this responsibility only after the lower-level plain-Python/LangGraph mechanics are understood well enough to judge the abstraction:

- model interface;
- `create_agent` / agent loop;
- tool definitions/calling;
- middleware/lifecycle hooks;
- retry/fallback/early-stop/guardrail concepts when materially relevant;
- relationship to LangGraph runtime.

Do not force the custom authority model into a generic agent abstraction if that obscures it.

## R4-D — implementation comparison

Compare plain Python / LangGraph / relevant LangChain use on:

```text
responsibility clarity
state-transition clarity
deterministic authority preservation
context projection control
freshness/revalidation placement
replay/checkpoint/observability value
failure/retry ownership
testability/debuggability
overhead
learning value
future multi-action/multi-turn extensibility
provider/model integration friction
```

This stage is also where concepts repeatedly encountered earlier should deepen through real comparison/debugging rather than detached lectures.

Framework product adoption remains a later explicit architecture/build decision.

## R4 focused tests

At minimum cover:

```text
valid ACTION_SELECTED + known current action
ACTION_SELECTED + null action_id
no-tool + non-null action_id
unknown action
action consumed/stale replay
budget exhausted after request construction
precondition changed after request construction
settled no-tool
known outside-boundary no-tool
no-justified-investigation no-tool
model output cannot redefine hidden action authority
R2 context exclusions remain intact
plain-Python/LangGraph semantic equivalence on bounded cases
```

Do not build a generalized framework test platform before evidence requires it.

## R4 pass condition

The evidence-refined seam exists coherently in ordinary Python and LangGraph, the bounded LangChain learning slice is understood against the same responsibility, focused tests/traces preserve the R2/R3 authority split, and the implementation comparison has evidence rather than preference alone.

Additionally, the LbD path must show that:

```text
important implementation mechanisms were learned at the depth required when they became material
+ central mechanisms deepened through repeated use/testing/debugging
+ deferred concepts retained concrete re-entry triggers instead of being forgotten
+ implementation did not materially outrun Ali's ability to explain/challenge the relevant responsibility
+ detached prerequisite study did not unnecessarily block progress
```

---

# Stage R5 — Bounded development/replay proof

Use development/consumed cases as development evidence only.

Minimum useful proof:

1. action-selection case;
2. settled no-tool case;
3. known outside-boundary no-tool case;
4. unresolved/no-justified-action case;
5. structured planning-evidence case;
6. consumed-action repeat suppression;
7. deterministic stale/unknown rejection;
8. exact request/output/state-transition trace;
9. plain-Python vs LangGraph comparison;
10. LangChain slice findings where applicable.

R5 is also a deliberate ownership-deepening stage: testing, replay, failure diagnosis, observability, and semantic-equivalence reasoning should move from first exposure toward stronger independent understanding through actual evidence.

Do not turn development proof into reliability/generalization claims.

---

# Stage R6 — Explicit X1 disposition

Serious outcomes:

### RETAIN AS LIMITED PILOT / CONTROL SEAM

Retain bounded architecture/experiment for learning/evaluation/reusable control mechanics while general adaptive-planner advantage remains unproven.

### DEFER RICHER X1

Defer richer product planning until independently useful capabilities create genuine non-trivial selection/sequencing pressure.

These may coexist.

### REJECT

Only if even the bounded seam/control/learning asset is not worth retaining.

General adaptive-planner ADOPT is not supported by current evidence alone.

R6 must also record what plain Python, LangGraph and LangChain did/did not buy without silently converting experiment results into product architecture.

---

# Stage R7 — Conditional fresh v3 protected evaluation

Activate only if R6 determines the narrow pilot claim needs fresh planner-quality evidence.

```text
freeze exact claim + implementation
→ reserve fresh holdouts before deep analysis
→ freeze protocol/model/config/prompt/schema
→ repeated protected evaluation
→ deterministic + human semantic scoring
→ final narrow disposition
```

Do not reuse exposed S001–S012 as untouched final holdouts.

---

# Stage R8 — Select next independently useful AI/product capability

Candidates include broader upstream semantic mechanism discovery, exact-head resolver/currentness/satisfiability evidence, mediated CI/environment interpretation, richer artifact/environment evidence, targeted behavioral differential reproduction, provenance/history, and repository-purpose/reproduction-context semantics.

Each must earn its own method from real responsibility, proof need, strongest deterministic baseline, safe boundary, product value, AI value and learning value.

Do not add a capability merely to make the planner multi-action.

---

# Stage R9 — Richer planner reactivation trigger

Reactivate richer planning when evidence shows approximately:

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

Then the real loop becomes:

```text
trusted state
→ bounded model observation
→ EvidenceGapPlanner
→ action/no-tool decision
→ fresh deterministic admission
→ execution
→ interpretation/update
→ re-plan
```

---

## 10. Modification boundary

Normally allowed:

- `experiments/`;
- `experiments/tests/`;
- this plan when its bounded sequence/proof/stop or implementation-learning coordination materially changes;
- `B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md` when a materially new R4 learning responsibility or re-entry trigger appears;
- dated `working-memory/` when execution/validation reasoning has handoff value;
- `MEMORY.md` when live continuation changes.

R4 may add experiment-only LangGraph/LangChain dependencies/configuration needed for the bounded comparison, subject to active Build/LbD procedure and without silently making them product runtime dependencies.

Separate product/architecture decision remains required for `src/upgradepilot/` planner integration, accepted specifications/ADRs, product framework adoption, provider/security policy changes, and broad product-simulation scope changes.

---

## 11. Proof hierarchy

```text
design/naming
→ responsibility trace + specs + recall test

context/decision/admission contract
→ representative state + focused deterministic tests

implementation-learning ownership
→ Ali can accurately explain/challenge the material mechanism at the depth required for that slice
   + real source/test/evidence has been inspected

framework learning/implementation
→ equivalent workflow implementation + traces/tests

model capability
→ actual local model behavior

reliability/generalization
→ repeated fresh protected evaluation

product behavior/adoption
→ product source/tests/runtime + explicit architecture/build decision
```

Learning understanding is not a substitute for implementation proof, and passing implementation proof is not by itself evidence of learner ownership.

Plan text itself is never implementation proof.

---

## 12. Prohibited scope

Do not:

- fabricate a second action;
- claim general adaptive-planner value from S001;
- integrate product planner/framework runtime automatically after experiment success;
- collapse semantic discovery and planning;
- adopt LangGraph/LangChain merely because they were learned;
- reject them merely because plain Python can implement the flow;
- pass whole evidence object graphs/raw external text without demonstrated need;
- reduce planner state permanently to labels when richer structured evidence is useful;
- let the model invent locators/authority;
- treat schema validity as semantic correctness;
- treat model proposal as execution authorization;
- treat rejected/stale proposals or transient transport attempts as consumed investigations;
- let provider retries automatically consume multiple semantic planner actions;
- invent precise time/cost estimates with no trustworthy measurement;
- reuse contaminated v2 material as clean protected evidence;
- continue product simulation merely for more cases;
- create a new plan after every stage;
- turn history into free-form LLM memory;
- make compatibility/safety/maintainer claims from planner output;
- let coding materially outrun the learning/ownership needed for the next decision;
- turn every syntax detail into a prerequisite course;
- forget deferred concepts by leaving them without a re-entry trigger.

---

## 13. Overall pass condition

The project can state with inspectable evidence:

```text
what EvidenceGapPlanner owns
what context it sees and why
what each no-tool state means
what exact decision it may propose
what deterministic admission owns
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
→ EvidenceGapDecision
→ deterministic admission/revalidation
→ bounded execution
→ domain interpretation
→ trusted state + consumed-action/budget update
→ optional next turn
```

in both framework-independent form and concrete plain-Python/LangGraph implementations, at a depth that increased when real implementation/testing/comparison made deeper mechanics useful.

---

## 14. Final stop line

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