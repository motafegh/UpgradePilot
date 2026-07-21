# UpgradePilot Current Memory

**Last updated:** 2026-07-21  
**Purpose:** Compact current-state memory for a newly started AI assistant. Keep this file below 200 lines.

## Current control state

- Primary project: UpgradePilot.
- Program window: 2026-07-20 through 2026-10-17.
- Current route/milestone: R2 / M2 — First automated vertical slice.
- M1 / UP-S01: Passed on `pydantic/pydantic#13432`.
- M1 recommendation: run targeted checks for semantic correctness of generated Algolia search records.
- M2-entry architecture-status audit: Passed.
- Initial source-layout decision: Accepted through `docs/architecture/ADR-0001-initial-python-source-layout.md`.
- Core pipeline/contract specification: Accepted through `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`.
- Runtime-contract method: Accepted through `docs/architecture/ADR-0002-pydantic-runtime-contract-models.md`.
- Active Career controls:
  - `docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md`;
  - `docs/program/career/plans/UPGRADEPILOT_M2_S01_TECHNICAL_CONTRACT_AMENDMENT.md`.
- M2-S01 status: Active; first AI-generated implementation draft exists and valid-case testing has begun.
- Mode: Green.
- Focused minutes: not recorded.
- Active working record: `working-memory/2026-07-20_M2-S01_case-identity-implementation-start.md`.
- Earlier M2-S01 record: `working-memory/2026-07-20_M2-S01_case-identity-normalization.md`; superseded history.

## Corrected semantic model

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

The flat eight-field dictionary remains a provisional manual M2 adapter, not the eventual public input or one permanent identity object.

## Accepted conceptual pipeline

```text
maintainer/operator request
→ acquisition request
→ raw source preservation
→ parsing and explicit normalization
→ validation and evidence-state classification
→ case/evidence assembly
→ repository/dependency context
→ deterministic recommendation or abstention
→ human-readable and machine-readable report
→ persistence and replay
→ evaluation and later experiments
```

## Accepted core boundaries

1. Acquisition request is distinct from the complete case record.
2. Snapshot identity contains repository, PR number, base SHA, and head SHA.
3. Dependency change and changed files are separate snapshot-associated facts/evidence.
4. Raw source/input remains separate from validated and trusted representations.
5. Provenance and explicit evidence states are central.
6. Invalid input differs from missing, inaccessible, stale, conflicting, rejected, unsupported, and not-applicable evidence.
7. Trusted contracts do not silently coerce; conversion belongs in an explicit adapter.
8. Application contracts, persistence records, and public report schemas remain distinct.
9. Persisted or externally serialized contracts eventually require version-aware evolution.
10. Only milestone-activated concepts are implemented.

## Accepted representation decision

Pydantic v2 is adopted for strict runtime boundary and trusted application contracts in M2 and the corresponding M3 path.

Accepted roles:

```text
raw manual/external data
→ preserve raw form
→ ManualCaseInput
→ explicit adapter
→ PullRequestSnapshotIdentity
→ DependencyChange
→ ChangedFileEvidence
→ InitialCaseRecord
```

Policies:

- raw source payloads remain plain source data or raw-source records;
- use strict Pydantic v2 validation;
- forbid undeclared fields in activated validated contracts;
- trusted models are frozen;
- trusted changed-file paths use `tuple[str, ...]`;
- all current fields remain required;
- flat-to-nested assembly remains a named, directly tested adapter;
- Pydantic `ValidationError` may remain internal during M2;
- no custom project-wide exception hierarchy yet;
- Pydantic models are not database rows or permanent public report schemas;
- Pydantic v3 requires reassessment.

## M2 activated contract

Required flat input:

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

Rules:

- exact required fields and types; no silent coercion;
- trim surrounding whitespace from declared strings and paths;
- canonicalize valid SHAs to lowercase;
- basic `owner/name` repository form;
- positive integer PR number, excluding booleans;
- 40-character hexadecimal base/head SHAs;
- non-empty dependency and versions;
- old/new versions differ;
- non-empty raw changed-file list;
- normalized paths are non-empty and unique;
- preserve source order;
- trusted paths become a tuple;
- raw dictionary and raw list remain unchanged;
- no mutable alias from raw list to trusted record;
- no partial trusted record on validation failure.

## Accepted source boundary

```text
UpgradePilot/
├── pyproject.toml
├── src/
│   └── upgradepilot/
│       ├── __init__.py
│       └── case_identity.py
└── tests/
    └── test_case_identity.py
```

Naming:

- repository/product: `UpgradePilot`;
- distribution/import package: `upgradepilot`;
- source root: `src/upgradepilot/`;
- tests: `tests/`.

Observed implementation-onboarding evidence:

- Python 3.12.3 is available as `python3`; the system has no `python` command.
- `.venv` was created and the project installed in editable mode.
- Pydantic 2.13.4 was installed under the accepted `>=2.13.4,<3` range.
- `upgradepilot` resolved from `src/upgradepilot/__init__.py`.
- the first AI-generated `case_identity.py` draft implements the activated boundary/trusted models and explicit adapter;
- the real M1 valid-case/non-mutation test passes; compileall passes;
- invalid-case regression tests, Ali-owned modification, and diagnosed-failure evidence remain incomplete.

## Ownership state

- Ali identified the requirements-before-method gap.
- Ali proposed Pydantic and challenged its premature rejection.
- The AI produced the detailed comparison, recommendation, ADR, and most specification wording.
- Ali explicitly approved and authorized the design direction.
- ADR-0002 is Ali-directed and substantially AI-generated.
- Ali correctly explained strict type and extra-field rejection.
- The AI created the package metadata, first valid test, and complete initial implementation draft.
- Practical Pydantic, packaging, test, debugging, and implementation ownership remain unproven pending Ali tracing/modification and diagnosed-failure evidence.

## Exact next authorized action

Trace the first draft through boundary validation, field/model validators, explicit nested assembly, structured errors, and serialization. Then add malformed-head-SHA and representative strict/non-mutation regression tests, complete one Ali-directed code change, and diagnose one intentional failure before accepting the M2-S01 behavior.

## Canonical references

- `README.md`
- `AGENTS.md`
- `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`
- `docs/architecture/ADR-0001-initial-python-source-layout.md`
- `docs/architecture/ADR-0002-pydantic-runtime-contract-models.md`
- `docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md`
- `docs/program/career/plans/UPGRADEPILOT_M2_S01_TECHNICAL_CONTRACT_AMENDMENT.md`
- `docs/program/career/tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md`
- `working-memory/2026-07-20_M2-S01_case-identity-implementation-start.md`
