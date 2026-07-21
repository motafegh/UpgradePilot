# UpgradePilot

UpgradePilot is a 90-day learning-by-building flagship project for creating an evidence-backed dependency-update decision system for maintainers of public Python repositories.

Given a public Python Dependabot pull request, the eventual product supports one bounded maintainer action:

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
| Current route | R2 — First automated vertical slice |
| Current milestone | M2 — First automated vertical slice |
| Active session | M2-S01 — Pydantic implementation onboarding |
| Session mode | Green; focused minutes not recorded |
| M1 result | Passed on `pydantic/pydantic#13432` |
| M1 recommendation | Run targeted checks for generated Algolia search-record correctness |
| Active Career plan | `docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md` |
| Controlling amendment | `docs/program/career/plans/UPGRADEPILOT_M2_S01_TECHNICAL_CONTRACT_AMENDMENT.md` |
| Core technical specification | `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md` |
| Source-layout decision | `docs/architecture/ADR-0001-initial-python-source-layout.md` |
| Runtime-contract decision | `docs/architecture/ADR-0002-pydantic-runtime-contract-models.md` |
| Active working record | `working-memory/2026-07-20_M2-S01_case-identity-implementation-start.md` |
| Accepted implementation | None; no package metadata, installed dependency, source, tests, import proof, or executable behavior yet |
| Accepted architecture | Source/package boundary plus bounded Pydantic runtime-contract policy; complete internal architecture remains undecided |
| Exact next action | Learn the minimum Pydantic v2 concepts, create the reviewed package boundary/dependency, verify installation/import, and write the valid nested-contract test first |

## Core semantic correction

The original M2 wording treated eight values as one case identity. The accepted model is:

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

The flat eight-field dictionary remains a provisional M2 manual adapter. It is not the eventual public product input and not one permanent semantic identity object.

## Core conceptual pipeline

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
→ human-readable and machine-readable report
→ persistence and replay
→ evaluation and later experiments
```

The specification defines the contracts required to make implementation decisions coherent. It does not authorize implementing every stage now.

Read:

- `docs/specifications/README.md`
- `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`

## Accepted Pydantic decision

ADR-0002 adopts Pydantic v2 for strict runtime boundary and trusted application contracts beginning with M2 and the corresponding M3 path.

```text
raw manual/external source data
→ preserve raw form
→ ManualCaseInput
→ explicit adapter/transformation
→ PullRequestSnapshotIdentity
→ DependencyChange
→ ChangedFileEvidence
→ InitialCaseRecord
```

Accepted policies:

- raw payloads remain plain source data or raw-source records;
- validated contracts use strict Pydantic v2 behavior;
- undeclared fields are rejected in the activated contracts;
- trusted models are frozen;
- trusted changed-file paths use `tuple[str, ...]`;
- flat-to-nested assembly remains a named, directly tested adapter;
- Pydantic validation errors remain internal during M2;
- application contracts are not database rows or permanent public report schemas;
- Pydantic v3 requires reassessment.

Read:

- `docs/architecture/README.md`
- `docs/architecture/ADR-0002-pydantic-runtime-contract-models.md`

## Current M2 contract

The provisional manual input supplies:

```text
repository
pr_number
base_sha
head_sha
dependency
old_version
new_version
changed_files
```

Activated rules:

- required exact fields and types;
- no silent coercion at the validated boundary;
- surrounding-whitespace trimming for declared strings and paths;
- valid SHAs canonicalized to lowercase;
- basic `owner/name` repository form;
- positive integer PR number, excluding booleans;
- full 40-character hexadecimal base/head SHAs;
- non-empty dependency and versions;
- old/new versions differ;
- non-empty raw changed-file list;
- normalized paths are non-empty and unique;
- source path order is preserved;
- trusted paths become a tuple;
- raw input and its list remain unchanged;
- no mutable alias from raw list to trusted record;
- no partial trusted record on validation failure.

Invalid caller input remains distinct from missing, inaccessible, stale, conflicting, rejected, unsupported, or not-applicable external evidence.

## Accepted source boundary

```text
UpgradePilot/
├── pyproject.toml             # not created yet
├── src/
│   └── upgradepilot/          # not created yet
└── tests/                     # not created yet
```

Naming:

```text
Product and repository:  UpgradePilot
Distribution package:    upgradepilot
Import package:          upgradepilot
Source root:              src/upgradepilot/
Test root:                tests/
```

This establishes a professional source/import boundary. It does not pre-create speculative source layers, services, persistence, or deployment architecture.

Read:

- `docs/architecture/ADR-0001-initial-python-source-layout.md`

## Authority and ownership

The Career repository remains canonical for route, capacity, milestone/session authorization, capability requirements, assistance/ownership evidence, and the general progress tracker.

UpgradePilot is canonical for project-level technical specifications, accepted architecture decisions, detailed project-local plans after authorization, working memory, learning artifacts, implementation, tests, and project evidence.

The current Career M2 plan remains active and must be read with its amendment. ADR-0002 closes the representation-method decision but does not establish working behavior or capability ownership.

## Repository responsibility map

| Question | Canonical owner |
|---|---|
| What is UpgradePilot and its high-level state? | `README.md` |
| How should an AI agent operate here? | `AGENTS.md` |
| How should learning be taught and assessed? | `LEARNING-PREFERENCES.md` |
| What is true now and what happens next? | `MEMORY.md` |
| What happened during formal work? | `working-memory/` |
| What reusable understanding should remain? | `learning/` |
| What must the system represent and guarantee? | `docs/specifications/` |
| Which consequential mechanism or source boundary is accepted? | `docs/architecture/` |
| How should authorized work execute? | active Career plan/amendment and `plans/` |
| What controls route, gates, capacity, and capability evidence? | canonical Career controls under `docs/program/career/` |
| What behavior is actually accepted? | source, observed execution, and tests |
| Where did the Career snapshot come from? | `docs/program/SOURCE.md` |

The Career tracker remains the single general product-progress and capability tracker.

## Start here

Read only what the task requires:

1. `AGENTS.md`;
2. `MEMORY.md`;
3. `LEARNING-PREFERENCES.md` for learning-critical work;
4. `docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md`;
5. `docs/program/career/plans/UPGRADEPILOT_M2_S01_TECHNICAL_CONTRACT_AMENDMENT.md`;
6. `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`;
7. `docs/architecture/ADR-0001-initial-python-source-layout.md`;
8. `docs/architecture/ADR-0002-pydantic-runtime-contract-models.md`;
9. `working-memory/2026-07-20_M2-S01_case-identity-implementation-start.md`;
10. the minimum relevant Career tracker or M1 evidence.

Do not scan every historical record or proposal for an ordinary bounded task.

## Learning-before-implementation rule

Before accepted source code is written for a learning-critical responsibility:

1. identify the authorized behavior and applicable contracts/ADRs;
2. establish the minimum accurate mental model;
3. obtain an informed prediction when useful;
4. let Ali perform or materially direct the learning-critical work;
5. inspect actual output or failure;
6. require an ownership-bearing modification, test, diagnosis, query, comparison, or explanation;
7. record evidence and assistance conservatively.

AI-generated implementation or professional-looking documentation does not establish capability by itself.

## Current repository layout

```text
UpgradePilot/
├── README.md
├── AGENTS.md
├── LEARNING-PREFERENCES.md
├── MEMORY.md
├── SECURITY.md
├── learning/
├── plans/
├── proposals/
├── working-memory/
├── examples/
└── docs/
    ├── specifications/
    │   ├── README.md
    │   └── UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md
    ├── architecture/
    │   ├── README.md
    │   ├── ADR-0001-initial-python-source-layout.md
    │   └── ADR-0002-pydantic-runtime-contract-models.md
    └── program/
        ├── SOURCE.md
        ├── FILES.txt
        └── career/
```

## Current boundary

Pydantic v2 is accepted as the runtime-contract method, but no dependency has been installed and no model, package, test, import result, or executable behavior exists. M2-S01 now proceeds through minimum Pydantic learning, reviewed package setup, editable installation/import verification, and the valid nested-contract test before implementation.