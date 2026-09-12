# CI Static↔Runtime Correlation Bridge — Working Memory

**Date:** 2026-09-12  
**Session status:** ACTIVE  
**Primary mode:** Planning/Design + Learning-by-Doing  
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

`src/upgradepilot/ci/dependency_exercise.py` deliberately does not correlate those layers. Its strongest current result remains `supported_not_correlated` when successful exact-head runtime CI and supported static dependency consumption coexist.

The new responsibility is a bounded third layer:

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

## A-phase responsibility

Determine the **smallest sound static↔runtime correlation contract** UpgradePilot can admit from evidence it already acquires, before considering job logs or any new runtime source.

A had to resolve:

1. positive job-correlation conditions;
2. positive step-correlation conditions;
3. ambiguity/unresolved conditions;
4. correct owner/layer;
5. exact proposition earned by correlation;
6. later Build proof strategy;
7. what remains outside the claim and what would justify a later log-evidence slice.

## Source facts entering A

### Static provider

`src/upgradepilot/github/workflow_definition.py` already preserves:

- `StepsJobDefinition.key` — static `jobs.<job_id>`;
- optional job `name` plus `contains_expression`;
- strategy/matrix structure as static values;
- ordered job `source_index`;
- ordered `RunStepDefinition.source_index` / `UsesStepDefinition.source_index`;
- optional step `name` plus `contains_expression`;
- `run:` command for run steps;
- conditions, `continue-on-error`, shell and working-directory where admitted;
- `JobProblem` / `StepProblem` instead of silently flattening unsupported structure;
- reusable-workflow jobs as a separate type.

### Runtime provider

`src/upgradepilot/github/actions.py` already preserves:

```text
WorkflowRun:
  run_id / workflow_id / head_sha / run_attempt / status / conclusion

WorkflowJob:
  job_id / run_id / name / head_sha / status / conclusion / optional steps

WorkflowStep:
  number / name / status / conclusion
```

Job acquisition is already complete/paginated and bound to the exact `(run_id, run_attempt)` plus frozen PR head.

### Existing static dependency locations

Static CI consumption/exercise evidence already carries the coordinates needed by a bridge:

```text
job_key
step_source_index
segment_index
command
```

Therefore the bridge does not need to rediscover dependency semantics. It only needs to map existing static job/step coordinates to factual runtime job/step records.

## Authoritative GitHub findings

Fresh GitHub documentation established:

- `jobs.<job_id>` is unique only inside the static workflow `jobs` object;
- `jobs.<job_id>.name` is the job display name;
- matrix strategy can expand one static job definition into many runtime jobs;
- the workflow-job REST payload exposes runtime numeric job ID, runtime display name, run/head identity, status/conclusion and step summaries, but no documented static YAML `jobs.<job_id>` field;
- a workflow step `id` is unique inside workflow syntax, but current runtime step summaries do not expose that YAML step ID;
- step `name` is the GitHub display name;
- `if` may prevent a step from running;
- step conclusion may be `success`, `failure`, `cancelled` or `skipped`;
- with `continue-on-error`, step **conclusion** can be `success` while its pre-policy **outcome** was `failure`;
- GitHub adds runtime-only `Set up job` and `Complete job` steps, and actions may add `Post ...` steps, so static source index and runtime step number are not the same coordinate system.

No adjacent documented Checks API field supplied a stronger static-job identifier.

## Real UpgradePilot evidence used in A

Historical UpgradePilot workflow at commit `d72011c1af2f3167ad9a552795c80876e85d0731` contains one static matrix job:

```yaml
jobs:
  test:
    name: Python ${{ matrix.python-version }}
    strategy:
      matrix:
        python-version: ["3.12", "3.13", "3.14"]
```

Workflow run `29695769492` produced three runtime jobs:

```text
Python 3.12
Python 3.13
Python 3.14
```

This directly proves why one-static-job↔one-runtime-job cannot be a generic assumption.

The same real run also showed the positive step-shape pressure:

```text
static user steps:
Check out repository
Set up Python
Install package
Compile source and tests
Run tests
Exercise bootstrap CLI

runtime steps:
Set up job
Check out repository
Set up Python
Install package
Compile source and tests
Run tests
Exercise bootstrap CLI
Post Set up Python
Post Check out repository
Complete job
```

The user-defined names remain in order while GitHub-generated steps appear around them and runtime step numbers contain gaps. This supports an **ordered named-subsequence** design rather than source-index==runtime-number matching.

## A selected design

### 1. Ownership / layer

Selected:

```text
GitHub static provider
→ factual workflow definition

GitHub runtime provider
→ factual run/job/step observations

CI correlation owner
→ deterministic relationship between those two factual sources

CI dependency coverage
→ interprets correlated runtime status for dependency-specific evidence
```

Do **not** place static↔runtime correlation in `github/actions.py`: the provider does not own cross-source CI meaning. Do **not** bury generic correlation inside dependency-specific command recognition either. The simplest justified structure is a small CI-domain correlation responsibility, likely a focused module such as `ci/workflow_runtime_correlation.py`, consumed by `ci/dependency_exercise.py`.

No ADR is justified: this is a bounded deterministic composition rule, not a new cross-cutting framework/service/persistence method. No Core/Generality specification change is required: existing `OBS-001`, `PROV-001`, `STATE-001`, `JUST-003/004`, and `GEN-006/007/012` already require the selected separation, traceability and unresolved behavior.

### 2. First admitted job-correlation class

The first positive job bridge is intentionally bounded to ordinary non-matrix steps workflows.

Positive admission requires the whole workflow/job set to be unambiguous:

```text
exact static workflow revision == run head SHA
+ run/jobs already same exact run attempt
+ workflow definition parses successfully
+ every static job is StepsJobDefinition
+ no reusable-workflow job / JobProblem
+ no strategy/matrix in the first admitted class
+ every static job has an explicit literal non-expression name
+ static job names are unique
+ runtime job names are unique
+ static-name set == runtime-name set
→ one-to-one static job key ↔ runtime job ID correlation
```

Using the full set as a bijection prevents one convenient name match from hiding another unnamed/dynamic/duplicate job that could collide.

Explicit unresolved cases include:

- matrix/strategy job;
- reusable-workflow job;
- `JobProblem` / workflow parse problem;
- missing job name;
- dynamic/expression job name;
- duplicate static job names;
- duplicate runtime job names;
- missing or extra runtime jobs / name-set mismatch.

The bridge does not guess a default relationship between an unnamed static `job_id` and runtime name because GitHub does not document a first-class runtime static-job-ID field.

### 3. First admitted step-correlation class

Step correlation occurs only inside an already-correlated job.

Positive admission requires:

```text
correlated static/runtime job
+ no StepProblem in the static job
+ every user-declared static step has an explicit literal non-expression name
+ static step names are unique
+ runtime steps are present
+ runtime step numbers are unique and monotonically ordered
+ each static step name appears exactly once in runtime steps
+ static step-name sequence appears in the same order as an ordered runtime subsequence
→ static step source_index ↔ runtime step number correlation
```

Runtime-only setup/post/completion steps are allowed as extra records and do not break the subsequence.

This intentionally does not use `source_index == runtime number`.

For the current dependency responsibility, only correlated `RunStepDefinition` locations are used to strengthen consumption/direct-exercise evidence. `UsesStepDefinition` records may participate in the ordered structure, but action-internal execution is not reinterpreted as dependency command execution.

Explicit unresolved cases include:

- job correlation unresolved;
- `StepProblem` / unsupported new step shape;
- missing step name;
- dynamic/expression step name;
- duplicate static step names;
- missing runtime step array;
- duplicate/non-monotonic runtime step numbers;
- missing or duplicate runtime match for a static step;
- user-step ordering mismatch.

### 4. Correlation and execution result stay separate

A correct identity relation does not itself mean a step executed successfully.

The correlation evidence should preserve the factual matched runtime step, including its status/conclusion, while dependency-CI interpretation decides the permitted claim.

For a strong **successful-step** interpretation, the target static run step must be correlated and GitHub must report:

```text
status == completed
conclusion == success
```

Additionally, `continue-on-error` must be absent or statically literal false before `conclusion == success` is used as evidence of an unmasked successful step outcome. If it is true or dynamic, correlation may still be valid, but success interpretation remains insufficient because GitHub documents that conclusion may become success even when the underlying step outcome was failure.

A condition does not prevent correlation. A correlated runtime step with `conclusion == skipped` is evidence that the step did **not** execute; it must not become positive execution evidence.

### 5. Exact claim earned by the bridge

The strongest claim this slice should earn is intentionally narrow:

```text
For this exact PR head and workflow run attempt,
this exact statically identified user-defined run step
corresponds to this GitHub runtime step,
and GitHub reports the runtime step's status/conclusion.
```

When the safe success conditions above hold:

```text
this correlated user-defined run step completed with GitHub conclusion=success
```

The bridge does **not** by itself establish:

- that every shell segment in a multi-command step ran or succeeded;
- that the static command recognizer interpreted arbitrary shell text correctly;
- that the changed dependency/version was actually installed;
- which artifact/wheel was selected or downloaded;
- exact wheel compatibility;
- behavioral compatibility;
- all relevant CI environments covered;
- proposal safety;
- any maintainer action.

The existing static command-recognition trust restriction therefore remains independent of the bridge.

### 6. Why job logs are not part of B

Current step summaries are sufficient for the admitted **identity + GitHub step-result** proposition. Adding logs now would violate the simplest-adequate-mechanism rule.

A later read-only log-evidence slice becomes justified only when the selected proposition requires facts absent from the step summary, for example:

```text
which exact dependency version resolved
which artifact/wheel was downloaded/installed
resolver output or command-level runtime details
```

Even then, logs would require their own acquisition/provenance/parsing/claim-limit design; merely downloading a log does not prove wheel serviceability automatically.

## B implementation/proof route selected by A

B should implement the correlation responsibility without broadening into logs or wheel semantics.

Expected bounded source route:

1. add a small CI-domain static↔runtime correlation representation/evaluator;
2. use existing `WorkflowDefinition` / `WorkflowJob` / `WorkflowStep` facts — no new provider request;
3. integrate correlation into `ci/dependency_exercise.py` so supported static dependency consumption can distinguish runtime-correlated successful-step evidence from `supported_not_correlated`;
4. preserve explicit unresolved/non-correlated states and reasons;
5. update only downstream consumers whose current logic assumes `supported_not_correlated` is the sole supported CI state (notably maintainer-action residual-uncertainty presentation if a new stronger coverage state is introduced).

No change to job-attempt acquisition is expected. No static YAML `step.id` addition is required for the first bridge because runtime summaries do not expose that ID.

### Focused proof classes for B

Correlation tests should cover at least:

**Positive**
- multiple ordinary non-matrix jobs with unique literal names;
- named run/uses steps correlated as an ordered subsequence;
- injected `Set up job`, `Post ...`, `Complete job` runtime steps;
- runtime number gaps;
- correlated dependency-consuming run step with completed/success result.

**Job unresolved**
- matrix/strategy;
- reusable workflow;
- missing/dynamic/duplicate static job name;
- duplicate runtime job name;
- runtime/static job-set mismatch.

**Step unresolved/non-positive**
- missing/dynamic/duplicate static step name;
- `StepProblem`;
- missing runtime steps;
- duplicate/non-monotonic runtime numbers;
- missing/duplicate runtime name match;
- order mismatch;
- correlated skipped/failure/cancelled step;
- correlated `continue-on-error: true` or dynamic step must not be strengthened to unmasked-success evidence.

**Integration/regression**
- existing `supported_not_correlated` behavior remains when bridge prerequisites are absent;
- a new correlated-support case is added without changing static consumption semantics;
- target-artifact composition continues to use static CI consumption without turning correlation into wheel compatibility;
- maintainer-action synthesis remains abstention-only and does not treat a stronger CI technical state as a new action permission;
- focused provider/static-parser tests remain green;
- nearest investigation/CI tests then full deterministic repository suite.

## A decision summary

```text
new acquisition needed?          NO
job logs needed for bridge?      NO
provider model expansion?        NO
static step ID needed now?       NO
new CI correlation responsibility? YES
matrix/reusable support now?     NO — explicit unresolved
identity and execution merged?   NO
wheel/version installation proven? NO
```

The design is intentionally conservative but not fixture-specific: it supports the real class of ordinary workflows with explicit literal unique job/step names and safely abstains outside that class, consistent with Minimum Useful Generality.

## Learning-by-Doing state

```text
Slice: CI static↔runtime correlation bridge

A — DONE:
    completed source/API/real-run investigation; selected CI-domain job/step correlation
    contract, explicit unresolved cases, exact claim limits, no-log boundary, and B proof route.

B — READY / NOT STARTED:
    implement the bounded correlation evaluator and integrate the stronger technical CI
    evidence state without adding logs, wheel semantics, or maintainer-action permissions.

C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

## Scope exclusions retained

Do not in B:

- download/parse job logs;
- add exact wheel/version installation semantics;
- reconstruct target environments beyond existing behavior;
- enable `run targeted checks`;
- add merge/investigate/block/defer permissions;
- redesign CLI/reporting;
- force matrix/reusable-workflow support into the first bridge.

`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
