# CI Static↔Runtime Correlation Bridge — Working Memory

**Date:** 2026-09-12  
**Session status:** ACTIVE  
**Primary mode:** Build/Implement + Learning-by-Doing  
**Parent selected plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Previous:** [`2026-09-11_ci-run-job-attempt-coherence-enhancement.md`](2026-09-11_ci-run-job-attempt-coherence-enhancement.md)

## Starting point

The previous cycle repaired and proved exact GitHub Actions run/job attempt coherence. UpgradePilot already owns two distinct evidence layers:

```text
STATIC WORKFLOW EVIDENCE
→ exact PR-head workflow definition
→ jobs / strategy / ordered steps / commands / conditions

RUNTIME ACTIONS EVIDENCE
→ exact workflow run + attempt
→ runtime jobs
→ runtime step summaries / status / conclusion
```

`src/upgradepilot/ci/dependency_exercise.py` deliberately did not correlate those layers. Its strongest pre-B result was `supported_not_correlated` when successful exact-head runtime CI and supported static dependency consumption coexisted.

The selected responsibility is a bounded third layer:

```text
STATIC EVIDENCE
        +
RUNTIME EVIDENCE
        ↓
CORRELATION EVIDENCE
        ↓
DEPENDENCY-CI INTERPRETATION
```

The provider objects remain factual. Cross-source correlation is a CI-domain proposition and must remain distinguishable from both source declarations and runtime observations.

## A-phase result — complete

A determined the smallest sound static↔runtime correlation contract from existing evidence only.

### Source facts

`src/upgradepilot/github/workflow_definition.py` already preserves static `jobs.<job_id>`, optional job names plus expression flags, strategy/matrix structure, ordered jobs/steps, optional step names, run commands, conditions, `continue-on-error`, and explicit `JobProblem` / `StepProblem` / reusable-workflow structures.

`src/upgradepilot/github/actions.py` already preserves exact-attempt `WorkflowRun`, `WorkflowJob`, and `WorkflowStep(number, name, status, conclusion)` records. Job acquisition is bound to `(run_id, run_attempt)` and the frozen PR head.

Static dependency consumption/exercise evidence already carries:

```text
job_key
step_source_index
segment_index
command
```

Therefore the bridge does not rediscover dependency semantics; it maps those existing static coordinates to factual runtime job/step records.

### Authoritative and real-run pressure

GitHub documentation established that static `jobs.<job_id>` is not exposed as a first-class field on runtime job records, job/step display names are separate concepts, matrices can expand one static job into multiple runtime jobs, and runtime step summaries do not expose YAML step IDs.

Historical UpgradePilot workflow/run evidence at commit `d72011c1af2f3167ad9a552795c80876e85d0731` showed:

```text
one static matrix job
→ Python 3.12
→ Python 3.13
→ Python 3.14 runtime jobs
```

and also:

```text
static user steps
→ runtime Set up job
→ same user step names in order
→ runtime Post ... steps
→ runtime Complete job
```

This ruled out generic static-job-ID/runtime-job-ID matching and static-source-index/runtime-step-number equality, while supporting an ordered named-subsequence rule for a bounded ordinary workflow class.

### Selected job correlation contract

Positive correlation is admitted only when:

```text
exact workflow revision == run head
+ valid WorkflowDefinition
+ all jobs are ordinary StepsJobDefinition
+ no strategy/matrix, reusable job, or JobProblem
+ every static job has explicit literal non-expression non-empty name
+ static job names unique
+ runtime job names unique
+ static-name set == runtime-name set
→ static job key ↔ runtime job ID
```

Matrix/strategy, reusable, malformed, unnamed, dynamic, duplicate-name, and job-set mismatch shapes remain unresolved.

### Selected step correlation contract

Inside an already-correlated job:

```text
no StepProblem
+ every user-defined step has explicit literal non-expression non-empty name
+ static step names unique
+ runtime steps present
+ runtime step numbers unique and strictly ordered
+ every static step name appears exactly once at runtime
+ static step-name sequence is an ordered runtime subsequence
→ static source_index ↔ runtime step number
```

Runtime-only setup/post/completion steps are allowed as extras.

### Correlation vs execution result

Identity and result interpretation remain separate. A correlated step may be success/failure/cancelled/skipped. A positive successful-step interpretation requires:

```text
runtime status == completed
runtime conclusion == success
```

and static `continue-on-error` must be absent or literal false before conclusion success is treated as an unmasked successful outcome.

### Exact claim boundary

The bridge may establish only:

```text
for this exact PR head/run attempt,
this statically identified user-defined run step
corresponds to this runtime step,
and GitHub reports this status/conclusion
```

It does **not** establish exact resolved dependency version, every shell segment succeeding, selected/downloaded wheel, wheel compatibility, behavioral compatibility, complete CI coverage, proposal safety, or any maintainer action.

No job-log acquisition is needed for this bridge. Logs remain a separate possible later responsibility only if a selected proposition needs facts absent from runtime step summaries.

## B-phase implementation — current checkpoint

Ali explicitly authorized formal Build entry. The full Build/Implement Skill was loaded and applied together with the already-active Learning-by-Doing and working-memory procedures. Naming and Source-Clarity owners were consulted because the new mechanism correlates evidence across modules.

### Implemented generic CI correlation owner

Added:

`src/upgradepilot/ci/workflow_runtime_correlation.py`

Primary entry point:

```text
correlate_workflow_runtime(
    exact RepositoryTextFile,
    exact WorkflowRun,
    exact-attempt WorkflowJob records,
)
→ WorkflowRuntimeCorrelationResult
```

The module keeps provider facts unchanged and returns either:

```text
correlated
→ WorkflowRuntimeJobCorrelation
   → WorkflowRuntimeStepCorrelation

unresolved
→ reason + detail
```

It implements the A-selected whole-workflow job-name bijection and ordered named-step-subsequence contract. It deliberately does not interpret runtime status/conclusion as dependency meaning.

Implementation commit:

```text
d3742f70da6b18287fbd05ec8dbb2b936225edf6  feat: add bounded CI workflow runtime correlation
```

### Added focused correlation proof cases

Added:

`tests/test_workflow_runtime_correlation.py`

The tests protect:

- multi-job literal-name correlation independent of runtime job ordering;
- user steps matched as runtime subsequences despite GitHub-generated setup/post/completion steps and number gaps;
- matrix/strategy unresolved;
- reusable workflow unresolved;
- missing/dynamic/duplicate static job names;
- duplicate runtime job names;
- static/runtime job-name-set mismatch;
- missing/dynamic/duplicate static step names;
- duplicate/non-monotonic runtime step numbers;
- missing/ambiguous runtime step-name matches;
- user-step order mismatch.

Test commit:

```text
ac9d03bf4d2e718275baa4acb9eabde78ea59ad5  test: prove bounded workflow runtime correlation
```

### Integrated correlation into dependency CI coverage

Modified:

`src/upgradepilot/ci/dependency_exercise.py`

The coverage state now admits one stronger technical state:

```text
supported_runtime_correlated
```

This means at least one already-supported static changed-dependency consumption location belongs to a `RunStepDefinition` that:

1. is safely correlated through the new workflow bridge;
2. has runtime `status == completed`;
3. has runtime `conclusion == success`;
4. has static `continue-on-error` absent or literal false.

The existing `supported_not_correlated` state remains as the conservative fallback when static consumption and successful exact-head CI exist but the bounded bridge cannot safely correlate the workflow.

If the bridge succeeds but the relevant consuming step is skipped/failed/cancelled/non-completed, coverage becomes unresolved instead of hiding the observed non-success behind `supported_not_correlated`.

If `continue-on-error` is true/dynamic, identity may still correlate but successful execution interpretation remains unresolved.

Static direct exercise remains its own axis and now has a separate runtime-correlated execution axis as well. The implementation searches all supported static consumption/direct-exercise step locations and accepts a positive runtime axis when at least one admissible matched run step is completed-successful.

The workflow result now preserves:

```text
static consumption state
static direct-exercise state
runtime-correlated consumption state
runtime-correlated direct-exercise state
WorkflowRuntimeCorrelationResult
```

The stronger state still does **not** claim exact dependency/version installation or wheel serviceability.

Implementation commit:

```text
0ba88f19c4b14589016119e6f1c7572d9cbd3672  feat: integrate runtime-correlated CI dependency evidence
```

### Maintainer-action compatibility preserved

Modified `src/upgradepilot/maintainer_action.py` so both technical support states:

```text
supported_not_correlated
supported_runtime_correlated
```

are treated as non-unresolved CI coverage input. This does **not** add a maintainer action: synthesis remains abstention-only.

Commit:

```text
783ffa468184d79217cf39fb437c4651215e3f9e  fix: accept runtime-correlated CI support in synthesis input
```

### Added dependency-CI integration proof cases

Added:

`tests/test_ci_runtime_correlated_dependency_coverage.py`

The tests protect:

- successful named consuming step → `supported_runtime_correlated`;
- runtime-correlated direct exercise remains a separate axis;
- correlated skipped consuming step does not become positive execution;
- `continue-on-error: true` prevents masked conclusion success from becoming unmasked-success evidence;
- an unbridgeable unnamed workflow retains the prior `supported_not_correlated` fallback.

Commit:

```text
b28a403534c1057cd0c5601b6d9da93697030c7b  test: prove runtime-correlated dependency CI coverage
```

### Added synthesis regression protection

Updated `tests/test_maintainer_action.py` with a case proving that `supported_runtime_correlated` CI evidence still produces only the currently admitted `abstain` action and does not manufacture a non-abstention permission.

Commit:

```text
f476b4cd5e3ac9ae5e4ae0013e68fd9b71308c69  test: keep runtime-correlated CI outside action permission
```

### Diff review

Compared the complete B implementation against the A→B handoff commit `45b24480...`.

Only the selected responsibility changed:

```text
src/upgradepilot/ci/workflow_runtime_correlation.py     added
src/upgradepilot/ci/dependency_exercise.py              modified
src/upgradepilot/maintainer_action.py                   modified
tests/test_workflow_runtime_correlation.py              added
tests/test_ci_runtime_correlated_dependency_coverage.py added
tests/test_maintainer_action.py                         modified
```

No GitHub provider acquisition, workflow parser representation, job logs, wheel semantics, target-environment semantics, CLI/reporting, or maintainer-action permission was added.

### Validation attempt and proof debt

A narrow-to-broad validation run was attempted in the available assistant execution environment by cloning current `main` and running the two new focused test modules.

The environment failed before repository acquisition:

```text
git clone https://github.com/motafegh/UpgradePilot.git
→ Could not resolve host: github.com
```

This is an assistant-container DNS/network limitation, not product evidence and not a test failure. No deterministic test result is claimed from this environment.

Therefore B source/test implementation is present and statically reviewed, but executable proof remains **deferred** to Ali's real WSL project environment. Required next proof sequence is:

```text
1. focused correlation tests
   tests.test_workflow_runtime_correlation
   tests.test_ci_runtime_correlated_dependency_coverage

2. nearest regression set
   tests.test_ci_dependency_coverage
   tests.test_investigation
   tests.test_maintainer_action
   tests.test_github_actions
   tests.test_github_workflow_definition

3. full deterministic repository suite
```

Do not mark B executable-proof complete until those commands actually pass in the real project environment.

## Learning-by-Doing state

```text
Slice: CI static↔runtime correlation bridge

A — DONE:
    selected the bounded job/step correlation contract, owner/layer, unresolved cases,
    exact claim limits, real GitHub/UpgradePilot evidence, no-log boundary, and Build proof route.

B — CURRENT:
    source and tests are implemented on main and diff-reviewed at the selected boundary;
    executable validation is still deferred because the assistant environment cannot resolve
    github.com. No green-test claim is made yet.

C — NOT STARTED:
    preserve final implementation/proof state only after executable validation is available.

D — NOT STARTED
E — NOT STARTED
```

## Scope exclusions retained

Do not in this slice:

- download/parse job logs;
- add exact wheel/version installation semantics;
- reconstruct target environments beyond existing behavior;
- enable `run targeted checks`;
- add merge/investigate/block/defer permissions;
- redesign CLI/reporting;
- force matrix/reusable-workflow support into the first bridge.

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
