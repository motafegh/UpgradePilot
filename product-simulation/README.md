# UpgradePilot Product Simulation Workspace

**Local authority:** [`AGENTS.md`](AGENTS.md)  
**Workspace governance:** [`SIMULATION_GOVERNANCE_AND_PLAN.md`](SIMULATION_GOVERNANCE_AND_PLAN.md)  
**Accepted historical synthesis:** [`D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md)

This workspace preserves the completed S001–S005 discovery cycle and also supports later
explicitly authorized product discovery, simulation, evaluation, and failure-modeling work.
It does not own the live UpgradePilot stage or immediate continuation; those belong only in
[`../MEMORY.md`](../MEMORY.md).

## Purpose

Product simulation is a laboratory for asking questions that are difficult to answer from
plans or implementation alone.

It can use real public cases, captured evidence, controlled variants, synthetic scenarios,
and generated cases to discover:

- what kinds of dependency-update impact or incompatibility actually occur;
- which activation conditions make an upstream change relevant to a target repository;
- what repository, dependency, CI, environment, or policy evidence is discriminating;
- which investigations or targeted checks add information and which do not;
- when evidence is sufficient to stop;
- how missing, conflicting, stale, failed, or superseded evidence should behave;
- what failure/recovery/security/evaluation responsibilities may matter later;
- which historical product assumptions survive changed evidence and which need reconsideration.

The workspace stays aligned with the wider UpgradePilot project but is not limited to the
current implementation slice, current plan, or current design hypothesis. Findings here are
discovery/evaluation evidence, not controlling product architecture by themselves.

## Historical foundation — S001–S005

| Scenario | Main contrast | Historical full result | Historical baseline relationship |
|---|---|---|---|
| [`S001`](scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/README.md) | transitive docs/advisory path; relevant green CI | merge after normal review | same action, stronger support |
| [`S002`](scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md) | adapter path; relevant tests skipped | run targeted checks | same action, exact missing authority/checks |
| [`S003`](scenarios/S003-event-handler-loader-typescript-5.9.3-to-7.0.2/README.md) | failing install; peer conflict; attribution | block proposal as-is | same broad action, cause/recovery added |
| [`S004`](scenarios/S004-glyphslib-pytest-9.0.2-to-9.0.3/README.md) | exact relevant green control; stopping | merge after normal review | baseline sufficient |
| [`S005`](scenarios/S005-modelarrayio-pytest-9.0.3-to-9.1.1/README.md) | lock-backed matrix; target-scoped caution | merge after normal review | baseline wrong action |

These actions are preserved historical outputs. They are not automatic truth labels for
later product behavior.

## Recalibrated discovery aids

- [`PRODUCT_SIMULATION_RECALIBRATION_2026-08-06.md`](PRODUCT_SIMULATION_RECALIBRATION_2026-08-06.md) — dated record explaining why the workspace was recalibrated after major product progress.
- [`IMPACT_INVESTIGATION_COVERAGE_REBASE_2026-08-06.md`](IMPACT_INVESTIGATION_COVERAGE_REBASE_2026-08-06.md) — re-reads S001–S005 through impact, activation, applicability, investigation, and stopping lenses without changing the historical cases.
- [`CASE_SELECTION_FRAMEWORK_V2.md`](CASE_SELECTION_FRAMEWORK_V2.md) — current non-controlling selection aid for real, real-derived, synthetic, and generated future work.
- [`CASE_CANDIDATE_SCREENING_01.md`](CASE_CANDIDATE_SCREENING_01.md) — preserved July 31 candidate screening; useful historical evidence, not a standing S006 selection.

## Historical logical runtime

D1 discovered this useful logical family:

```text
real event and invocation
→ exact identity freeze
→ material operations
→ raw or durable evidence
→ evidence records and states
→ claims and interpretations
→ findings and uncertainty
→ transparent baseline
→ conditional-stage activation or non-activation
→ bounded decision or abstention
→ machine and human reports
→ follow-up, rerun, and supersession
→ review, ownership, stopping, and validation
```

Exact files, fields, and action vocabulary remain historical discovery rather than a frozen
future architecture.

## Durable lessons from the historical cycle

- invocation is distinct from discovered identity;
- exact repository/base/head/change identity matters;
- dependency role and path are multi-axis;
- CI authority requires dependency identity, trigger, job, step, command, revision,
  environment, scope, result, and retention context;
- evidence states can change what further work is justified;
- evidence, interpretations, findings, decisions, and reports are distinct;
- reports are projections from accepted state;
- conditional stages need activation conditions;
- non-activation and stopping are affirmative technical results;
- historical merge state is action, not correctness evidence;
- structural validation is deterministic work;
- AI completion does not prove Ali-owned capability.

## Conditional historical artifacts

These remain conditional rather than universal:

- `CHECK_EXECUTIONS.jsonl` for repeated or comparable executions;
- `FAILURE_ATTRIBUTION.json` for competing causes;
- `STOPPING_EVALUATION.json` for sufficiency, cost, or overreach;
- advisory, adapter, dynamic, private, platform, temporal, and post-merge analysis;
- separate dependency-update and PR-action dimensions.

New future work may trial additional representations when a distinct responsibility is
actually demonstrated.

## Safety and ownership

No target repository should be mutated from simulation work without Ali's exact authorization.
Public repository material and downloaded evidence are untrusted data. Simulation success does
not establish update safety, universal compatibility, production readiness, automated
reliability, or Ali-owned technical mastery.
