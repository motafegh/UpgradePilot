# Technical Specifications and Engineering Standards

This directory contains accepted project-level technical specifications plus the retained project-wide naming/terminology engineering standard.

## Technical specification responsibility

A technical specification states **what admitted system behavior must represent or guarantee** independently of implementation mechanism. It may define:

- conceptual pipeline and information boundaries;
- required/optional/conditional/unavailable data semantics;
- invariants;
- validation, authority, failure, degradation, and abstention behavior;
- criteria that later architecture and implementation must satisfy.

A technical specification does not by itself select a Python framework, dependency, database, service boundary, directory hierarchy, provider, deployment mechanism, live project position, or execution sequence.

## Responsibility ownership across artifacts

- `../../PROJECT_CHARTER.md` → stable mission, user, supported boundary, evidence doctrine, claim limits.
- `../../plans/UPGRADEPILOT_90_DAY_PLAN.md` → stable route and gate definitions.
- `../../MEMORY.md` → sole live project position and continuation.
- technical specifications here → framework-independent required behavior/invariants.
- `../architecture/` → accepted consequential mechanisms/structural choices.
- `../../plans/` → bounded execution sequence, proof, and stop lines.
- source/tests/commands/outputs/environment → implemented truth.
- `../../working-memory/` → dated evidence/reasoning.
- `../../proposals/` → unadmitted future ideas.

Do not resolve disagreements through a generic total ranking after the user/local-instruction layer. Resolve them through the owner of the disputed responsibility. For example:

- a specification controls required behavior;
- an ADR controls the selected method used to satisfy it;
- a plan coordinates implementation/proof of that method;
- source/tests establish what is actually implemented.

A different artifact may add detail within its own responsibility but may not silently redefine another owner's contract. Explicit supersession is required when a later accepted artifact replaces an earlier rule within the same responsibility.

## Status vocabulary

Technical specifications may use:

- **Accepted** — required when applicable unless explicitly superseded.
- **Provisional** — usable now with an explicit reassessment trigger.
- **Open** — unresolved before the named boundary.
- **Deferred** — intentionally postponed.
- **Rejected** — considered and not permitted under stated conditions.

## Navigation

This list is navigation only and never implies live activation, completion, or behavior validation.

- [`UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md) — accepted stable project-wide trust, evidence, validation, authority, representation, and failure invariants.
- [`UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md) — accepted automation-generality requirements preventing fixture-specific/manual interpretation from being promoted to product capability.
- [`UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`](UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md) — accepted project-wide **engineering standard** for naming and terminology clarity; stored here for discoverability but not a system-behavior contract.

Historical technical contracts that are no longer part of the active normative surface belong under `../../archive/` or dated evidence with an explicit non-controlling status, rather than remaining embedded in active specifications solely for traceability.

Do not add labels such as **current specification**, **active specification**, or **next specification** here. Live project position belongs only in `../../MEMORY.md`.
