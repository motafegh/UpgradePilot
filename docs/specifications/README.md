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

A specification answers **what the system must represent and guarantee**. It does not by itself select a Python framework, database, service boundary, directory hierarchy, or deployment mechanism.

## Relationship to other artifacts

- The Career charter, capability specification, learning/execution contract, roadmap, milestone plan, tracker, and active plan control mission, authorization, sequence, gates, and capability evidence.
- `docs/specifications/` controls accepted project-level technical contracts within those authorized boundaries.
- `docs/architecture/` records accepted consequential implementation or structural choices and their trade-offs.
- `plans/` coordinates execution of an authorized bounded responsibility.
- `working-memory/` records what occurred during material work.
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

## Current specification

- [`UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md) — conceptual pipeline, core information contracts, invariants, evidence states, failure semantics, M2 activation boundary, and method-selection criteria.
