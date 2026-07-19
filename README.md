# UpgradePilot

UpgradePilot is a 90-day learning-by-building flagship project for creating an evidence-backed dependency-update decision system for maintainers of public Python repositories.

Given a public Python Dependabot pull request, the eventual product will support one bounded maintainer action:

- merge after normal review;
- run targeted checks;
- investigate or block;
- defer; or
- abstain.

It is decision support—not an automatic merge bot, a generic vulnerability scanner, or proof that an update is safe.

## Current state

| Field | State |
|---|---|
| Program window | 2026-07-20 through 2026-10-17 |
| Current route | R2 — Automated vertical slice |
| Current milestone | M2 — First automated vertical slice |
| Controlling next session | M2-S01 — approved, not started |
| M2-S01 responsibility | Validate and normalize manually supplied case identity without mutating raw input |
| Completed session | UP-S01 on `pydantic/pydantic#13432` |
| M1 recommendation | Run targeted checks for generated Algolia search-record correctness |
| Architecture-status audit | `M2-ENTRY-01` passed; retained files are historical proposals only |
| Accepted implementation | None before M2-S01 execution |
| Accepted architecture | None |
| Repository role | Documentation, memory, and authorized implementation home |
| Exact next action | Start M2-S01 and answer its five pre-code questions before creating source files |

## Important correction and audit result

An earlier AI agent was asked to create a repository skeleton but also generated source code, tests, package configuration, executable examples, CI, and architecture claims. Ali had not learned, directed, reviewed, or owned that implementation.

The executable scaffold was removed from the active tree and remains only in Git history. It must not be restored, repaired, continued, or treated as an implementation baseline automatically.

The retained architecture documents were audited:

- [`docs/architecture/ARCHITECTURE.md`](docs/architecture/ARCHITECTURE.md) is an unreviewed, non-controlling prior AI proposal;
- [`docs/architecture/DECISIONS.md`](docs/architecture/DECISIONS.md) is an unreviewed proposal register;
- no retained proposal is accepted, active, or Ali-owned;
- no package layout, CLI, contract, policy, database, adapter, test strategy, or CI choice was adopted.

Audit evidence:

- [`working-memory/2026-07-19_M2-ENTRY_architecture-status-audit.md`](working-memory/2026-07-19_M2-ENTRY_architecture-status-audit.md)

Future architecture must be derived responsibility by responsibility through the authorized learning and decision process.

## Authority and provenance

The [Career repository](https://github.com/motafegh/Career) remains the canonical authority for the 90-day program, workload, gates, tracker, capability requirements, and approved session plans.

This repository contains a read-only Career snapshot whose exact provenance is recorded in [`docs/program/SOURCE.md`](docs/program/SOURCE.md). The controlling next technical session is [`docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md`](docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md).

## Start here

A new contributor or AI assistant should read:

1. [`AGENTS.md`](AGENTS.md) — stable repository-wide operating instructions;
2. [`MEMORY.md`](MEMORY.md) — compact latest project state and exact next action;
3. [`LEARNING-PREFERENCES.md`](LEARNING-PREFERENCES.md) — stable teaching, pacing, assessment, and learner-ownership preferences;
4. [`docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md`](docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md) — approved controlling next session;
5. the active or most relevant record under [`working-memory/`](working-memory/);
6. [`docs/program/career/governance/EXECUTION_CONTRACT.md`](docs/program/career/governance/EXECUTION_CONTRACT.md);
7. [`docs/program/career/strategy/STRATEGY_AND_SCOPE.md`](docs/program/career/strategy/STRATEGY_AND_SCOPE.md);
8. [`docs/program/career/UpgradePilot.md`](docs/program/career/UpgradePilot.md);
9. the capability, learning, roadmap, milestone, tracker, and session controls linked from the Career snapshot.

## Learning-before-implementation rule

Before accepted source code is written for a responsibility:

1. identify the authorized product responsibility;
2. teach the minimum accurate concepts and boundaries;
3. obtain an informed prediction when useful;
4. let Ali perform or materially direct the learning-critical work;
5. inspect actual output;
6. require an ownership-bearing modification, test, diagnosis, query, comparison, or explanation;
7. record evidence and assistance honestly.

AI-generated implementation does not become progress merely because it exists or passes tests.

## Instruction and memory system

- `AGENTS.md` contains durable, tool-neutral repository operating rules.
- `LEARNING-PREFERENCES.md` contains durable project-specific learning-interaction preferences.
- `MEMORY.md` contains current state only and must remain below 200 lines.
- `working-memory/` contains dated, detailed records updated while work proceeds.
- canonical control documents and trackers outrank all repository instruction and memory files.
- tool-specific instruction files should not duplicate the root contract; add only thin routing shims if a tool demonstrably requires them.

## Current repository layout

```text
UpgradePilot/
├── README.md
├── AGENTS.md
├── LEARNING-PREFERENCES.md
├── MEMORY.md
├── SECURITY.md
├── .gitignore
├── working-memory/
│   ├── README.md
│   ├── 2026-07-19_REPO-AUDIT_premature-scaffold-correction.md
│   ├── 2026-07-19_UP-S01_manual-evidence-investigation.md
│   ├── 2026-07-19_M2-ENTRY_architecture-status-audit.md
│   └── 2026-07-19_REPO-GOV_agent-instructions-and-learning-preferences.md
├── examples/
│   └── README.md
└── docs/
    ├── architecture/          # retained historical proposals; not accepted
    └── program/
        ├── SOURCE.md
        ├── FILES.txt
        └── career/            # read-only Career authority snapshot
```

## Current boundary

M1 and the architecture-status audit have closed. M2-S01 is approved but not started. Do not create source files until its five pre-code questions are answered. M2-S01 authorizes only case-identity normalization with its required tests and ownership evidence; it does not authorize restoration of the prior scaffold or broader architecture, acquisition, persistence, recommendation policy, services, containers, cloud, models, or agents.
