# B2/X1 Product-Simulation Transfer Evaluations Index

**Date:** 2026-08-28  
**Status:** NON-CONTROLLING SIMULATION INDEX  
**Purpose:** discoverability and evidence lineage only; not live project status, implementation authority, or continuation ownership

This index groups the bounded B2/X1 product-simulation evaluations created on the dedicated support-lab branch.

Read `AGENTS.md` and `SIMULATION_GOVERNANCE_AND_PLAN.md` first. Read `../MEMORY.md` for live project position.

## 1. Transfer-pressure inventory

[`B2_X1_MODEL_READY_TRANSFER_PRESSURE_INVENTORY_2026-08-28.md`](B2_X1_MODEL_READY_TRANSFER_PRESSURE_INVENTORY_2026-08-28.md)

Question:

> Which materially different planning/investigation behaviors already discovered by the simulation corpus are covered, partial, missing-now, later-loop pressure, or outside the current X1 claim?

Main bounded results:

- no simulation blocker to the intentionally small Phase-4A development smoke;
- harder no-tool disposition reasoning deserved transfer pressure;
- S007 pre-execution action staleness deserved a separate later-loop pressure;
- S009/S010-style responsibilities should not be pulled into the one-action planner merely for breadth;
- no S013 or fabricated second action was justified.

## 2. No-tool disposition transfer

[`b2-x1-no-tool-disposition-transfer/README.md`](b2-x1-no-tool-disposition-transfer/README.md)

Question:

> Can `stop`, `defer`, and `unresolved` be distinguished for the correct planning-question/evidence reasons rather than by shallow heuristics such as “anything unresolved means continue” or “no action means stop”?

Primary evidence:

- S005 / S006 / S012 — known useful outside capability → `defer` shape;
- S008 / S011 — owned question settled while adjacent/deeper facts remain unresolved → `stop` shape;
- conflicted synthetic control — no action and no grounded outside capability → `unresolved` shape.

Important transfer finding:

```text
tool safety
!=
semantic correctness of model-driven no-tool control flow
```

Current pilot appropriately evaluates no-tool semantics rather than treating deterministic no-capability admission as proof that the model's reasoning is correct.

## 3. Pre-execution action staleness

[`b2-x1-pre-execution-action-staleness/README.md`](b2-x1-pre-execution-action-staleness/README.md)

Question:

> What happens when an action was useful when selected but trusted evidence changes before execution and the action loses discriminating value or no longer satisfies its precondition?

Primary evidence:

- real S007: resolver dry-run was plausible at T1, then authoritative package-family evidence closed the proposition before execution;
- current `AllowedInvestigationAction` preconditions and `admit_agent_plan(...)` state/coverage recheck;
- current Phase-4A runner reuses one frozen case snapshot because it performs no real action execution.

Important transfer finding:

```text
selection-time validity
!=
execution-time validity
```

The closest standard engineering concepts are TOCTOU/stale-plan control and pre-execution revalidation. Current action contracts can participate in revalidation if future orchestration supplies current trusted state; no snapshot-version/framework implementation is justified now.

## 4. Action-failure and retry boundary

[`b2-x1-action-failure-retry-boundary/README.md`](b2-x1-action-failure-retry-boundary/README.md)

Question:

> Which failures should consume a planner action and block blind model-level repetition, and which failures may instead belong to bounded deterministic transport/executor retry policy?

Primary evidence:

- `AttemptedInvestigationAction` + `action_already_attempted` repeat guard;
- Phase-1 statement that immutable A1 is logically idempotent but should not be blindly repeated after an available/problem result;
- GitHub provider acquisition taxonomy;
- target-Python typed problem taxonomy.

Important transfer finding:

```text
typed domain/evidence problem
!=
transient acquisition/transport failure
```

Planner repeat suppression and provider/executor retry are separate responsibilities. Future integration should not flatten timeout/rate-limit/transport failure and stable target-declaration problems into one planner-history meaning when that would change retry/defer semantics.

## 5. Shared boundaries across the evaluation family

These assets jointly preserve the following current conclusions without turning them into product architecture authority:

```text
closed action catalog
+ deterministic tool admission
is necessary
but not sufficient for complete orchestration correctness
```

Why:

- no-tool decisions can be semantically wrong while executing no capability;
- selected actions can become stale before execution;
- failure classification can change whether repeating an action is useful or merely redundant;
- current trusted evidence state, planning-question ownership, and lower-layer failure authority must remain explicit.

At the same time, none of these findings currently justify delaying the small development smoke or adding:

- a second action;
- an agent framework;
- generic middleware/hook layers;
- snapshot-version infrastructure;
- production retry machinery;
- a new numbered public scenario.

## 6. Preservation rule

These files are product-simulation discovery/transfer evidence.

They do not:

- update `MEMORY.md`;
- authorize product/experiment mutation;
- change the accepted Phase-3A protocol;
- establish local runtime PASS or model quality;
- own future continuation.

Admit another B2/X1 simulation asset only when a materially different question remains after checking these records and the preserved S001–S012 evidence.
