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
| Repository role | Documentation, memory, learning, planning, and authorized implementation home |
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

## Authority and planning ownership

The [Career repository](https://github.com/motafegh/Career) remains canonical for the 90-day route, monthly and weekly priorities, daily capacity, milestone gates, cross-project allocation, capability requirements, and evidence tracking.

UpgradePilot is canonical for future detailed project-local technical plans, learning artifacts, working records, implementation, tests, and project evidence inside an authorized boundary.

The current M2-S01 plan remains a Career-owned transition artifact and is mirrored at [`docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md`](docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md). Do not move or duplicate it during M2-S01. After this session, Career should authorize the bounded objective and gate, then link to one detailed plan under [`plans/`](plans/).

The read-only Career snapshot provenance is recorded in [`docs/program/SOURCE.md`](docs/program/SOURCE.md).

## Learning and planning environment

- [`learning/`](learning/) stores durable educational material worth revisiting. It is not a transcript archive.
- [`plans/`](plans/) stores future detailed project-local technical plans when a separate plan is justified.
- [`working-memory/`](working-memory/) records what happened during formal sessions and material work.
- Accepted learning artifacts belong on `main`; there is no permanent learning branch.
- Short-lived branches may isolate unfinished session, feature, experiment, or repair work.
- Subdirectories are created only when real artifacts require them.

## Start here

A new contributor or AI assistant should read only what the task requires, beginning with:

1. [`AGENTS.md`](AGENTS.md) — stable repository-wide operating instructions;
2. [`MEMORY.md`](MEMORY.md) — compact latest project state and exact next action;
3. [`LEARNING-PREFERENCES.md`](LEARNING-PREFERENCES.md) — stable teaching, pacing, assessment, and learner-ownership preferences;
4. [`docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md`](docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md) — approved controlling next session;
5. the active record under [`working-memory/`](working-memory/), when one exists;
6. [`learning/README.md`](learning/README.md) when creating durable learning material;
7. [`plans/README.md`](plans/README.md) when creating a future project-local plan;
8. the minimum relevant canonical Career controls in the snapshot.

Do not scan every historical record or control file for a lightweight question.

## Learning-before-implementation rule

Before accepted source code is written for a learning-critical responsibility:

1. identify the authorized product responsibility;
2. teach the minimum accurate concepts and boundaries;
3. obtain an informed prediction when useful;
4. let Ali perform or materially direct the learning-critical work;
5. inspect actual output;
6. require an ownership-bearing modification, test, diagnosis, query, comparison, or explanation;
7. record evidence and assistance at the level justified by the work.

AI-generated implementation does not become progress merely because it exists or passes tests.

## Instruction, memory, and artifact system

- `AGENTS.md` contains durable, tool-neutral repository operating rules.
- `LEARNING-PREFERENCES.md` contains durable project-specific learning-interaction preferences.
- `MEMORY.md` contains current state only and must remain below 200 lines.
- `working-memory/` contains dated detailed records for formal sessions and material work.
- `learning/` contains durable educational artifacts.
- `plans/` contains future detailed project-local technical plans.
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
├── learning/
│   └── README.md
├── plans/
│   └── README.md
├── working-memory/
│   ├── README.md
│   └── dated session and governance records
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