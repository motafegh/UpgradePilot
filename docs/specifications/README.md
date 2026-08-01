# Technical Specifications

This directory contains accepted UpgradePilot technical specifications that define project-level conceptual contracts before implementation mechanisms are selected.

## Responsibility

A technical specification records:

- the end-to-end conceptual pipeline;
- information and responsibility boundaries;
- required, optional, conditional, and unavailable data;
- invariants and failure/degradation semantics;
- provisional assumptions and explicit open decisions;
- milestone activation boundaries;
- criteria that later implementation or architecture decisions must satisfy.

A specification answers **what the system must represent and guarantee**. It does not by itself select a Python framework, database, service boundary, directory hierarchy, deployment mechanism, or live project position.

## Relationship to other artifacts

- `../../PROJECT_CHARTER.md` controls the stable product mission and boundary.
- `../../plans/UPGRADEPILOT_90_DAY_PLAN.md` controls the stable route and gate definitions.
- `../../MEMORY.md` is the sole owner of live project position, verified behavior, blockers, selected plan, and exact continuation.
- `docs/specifications/` controls accepted project-level technical contracts within the authorized boundary.
- `docs/architecture/` records accepted consequential implementation or structural choices and their trade-offs.
- `plans/` coordinates execution of an authorized bounded responsibility without owning live status.
- `working-memory/` records dated evidence and reasoning without owning live status.
- `proposals/` preserves unadmitted future ideas.
- Source code, observed execution, and tests control actual executable behavior.

When a specification and an ADR differ, inspect their responsibilities: the specification controls required behavior and information boundaries; the ADR controls the selected mechanism. A later accepted artifact must explicitly state when it supersedes an earlier rule.

## Status vocabulary

Specifications should label material statements as one of:

- **Accepted** — required unless a later approved change supersedes it.
- **Provisional** — used to proceed now, with an explicit reassessment trigger.
- **Open** — must be decided before the named implementation boundary.
- **Deferred** — intentionally postponed until a later milestone or observed need.
- **Rejected** — considered and not permitted under the stated conditions.

## Specification navigation

This section is navigation only. It must not be used to infer which responsibility is active, completed, next, or behavior-validated. Each specification's own status line controls its acceptance status; `../../MEMORY.md` alone controls live project position and activation.

- [`UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md) — stable project invariants and retained historical M2 contract.
- [`UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md) — acceptance standard preventing fixture-specific or manually interpreted behavior from being promoted to automated product behavior.
- [`UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`](UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md) — project-wide naming and terminology clarity requirements.

Do not add labels such as **current specification**, **active specification**, **next specification**, or similar live-state wording here. If project position changes, update `../../MEMORY.md` only.