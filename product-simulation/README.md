# UpgradePilot Product Simulation Workspace

**Status:** Active complete-runtime and artifact-lifecycle discovery workspace  
**Local authority:** [`AGENTS.md`](AGENTS.md)  
**Controlling plan:** [`SIMULATION_GOVERNANCE_AND_PLAN.md`](SIMULATION_GOVERNANCE_AND_PLAN.md)  
**Parent authorization:** [`../plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md`](../plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md)

## Purpose

This workspace manually performs the intended UpgradePilot runtime on materially
different real dependency-update cases before more implementation proceeds.

It discovers both:

1. **product behavior** — what must be investigated, concluded, reported, and
   requested from the maintainer; and
2. **artifact behavior** — what invocation, identity, operation, evidence,
   transformation, finding, decision, report, follow-up, review, and replay state
   must be created and preserved.

A complete `CASE.md` is necessary but is not sufficient by itself.

## Local control

Inside `product-simulation/`, local rules control conflicting project-local
process, artifact, method, milestone, and completion rules.

Any lawful, safe, accessible, materially useful method may be used for discovery,
including scripts, local execution, containers, databases, models, agents,
static/dynamic analysis, and human review. Simulation use does not admit a method
into permanent product architecture or establish automated capability.

## Controlling and current files

- [`AGENTS.md`](AGENTS.md) — local instruction routing and completion behavior;
- [`SIMULATION_GOVERNANCE_AND_PLAN.md`](SIMULATION_GOVERNANCE_AND_PLAN.md) — local
  governance and execution plan;
- [`RUNTIME_ARTIFACT_SPECIFICATION.md`](RUNTIME_ARTIFACT_SPECIFICATION.md) —
  required logical runtime-artifact family;
- [`TRANSPARENT_BASELINE_SPECIFICATION.md`](TRANSPARENT_BASELINE_SPECIFICATION.md)
  — restricted comparator used to test the thesis;
- [`SCENARIO_EXECUTION_TEMPLATE.md`](SCENARIO_EXECUTION_TEMPLATE.md) — adaptable
  complete-run structure;
- [`SCENARIO_COVERAGE.md`](SCENARIO_COVERAGE.md) — compact cross-case status;
- [`S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md`](S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md)
  — completed two-case artifact and product synthesis;
- [`S003_FAILING_CI_SCENARIO_REQUIREMENTS.md`](S003_FAILING_CI_SCENARIO_REQUIREMENTS.md)
  — entry, execution, attribution, artifact, validation, and stop requirements for
  the next case.

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

`CASE.md` is the complete human-auditable story. The bundle is the simulated
system state. The logical responsibilities are repeated stable candidates; the
exact fields and physical split are not frozen production schemas.

## Progressive requirement

Every new case must create artifacts during the investigation:

```text
selected and frozen
→ materially investigated
→ decision and reports completed
→ reviewed or explicitly pending review
```

S001 and S002 are honest retrospective reconstructions. S003 must be the first
prospective case whose repository history demonstrates this lifecycle naturally.

## Completed cases

| Scenario | Result | Artifact status | Baseline result | Review status |
|---|---|---|---|---|
| [`S001`](scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/README.md) | Merge after normal maintainer review | Complete retrospective bundle: 35 manifest items, 22 operations, 26 evidence items, 16 transformations, 12 findings; validation passed | Same action; weaker reasons, certainty, and actionability | Factual correction complete; Ali final acceptance pending; external confirmation absent |
| [`S002`](scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md) | Run targeted checks; merge only after exact-head checks pass | Complete retrospective bundle: 39 files, 10 operations, 20 evidence items, 9 transformations, 9 findings; validation passed | Same action; weaker reasons, certainty, and actionability | AI factual recheck complete; Ali review pending; exact behavior not confirmed |

Artifact counts describe recording granularity and preservation choices. They are
not quality or success metrics.

## Cross-case result

The default logical artifact family survived two materially different cases.
No evidence currently justifies removing a universal responsibility or adding a
new universal top-level artifact.

The main defects discovered were:

- inconsistent field names, IDs, time formats, serialization, and validator
  practices across cases;
- no prospective progression proof yet;
- no structured repeated-check execution surface yet;
- no tested causal-failure attribution model;
- unresolved separation between dependency-update assessment and overall PR
  mergeability.

For S003:

- retain the default bundle;
- apply one common machine-artifact envelope and ID convention;
- use deterministic readable JSON formatting;
- trial `CHECK_EXECUTIONS.jsonl` and `FAILURE_ATTRIBUTION.json`;
- execute the transparent baseline before deep investigation;
- preserve actual failing CI at run/job/step/command/environment depth;
- compare update-caused, pre-existing, flaky, environmental, unrelated, mixed,
  and unresolved explanations;
- create natural durable checkpoints;
- use one declared structural-validation profile.

The trial artifacts are not universal until S003 and later cases demonstrate that
need.

## Thesis status

There are now two materialized comparative cases. In both:

```text
baseline broad action = full-investigation broad action
```

The full investigation still materially improved evidence authority, uncertainty
location, explanation, auditability, or actionability.

This supports one thesis class but does not validate the overall thesis. Future
coverage still needs:

- baseline wrong action;
- baseline sufficient with little added value;
- unresolved comparison;
- possible full-investigation overreach or excessive cost.

S003 must not be selected or interpreted to force a thesis result.

## Stable and conditional behavior

Repeated stable candidates include exact identity freeze, dependency-path
analysis, multi-axis dependency role, bounded evidence preservation, CI authority
analysis, explicit missing-evidence states, separate findings/decisions/reports,
supersession, follow-up transitions, structural validation, and distinct review
and ownership states.

Conditional responsibilities include advisory/exploitability analysis, adapter
compatibility, dynamic execution, private acquisition, post-merge checks,
platform/native analysis, and causal failure attribution.

Conditional work must not become a universal stage.

## Current next action

Do not resume M2-S03 implementation.

1. Ali reviews the cross-case synthesis and S003 requirements.
2. Correct only a real local-model defect identified during that review.
3. Select one S003 candidate satisfying the failing-CI and evidence-retention
   criteria.
4. Create S003 from the first selected-and-frozen checkpoint prospectively.
5. Use S003 to test causal attribution, repeated check execution, decision-axis
   separation, and the current artifact family.

No S003 candidate has been selected by the synthesis files alone.
