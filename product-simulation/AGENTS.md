# Local Agent Instructions — Product Simulation

## Scope and authority

These instructions apply under `product-simulation/`.

Product simulation is **closed at the current planning depth**. D1 was accepted on
2026-07-23 and control has returned to active B1 under:

- [`../plans/D1_ACCEPTANCE_AND_B1_ACTIVATION.md`](../plans/D1_ACCEPTANCE_AND_B1_ACTIVATION.md)
- [`../plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md`](../plans/B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md)
- [`../plans/UPGRADEPILOT_90_DAY_PLAN.md`](../plans/UPGRADEPILOT_90_DAY_PLAN.md)

Inside this subtree, this file still controls preservation, interpretation, and any
future explicitly authorized simulation work.

Authority order:

1. external safety, law, privacy, credentials, permissions, and platform limits;
2. Ali's explicit current instruction;
3. this file;
4. [`SIMULATION_GOVERNANCE_AND_PLAN.md`](SIMULATION_GOVERNANCE_AND_PLAN.md);
5. runtime artifact and transparent baseline specifications;
6. accepted synthesis, coverage, scenario bundles, and historical requirements.

## Current state

Completed:

- S001 — retrospective transitive/advisory case;
- S002 — retrospective adapter and incomplete-CI case;
- S003 — prospective failing-install and attribution case;
- S004 — prospective baseline-sufficient stopping control;
- S005 — prospective baseline-wrong-action case;
- accepted S001–S005 synthesis.

No S006 is authorized by default.

Do not:

- restart completed cases;
- select another case merely to increase case count;
- reactivate M2-S03;
- treat simulation files as production schemas;
- begin B2 product implementation from this subtree;
- infer safety, automated reliability, or Ali-owned capability from the cases.

A future case may be authorized only when B1 or later evaluation identifies a named
material uncertainty that existing evidence cannot resolve.

## Preservation rules

Maintain the evidence already established:

- exact invocation and frozen identity;
- operation and acquisition history;
- raw or durable evidence references;
- explicit evidence states;
- observation, interpretation, and finding separation;
- baseline and full-result comparison;
- conditional activation and non-activation;
- bounded decision and report lineage;
- follow-up, rerun, and supersession;
- review, assistance, ownership, cost, stopping, and validation state.

Never rewrite retrospective cases as prospective history or erase failed, inaccessible,
superseded, contradicted, or unresolved states.

## Conditional artifacts

These remain conditional, not universal:

- `CHECK_EXECUTIONS.jsonl` — repeated, matrix, rerun, or comparison executions;
- `FAILURE_ATTRIBUTION.json` — competing causes of failing evidence;
- `STOPPING_EVALUATION.json` — sufficiency, overreach, stage activation, or cost.

Separate dependency-update and PR-action dimensions remain conditional.

## Future simulation admission

When a future case is explicitly authorized:

1. name the planning or evaluation uncertainty;
2. show why existing cases cannot answer it;
3. prefer a supported-boundary Python Dependabot case;
4. preserve prospective screening, frozen baseline, material checkpoints, and honest
   stopping;
5. update synthesis only for findings that materially change the model.

Target repositories must not be mutated, approved, commented on, rerun, closed, or
merged without Ali's exact authorization.

## Current handoff

The next work belongs to B1:

```text
inspect current source and tests
→ reconcile existing implementation
→ freeze minimum executable responsibility
→ define B2 tests and Ali ownership work
→ create one bounded B2 plan
```
