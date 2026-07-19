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
| Career snapshot | Refreshed from Career commit `4237a0f422c60b0faad236c00c536dca4dfe98b6` |
| Accepted implementation | None |
| Accepted architecture | None |
| Repository role | Documentation, memory, and future implementation home |
| Exact next action | Audit retained `docs/architecture/` claims and repository state, then authorize one bounded M2 session without restoring the removed scaffold |

## Important correction

An earlier AI agent was asked to create a repository skeleton but also generated source code, tests, package configuration, executable examples, CI, and architecture claims. Ali had not learned, directed, reviewed, or owned that implementation.

The executable scaffold has therefore been removed from the active tree. It remains available through Git history but must not be restored, repaired, or continued automatically.

The Markdown files under `docs/architecture/` are retained for a dedicated audit. They are not currently accepted, controlling, or evidence of Ali's technical ownership. Their internal `Accepted`, `Active`, and decision-owner statements conflict with the repository entry points and are the current M2-entry blocker.

## Authority and provenance

The [Career repository](https://github.com/motafegh/Career) remains the canonical authority for the 90-day program, workload, gates, tracker, and approved session plans.

This repository contains a read-only snapshot of the active UpgradePilot control documents from Career commit `4237a0f422c60b0faad236c00c536dca4dfe98b6`. See [snapshot provenance](docs/program/SOURCE.md) and the exact [mirrored file list](docs/program/FILES.txt).

The canonical M1 evidence report remains in Career and is linked from the mirrored tracker. It is not duplicated here because `tracking/evidence/` is not part of the fixed snapshot list.

## Start here

A new contributor or AI assistant should read:

1. [`AGENTS.md`](AGENTS.md) — stable repository instructions for AI agents;
2. [`MEMORY.md`](MEMORY.md) — compact latest project state;
3. [`working-memory/2026-07-19_UP-S01_manual-evidence-investigation.md`](working-memory/2026-07-19_UP-S01_manual-evidence-investigation.md) — completed M1 session record;
4. [`working-memory/2026-07-19_REPO-AUDIT_premature-scaffold-correction.md`](working-memory/2026-07-19_REPO-AUDIT_premature-scaffold-correction.md) — scaffold correction evidence;
5. [`docs/program/career/governance/EXECUTION_CONTRACT.md`](docs/program/career/governance/EXECUTION_CONTRACT.md);
6. [`docs/program/career/strategy/STRATEGY_AND_SCOPE.md`](docs/program/career/strategy/STRATEGY_AND_SCOPE.md);
7. [`docs/program/career/UpgradePilot.md`](docs/program/career/UpgradePilot.md);
8. the capability, learning, roadmap, milestone, tracker, and session controls linked from the Career snapshot.

## Learning-before-implementation rule

Before accepted source code is written for a responsibility:

1. identify the authorized product responsibility;
2. teach the minimum required concepts and boundaries;
3. ask Ali to predict representative behavior;
4. let Ali perform or materially direct the work;
5. inspect actual output;
6. require an ownership-bearing modification, test, diagnosis, query, or explanation;
7. record evidence and assistance honestly.

AI-generated implementation does not become progress merely because it exists or passes tests.

## Memory system

- `AGENTS.md` contains stable, length-optimized instructions.
- `MEMORY.md` contains only current state and must always remain below 200 lines.
- `working-memory/` contains dated, detailed session and major-step records that are updated while work proceeds.
- Canonical control documents and trackers outrank all memory files.

## Current repository layout

```text
UpgradePilot/
├── README.md
├── AGENTS.md
├── MEMORY.md
├── SECURITY.md
├── .gitignore
├── working-memory/
│   ├── README.md
│   ├── 2026-07-19_REPO-AUDIT_premature-scaffold-correction.md
│   └── 2026-07-19_UP-S01_manual-evidence-investigation.md
├── examples/
│   └── README.md
└── docs/
    ├── architecture/          # retained; internally conflicting; audit required
    └── program/
        ├── SOURCE.md
        ├── FILES.txt
        └── career/            # read-only Career authority snapshot
```

## Current boundary

M1 has closed, but M2 implementation is not yet active. Until the retained-architecture audit closes and a bounded M2 session is explicitly authorized, do not add or restore source code, tests, package metadata, executable examples, CI, schemas, architecture adoption, acquisition, persistence, models, services, queues, containers, Kubernetes, cloud, or agents.