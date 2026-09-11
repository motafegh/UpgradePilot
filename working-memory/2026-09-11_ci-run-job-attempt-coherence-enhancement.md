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

The older correctness investigation recorded this as a seed hypothesis: `WorkflowRun` stores `run_attempt`, while job acquisition requests the latest jobs. That earlier plan deliberately did not authorize product repair. The current user has now explicitly selected this bounded CI enhancement cycle because the downstream synthesis responsibility supplies a concrete reason to re-enter it.

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
- current acquisition tests protect exact-head filtering, run/job IDs, step parsing, pagination behavior and the `latest` filter, but do not prove same-attempt run/job coherence.

The CI interpretation layer already states a separate limitation: successful exact-head runtime evidence and static changed-dependency consumption are not correlated to runtime step execution. This attempt-coherence slice must not silently claim to repair that different boundary.

## Scope

In scope for this slice:

- verify the authoritative GitHub Actions API semantics for acquiring jobs from a **specific run attempt**;
- decide the smallest provider/type change that makes same-attempt acquisition enforceable and inspectable;
- update `src/upgradepilot/github/actions.py` only as needed for that invariant;
- update focused GitHub Actions acquisition tests with stable-attempt and rerun/attempt contrasts;
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
    Re-anchor current CI acquisition/provider contracts, focused tests, the earlier
    attempt-mixing finding, downstream consumers and authoritative GitHub endpoint
    semantics. Decide the smallest enforceable same-attempt identity method and what
    evidence/tests will discriminate it. Do not begin log/wheel evidence work here.

B — NOT STARTED: REAL BOUNDED BUILD / ACTION
    Implement the smallest same-attempt acquisition correction at the owning provider
    boundary; preserve exact PR-head/run identity; add focused stable-attempt and rerun
    contrasts; propagate representation only where genuinely required; validate the
    nearest CI composition without adding richer runtime-evidence semantics.

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

1. What exact GitHub API operation binds jobs to a named workflow run attempt?
2. Does the provider need to preserve attempt identity on each `WorkflowJob`, or is endpoint-level binding plus existing run identity sufficient and testable?
3. What controlled rerun sequence would fail under the current `latest` behavior and pass under the corrected behavior?
4. Which downstream consumers depend only on coherent jobs and therefore need no semantic redesign?
5. What stronger claims remain intentionally unavailable after the fix?

The simplest credible correction should win. Do not add an attempt registry, workflow orchestration layer, log subsystem, or generalized CI identity framework merely to solve this defect.

## Proof target for this slice

A successful bounded result should establish:

```text
same frozen PR head
+ same workflow run ID
+ explicitly selected run attempt
+ jobs acquired from that exact attempt
```

with focused controlled tests that distinguish a stable single attempt from a rerun where `latest` would otherwise be capable of selecting different jobs.

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
