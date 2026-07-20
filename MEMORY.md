# UpgradePilot Current Memory

**Last updated:** 2026-07-21  
**Purpose:** Compact current-state memory for a newly started AI assistant. Keep this file below 200 lines.

## Current control state

- Primary project: UpgradePilot.
- Program window: 2026-07-20 through 2026-10-17.
- Current route: R2 — First automated vertical slice.
- Current milestone: M2 — First automated vertical slice.
- M1 / UP-S01: Passed on `pydantic/pydantic#13432`.
- M1 recommendation: run targeted checks for semantic correctness of generated Algolia search records.
- M2-entry architecture-status audit: Passed.
- Initial Python source-layout decision: Accepted through `docs/architecture/ADR-0001-initial-python-source-layout.md`.
- Active Career controls:
  - `docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md`;
  - `docs/program/career/plans/UPGRADEPILOT_M2_S01_TECHNICAL_CONTRACT_AMENDMENT.md`.
- Accepted project-level technical specification:
  - `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`.
- M2-S01 status: Active; technical-contract correction and representation-method decision are in progress.
- Mode: Green.
- Focused minutes: not recorded.
- Active working record: `working-memory/2026-07-20_M2-S01_case-identity-implementation-start.md`.
- Earlier M2-S01 record: `working-memory/2026-07-20_M2-S01_case-identity-normalization.md`; retained as superseded pre-correction history.

## Why the M2 contract changed

Pre-code discussion showed that the original eight-field “case identity” mixed different concepts:

```text
repository + pr_number + base_sha + head_sha
→ pull-request snapshot identity

dependency + old_version + new_version
→ dependency change

changed_files
→ changed-file evidence

all components + raw/manual source reference
→ initial case record
```

The eight-field dictionary remains a provisional manually assembled M2 input. It is not the eventual public product input and is not one permanent semantic identity object.

## Accepted conceptual pipeline

```text
maintainer/operator request
→ acquisition request
→ raw source preservation
→ parsing and normalization
→ validation and evidence-state classification
→ initial case and later evidence assembly
→ repository/dependency context
→ deterministic recommendation or abstention
→ human-readable and machine-readable report
→ persistence and replay
→ evaluation and later experiments
```

The specification defines conceptual contracts without requiring their implementation now.

## Accepted core boundaries

1. Acquisition request is distinct from the complete case record.
2. Pull-request snapshot identity contains repository, PR number, base SHA, and head SHA.
3. Dependency transition and changed files are separate snapshot-associated facts/evidence.
4. Raw source/input remains separate from normalized or trusted representations.
5. Provenance and explicit evidence states are central project contracts.
6. Missing, invalid, inaccessible, stale, conflicting, rejected, unsupported, and not-applicable states must remain distinguishable where relevant.
7. Trusted contracts do not silently coerce values; any conversion belongs in an explicit adapter.
8. Application contracts, persistence records, and report schemas are conceptually distinct.
9. Persisted or externally serialized contracts eventually require version-aware evolution.
10. Conceptual objects are implemented only when their milestone activates them.

## M2 activated contract

The provisional manual M2 adapter supplies:

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

- all fields required;
- exact accepted types; no silent coercion;
- trim surrounding whitespace only from declared strings and paths;
- basic `owner/name` repository form;
- positive integer PR number, excluding booleans;
- 40-character hexadecimal base/head SHAs;
- non-empty dependency and version values;
- old/new versions differ;
- non-empty list of non-empty changed-file paths;
- raw input and nested mutable values remain unchanged;
- no partial trusted initial case record on adapter failure.

## Open representation decision

Before source implementation, compare:

- plain dictionaries plus explicit validation functions;
- `TypedDict` plus runtime validation;
- standard-library dataclasses;
- Pydantic models;
- a justified combination.

Comparison criteria include runtime validation, strict/coercing behavior, normalization order, cross-field rules, nested composition, mutation resistance, structured errors, serialization, version evolution, persistence separation, dependency/security cost, testing/diagnosis clarity, Ali ownership, and reversal path.

No representation framework has been accepted yet. A durable external framework or cross-project representation policy requires an ADR.

## Accepted initial source boundary

```text
UpgradePilot/
├── pyproject.toml             # not created yet
├── src/
│   └── upgradepilot/          # not created yet
└── tests/                     # not created yet
```

Naming:

- repository/product: `UpgradePilot`;
- distribution/import package: `upgradepilot`;
- source root: `src/upgradepilot/`;
- tests: `tests/`.

No complete internal architecture, source subpackages, runtime dependency, source file, test file, installation output, or accepted executable behavior exists yet.

## Current ownership state

- Ali identified that method selection was premature without whole-project contracts.
- Ali proposed Pydantic as a capable candidate and correctly challenged scope-based rejection before product requirements were analyzed.
- The AI identified and drafted the conceptual contract correction and governance alignment under Ali's direction.
- The technical specification and amendment are Ali-directed and substantially AI-generated.
- Practical representation selection, dependency adoption, implementation, packaging, testing, and debugging ownership remain unproven.

## Current decisions

1. Preserve the charter, capability specification, learning/execution contract, roadmap, milestone order, and source-layout ADR.
2. Add a project-level technical specification layer between governance and implementation.
3. Correct the original semantic conflation before code is created.
4. Treat the M2 eight-field dictionary as a provisional manual adapter.
5. Compare methods against the whole activated contract rather than one normalization function.
6. Do not reject or adopt Pydantic merely because it is a framework; decide from requirements, costs, evidence, and ownership.
7. Do not implement all conceptual contracts during M2.

## Exact next authorized action

Compare the candidate Python representation and validation methods against the accepted core specification and M2 amendment. Select the smallest credible method for the activated M2 contract and M3 path, record an ADR if the decision is durable, then resume the minimum package and test-first implementation.

## Canonical references

- `README.md`
- `AGENTS.md`
- `docs/specifications/README.md`
- `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`
- `docs/architecture/README.md`
- `docs/architecture/ADR-0001-initial-python-source-layout.md`
- `docs/program/SOURCE.md`
- `docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md`
- `docs/program/career/plans/UPGRADEPILOT_M2_S01_TECHNICAL_CONTRACT_AMENDMENT.md`
- `docs/program/career/tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md`
- `working-memory/2026-07-20_M2-S01_case-identity-implementation-start.md`
