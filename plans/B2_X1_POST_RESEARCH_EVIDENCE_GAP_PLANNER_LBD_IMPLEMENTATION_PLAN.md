# B2/X1 Post-Research EvidenceGapPlanner Learning-by-Doing Implementation Plan

**Status:** AUTHORIZED PLAN ARTIFACT — position-neutral; `MEMORY.md` alone selects live activation  
**Date:** 2026-08-30  
**Revision:** R2 request/context contract complete; R3 output/admission design active  
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

The route must avoid both extremes:

```text
UNDER-ENGINEERING
→ dismiss the planner/agent work because the first seam is simple

OVER-ENGINEERING
→ manufacture capabilities/framework machinery only to make the system look agentic
```

The project should build enough real agent-engineering surface to learn from and evaluate honestly while keeping authority and claims bounded by evidence.

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

### Immediate continuity

- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R0-R1-responsibility-vocabulary.md`
- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-model-visible-context.md`
- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-planning-question.md`
- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-proposition-projection.md`
- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-action-history-and-retry-boundary.md`
- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-planning-budget-envelope.md`
- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-capability-descriptor-boundary.md`
- `../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-final-request-projection-proof.md`
- E1–E5 dated working memories
- `../working-memory/2026-08-28_B2-X1-product-simulation-capability-research-response.md`
- historical `B2_X1_PHASE3_EVALUATION_PROTOCOL.md`

Do not reopen all historical material for every step.

---

## 3. Bounded outcome

This plan is complete when UpgradePilot has:

1. precise `EvidenceGapPlanner` / `EvidenceGapDecision` responsibility vocabulary;
2. an explicit model-visible input contract;
3. an explicit planning-budget contract;
4. an explicit model-visible action/capability descriptor boundary;
5. a frozen `EvidenceGapDecision` semantic/schema contract and deterministic admission contract;
6. a coherent ordinary-Python experimental reference seam;
7. the same bounded responsibility implemented with LangGraph for real comparison/LbD;
8. a smaller LangChain agent/tool/middleware learning slice;
9. focused tests/replay evidence;
10. an evidence-backed X1 disposition;
11. a decision on whether fresh v3 protected evaluation is justified;
12. a selected next independently useful AI/product capability direction or explicit defer;
13. a clear trigger for richer multi-action/multi-turn planning;
14. material LbD closure for the concepts actually encountered.

This plan does **not** require general adaptive-planner product adoption or framework adoption.

---

## 4. Candidate responsibility

Working component:

**`EvidenceGapPlanner`**

Working responsibility:

> Given one bounded UpgradePilot planning question, trusted typed proposition state, selected bounded structured planning evidence, trusted consumed-investigation history, a bounded planning budget, and a closed set of currently admitted bounded investigation actions, identify the material evidence gap that should be addressed next and select one useful action, or explicitly decide why no action should execute now.

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

The accepted Product Decision Model remains the framework-independent semantic owner. `EvidenceGapPlanner` is a candidate implementation method for part of that responsibility.

---

## 5. Learning-by-Doing execution rule

Each substantive stage follows proportionately:

```text
ORIENT
→ establish only concepts/dataflow/owners needed now

USER REASONING
→ learner predicts/challenges/selects/explains a material point when useful

REAL BOUNDED WORK
→ design / implement / evaluate one actual slice

INSPECT EVIDENCE
→ source/tests/model output/replay/result

CORRECT MODEL
→ observation vs interpretation vs remaining uncertainty

PRESERVE MATERIAL STATE
→ working memory / MEMORY / plan only when continuation materially changes

TEACHING CLOSURE
→ what changed, why, concept learned, what remains deferred
```

Do not turn every edit or command into ceremony.

### Framework/LbD rule

```text
new tool only because fashionable
→ not justified

new tool because it gives meaningful learning exposure
AND attaches to a real UpgradePilot responsibility
AND can be compared against a real baseline
→ justified bounded experiment
```

Learning value is legitimate project value. Framework learning/comparison and framework product adoption are separate decisions.

---

# Stage R0 — Re-anchor baseline

**Status:** COMPLETE / PASS.

Do not restart E1–E5 or capability research without contradictory evidence.

---

# Stage R1 — Responsibility vocabulary

**Status:** COMPLETE.

Working names:

```text
EvidenceGapPlanner
EvidenceGapDecision
EvidenceGapDecisionKind
```

Candidate decision-kind vocabulary entering R3:

```text
ACTION_SELECTED
QUESTION_SETTLED
KNOWN_INVESTIGATION_NOT_ADMITTED
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

R3 may refine semantics if integration evidence shows a mismatch; historical vocabulary is evidence, not retention authority.

---

# Stage R2 — Model-visible context contract

**Status:** COMPLETE / PASS.

Detailed integration proof:

`../working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-final-request-projection-proof.md`

## Final candidate observation

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

output_schema / provider structured-output contract
```

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
current coarse cost_class
provider/executor retry policy
full execution/audit trace
oracle/evaluator metadata
```

## R2 decisions retained

### Planning question

One concise project-owned bounded question. It defines the uncertainty being advanced without duplicating evidence or encoding the expected result.

### Dependency transition

Use canonical:

```text
normalized_package
old_version
proposed_version
```

### Proposition projection

Use:

```text
key
state
evidence_coverage
evidence_owner
detail
```

### Structured planning evidence

```text
Level 1 = propositions
Level 2 = selected EvidenceGapPlanningEvidence
Level 3 = raw evidence

current model observation = Level 1 + selected Level 2
```

Selected Level-2 evidence may retain bounded mechanism/witness/limitation/unresolved-condition detail when it changes planning value.

### Consumed history

```text
consumed_actions: [action_id]
```

Consumed means an admitted bounded investigation produced a trusted typed result/problem for the state. Rejected/stale proposals and transient provider failures are not automatically consumed.

### Planning budget

```text
planning_budget:
    remaining_investigations: int
```

Spend when fresh-admitted bounded execution begins. Internal deterministic provider retries do not spend extra semantic investigation units.

Potential time/cost/resource dimensions remain deferred until real competing actions, real bounds and trustworthy measurements make them decision-relevant.

### Action descriptor

```text
EvidenceGapActionDescriptor
    action_id
    purpose
    target_proposition
    evidence_yield
```

The model reasons about what it can learn; deterministic code owns whether/how an action may execute.

## R2 proof cases

The final projection was inspected against:

- real S001 action state;
- real S004 settled/no-tool state;
- S001 richer CI reachability/witness evidence;
- consumed-action/no-blind-repeat state.

No fabricated multi-action cost case was created.

## No-tool state meaning

A no-tool state is a valid planner turn in which no investigation action should execute now. It is an umbrella branch, not an error.

Candidate meanings:

```text
QUESTION_SETTLED
KNOWN_INVESTIGATION_NOT_ADMITTED
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

No-tool does not imply zero budget and does not require that no capabilities exist globally.

---

# Stage R3 — Freeze EvidenceGapDecision semantics + deterministic admission

**Status:** ACTIVE NEXT STAGE.

## R3 question

What is the smallest model output that preserves useful planning/no-tool semantics while trusted metadata and execution authorization remain deterministic?

## First semantic issue — historical `stop` is overloaded

Historical E5/Phase-3 semantics allowed `stop` to mean roughly:

```text
question sufficiently settled
OR
no further justified work remains
```

But candidate `QUESTION_SETTLED` is narrower.

Integration evidence shows the historical consumed-action `d-repeat-stop` state is still unresolved:

```text
material proposition unresolved
+
A1 already meaningfully consumed
+
remaining investigation budget may exist
+
no justified current action remains
```

That is not naturally `QUESTION_SETTLED`.

Strong current candidate mapping for R3 to evaluate:

```text
S004 clean settled state
→ QUESTION_SETTLED

S006 useful outside investigation identified
→ KNOWN_INVESTIGATION_NOT_ADMITTED

conflicted state with no justified action
→ NO_JUSTIFIED_INVESTIGATION_IDENTIFIED

consumed-A1 unresolved state with no justified remaining action
→ likely NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

Do not preserve historical `stop` mechanically if the new names are more precise.

## Candidate minimal model output

Evaluate:

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

R3 must explicitly reconsider historical echoes:

```text
target_proposition
expected_result_categories
limitations
```

Remove any field whose authoritative meaning already belongs to the trusted action/context and whose model echo does not add decision value.

## Deterministic admission must own/recheck

At minimum:

```text
action ID exists in current trusted catalog
exact hidden action metadata is rebound from trusted owner
current proposition/evidence preconditions still hold
action is not forbidden by consumed-history/repeat policy
planning budget permits execution
mutation policy remains allowed
fresh state/catalog still supports the action immediately before execution
```

Schema validity is not semantic correctness or execution authorization.

## R3 proof

Use focused counterfactuals such as:

- valid action selection;
- unknown action;
- stale action;
- consumed/repeat action;
- zero budget;
- settled no-tool state;
- known-outside-capability no-tool state;
- unresolved/conflicted no-justified-action state.

## R3 pass condition

One clear `EvidenceGapDecision` schema and one deterministic admission contract exist with no semantic collision between no-tool states and no hidden transfer of authority to the model.

Stop before R4 implementation until this passes.

---

# Stage R4 — Build and compare the coherent agent seam

Product runtime remains untouched; work stays under `experiments/` / `experiments/tests/` unless a later explicit product-integration decision changes that boundary.

## R4-A — ordinary-Python reference/control implementation

Build the smallest coherent reference seam for:

- R2 context projection;
- local model request/response;
- R3 decision parsing;
- trusted action lookup/rebinding;
- deterministic admission/revalidation;
- consumed-history/budget transitions;
- deterministic trace/replay.

This is a reference/control, not a predetermined winner.

## R4-B — LangGraph implementation/comparison

**Explicitly authorized for LbD.**

Implement the same responsibility using LangGraph and map real concepts:

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

continue / no-tool routing
→ conditional edges
```

Learn against real flow where useful:

- `StateGraph`;
- nodes/edges/conditional routing;
- persistence/checkpoints;
- interrupts/HITL concepts;
- pre-execution freshness placement;
- tracing/state-transition observability.

## R4-C — LangChain learning/integration slice

Explore only abstractions that intersect this responsibility:

- model interface;
- `create_agent` / agent loop;
- tools;
- middleware/lifecycle hooks;
- retry/fallback/early-stop/guardrail patterns;
- relationship to LangGraph runtime.

Do not force the custom EvidenceGapPlanner authority model into a generic agent abstraction if the abstraction obscures it.

## R4-D — comparison

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

Framework adoption remains a later architecture/product decision.

---

# Stage R5 — Bounded development/replay proof

Minimum useful proof:

1. action-selection case;
2. settled no-tool case;
3. known-outside-capability no-tool case;
4. unresolved/no-justified-action case;
5. structured planning-evidence case;
6. consumed-action repeat suppression;
7. deterministic stale/unknown rejection;
8. exact request/output/state-transition trace;
9. plain-Python vs LangGraph comparison;
10. LangChain slice findings where applicable.

Development evidence is not reliability/generalization evidence.

---

# Stage R6 — Explicit current X1 disposition

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

Candidate directions include:

- broader upstream semantic mechanism discovery;
- exact-head resolver/currentness/satisfiability evidence;
- mediated CI/environment-consumption interpretation;
- richer target artifact/environment evidence;
- targeted behavioral differential reproduction;
- persisted-artifact provenance/history;
- repository-purpose/reproduction-context semantics.

Each must earn its own method from real responsibility, proof need, strongest deterministic baseline, safe boundary, product value, AI value and learning value.

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

## 11. Proof hierarchy

```text
design/naming
→ responsibility trace + specs + recall test

context/budget/action projection
→ representative rendered state + focused deterministic tests

admission
→ deterministic tests + counterfactual rejection

framework learning/implementation
→ equivalent workflow implementation + traces/tests

model capability
→ actual local model behavior

reliability/generalization
→ repeated fresh protected evaluation

product behavior/adoption
→ product source/tests/runtime + explicit architecture/build decision
```

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
- preserve historical `stop` semantics without resolving its current ambiguity;
- reuse contaminated v2 material as clean protected evidence;
- continue product simulation merely for more cases;
- create a new plan after every stage;
- turn history into free-form LLM memory;
- make compatibility/safety/maintainer claims from planner output.

---

## 13. Overall pass condition

The project can state with inspectable evidence:

```text
what EvidenceGapPlanner owns
what context it sees and why
what it does not see and why
what counts as consumed investigation history
what budget is planner-visible vs executor-owned
what each no-tool state means
what exact decision it may propose
what deterministic admission still owns
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
→ trusted state + consumed-action/budget update
→ optional next turn
```

in both framework-independent form and concrete plain-Python/LangGraph implementations.

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
