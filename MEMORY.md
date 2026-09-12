# UpgradePilot Current Memory

**Last updated:** 2026-09-12  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** E-phase analysis for the CI evidence path: determine whether the already-acquired runtime step summaries can support trustworthy static→runtime dependency-step correlation or whether a separate bounded job-log evidence slice is required before returning to targeted-check synthesis.
- **Mode:** Learning-by-Doing analysis/design after completed CI attempt-coherence Build proof; A/B/C/D are complete and E is current.
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

The prerequisite CI attempt-identity defect has now been repaired and deterministically proven. Targeted-check synthesis B remains deliberately unstarted until E decides whether stronger read-only runtime evidence is justified.

## CI run/job attempt coherence — implementation and proof complete

The previous provider path could mix a captured run from one attempt with `latest` jobs from a later rerun while `run_id` and `head_sha` still matched.

The accepted correction binds job acquisition to the captured `WorkflowRun.run_attempt`:

```text
frozen PR head SHA
+ exact workflow run ID
+ exact run attempt
+ jobs acquired from that same attempt
→ coherent factual CI execution evidence
```

`GitHubActionsClient.get_workflow_jobs(...)` now requests:

```text
/repos/{repository}/actions/runs/{run_id}/attempts/{run_attempt}/jobs
```

and no longer uses `filter="latest"`.

Implementation commits:

```text
2cd930afee6127d9f3bfd2fb4492e16f9ec85261  fix: bind workflow jobs to captured run attempt
e01785e7364e015365d9a676792e0f70e9431a17  test: prove workflow job attempt binding
```

Validation on Ali's WSL environment:

```text
focused provider tests      9  OK
nearest CI/application     31  OK
full deterministic suite  533  OK
```

The attempt-coherence Build proof is closed at the deterministic repository-test boundary.

## D ownership result retained

The current mental model is:

```text
run_id
→ identifies the workflow run

run_attempt
→ identifies the particular execution/rerun of that run

(run_id, run_attempt)
→ identifies the exact execution whose jobs are being interpreted
```

This is a provenance/identity correction only. It does not establish what dependency-related commands executed inside the job.

The second important separation is:

```text
static workflow evidence
→ what the YAML declares

runtime Actions evidence
→ what GitHub reports about the executed run/job/step
```

Those evidence types must not be collapsed without an explicit correlation rule.

## E-phase current finding — runtime step data already exists

The provider already acquires optional runtime `WorkflowStep` summaries for each job. Each step preserves:

```text
number
name
status
conclusion
```

and provider tests protect this parsing.

However, `src/upgradepilot/ci/dependency_exercise.py` intentionally separates:

```text
successful exact-head runtime workflow/job authority
static changed-dependency consumption
static direct changed-package exercise
```

and explicitly states that the static dependency propositions are not correlated to runtime step execution. Its strongest current state is therefore:

```text
supported_not_correlated
```

The current evaluator does not use `WorkflowJob.steps` to prove that a statically identified install/exercise step actually executed. CI coverage tests can establish `supported_not_correlated` even when the supplied runtime job has `steps=()`.

Current capability boundary:

```text
exact coherent run/job attempt                    ✅
run/job runtime success                           ✅
runtime step summaries acquired                   ✅
static dependency consumption/exercise analysis   ✅
static step ↔ runtime step correlation             ❌
runtime proof dependency install executed          ❌
runtime proof exact version/wheel                  ❌
```

## Relevant remaining trust restrictions

Separate established reliability concerns remain:

1. requirements/constraints patch-to-frozen-head correspondence is not established;
2. static command recognition can produce false-positive direct-requirements evidence from unsupported shell text;
3. workflow run/job attempt coherence is repaired and focused/nearest/broader deterministically proven;
4. static dependency declarations are still not correlated to runtime step execution.

## Immediate continuation — canonical LbD cycle

```text
A — DONE:
    confirmed historical mixed-attempt defect and selected provider-bound exact-attempt
    acquisition.

B — DONE:
    implemented attempt-specific acquisition and regression protection.

C — DONE:
    preserved implementation, proof, rationale and non-proofs.

D — DONE:
    established ownership of run ID vs attempt identity, provider provenance, and the
    static-vs-runtime evidence distinction.

E — CURRENT:
    inspect the existing WorkflowStep runtime summaries and determine whether they can
    safely correlate a static dependency-related step to runtime execution; if not,
    determine whether bounded read-only job-log evidence is the next justified slice.
```

Do not parse job logs, add wheel-serviceability semantics, reconstruct target environments, enable `run targeted checks`, or redesign CLI/reporting until E explicitly selects the next responsibility.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-build-implement`
