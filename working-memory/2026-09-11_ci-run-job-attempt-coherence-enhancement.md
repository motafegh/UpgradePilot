# CI Run/Job Attempt-Coherence Enhancement — Working Memory

**Date:** 2026-09-11  
**Session status:** ACTIVE  
**Primary mode:** Build/Implement + Learning-by-Doing  
**Parent selected plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Supporting historical investigation owner:** [`../plans/SYSTEM_LIMITATIONS_AND_CORRECTNESS_INVESTIGATION_PLAN.md`](../plans/SYSTEM_LIMITATIONS_AND_CORRECTNESS_INVESTIGATION_PLAN.md)  
**Previous:** [`2026-09-11_targeted-check-action-admission.md`](2026-09-11_targeted-check-action-admission.md)

## Session anchor

The targeted-check maintainer-action A-phase exposed an upstream evidence-reliability dependency rather than a synthesis rule to invent downstream. Exact artifact/wheel serviceability may later benefit from trustworthy exact-CI execution evidence, but the prior GitHub Actions acquisition path could combine a captured `WorkflowRun` from one attempt with `latest` jobs from a later rerun.

This is now an admitted CI re-entry because downstream synthesis supplies a concrete need:

```text
maintainer-action synthesis
→ may need stronger producer-grounded CI execution evidence
→ stronger CI evidence first needs coherent run/job attempt identity
→ repair CI acquisition identity before richer CI evidence work
```

## Confirmed historical defect

The September 8 correctness investigation did not leave this merely hypothetical. A controlled fake-provider rerun sequence against the actual Actions parsing and CI evaluator confirmed that:

```text
captured run attempt 1 / success
+
latest jobs from attempt 2
→ can be accepted as one evidence pair
because run_id and head_sha still match
```

The reproduced contrasts showed downstream classification differences while the wrong-run-ID control was correctly rejected. The proof established an acquisition/normalization consistency defect, not public-case frequency, runtime dependency exercise, wheel compatibility, or a maintainer recommendation.

## Exact responsibility

Strengthen the GitHub Actions evidence path so a workflow run and the jobs consumed with it are demonstrably from the **same workflow run attempt**, while preserving exact PR-head and run-ID identity checks.

Required bounded invariant:

```text
frozen PR head SHA
+ exact workflow run ID
+ exact workflow run attempt
+ jobs acquired for that same attempt
→ coherent factual CI execution evidence
```

This slice does not establish static-to-runtime step correlation, dependency installation/exercise, wheel compatibility, complete CI coverage, safety, or a maintainer action.

## A-phase findings and accepted design

Current source entering the slice established:

- `WorkflowRun` preserves `run_id`, `head_sha`, and `run_attempt`;
- `get_workflow_jobs(...)` used `/actions/runs/{run_id}/jobs` with `filter="latest"`;
- `WorkflowJob` preserves job/run/head/status/conclusion/steps but no attempt field;
- `_parse_workflow_job(...)` protects run-ID and frozen-head coherence;
- the application preserves each `WorkflowRun` together with its returned jobs and passes that pair into `WorkflowDependencyCoverageInput`.

Authoritative GitHub REST documentation confirms a dedicated endpoint:

```text
GET /repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/jobs
```

### Selected — Option 1: provider-bound exact-attempt acquisition

```text
WorkflowRun(run_id, head_sha, run_attempt)
→ request /runs/{run_id}/attempts/{run_attempt}/jobs
→ retain existing job run_id/head_sha validation
→ preserve existing (run, jobs) pair
→ CI consumer
```

Reasoning:

- the provider is the earliest sufficient owner of the acquisition-identity proposition;
- the exact attempt is selected by the API request itself;
- the normal application flow keeps the owning run and jobs together;
- no admitted current consumer needs a standalone job to independently re-establish attempt identity;
- this is the smallest mechanism satisfying the defect and proof boundary.

### Rejected for now — Option 2: duplicate `run_attempt` on every `WorkflowJob`

Do **not** add a job-level attempt field in this slice. Current evidence does not establish a separate provenance, persistence, serialization, alternate-composition, or independent-consumer responsibility that needs duplicate attempt metadata. Under Core `JUST-003` through `JUST-005`, adding it now would be unsupported propagation/validation ceremony.

**Re-entry condition:** reconsider job-level attempt metadata only if a real admitted consumer or boundary later needs a `WorkflowJob` independently from its owning `WorkflowRun` and must inspect/re-establish attempt identity.

## B-phase implementation — source and proof

Implemented on `main`:

- `src/upgradepilot/github/actions.py`
  - `get_workflow_jobs(...)` now requests `/actions/runs/{run_id}/attempts/{run.run_attempt}/jobs`;
  - `filter="latest"` was removed;
  - existing run/head validation and `WorkflowJob` representation remain unchanged.
- `tests/test_github_actions.py`
  - attempt 1 request is bound to `/attempts/1/jobs`;
  - attempt 2 request is bound to `/attempts/2/jobs`;
  - multi-page acquisition keeps the same attempt path;
  - no `filter` parameter remains;
  - run-ID/head-SHA rejection and step parsing remain protected.

Implementation commits:

```text
2cd930afee6127d9f3bfd2fb4492e16f9ec85261  fix: bind workflow jobs to captured run attempt
e01785e7364e015365d9a676792e0f70e9431a17  test: prove workflow job attempt binding
```

### Executed proof on Ali's WSL project environment

Ali synchronized local `main` through `e01785e7` and used the project `.venv`.

Focused provider suite:

```text
python -m unittest discover -s tests -p 'test_github_actions.py' -v
→ 9 tests
→ OK
```

Nearest CI/application regression set:

```text
python -m unittest \
  tests.test_ci_dependency_coverage \
  tests.test_investigation \
  -v
→ 31 tests
→ OK
```

Broader repository deterministic suite:

```text
python -m unittest discover -s tests -v
→ 533 tests
→ OK
```

Together these results establish the attempt-specific provider request contract, preserve the nearest CI/application consumers, and close the broader deterministic regression obligation for this exact implementation checkpoint.

No live/public GitHub rerun race was required to prove the correction: the historical controlled reproducer established the defect, and the permanent provider tests now protect the corrected attempt-specific request contract.

## Proof limits retained

Even with the focused, nearest, and broader suites green, this correction proves only coherent run/job attempt acquisition. It does **not** establish that:

- a statically visible install command executed;
- the changed dependency was installed or exercised successfully;
- a particular wheel served an environment;
- exact wheel compatibility is known;
- all relevant CI environments are covered;
- the proposal is safe;
- any maintainer action is justified.

The separate command-recognition and PR patch/revision reliability findings also remain unchanged.

## D-phase ownership result

The implementation/learning review established the intended mental model:

```text
run_id
→ identifies one workflow run

run_attempt
→ identifies which execution/rerun of that workflow run

(run_id, run_attempt)
→ selects the exact execution whose jobs are being interpreted
```

The key correction is therefore provenance/identity, not a new CI capability. The provider now guarantees that the `WorkflowRun` and acquired jobs belong to the same attempt. That does not by itself establish what dependency-related commands executed inside those jobs.

A second distinction is now explicit:

```text
static workflow evidence
→ what the YAML declares

runtime Actions evidence
→ what GitHub reports about the executed run/job/step
```

Those sources must not be silently collapsed into a stronger execution claim.

## E-phase initial analysis — existing runtime layer

Current source already contains more runtime structure than run/job status alone:

- `WorkflowJob.steps` carries optional `WorkflowStep` records;
- each `WorkflowStep` preserves `number`, `name`, `status`, and `conclusion` from GitHub;
- provider tests explicitly protect step-summary parsing;
- therefore factual runtime step summaries are already acquired when GitHub supplies them.

However, `src/upgradepilot/ci/dependency_exercise.py` intentionally keeps three propositions separate:

```text
1. successful exact-head runtime workflow/job authority
2. static changed-dependency consumption
3. stronger static direct changed-package exercise
```

The module states that the static propositions are **not correlated to runtime step execution**. Its strongest current state is consequently named:

```text
supported_not_correlated
```

The current evaluator uses run/job success as runtime authority and the exact workflow definition for static consumption/exercise. It does not inspect `WorkflowJob.steps` to prove that the statically identified consuming or invocation step actually executed. Current CI coverage tests reinforce that boundary: helper jobs use `steps=()` while still establishing `supported_not_correlated` when static consumption plus successful run/job evidence exist.

Therefore the present capability boundary is:

```text
exact coherent run/job attempt                    ✅
run/job runtime success                           ✅
runtime step summaries acquired by provider       ✅
static dependency consumption/exercise analysis   ✅
static step ↔ runtime step correlation             ❌
runtime proof that dependency install executed    ❌
runtime proof of exact installed version/wheel     ❌
```

### E-phase question now under investigation

Before selecting another Build slice, determine the smallest trustworthy bridge from the already-acquired runtime evidence to a stronger dependency-specific execution proposition.

Candidate questions, in order:

1. Can GitHub's existing step summaries safely correlate a static YAML step with the executed runtime step, and under what identity/name/order constraints?
2. If step summaries are insufficient because they do not expose command/output semantics, is bounded read-only job-log evidence required?
3. What exact stronger claim would either route justify: step execution, dependency/version installation, or only a narrower positive witness?
4. What failure/ambiguity cases must remain unresolved rather than inferred?

No log parsing, wheel-serviceability semantics, or implementation is authorized by this initial E analysis alone.

## Learning-by-Doing state

```text
Slice: CI run/job attempt coherence

A — DONE:
    confirmed the historical defect, verified the attempt-specific GitHub endpoint,
    traced producer/consumer ownership, selected Option 1, and rejected duplicate
    job-level attempt metadata until a concrete independent consumer exists.

B — DONE:
    exact-attempt provider acquisition and focused regression tests are implemented;
    9 focused provider tests, 31 nearest CI/application regressions, and the full
    533-test deterministic suite all pass on Ali's WSL project environment.

C — DONE:
    source/test commits, exact local commands/results, proof strength, proof limits,
    selected/rejected design alternatives, and the remaining non-proofs are preserved.

D — DONE:
    ownership review established run ID vs attempt identity, provider-level provenance,
    and the separation between static declarations and runtime execution evidence.

E — CURRENT:
    inspect the already-existing runtime step-summary path and decide whether it can
    support trustworthy static→runtime correlation or whether bounded job-log evidence
    is required for the next independently justified slice.
```

## Return path

After E selects or rejects a stronger CI-evidence route, return to the targeted-check/admissible-evidence question with the strongest justified producer-grounded CI evidence. A separate later slice may evaluate a positive runtime/wheel-serviceability witness; this record does not pre-authorize that capability.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-build-implement`
