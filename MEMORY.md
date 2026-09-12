# UpgradePilot Current Memory

**Last updated:** 2026-09-12  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** E-phase gap repair / next-slice orientation for the bounded CI static↔runtime correlation bridge. A/B/C/D are complete; implementation proof is green and the ownership check is closed.
- **Mode:** Learning-by-Doing analysis/orientation. Do not begin a new implementation responsibility until E selects and bounds it, unless Ali explicitly redirects.
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

No merge, targeted-check, investigate, block, or defer permission is implemented. `run targeted checks` remains paused while UpgradePilot first determines whether its own read-only evidence path can resolve the relevant uncertainty.

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

## CI static↔runtime correlation bridge — implementation/proof/ownership complete

UpgradePilot now keeps three distinct evidence responsibilities:

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

Unsupported or ambiguous shapes remain unresolved at the correlation layer.

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

GitHub-generated setup/post/completion steps are allowed as extras. Static source index is not equated with runtime step number.

### Result interpretation boundary

Correlation establishes identity, not success. Positive runtime execution interpretation requires:

```text
runtime status == completed
runtime conclusion == success
+ static continue-on-error absent or literal false
```

The bridge still does not prove exact resolved dependency version, selected/downloaded wheel, wheel compatibility, behavioral compatibility, complete CI coverage, proposal safety, or a maintainer action.

## Implemented source and states

Added:

`src/upgradepilot/ci/workflow_runtime_correlation.py`

Primary entry point:

```text
correlate_workflow_runtime(...)
→ WorkflowRuntimeCorrelationResult
```

Updated:

`src/upgradepilot/ci/dependency_exercise.py`

New strongest technical CI coverage state:

```text
supported_runtime_correlated
```

This requires already-supported static changed-dependency consumption whose owning user-defined run step is safely correlated to an exact-attempt runtime step with `completed/success` and no visible `continue-on-error` masking.

The prior:

```text
supported_not_correlated
```

remains the conservative fallback when successful exact-head CI + supported static consumption exist but the bounded bridge cannot safely correlate the workflow.

Important state distinction preserved during D:

```text
matrix / unsupported shape
→ correlation result: unresolved
```

but if successful exact-head CI and supported static dependency consumption still exist:

```text
correlation unresolved
+ static consumption supported
+ successful CI
→ dependency-CI coverage: supported_not_correlated
```

A correlated skipped/failed/cancelled/non-completed consuming step becomes unresolved rather than falsely strengthened. Dynamic/true `continue-on-error` likewise keeps successful execution interpretation unresolved.

Static direct exercise remains separate and now also has its own runtime-correlated execution axis.

Updated `src/upgradepilot/maintainer_action.py` only so `supported_runtime_correlated` is recognized as a non-unresolved technical CI state. Synthesis remains abstention-only and gains no new action permission.

## Proof

Added:

- `tests/test_workflow_runtime_correlation.py`
- `tests/test_ci_runtime_correlated_dependency_coverage.py`

Updated:

- `tests/test_maintainer_action.py`

Ali ran narrow-to-broad validation in the real WSL project environment:

```text
focused correlation tests
→ PASS / GREEN

nearest CI / investigation / provider / parser / synthesis regression set
→ PASS / GREEN

full deterministic repository suite
→ Ran 549 tests in 0.144s
→ OK
```

Therefore A/B/C implementation/proof/preservation are closed.

## D ownership result — CLOSED

Ali demonstrated ownership of the central model:

```text
static declaration
+ runtime observation
≠ automatically correlated
```

The bridge uses display names as the matching anchor only under strict surrounding safety conditions: exact workflow/run identity, literal names, uniqueness, whole-set consistency, ordered step matching, and exclusion of unsupported ambiguous shapes.

The safety contract is also the current method boundary: UpgradePilot does not guess a relationship when those conditions do not hold.

Ali also distinguished:

```text
supported_not_correlated
→ static dependency consumption + successful CI, but no safe consuming-step↔runtime-step relationship

supported_runtime_correlated
→ the supported static consuming step is safely tied to a completed-successful runtime step
```

and retained the stronger-claim limit that exact installed version/wheel and compatibility are still unproven.

## Relevant remaining trust restrictions

1. requirements/constraints patch-to-frozen-head correspondence is not established;
2. static command recognition can produce false-positive direct-requirements evidence from unsupported shell text;
3. run/job attempt coherence is repaired and proven;
4. static↔runtime step identity is now correlated only for the bounded ordinary named-workflow class;
5. no exact runtime dependency-version/wheel proof exists yet.

## Immediate continuation — E gap repair / next-slice orientation

E must decide what actually matters next rather than automatically broadening CI support.

Evaluate at least:

```text
current correlation limitations
→ do any real cases/product decisions require matrix/reusable/dynamic-name support now?

supported_runtime_correlated
→ what uncertainty did this actually remove from target/artifact/serviceability reasoning?

remaining evidence gaps
→ correlation breadth?
→ exact runtime dependency/version/artifact proof?
→ static command-recognition trust?
→ another earlier evidence boundary?

possible stronger runtime source
→ are job logs/artifacts justified only after a precise missing proposition is selected?

maintainer-action synthesis
→ does stronger UpgradePilot-executable evidence reduce or eliminate any need for maintainer targeted checks?
```

E is analysis/orientation only until it selects a distinct next responsibility.

## Current canonical Learning-by-Doing cycle

```text
Slice: CI static↔runtime correlation bridge

A — DONE
B — DONE
    full suite: 549 tests OK
C — DONE
D — DONE
E — CURRENT
```

Do not yet parse job logs, add exact wheel-serviceability semantics, enable `run targeted checks`, add non-abstention maintainer actions, redesign CLI/reporting, or expand matrix/reusable/dynamic-name support merely for completeness.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-build-implement`
