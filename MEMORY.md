# UpgradePilot Current Memory

**Last updated:** 2026-09-12  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** B-phase Build for the bounded CI static↔runtime correlation bridge. A is complete; B source/tests are implemented and diff-reviewed, but executable validation is still deferred because the assistant environment cannot resolve `github.com`.
- **Mode:** Learning-by-Doing + Build/Implement. Do not claim B proof complete until focused, nearest, and full deterministic tests pass in Ali's real WSL project environment.
- **Selected parent plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Active working memory:** `working-memory/2026-09-12_ci-static-runtime-correlation-bridge.md`.
- **Previous working memory:** `working-memory/2026-09-11_ci-run-job-attempt-coherence-enhancement.md`.
- **Repository route:** continue directly on `main` unless Ali later requests otherwise.
- **Framework status:** ordinary-Python / LangGraph / LangChain comparison remains closed; no framework re-entry is justified.

## Maintainer-action synthesis state retained

The first deterministic maintainer-action evaluator remains abstention-only:

```text
PublicPullRequestInvestigation
→ synthesize_maintainer_action(...)
→ MaintainerActionSynthesis(action="abstain")
```

No merge, targeted-check, investigate, block, or defer permission is implemented. `run targeted checks` remains paused while UpgradePilot first strengthens its own read-only CI evidence path.

## CI run/job attempt coherence — previous cycle closed

The mixed-rerun-attempt defect is repaired and proven. Exact job acquisition now binds:

```text
frozen PR head SHA
+ workflow run ID
+ run attempt
→ jobs from that exact attempt
```

Previous proof on Ali's WSL environment:

```text
focused provider tests      9  OK
nearest CI/application     31  OK
full deterministic suite  533  OK
```

That Learning-by-Doing cycle is CLOSED A→E.

## CI static↔runtime correlation bridge — A complete

A selected a CI-domain correlation responsibility between the existing factual layers:

```text
STATIC WORKFLOW EVIDENCE
        +
RUNTIME ACTIONS EVIDENCE
        ↓
CI CORRELATION EVIDENCE
        ↓
DEPENDENCY-CI INTERPRETATION
```

Provider objects remain factual-only.

### First admitted job correlation class

Positive job correlation requires:

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

Unsupported/ambiguous shapes remain unresolved.

### First admitted step correlation class

Inside an already-correlated job:

```text
no StepProblem
+ explicit literal non-expression unique static step names
+ runtime steps available with unique strictly ordered numbers
+ every static step name appears exactly once at runtime
+ static step-name sequence is an ordered runtime subsequence
→ static source_index ↔ runtime step number
```

GitHub-generated setup/post/completion steps are allowed as extras. Static source index is not equated with runtime step number.

### Result interpretation boundary

Correlation is identity, not success. Positive runtime execution interpretation requires:

```text
runtime status == completed
runtime conclusion == success
+ static continue-on-error absent or literal false
```

The bridge still does not prove exact resolved dependency version, selected/downloaded wheel, wheel compatibility, behavioral compatibility, complete CI coverage, proposal safety, or a maintainer action.

No job-log work is selected for this bridge.

## B implementation — current state

Implemented on `main`:

### Generic correlation owner

Added:

`src/upgradepilot/ci/workflow_runtime_correlation.py`

It returns either:

```text
correlated
→ static job ↔ runtime job
→ static user step ↔ runtime step

unresolved
→ exact reason/detail
```

The module implements the A-selected job-name bijection and ordered named-step-subsequence rules without changing provider models or making new GitHub requests.

### Dependency-CI integration

Updated:

`src/upgradepilot/ci/dependency_exercise.py`

New strongest technical coverage state:

```text
supported_runtime_correlated
```

This state requires already-supported static changed-dependency consumption whose owning user-defined run step is safely correlated to an exact-attempt runtime step with `completed/success` and no visible `continue-on-error` masking.

The prior state remains:

```text
supported_not_correlated
```

for successful exact-head CI + supported static consumption when the bounded bridge cannot safely correlate the workflow.

If correlation succeeds but the relevant consuming step is skipped/failed/cancelled/non-completed, coverage is unresolved rather than falsely strengthened. Dynamic/true `continue-on-error` likewise keeps successful execution interpretation unresolved.

Static direct exercise remains separate and now also has a distinct runtime-correlated execution axis.

### Maintainer-action compatibility

Updated `src/upgradepilot/maintainer_action.py` only so `supported_runtime_correlated` is recognized as a non-unresolved technical CI state. Synthesis remains abstention-only and gains no new action permission.

### Proof assets added

Added:

- `tests/test_workflow_runtime_correlation.py`
- `tests/test_ci_runtime_correlated_dependency_coverage.py`

Updated:

- `tests/test_maintainer_action.py`

The proof set covers positive job/step correlation, runtime-generated extra steps and number gaps, matrix/reusable/name/order ambiguity, correlated consumption/direct exercise, skipped execution, `continue-on-error` masking, fallback to `supported_not_correlated`, and preservation of abstention-only synthesis.

### B commits so far

```text
d3742f70da6b18287fbd05ec8dbb2b936225edf6  feat: add bounded CI workflow runtime correlation
ac9d03bf4d2e718275baa4acb9eabde78ea59ad5  test: prove bounded workflow runtime correlation
0ba88f19c4b14589016119e6f1c7572d9cbd3672  feat: integrate runtime-correlated CI dependency evidence
783ffa468184d79217cf39fb437c4651215e3f9e  fix: accept runtime-correlated CI support in synthesis input
b28a403534c1057cd0c5601b6d9da93697030c7b  test: prove runtime-correlated dependency CI coverage
f476b4cd5e3ac9ae5e4ae0013e68fd9b71308c69  test: keep runtime-correlated CI outside action permission
6730d222eb60547437966f799bee0df8056f4a51  docs: preserve CI correlation B implementation checkpoint
```

## Validation status / current proof debt

Attempted narrow validation in the assistant execution environment, but repository acquisition failed before tests could start:

```text
git clone https://github.com/motafegh/UpgradePilot.git
→ Could not resolve host: github.com
```

This is an assistant-container DNS/network limitation, not a product failure and not a passing test result.

Required next executable proof on Ali's WSL project environment:

```text
python -m unittest \
  tests.test_workflow_runtime_correlation \
  tests.test_ci_runtime_correlated_dependency_coverage \
  -v

python -m unittest \
  tests.test_ci_dependency_coverage \
  tests.test_investigation \
  tests.test_maintainer_action \
  tests.test_github_actions \
  tests.test_github_workflow_definition \
  -v

python -m unittest discover -s tests -v
```

Do not move B to DONE until these are executed successfully or a real failure is diagnosed and repaired.

## Relevant remaining trust restrictions

1. requirements/constraints patch-to-frozen-head correspondence is not established;
2. static command recognition can produce false-positive direct-requirements evidence from unsupported shell text;
3. run/job attempt coherence is repaired and proven;
4. the new correlation bridge addresses static↔runtime step identity only for the bounded ordinary named-workflow class;
5. no exact version/wheel runtime proof exists yet.

## Immediate continuation — canonical LbD cycle

```text
Slice: CI static↔runtime correlation bridge

A — DONE

B — CURRENT:
    source/tests implemented and diff-reviewed;
    executable validation pending in Ali's WSL environment.

C — NOT STARTED:
    preserve final implementation/proof state after B validation closes.

D — NOT STARTED
E — NOT STARTED
```

Do not yet parse job logs, add wheel-serviceability semantics, enable `run targeted checks`, add non-abstention maintainer actions, or redesign CLI/reporting.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-build-implement`
