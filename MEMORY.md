# UpgradePilot Current Memory

**Last updated:** 2026-08-30  
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

New tools/frameworks are not prohibited merely because plain Python can implement the same behavior. Bounded learning/comparison is justified when attached to a real UpgradePilot responsibility and real baseline. Product adoption remains a separate evidence-backed decision.

---

## Live position

- **Route:** B2/X1 — Product Agentic Investigation / Orchestration Evaluation checkpoint.
- **Mode:** Learning-by-Doing / Building.
- **Selected plan:** `plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`.
- **Progress:** R0 PASS; R1 COMPLETE; **R2 COMPLETE / PASS**.
- **Live next stage:** **R3 — freeze `EvidenceGapDecision` semantics + deterministic admission contract**.
- **Product runtime integration:** not authorized; planner/framework work remains experiment-owned.
- **Technical blocker:** none.
- **Product-simulation:** prior capability/value research complete; do not launch broad new simulation merely for case count.

Current R2 owners:

- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-model-visible-context.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-planning-question.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-proposition-projection.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-action-history-and-retry-boundary.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-planning-budget-envelope.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-capability-descriptor-boundary.md`
- `working-memory/2026-08-30_B2-X1-EvidenceGapPlanner-R2-final-request-projection-proof.md`

Historical E1–E5/v2/capability-research detail remains in dated records and should not be duplicated here.

---

## Current responsibility vocabulary

### `EvidenceGapPlanner`

> Given one bounded UpgradePilot planning question, trusted proposition state, selected structured planning evidence, trusted consumed-investigation history, a bounded planning budget, and a closed set of currently admitted bounded actions, decide which material evidence gap should be addressed next by selecting one useful action, or explicitly decide why no action should execute now.

### `EvidenceGapDecision`

Untrusted model proposal; never execution authority.

### `EvidenceGapDecisionKind` — candidate semantics entering R3

```text
ACTION_SELECTED
QUESTION_SETTLED
KNOWN_INVESTIGATION_NOT_ADMITTED
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

These names are not yet final wire semantics. R3 must reconcile historical `stop` overloading before freezing them.

---

## R2 final evidence-refined model observation — PASS

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
raw source/provider objects
oracle/evaluator metadata
```

R2 final synthesis used real S001 action state, real S004 no-tool/settled state, S001 Level-2 CI reachability/witness evidence, and a consumed-action repeat state. The integrated observation passed without whole-object/raw-evidence dumping or label starvation.

### No-tool state meaning

A **no-tool state** is a valid planner turn where no investigation action should execute now. It is not planner failure.

Candidate semantic branches:

```text
QUESTION_SETTLED
→ bounded question is sufficiently settled

KNOWN_INVESTIGATION_NOT_ADMITTED
→ useful next investigation is known but outside the admitted action/support boundary

NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
→ state remains non-final but no justified admitted or known outside investigation is identified
```

No-tool does not imply zero budget and does not require that the global capability system has no tools.

### Dependency transition

Model-visible:

```text
normalized_package
old_version
proposed_version
```

Canonical identity, not presentation spelling.

### Proposition projection

Model-visible:

```text
key
state
evidence_coverage
evidence_owner
detail
```

### `EvidenceGapPlanningEvidence`

```text
Level 1 = proposition state
Level 2 = selected EvidenceGapPlanningEvidence
Level 3 = raw evidence

current model context = Level 1 + selected Level 2
Level 3 excluded by default
```

### Consumed-action history

```text
consumed_actions: [action_id]
```

Consumed means an admitted bounded investigation produced a trusted typed result/problem for the bounded state. Rejected/stale proposals and transient provider failures are not automatically consumed.

### Planning budget

```text
planning_budget:
    remaining_investigations: int
```

Spend when fresh-admitted bounded execution actually begins. Provider-internal retries do not automatically spend extra semantic investigation units.

### `EvidenceGapActionDescriptor`

```text
action_id
purpose
target_proposition
evidence_yield
```

Hidden from model:

```text
repository/revision/path
exact preconditions
mutation_class
exact result classes
current cost_class
provider/executor metadata
```

---

## R3 active responsibility

R3 must freeze the smallest `EvidenceGapDecision` + deterministic admission contract.

### First semantic issue to resolve

Historical `stop` semantics included both:

```text
question sufficiently settled
OR
no further justified work remains
```

But candidate `QUESTION_SETTLED` is narrower.

Historical `d-repeat-stop` has:

```text
proposition still unresolved
+
A1 already meaningfully consumed
+
remaining investigation budget may still exist
+
no justified current repeat/action
```

That state is not truly settled. Strong current expectation entering R3:

```text
S004 clean settled state
→ QUESTION_SETTLED

S006 known outside investigation
→ KNOWN_INVESTIGATION_NOT_ADMITTED

conflicted state with no justified action
→ NO_JUSTIFIED_INVESTIGATION_IDENTIFIED

consumed-A1 unresolved state with no justified remaining action
→ likely NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

R3 must decide this explicitly rather than preserving historical names mechanically.

### Candidate minimal output to evaluate

```text
decision_kind
action_id | null
explanation
```

R3 must reconsider historical model echoes:

```text
target_proposition
expected_result_categories
limitations
```

Do not retain them merely because v2 returned them if trusted context/action owners already provide those meanings.

### Deterministic admission must continue to own

- current action ID membership;
- exact action binding / locator recovery;
- fresh proposition/evidence preconditions;
- consumed-action/repeat guard;
- planning budget;
- mutation policy;
- exact result-family contract;
- fresh-state / TOCTOU revalidation immediately before execution.

JSON/schema validity is not semantic correctness or execution authorization.

---

## R4 framework/LbD route — already planned

```text
R4-A
ordinary-Python reference/control implementation

R4-B
same bounded responsibility implemented with LangGraph

R4-C
smaller LangChain model/tool/agent/middleware learning slice

R4-D
compare real implementations against UpgradePilot responsibilities
```

Framework learning/comparison is authorized. Product framework/dependency adoption remains a later explicit architecture/build decision.

---

## Claim limits / stop lines

Current evidence does **not** prove:

- production reliability;
- general adaptive-planner superiority;
- correct selection across several real actions;
- product/framework adoption value;
- compatibility/safety/merge authority;
- that raw evidence should never enter any future agent;
- that cost/time belong in current model state.

Do not:

- fabricate a second action;
- freeze v3 before a narrow claim and fresh holdouts exist;
- reuse historical v2 protected material as uncontaminated final evidence;
- begin `src/upgradepilot` planner integration merely because the experiment works;
- adopt LangGraph/LangChain merely because they are learned;
- reject them merely because plain Python can implement the flow;
- expose exact action authority/preconditions/result classes merely for model completeness;
- turn consumed history into free-form LLM memory;
- continue product simulation merely for more cases.

---

## Immediate route

```text
R3 decision semantics + minimal structured output + deterministic admission
→ R4 plain Python + LangGraph + LangChain learning/comparison
→ R5 bounded replay/development proof
→ R6 explicit X1 disposition
```

Richer multi-action/multi-turn planner work reopens only when multiple independently justified actions naturally coexist and real state/history/budget/resource-dependent choice becomes materially non-trivial for a small deterministic policy.
