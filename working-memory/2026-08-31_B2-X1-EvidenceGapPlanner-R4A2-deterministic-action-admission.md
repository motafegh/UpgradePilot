# B2/X1 EvidenceGapPlanner R4-A2 — deterministic action rebinding/admission

**Date:** 2026-08-31  
**Mode:** Learning-by-Doing / Build  
**Scope:** experiment-owned ordinary-Python reference/control only  
**Product runtime integration:** not authorized

## 1. Slice contract

### Build target

Implement the fresh deterministic boundary between an untrusted model decision and executable investigation authority:

```text
T1 EvidenceGapPlannerContext
→ model returns EvidenceGapDecision(ACTION_SELECTED, action_id)

T2 latest trusted state
+ exact bound-action catalog
→ deterministic rebinding/admission
→ exact admitted action OR typed admission problem
```

No model/provider call and no investigation execution belong to this increment.

### Learning target

Material concepts encountered:

```text
stable action-ID lookup/rebinding
typed admitted-result vs typed problem result
early-return guard flow
closed Literal reason vocabulary
fresh-state/precondition validation
TOCTOU / stale-plan control
proposal/recommendation != authorization
defense in depth
Python 3.12 `type Alias = A | B` union alias syntax
```

Deeper generic typing, policy frameworks, rule engines, async/concurrency, and orchestration frameworks remain deferred behind the triggers in `plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`.

## 2. Executable changes

New source:

`experiments/b2_x1_evidence_gap_admission.py`

New focused tests:

`experiments/tests/test_b2_x1_evidence_gap_admission.py`

Source/test commits:

```text
initial admission source
4ba45353b93c4bb5596a796c6e6564cca9d5796f

initial focused tests
9abc63a7b48c2a60b94b854b8edf43a8a1491d90

harden exact A1 binding invariants
59de48889decee62c8734fd1f420d2b37c7777b0

cover hardened binding invariants
b16f1cf24407cbbd5cfda69a01abc37e6958f16c
```

## 3. New reference types

### `BoundInvestigationAction`

Owns the exact trusted executable action contract that the model may select only by ID.

Current fields:

```text
action_id
purpose
target_proposition
evidence_yield
repository
revision
path
required_proposition_state
required_evidence_coverage
mutation_class
result_families
```

`purpose`, `target_proposition`, and `evidence_yield` can be projected into `EvidenceGapActionDescriptor` for model reasoning. Exact repository/revision/path, preconditions, mutation policy, and result-family contract remain hidden.

For the real A1 identity `acquire_exact_target_python_declaration`, construction now protects the exact target proposition, `pyproject.toml` path, unresolved/insufficient preconditions, read-only mutation class, and `TargetPythonDeclaration | TargetPythonDeclarationProblem` result-family contract. The same ID therefore cannot silently be repurposed after R3 removed model echoes of those fields.

### `EvidenceGapAdmissionState`

Latest trusted deterministic state immediately before execution:

```text
repository
revision
propositions
consumed_actions
remaining_investigations
actions: BoundInvestigationAction[]
```

This is intentionally not `EvidenceGapPlannerContext`.

```text
planner context
→ bounded T1 model observation

admission state
→ latest T2 deterministic execution-authority state
```

The admission state deliberately permits a bound action to remain present even if it has become consumed or stale. The admission function must prove it can reject those T1→T2 changes rather than assuming a perfectly pre-pruned catalog.

### Result types

```text
AdmittedInvestigationAction
EvidenceGapAdmissionProblem

type EvidenceGapAdmissionResult =
    AdmittedInvestigationAction | EvidenceGapAdmissionProblem
```

Expected stale/authorization outcomes are typed values, not exceptions. Calling selected-action admission with a valid no-tool decision is instead treated as orchestration/programmer misuse because R3 already routes no-tool decisions away from capability execution.

## 4. Admission order

`admit_selected_investigation_action(...)` currently checks:

```text
1. decision is ACTION_SELECTED
2. selected action ID exists in the current trusted bound-action catalog
3. action is not now consumed
4. investigation budget remains
5. exact repository/revision binding matches current trusted target identity
6. current policy permits the action (read-only first seam)
7. target proposition still exists
8. current state/coverage still satisfy the action precondition
9. return exact bound action; model explanation remains trace-only
```

The model explanation cannot redefine repository/revision/path or any hidden action authority.

## 5. Freshness model

The implementation preserves the four distinct stale-state pressures found by the prior product-simulation transfer:

```text
source identity staleness
→ action_identity_stale

action-history staleness
→ action_consumed

budget/policy/catalog staleness
→ budget_exhausted / unknown_action / action_not_allowed_by_policy

evidence-state/epistemic staleness
→ action_not_currently_actionable
```

This is the practical TOCTOU boundary:

```text
valid at planning time T1
!= permanently authorized at execution time T2
```

## 6. Focused tests written

The R4-A2 focused suite covers:

```text
bound action → planner-visible descriptor excludes hidden authority
real A1 ID cannot be repurposed with different preconditions
real A1 ID cannot be repurposed with different result-family contract
valid selected action rebinds exact repository/revision/path/result contract
model explanation cannot redefine hidden identity
unknown/invented action ID
consumed-after-planning state
budget exhausted after planning
stale revision binding
mutation blocked by current policy
proposition changed after planning
proposition disappeared after planning
no-tool decision does not enter selected-action admission
```

## 7. Validation evidence

Observed current project runtime contract:

`pyproject.toml` requires Python `>=3.12`, so the Python 3.12 `type EvidenceGapAdmissionResult = ...` syntax is within the supported project runtime.

Post-write source and tests were fetched back from `main` and statically inspected.

GitHub Actions query for the latest focused-test commit returned:

```text
total_count = 0
workflow_runs = []
```

The assistant local shell still cannot resolve `raw.githubusercontent.com` / GitHub, so a fresh repository checkout or exact local test execution could not be obtained in this session.

Therefore current proof is:

```text
implementation landed
→ YES

actual landed source/test inspection
→ YES

focused tests written
→ YES

Python-version syntax compatibility
→ YES (`requires-python >=3.12`)

focused runtime test PASS
→ NOT YET ESTABLISHED
```

Do not convert this into runtime PASS.

## 8. Learning closure

The important mental model from A2 is:

```text
LLM says: "choose A1"
→ recommendation/proposal

trusted system looks up A1
→ recovers exact executable contract

trusted system checks latest T2 state
→ authorization decision

only then
→ capability may execute
```

The `action_id` is therefore a stable rendezvous key between model reasoning and deterministic authority; it is not itself authority.

Early returns make the admission chain readable as ordered guards:

```text
if unknown → problem
if consumed → problem
if no budget → problem
if stale identity → problem
if policy blocks → problem
if precondition stale → problem
else → admitted exact action
```

The union result type makes expected denial/staleness part of normal control flow rather than treating those states as exceptional crashes.

## 9. Stop / continue decision

R4-A2 implementation responsibility is materially complete at source/test level, but its focused runtime proof remains pending.

Do not begin the model/provider seam while pretending A2 is runtime-proven. The next bounded step should first obtain the narrow A1+A2 focused test result in a runnable UpgradePilot environment. Once that proof is green (or a failure is diagnosed/repaired), continue to R4-A3 bounded local model request/response.
