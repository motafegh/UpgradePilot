# B2/X1 EvidenceGapPlanner R4-A1 — Boundary Types and Explicit Projection

**Date:** 2026-08-30  
**Status:** R4-A INCREMENT COMPLETE — source/test implementation landed; focused runtime validation still pending  
**Plan:** `../plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`  
**Primary operation:** Build / Implement + Learning-by-Doing  
**Product runtime integration:** not authorized; this increment remains experiment-owned

## 1. Bounded responsibility

Implement the first ordinary-Python reference/control increment for the evidence-refined `EvidenceGapPlanner` without yet adding:

```text
LM Studio/model invocation
deterministic action admission/execution
LangGraph
LangChain
product-runtime integration
```

This increment owns only:

```text
R2 model-facing data contract
+ explicit model request projection
+ R3 EvidenceGapDecision wire/parser contract
+ focused deterministic tests for those boundaries
```

Historical B2/X1 planner modules remain unchanged as evidence rather than being rewritten in place.

## 2. Source added

Created:

`experiments/b2_x1_evidence_gap_planner.py`

Initial source commit:

`0ecbaf7d818ebf4ed5d1bf89a3ba17edf6892375`

The module now defines:

```text
EvidenceGapDependencyTransition
EvidenceGapPlanningEvidenceFact
EvidenceGapPlanningEvidence
EvidenceGapActionDescriptor
EvidenceGapPlanningBudget
EvidenceGapPlannerContext
EvidenceGapDecision
EvidenceGapDecisionKind
EVIDENCE_GAP_DECISION_JSON_SCHEMA
render_evidence_gap_planner_request(...)
evidence_gap_decision_from_mapping(...)
```

### Important implementation boundary

`render_evidence_gap_planner_request(...)` enumerates model-visible fields explicitly rather than using a wholesale dataclass/object serializer.

Reason:

```text
trusted internal type gains a field
!=
model automatically gains visibility to that field
```

The explicit projection keeps the R2 authority boundary inspectable.

## 3. First coherent `EvidenceGapPlanningEvidence` representation

R2 intentionally froze semantics before a concrete dataclass. R4-A1 now uses the smallest general representation needed by the accepted examples:

```text
EvidenceGapPlanningEvidence
    evidence_kind
    summary
    facts[]

EvidenceGapPlanningEvidenceFact
    name
    value
```

Current allowed fact values are bounded JSON-like values:

```text
trimmed text
int
bool
tuple[str, ...]
```

This is enough for current structured planning evidence such as:

```text
consumption_state
reachability_kind
witness_path
direct_exercise_established
```

without admitting arbitrary nested source/provider objects.

This is experiment representation, not a frozen product specification.

## 4. Context coherence invariants

`EvidenceGapPlannerContext` currently enforces:

- at least one proposition;
- unique proposition keys;
- unique consumed action IDs;
- unique currently offered action IDs;
- every offered action targets a proposition present in the model observation;
- an action already in `consumed_actions` must not also be offered in `allowed_actions`.

The last invariant was rechecked against the final R2 projection proof before retention. R2's consumed-repeat example explicitly uses:

```text
consumed_actions:
  - acquire_exact_target_python_declaration

allowed_actions: []
```

while deterministic admission is still expected to retain a repeat guard as defense-in-depth against stale/concurrent state.

## 5. Decision wire implementation

R3's fixed three-field result is implemented as:

```text
EvidenceGapDecision
    decision_kind
    action_id | null
    explanation
```

Parser/dataclass invariants:

```text
ACTION_SELECTED
→ action_id must be non-null trimmed text

QUESTION_SETTLED
KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
→ action_id must be null

all decisions
→ explanation must be non-empty trimmed text
```

Historical model echoes are not present:

```text
target_proposition
expected_result_categories
limitations
```

## 6. Focused tests added

Created:

`experiments/tests/test_b2_x1_evidence_gap_planner.py`

Test commit:

`c2c40e2cb77289cbf9c0c296281d78a689611a94`

The focused suite covers:

1. exact top-level request projection;
2. canonical dependency transition projection;
3. four-field `EvidenceGapActionDescriptor` projection;
4. absence of stale/authority fields such as repository/revision/path/preconditions/result classes/cost class/attempted-actions/remaining-steps;
5. structured CI witness-path evidence without raw workflow/command fields;
6. action target proposition must exist in planner propositions;
7. consumed action cannot also be offered;
8. `ACTION_SELECTED` requires an action ID;
9. no-tool decisions reject action IDs;
10. strict mapping parser accepts action/no-tool decisions;
11. strict parser rejects extra authority fields;
12. output schema remains exact three-field shape.

## 7. Validation evidence

### Source/test inspection

PASS for intended static structure.

The exact files written to `main` were fetched back and inspected after mutation.

Observed source blob:

`experiments/b2_x1_evidence_gap_planner.py` → `2bf88bc1cb267c481183ac1bd563df7f24bb73a7`

Observed test blob:

`experiments/tests/test_b2_x1_evidence_gap_planner.py` → `43d34193929bb9211e633e39b46eb5285df30cbc`

### Repository CI

No GitHub workflow run was associated with test commit `c2c40e2cb77289cbf9c0c296281d78a689611a94` when checked.

### Local runtime attempt

A temporary public-repository clone was attempted for focused `unittest` execution, but the execution environment could not resolve `github.com` and the clone failed before a repository checkout existed.

Therefore:

```text
source/test implementation landed
+ post-write source/test inspection performed
!= focused runtime test PASS
```

Runtime validation remains pending and must be obtained in a later executable environment before claiming the focused suite passes.

## 8. What this increment proves

Supported:

- the evidence-refined R2/R3 contracts can be represented coherently in ordinary Python;
- explicit request projection exists and visibly excludes the stale v2 authority fields;
- the planned three-field decision parser/schema exists;
- focused tests exist for the intended boundary.

Not yet proved:

- that the new tests execute successfully in the project environment;
- model/provider behavior;
- deterministic action admission/revalidation;
- capability execution/state update;
- full ordinary-Python agent loop;
- LangGraph/LangChain behavior;
- product integration or planner reliability.

## 9. LbD closure for this increment

### High-value code concepts introduced

**`@dataclass(frozen=True, slots=True)`**

Used for small typed value/state objects. `frozen=True` prevents ordinary field reassignment after construction; `slots=True` gives a fixed declared field layout and avoids a per-instance arbitrary attribute dictionary. Neither makes external evidence trustworthy; they make the in-process contract smaller and harder to mutate accidentally.

**`Literal[...]`**

Expresses the admitted finite decision vocabulary to type checkers/readers. Runtime validation is still performed explicitly because Python type annotations do not enforce values by themselves.

**`__post_init__`**

Runs immediately after dataclass construction and is used here for runtime invariants such as non-empty names, unique IDs, and action/context coherence.

**explicit projection**

The model request is assembled field-by-field. This is a context-engineering and authority-boundary mechanism, not just formatting.

**JSON Schema vs parser**

JSON Schema owns outer provider/wire shape; the Python parser/dataclass owns cross-field semantics such as action ID required only for `ACTION_SELECTED`. Neither grants execution authority.

## 10. Next bounded R4-A slice

Implement **fresh deterministic action rebinding/admission** against trusted hidden action state while keeping the model-facing `EvidenceGapDecision` small.

The next slice should answer concretely:

```text
EvidenceGapDecision.ACTION_SELECTED(action_id)
        ↓
trusted current action catalog lookup
        ↓
consumed-history check
        ↓
planning-budget check
        ↓
current proposition/evidence precondition check
        ↓
mutation/policy check
        ↓
exact hidden locator remains trusted
        ↓
admitted action OR typed admission problem
```

Do not add model invocation or LangGraph until this deterministic boundary is implemented and understood.
