# UpgradePilot Product Simulation Workspace

**Status:** Active D1 complete-runtime and artifact-lifecycle discovery workspace
**Local authority:** [`AGENTS.md`](AGENTS.md)
**Controlling plan:** [`SIMULATION_GOVERNANCE_AND_PLAN.md`](SIMULATION_GOVERNANCE_AND_PLAN.md)
**Project route:** [`../plans/UPGRADEPILOT_90_DAY_PLAN.md`](../plans/UPGRADEPILOT_90_DAY_PLAN.md)
**Historical authorization:** [`../plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md`](../plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md)
**Learning companion:** [`../learning/product-simulation/`](../learning/product-simulation/)

## Purpose

This workspace manually performs the intended UpgradePilot runtime on materially
different real dependency-update cases before B1 freezes the first implementation
responsibility.

It discovers both:

1. **product behavior** — what must be investigated, concluded, reported, stopped,
   and requested from the maintainer; and
2. **artifact behavior** — what invocation, identity, operation, evidence,
   transformation, finding, decision, report, follow-up, review, and replay state
   must be created and preserved.

A complete `CASE.md` is necessary but is not sufficient by itself.

## Local control and method boundary

Inside `product-simulation/`, local rules control conflicting project-local
process, artifact, method, milestone, and completion rules.

Any lawful, safe, accessible, materially useful method may be used for discovery.
Simulation use does not admit a method into permanent architecture, establish
automated capability, expand the charter's Python boundary, or authorize
target-repository mutation.

## Controlling and synthesis files

- [`AGENTS.md`](AGENTS.md)
- [`SIMULATION_GOVERNANCE_AND_PLAN.md`](SIMULATION_GOVERNANCE_AND_PLAN.md)
- [`RUNTIME_ARTIFACT_SPECIFICATION.md`](RUNTIME_ARTIFACT_SPECIFICATION.md)
- [`TRANSPARENT_BASELINE_SPECIFICATION.md`](TRANSPARENT_BASELINE_SPECIFICATION.md)
- [`SCENARIO_EXECUTION_TEMPLATE.md`](SCENARIO_EXECUTION_TEMPLATE.md)
- [`SCENARIO_COVERAGE.md`](SCENARIO_COVERAGE.md)
- [`S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md`](S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md)
- [`S003_FAILING_CI_SCENARIO_REQUIREMENTS.md`](S003_FAILING_CI_SCENARIO_REQUIREMENTS.md)
- [`S003_POST_CASE_SYNTHESIS.md`](S003_POST_CASE_SYNTHESIS.md)

## Default scenario bundle

```text
product-simulation/scenarios/<case-id>/
├── README.md
├── CASE.md
└── artifacts/
    ├── RUN_MANIFEST.json
    ├── INVOCATION.json
    ├── CASE_IDENTITY.json
    ├── OPERATION_EVENTS.jsonl
    ├── EVIDENCE_ITEMS.jsonl
    ├── CLAIMS_AND_INTERPRETATIONS.jsonl
    ├── FINDINGS.json
    ├── BASELINE_RESULT.json
    ├── DECISION.json
    ├── MACHINE_REPORT.json
    ├── FOLLOW_UP_STATE.json
    ├── REVIEW_AND_OWNERSHIP.json
    ├── HUMAN_REPORT.md
    ├── raw/
    └── checks/
```

The logical responsibilities are repeated stable candidates. Exact fields,
physical splits, and persistence architecture remain provisional.

Conditional artifacts may be added when a case activates a real responsibility.
S003 demonstrated two conditional candidates:

- `CHECK_EXECUTIONS.jsonl` for repeated or comparative executions;
- `FAILURE_ATTRIBUTION.json` for competing causal explanations.

They are not universal default artifacts yet.

## Progressive requirement

Every new case must create artifacts during the investigation:

```text
candidate screening
→ selected and frozen
→ material evidence acquired
→ interpretation/findings updated
→ decision and reports completed
→ validated and reviewed or explicitly review-pending
```

S001 and S002 are honest retrospective reconstructions. S003 is the first
prospective scenario with separate durable checkpoints for this lifecycle.

## Completed cases

| Scenario | Result | Artifact status | Baseline result | Review status |
|---|---|---|---|---|
| [`S001`](scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/README.md) | Merge after normal maintainer review | Complete retrospective bundle; validation passed | Same action; weaker reasons, certainty, and actionability | Factual correction complete; Ali final acceptance pending |
| [`S002`](scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md) | Run targeted checks before merge | Complete retrospective bundle; validation passed | Same action; weaker reasons, certainty, and actionability | AI factual recheck complete; Ali review pending; behavior not confirmed |
| [`S003`](scenarios/S003-event-handler-loader-typescript-5.9.3-to-7.0.2/README.md) | Block current TypeScript 7.0.2 proposal as-is; coordinated compatible toolchain revision required | Complete prospective bundle; five natural checkpoints; validation passed | Same broad action; full result identified failed responsibility, peer conflict, comparison evidence, recovery, and decision dimensions | AI factual review complete; Ali review pending; controlled local reproduction unavailable |

Artifact and record counts describe granularity and preservation choices. They are
not quality metrics.

## S003 result

S003 investigated `xayanide/event-handler-loader#341`, TypeScript `5.9.3` →
`7.0.2`.

The visible `Linters` workflow failed during `npm ci`; ESLint never ran. The
proposal retained TypeScript-ESLint `8.65.0`, whose frozen peer declarations support
TypeScript `>=4.8.4 <6.1.0`. An adjacent PR from the exact same base passed
installation and lint under a near-comparable public environment.

Current attribution:

```text
update_caused
at dependency-tree/installability layer
strongly supported, not absolute
```

Current decision dimensions:

```text
dependency update: update_caused_block
PR action: blocked_by_current_ci
```

The evidence blocks this proposal as generated, not every future TypeScript 7
migration.

## Cross-case findings after S003

Repeated stable candidates now include:

- exact identity freeze and separate invocation;
- dependency path and multi-axis role;
- peer/support relationships as dependency evidence;
- CI trigger, job, step, command, revision, environment, and retention authority;
- explicit missing, expired, inaccessible, superseded, and method-failure states;
- separate operations, evidence, transformations, findings, decisions, reports,
  follow-up, review, and ownership;
- versioned transitions and new-run rules;
- structural validation;
- prospective checkpoint history.

Conditional responsibilities include advisory/exploitability analysis,
adapter/framework compatibility, artifact identity, repeated execution modeling,
causal failure attribution, semantic-version/peer-range comparison, dynamic
execution, private acquisition, and platform/native/toolchain analysis.

Conditional work must not become a universal stage.

## Thesis status

S001, S002, and S003 all currently belong to this comparative class:

```text
baseline broad action = full-investigation broad action
+
full investigation materially improves authority, calibration, explanation,
auditability, actionability, or transitions
```

This is meaningful evidence but does not validate the full thesis. Required
contrasts remain:

- baseline sufficient with little added value;
- baseline wrong action;
- unresolved comparison;
- possible overreach or excessive investigation cost.

## Current D1 action

Implementation remains paused.

1. Select S004 as a deliberately simple baseline-sufficient control.
2. Create S004 prospectively and stop when decision support is already sufficient.
3. Record investigation cost and stopping implications.
4. Select S005 as the strongest available baseline-wrong-action or
   dependency-versus-PR-action divergence case.
5. Execute S005 prospectively and perform focused synthesis.
6. Return to the controlling route for B1 implementation-responsibility freeze.

Do not resume M2-S03, continue merely to reach a fixed case count, or universalize
S003's conditional artifacts.

No target repository was mutated during S003. Independent Ali capability is not
inferred from AI-controlled execution.
