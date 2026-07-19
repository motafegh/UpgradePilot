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
| Current route | R2 — Automated vertical slice entry preparation |
| Current milestone | M2 — First automated vertical slice — Ready, not activated |
| Completed session | UP-S01 on `pydantic/pydantic#13432` |
| Canonical M1 report | `Career/tracking/evidence/UP-S01_pydantic-13432_manual-evidence-report.md` |
| M1 recommendation | Run targeted checks for generated Algolia search-record correctness |
| Architecture-status audit | `M2-ENTRY-01` passed |
| Career snapshot | Refreshed from Career commit `4237a0f422c60b0faad236c00c536dca4dfe98b6` |
| Accepted implementation | None |
| Accepted architecture | None |
| Repository role | Documentation, memory, and future authorized implementation home |
| Exact next action | Define and activate the first bounded M2 learning/implementation session using the completed Pydantic case |

## Important correction and retained proposals

An earlier AI agent was asked to create a repository skeleton but also generated source code, tests, package configuration, executable examples, CI, and architecture claims. Ali had not learned, directed, reviewed, or owned that implementation.

The executable scaffold was removed from the active tree. It remains available through Git history but must not be restored, repaired, continued, or treated as a baseline automatically.

The architecture-status audit removed or superseded false `Accepted`, `Active`, and Ali-decision-owner claims:

- `docs/architecture/ARCHITECTURE.md` is an unreviewed prior AI proposal;
- `docs/architecture/DECISIONS.md` is an unreviewed proposal register;
- neither file controls implementation;
- none of the retained proposals is accepted or Ali-owned.

Future architecture must be derived responsibility by responsibility through the authorized learning and decision process.

## Authority and provenance

The [Career repository](https://github.com/motafegh/Career) remains the canonical authority for the 90-day program, workload, gates, tracker, capability requirements, and approved session plans.

This repository contains a read-only snapshot of active UpgradePilot control documents from Career commit `4237a0f422c60b0faad236c00c536dca4dfe98b6`. See [snapshot provenance](docs/program/SOURCE.md) and the exact [mirrored file list](docs/program/FILES.txt).

The canonical M1 evidence report remains in Career and is linked from the mirrored tracker. It is not duplicated here because `tracking/evidence/` is not part of the fixed snapshot list.

## Start here

A new contributor or AI assistant should read:

1. [`AGENTS.md`](AGENTS.md) — stable repository-wide operating instructions;
2. [`MEMORY.md`](MEMORY.md) — compact latest project state and exact next action;
3. [`LEARNING-PREFERENCES.md`](LEARNING-PREFERENCES.md) — stable teaching, pacing, assessment, and learner-ownership rules;
4. the active or most relevant record under [`working-memory/`](working-memory/);
5. [`docs/program/career/governance/EXECUTION_CONTRACT.md`](docs/program/career/governance/EXECUTION_CONTRACT.md);
6. [`docs/program/career/strategy/STRATEGY_AND_SCOPE.md`](docs/program/career/strategy/STRATEGY_AND_SCOPE.md);
7. [`docs/program/career/UpgradePilot.md`](docs/program/career/UpgradePilot.md);
8. the capability, learning, roadmap, milestone, tracker, and session controls linked from the Career snapshot.

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
- `LEARNING-PREFERENCES.md` contains durable learning-interaction rules.
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
    ├── architecture/          # retained unreviewed proposals; non-controlling
    └── program/
        ├── SOURCE.md
        ├── FILES.txt
        └── career/            # read-only Career authority snapshot
```

## Current boundary

The architecture-status audit has closed, but no bounded M2 implementation session is active. Until one is explicitly defined and authorized, do not add or restore source code, tests, package metadata, executable examples, CI, schemas, architecture adoption, acquisition, persistence, models, services, queues, containers, Kubernetes, cloud, or agents.
