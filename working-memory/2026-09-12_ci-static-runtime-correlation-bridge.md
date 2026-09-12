# CI Static↔Runtime Correlation Bridge — Working Memory

**Date:** 2026-09-12  
**Session status:** ACTIVE  
**Primary mode:** Learning-by-Doing  
**Parent selected plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Previous:** [`2026-09-11_ci-run-job-attempt-coherence-enhancement.md`](2026-09-11_ci-run-job-attempt-coherence-enhancement.md)

## Responsibility

UpgradePilot already owns two separate evidence layers:

```text
STATIC WORKFLOW EVIDENCE
→ exact PR-head workflow definition
→ jobs / strategy / ordered steps / commands / conditions

RUNTIME ACTIONS EVIDENCE
→ exact workflow run + attempt
→ runtime jobs
→ runtime step summaries / status / conclusion
```

The selected responsibility adds a bounded third layer without collapsing those authorities:

```text
STATIC EVIDENCE
        +
RUNTIME EVIDENCE
        ↓
CI CORRELATION EVIDENCE
        ↓
DEPENDENCY-CI INTERPRETATION
```

The bridge maps existing static job/step coordinates to factual runtime job/step records. It does not rediscover dependency semantics and does not turn provider observations into dependency claims by itself.

## A — design/investigation result — DONE

A established the smallest sound first correlation class from current source, GitHub documentation, and real historical UpgradePilot workflow/run evidence.

### Job correlation

Positive correlation is admitted only when:

```text
exact workflow revision == run head
+ valid WorkflowDefinition
+ all jobs are ordinary StepsJobDefinition
+ no strategy/matrix, reusable job, or JobProblem
+ every static job has an explicit literal non-expression non-empty name
+ static job names unique
+ runtime job names unique
+ static-name set == runtime-name set
→ static job key ↔ runtime job ID
```

Matrix/strategy, reusable, malformed, unnamed, dynamic, duplicate-name, and job-set mismatch shapes remain unresolved.

Historical UpgradePilot evidence directly demonstrated the matrix pressure: one static job named `Python ${{ matrix.python-version }}` produced three runtime jobs (`Python 3.12`, `Python 3.13`, `Python 3.14`).

### Step correlation

Inside an already-correlated job:

```text
no StepProblem
+ every user-defined step has explicit literal non-expression non-empty name
+ static step names unique
+ runtime steps present
+ runtime step numbers unique and strictly ordered
+ each static step name appears exactly once at runtime
+ static step-name sequence is an ordered runtime subsequence
→ static source_index ↔ runtime step number
```

Runtime-only setup/post/completion steps are allowed as extras. Static source index is never equated directly with runtime step number.

A real UpgradePilot run showed the intended shape: user-declared step names remained ordered while GitHub inserted `Set up job`, `Post ...`, and `Complete job` records plus runtime-number gaps.

### Correlation vs runtime-success interpretation

Identity and result interpretation remain separate. A correlated step may be success/failure/cancelled/skipped.

A positive successful-step interpretation requires:

```text
runtime status == completed
runtime conclusion == success
+ static continue-on-error absent or literal false
```

`continue-on-error: true` or dynamic semantics prevent treating conclusion `success` as an unmasked successful outcome.

### Claim boundary

The bridge may establish only:

```text
for this exact PR head/run attempt,
this statically identified user-defined run step
corresponds to this runtime step,
and GitHub reports this status/conclusion
```

It does **not** establish exact resolved dependency version, every shell segment succeeding, selected/downloaded wheel, wheel compatibility, behavioral compatibility, complete CI coverage, proposal safety, or any maintainer action.

No job-log acquisition is needed for this bridge. Logs remain a separate possible responsibility only if a later selected proposition needs facts absent from runtime step summaries.

## B — Build/Implement — DONE

Ali explicitly authorized formal Build entry. The Build/Implement Skill, Learning-by-Doing procedure, working-memory procedure, Naming Clarity owner, and Source-Clarity guidance were applied.

### Generic CI correlation owner

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

The module returns either:

```text
correlated
→ WorkflowRuntimeJobCorrelation
   → WorkflowRuntimeStepCorrelation

unresolved
→ reason + detail
```

It implements the A-selected whole-workflow job-name bijection and ordered named-step-subsequence contract while keeping provider facts unchanged.

Implementation commit:

```text
d3742f70da6b18287fbd05ec8dbb2b936225edf6  feat: add bounded CI workflow runtime correlation
```

### Focused correlation proof cases

Added:

`tests/test_workflow_runtime_correlation.py`

The tests protect positive multi-job/step correlation, GitHub-generated runtime extras/number gaps, matrix/reusable unresolved behavior, static/runtime job-name ambiguity, step-name ambiguity, runtime-number defects, missing/ambiguous runtime matches, and step-order mismatch.

Commit:

```text
ac9d03bf4d2e718275baa4acb9eabde78ea59ad5  test: prove bounded workflow runtime correlation
```

### Dependency-CI integration

Modified:

`src/upgradepilot/ci/dependency_exercise.py`

The coverage result now admits one stronger technical state:

```text
supported_runtime_correlated
```

This means at least one already-supported static changed-dependency consumption location belongs to a user-defined `RunStepDefinition` that:

1. is safely correlated through the workflow bridge;
2. has runtime `status == completed`;
3. has runtime `conclusion == success`;
4. has static `continue-on-error` absent or literal false.

The existing `supported_not_correlated` state remains the conservative fallback when static consumption and successful exact-head CI exist but the bounded bridge cannot safely correlate the workflow.

If the bridge succeeds but the relevant consuming step is skipped/failed/cancelled/non-completed, coverage is unresolved instead of hiding the observed non-success. If `continue-on-error` is true/dynamic, identity may correlate but success interpretation remains unresolved.

Static direct exercise remains separate and now also has a distinct runtime-correlated execution axis.

Implementation commit:

```text
0ba88f19c4b14589016119e6f1c7572d9cbd3672  feat: integrate runtime-correlated CI dependency evidence
```

### Maintainer-action compatibility

Modified `src/upgradepilot/maintainer_action.py` so both technical support states:

```text
supported_not_correlated
supported_runtime_correlated
```

are treated as non-unresolved CI evidence. This does **not** add a maintainer action; synthesis remains abstention-only.

Commit:

```text
783ffa468184d79217cf39fb437c4651215e3f9e  fix: accept runtime-correlated CI support in synthesis input
```

### Dependency-CI and synthesis proof assets

Added:

`tests/test_ci_runtime_correlated_dependency_coverage.py`

Updated:

`tests/test_maintainer_action.py`

These protect successful runtime-correlated consumption, separately correlated direct exercise, skipped/non-successful execution, `continue-on-error` masking, fallback to `supported_not_correlated`, and preservation of abstention-only synthesis.

Commits:

```text
b28a403534c1057cd0c5601b6d9da93697030c7b  test: prove runtime-correlated dependency CI coverage
f476b4cd5e3ac9ae5e4ae0013e68fd9b71308c69  test: keep runtime-correlated CI outside action permission
```

### Scope/diff review

The Build diff remained inside the selected responsibility:

```text
src/upgradepilot/ci/workflow_runtime_correlation.py     added
src/upgradepilot/ci/dependency_exercise.py              modified
src/upgradepilot/maintainer_action.py                   modified
tests/test_workflow_runtime_correlation.py              added
tests/test_ci_runtime_correlated_dependency_coverage.py added
tests/test_maintainer_action.py                         modified
```

No GitHub provider acquisition, workflow parser representation, job logs, wheel semantics, target-environment semantics, CLI/reporting, or new maintainer-action permission was added.

### Executable validation — CLOSED GREEN

The assistant execution environment could not clone GitHub because of DNS failure; that was recorded only as non-product proof debt.

Ali then ran the required narrow-to-broad validation in the real WSL UpgradePilot environment:

```text
focused correlation tests
→ PASS / GREEN

nearest CI / investigation / provider / parser / synthesis regression set
→ PASS / GREEN

full deterministic repository suite
→ Ran 549 tests in 0.144s
→ OK
```

Therefore B's executable proof boundary is now closed. The implementation is not merely statically reviewed; it is deterministically proven across the focused responsibility, nearest integrations/regressions, and full repository suite.

The proof still does **not** establish exact dependency/version installation, selected wheel, wheel compatibility, behavioral compatibility, complete external CI coverage, proposal safety, or a maintainer-action permission.

## C — state preservation — DONE

Final B implementation, proof results, scope boundaries, and stronger-claim exclusions are preserved here and in `MEMORY.md`. No additional product mutation is required for C.

## Current Learning-by-Doing state

```text
Slice: CI static↔runtime correlation bridge

A — DONE
    bounded design/contract selected

B — DONE
    implementation + tests + diff review + deterministic validation complete
    full suite: 549 tests OK

C — DONE
    final implementation/proof state preserved

D — CURRENT
    post-implementation learning / ownership check

E — NOT STARTED
```

## Scope exclusions retained

This completed Build still does not:

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
