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
| Current route | R2 — First automated vertical slice |
| Current milestone | M2 — First automated vertical slice |
| Active session | M2-S01 — technical-contract correction and representation-method decision |
| Session mode | Green; focused minutes not recorded |
| M1 result | Passed on `pydantic/pydantic#13432` |
| M1 recommendation | Run targeted checks for generated Algolia search-record correctness |
| Active Career plan | `docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md` |
| Controlling amendment | `docs/program/career/plans/UPGRADEPILOT_M2_S01_TECHNICAL_CONTRACT_AMENDMENT.md` |
| Core technical specification | `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md` |
| Active working record | `working-memory/2026-07-20_M2-S01_case-identity-implementation-start.md` |
| Initial source-layout decision | Accepted: `docs/architecture/ADR-0001-initial-python-source-layout.md` |
| Accepted implementation | None; no package metadata, source, tests, installation result, or executable behavior exists yet |
| Accepted architecture | Initial source/package boundary only; representation method and complete internal architecture remain undecided |
| Exact next action | Compare representation/validation methods against the accepted specification, select and record the method, then resume minimum test-first implementation |

## Why the technical contract was added

The governing Career documents correctly define the mission, product boundary, evidence doctrine, route, gates, and learning method. Before implementation, discussion exposed a missing layer between those controls and local code decisions.

The original M2 wording treated these eight values as one case identity:

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

The accepted correction is:

```text
repository + pr_number + base_sha + head_sha
→ PullRequestSnapshotIdentity

dependency + old_version + new_version
→ DependencyChange

changed_files
→ ChangedFileEvidence

all components + preserved raw/manual source reference
→ InitialCaseRecord
```

The flat eight-field dictionary remains a provisional M2 manual adapter. It is not the eventual public product input and not one permanent semantic identity object.

## Core conceptual pipeline

```text
maintainer/operator request
→ acquisition request
→ source acquisition or accepted manual evidence
→ raw source preservation
→ parsing and normalization
→ structural and semantic validation
→ evidence-state classification
→ case assembly
→ repository/dependency context
→ decision input
→ deterministic recommendation or abstention
→ human-readable and machine-readable report
→ persistence and replay
→ evaluation and later experiments
```

The specification defines the contracts and boundaries required to make implementation decisions coherent. It does not authorize implementing every stage now.

Read:

- `docs/specifications/README.md`
- `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`

## Current M2 contract

The provisional manual input still supplies:

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

Current activated rules include:

- required exact fields and types;
- no silent coercion at the trusted manual boundary;
- surrounding-whitespace trimming only for declared strings and paths;
- basic `owner/name` repository form;
- positive integer PR number, excluding booleans;
- full 40-character hexadecimal base/head SHAs;
- non-empty dependency, versions, and changed-file paths;
- different old and new versions;
- raw input and nested mutable values remain unchanged;
- no partial trusted initial case record on adapter failure.

Invalid caller input remains distinct from missing, inaccessible, stale, conflicting, rejected, unsupported, or not-applicable external evidence.

## Open representation decision

Before implementation, compare:

- plain dictionaries plus explicit validation functions;
- `TypedDict` plus runtime validation;
- standard-library dataclasses;
- Pydantic models;
- a justified combination.

The decision must consider runtime validation, strictness/coercion, normalization order, cross-field rules, composition, mutation resistance, structured errors, serialization, contract evolution, persistence separation, dependency/security cost, test clarity, diagnosis, Ali ownership, and reversal path.

A durable external framework or cross-project representation policy requires an ADR. No method has been accepted yet.

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

This establishes a professional source/import boundary. It does not pre-create internal layers, services, persistence, frameworks, or deployment design.

Read:

- `docs/architecture/README.md`
- `docs/architecture/ADR-0001-initial-python-source-layout.md`

## Authority and planning ownership

The Career repository remains canonical for:

- the 90-day route and capacity;
- milestone and session authorization;
- capability requirements;
- assistance and ownership evidence;
- the general progress tracker.

UpgradePilot is canonical for:

- project-level technical specifications;
- detailed project-local technical plans after authorization;
- working memory and durable learning artifacts;
- accepted architecture decisions;
- implementation, tests, and project evidence.

The current M2-S01 Career plan remains active and must be read with its technical-contract amendment. The amendment supersedes only conflicting M2 wording.

## Repository responsibility map

| Question or information | Canonical owner |
|---|---|
| What is UpgradePilot and what is its high-level state? | `README.md` |
| How should an AI agent operate here? | `AGENTS.md` |
| How should learning be taught and assessed? | `LEARNING-PREFERENCES.md` |
| What is true now and what happens next? | `MEMORY.md` |
| What happened during formal work? | `working-memory/` |
| What reusable understanding should remain? | `learning/` |
| What must the system represent and guarantee? | `docs/specifications/` |
| What consequential mechanism or source boundary is accepted? | `docs/architecture/` |
| How should an authorized responsibility be executed? | `plans/` and the active Career plan/amendment |
| Where do unadmitted future ideas live? | `proposals/` |
| What controls route, gates, capacity, and capability evidence? | canonical Career controls under `docs/program/career/` |
| What behavior is actually accepted? | source, observed execution, and tests |
| Where did the Career snapshot come from? | `docs/program/SOURCE.md` |

The Career evidence and progress tracker remains the single general product-progress and capability tracker.

## Start here

Read only what the task requires, beginning with:

1. `AGENTS.md`;
2. `MEMORY.md`;
3. `LEARNING-PREFERENCES.md` for learning-critical work;
4. `docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md`;
5. `docs/program/career/plans/UPGRADEPILOT_M2_S01_TECHNICAL_CONTRACT_AMENDMENT.md`;
6. `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`;
7. `working-memory/2026-07-20_M2-S01_case-identity-implementation-start.md`;
8. `docs/architecture/ADR-0001-initial-python-source-layout.md`;
9. the minimum relevant Career tracker or M1 evidence.

Do not scan every historical record or proposal for an ordinary bounded task.

## Learning-before-implementation rule

Before accepted source code is written for a learning-critical responsibility:

1. identify the authorized product behavior and applicable contract;
2. establish the minimum accurate mental model;
3. compare unfamiliar consequential alternatives before asking Ali to choose;
4. obtain an informed prediction when useful;
5. let Ali perform or materially direct the learning-critical work;
6. inspect actual output or failure;
7. require an ownership-bearing modification, test, diagnosis, query, comparison, or explanation;
8. record evidence and assistance conservatively.

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
    │   └── ADR-0001-initial-python-source-layout.md
    └── program/
        ├── SOURCE.md
        ├── FILES.txt
        └── career/
```

## Current boundary

No implementation method, dependency, package metadata, source code, tests, installation result, or executable behavior has been accepted. M2-S01 is paused at the representation-method decision, not at an artificial prohibition against frameworks. The next step is to compare candidate methods against the accepted technical contract and then resume the smallest coherent test-first implementation.
