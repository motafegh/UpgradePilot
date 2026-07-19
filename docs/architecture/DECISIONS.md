# UpgradePilot Architecture Decisions

**Status:** Active

**Recorded:** 2026-07-19

This record captures decisions that materially shape the product. A changed decision must include observed evidence, the affected boundary, migration cost, and what remains fixed.

| ID | Decision | Status | Why | Revisit trigger |
|---|---|---|---|---|
| D-001 | Use a Python 3.12+ `src/`-layout package | Accepted | Matches the available environment, prevents accidental root imports, and supports an installable CLI | A supported deployment or contributor environment requires another version |
| D-002 | Begin as a CLI-first modular monolith | Accepted | The user workflow is a bounded investigation and report; one process maximizes traceability and ownership | A measured lifecycle, isolation, or scaling need appears |
| D-003 | Keep the domain core dependency-free | Accepted | Evidence states and deterministic rules do not require a framework; fewer dependencies reduce bootstrap and supply-chain risk | Validation complexity or repeated adapter code demonstrates a concrete benefit |
| D-004 | Use versioned JSON as the canonical input and report contract | Accepted | JSON is replayable, diffable, machine-readable, and maps directly to public APIs | Scale or query evidence requires an additional internal representation |
| D-005 | Render Markdown from the canonical report | Accepted | Maintainers need a readable artifact without creating a second source of truth | A real user needs another projection |
| D-006 | Use a transparent deterministic policy before ML/LLM/agents | Accepted | Required by the thesis and evaluation doctrine; supplies a falsifiable baseline | Never removed; later methods compare against it |
| D-007 | Preserve raw evidence separately from normalized contracts | Accepted | Enables provenance, replay, schema correction, and source-failure diagnosis | Never removed; storage form may evolve |
| D-008 | Adopt SQLite at the persistence stage | Planned | It provides relational queries and reproducibility without a service dependency | Concurrency, deployment, or query evidence shows it is insufficient |
| D-009 | Keep network acquisition behind adapters and out of unit tests | Accepted | External sources are mutable and failure-prone; deterministic tests require preserved fixtures | Never removed; bounded live probes remain separate |
| D-010 | Pin GitHub Actions by immutable commit | Accepted | Reduces workflow supply-chain drift while retaining explicit version comments | Reviewed dependency update |
| D-011 | Do not choose FastAPI, Pydantic, an ORM, Docker, or a cloud provider yet | Deferred | None is required for the current input-to-report responsibility | A named user-visible or operating limitation is observed |
| D-012 | Treat advanced systems as branch/pilot comparisons around the core | Accepted | Preserves the mission and allows honest A1/A2 evidence without architecture theater | A pilot earns an explicit A3 adopt decision |

## Dependency admission checklist

Before adding a runtime dependency, record:

1. the exact current limitation;
2. the standard-library or existing baseline;
3. the smallest candidate integration;
4. measurable benefit and rejection condition;
5. security and maintenance cost;
6. how Ali will explain, modify, test, and diagnose it;
7. removal or migration path.

## First expected decision review

After the completed UP-S01 report is converted to the JSON contract, review D-003, D-004, D-006, and D-007 against the real case. Correct contract or policy defects before adding live acquisition.
