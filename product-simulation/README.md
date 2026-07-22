# UpgradePilot Product Simulation Workspace

**Status:** Active D1 complete-runtime and artifact-lifecycle discovery workspace  
**Local authority:** [`AGENTS.md`](AGENTS.md)  
**Controlling plan:** [`SIMULATION_GOVERNANCE_AND_PLAN.md`](SIMULATION_GOVERNANCE_AND_PLAN.md)  
**Project route:** [`../plans/UPGRADEPILOT_90_DAY_PLAN.md`](../plans/UPGRADEPILOT_90_DAY_PLAN.md)  
**Learning companion:** [`../learning/product-simulation/`](../learning/product-simulation/)

## Purpose

This workspace manually performs the intended UpgradePilot runtime on materially
different real dependency-update cases before B1 freezes the first implementation
responsibility.

It discovers:

1. **product behavior** — what must be acquired, investigated, concluded, reported,
   stopped, and requested from the maintainer;
2. **artifact behavior** — what invocation, identity, operation, evidence,
   transformation, finding, decision, report, follow-up, review, and replay state
   must be created and preserved;
3. **stopping behavior** — when a baseline needs deeper work and when confirming its
   authority is enough;
4. **automation boundaries** — which responsibilities appear deterministic,
   tool-assisted, model-dependent, or human-controlled.

A complete `CASE.md` is necessary but not sufficient by itself.

## Scope and non-admission

Inside `product-simulation/`, local rules control conflicting project-local process,
artifact, method, milestone, and completion rules.

Any lawful, safe, accessible, materially useful method may be used for discovery.
Simulation use does not:

- admit a permanent architecture or product dependency;
- establish automated capability;
- expand the charter's public-Python boundary;
- prove target-update safety;
- authorize target-repository mutation.

## Current controlling and synthesis files

- [`AGENTS.md`](AGENTS.md)
- [`SIMULATION_GOVERNANCE_AND_PLAN.md`](SIMULATION_GOVERNANCE_AND_PLAN.md)
- [`RUNTIME_ARTIFACT_SPECIFICATION.md`](RUNTIME_ARTIFACT_SPECIFICATION.md)
- [`TRANSPARENT_BASELINE_SPECIFICATION.md`](TRANSPARENT_BASELINE_SPECIFICATION.md)
- [`SCENARIO_EXECUTION_TEMPLATE.md`](SCENARIO_EXECUTION_TEMPLATE.md)
- [`SCENARIO_COVERAGE.md`](SCENARIO_COVERAGE.md)
- [`S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md`](S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md)
- [`S003_POST_CASE_SYNTHESIS.md`](S003_POST_CASE_SYNTHESIS.md)
- [`S004_POST_CASE_SYNTHESIS.md`](S004_POST_CASE_SYNTHESIS.md)
- [`S005_ACTION_CHANGE_OR_DIVERGENCE_REQUIREMENTS.md`](S005_ACTION_CHANGE_OR_DIVERGENCE_REQUIREMENTS.md)

## Default scenario responsibilities

```text
real event and invocation
→ exact identity freeze
→ material operations
→ raw/reference evidence
→ evidence records and states
→ claims and interpretations
→ findings and uncertainty
→ transparent baseline
→ bounded decision
→ machine and human reports
→ follow-up, rerun, and supersession
→ review, ownership, cost, stopping, and validation
```

Exact files and fields remain illustrative. Required logical responsibilities must
remain discoverable.

Conditional artifacts activate only when their responsibility is real:

- `CHECK_EXECUTIONS.jsonl` — repeated/comparable executions;
- `FAILURE_ATTRIBUTION.json` — competing causes of failing evidence;
- `STOPPING_EVALUATION.json` — sufficiency, stage activation, or investigation-cost
  questions.

None is universal merely because one case used it.

## Progressive execution

Every new case must preserve natural checkpoints:

```text
candidate screening
→ selected, frozen, and baseline executed
→ material evidence and live findings
→ decision and reports
→ validation, synthesis, and review state
```

S001 and S002 are retrospective reconstructions. S003 and S004 are prospective.

## Completed cases

| Scenario | Main contrast | Result | Baseline relationship | Review |
|---|---|---|---|---|
| [`S001`](scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/README.md) | Python transitive docs/advisory path; relevant green CI | Merge after normal review | Same action; stronger evidence and calibration | AI factual correction complete; Ali acceptance pending |
| [`S002`](scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md) | Python direct/adapter path; relevant tests skipped | Run targeted checks | Same action; exact relevance and checks added | AI recheck complete; Ali review pending |
| [`S003`](scenarios/S003-event-handler-loader-typescript-5.9.3-to-7.0.2/README.md) | Failing install; peer conflict; comparison and attribution | Block current proposal as-is | Same broad action; exact failure, cause, recovery and decision dimensions added | AI review complete; Ali review pending |
| [`S004`](scenarios/S004-glyphslib-pytest-9.0.2-to-9.0.3/README.md) | Python baseline-sufficient control; exact relevant green CI; early stopping | Merge after normal review | Baseline sufficient; full process added no material action/check/uncertainty value | AI review complete; Ali review pending; validation passed with method degradation |

Artifact and record counts describe preservation choices, not quality.

## S004 result

S004 confirmed a narrow operating principle:

> Verify the transparent baseline's authority-critical assumptions with the smallest
> sufficient evidence set, then stop when no remaining question can change the
> action, material uncertainty, required check, or product conclusion.

It did not establish “patch + green CI = merge.” The exact pytest pin had to be
mapped through the changed requirements file into ordinary and regression pytest
commands on the frozen head.

S004 deliberately left failure attribution, dynamic reproduction, adapter analysis,
advisory exploitability, platform analysis, and targeted checks inactive. Their
non-activation was a product result, not missing work.

## Thesis status after S004

| Comparative class | Evidence |
|---|---|
| Same action, materially stronger support | S001, S002, S003 |
| Baseline sufficient; no material added value | S004 |
| Baseline wrong action | Not covered |
| Dependency/PR action divergence | Not covered |
| Unresolved | Not covered |

The current evidence rejects the assumption that deeper investigation must always
win.

## Current D1 action

Implementation remains paused.

1. Screen and execute **S005** under
   [`S005_ACTION_CHANGE_OR_DIVERGENCE_REQUIREMENTS.md`](S005_ACTION_CHANGE_OR_DIVERGENCE_REQUIREMENTS.md).
2. Prefer a public Python Dependabot case where the baseline action changes or the
   dependency assessment diverges from current PR action.
3. Preserve an unresolved result rather than forcing the preferred class.
4. Perform focused S001–S005 synthesis.
5. Return to the project route for the B1 implementation-responsibility decision.

Do not resume M2-S03, continue to satisfy a fixed case count, or universalize a
conditional artifact.

No target repository was mutated during S001–S004. Independent Ali capability is
not inferred from AI-controlled execution.
