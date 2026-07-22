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

| Scenario | Case | Manual outcome | Main product insight |
|---|---|---|---|
| [`S001`](scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/CASE.md) | `pydantic/pydantic#13432` — Soup Sieve 2.6 → 2.8.4 | Merge after normal review | Dependency graph, repository usage, advisory evidence, and exact CI-path coverage must be joined before evidence may affect a decision |

## Artifacts created only when evidence requires them

Expected later artifacts may include:

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

This is a candidate organization, not a mandatory fixed structure. Files may be combined, split, renamed, added, or removed when real scenario work shows a clearer and less ceremonial organization.

Do not create empty placeholders.

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
6. Record candidate methods without prematurely selecting permanent architecture.
7. Preserve missing, conflicting, ambiguous, stale, invalid, inaccessible, or irrelevant evidence.
8. Add structure only when it improves product understanding or traceability.
9. Do not implement product code while the simulation plan is current.
10. Treat all enumerations as starting prompts rather than closed schemas.

## Current next action

Select a second real case that materially contrasts with S001.

The highest-value contrast is:

> A direct runtime dependency update with an API or behavior change and failing or conflicting CI.

The next case should be selected because it tests unresolved product behavior, not merely because it is convenient or similar.
