# CI Run/Job Attempt-Coherence Enhancement — Working Memory

**Date:** 2026-09-11  
**Session status:** ACTIVE  
**Primary mode:** Planning/Design orientation + Learning-by-Doing; bounded Build is authorized after A resolves the smallest correction shape  
**Parent selected plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Supporting historical investigation owner:** [`../plans/SYSTEM_LIMITATIONS_AND_CORRECTNESS_INVESTIGATION_PLAN.md`](../plans/SYSTEM_LIMITATIONS_AND_CORRECTNESS_INVESTIGATION_PLAN.md)  
**Previous:** [`2026-09-11_targeted-check-action-admission.md`](2026-09-11_targeted-check-action-admission.md)

## Session anchor

The targeted-check maintainer-action A-phase exposed a real upstream dependency rather than a synthesis rule to invent downstream. Exact artifact/wheel serviceability may benefit from trustworthy exact-CI execution evidence, but the current GitHub Actions acquisition path does not establish that the `WorkflowRun` metadata and acquired `WorkflowJob` records belong to the same workflow **attempt** after a rerun.

This is a legitimate re-entry trigger for intentionally deferred CI reliability work:

```text
maintainer-action synthesis
→ needs stronger producer-grounded evidence before a targeted-check permission can be earned
→ exact CI execution evidence is a candidate source
→ exact CI execution evidence first needs coherent run/job attempt identity
→ repair the CI acquisition identity boundary before richer CI evidence work
```

### Correction to the initial re-entry summary

The September 8 correctness investigation did not leave this only as a seed hypothesis. It later executed a controlled fake-provider rerun sequence against the actual Actions parsing and CI evaluator and **confirmed** the defect within that proof boundary.

The reproduced contrast included:

```text
captured run attempt 1 / success
+
latest jobs from attempt 2
→ accepted as one evidence pair because run_id and head_sha still matched
```

The controlled cases showed that mixed-attempt evidence could preserve `supported_not_correlated` in one rerun shape and produce `no_successful_ci` in another, while a coherent failed-attempt control produced `workflow_not_successful`. A wrong-run-ID control was correctly rejected. This established an acquisition/normalization consistency defect and a downstream classification consequence; it did not establish public-case frequency, runtime dependency exercise, or a wrong maintainer recommendation.

The repair itself remained deliberately unselected at that time. The current user has now explicitly selected this bounded CI enhancement cycle because downstream synthesis supplies a concrete activation reason.

## Exact responsibility

Strengthen the GitHub Actions evidence path so a workflow run and the jobs consumed with it are demonstrably from the **same run attempt**, while preserving the already-established exact PR-head and run-ID identity checks.

The intended invariant is:

```text
frozen PR head SHA
+ exact workflow run ID
+ exact workflow run attempt
+ jobs acquired for that same run attempt
→ coherent factual CI execution evidence
```

This slice does **not** yet establish that a dependency was installed, exercised, wheel-compatible, or safe. It establishes only the identity/provenance prerequisite needed before stronger runtime observations can be trusted.

## Current implementation facts entering A

Current source establishes:

- `WorkflowRun` preserves `run_id`, `head_sha`, and `run_attempt`;
- `GitHubActionsClient.get_workflow_jobs(...)` checks that the requested run is bound to the frozen PR head;
- job acquisition currently uses the run-level jobs endpoint with `filter="latest"`;
- `WorkflowJob` preserves `job_id`, `run_id`, `head_sha`, status/conclusion and optional step summaries, but not an attempt identity;
- `_parse_workflow_job(...)` verifies only run ID and frozen PR head correspondence;
- current acquisition tests protect exact-head filtering, run/job IDs, step parsing, pagination behavior and the `latest` filter, but do not prove same-attempt run/job coherence;
- the application preserves each acquired `WorkflowRun` together with the `WorkflowJob` tuple returned for that run and passes that pair together into `WorkflowDependencyCoverageInput`.

The CI interpretation layer already states a separate limitation: successful exact-head runtime evidence and static changed-dependency consumption are not correlated to runtime step execution. This attempt-coherence slice must not silently claim to repair that different boundary.

## A-phase authoritative API finding

GitHub exposes a dedicated read-only endpoint for jobs from a **specific workflow run attempt**:

```text
GET /repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/jobs
```

The attempt number is a path parameter. Pagination remains `per_page` + `page`; the attempt-specific endpoint does not use the generic run-level `filter="latest"` selector.

This directly supplies the missing provider primitive: the already-captured `WorkflowRun.run_attempt` can select the same attempt when jobs are acquired.

## A-phase ownership/representation analysis

Two candidate correction shapes were considered:

### Option 1 — bind acquisition to the captured attempt at the provider boundary

```text
WorkflowRun(run_id, head_sha, run_attempt)
→ request /runs/{run_id}/attempts/{run_attempt}/jobs
→ existing job run_id/head_sha validation
→ existing (run, jobs) pair
→ CI consumer
```

This repairs the normal producer path at the earliest sufficient owner. The API request itself establishes which attempt supplied the returned collection, while the existing run/job pair retains that acquisition context through the normal application flow.

### Option 2 — bind acquisition and also add `run_attempt` to every `WorkflowJob`

This could make standalone job objects self-describing, but no current admitted normal-flow consumer has been found that receives a `WorkflowJob` without its owning `WorkflowRun` and independently needs to re-establish attempt identity. GitHub's attempt-specific jobs response also identifies the attempt through the request path rather than a job-level `run_attempt` field in the documented response schema.

Under Core `JUST-003` through `JUST-005`, current evidence therefore favors **Option 1 as the smallest credible correction**. Adding a duplicate job field/check would need an independent provenance, serialization, persistence, alternate-composition, or consumer responsibility that is not currently admitted. If such a responsibility appears later, reconsider it then rather than pre-building it now.

## A-phase discriminating proof shape

The focused provider proof should establish at least:

1. a captured attempt-1 run requests `/attempts/1/jobs` and no `filter="latest"`;
2. a captured attempt-2 run requests `/attempts/2/jobs`, demonstrating that acquisition follows the captured run rather than whichever rerun is latest when the jobs call occurs;
3. existing run-ID/head-SHA mismatch rejection remains intact;
4. pagination stays bound to the same attempt path across pages;
5. nearest application/CI tests continue to consume `(run, jobs)` without a new job-level attempt contract.

The prior controlled rerun reproducer remains the reason for the correction; the new focused tests should protect the corrected provider contract rather than recreate an entire race simulator inside every downstream layer.

## Scope

In scope for this slice:

- use the authoritative GitHub Actions specific-attempt jobs semantics;
- implement the smallest provider change that makes same-attempt acquisition enforceable and inspectable;
- update `src/upgradepilot/github/actions.py` only as needed for that invariant;
- update focused GitHub Actions acquisition tests with attempt-specific and pagination protection;
- update downstream CI/domain tests only where the provider contract change genuinely requires it;
- run focused and nearest deterministic regressions, then the broader deterministic suite when the bounded change is ready;
- preserve exact proof limits and return to the synthesis dependency only after the cycle closes.

Out of scope for this slice:

- job-log parsing;
- proving dependency installation from runtime logs;
- producing a wheel-serviceability witness;
- reconstructing or executing a third-party target environment;
- changing artifact-serviceability semantics;
- enabling `run targeted checks` in synthesis;
- CLI/report redesign;
- repairing unrelated command-recognition or PR patch/revision findings;
- broad GitHub Actions feature expansion.

## Canonical Learning-by-Doing cycle

```text
A — CURRENT: PRE-IMPLEMENTATION ORIENTATION
    Current provider/consumer path, confirmed historical defect, authoritative
    attempt-specific API and smallest correction shape are now mapped. Remaining A work
    is the learner/ownership decision on provider-bound attempt identity versus adding
    duplicate job-level attempt metadata before Build begins.

B — NOT STARTED: REAL BOUNDED BUILD / ACTION
    Implement the smallest same-attempt acquisition correction at the owning provider
    boundary; preserve exact PR-head/run identity; add focused attempt-specific and
    pagination contrasts; propagate representation only where genuinely required;
    validate nearest CI composition without adding richer runtime-evidence semantics.

C — NOT STARTED: PROGRESSIVE STATE PRESERVATION
    Record the exact implementation, tests/commands/results, surprises/corrections,
    proof strength and remaining non-proof. Reconcile MEMORY.md only when the live
    continuation materially changes.

D — NOT STARTED: POST-IMPLEMENTATION LEARNING / OWNERSHIP CHECK
    Learn from the actual provider → typed evidence → CI-consumer flow. Explain what
    exact attempt binding now proves, what it still does not prove about step execution
    or dependency/wheel behavior, and reason about the focused tests and failure modes.

E — NOT STARTED: GAP REPAIR + NEXT-SLICE ORIENTATION
    Repair any implementation or understanding gap. Then decide, from evidence, whether
    the next justified CI slice is a read-only positive execution/wheel-serviceability
    witness or whether enough upstream proof exists to return directly to targeted-check
    synthesis. Do not silently start either next responsibility before D/E closes.
```

## A-phase acceptance intent

Before B, we need enough evidence to answer:

1. What exact GitHub API operation binds jobs to a named workflow run attempt? **Established: the specific-attempt jobs endpoint.**
2. Does the provider need to preserve attempt identity on each `WorkflowJob`, or is endpoint-level binding plus existing run identity sufficient and testable? **Current design hypothesis: endpoint-level binding is sufficient for the admitted normal flow; learner/ownership review remains.**
3. What controlled evidence discriminates the correction? **Established: attempt-specific request coordinates plus the previously confirmed rerun-mixing contrast.**
4. Which downstream consumers depend only on coherent jobs and therefore need no semantic redesign? **Current normal application/CI composition keeps the owning run and jobs together; no independent job-only attempt consumer has been found.**
5. What stronger claims remain intentionally unavailable after the fix? **Runtime step correlation, dependency installation/exercise, exact wheel compatibility, complete CI coverage, safety and maintainer-action permission remain unavailable.**

The simplest credible correction should win. Do not add an attempt registry, workflow orchestration layer, log subsystem, duplicated job metadata without a consumer need, or generalized CI identity framework merely to solve this defect.

## Proof target for this slice

A successful bounded result should establish:

```text
same frozen PR head
+ same workflow run ID
+ explicitly selected run attempt
+ jobs acquired from that exact attempt
```

with focused controlled tests that prove request binding to the captured attempt and preserve existing identity/pagination behavior.

It still must **not** be interpreted as proof that:

- a statically visible install command executed;
- the changed dependency was installed successfully;
- a particular wheel served the environment;
- all CI environments were covered;
- the proposal is safe or should receive any maintainer action.

## Return path

After this cycle closes, return to the targeted-check/admissible-evidence question with the stronger CI identity boundary. Only then decide whether a second CI evidence slice is justified for a positive runtime/wheel witness. If that evidence capability is not justified or cannot be established safely, synthesis must preserve the limitation rather than manufacture a maintainer check.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-planning-design`
