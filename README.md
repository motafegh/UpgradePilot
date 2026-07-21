# UpgradePilot

UpgradePilot is a 90-day learning-by-building flagship project for creating an evidence-backed dependency-update decision system for maintainers of public Python repositories.

Given a public Python Dependabot pull request, the product is intended to support one bounded maintainer action:

- merge after normal review;
- run targeted checks;
- investigate or block;
- defer; or
- abstain.

It is decision support—not an automatic merge bot, a generic vulnerability scanner, or proof that an update is safe.

## Product boundary

UpgradePilot focuses on:

- public Python repositories;
- Dependabot pull requests;
- evidence acquisition and preservation;
- strict data contracts and explicit evidence states;
- repository/dependency context;
- deterministic recommendation or abstention;
- traceable human-readable and machine-readable reports;
- reproducible evaluation and later bounded experiments.

The project does not treat SemVer, passing CI, merged status, model output, or a single score as safety proof.

## High-level flow

```text
maintainer/operator request
→ acquisition request
→ source acquisition or accepted manual evidence
→ raw source preservation
→ parsing and explicit normalization
→ structural and semantic validation
→ evidence-state classification
→ case/evidence assembly
→ repository/dependency context
→ decision input
→ deterministic recommendation or abstention
→ traceable report
→ persistence, replay, evaluation, and later experiments
```

The stages are delivered incrementally. A conceptual stage is not implemented merely because the specification defines it.

## Current maturity

UpgradePilot is in the early automated-vertical-slice stage.

Accepted project-local controls include:

- an initial Python source/package boundary;
- a core pipeline and contract specification;
- Pydantic v2 for the activated strict runtime application contracts;
- a bounded first trusted-case transformation design.

Early implementation-onboarding artifacts may exist, but acceptance, complete test evidence, and Ali-owned capability remain governed by the canonical Career tracker and actual source/test evidence.

For exact current milestone, gate, capability, blocker, and next controlled responsibility, use the canonical Career tracker referenced by [`docs/program/SOURCE.md`](docs/program/SOURCE.md). Do not use this README as a live tracker.

## Core semantic model

```text
repository + pr_number + base_sha + head_sha
→ PullRequestSnapshotIdentity

dependency + old_version + new_version
→ DependencyChange

changed_files
→ ChangedFileEvidence

all trusted components
→ InitialCaseRecord
```

The flat eight-field dictionary is a provisional manual adapter for the first slice. It is not the eventual public input and not one permanent identity object.

## Source boundary

```text
UpgradePilot/
├── pyproject.toml
├── src/
│   └── upgradepilot/
└── tests/
```

Naming:

- product/repository: `UpgradePilot`;
- distribution/import package: `upgradepilot`;
- source root: `src/upgradepilot/`;
- tests: `tests/`.

This boundary does not pre-create speculative services, persistence layers, deployment systems, or architecture.

## Project-local authority

| Question | Canonical owner |
|---|---|
| What is the product mission, user, supported decision, and boundary? | Canonical Career `UpgradePilot.md` |
| What controls route, capacity, gates, and capability evidence? | Canonical Career controls and tracker |
| What must the system represent and guarantee? | `docs/specifications/` |
| Which consequential mechanism or source boundary is accepted? | `docs/architecture/` |
| What is actually implemented and verified? | Source, tests, commands, and observed outputs |
| What is the concise project-local continuation context? | `MEMORY.md` |
| What happened during material project work? | `working-memory/` |
| Where did the local Career snapshot come from? | `docs/program/SOURCE.md` |
| How should an AI operate in this repository? | `AGENTS.md` |

README is a public orientation and navigation entrypoint. It must not duplicate exact session state, method gates, current commands, or detailed tracker content.

## Start here

Read only what the task requires:

1. [`AGENTS.md`](AGENTS.md);
2. [`MEMORY.md`](MEMORY.md) for concise project-local continuation;
3. [`docs/program/SOURCE.md`](docs/program/SOURCE.md) before relying on the local Career snapshot;
4. the minimum relevant canonical Career tracker/session artifact;
5. [`docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md) for system requirements;
6. [`docs/architecture/README.md`](docs/architecture/README.md) and the applicable accepted ADR for implementation decisions;
7. current source, tests, outputs, and working-memory evidence.

Do not scan every historical proposal or record for an ordinary bounded task.

## Repository layout

```text
UpgradePilot/
├── README.md
├── AGENTS.md
├── LEARNING-PREFERENCES.md
├── MEMORY.md
├── SECURITY.md
├── src/
├── tests/
├── learning/
├── plans/
├── proposals/
├── working-memory/
├── examples/
└── docs/
    ├── specifications/
    ├── architecture/
    └── program/
```

## Claim discipline

- Accepted documentation or ADRs do not establish executable behavior.
- Passing AI-generated tests does not establish Ali-owned capability.
- Product maturity, capability depth, and AI assistance must remain separate.
- Use “production-oriented” unless reliability, security, operation, scale, and support evidence justify a stronger claim.
- Preserve limitations, failures, abstentions, rejected methods, and uncertainty.