# CI Run/Job Attempt-Coherence Enhancement — Working Memory

**Date:** 2026-09-11  
**Session status:** CLOSED  
**Primary mode:** Build/Implement + Learning-by-Doing  
**Parent selected plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Supporting historical investigation owner:** [`../plans/SYSTEM_LIMITATIONS_AND_CORRECTNESS_INVESTIGATION_PLAN.md`](../plans/SYSTEM_LIMITATIONS_AND_CORRECTNESS_INVESTIGATION_PLAN.md)  
**Previous:** [`2026-09-11_targeted-check-action-admission.md`](2026-09-11_targeted-check-action-admission.md)  
**Continued by:** [`2026-09-12_ci-static-runtime-correlation-bridge.md`](2026-09-12_ci-static-runtime-correlation-bridge.md)

## Session anchor

The targeted-check maintainer-action A-phase exposed an upstream evidence-reliability dependency rather than a synthesis rule to invent downstream. Exact artifact/wheel serviceability may later benefit from trustworthy exact-CI execution evidence, but the prior GitHub Actions acquisition path could combine a captured `WorkflowRun` from one attempt with `latest` jobs from a later rerun.

The admitted re-entry was:

```text
maintainer-action synthesis
→ may need stronger producer-grounded CI execution evidence
→ stronger CI evidence first needs coherent run/job attempt identity
→ repair CI acquisition identity before richer CI evidence work
```

## Confirmed historical defect

The September 8 correctness investigation had already reproduced this failure shape against the actual Actions parsing and CI evaluator:

```text
captured run attempt 1 / success
+
latest jobs from attempt 2
→ accepted as one evidence pair
because run_id and head_sha still match
```

This established an acquisition/normalization consistency defect. It did not establish runtime dependency exercise, wheel compatibility, public-case frequency, or a maintainer recommendation.

## Exact responsibility and accepted design

The bounded responsibility was to guarantee that a workflow run and the jobs interpreted with it belong to the same workflow-run attempt while retaining exact PR-head and run-ID identity checks.

Required invariant:

```text
frozen PR head SHA
+ exact workflow run ID
+ exact workflow run attempt
+ jobs acquired for that same attempt
→ coherent factual CI execution evidence
```

Current source entering the slice already preserved `WorkflowRun.run_attempt`; the defect was that `get_workflow_jobs(...)` used the run-level jobs endpoint with `filter="latest"`.

### Selected — provider-bound exact-attempt acquisition

```text
WorkflowRun(run_id, head_sha, run_attempt)
→ request /runs/{run_id}/attempts/{run_attempt}/jobs
→ retain existing job run_id/head_sha validation
→ preserve existing (run, jobs) pair
→ CI consumer
```

The provider is the earliest sufficient owner of acquisition identity, and the exact-attempt request itself establishes which attempt supplied the jobs.

### Rejected for now — duplicate `run_attempt` on every `WorkflowJob`

No admitted independent consumer, persistence boundary, or serialization boundary requires each job to carry duplicate attempt metadata. Reconsider only if a future consumer must interpret a `WorkflowJob` independently from its owning `WorkflowRun`.

## B-phase implementation and proof

Implemented on `main`:

- `src/upgradepilot/github/actions.py`
  - `get_workflow_jobs(...)` now requests `/actions/runs/{run_id}/attempts/{run_attempt}/jobs`;
  - `filter="latest"` was removed;
  - existing run-ID/head-SHA validation, pagination, job representation, and step-summary parsing remain.
- `tests/test_github_actions.py`
  - protects attempt-1 and attempt-2 request coordinates;
  - protects multi-page acquisition on one fixed attempt;
  - protects removal of `filter`;
  - retains wrong-run and wrong-head rejection plus step parsing.

Implementation commits:

```text
2cd930afee6127d9f3bfd2fb4492e16f9ec85261  fix: bind workflow jobs to captured run attempt
e01785e7364e015365d9a676792e0f70e9431a17  test: prove workflow job attempt binding
```

Validation on Ali's WSL project environment:

```text
python -m unittest discover -s tests -p 'test_github_actions.py' -v
→ 9 tests
→ OK

python -m unittest tests.test_ci_dependency_coverage tests.test_investigation -v
→ 31 tests
→ OK

python -m unittest discover -s tests -v
→ 533 tests
→ OK
```

The bounded Build proof is therefore closed at the deterministic repository-test boundary.

## D-phase ownership result

The learned identity model is:

```text
run_id
→ identifies the workflow run lineage/resource

run_attempt
→ identifies which execution/rerun of that run

(run_id, run_attempt)
→ selects the exact workflow execution whose jobs are interpreted
```

This is a provenance/identity correction, not a new CI semantic capability.

A second important distinction became explicit:

```text
static workflow evidence
→ what the exact YAML declares

runtime Actions evidence
→ what GitHub reports about the exact run/job/step execution
```

Those evidence sources must not be silently collapsed into a stronger execution claim.

## E-phase findings and closure

Inspection of the existing source showed that UpgradePilot already has both sides needed for a possible stronger CI evidence path:

### Static side

`upgradepilot.github.workflow_definition` and the CI composition path preserve bounded static workflow structure including:

- unique static job key;
- job display name when literal;
- strategy/matrix structure;
- ordered step source index;
- step display name when present;
- `run:` command;
- condition / `continue-on-error` / working-directory and related static structure.

### Runtime side

`upgradepilot.github.actions` already acquires optional `WorkflowStep` summaries for an exact-attempt `WorkflowJob`. Each runtime step currently preserves:

```text
number
name
status
conclusion
```

### Current semantic boundary

`src/upgradepilot/ci/dependency_exercise.py` intentionally separates:

```text
1. successful exact-head runtime workflow/job authority
2. static changed-dependency consumption
3. stronger static direct changed-package exercise
```

The strongest existing state remains:

```text
supported_not_correlated
```

because the static dependency propositions are not correlated to runtime step execution.

Current capability boundary at closure:

```text
exact coherent run/job attempt                    ✅
run/job runtime success                           ✅
runtime step summaries acquired                   ✅
static dependency consumption/exercise analysis   ✅
static job/step ↔ runtime job/step correlation     ❌
runtime proof dependency install executed          ❌
runtime proof exact installed version/wheel        ❌
```

### E architectural conclusion

Do **not** merge static and runtime evidence into one undifferentiated CI layer. Preserve three responsibilities:

```text
STATIC EVIDENCE
what the exact workflow definition declares

RUNTIME EVIDENCE
what GitHub reports for the exact execution

CORRELATION EVIDENCE
whether one static job/step can be soundly tied to one runtime job/step
```

The later dependency-CI interpreter may consume correlation evidence to make a stronger claim, but the bridge must not manufacture authority.

### Correlation facts established before closure

- runtime step `name` alone is not a universal identity key;
- runtime step `number` cannot simply equal static `source_index` because GitHub inserts setup/post/completion execution steps;
- static YAML step `id` can be unique within a job, but the current runtime job-step summaries do not expose that YAML `id`, so merely parsing it would not solve correlation;
- static job `jobs.<job_id>` is unique in the workflow definition, but the runtime job object exposes a runtime job ID and display name rather than a direct static-job-ID field;
- matrix expansion means one static job definition can legitimately produce multiple runtime jobs;
- reusable workflows, dynamic names/expressions, duplicate display names, conditional/skipped steps, matrix expansion, and other ambiguous shapes must remain unresolved unless separately supported;
- job logs are **not yet selected**. Existing step-summary evidence should be exhausted first; logs become justified only if the next A-phase establishes a concrete proposition that summaries cannot prove.

### Selected next responsibility

Open a new Learning-by-Doing cycle under Planning/Design to determine the **smallest sound static↔runtime correlation contract** that can be admitted from existing evidence.

The next cycle begins with job correlation before step correlation because a step cannot be soundly correlated until its owning static/runtime job relationship is known.

The intended baseline is conservative:

```text
correlated
unresolved / not safely correlatable
```

rather than guessing through ambiguous workflow shapes.

No source/test implementation, job-log parsing, wheel-serviceability semantics, target-environment reconstruction, or maintainer-action expansion is authorized by this closure.

## Learning-by-Doing closure

```text
Slice: CI run/job attempt coherence

A — DONE:
    confirmed the mixed-attempt defect, traced ownership, verified the exact-attempt API,
    and selected provider-bound exact-attempt acquisition.

B — DONE:
    implemented exact-attempt job acquisition and focused regression protection.

C — DONE:
    preserved source/test commits, executed proof, rationale, alternatives, and non-proofs.

D — DONE:
    established ownership of run ID vs attempt identity and static-vs-runtime evidence.

E — DONE:
    found the existing runtime-step layer, identified the missing correlation responsibility,
    selected a separate conservative correlation layer, rejected premature layer collapse/log
    parsing, and handed off to a fresh correlation-bridge A-phase.
```

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-planning-design`
