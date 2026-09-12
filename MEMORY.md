# UpgradePilot Current Memory

**Last updated:** 2026-09-12  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** complete D-phase ownership/learning closure for the bounded GitHub Actions run/job attempt-coherence correction before deciding the next upstream evidence slice for targeted-check synthesis.
- **Mode:** Learning-by-Doing ownership/review after completed Build proof; A/B/C are complete and D is current.
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

The prerequisite CI attempt-identity defect has now been repaired and deterministically proven. Targeted-check synthesis B remains deliberately unstarted until the current CI slice completes D/E and we decide whether a richer read-only CI execution/wheel-evidence slice is justified.

## CI run/job attempt coherence — implementation and proof complete

The September 8 correctness work confirmed that the previous provider path could mix a captured run from one attempt with `latest` jobs from a later rerun while `run_id` and `head_sha` still matched.

### Accepted implementation decision

**Selected Option 1:** bind job acquisition to the captured `WorkflowRun.run_attempt` at the provider boundary, preserve the existing `(run, jobs)` composition, and retain existing run-ID/head-SHA checks.

**Rejected for now Option 2:** do not add `run_attempt` to every `WorkflowJob`. No admitted independent consumer needs a standalone job to re-establish attempt identity. Reconsider only if a real persistence/serialization/alternate-consumer boundary later requires it.

The bounded invariant is:

```text
frozen PR head SHA
+ exact workflow run ID
+ exact run attempt
+ jobs acquired from that same attempt
→ coherent factual CI execution evidence
```

### Implemented behavior

`GitHubActionsClient.get_workflow_jobs(...)` now requests:

```text
/repos/{repository}/actions/runs/{run_id}/attempts/{run_attempt}/jobs
```

and no longer uses `filter="latest"`.

Existing `WorkflowJob` representation, run-ID validation, frozen-head validation, job pagination, and step parsing remain intact.

Implementation commits:

```text
2cd930afee6127d9f3bfd2fb4492e16f9ec85261  fix: bind workflow jobs to captured run attempt
e01785e7364e015365d9a676792e0f70e9431a17  test: prove workflow job attempt binding
```

### Validation established on Ali's WSL environment

Local `main` was synchronized through `e01785e7` before execution.

Focused provider proof:

```text
python -m unittest discover -s tests -p 'test_github_actions.py' -v
→ 9 tests
→ OK
```

Nearest CI/application regressions:

```text
python -m unittest tests.test_ci_dependency_coverage tests.test_investigation -v
→ 31 tests
→ OK
```

Broader deterministic regression:

```text
python -m unittest discover -s tests -v
→ 533 tests
→ OK
```

Therefore the bounded CI attempt-coherence Build proof is closed at the deterministic repository-test boundary.

This correction does **not** establish runtime step correlation, dependency installation/exercise, wheel compatibility, complete CI coverage, safety, or any maintainer action.

## Relevant remaining trust restrictions

Separate established reliability concerns remain:

1. requirements/constraints patch-to-frozen-head correspondence is not established;
2. static command recognition can produce false-positive direct-requirements evidence from unsupported shell text;
3. workflow run/job attempt coherence is now repaired and focused/nearest/broader deterministically proven.

Repairing item 3 does not repair items 1 or 2.

## Immediate continuation — canonical LbD cycle

```text
A — DONE:
    confirmed historical mixed-attempt defect; verified specific-attempt GitHub jobs API;
    traced provider/consumer ownership; selected provider-bound exact-attempt acquisition;
    rejected duplicate WorkflowJob.run_attempt until a real consumer requires it.

B — DONE:
    implemented attempt-specific acquisition and focused regression protection;
    9 focused provider tests, 31 nearest CI/application tests, and 533 full repository
    deterministic tests all pass on Ali's WSL environment.

C — DONE:
    exact source/test commits, commands/results, design rationale, proof strength and
    remaining non-proofs are preserved in the active working memory.

D — CURRENT:
    learn from the actual provider → WorkflowRun/run_attempt → exact-attempt jobs →
    existing CI-consumer flow; verify what identity coherence establishes and what it
    still cannot establish about runtime dependency/wheel behavior.

E — NOT STARTED:
    repair any understanding or implementation gap, then decide whether the next
    justified slice is richer read-only CI execution/wheel evidence or a direct return
    to targeted-check synthesis.
```

Do not parse job logs, add wheel-serviceability semantics, reconstruct target environments, enable `run targeted checks`, or redesign CLI/reporting until D/E closes and the next responsibility is explicitly selected.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-build-implement`
