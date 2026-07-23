# UpgradePilot Current Memory

**Last updated:** 2026-07-23  
**Purpose:** Concise project-local continuation. Source, tests, commands, outputs, artifacts, and the actual environment remain the authority for behavior.

## Current route

The controlling route is [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md).

Historical M0–M8 and M2-S03 routes are superseded. The stable core remains a Python implementation for maintainers of public Python repositories receiving Dependabot PRs.

Implementation remains paused.

## Completed discovery evidence

- **S001:** transitive docs/advisory case; relevant green CI; `merge_after_normal_review`.
- **S002:** direct/adapter case; relevant tests skipped; `run_targeted_checks`.
- **S003:** failing install and peer conflict; update-caused attribution; block current proposal as-is.
- **S004:** exact relevant green control; baseline sufficient; `merge_after_normal_review`; early stop.
- **S005:** ModelArrayIO pytest 9.0.3 → 9.1.1; exact lock-backed matrix; upstream caution outside target path; baseline `run_targeted_checks` changed to full `merge_after_normal_review`.

Comparative classes:

```text
S001–S003: same broad action, materially stronger support
S004: baseline sufficient
S005: baseline wrong action
```

This is sufficient technical contrast for B1 planning, not representative validation or safety proof.

## S005 closure

Navigation:

- [`product-simulation/scenarios/S005-modelarrayio-pytest-9.0.3-to-9.1.1/README.md`](product-simulation/scenarios/S005-modelarrayio-pytest-9.0.3-to-9.1.1/README.md)
- [`product-simulation/S005_POST_CASE_SYNTHESIS.md`](product-simulation/S005_POST_CASE_SYNTHESIS.md)
- [`product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md)

Run: `s005-20260723T123700Z-r1`.

Material result:

- PR #85 changed only pytest in `uv.lock`;
- latest tox environments consumed the lock through `uv-venv-lock-runner`;
- exact pytest 9.1.1 jobs passed on Python 3.11–3.14;
- the Python 3.12 job included downloaded-data tests;
- official pytest 9.1 breaking behavior required `--doctest-modules`, absent from the target;
- listed deprecated APIs/patterns were absent or used in supported form;
- all parametrization values were concrete Collections;
- no useful targeted check remained;
- `CHECK_EXECUTIONS.jsonl` activated; failure attribution and separate decision dimensions did not;
- degraded structural validation reported zero errors, but the retained validator was not executed from a clean clone because local GitHub DNS failed;
- AI factual review complete; Ali review pending;
- no target mutation or Ali-owned capability conclusion.

## Current stage

**D1 technical discovery complete; Ali acceptance review pending.**

Current controlling sources:

- [`product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md)
- [`product-simulation/SCENARIO_COVERAGE.md`](product-simulation/SCENARIO_COVERAGE.md)
- [`plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md`](plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md)
- [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)

## Immediate continuation

1. Review the D1 final synthesis with Ali.
2. Ali explains/challenges S004 stopping, S005 action change, CI dependency identity, target relevance, and universal versus conditional responsibilities.
3. Record acceptance, corrections, and deferred disagreements.
4. Activate B1 only after acceptance.
5. Inspect current source/tests and freeze the minimum credible executable responsibility.
6. Create one bounded B2 implementation plan.
7. Begin the replay-to-decision kernel through learning by building.

Do not:

- select S006 without a named planning blocker;
- resume M2-S03;
- require a fixed case count;
- start B2 before B1 acceptance;
- select database, service, model, agent, queue, graph, or deployment architecture before its gate;
- infer Ali-owned capability from AI-generated cases or plans.

## Ownership state

Ali identified the narrative-only simulation defect, required complete runtime artifacts, and authorized S001–S005. Technical execution, validation profiles, synthesis, and route updates remain substantially AI-controlled. Ali review and ownership-bearing implementation remain required before capability claims.