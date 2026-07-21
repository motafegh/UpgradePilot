# UpgradePilot

UpgradePilot is a 90-day learning-by-building flagship project for creating an evidence-backed dependency-update decision system for maintainers of public Python repositories.

Given a public Python Dependabot pull request, the product supports one bounded maintainer action:

- merge after normal review;
- run targeted checks;
- investigate or block;
- defer; or
- abstain.

It is decision support—not an automatic merge bot, generic vulnerability scanner, or proof that an update is safe.

The stable mission, user, product boundary, evidence doctrine, admission rules, termination conditions, and claim limits are controlled by [`PROJECT_CHARTER.md`](PROJECT_CHARTER.md).

## Product boundary

UpgradePilot focuses on:

- public Python repositories and Dependabot pull requests;
- lawful evidence acquisition and preservation;
- strict data contracts and explicit evidence states;
- repository and dependency context;
- deterministic recommendation or abstention;
- traceable human-readable and machine-readable reports;
- reproducible evaluation and later bounded experiments.

SemVer, passing CI, merged status, model output, or a single score is never treated as safety proof.

## High-level flow

```text
maintainer request
→ evidence acquisition or accepted manual evidence
→ raw preservation
→ parsing and explicit normalization
→ structural and semantic validation
→ evidence-state classification
→ repository/dependency context
→ deterministic recommendation or abstention
→ traceable report
→ persistence, replay, evaluation, and admitted experiments
```

Stages are delivered incrementally. A conceptual stage is not implemented merely because it is named.

## Project ownership

UpgradePilot is self-contained for ordinary project work.

| Responsibility | Owner |
|---|---|
| Stable mission, user, boundary, and claim limits | `PROJECT_CHARTER.md` |
| Public orientation and navigation | `README.md` |
| Learning, execution, blockers, and assistance fading | `OPERATING_GUIDE.md` |
| Route, capacity, milestones, and project gates | `plans/UPGRADEPILOT_90_DAY_PLAN.md` |
| Current bounded responsibility | Current file under `plans/` |
| Concise current continuation | `MEMORY.md` |
| Required technical behavior and invariants | `docs/specifications/` |
| Accepted consequential methods | `docs/architecture/` |
| Actual implementation truth | Source, tests, commands, outputs, and environment |
| Detailed material-work evidence | `working-memory/` |

Career contains only durable career/program state and formal capability assessments. It is not updated for ordinary project progress. Ali explicitly initiates a Career review when that state should be reconsidered or refreshed.

## Current stage

UpgradePilot is in M2, the first automated vertical-slice stage.

The current project-local responsibility is defined by:

- [`plans/M2_S01_INITIAL_TRUSTED_CASE_PLAN.md`](plans/M2_S01_INITIAL_TRUSTED_CASE_PLAN.md);
- [`MEMORY.md`](MEMORY.md);
- current source, tests, environment, and working evidence.

The current trusted semantic structure is:

```text
PullRequestSnapshotIdentity
+ DependencyChange
+ ChangedFileEvidence
→ InitialCaseRecord
```

The flat eight-field mapping is a provisional M2 adapter, not the eventual public input or one permanent identity object.

## Source boundary

```text
UpgradePilot/
├── pyproject.toml
├── src/
│   └── upgradepilot/
└── tests/
```

- product/repository: `UpgradePilot`;
- distribution/import package: `upgradepilot`;
- source root: `src/upgradepilot/`;
- tests: `tests/`.

This boundary does not pre-create speculative services, persistence layers, deployment systems, or internal package hierarchies.

## Start here

For ordinary work, read only what is necessary:

1. [`AGENTS.md`](AGENTS.md);
2. [`MEMORY.md`](MEMORY.md);
3. the current project plan;
4. [`OPERATING_GUIDE.md`](OPERATING_GUIDE.md) when process or learning guidance matters;
5. [`PROJECT_CHARTER.md`](PROJECT_CHARTER.md) when product scope or admission is material;
6. the applicable specification or ADR;
7. current source, tests, outputs, and evidence.

Do not scan historical proposals or Career documents for a bounded implementation task.

## Repository layout

```text
UpgradePilot/
├── README.md
├── PROJECT_CHARTER.md
├── AGENTS.md
├── OPERATING_GUIDE.md
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
    └── architecture/
```

## Claim discipline

- Accepted documentation or ADRs do not establish executable behavior.
- Passing AI-generated tests does not establish Ali-owned capability.
- Product maturity, capability depth, and AI assistance remain separate.
- Use “production-oriented” unless reliability, security, operation, scale, and support evidence justify a stronger claim.
- Preserve limitations, failures, abstentions, rejected methods, and uncertainty.
