# UpgradePilot Current Memory

**Last updated:** 2026-09-11  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** implement the bounded GitHub Actions run/job attempt-coherence correction before using richer CI execution evidence as an upstream prerequisite for targeted-check synthesis.
- **Mode:** Build/Implement + Learning-by-Doing; A-phase design is complete and B is current.
- **Selected parent plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Supporting historical investigation owner:** `plans/SYSTEM_LIMITATIONS_AND_CORRECTNESS_INVESTIGATION_PLAN.md`.
- **Active working memory:** `working-memory/2026-09-11_ci-run-job-attempt-coherence-enhancement.md`.
- **Previous working memory:** `working-memory/2026-09-11_targeted-check-action-admission.md`.
- **Repository route:** continue directly on `main` unless Ali later requests otherwise.
- **Framework status:** ordinary-Python / LangGraph / LangChain comparison remains closed; no framework re-entry is justified.

## Synthesis state retained

The first deterministic maintainer-action evaluator is implemented and locally proven at its admitted boundary:

```text
PublicPullRequestInvestigation
→ synthesize_maintainer_action(...)
→ MaintainerActionSynthesis(action="abstain")
```

Established proof on Ali's project environment:

- focused synthesis tests: `2`, `OK`;
- full repository unit suite at that checkpoint: `530`, `OK`;
- manual runtime inspection produced structured explained abstention and preserved source-investigation identity.

No non-abstention action, CLI/application integration, complete report projection, persistence, or objective-safety claim is implemented.

## Targeted-check synthesis — paused on upstream evidence reliability

`run targeted checks` still requires, together:

```text
exact decision-critical unresolved proposition(s)
+ bounded discriminating maintainer check(s)
+ outcome interpretation / stopping logic
+ no justified UpgradePilot-executable equivalent investigation first
+ no broader adaptive inquiry needed instead
+ no independently established block condition
```

The targeted-check A-phase found that artifact serviceability preserves exact wheel-compatibility uncertainty and deterministic reevaluation semantics, but it does not yet establish a producer-grounded maintainer-outsource contract. Before outsourcing the work, UpgradePilot should first determine whether trustworthy read-only CI execution evidence can resolve part of the proposition itself.

That route depends on trustworthy CI attempt identity, so targeted-check synthesis B remains deliberately unstarted while the bounded CI correction below is completed.

## Current CI attempt-coherence responsibility

The September 8 correctness work **confirmed** a defect, not merely a hypothesis:

```text
captured WorkflowRun from attempt N
+
job acquisition using filter="latest"
→ can return jobs from later attempt N+1
while run_id and head_sha still match
```

This can mix observations from different attempts and change downstream CI classification.

Current source already preserves `WorkflowRun.run_attempt`. Authoritative GitHub REST semantics provide a specific-attempt jobs endpoint:

```text
GET /repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/jobs
```

### Accepted A-phase implementation decision

**Selected Option 1:** bind job acquisition to the captured `WorkflowRun.run_attempt` at the provider boundary, preserve the existing `(run, jobs)` composition, and retain existing run-ID/head-SHA checks.

**Rejected for now Option 2:** do not add `run_attempt` to every `WorkflowJob`. No current admitted independent consumer needs a standalone job to re-establish attempt identity, so duplicate metadata/validation is not justified under Core `JUST-003` through `JUST-005`.

Reconsider job-level attempt metadata only if a real future consumer or persistence/serialization boundary needs it independently from the owning run.

The bounded invariant is:

```text
frozen PR head SHA
+ exact workflow run ID
+ exact run attempt
+ jobs acquired from that same attempt
→ coherent factual CI execution evidence
```

This correction does **not** establish runtime step correlation, dependency installation/exercise, wheel compatibility, complete CI coverage, safety, or any maintainer action.

## Relevant remaining trust restrictions

Separate established reliability concerns remain:

1. requirements/constraints patch-to-frozen-head correspondence is not established;
2. static command recognition can produce false-positive direct-requirements evidence from unsupported shell text;
3. workflow run/job attempt coherence is the **current bounded repair**.

Repairing item 3 does not repair items 1 or 2.

## Immediate continuation — canonical LbD cycle

```text
A — DONE:
    confirmed historical mixed-attempt defect; verified specific-attempt GitHub jobs API;
    traced provider/consumer ownership; selected provider-bound exact-attempt acquisition;
    rejected duplicate WorkflowJob.run_attempt until a real consumer requires it.

B — CURRENT:
    change GitHubActionsClient job acquisition to
    /runs/{run_id}/attempts/{run_attempt}/jobs;
    remove filter="latest"; preserve run/head checks and current job type;
    add focused attempt-1/attempt-2/pagination regression proof;
    run nearest deterministic regressions.

C — NOT STARTED:
    preserve exact source/test changes, executed proof, surprises and proof limits.

D — NOT STARTED:
    learn from actual provider → typed run/jobs → CI-consumer flow and verify ownership
    of what attempt coherence now proves and what remains unproven.

E — NOT STARTED:
    repair any gap, then decide whether a separate read-only CI execution/wheel-witness
    slice is justified or whether to return directly to targeted-check synthesis.
```

Do not parse job logs, add wheel-serviceability semantics, reconstruct target environments, enable `run targeted checks`, or redesign CLI/reporting during this slice.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-build-implement`
