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
| Architecture-status audit | `M2-ENTRY-01` passed; retained files are historical proposals only |
| Accepted implementation | None; no source or tests exist yet |
| Accepted architecture | None |
| Repository role | Documentation, memory, learning, planning, and authorized implementation home |
| Exact next action | Close the integrated pre-code reasoning gate, compare the three temporary layout options, and record Ali's selected layout before creating source files |

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
| What controls the 90-day route, capacity, gates, and capability requirements? | Canonical Career controls under [`docs/program/career/`](docs/program/career/) |
| What product and capability progress has actually been demonstrated? | [`Career/tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md`](https://github.com/motafegh/Career/blob/main/tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md) |
| What behavior is accepted and executable? | Accepted source code, observed execution, and tests |
| Where did the local Career snapshot come from? | [`docs/program/SOURCE.md`](docs/program/SOURCE.md) |
| What architecture is accepted? | Accepted decision records; currently none. Files under `docs/architecture/` are historical proposals only. |

The Career evidence and progress tracker is the **single general product-progress and capability tracker**. Do not create a second general tracker in UpgradePilot. A separate technical inventory is justified only when it measures a distinct engineering concern—such as test coverage, case inventory, or experiment status—and does not duplicate the canonical tracker.

Accepted learning artifacts belong on `main`; there is no permanent learning branch. Short-lived branches may isolate unfinished session, feature, experiment, or repair work. Create subdirectories only when real artifacts require them.

## Start here

A new contributor or AI assistant should read only what the task requires, beginning with:

1. [`AGENTS.md`](AGENTS.md) — stable repository-wide operating instructions;
2. [`MEMORY.md`](MEMORY.md) — compact latest project state and exact next action;
3. [`LEARNING-PREFERENCES.md`](LEARNING-PREFERENCES.md) — stable teaching, pacing, assessment, and learner-ownership preferences;
4. [`docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md`](docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md) — approved controlling active session;
5. [`working-memory/2026-07-20_M2-S01_case-identity-normalization.md`](working-memory/2026-07-20_M2-S01_case-identity-normalization.md) — active session record;
6. [`learning/concepts/case-identity-validation-and-normalization.md`](learning/concepts/case-identity-validation-and-normalization.md) — concise review note for the current concepts;
7. [`learning/README.md`](learning/README.md) when creating durable learning material;
8. [`plans/README.md`](plans/README.md) when creating a future project-local plan;
9. the minimum relevant canonical Career controls in the snapshot.

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
├── working-memory/
│   ├── README.md
│   ├── 2026-07-20_M2-S01_case-identity-normalization.md
│   └── prior dated session and governance records
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

M1 and the architecture-status audit have closed. M2-S01 is active, with pre-code onboarding in progress. No source or test file may be created until the integrated pre-code gate passes and Ali selects and records a temporary file layout. M2-S01 authorizes only case-identity normalization with its required tests and ownership evidence; it does not authorize restoration of the prior scaffold or broader architecture, acquisition, persistence, recommendation policy, services, containers, cloud, models, or agents.