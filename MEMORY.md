# UpgradePilot Current Memory

**Last updated:** 2026-09-12  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** D-phase post-implementation learning/ownership check for the bounded CI static↔runtime correlation bridge. A/B/C are complete and executable proof is green.
- **Mode:** Learning-by-Doing. No new implementation responsibility should begin until D/E close unless Ali explicitly redirects.
- **Selected parent plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Active working memory:** `working-memory/2026-09-12_ci-static-runtime-correlation-bridge.md`.
- **Previous working memory:** `working-memory/2026-09-11_ci-run-job-attempt-coherence-enhancement.md`.
- **Repository route:** continue directly on `main` unless Ali later requests otherwise.
- **Framework status:** ordinary-Python / LangGraph / LangChain comparison remains closed; no framework re-entry is justified.

## Maintainer-action synthesis state retained

The deterministic maintainer-action evaluator remains abstention-only:

```text
PublicPullRequestInvestigation
→ synthesize_maintainer_action(...)
→ MaintainerActionSynthesis(action="abstain")
```

No merge, targeted-check, investigate, block, or defer permission is implemented. `run targeted checks` remains paused while UpgradePilot first strengthens and evaluates its own read-only evidence path.

## Previous CI run/job attempt-coherence cycle — CLOSED

The mixed-rerun-attempt defect is repaired and proven. Exact job acquisition binds:

```text
frozen PR head SHA
+ workflow run ID
+ run attempt
→ jobs from that exact attempt
```

Proof on Ali's WSL environment:

```text
focused provider tests      9  OK
nearest CI/application     31  OK
full deterministic suite  533  OK
```

That Learning-by-Doing cycle is CLOSED A→E.

## CI static↔runtime correlation bridge — implementation/proof complete

UpgradePilot now has three deliberately separate evidence responsibilities:

```text
STATIC WORKFLOW EVIDENCE
        +
RUNTIME ACTIONS EVIDENCE
        ↓
CI CORRELATION EVIDENCE
        ↓
DEPENDENCY-CI INTERPRETATION
```

Provider objects remain factual-only. CI owns the cross-source relationship.

### Job correlation contract

Positive job correlation is admitted only for the bounded ordinary named-workflow class:

```text
exact workflow revision == run head
+ valid WorkflowDefinition
+ ordinary StepsJobDefinition jobs only
+ no strategy/matrix, reusable job, or JobProblem
+ explicit literal non-expression unique static job names
+ unique runtime job names
+ exact static/runtime job-name-set match
→ static job key ↔ runtime job ID
```

Unsupported or ambiguous shapes remain unresolved.

### Step correlation contract

Inside an already-correlated job:

```text
no StepProblem
+ explicit literal non-expression unique static step names
+ runtime steps present with unique strictly ordered numbers
+ every static step name appears exactly once at runtime
+ static step-name sequence is an ordered runtime subsequence
→ static source_index ↔ runtime step number
```

GitHub-generated setup/post/completion steps are allowed as extras. Static source index is never equated directly with runtime step number.

### Result interpretation boundary

Correlation is identity, not success. Positive runtime execution interpretation requires:

```text
runtime status == completed
runtime conclusion == success
+ static continue-on-error absent or literal false
```

The bridge still does not prove exact resolved dependency version, selected/downloaded wheel, wheel compatibility, behavioral compatibility, complete CI coverage, proposal safety, or a maintainer action.

No job-log work was needed for this bridge.

## Implemented source

Added:

`src/upgradepilot/ci/workflow_runtime_correlation.py`

Primary entry point:

```text
correlate_workflow_runtime(...)
→ WorkflowRuntimeCorrelationResult
```

It returns either a correlated static↔runtime job/step relationship or an explicit unresolved reason/detail.

Updated:

`src/upgradepilot/ci/dependency_exercise.py`

New strongest technical CI coverage state:

```text
supported_runtime_correlated
```

This requires already-supported static changed-dependency consumption whose owning user-defined run step is safely correlated to an exact-attempt runtime step with `completed/success` and no visible `continue-on-error` masking.

The previous:

```text
supported_not_correlated
```

remains the conservative fallback when successful exact-head CI + supported static consumption exist but the bounded bridge cannot safely correlate the workflow.

A correlated skipped/failed/cancelled/non-completed consuming step becomes unresolved rather than falsely strengthened. Dynamic/true `continue-on-error` likewise keeps successful execution interpretation unresolved.

Static direct exercise remains separate and now also has a distinct runtime-correlated execution axis.

Updated:

`src/upgradepilot/maintainer_action.py`

only so `supported_runtime_correlated` is recognized as a non-unresolved technical CI state. Synthesis remains abstention-only and gains no new action permission.

## Proof assets

Added:

- `tests/test_workflow_runtime_correlation.py`
- `tests/test_ci_runtime_correlated_dependency_coverage.py`

Updated:

- `tests/test_maintainer_action.py`

The proof set covers positive job/step correlation, runtime-generated extra steps and number gaps, matrix/reusable/name/order ambiguity, correlated consumption/direct exercise, skipped execution, `continue-on-error` masking, fallback to `supported_not_correlated`, and preservation of abstention-only synthesis.

## Relevant implementation commits

```text
d3742f70da6b18287fbd05ec8dbb2b936225edf6  feat: add bounded CI workflow runtime correlation
ac9d03bf4d2e718275baa4acb9eabde78ea59ad5  test: prove bounded workflow runtime correlation
0ba88f19c4b14589016119e6f1c7572d9cbd3672  feat: integrate runtime-correlated CI dependency evidence
783ffa468184d79217cf39fb437c4651215e3f9e  fix: accept runtime-correlated CI support in synthesis input
b28a403534c1057cd0c5601b6d9da93697030c7b  test: prove runtime-correlated dependency CI coverage
f476b4cd5e3ac9ae5e4ae0013e68fd9b71308c69  test: keep runtime-correlated CI outside action permission
6730d222eb60547437966f799bee0df8056f4a51  docs: preserve CI correlation B implementation checkpoint
7413c01a414e9de923c76a212fe90dd77c034d3d  docs: close CI correlation build proof
```

## Executable validation — GREEN

Ali ran the required narrow-to-broad validation in the real WSL UpgradePilot environment:

```text
focused correlation tests
→ PASS / GREEN

nearest CI / investigation / provider / parser / synthesis regression set
→ PASS / GREEN

full deterministic repository suite
→ Ran 549 tests in 0.144s
→ OK
```

Therefore B implementation and deterministic proof are complete. C preservation is also complete through the active working memory and this file.

The proof does **not** establish exact dependency/version installation, selected wheel, wheel compatibility, behavioral compatibility, complete external CI coverage, proposal safety, or any maintainer-action permission.

## Relevant remaining trust restrictions

1. requirements/constraints patch-to-frozen-head correspondence is not established;
2. static command recognition can produce false-positive direct-requirements evidence from unsupported shell text;
3. run/job attempt coherence is repaired and proven;
4. static↔runtime step identity is now correlated only for the bounded ordinary named-workflow class;
5. no exact runtime dependency-version/wheel proof exists yet.

## Immediate continuation — canonical Learning-by-Doing cycle

```text
Slice: CI static↔runtime correlation bridge

A — DONE
    correlation contract, ownership, ambiguity states, claim limits, and proof route selected

B — DONE
    source/tests implemented, diff-reviewed, and deterministically validated
    full suite: 549 tests OK

C — DONE
    final implementation/proof state preserved

D — CURRENT
    post-implementation learning / ownership check

E — NOT STARTED
    decide next bounded responsibility only after D closes
```

Do not yet parse job logs, add wheel-serviceability semantics, enable `run targeted checks`, add non-abstention maintainer actions, or redesign CLI/reporting.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-build-implement`
