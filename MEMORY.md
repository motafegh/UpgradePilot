# UpgradePilot Current Memory

**Last updated:** 2026-07-22  
**Purpose:** Concise project-local continuation. Source, tests, commands, outputs,
artifacts, and the current environment remain the authority for actual behavior.

## Current responsibility

Manual end-to-end product and artifact-lifecycle simulation using the locally
governed [`product-simulation/`](product-simulation/) workspace.

Local control:

- [`product-simulation/AGENTS.md`](product-simulation/AGENTS.md);
- [`product-simulation/SIMULATION_GOVERNANCE_AND_PLAN.md`](product-simulation/SIMULATION_GOVERNANCE_AND_PLAN.md);
- [`product-simulation/RUNTIME_ARTIFACT_SPECIFICATION.md`](product-simulation/RUNTIME_ARTIFACT_SPECIFICATION.md);
- [`product-simulation/TRANSPARENT_BASELINE_SPECIFICATION.md`](product-simulation/TRANSPARENT_BASELINE_SPECIFICATION.md).

Current synthesis and next-case preparation:

- [`product-simulation/S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md`](product-simulation/S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md);
- [`product-simulation/S003_FAILING_CI_SCENARIO_REQUIREMENTS.md`](product-simulation/S003_FAILING_CI_SCENARIO_REQUIREMENTS.md).

The parent authorization remains
[`plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md`](plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md).

M2-S03 implementation remains paused. Do not resume implementation until further
prospective cases and synthesis support an explicit corrected responsibility.

## Governing artifact correction

Every scenario must preserve both:

```text
complete human-auditable CASE.md
+
manual runtime artifact bundle
```

The default bundle represents invocation, frozen identity, operations,
raw/reference evidence, claims/interpretations, findings, baseline, decision,
machine report, human report, follow-up, review, and ownership.

It is a controlling manual-simulation organization, not a frozen production
schema.

## S001 — complete retrospective reconstruction

Navigation:
[`product-simulation/scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/README.md`](product-simulation/scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/README.md)

Case: `pydantic/pydantic#13432`, Soup Sieve 2.6 → 2.8.4.

Run:

- run ID: `s001-retrofit-20260722-r1`;
- execution mode: retrospective artifact reconstruction;
- manifest inventory: 35 items;
- operation events: 22;
- evidence items: 26;
- claims/interpretations: 16;
- findings: 12;
- validation errors: 0;
- factual review: corrected;
- Ali final acceptance: pending;
- external confirmation: absent.

Outcome:

> Merge after normal maintainer review.

Material findings:

- Soup Sieve is transitive documentation tooling through the docs path, not a
  published Pydantic runtime dependency;
- target documentation uses Beautiful Soup through an MkDocs hook;
- Soup Sieve 2.8.4's Python floor is compatible with Pydantic's declared floor;
- Soup Sieve 2.6 is advisory-affected and 2.8.4 is patched;
- target exploitability remains unresolved and limited by bounded static evidence;
- proposed artifacts align with official package identities;
- exact-head docs CI exercised the owning path and passed;
- exact Dependabot trigger remains unresolved;
- credentialed post-merge publication evidence was unavailable;
- original July 9 advisory timing and strong trigger inference were corrected to
  June 1, 2026 and a plausible-but-unproven trigger.

Baseline `simulation-transparent-baseline-v0.1` also selected
`merge_after_normal_review`, but with weaker reasons, miscalibrated certainty,
and less actionable explanation.

## S002 — complete retrospective reconstruction

Navigation:
[`product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md`](product-simulation/scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md)

Case: `Aidan-Wallace/kubernetes-dashboard-token-api#20`, HTTPX 0.27.2 → 0.28.1.

Run:

- run ID: `s002-retrofit-2026-07-22-r1`;
- execution mode: retrospective artifact reconstruction;
- artifact inventory: 39 files;
- operation events: 10;
- evidence items: 20;
- claims/interpretations: 9;
- findings: 9;
- validation defects: 0;
- AI factual recheck: complete;
- Ali review: pending;
- external behavior confirmation: absent.

Outcome:

> Run targeted checks; merge only if exact-head resolver capture, Ruff, and pytest
> checks pass.

Material findings:

- HTTPX is directly declared, framework-mediated through FastAPI/Starlette
  `TestClient`, not directly observed in application source, and installed in the
  production image;
- HTTPX 0.28 removed the `app` Client argument;
- Starlette 0.36.3 passed it, while 0.37.2 removed it;
- a compatible FastAPI/Starlette line existed, but exact historical resolution is
  unavailable;
- Docker CI proved installation and image construction only;
- Python tests did not trigger because `requirements.txt` was excluded;
- historical job logs return HTTP 410;
- predecessor PR #17 was superseded by #20;
- eventual merge is historical action, not correctness proof.

Baseline `simulation-transparent-baseline-v0.1` also selected
`run_targeted_checks`, but did not identify the TestClient path, compatible
framework threshold, skipped relevant tests, exact checks, or state transitions.

## Completed cross-case artifact review

The two-case review concludes:

- the default top-level logical artifact family survived both cases;
- no universal responsibility should currently be removed or added;
- existing S001/S002 IDs and field names should not be cosmetically rewritten;
- representation drift must be controlled prospectively in S003;
- artifact and record counts are not quality metrics;
- both cases are retrofits and do not test natural progressive persistence;
- structured repeated-check execution and failure attribution remain untested;
- one decision outcome may be insufficient when dependency assessment and overall
  PR mergeability diverge.

Repeated stable candidates:

- exact case identity freeze;
- separate invocation and discovered identity;
- dependency path and multi-axis role;
- bounded raw preservation;
- CI trigger/command/responsibility/revision/environment authority;
- explicit missing, expired, inaccessible, and superseded states;
- separate operations, evidence, transformations, findings, decision, reports,
  follow-up, and review;
- structural validation;
- separate factual, Ali, external, and capability states.

Conditional responsibilities include advisory/exploitability analysis,
framework-adapter comparison, dynamic execution, private acquisition, post-merge
checks, platform/native analysis, and causal failure attribution.

## Thesis status

There are now two materialized comparative cases. Both belong to the same class:

```text
baseline broad action = full-investigation broad action
+
full investigation materially improves authority, calibration, explanation,
auditability, or actionability
```

This supports one thesis class but does not validate the overall thesis.
Still required:

- baseline wrong action;
- baseline sufficient with little added value;
- unresolved comparison;
- possible full-investigation overreach or excessive cost.

## S003 preparation

S003 is not yet selected.

Its primary responsibility is causal attribution of actual failing CI in a real
dependency-update PR.

The candidate must provide:

- exact base/head and dependency change identity;
- an actual failing decision-relevant check;
- accessible run/job/step/command/failure evidence;
- enough base/main/rerun/environment comparison to distinguish credible causes;
- genuine ambiguity among update-caused, pre-existing, flaky, environmental,
  unrelated, mixed, or unresolved explanations;
- a safe and bounded public investigation surface.

S003 must:

- create artifacts prospectively from the selected-and-frozen checkpoint;
- use a common envelope, lowercase ID convention, RFC 3339 UTC timestamps, and
  readable deterministic JSON;
- retain the default bundle;
- trial `CHECK_EXECUTIONS.jsonl` and `FAILURE_ATTRIBUTION.json`;
- run the transparent baseline before deep full-investigation comparison;
- preserve exact CI authority and comparability;
- test dependency-update assessment separately from overall PR action;
- preserve attribution alternatives and supersession;
- use one declared structural-validation profile;
- update cross-case synthesis after completion.

## Immediate continuation

1. Ali reviews
   [`product-simulation/S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md`](product-simulation/S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md).
2. Ali reviews
   [`product-simulation/S003_FAILING_CI_SCENARIO_REQUIREMENTS.md`](product-simulation/S003_FAILING_CI_SCENARIO_REQUIREMENTS.md).
3. Correct only a real local-model defect identified during review.
4. Select one qualifying S003 candidate.
5. Freeze S003 identity and baseline before deep investigation.
6. Execute S003 prospectively with natural durable checkpoints.
7. Keep M2-S03 paused.

## Ownership and assistance

- Ali identified that narrative-only cases did not model the complete runtime
  artifact lifecycle.
- Ali required the S001/S002 retrofits and requested the cross-case synthesis and
  S003 preparation.
- Technical acquisition, artifact construction, comparison, and writing remain
  substantially AI-controlled under Ali's direction.
- Ali acceptance of the cross-case synthesis and S003 requirements is pending.
- Independent Ali capability is not inferred from project ownership or artifact
  completion.

## Career boundary

Do not update Career for this ordinary project correction. Ali explicitly
initiates a Career review when durable capability, workload, or program state
should change.
