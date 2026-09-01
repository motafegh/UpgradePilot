# B2/X1 R4 A1→A3→A2 — Ownership Study Note

**Snapshot date:** 2026-09-01  
**Pinned source/test commit:** `2467bf1734a7261a96f15027ca292fc840f8b396`  
**Learning depth represented:** implementation-adjacent with guided ownership practice; not independent mastery.  
**Purpose:** compact relearning note for the ordinary-Python EvidenceGapPlanner seam before A4.

## 1. Big picture

The three files have deliberately different responsibilities:

```text
trusted UpgradePilot state
→ A1: bounded planner observation + decision contract
→ A3: local model/provider request-response boundary
→ A2: fresh deterministic action rebinding/admission
```

Exact files:

```text
experiments/b2_x1_evidence_gap_planner.py    # A1
experiments/b2_x1_evidence_gap_model.py      # A3
experiments/b2_x1_evidence_gap_admission.py  # A2
```

Core rule to retain:

> A valid model answer is still untrusted planning output, not execution authority.

## 2. A1 — what the model may see and return

`EvidenceGapPlannerContext` is the bounded model observation:

```text
planning_question
dependency_transition
propositions
planning_evidence
consumed_actions
planning_budget
allowed_actions
```

The model does **not** receive by default:

```text
repository / pull number / exact revision
exact action path
exact action preconditions
mutation policy
result-family contract
raw workflow YAML / lockfiles / logs / source files
```

`render_evidence_gap_planner_request(...)` explicitly enumerates visible fields instead of serializing whole trusted objects. Therefore adding a new internal field does not automatically expose it to the LLM.

The returned model wire shape is only:

```text
EvidenceGapDecision
    decision_kind
    action_id | None
    explanation
```

Important decision semantics:

```text
ACTION_SELECTED
→ action_id required

QUESTION_SETTLED
KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY
NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
→ action_id must be None
```

`EVIDENCE_GAP_DECISION_JSON_SCHEMA` constrains provider output shape, while `evidence_gap_decision_from_mapping(...)` and `EvidenceGapDecision.__post_init__` enforce Python-side/cross-field semantics.

### A1 mental model

```text
trusted rich state
→ explicit projection
→ small model-visible context
→ strict three-field untrusted decision
```

## 3. A3 — one bounded LM Studio call

`LocalEvidenceGapPlanner.decide(context)` performs one local structured-output inference:

```text
EvidenceGapPlannerContext
→ A1 render_evidence_gap_planner_request(...)
→ LM Studio /v1/chat/completions
→ provider envelope validation
→ JSON message decoding
→ A1 decision parser
→ EvidenceGapDecision OR EvidenceGapModelInvocationProblem
```

Current deployment choices in this snapshot:

```text
model = gemma-4-e4b-it-ud
base URL = http://127.0.0.1:12345
timeout = 180 seconds
max completion tokens = 512
temperature = 0
seed = 0
no automatic retry
strict JSON-Schema structured output
```

`build_lm_studio_session()` sets:

```python
session.trust_env = False
```

so localhost inference does not silently inherit ambient proxy configuration.

A3 separates failure families instead of collapsing everything into "model failed":

```text
provider_request_failed
provider_http_error
provider_response_malformed
completion_truncated
structured_output_invalid
```

### A3 mental model

```text
transport validity
!= structured-output validity
!= semantic model quality
!= execution authorization
```

## 4. A2 — proposal becomes current trusted admission or rejection

The model sees a small `EvidenceGapActionDescriptor`, but A2 owns the richer `BoundInvestigationAction`.

For the first real action, the hidden trusted binding includes:

```text
action_id = acquire_exact_target_python_declaration
repository
revision
path = pyproject.toml
target proposition = exact_target_python_declaration_established
required state = unresolved
required evidence coverage = insufficient
mutation class = read_only
result families = TargetPythonDeclaration | TargetPythonDeclarationProblem
```

`project_action_descriptor(action)` reveals only:

```text
action_id
purpose
target_proposition
evidence_yield
```

After the model selects only `action_id`, `admit_selected_investigation_action(...)` checks the **latest** trusted state:

```text
1. action ID still exists
2. action not already consumed
3. budget still remains
4. repository/revision identity still matches
5. current policy still permits it
6. target proposition still exists
7. proposition state/coverage still satisfy the action preconditions
```

This is the practical TOCTOU lesson:

```text
valid at planning time T1
!= automatically authorized at execution time T2
```

The model explanation is retained for traceability but cannot change repository, revision, path, policy, preconditions, or result contract.

## 5. End-to-end S001 mental model

Use this real case when relearning the seam:

```text
soupsieve 2.6 → 2.8.4
upstream Python 3.8 support drop already established
exact target Python declaration unresolved
intersection with dropped Python line unresolved
one offered action:
    acquire_exact_target_python_declaration
```

The intended control flow is:

```text
product/domain state
→ A1 bounded context
→ A3 model decides whether/what to investigate
→ untrusted ACTION_SELECTED + action_id
→ A2 rebinds exact hidden authority
→ admitted action OR typed problem
```

## 6. Python / AI-engineering mechanisms worth knowing

### Must understand practically

```text
@dataclass(frozen=True, slots=True)
__post_init__ invariants
Literal[...] constrained vocabularies
X | None and tuple[X, ...]
Mapping[str, Any] at an untrusted boundary
json.dumps vs json.loads
JSON Schema vs Python parser validation
isinstance(...) runtime narrowing
try/except → typed problems
early-return guard flow
stable action-ID lookup/rebinding
next((...), None)
TOCTOU
proposal != authorization
structured output
context projection / context engineering
trust boundary / deterministic admission
```

### Recognition level is enough for now

```text
deep requests internals
advanced generic typing
multi-provider abstraction
async/concurrency
sophisticated retry frameworks
prompt-optimization frameworks
```

Reopen those only when a real responsibility needs them.

## 7. What the focused tests protect

```text
test_b2_x1_evidence_gap_planner.py
→ exact model-visible projection
→ hidden authority excluded
→ decision shape/parser invariants

 test_b2_x1_evidence_gap_model.py
→ request construction
→ strict structured output
→ provider failure classification
→ no accidental proxy inheritance

 test_b2_x1_evidence_gap_admission.py
→ exact hidden action rebinding
→ stale/consumed/budget/policy/proposition rejection
→ model explanation cannot redefine authority
```

At this snapshot the wider A1/A2/A3/composition focused family later reached **40/40 PASS**. Passing tests prove the tested contracts, not general planner quality or production readiness.

## 8. Fast relearning route

Study in this order:

```text
1. Draw A1 → A3 → A2 from memory.
2. Open EvidenceGapPlannerContext and name visible vs hidden state.
3. Trace one ACTION_SELECTED response through LocalEvidenceGapPlanner.decide(...).
4. Trace the same action ID through admit_selected_investigation_action(...).
5. Read one focused test from each file and say exactly what it protects.
```

## 9. Ownership checks for a future study session

Without looking at this note, explain:

1. Why does A1 not receive/establish proposition truth itself?
2. Why is strict JSON Schema not enough to authorize execution?
3. Why does A2 re-check budget/consumed/revision/proposition state after the model returns?
4. What exact information can the LLM choose, and what exact information remains deterministic?
5. If the model explanation says "read secrets.txt", why can that not redirect the admitted action?

Transfer exercise: change one trusted fact hypothetically (for example revision becomes stale) and predict which layer should reject the action and why.

## 10. Source and evidence anchors

Source:

```text
experiments/b2_x1_evidence_gap_planner.py
experiments/b2_x1_evidence_gap_model.py
experiments/b2_x1_evidence_gap_admission.py
```

Focused tests:

```text
experiments/tests/test_b2_x1_evidence_gap_planner.py
experiments/tests/test_b2_x1_evidence_gap_model.py
experiments/tests/test_b2_x1_evidence_gap_admission.py
```

Detailed historical learning/execution records:

```text
working-memory/2026-08-31_B2-X1-EvidenceGapPlanner-R4A1-boundary-types-and-projection.md
working-memory/2026-08-31_B2-X1-EvidenceGapPlanner-R4A2-deterministic-action-admission.md
working-memory/2026-08-31_B2-X1-EvidenceGapPlanner-R4A3-local-model-request-response.md
working-memory/2026-08-31_B2-X1-R4A3-mocked-proof-and-ownership-reentry.md
working-memory/2026-09-01_B2-X1-R4-ownership-reentry-and-next-route.md
```

This note is a frozen learning snapshot, not the live project-state owner.
