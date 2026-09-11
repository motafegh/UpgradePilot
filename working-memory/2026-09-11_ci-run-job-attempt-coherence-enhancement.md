# CI Run/Job Attempt-Coherence Enhancement — Working Memory

**Date:** 2026-09-11  
**Session status:** ACTIVE  
**Primary mode:** Build/Implement + Learning-by-Doing  
**Parent selected plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Supporting historical investigation owner:** [`../plans/SYSTEM_LIMITATIONS_AND_CORRECTNESS_INVESTIGATION_PLAN.md`](../plans/SYSTEM_LIMITATIONS_AND_CORRECTNESS_INVESTIGATION_PLAN.md)  
**Previous:** [`2026-09-11_targeted-check-action-admission.md`](2026-09-11_targeted-check-action-admission.md)

## Session anchor

The targeted-check maintainer-action A-phase exposed an upstream evidence-reliability dependency rather than a synthesis rule to invent downstream. Exact artifact/wheel serviceability may later benefit from trustworthy exact-CI execution evidence, but the current GitHub Actions acquisition path can combine a captured `WorkflowRun` from one attempt with `latest` jobs from a later rerun.

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

## A-phase findings

Current source establishes:

- `WorkflowRun` preserves `run_id`, `head_sha`, and `run_attempt`;
- `get_workflow_jobs(...)` currently requests `/actions/runs/{run_id}/jobs` with `filter="latest"`;
- `WorkflowJob` preserves job/run/head/status/conclusion/steps but no attempt field;
- `_parse_workflow_job(...)` protects run-ID and frozen-head coherence;
- the application preserves each `WorkflowRun` together with its returned jobs and passes that pair into `WorkflowDependencyCoverageInput`;
- current focused tests protect run/head identity, job parsing, step summaries, pagination, and the existing `latest` request, but not same-attempt coherence.

Authoritative GitHub REST documentation confirms a dedicated endpoint:

```text
GET /repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/jobs
```

where `attempt_number` is a required path parameter and pagination remains `per_page` + `page`.

## A-phase design decision — ACCEPTED

Ali accepted **Option 1** after the ownership/proportionality analysis.

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
- no admitted current consumer has been found that receives a job independently and needs to re-establish attempt identity;
- this is the smallest mechanism satisfying the actual defect and proof boundary.

### Rejected for now — Option 2: duplicate `run_attempt` on every `WorkflowJob`

Do **not** add a job-level attempt field in this slice.

It could make standalone jobs more self-describing, but current evidence does not establish a separate provenance, serialization, persistence, alternate-composition, or independent-consumer responsibility that needs the duplicate metadata. Under Core `JUST-003` through `JUST-005`, adding it now would be unsupported propagation/validation ceremony.

**Re-entry condition:** reconsider job-level attempt metadata only if a real admitted consumer or boundary later needs a `WorkflowJob` independently from its owning `WorkflowRun` and must inspect/re-establish attempt identity.

## B-phase implementation boundary

Implement only:

1. change job acquisition to the attempt-specific jobs endpoint using the captured `run.run_attempt`;
2. remove `filter="latest"` from that request;
3. preserve existing run-ID/head-SHA validation and job representation;
4. update focused provider tests to prove attempt-1 and attempt-2 request coordinates plus pagination on the same attempt path;
5. preserve mismatch rejection and step parsing;
6. run focused provider tests, nearest CI/application regressions, then broader deterministic tests as justified.

Do not add logs, runtime command correlation, wheel witness semantics, target-environment reconstruction, synthesis actions, CLI changes, or unrelated reliability repairs in this slice.

## Proof shape

Focused proof should discriminate the old defect boundary by establishing:

```text
captured attempt 1 → /attempts/1/jobs
captured attempt 2 → /attempts/2/jobs
pagination page 1/2 → same captured attempt path
no `filter="latest"`
existing run/head mismatch checks remain
```

The earlier controlled rerun reproduction remains the evidence for why this correction is needed; the new permanent tests protect the corrected provider contract without duplicating the entire race diagnostic downstream.

## Learning-by-Doing state

```text
Slice: CI run/job attempt coherence

A — DONE:
    confirmed the historical defect, verified the attempt-specific GitHub endpoint,
    traced current producer/consumer ownership, selected Option 1, and rejected
    duplicate job-level attempt metadata until a concrete independent consumer exists.

B — CURRENT:
    implement the exact-attempt provider request and focused regression proof only.

C — NOT STARTED:
    preserve exact changed source/tests, executed validation, surprises, proof limits,
    and any resulting live-state change.

D — NOT STARTED:
    teach from the actual provider → run/jobs → CI-consumer flow and check ownership
    of what same-attempt identity proves and what remains unproven.

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
