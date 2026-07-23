# S005 Action-Change or Dependency/PR-Divergence Requirements

**Status:** Fulfilled and retained as historical execution requirements  
**Date:** 2026-07-23  
**Selected case:** [`S005`](scenarios/S005-modelarrayio-pytest-9.0.3-to-9.1.1/README.md)  
**Result synthesis:** [`S005_POST_CASE_SYNTHESIS.md`](S005_POST_CASE_SYNTHESIS.md)  
**D1 synthesis:** [`D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md)

## Original purpose

S005 had to test a contrast not covered by S001–S004:

1. full evidence changes the transparent baseline's broad action; or
2. dependency assessment and current PR action genuinely diverge.

The case could not be selected or interpreted merely to manufacture either result.

## Fulfilled result

`PennLINC/ModelArrayIO#85`, pytest 9.0.3 → 9.1.1, satisfied the first class.

```text
baseline: run_targeted_checks
full decision: merge_after_normal_review
classification: baseline_wrong_action
```

The action changed because:

- exact pytest 9.1.1 identity was tied through `uv.lock` and `uv-venv-lock-runner` to the successful matrix;
- exact-head latest jobs passed on Python 3.11–3.14;
- the official breaking behavior required `--doctest-modules`, absent from the target;
- listed deprecated APIs/patterns were absent or used in supported form;
- no useful target-specific check remained.

## Admission requirements satisfied

- exact repository, PR, base, head, dependency, and changed-file identity;
- retained workflow/run/job/command/revision/result evidence;
- baseline frozen before final findings and decision;
- material target evidence hidden from the baseline;
- bounded public-safe investigation;
- explicit stop and new-run rules;
- prospective checkpoint history;
- structural validation with degraded method state preserved.

## Candidate rejection lessons retained

- PR closure without a public cause cannot establish dependency/PR divergence.
- Green CI is non-authoritative when the changed dependency identity does not reach the executed environment.
- A workflow may run tox while resolving a broad pytest constraint rather than the proposal.
- A workflow may ignore the changed requirements file and hard-code the old version.
- Overall color without exact-head command authority is insufficient.

The detailed screening record is [`S005_CANDIDATE_SCREENING.md`](S005_CANDIDATE_SCREENING.md).

## Conditional artifact result

- `CHECK_EXECUTIONS.jsonl`: activated naturally and became a repeated conditional stable candidate after S003/S005.
- `FAILURE_ATTRIBUTION.json`: inactive because no failure or competing cause existed.
- separate dependency/PR dimensions: inactive because both assessments supported normal review.
- dedicated stopping artifact: inactive because cost/overreach was not the primary question.

## Completion state

S005 is complete with:

- candidate screening;
- prospective identity and baseline freeze;
- exact dependency/CI authority;
- upstream-to-target mapping;
- action-changing findings;
- machine and human reports;
- follow-up and new-run transitions;
- review and ownership state;
- degraded structural validation;
- post-case and D1 synthesis.

No target repository was mutated. Ali review remains pending. AI-produced completion does not establish Ali-owned capability.

## Route consequence

These requirements no longer control active case execution. Current control is:

1. [`D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md);
2. [`../plans/UPGRADEPILOT_90_DAY_PLAN.md`](../plans/UPGRADEPILOT_90_DAY_PLAN.md);
3. [`../plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md`](../plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md).

Implementation remains paused until Ali accepts/corrects D1 synthesis and B1 freezes the minimum credible executable responsibility.