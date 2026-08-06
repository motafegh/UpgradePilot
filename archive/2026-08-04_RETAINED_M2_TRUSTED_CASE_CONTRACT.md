# Retained Historical M2 Trusted-Case Contract

**Status:** Historical, non-controlling reference  
**Extracted from:** `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md` on 2026-08-04  
**Historical implementation anchor:** `e7425dcfc20f093ac10c9a903f1c4ae50a8b2638`

## Purpose

This file preserves the detailed trusted-case contract that was admitted during historical M2 work.

It is retained for traceability, comparison, and learning only. It does **not** activate M2, authorize implementation, establish current product contracts, or override active specifications, accepted ADRs, selected plans, source/tests, or `MEMORY.md`.

The active project-wide invariant specification is:

- [`../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md)

The clean-source separation from historical M2 implementation is controlled by:

- [`../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md`](../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md)
- [`2026-07-23_PRE_B2_M2_IMPLEMENTATION.md`](2026-07-23_PRE_B2_M2_IMPLEMENTATION.md)

## Historical caller input

The M2 manual adapter accepted exactly:

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

This mapping was a provisional adapter boundary. It was not the eventual public request or permanent semantic identity.

## Historical trusted structure

```text
InitialCaseRecord
├── snapshot_identity: PullRequestSnapshotIdentity
├── dependency_change: DependencyChange
└── changed_file_evidence: ChangedFileEvidence
```

| ID | Historical requirement |
|---|---|
| `CASE-STRUCT-001` | The trusted case used the nested structure above. |
| `CASE-STRUCT-002` | The flat eight-field input was not to become the permanent semantic identity or public interface. |
| `CASE-ATOMIC-001` | No partial trusted `InitialCaseRecord` could be returned when required validation failed. |

## Historical pull-request snapshot identity

```text
repository
pr_number
base_sha
head_sha
```

| ID | Historical requirement |
|---|---|
| `SNAP-REPO-001` | Repository identified one supported GitHub `owner/name` pair. |
| `SNAP-PR-001` | PR number was a positive non-boolean integer. |
| `SNAP-SHA-001` | Base/head revisions contained exactly 40 hexadecimal characters. |
| `SNAP-SHA-002` | Accepted SHA values were stored in lowercase canonical form. |
| `SNAP-REV-001` | Evidence from one head revision could not be silently reused for another. |
| `SNAP-REMOTE-001` | Format validation did not prove remote repository/PR/revision existence. |

## Historical dependency change

```text
dependency
old_version
new_version
```

| ID | Historical requirement |
|---|---|
| `DEP-NAME-001` | Dependency name was non-empty after permitted normalization. |
| `DEP-VER-001` | Old/new version values were non-empty after permitted normalization. |
| `DEP-VER-002` | Old/new version values differed. |
| `DEP-VER-003` | Source version strings remained source values unless a later explicit parser derived additional meaning. |
| `DEP-SEMVER-001` | Version category could be evidence but not compatibility proof. |

## Historical changed-file evidence

| ID | Historical requirement |
|---|---|
| `PATH-001` | At least one changed-file path existed for the retained M2 case. |
| `PATH-002` | Every accepted path was non-empty after permitted trimming. |
| `PATH-003` | Duplicate normalized paths were rejected rather than silently removed. |
| `PATH-004` | Source path order was preserved. |
| `PATH-005` | Trusted changed-file paths used an immutable collection. |
| `PATH-006` | Changed files remained snapshot-associated evidence rather than part of the minimal snapshot identifier. |

## Historical shape, type, and normalization rules

| ID | Historical requirement |
|---|---|
| `M2-IN-001` | All eight fields were present. |
| `M2-IN-002` | Unknown top-level fields were rejected. |
| `M2-TYPE-001` | Accepted types were exact at the validated boundary; material values were not silently coerced. |
| `M2-TYPE-002` | Boolean was not accepted as PR number despite Python's integer subtype relationship. |
| `M2-LIST-001` | `changed_files` was a raw list at the provisional caller boundary. |
| `M2-NORM-001` | Surrounding whitespace could be trimmed from declared text fields. |
| `M2-NORM-002` | Surrounding whitespace could be trimmed from each changed-file path. |
| `M2-NORM-003` | Valid hexadecimal SHAs were canonicalized to lowercase. |
| `M2-NORM-004` | Repository, dependency, version, and path spelling/casing were otherwise preserved. |

The historical adapter did not guess repositories, complete shortened SHAs, correct dependency names, rewrite version semantics, canonicalize paths beyond trimming, silently remove duplicates, or invent missing values.

## Historical raw-preservation and aliasing rules

| ID | Historical requirement |
|---|---|
| `M2-RAW-001` | Supplied raw mapping remained unchanged. |
| `M2-RAW-002` | Supplied raw changed-file list remained unchanged. |
| `M2-ALIAS-001` | Trusted values did not retain a mutable alias to the raw list. |
| `M2-TRUST-001` | Trusted changed-file paths were immutable. |

## Historical adapter and failure rules

| ID | Historical requirement |
|---|---|
| `M2-ADAPTER-001` | Flat-to-nested transformation remained an explicit named adapter/function/method. |
| `M2-ADAPTER-002` | Complete restructuring was not hidden in an opaque broad hook. |
| `M2-CASE-001` | The adapter returned the nested trusted record only after required checks passed. |
| `M2-CASE-002` | Validation failure did not return a partial trusted record. |
| `M2-ERR-001` | Representative invalid caller input produced structured validation evidence. |
| `M2-ERR-002` | Framework-specific error rendering could remain internal and was not a permanent public error contract by default. |
| `M2-ERR-003` | A project-wide exception hierarchy was not added before demonstrated need. |

## Historical proof obligations

| Proof ID | Historical evidence requirement |
|---|---|
| `M2-PROOF-001` | Minimal package metadata with admitted runtime dependency/version range. |
| `M2-PROOF-002` | Editable installation and import resolution from `src/upgradepilot/`. |
| `M2-PROOF-003` | Historical real case mapped into the expected nested trusted record. |
| `M2-PROOF-004` | Permitted whitespace normalization and lowercase SHA canonicalization. |
| `M2-PROOF-005` | Representative strict invalid cases rejected. |
| `M2-PROOF-006` | Raw mapping and raw changed-file list unchanged. |
| `M2-PROOF-007` | Trusted paths immutable and non-aliased. |
| `M2-PROOF-008` | Malformed head SHA produced structured validation evidence. |
| `M2-PROOF-009` | One Ali-directed central rule/error/behavior/test change implemented and tested. |
| `M2-PROOF-010` | One intentional relevant failure predicted, observed, diagnosed, repaired, and revalidated. |
| `M2-PROOF-011` | Assistance and ownership recorded conservatively. |

Historical tests and evidence show whether those obligations passed at a particular revision. This archive file does not establish present proof.

## Historical failure-category distinction

The retained contract distinguished:

1. reject caller request;
2. reject proposed trusted record;
3. preserve an external evidence state while continuing;
4. degrade the result;
5. abstain;
6. fail the run because trustworthy continuation is impossible.

M2 covered primarily caller/trusted-record validation. Later evidence degradation and decision responsibilities required separate admission.

## Historical unadmitted concepts

At the time, the following remained design needs rather than fully admitted M2 contracts:

- acquisition request and raw-source records;
- detailed provenance records;
- source-specific normalized evidence;
- full evidence-state hierarchy;
- repository dependency context;
- decision input/result;
- human/machine report contracts;
- persistence, replay, evaluation, and experiment records.

Their presence in this historical file does not imply current activation.
