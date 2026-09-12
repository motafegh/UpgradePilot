# UpgradePilot Current Memory

**Last updated:** 2026-09-12  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** A-phase Planning/Design for a bounded CI static↔runtime correlation bridge: determine the smallest sound contract that can correlate existing exact-workflow static evidence with existing exact-attempt runtime job/step evidence before any stronger dependency-execution claim is admitted.
- **Mode:** Learning-by-Doing + Planning/Design. The previous CI run/job attempt-coherence cycle is fully closed A→E; the new correlation-bridge cycle has A current and B/C/D/E not started.
- **Selected parent plan:** `plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`.
- **Active working memory:** `working-memory/2026-09-12_ci-static-runtime-correlation-bridge.md`.
- **Previous working memory:** `working-memory/2026-09-11_ci-run-job-attempt-coherence-enhancement.md`.
- **Repository route:** continue directly on `main` unless Ali later requests otherwise.
- **Framework status:** ordinary-Python / LangGraph / LangChain comparison remains closed; no framework re-entry is justified.

## Maintainer-action synthesis state retained

The first deterministic maintainer-action evaluator remains implemented at its admitted abstention-only boundary:

```text
PublicPullRequestInvestigation
→ synthesize_maintainer_action(...)
→ MaintainerActionSynthesis(action="abstain")
```

Established proof at that checkpoint:

```text
focused synthesis tests   2  OK
full repository suite   530  OK
```

No non-abstention action, CLI/application integration, complete report projection, persistence, or objective-safety claim is implemented.

`run targeted checks` remains paused. Its admission still requires:

```text
exact decision-critical unresolved proposition(s)
+ bounded discriminating maintainer check(s)
+ outcome interpretation / stopping logic
+ no justified UpgradePilot-executable equivalent investigation first
+ no broader adaptive inquiry needed instead
+ no independently established block condition
```

The current upstream CI work exists because UpgradePilot should first determine whether trustworthy read-only execution evidence can resolve part of the wheel/serviceability uncertainty itself before outsourcing a check to the maintainer.

## CI run/job attempt coherence — cycle closed

The historical defect allowed a captured workflow run from one rerun attempt to be paired with `latest` jobs from another attempt while `run_id` and `head_sha` still matched.

Implemented correction:

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

The previous Learning-by-Doing cycle is formally CLOSED with A/B/C/D/E complete. Detailed closure is preserved in `working-memory/2026-09-11_ci-run-job-attempt-coherence-enhancement.md`.

## New selected responsibility — static↔runtime correlation bridge

E from the previous cycle established that UpgradePilot already has two distinct evidence layers:

```text
STATIC WORKFLOW EVIDENCE
→ exact PR-head workflow definition
→ static jobs / strategy / ordered steps / commands / conditions

RUNTIME ACTIONS EVIDENCE
→ exact workflow run + attempt
→ runtime jobs
→ runtime step summaries / status / conclusion
```

`src/upgradepilot/ci/dependency_exercise.py` deliberately does not correlate them. Its strongest current combined state is still:

```text
supported_not_correlated
```

The next responsibility is an explicit third layer:

```text
STATIC EVIDENCE
        +
RUNTIME EVIDENCE
        ↓
CORRELATION EVIDENCE
        ↓
DEPENDENCY-CI INTERPRETATION
```

Do not collapse static declarations, runtime observations, and correlation conclusions into one undifferentiated authority-bearing layer.

### Existing data available to A

Static workflow representation already preserves, where admitted:

```text
static jobs.<job_id>
job name
strategy/matrix structure
job source order
step source order
step name
run command
condition / continue-on-error / working-directory
```

Runtime Actions representation already preserves:

```text
WorkflowRun:
  run_id / workflow_id / head_sha / run_attempt / status / conclusion

WorkflowJob:
  job_id / run_id / name / head_sha / status / conclusion / optional steps

WorkflowStep:
  number / name / status / conclusion
```

### Important A constraints already established

- job correlation must be solved before step correlation;
- display name alone is not a universal identity key;
- runtime step number cannot simply equal static source index because GitHub inserts execution steps;
- a static step `id` would not by itself solve the problem because current runtime step summaries do not expose the YAML step ID;
- one static matrix job can expand to multiple runtime jobs;
- reusable workflows and ambiguous/dynamic/duplicate-name shapes must remain unresolved unless separately supported;
- job logs are not selected yet. Existing step-summary evidence must be exhausted first.

## Current A-phase question

Determine, from current source/tests and authoritative GitHub behavior, the smallest positive correlation contract and its explicit unresolved cases.

A must establish:

```text
positive job-correlation conditions
→ then positive step-correlation conditions
→ explicit unresolved/ambiguous states
→ correct owner/layer
→ exact claim earned by successful correlation
→ later Build proof strategy
→ stronger claims/non-goals still excluded
```

The current design baseline favors a CI-domain correlation evidence type while keeping GitHub provider objects factual-only, but that is not yet treated as an accepted implementation decision until A finishes the ownership/design trace.

## Relevant trust restrictions

Separate reliability limits remain:

1. requirements/constraints patch-to-frozen-head correspondence is not established;
2. static command recognition can produce false-positive direct-requirements evidence from unsupported shell text;
3. run/job attempt coherence is repaired and deterministically proven;
4. static dependency declarations are not yet correlated to runtime step execution.

A successful correlation bridge would address only item 4 at its admitted boundary. It would not automatically repair items 1 or 2 or prove exact version/wheel installation.

## Immediate continuation — new canonical LbD cycle

```text
Slice: CI static↔runtime correlation bridge

A — CURRENT:
    determine the smallest sound correlation contract, owner/layer, unresolved cases,
    exact earned claim, and later proof strategy from existing static/runtime evidence.

B — NOT STARTED:
    no source/test implementation until A resolves the material design questions.

C — NOT STARTED
D — NOT STARTED
E — NOT STARTED
```

Do not yet parse job logs, add wheel-serviceability semantics, reconstruct target environments, enable `run targeted checks`, change maintainer-action synthesis, or redesign CLI/reporting.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-planning-design`
