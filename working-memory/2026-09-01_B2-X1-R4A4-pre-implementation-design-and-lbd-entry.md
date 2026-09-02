# B2/X1 R4-A4 — Transition/Update/Trace Design Closure and First Build Slice

**Date:** 2026-09-01 / updated 2026-09-02  
**Mode:** Learning-by-Doing + Build/Implement  
**Scope:** experiment-owned ordinary-Python R4-A4 transition/update/trace responsibility  
**Product runtime integration:** not authorized

## 1. Controlling route

Primary plan:

`plans/B2_X1_POST_RESEARCH_EVIDENCE_GAP_PLANNER_LBD_IMPLEMENTATION_PLAN.md`

Learning-depth companion:

`plans/B2_X1_R4_LBD_LEARNING_DEPTH_AND_REENTRY_MAP.md`

Active procedure after design closure:

```text
UP-SKILL:upgradepilot-build-implement
+ UP-SKILL:upgradepilot-learning-by-doing
```

No new A4 plan is created. The selected implementation plan still owns sequence/proof/stop scope.

## 2. Entry point and responsibility

A1/A3/A2 plus real S001 composition/live A3 were already established before A4:

```text
A1 = OBSERVE
→ bounded model-visible trusted context

A3 = DECIDE
→ EvidenceGapDecision

A2 = AUTHORIZE
→ fresh exact action rebinding/admission

A4 = ACT + INTERPRET + TRANSITION + TRACE
→ what happens after an admitted action or no-action decision?
```

Real S001 stopped at:

```text
ACTION_SELECTED
→ acquire_exact_target_python_declaration
→ A2 admitted_action
→ capability_executed = False
```

A4 begins exactly there and must not reopen A1/A2/A3 ownership.

## 3. Reuse boundary

A4 does not reimplement target acquisition or Python-support semantics.

Existing owners remain:

```text
GitHubRepositoryClient.get_exact_commit_text_file(...)
→ interpret_target_python_declaration(...)
→ TargetPythonDeclaration | TargetPythonDeclarationProblem
→ evaluate_target_python_relevance(...)
→ evaluate_python_support_drop_impact(...)
```

The LLM does not choose repository, revision, path, parser, result family, domain interpretation, or state truth.

## 4. D1 — evolving investigation state

**Resolved.** Keep stable case context separate from evolving state.

First A4 state responsibility:

```text
EvidenceGapInvestigationState
├── current Python-support domain assessment
├── consumed action IDs
├── remaining investigation budget
└── bounded planner-loop continuation status
```

Do not duplicate full `PublicPullRequestInvestigation`, raw source, CI evidence, exact source authority, model explanation, or historical trace into every state.

Use immutable replacement:

```text
STATE 0 remains inspectable
→ one A4 transition
→ STATE 1 is a new immutable value
```

## 5. D2 — semantic result/domain ownership

**Resolved.** A completed action must preserve meaningful typed evidence rather than only an action label.

For the first real action:

```text
TargetPythonDeclaration | TargetPythonDeclarationProblem
→ target relevance
→ updated PythonSupportDropImpactAssessment
```

The assessment already retains the relevant nested evidence/relevance chain. Do not add redundant parallel state fields for the same domain facts.

`InvestigationState` answers what is trusted now; `TransitionTrace` answers what happened in this transition.

## 6. D3 — consumed action vs operational failure

**Resolved.**

Valid semantic result:

```text
TargetPythonDeclaration(...)
OR
TargetPythonDeclarationProblem(...)

→ action is semantically consumed
→ budget was spent because execution began
→ domain assessment updates from the valid result
```

A typed problem result can leave the proposition unresolved and still consume the exact immutable investigation.

Operational failure before a valid semantic result:

```text
timeout / transport error / rate limit / other GitHub acquisition failure
OR
untrusted successful provider response

→ budget is spent because execution began
→ action is NOT added to semantic consumed_actions
→ domain assessment remains unchanged
→ operational failure is recorded in trace
```

`not_found_or_inaccessible` is already converted by the repository owner into `UnavailableRepositoryFile`, which the target interpreter converts into a valid `TargetPythonDeclarationProblem(state="file_unavailable")`; therefore it belongs to the semantic-result branch, not the operational-failure branch.

## 7. Terminology refinement

Current R4 terminology uses **no-action decision**, not `no-tool`, for the umbrella branch where the planner chooses no investigation action for the turn.

```text
EvidenceGapDecision
├── ACTION_SELECTED
└── no-action decision
    ├── QUESTION_SETTLED
    ├── KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY
    └── NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
```

This is descriptive vocabulary, not a fifth `EvidenceGapDecisionKind`. Historical E5/product-simulation records may retain old terminology.

## 8. D4 — no-action transition

**Resolved.** A valid no-action decision performs no capability execution and creates no fake action result.

Shared behavior:

```text
no capability execution
→ budget unchanged
→ consumed_actions unchanged
→ domain assessment unchanged
→ immutable next state changes continuation status
→ trace retains exact decision + model explanation
```

Continuation semantics:

```text
ACTIVE
→ another planner turn may still be eligible

QUESTION_SETTLED
→ SETTLED
→ terminal for this bounded planner loop/question

KNOWN_INVESTIGATION_OUTSIDE_CURRENT_BOUNDARY
→ OUTSIDE_CURRENT_BOUNDARY
→ terminal for this bounded planner loop
→ broader investigation may still have known useful work

NO_JUSTIFIED_INVESTIGATION_IDENTIFIED
→ NO_JUSTIFIED_INVESTIGATION
→ terminal for this bounded planner loop
→ underlying evidence question may remain unresolved
```

Do not collapse these to a generic `STOPPED` flag.

A4 deterministically routes a structurally valid model decision; it does not become a second semantic planner that re-decides whether the model's disposition was wise. Semantic quality remains evaluation responsibility.

The model explanation belongs in the trace, not the evolving state.

## 9. D5 — execution seam and source placement

**Resolved.** Keep the new A4 seam under `experiments/` throughout the R4 reference/control + framework comparison period.

First action path:

```text
AdmittedInvestigationAction
+ current EvidenceGapInvestigationState
+ repository client

→ get_exact_commit_text_file(action.repository, action.revision, action.path)
→ interpret_target_python_declaration(...)
→ evaluate_target_python_relevance(current assessment candidate upstream claim, target result)
→ evaluate_python_support_drop_impact(current assessment candidate, relevance)
→ next trusted assessment
```

A2 has already rebound trusted `repository + revision + path`, so A4 does not reconstruct a `PullRequestIdentity` solely to fetch the file.

Do not add a generic executor registry for the current one-action seam.

Post-experiment direction:

```text
finish plain-Python/LangGraph/LangChain experiment + comparison
→ separate evidence-backed product-integration pass
→ move/refactor only responsibilities that earned adoption into src/upgradepilot/
```

This is not permission to copy experiment files wholesale.

## 10. D6 — minimum trace/replay contract

**Resolved.** Keep the actual small immutable before/after states in each in-memory trace; do not introduce persistence IDs/checkpoint storage yet.

Minimum trace:

```text
EvidenceGapTransitionTrace
├── before_state
├── EvidenceGapDecision
├── admitted action | none
├── valid semantic execution result
│   OR expected operational failure
│   OR no execution outcome for no-action decisions
└── after_state
```

The decision object already carries:

```text
decision_kind
action_id | None
explanation
```

so those fields are not duplicated separately.

Replay semantics:

```text
recorded before_state
+ recorded decision
+ recorded semantic result / operational-failure branch
+ same deterministic A4 reduction logic
→ reconstructed after_state
```

Replay does **not** call LM Studio or GitHub again. That would be re-execution, not deterministic transition replay.

Proof target:

```text
replay(trace) == trace.after_state
```

This is sufficient for focused deterministic tests and later plain-Python vs LangGraph semantic-equivalence comparison without introducing event sourcing or a database.

## 11. First A4 Build slice implemented

New source:

`experiments/b2_x1_evidence_gap_transition.py`

Source commit:

`a5f3d822d0493d3f5c3636897d30835fd4163335`

Implemented:

```text
EvidenceGapInvestigationState
EvidenceGapOperationalFailure
EvidenceGapTransitionTrace
run_evidence_gap_transition(...)
replay_evidence_gap_transition(...)
```

The implementation supports exactly the designed first responsibility:

```text
no-action lifecycle transition
OR
already-admitted acquire_exact_target_python_declaration
→ existing product acquisition/interpreter/domain owners
→ immutable state update
→ trace
```

Expected GitHub operational failures preserved in trace are:

```text
GitHubAcquisitionError
GitHubResponseError
```

Unexpected programming/domain invariant failures are not silently converted into operational evidence.

New focused test family:

`experiments/tests/test_b2_x1_evidence_gap_transition.py`

Test commit:

`e9aec190099cd994d586b2ff9bbf2827e1417b0b`

The tests are designed to discriminate:

```text
valid declaration result
→ domain update + consumed action + spent budget + replay

typed target problem result
→ valid semantic result + consumed action + spent budget + replay

timeout / untrusted GitHub response
→ spent budget + no semantic consumption + unchanged domain state + trace/replay behavior

all three no-action decisions
→ no execution/budget/consumption/domain change + distinct continuation status + replay

ACTION_SELECTED without prior A2 admission
→ rejected

terminal bounded-loop state
→ cannot enter another A4 transition
```

## 12. Validation status and proof limit

Changed source/tests were re-read after commit against the Build Source-Clarity and Naming-Clarity requirements. The module states its ownership boundary, primary entry point, cross-file flow, deferred generalization trigger, and replay meaning.

No GitHub commit status/check has been produced for the latest test commit.

Therefore current validation is:

```text
SOURCE/TEST INSPECTION
→ COMPLETE

FOCUSED RUNTIME TEST EXECUTION
→ PENDING

REAL S001 A4 EXECUTION
→ PENDING
```

Do **not** claim the new A4 tests pass until they are executed in the normal UpgradePilot runtime.

## 13. Next continuation

The pre-implementation D1–D6 design block is closed. Planning/Design no longer blocks the first A4 implementation.

Next bounded sequence:

```text
1. run the new focused A4 transition test family in the normal UpgradePilot runtime
2. repair only evidence-backed failures if any
3. integrate the new transition seam into the existing real S001 experiment path
4. run one real S001 admitted-action transition
5. inspect exact trace/state result and replay equivalence
6. update working memory / live MEMORY with actual runtime evidence
7. stop before automatic multi-turn looping unless the next responsibility is explicitly justified
```

Still prohibited:

```text
NO product runtime integration
NO generic executor registry
NO generalized agent loop
NO database/event-sourcing infrastructure
NO framework adoption before the ordinary-Python reference is coherent
NO broad product-simulation expansion merely for case count
```

This working memory owns the detailed A4 design/build handoff. `MEMORY.md` remains the sole live-position owner.
