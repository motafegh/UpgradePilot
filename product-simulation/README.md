# UpgradePilot Product Simulation Workspace

**Status:** D1 technical discovery complete; Ali acceptance review pending  
**Local authority:** [`AGENTS.md`](AGENTS.md)  
**Controlling plan:** [`SIMULATION_GOVERNANCE_AND_PLAN.md`](SIMULATION_GOVERNANCE_AND_PLAN.md)  
**Project route:** [`../plans/UPGRADEPILOT_90_DAY_PLAN.md`](../plans/UPGRADEPILOT_90_DAY_PLAN.md)  
**Current synthesis:** [`D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md)  
**Learning companion:** [`../learning/product-simulation/`](../learning/product-simulation/)

## Purpose

This workspace manually performed the intended UpgradePilot runtime on materially different real dependency-update cases before B1 freezes the first implementation responsibility.

It discovered:

- product behavior: acquisition, investigation, action, abstention, stopping, and follow-up;
- artifact behavior: invocation, identity, operations, evidence, transformations, findings, baseline, decision, reports, transitions, review, and validation;
- conditional behavior: when advisory, compatibility, repeated execution, attribution, or stopping work activates;
- automation boundaries: deterministic state, tool-assisted interpretation, and human authority.

Simulation artifacts are discovery evidence, not final production schemas or proof of automation.

## Current controlling and synthesis files

- [`AGENTS.md`](AGENTS.md)
- [`SIMULATION_GOVERNANCE_AND_PLAN.md`](SIMULATION_GOVERNANCE_AND_PLAN.md)
- [`RUNTIME_ARTIFACT_SPECIFICATION.md`](RUNTIME_ARTIFACT_SPECIFICATION.md)
- [`TRANSPARENT_BASELINE_SPECIFICATION.md`](TRANSPARENT_BASELINE_SPECIFICATION.md)
- [`SCENARIO_COVERAGE.md`](SCENARIO_COVERAGE.md)
- [`S003_POST_CASE_SYNTHESIS.md`](S003_POST_CASE_SYNTHESIS.md)
- [`S004_POST_CASE_SYNTHESIS.md`](S004_POST_CASE_SYNTHESIS.md)
- [`S005_POST_CASE_SYNTHESIS.md`](S005_POST_CASE_SYNTHESIS.md)
- [`D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md)

## Runtime responsibilities discovered

```text
real event and invocation
→ exact identity freeze
→ material operations
→ raw/reference evidence
→ evidence records and states
→ claims and interpretations
→ findings and uncertainty
→ transparent baseline
→ bounded decision or abstention
→ machine and human reports
→ follow-up, rerun, supersession, and changed-boundary transitions
→ review, ownership, conditional-stage state, and validation
```

Exact files and fields remain illustrative.

Conditional artifacts demonstrated:

- `CHECK_EXECUTIONS.jsonl` — S003 and S005;
- `FAILURE_ATTRIBUTION.json` — S003;
- `STOPPING_EVALUATION.json` — S004.

## Completed cases

| Scenario | Main contrast | Full action | Baseline relationship |
|---|---|---|---|
| [`S001`](scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/README.md) | transitive docs/advisory path; relevant green CI | merge after normal review | same action; stronger authority/calibration |
| [`S002`](scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md) | adapter path; relevant tests skipped | run targeted checks | same action; exact missing authority/checks |
| [`S003`](scenarios/S003-event-handler-loader-typescript-5.9.3-to-7.0.2/README.md) | failing install; peer conflict; causal comparison | block current proposal as-is | same broad action; cause/recovery added |
| [`S004`](scenarios/S004-glyphslib-pytest-9.0.2-to-9.0.3/README.md) | exact relevant green control; early stop | merge after normal review | baseline sufficient |
| [`S005`](scenarios/S005-modelarrayio-pytest-9.0.3-to-9.1.1/README.md) | exact lock-backed matrix; scoped caution | merge after normal review | baseline wrong action |

All remain AI-controlled evidence with Ali review pending.

## D1 result

Technical discovery is sufficient to state the minimum credible runtime responsibility. The future core must preserve exact identity, evidence states and lineage, a transparent baseline, conditional-stage activation, bounded decisions, both reports, transitions, review state, and validation.

It must not make every conditional investigation universal.

## Current action

Implementation remains paused.

1. Ali reviews [`D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md).
2. Record acceptance, corrections, and deferred disagreements.
3. Activate B1 through [`../plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md`](../plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md).
4. Inspect current source/tests and freeze the first executable responsibility.
5. Create one bounded B2 implementation plan only after B1 acceptance.

Do not resume M2-S03 or add another simulation case without a named planning uncertainty.

No target repository was mutated during S001–S005. Independent Ali capability is not inferred from AI-controlled execution.