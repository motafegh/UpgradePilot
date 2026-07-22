# UpgradePilot Product Simulation Workspace

**Status:** Active manual product-discovery workspace  
**Controlling plan:** [`../plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md`](../plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md)  
**Implementation:** No product code is authorized by this workspace

## Purpose

This workspace is used to manually perform the complete intended UpgradePilot runtime on real public dependency-update cases before more implementation proceeds.

Ali and the AI assistant act as the UpgradePilot system and document:

- what starts the run;
- what information is supplied initially;
- what evidence must be discovered or acquired;
- where each item originates;
- why each item matters;
- how the investigation proceeds;
- which tool, command, query, or manual method is selected and why;
- what useful output is expected and what success would not prove;
- what raw or material output is obtained;
- which approaches fail, are abandoned, or are superseded;
- how each outcome causes the next selected action;
- what is observed, interpreted, inferred, contradicted, missing, or unresolved;
- what decision support can be justified;
- what the maintainer receives and does next;
- which future methods might automate each responsibility;
- what each case changes in the shared product model.

The workspace validates complete product behavior. It does not predetermine implementation architecture.

## Current files

- [`SCENARIO_EXECUTION_TEMPLATE.md`](SCENARIO_EXECUTION_TEMPLATE.md) — adaptable structure for one complete manual runtime;
- [`SCENARIO_COVERAGE.md`](SCENARIO_COVERAGE.md) — evolving coverage dimensions and scenario register.

## Completed scenarios

| Scenario | Primary record | Manual outcome | Main product insight |
|---|---|---|---|
| [`S001`](scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/CASE.md) | [Unified full record](scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/CASE.md) | Merge after normal review | Dependency graph, repository usage, advisory evidence, exact CI-path coverage, and operation lineage must be joined before evidence may affect a decision |
| [`S002`](scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/README.md) | [Progressive result](scenarios/S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1/CASE.md) | Run targeted checks; merge only if exact-head Python checks pass | Green CI has decision authority only when the changed path triggered the relevant job, the job executed the relevant commands, and the tested dependency environment is identifiable |

S001 now has one authoritative `CASE.md` containing the correction notice, operational trace, exact tools and reasons, failures and replacements, evidence model, findings, decision, outputs, diagrams, and retrospective. Official advisory publication dates are June 1, 2026, and the exact Dependabot trigger remains unresolved. The correction does not change its primary recommendation.

S002 was executed using `CASE.md` as the live progressive primary record. It did not require a separate execution-trace file.

## Artifact organization

The normal scenario organization is:

```text
product-simulation/
├── scenarios/
│   └── <case-id>/
│       └── CASE.md
├── SYSTEM_OPERATING_MODEL.md
├── INPUT_AND_EVIDENCE_CATALOG.md
├── DATA_FLOW_AND_USER_FLOW.md
└── SYNTHESIS.md
```

A scenario should keep its complete operational execution and final product result together in one `CASE.md` whenever that remains readable. Add another scenario-local file only when a real external need cannot be satisfied clearly inside the primary record; do not split execution from meaning merely for organizational symmetry.

The cross-case artifacts remain candidates and are created only when evidence makes them useful. Do not create empty placeholders.

## Non-exhaustive rule

No list in this workspace is a hard limit.

Real cases may reveal new:

- actors;
- input types;
- evidence sources;
- investigation stages;
- failure states;
- methods;
- outputs;
- user interactions;
- decision outcomes;
- diagrams;
- product responsibilities.

The workspace must adapt to those discoveries. A case must not be forced into a current list or template when doing so would hide reality.

## Working rules

1. Use real public cases and preserve time/revision context.
2. Distinguish invocation inputs from evidence acquired later.
3. Separate source observations, attributed claims, interpretations, findings, and decisions.
4. Record origin, purpose, authority, limitations, and failure behavior for material information.
5. Follow the complete case through to a maintainer-facing result.
6. Record each material current state → selected approach and reason → exact operation → expected output → material/raw output → interpretation → outcome → next action chain.
7. Preserve failed, abandoned, contradictory, missing, ambiguous, stale, invalid, inaccessible, irrelevant, and superseded paths.
8. Record candidate methods without prematurely selecting permanent architecture.
9. Keep each scenario's execution and final meaning unified in its primary `CASE.md` unless a real readability or external constraint requires otherwise.
10. Add structure only when it improves product understanding or traceability.
11. Do not implement product code while the simulation plan is current.
12. Treat all enumerations as starting prompts rather than closed schemas.
13. Do not reconstruct an artificially clean history or invent missing operational details.

## Current next action

Review S002's scenario entry point and progressive `CASE.md`. Challenge:

- whether the direct-declaration, test-use, and production-installation distinction is accurate;
- whether the FastAPI/Starlette compatibility threshold received appropriate authority;
- whether the successful Docker build was correctly limited to installation/image-build evidence;
- whether the skipped Python workflow and expired logs justify the targeted-check outcome;
- whether any material operation, failed approach, uncertainty, or result-to-next-action transition is missing.

After that review, select a third case because it tests the highest-value remaining product uncertainty:

> A real dependency-update PR with an actual failing test workflow, where UpgradePilot must distinguish update-caused failure from pre-existing, flaky, environmental, or unrelated failure.

Do not select another case merely because it is convenient or similar.
