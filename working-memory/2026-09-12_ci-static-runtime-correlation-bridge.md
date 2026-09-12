# CI Static↔Runtime Correlation Bridge — Working Memory

**Date:** 2026-09-12  
**Session status:** ACTIVE  
**Primary mode:** Learning-by-Doing  
**Parent selected plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Previous:** [`2026-09-11_ci-run-job-attempt-coherence-enhancement.md`](2026-09-11_ci-run-job-attempt-coherence-enhancement.md)

## Responsibility

UpgradePilot has three deliberately separate CI evidence responsibilities:

```text
STATIC WORKFLOW EVIDENCE
→ exact PR-head workflow definition
→ jobs / strategy / ordered steps / commands / conditions

RUNTIME ACTIONS EVIDENCE
→ exact workflow run + attempt
→ runtime jobs
→ runtime step summaries / status / conclusion

STATIC + RUNTIME
        ↓
CI CORRELATION EVIDENCE
        ↓
DEPENDENCY-CI INTERPRETATION
```

The bridge maps existing static job/step coordinates to factual runtime job/step records. It does not rediscover dependency semantics and does not turn provider observations into dependency claims by itself.

## A — design/investigation — DONE

A selected the smallest sound first correlation class from current source, GitHub documentation, and real historical UpgradePilot workflow/run evidence.

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

Matrix/strategy, reusable, malformed, unnamed, dynamic, duplicate-name, and job-set mismatch shapes remain unresolved at the correlation layer.

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

### Correlation vs runtime-success interpretation

Identity and result interpretation remain separate. A positive successful-step interpretation requires:

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

No job-log acquisition was needed for this bridge.

## B — Build/Implement — DONE

Implemented:

- `src/upgradepilot/ci/workflow_runtime_correlation.py`
- runtime-correlation integration in `src/upgradepilot/ci/dependency_exercise.py`
- compatibility handling in `src/upgradepilot/maintainer_action.py`
- focused correlation and dependency-CI proof tests
- maintainer-action regression protection

The correlation module returns either:

```text
correlated
→ WorkflowRuntimeJobCorrelation
   → WorkflowRuntimeStepCorrelation

unresolved
→ reason + detail
```

`dependency_exercise.py` now admits:

```text
supported_runtime_correlated
```

when an already-supported static dependency-consuming run step is safely correlated to an exact-attempt runtime step with `completed/success` and no visible `continue-on-error` masking.

The previous:

```text
supported_not_correlated
```

remains the conservative fallback when supported static consumption and successful exact-head CI exist but the bounded bridge cannot safely correlate the workflow.

If correlation succeeds but the relevant consuming step is skipped/failed/cancelled/non-completed, dependency-CI coverage becomes unresolved instead of hiding observed non-success. Static direct exercise remains a separate axis and now also has its own runtime-correlated execution axis.

### Relevant implementation commits

```text
d3742f70da6b18287fbd05ec8dbb2b936225edf6  feat: add bounded CI workflow runtime correlation
ac9d03bf4d2e718275baa4acb9eabde78ea59ad5  test: prove bounded workflow runtime correlation
0ba88f19c4b14589016119e6f1c7572d9cbd3672  feat: integrate runtime-correlated CI dependency evidence
783ffa468184d79217cf39fb437c4651215e3f9e  fix: accept runtime-correlated CI support in synthesis input
b28a403534c1057cd0c5601b6d9da93697030c7b  test: prove runtime-correlated dependency CI coverage
f476b4cd5e3ac9ae5e4ae0013e68fd9b71308c69  test: keep runtime-correlated CI outside action permission
```

### Executable validation — GREEN

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

The proof does **not** establish exact dependency/version installation, selected wheel, wheel compatibility, behavioral compatibility, complete external CI coverage, proposal safety, or a maintainer-action permission.

## C — state preservation — DONE

Final implementation, proof results, scope boundaries, and stronger-claim exclusions are preserved here and in `MEMORY.md`.

## D — post-implementation learning / ownership — DONE

The ownership check covered the implemented system as one flow rather than isolated syntax.

Ali demonstrated the following mental model:

1. the static layer tells UpgradePilot what workflow/job/step and command are declared;
2. the runtime layer tells UpgradePilot what GitHub reports for the exact run/attempt/job/step;
3. the bridge does not create a new runtime fact — it establishes which static declaration the runtime observation belongs to;
4. the first bridge uses display `name` as the matching anchor only under surrounding safety conditions such as exact workflow/run identity, literal names, uniqueness, whole-set consistency, ordering, and exclusion of unsupported ambiguous shapes;
5. those safety conditions are also current capability limitations: unsupported shapes are not guessed into positive correlation;
6. `supported_runtime_correlated` is stronger than `supported_not_correlated` because the exact supported static consuming step is tied to a completed-successful runtime step, while exact installed version/wheel and compatibility remain unproven;
7. stronger technical CI evidence does not create a maintainer-action permission.

### Final D state-label correction

One important nuance was clarified before closure:

```text
matrix/unsupported shape
→ correlation layer: unresolved
```

but when the workflow still has successful exact-head CI plus supported static dependency consumption:

```text
correlation unresolved
+ static consumption supported
+ successful CI
→ dependency-CI coverage: supported_not_correlated
```

This distinction preserves evidence already earned rather than collapsing the whole CI result to unresolved merely because the stronger bridge cannot be established.

Ali's core ownership conclusion is correct: UpgradePilot must not guess or invent a static↔runtime relationship when the correlation safety contract does not hold.

## E — CURRENT — gap repair / next-slice orientation

E must now evaluate the remaining limitations and evidence gaps against the actual product decision responsibility rather than automatically expanding GitHub Actions support.

Questions for E include:

- Which current correlation limitations, if any, materially block the next useful product claim?
- Are matrix jobs, reusable workflows, dynamic/missing names, or another unsupported workflow shape actually required by current real cases?
- Does the stronger `supported_runtime_correlated` evidence materially reduce the previously identified target/wheel/serviceability uncertainty?
- Is the next missing fact about correlation breadth, exact runtime dependency/version/artifact evidence, static command-recognition trust, or another earlier evidence boundary?
- Are job logs or another runtime source justified only after a precise missing proposition is selected?
- How does this stronger evidence affect the earlier question of whether UpgradePilot should investigate itself before asking a maintainer to run targeted checks?

E is analysis/orientation only until it selects a distinct next responsibility.

## Current Learning-by-Doing state

```text
Slice: CI static↔runtime correlation bridge

A — DONE
B — DONE
    full suite: 549 tests OK
C — DONE
D — DONE
E — CURRENT
```

## Scope exclusions retained until E selects otherwise

Do not yet:

- download/parse job logs;
- add exact wheel/version installation semantics;
- reconstruct target environments beyond existing behavior;
- enable `run targeted checks`;
- add merge/investigate/block/defer permissions;
- redesign CLI/reporting;
- expand matrix/reusable/dynamic-name support merely for completeness.

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
