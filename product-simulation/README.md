# UpgradePilot Product Simulation Workspace

**Historical status:** D1 discovery completed and accepted on 2026-07-23; workspace retained as evidence  
**Local authority:** [`AGENTS.md`](AGENTS.md)  
**Accepted synthesis:** [`D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md`](D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md)  
**Acceptance record:** [`../plans/D1_ACCEPTANCE_AND_B1_ACTIVATION.md`](../plans/D1_ACCEPTANCE_AND_B1_ACTIVATION.md)

This file records completed discovery. It does not state the live project position or next
action; those belong only in [`../MEMORY.md`](../MEMORY.md).

## Purpose

This workspace manually performed the intended UpgradePilot runtime on materially different
real dependency-update cases before implementation responsibility was frozen.

It discovered:

- product behavior — what must be acquired, interpreted, concluded, reported, stopped, and requested;
- artifact behavior — what invocation, identity, operation, evidence, transformation, finding,
  decision, report, follow-up, review, and replay state must exist;
- stopping behavior — when a baseline needs deeper work and when confirmation is enough;
- automation boundaries — which responsibilities appear deterministic, interpretive,
  model-dependent, or human-controlled.

The workspace is discovery evidence. It is not the product runtime or a final schema.

## Completed cases

| Scenario | Main contrast | Full result | Baseline relationship |
|---|---|---|---|
| [`S001`](scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/README.md) | transitive docs/advisory path; relevant green CI | merge after normal review | same action, stronger support |
| [`S002`](scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md) | adapter path; relevant tests skipped | run targeted checks | same action, exact missing authority/checks |
| [`S003`](scenarios/S003-event-handler-loader-typescript-5.9.3-to-7.0.2/README.md) | failing install; peer conflict; attribution | block proposal as-is | same broad action, cause/recovery added |
| [`S004`](scenarios/S004-glyphslib-pytest-9.0.2-to-9.0.3/README.md) | exact relevant green control; stopping | merge after normal review | baseline sufficient |
| [`S005`](scenarios/S005-modelarrayio-pytest-9.0.3-to-9.1.1/README.md) | lock-backed matrix; target-scoped caution | merge after normal review | baseline wrong action |

Ali accepted the cross-case synthesis on 2026-07-23.

## Discovered logical runtime

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

Exact files and fields remain illustrative.

## Stable conclusions

- invocation is distinct from discovered identity;
- exact repository/base/head/change identity is mandatory;
- dependency role and path are multi-axis;
- CI authority requires dependency identity, trigger, job, step, command, revision,
  environment, scope, result, and retention context;
- evidence states can create actions;
- evidence, interpretations, findings, decisions, and reports are distinct;
- reports are projections from accepted state;
- conditional stages need activation conditions;
- non-activation and stopping are durable results;
- merge history is action, not correctness evidence;
- structural validation is deterministic work;
- AI completion does not prove Ali-owned capability.

## Conditional conclusions

These artifacts remain conditional rather than universal:

- `CHECK_EXECUTIONS.jsonl` for repeated or comparable executions;
- `FAILURE_ATTRIBUTION.json` for competing causes;
- `STOPPING_EVALUATION.json` for sufficiency, cost, or overreach;
- advisory, adapter, dynamic, private, platform, and post-merge analysis;
- separate dependency-update and PR-action dimensions.

No additional simulation is authorized merely to increase case count. A future case requires
an explicitly selected uncertainty that existing evidence cannot resolve.

No target repository was mutated during S001–S005.