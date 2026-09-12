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

## B-phase implementation — source and focused proof

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

This establishes that the exact-attempt provider contract works under the focused mocked-response proof and that the existing CI coverage/application investigation consumers continue to behave across the nearest deterministic regression boundary.

### Proof still outstanding before B is fully closed

The parent plan and this slice call for a broader deterministic regression after focused and nearest proof. That broader suite has **not yet been run for this exact implementation checkpoint**. Therefore do not yet claim repository-wide deterministic regression closure.

No live/public GitHub rerun race was required to prove the correction: the historical controlled reproducer established the defect, and the permanent provider tests now protect the corrected attempt-specific request contract.

## Proof limits retained

Even with the focused and nearest suites green, this correction proves only coherent run/job attempt acquisition. It does **not** establish that:

- a statically visible install command executed;
- the changed dependency was installed or exercised successfully;
- a particular wheel served an environment;
- exact wheel compatibility is known;
- all relevant CI environments are covered;
- the proposal is safe;
- any maintainer action is justified.

The separate command-recognition and PR patch/revision reliability findings also remain unchanged.

## Learning-by-Doing state

```text
Slice: CI run/job attempt coherence

A — DONE:
    confirmed the historical defect, verified the attempt-specific GitHub endpoint,
    traced producer/consumer ownership, selected Option 1, and rejected duplicate
    job-level attempt metadata until a concrete independent consumer exists.

B — CURRENT:
    source correction and focused/nearest deterministic proof are complete and green;
    broader repository deterministic regression remains before B proof closure.

C — CURRENT:
    source/test commits, exact local commands/results, proof strength and proof limits
    are preserved here; final B validation result still needs to be added.

D — NOT STARTED:
    after B proof closes, teach from the actual provider → run/jobs → CI-consumer flow
    and check ownership of what same-attempt identity proves and leaves unresolved.

E — NOT STARTED:
    repair any remaining gap, then decide whether richer read-only CI execution/wheel
    evidence is justified or whether to return directly to targeted-check synthesis.
```

## Return path

After this cycle closes, return to the targeted-check/admissible-evidence question with the stronger CI identity boundary. A separate later slice may evaluate a positive runtime/wheel-serviceability witness; this slice does not pre-authorize that capability.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-build-implement`
