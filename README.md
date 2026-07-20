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
| Active session | M2-S01 — pre-code onboarding in progress |
| Session mode | Green; focused minutes not recorded |
| M2-S01 responsibility | Validate and normalize manually supplied case identity without mutating raw input |
| Active working record | [`working-memory/2026-07-20_M2-S01_case-identity-normalization.md`](working-memory/2026-07-20_M2-S01_case-identity-normalization.md) |
| Concise learning note | [`learning/concepts/case-identity-validation-and-normalization.md`](learning/concepts/case-identity-validation-and-normalization.md) |
| Completed session | UP-S01 on `pydantic/pydantic#13432` |
| M1 recommendation | Run targeted checks for generated Algolia search-record correctness |
| M2-entry audit | Passed; former AI-generated architecture and scaffold have no current authority |
| Initial source-layout decision | Accepted: [`docs/architecture/ADR-0001-initial-python-source-layout.md`](docs/architecture/ADR-0001-initial-python-source-layout.md) |
| Accepted implementation | None; no `pyproject.toml`, source, tests, installation result, or executable behavior exists yet |
| Accepted architecture | Initial source/package boundary only; complete internal architecture remains undecided |
| Repository role | Documentation, memory, learning, planning, proposal preservation, architecture decisions, and authorized implementation home |
| Exact next action | Close the integrated behavior gate, then create the minimal installable package boundary and write the valid test first |

## Architecture correction and current decision

An earlier AI agent generated source code, tests, package configuration, executable examples, CI, and architecture claims before Ali had learned, directed, reviewed, or owned those decisions.

The executable scaffold was removed from the active tree and remains only in Git history. The former AI-generated architecture files were audited and then removed from the active tree after a fresh source-layout decision replaced the only boundary currently needed.

Historical correction evidence remains at:

- [`working-memory/2026-07-19_M2-ENTRY_architecture-status-audit.md`](working-memory/2026-07-19_M2-ENTRY_architecture-status-audit.md)
- Git history

The accepted decision is now:

```text
UpgradePilot/                  # repository and product workspace
├── pyproject.toml             # minimum project/install metadata; not created yet
├── src/
│   └── upgradepilot/          # Python import package; not created yet
│       ├── __init__.py
│       └── case_identity.py
└── tests/
    └── test_case_identity.py
```

Naming:

```text
Product and repository:  UpgradePilot
Distribution package:    upgradepilot
Import package:          upgradepilot
First module:            upgradepilot.case_identity
```

This decision establishes a professional source and import boundary. It does not pre-create or accept a full layered architecture, CLI, adapters, services, persistence, framework, or deployment design.

Read:

- [`docs/architecture/README.md`](docs/architecture/README.md)
- [`docs/architecture/ADR-0001-initial-python-source-layout.md`](docs/architecture/ADR-0001-initial-python-source-layout.md)

## Authority and planning ownership

The [Career repository](https://github.com/motafegh/Career) remains canonical for the 90-day route, monthly and weekly priorities, daily capacity, milestone gates, cross-project allocation, capability requirements, and evidence tracking.

UpgradePilot is canonical for detailed project-local technical plans, learning artifacts, working records, accepted architecture decisions, implementation, tests, and project evidence inside an authorized boundary.

The current M2-S01 plan remains a Career-owned transition artifact and is mirrored at [`docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md`](docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md). Do not move or duplicate it during M2-S01. After this session, Career should authorize the bounded objective and gate, then link to one detailed plan under [`plans/`](plans/).

The read-only Career snapshot provenance is recorded in [`docs/program/SOURCE.md`](docs/program/SOURCE.md).

Substantial ambitious ideas that are not yet admitted belong under [`proposals/`](proposals/). A proposal preserves thinking; it does not authorize work or alter controlling scope.

## Repository responsibility map

This table is a routing reference, not another authority. The linked owner controls its subject if a summary here ever becomes stale.

| Question or information | Canonical owner |
|---|---|
| What is UpgradePilot and what is its high-level state? | [`README.md`](README.md) |
| How should an AI agent operate in this repository? | [`AGENTS.md`](AGENTS.md) |
| How should learning be taught, paced, and assessed? | [`LEARNING-PREFERENCES.md`](LEARNING-PREFERENCES.md) |
| What is true right now and what happens next? | [`MEMORY.md`](MEMORY.md) |
| What happened during a formal session or material work item? | [`working-memory/`](working-memory/) |
| What reusable understanding should be retained? | [`learning/`](learning/) |
| How should a bounded technical responsibility be executed? | [`plans/`](plans/) and the active authorized plan |
| Where do ambitious future ideas and unadmitted designs live? | [`proposals/`](proposals/) |
| What source/package or architecture decisions are accepted? | [`docs/architecture/`](docs/architecture/) |
| What controls the 90-day route, capacity, gates, and capability requirements? | Canonical Career controls under [`docs/program/career/`](docs/program/career/) |
| What product and capability progress has actually been demonstrated? | [`Career/tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md`](https://github.com/motafegh/Career/blob/main/tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md) |
| What behavior is accepted and executable? | Accepted source code, observed execution, and tests |
| Where did the local Career snapshot come from? | [`docs/program/SOURCE.md`](docs/program/SOURCE.md) |

The Career evidence and progress tracker is the **single general product-progress and capability tracker**. Do not create a second general tracker in UpgradePilot. A separate technical inventory is justified only when it measures a distinct engineering concern and does not duplicate the canonical tracker.

Accepted learning artifacts and architecture decisions belong on `main`; there is no permanent learning or architecture branch. Short-lived branches may isolate unfinished session, feature, experiment, proposal, architecture-decision, or repair work. Create subdirectories only when real artifacts or implemented responsibilities require them.

## Start here

A new contributor or AI assistant should read only what the task requires, beginning with:

1. [`AGENTS.md`](AGENTS.md) — stable repository-wide operating instructions;
2. [`MEMORY.md`](MEMORY.md) — compact latest project state and exact next action;
3. [`LEARNING-PREFERENCES.md`](LEARNING-PREFERENCES.md) — stable teaching, pacing, assessment, and learner-ownership preferences;
4. [`docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md`](docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md) — approved controlling active session;
5. [`working-memory/2026-07-20_M2-S01_case-identity-normalization.md`](working-memory/2026-07-20_M2-S01_case-identity-normalization.md) — active session record;
6. [`docs/architecture/ADR-0001-initial-python-source-layout.md`](docs/architecture/ADR-0001-initial-python-source-layout.md) — accepted source boundary;
7. [`learning/concepts/case-identity-validation-and-normalization.md`](learning/concepts/case-identity-validation-and-normalization.md) — concise review note for the current concepts;
8. [`learning/README.md`](learning/README.md) when creating durable learning material;
9. [`plans/README.md`](plans/README.md) when creating a future project-local plan;
10. [`proposals/README.md`](proposals/README.md) only when preserving or reviewing unadmitted future ideas;
11. the minimum relevant canonical Career controls in the snapshot.

Do not scan every historical record, proposal, or control file for a lightweight question.

## Learning-before-implementation rule

Before accepted source code is written for a learning-critical responsibility:

1. identify the authorized product responsibility;
2. teach the minimum accurate concepts and boundaries;
3. obtain an informed prediction when useful;
4. let Ali perform or materially direct the learning-critical work;
5. inspect actual output;
6. require an ownership-bearing modification, test, diagnosis, query, comparison, or explanation;
7. record evidence and assistance at the level justified by the work.

AI-generated implementation or accepted design documentation does not become capability merely because it exists or looks professional.

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
│   ├── README.md
│   └── concepts/
│       └── case-identity-validation-and-normalization.md
├── plans/
│   └── README.md
├── proposals/
│   ├── README.md
│   └── 2026-07-20_UPGRADEPILOT_PRODUCT_AMBITION_AND_ENHANCEMENT_PROPOSAL.md
├── working-memory/
│   ├── README.md
│   ├── 2026-07-20_M2-S01_case-identity-normalization.md
│   └── prior dated session and governance records
├── examples/
│   └── README.md
└── docs/
    ├── architecture/
    │   ├── README.md
    │   └── ADR-0001-initial-python-source-layout.md
    └── program/
        ├── SOURCE.md
        ├── FILES.txt
        └── career/            # read-only Career authority snapshot
```

The accepted but not-yet-created first implementation paths are:

```text
pyproject.toml
src/upgradepilot/__init__.py
src/upgradepilot/case_identity.py
tests/test_case_identity.py
```

## Current boundary

M1, the architecture-status audit, and the initial source-layout decision have closed. M2-S01 remains active, with the integrated behavior gate open. No `pyproject.toml`, package directory, source module, or test file may be created until Ali completes that gate. After it passes, M2-S01 authorizes only the minimum installable package boundary and case-identity normalization behavior required by the controlling plan. It does not authorize broader acquisition, evidence contracts, persistence, recommendation policy, report generation, CLI, services, containers, cloud, models, graphs, agents, or speculative internal source layers.