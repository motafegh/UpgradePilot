# UpgradePilot Current Memory

**Last updated:** 2026-07-23  
**Purpose:** Concise project-local continuation. Source, tests, commands, outputs,
artifacts, and the actual environment remain the authority for behavior.

## Current route

The controlling route is
[`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md), the
evidence-derived learning and building plan.

Historical M0–M8 and M2-S03 routes are superseded. Implementation remains paused.

The stable mission is unchanged: UpgradePilot remains a Python implementation for
maintainers of public Python repositories receiving Dependabot pull requests.
Cross-ecosystem simulation evidence does not broaden the supported core.

## Completed discovery evidence

- **S001:** retrospective Python transitive documentation/advisory case; relevant
  green CI; outcome `merge_after_normal_review`.
- **S002:** retrospective Python direct/adapter case; relevant tests skipped and logs
  expired; outcome `run_targeted_checks`.
- **S003:** prospective transfer case; failing `npm ci`, peer conflict, comparison,
  and causal attribution; current proposal blocked as-is.
- **S004:** prospective Python baseline-sufficient control; pytest `9.0.2` → `9.0.3`;
  exact relevant ordinary and regression CI passed; outcome
  `merge_after_normal_review`; investigation stopped before inactive conditional
  stages.

Baseline/full classes:

```text
S001–S003: same broad action, materially stronger support
S004: baseline sufficient, no material added decision value
```

This is contrasting evidence, not representative validation.

## S004 closure

Navigation:

- [`product-simulation/scenarios/S004-glyphslib-pytest-9.0.2-to-9.0.3/README.md`](product-simulation/scenarios/S004-glyphslib-pytest-9.0.2-to-9.0.3/README.md)
- [`product-simulation/S004_POST_CASE_SYNTHESIS.md`](product-simulation/S004_POST_CASE_SYNTHESIS.md)

Run: `s004-20260722T224500Z-r1`.

Material result:

- one pinned pytest development dependency changed;
- tox installed the changed requirements file and invoked pytest;
- exact-head ordinary tests passed on Python 3.10/3.14 and Ubuntu/Windows;
- exact-head regression tests reinstalled the proposed requirements and passed;
- official upstream material called 9.0.3 a drop-in bug-fix release;
- all precommitted stop conditions passed;
- no targeted check, dynamic reproduction, failure attribution, adapter analysis,
  exploitability analysis, or platform analysis was activated;
- structural validation returned zero errors through a connector-backed offline
  fallback after fresh clone failed because the local environment could not resolve
  GitHub;
- AI factual review complete; Ali review pending;
- no target mutation and no Ali-owned capability conclusion.

`STOPPING_EVALUATION.json` is now a conditional stable candidate for cases where
sufficiency, stage activation, overreach, or investigation cost is material.

## Current stage

**D1 — Contrast closure; S004 complete, S005 remaining**

Local execution is governed by:

- [`product-simulation/AGENTS.md`](product-simulation/AGENTS.md);
- [`product-simulation/SIMULATION_GOVERNANCE_AND_PLAN.md`](product-simulation/SIMULATION_GOVERNANCE_AND_PLAN.md);
- [`product-simulation/RUNTIME_ARTIFACT_SPECIFICATION.md`](product-simulation/RUNTIME_ARTIFACT_SPECIFICATION.md);
- [`product-simulation/TRANSPARENT_BASELINE_SPECIFICATION.md`](product-simulation/TRANSPARENT_BASELINE_SPECIFICATION.md);
- [`product-simulation/SCENARIO_COVERAGE.md`](product-simulation/SCENARIO_COVERAGE.md);
- [`product-simulation/S004_POST_CASE_SYNTHESIS.md`](product-simulation/S004_POST_CASE_SYNTHESIS.md);
- [`product-simulation/S005_ACTION_CHANGE_OR_DIVERGENCE_REQUIREMENTS.md`](product-simulation/S005_ACTION_CHANGE_OR_DIVERGENCE_REQUIREMENTS.md).

## Immediate continuation

1. Screen public Python Dependabot candidates for **S005**.
2. Prefer a case where:
   - full evidence changes the transparent baseline's broad action; or
   - dependency assessment and current PR action genuinely diverge.
3. Freeze S005 identity and baseline prospectively.
4. Execute the case without forcing a preferred classification.
5. Perform focused S001–S005 synthesis.
6. Decide whether D1 passes and B1 may freeze the minimum credible runtime
   responsibility.
7. Create a bounded B2 implementation plan only after B1 acceptance.

Do not:

- repeat or reopen S004 without new boundary evidence;
- resume M2-S03;
- require a fixed case count;
- select database, service, model, agent, queue, graph, or deployment architecture
  before its evidence gate;
- infer Ali-owned capability from AI-generated cases, plans, or validation.

## Ownership state

Ali identified the narrative-only simulation defect, required complete runtime
artifacts, authorized S001–S004, and authorized route correction.

Technical execution, synthesis, and route updates remain substantially AI-controlled.
Ali review and future ownership-bearing implementation work remain required before
capability claims.
