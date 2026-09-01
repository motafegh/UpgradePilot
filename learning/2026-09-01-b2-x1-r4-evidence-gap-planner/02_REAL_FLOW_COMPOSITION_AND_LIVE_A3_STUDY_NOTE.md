# B2/X1 R4 — Real-Flow Composition + Live A3 Study Note

**Snapshot date:** 2026-09-01  
**Pinned source/test commit:** `2467bf1734a7261a96f15027ca292fc840f8b396`  
**Learning depth represented:** operationally understood with guidance; implementation-adjacent study material; ownership catch-up still requires later recall/transfer.  
**Purpose:** compact relearning note for the new real-product composition seam, S001 probes, and first live A3 planner call.

## 1. Big picture

The new responsibility added on 2026-09-01 is:

```text
normal UpgradePilot product result
→ thin experiment-owned composition/projection
→ EvidenceGapPlannerContext
→ A1 model-visible request
→ A3 live planner decision
→ A2 admission
→ STOP before capability execution
```

Exact new source/proof files:

```text
experiments/b2_x1_evidence_gap_composition.py
experiments/tests/test_b2_x1_evidence_gap_composition.py
experiments/b2_x1_s001_real_flow_composition_probe.py
experiments/b2_x1_s001_real_flow_a3_smoke.py
```

The central design rule:

> Composition reuses product-owned truth and reshapes it for planning. It must not become a second owner of dependency truth, proposition truth, CI reachability, or executable action authority.

## 2. Real S001 case used for learning

Public case:

```text
pydantic/pydantic#13432
soupsieve 2.6 → 2.8.4
```

Relevant product state before target-Python acquisition:

```text
upstream_python_support_drop_crossed
→ established

exact_target_python_declaration_established
→ unresolved

declared_python_range_intersects_dropped_line
→ unresolved
```

Real supported CI witness used in planner evidence:

```text
mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

Current deterministic investigation selection:

```text
acquire_exact_target_python_declaration
```

## 3. `b2_x1_evidence_gap_composition.py` responsibility

Main function:

```python
compose_pre_target_python_support_planner_context(...)
```

It receives one already-produced `PublicPullRequestInvestigation` and builds the smaller `EvidenceGapPlannerContext`.

### 3.1 Dependency transition

Input product object:

```text
DependencyVersionChange
    normalized_package = soupsieve
    old_version = 2.6
    proposed_version = 2.8.4
    richer product/source fields...
```

Projected planner object:

```text
EvidenceGapDependencyTransition
    normalized_package = soupsieve
    old_version = 2.6
    proposed_version = 2.8.4
```

Key lesson: **reuse truth without exposing the whole truth-owning object**.

The `isinstance(dependency, DependencyVersionChange)` guard does not re-establish the dependency change; it checks that this composition path received the product state it requires.

### 3.2 Python-support assessment and propositions

The adapter requires `PythonSupportDropImpactAssessment` and specifically the **pre-target** state:

```text
assessment.target_relevance is None
```

It also checks:

```text
assessment.candidate.dependency == dependency
```

This protects cross-object coherence: individually valid objects must still describe the same real dependency transition.

The propositions are flattened from the product-owned applicability paths:

```python
propositions = tuple(
    proposition
    for path in assessment.applicability.paths
    for proposition in path.propositions
)
```

Expanded mental model:

```text
for each applicability path
→ for each proposition in that path
→ collect existing PropositionAssessment objects
→ one flat tuple for the planner
```

The composition layer **collects** proposition truth; it does not recreate it.

### 3.3 Product selection → bound action → model descriptor

Product output:

```text
python_support_drop_investigation_selection
→ acquire_exact_target_python_declaration
```

The adapter calls `_bound_action_for_selection(...)`, which rebuilds the exact A2 action from trusted repository/revision and checks that selection and action still agree on:

```text
selection kind ↔ action_id
selection path ↔ action path
selection proposition key ↔ target proposition
```

Then pre-call orchestration state decides whether the action may be offered:

```python
offer_action = (
    remaining_investigations > 0
    and action.action_id not in consumed_actions
)
```

So deterministic code decides the action menu; the LLM chooses only from that menu.

If offered, the richer action becomes:

```text
EvidenceGapActionDescriptor
    action_id
    purpose
    target_proposition
    evidence_yield
```

Repository, revision, exact path, preconditions, mutation policy, and result contract stay hidden for later A2 admission.

### 3.4 CI evidence projection

Helper:

```python
_project_supported_ci_consumption_evidence(...)
```

Traversal:

```text
coverage.workflows
→ workflow.consumptions
→ keep only state == supported
→ project bounded facts
```

The real planner-useful facts can include:

```text
consumption_state
mechanism
reachability_kind
witness_path
direct_exercise_established
```

The adapter deliberately skips non-supported records with `continue`; it does not promote unresolved evidence to supported evidence.

Important proof boundary:

```text
supported static dependency consumption
!= runtime execution proof
!= runtime dependency-use proof
!= compatibility proof
```

### 3.5 Final assembly

The final `EvidenceGapPlannerContext` combines three origins:

```text
PRODUCT-OWNED STATE
→ dependency transition
→ propositions
→ selected CI evidence
→ current investigation selection

ORCHESTRATION STATE
→ planning question
→ consumed actions
→ remaining investigation budget

TRUSTED ACTION CATALOG
→ exact bound action
→ projected allowed-action descriptor
```

Compact mental model:

```text
product facts + orchestration state + trusted action catalog
→ bounded planner context
```

## 4. Python syntax/mechanisms worth learning from this file

### Must understand practically

```text
object.attribute access
isinstance(...)
if ...: raise ValueError(...)
object-to-smaller-object projection
nested generator expression / flattening
nested for loops
continue
list.append(...)
tuple(...)
conditional expression: X if condition else Y
one-element tuple: (item,)
None checks
```

Learn these through the S001 data flow above, not isolated toy examples.

### Recognition level is enough

```text
private helper naming with leading _
__all__
advanced typing internals
all fixture-construction syntax inside tests
```

## 5. What the composition tests prove

`test_b2_x1_evidence_gap_composition.py` owns four focused checks:

```text
1. Real UpgradePilot result types are reused and all supported CI consumptions are preserved.

2. Rendered planner context keeps exact source/action authority hidden.

3. Consumed actions or zero-budget actions are not offered before the model call.

4. Product selection ↔ bound-action contract drift is rejected.
```

Do not memorize the large test fixture. Understand the proposition each test protects.

Observed combined focused result at this snapshot:

```text
A1 + A2 + A3 + composition
→ 40/40 PASS
```

## 6. Real-flow composition probe

File:

```text
experiments/b2_x1_s001_real_flow_composition_probe.py
```

Purpose:

```text
real public S001
→ investigate_public_pull_request(...)
→ real product outputs
→ composition seam
→ A1 request
→ assertions
→ STOP before new A3 planner
```

Observed proof:

```text
normal_product_path_used: True
new_a3_planner_invoked: False
expected_s001_transition_preserved: True
expected_product_propositions_preserved: True
expected_ci_witness_preserved: True
hidden_source_action_authority_absent_from_request: True
```

A useful Python/runtime lesson came from the initial launch failure:

```text
python experiments/b2_x1_s001_real_flow_composition_probe.py
→ ModuleNotFoundError: No module named 'experiments'
```

Correct repository-root module invocation:

```text
python -m experiments.b2_x1_s001_real_flow_composition_probe
```

Mental model:

```text
python path/to/file.py
→ script directory becomes the key import location

python -m package.module
→ run through the repository/package import structure
```

No `sys.path` hack was needed.

## 7. Live A3 smoke

File:

```text
experiments/b2_x1_s001_real_flow_a3_smoke.py
```

Real path:

```text
S001 normal product investigation
→ composition
→ EvidenceGapPlannerContext
→ LocalEvidenceGapPlanner.decide(...)
→ EvidenceGapDecision
→ if ACTION_SELECTED: A2 admission
→ no capability execution
```

Observed live decision:

```text
decision_kind = ACTION_SELECTED
action_id = acquire_exact_target_python_declaration
basic_expectation_match = True
admission_kind = admitted_action
capability_executed = False
```

The model explanation matched the actual bounded state: upstream support drop was established, exact target declaration was unresolved, and the offered action directly targeted that gap.

LM Studio independently showed the planner request used schema:

```text
upgradepilot_evidence_gap_decision_v1
```

with `finish_reason=stop` and no truncation.

The same runtime also emitted an outdated Gemma-4 chat-template compatibility warning. It was observational/non-blocking in this snapshot because both structured requests completed correctly; reopen only if later behavior shows a material effect.

## 8. What this real-flow proof does NOT establish

Do not overclaim from one successful case:

```text
one S001 success
!= general planner quality
!= multi-case generality
!= production reliability
!= capability execution/update correctness
!= persistence/state-transition design
!= LangGraph/LangChain adoption value
```

The smoke deliberately stops before capability execution. That missing execution/update/state-transition responsibility is what A4 must address.

## 9. Fast relearning route

Use this order for a later study session:

```text
1. Draw PublicPullRequestInvestigation → composition → A1 → A3 → A2.
2. Open composition.py and trace only S001 dependency, propositions, CI witness, and action.
3. Explain product-owned state vs orchestration state.
4. Explain exact bound action vs model-visible descriptor.
5. Read the four composition tests by proposition, not by fixture syntax.
6. Read the composition probe and live A3 smoke and state what each proves and where each stops.
```

## 10. Ownership checks for later mastery

Without the note, answer:

1. Why must composition not parse the changelog/lockfile/workflow again to establish facts?
2. Why is `assessment.candidate.dependency != dependency` a different guard from `isinstance(...)`?
3. Why are unresolved CI records skipped instead of sent as supported evidence?
4. Why does zero budget remove the action before the LLM call even though A2 checks budget again later?
5. Why can the LLM select `action_id` but not choose `pyproject.toml` or repository/revision?
6. What exactly did the real composition probe prove that the four focused tests did not?
7. What exactly did the live A3 smoke add beyond the composition probe?

Transfer exercise: imagine the target declaration has already been acquired. Predict which pre-target assumptions would no longer hold and why this specific composition function should not represent that later state unchanged.

## 11. Source and evidence anchors

Source/proof files:

```text
experiments/b2_x1_evidence_gap_composition.py
experiments/tests/test_b2_x1_evidence_gap_composition.py
experiments/b2_x1_s001_real_flow_composition_probe.py
experiments/b2_x1_s001_real_flow_a3_smoke.py
```

Detailed session records:

```text
working-memory/2026-09-01_B2-X1-R4-ownership-reentry-and-next-route.md
working-memory/2026-09-01_2055_B2-X1-R4-real-flow-proof-and-live-A3.md
```

This note is a frozen learning snapshot, not the live project-state owner and not authorization to start A4 or product integration.
