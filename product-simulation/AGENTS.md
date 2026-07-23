# Local Agent Instructions — Product Simulation

## Scope and authority

These instructions apply under `product-simulation/` and control simulation execution, evidence preservation, stopping, review, completion, and synthesis.

Authority order:

1. external safety, law, privacy, credentials, permissions, and platform limits;
2. Ali's explicit current instruction;
3. this file;
4. [`SIMULATION_GOVERNANCE_AND_PLAN.md`](SIMULATION_GOVERNANCE_AND_PLAN.md);
5. artifact and baseline specifications;
6. current synthesis and coverage;
7. other project-local records.

Simulation does not mutate target repositories, expand the public-Python boundary, select permanent architecture, or establish automated capability.

## Current shared owners

- [`D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md)
- [`SCENARIO_COVERAGE.md`](SCENARIO_COVERAGE.md)
- [`S005_POST_CASE_SYNTHESIS.md`](S005_POST_CASE_SYNTHESIS.md)
- [`../plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md`](../plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md)

## Core simulation rule

Manually perform the intended product responsibility and create the durable state the future system conceptually needs. `CASE.md` is a human-auditable story, not a substitute for invocation, identity, operations, evidence, transformations, findings, baseline, decision, reports, follow-up, review, and validation.

## External-action boundary

- Do not mutate, approve, comment on, close, merge, rerun, or otherwise change a target repository without Ali's exact authorization.
- Do not use private or credential-sensitive evidence without authorization.
- Treat source, packages, logs, release notes, and model output as untrusted.
- Preserve method, inputs, outputs, failures, side effects, and proof limits.
- Never invent raw output, diagnostics, environments, timestamps, or results.

## Evidence and lineage

Use the smallest preservation strategy retaining decision, audit, replay, and diagnostic value.

```text
report
→ decision reason
→ finding or limitation
→ claim or interpretation
→ evidence
→ operation
→ raw/reference source
→ frozen identity
```

Evidence acquisition proves observation, not truth or relevance.

## Baseline, action change, and stopping

- Execute the transparent baseline before final full-result interpretation.
- Preserve the baseline even when the full decision supersedes it.
- Do not force the full investigation to win.
- Identify the smallest authority-critical question and stop/switch conditions.
- Stop when further work cannot materially change action, uncertainty, required checks, conditional-stage activation, or the evaluation conclusion.
- Non-activation is affirmative runtime state.

## Conditional state

Activate only when the responsibility is real:

- `CHECK_EXECUTIONS.jsonl` for material repeated/matrix/comparable executions;
- `FAILURE_ATTRIBUTION.json` for competing causes of failing evidence;
- `STOPPING_EVALUATION.json` for material sufficiency, cost, or overreach questions;
- separate dependency/PR decision dimensions only when evidence supports different answers.

Do not universalize a conditional artifact.

## Review and ownership

Keep execution, factual review, Ali review, external confirmation, AI assistance, and Ali-owned capability separate. AI-produced completion and historical merge state are not correctness or capability proof.

## Case completion

A case is complete only when:

- invocation and frozen identity are clear;
- the work reaches a justified stop;
- required logical state exists or is explicitly unavailable/not applicable;
- JSON/JSONL and references are structurally coherent;
- failures, missing evidence, supersession, contradiction, and uncertainty remain visible;
- baseline/full comparison is complete;
- decision and reports trace to evidence;
- transitions and new-run boundaries exist;
- review and ownership states are explicit;
- coverage and synthesis are updated;
- unsupported safety, automation, or capability claims are absent.

## Current route

S001–S005 are complete technical discovery evidence. Do not select S006 merely to continue simulation.

Current sequence:

1. Ali reviews [`D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md).
2. Record corrections, acceptance, or deferred disagreements.
3. Return control to the project route and activate B1.
4. Execute the responsibility-freeze requirements before any B2 implementation plan.

Add another simulation only when a named planning uncertainty still blocks B1. Do not resume M2-S03 or select architecture from illustrative artifacts.