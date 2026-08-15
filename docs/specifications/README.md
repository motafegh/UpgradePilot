# Technical Specifications and Engineering Standards

This directory contains accepted project-level technical specifications plus the retained project-wide naming/terminology engineering standard.

For repository-wide documentation ownership and decision-promotion navigation, start at [`../README.md`](../README.md).

## Technical specification responsibility

A technical specification states **what admitted system behavior must represent or guarantee** independently of implementation mechanism. It may define:

- conceptual pipeline and information boundaries;
- required/optional/conditional/unavailable data semantics;
- invariants;
- validation, authority, failure, degradation, and abstention behavior;
- accepted product decision/reasoning semantics;
- criteria that later architecture and implementation must satisfy.

A technical specification does not by itself select a Python framework, dependency, database, service boundary, directory hierarchy, provider, deployment mechanism, live project position, or execution sequence.

## Responsibility ownership across artifacts

- `../../PROJECT_CHARTER.md` → stable mission, user, supported boundary, evidence doctrine, claim limits.
- `../../plans/UPGRADEPILOT_90_DAY_PLAN.md` → stable route and gate definitions.
- `../../MEMORY.md` → sole live project position and continuation.
- technical specifications here → framework-independent required behavior/invariants and accepted product decision semantics.
- `../architecture/` → accepted consequential mechanisms/structural choices.
- `../../plans/` → bounded execution sequence, proof, and stop lines.
- source/tests/commands/outputs/environment → implemented truth.
- `../../working-memory/` → dated evidence/reasoning and historical decision trail.
- `../../proposals/` → unadmitted future ideas and non-controlling horizons.

Do not resolve disagreements through a generic total ranking after the user/local-instruction layer. Resolve them through the owner of the disputed responsibility. For example:

- a specification controls required behavior/semantics;
- an ADR controls the selected consequential method used to satisfy it;
- a plan coordinates implementation/proof of that method;
- source/tests establish what is actually implemented.

A different artifact may add detail within its own responsibility but may not silently redefine another owner's contract. Explicit supersession is required when a later accepted artifact replaces an earlier rule within the same responsibility.

## Promotion from dated reasoning

Dated working-memory, audits, simulations, and proposals may contain important reasoning or provisional decisions. When a conclusion becomes stable, accepted, reusable, and expected to guide unrelated future sessions, promote it to the normal durable owner for its responsibility rather than requiring future sessions to reconstruct the rule from history.

See [`../README.md`](../README.md) for the full promotion lifecycle.

Historical records remain unchanged unless a broken link or factual corruption requires repair. Canonical artifacts should preserve provenance links to the important records that justified the accepted rule.

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
- [`UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md) — accepted technical impact-candidate, applicability, coverage/negative-inference, discriminating-investigation, result-feedback, stopping, and later-synthesis-boundary semantics.
- [`UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md) — accepted automation-generality requirements preventing fixture-specific/manual interpretation from being promoted to product capability.
- [`UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`](UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md) — accepted project-wide **engineering standard** for naming and terminology clarity; stored here for discoverability but not a system-behavior contract.

The intended split is:

```text
CORE PIPELINE + CONTRACT
→ stable trust / provenance / representation / failure invariants

PRODUCT DECISION MODEL
→ candidate / applicability / coverage / investigation / stopping semantics

MINIMUM USEFUL GENERALITY
→ acceptance standard for variable-input automated responsibilities

NAMING CLARITY
→ terminology and naming engineering standard
```

Historical technical contracts that are no longer part of the active normative surface belong under `../../archive/` or dated evidence with an explicit non-controlling status, rather than remaining embedded in active specifications solely for traceability.

Do not add labels such as **current specification**, **active specification**, or **next specification** here. Live project position belongs only in `../../MEMORY.md`.
