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

The workspace validates the complete product behavior. It does not predetermine implementation architecture.

## Current files

- [`SCENARIO_EXECUTION_TEMPLATE.md`](SCENARIO_EXECUTION_TEMPLATE.md) — adaptable structure for one complete manual runtime;
- [`SCENARIO_COVERAGE.md`](SCENARIO_COVERAGE.md) — evolving coverage dimensions and scenario register.

## Completed scenarios

| Scenario | Case records | Manual outcome | Main product insight |
|---|---|---|---|
| [`S001`](scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/README.md) | [result](scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/CASE.md) · [execution trace](scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/EXECUTION_TRACE.md) | Merge after normal review | Dependency graph, repository usage, advisory evidence, and exact CI-path coverage must be joined before evidence may affect a decision |

S001 includes a correction notice: official advisory publication dates are June 1, 2026, and the exact Dependabot trigger remains unresolved. The correction does not change the primary recommendation.

## Artifacts created only when evidence requires them

Expected later artifacts may include:

```text
product-simulation/
├── scenarios/
│   └── <case-id>/
│       ├── README.md
│       ├── CASE.md
│       └── EXECUTION_TRACE.md  # only when a separate trace improves clarity
├── SYSTEM_OPERATING_MODEL.md
├── INPUT_AND_EVIDENCE_CATALOG.md
├── DATA_FLOW_AND_USER_FLOW.md
└── SYNTHESIS.md
```

This is a candidate organization, not a mandatory fixed structure. Files may be combined, split, renamed, added, or removed when real scenario work shows a clearer and less ceremonial organization.

Do not create empty placeholders.

For S002 onward, the active `CASE.md` remains the progressive primary execution record. A separate trace is not mandatory when `CASE.md` already preserves the complete live operation chain without becoming unreadable.

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
9. Add structure only when it improves product understanding or traceability.
10. Do not implement product code while the simulation plan is current.
11. Treat all enumerations as starting prompts rather than closed schemas.
12. Do not reconstruct an artificially clean history or invent missing operational details.

## Current next action

Review S001's result, execution trace, and correction notice together. Challenge:

- whether the operational reconstruction is sufficiently honest and reproducible;
- whether any material tool choice, failure, or transition is still missing;
- whether the corrected advisory timing changes any other product insight;
- whether the decision remains proportionate.

After that review, select a second real case that materially contrasts with S001.

The highest-value contrast remains:

> A direct runtime dependency update with an API or behavior change and failing or conflicting CI.

The next case should be selected because it tests unresolved product behavior, not merely because it is convenient or similar.
