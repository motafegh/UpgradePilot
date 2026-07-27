# UpgradePilot Core Invariants and Retained M2 Contract

**Status:** Accepted controlling technical specification  
**Owner:** Ali Rajabi  
**Responsibility:** Stable project-wide invariants and the retained historical M2 trusted-case contract  
**Implementation decisions:** ADRs under `../architecture/`  
**Actual behavior:** Source, tests, commands, outputs, and environment

## 1. Boundary and activation separation

This specification defines framework-independent behavior that admitted implementation must
preserve.

It does not:

- define project operation or learning procedure;
- select a framework, database, service, cloud, or deployment method;
- define live progress, stage, selected plan, latest commit, or next action;
- pre-create every future product record;
- activate a requirement merely because it is named here.

`../../MEMORY.md` is the sole owner of live project position and selects the position-neutral
plan that admits a responsibility. A requirement becomes an acceptance obligation only when
the selected plan activates its scope.

Sections 5–8 retain the historical M2 contract for traceability and comparison. They do not
state that M2 is presently selected.

## 2. Normative language

- **MUST** — required for acceptance when the requirement is admitted.
- **MUST NOT** — prohibited within the admitted scope.
- **SHOULD** — expected unless evidence justifies an exception.
- **MAY** — permitted.

## 3. Stable project invariants

| ID | Requirement |
|---|---|
| `FLOW-001` | Implemented responsibilities MUST reconnect to one continuous dependency-update decision flow. |
| `RAW-001` | Source/raw form MUST remain separate from normalized/trusted form. |
| `RAW-002` | Normalization or interpretation MUST NOT overwrite or mutate supplied raw evidence. |
| `OBS-001` | Observation, interpretation, evidence quality, and decision MUST remain distinct. |
| `SNAP-001` | Material evidence and conclusions MUST identify the repository and PR revision to which they apply. |
| `PROV-001` | Material normalized evidence and factual report claims MUST eventually resolve to origin, time/revision, and transformation identity when that responsibility is admitted. |
| `STATE-001` | Missing, inaccessible, stale, conflicting, invalid, rejected, unsupported, and not-applicable states MUST remain distinguishable where applicable. |
| `TRUST-001` | Trusted application contracts MUST NOT silently coerce material values. |
| `FAIL-001` | Invalid caller input, malformed source data, unavailable evidence, and internal defects MUST remain different failure categories. |
| `REP-001` | Application, persistence, and report representations MUST NOT be assumed identical. |
| `VERSION-001` | Persisted or externally serialized contracts MUST become version-aware before compatibility matters. |
| `ACT-001` | Only requirements admitted by the plan selected in `MEMORY.md` MAY be implemented as accepted product behavior. |
| `PROOF-001` | An accepted ADR authorizes a method but MUST NOT be treated as proof of implementation or learner ownership. |
| `AUTH-001` | A model-derived claim MUST retain its authority level and transformation identity when crossing grounding, orchestration, and decision boundaries. |
| `AUTH-002` | Literal source grounding MUST NOT be represented as independent corroboration or semantic truth. |
| `AUTH-003` | An uncorroborated model-derived claim MUST NOT independently justify a less cautious recommendation. |
| `AUTH-004` | Absence of a model-derived claim MUST NOT be treated as evidence that no relevant risk exists. |
| `AUTH-005` | Model output MUST NOT assign its own authority level, evidence state, or permitted decision effect. |
| `CLAIM-001` | A statement extracted from external evidence MUST be represented as an attributed source claim, not independently confirmed truth. |
| `CLAIM-002` | Accepting an evidence item for processing MUST establish only its eligibility and recorded state; it MUST NOT establish that every statement inside it is correct. |
| `CLAIM-003` | Distinct contradictory source claims MUST remain visible for later conflict handling rather than being silently collapsed or guessed away. |
| `GROUND-001` | Grounding MUST establish correspondence between an extracted claim and its cited source content; it MUST NOT be represented as corroboration of the claim. |
| `CORR-001` | Corroborated, contradicted, irrelevant-to-the-case, and not-yet-corroborated claim states MUST remain distinguishable when cross-source assessment is admitted. |
| `CONTENT-001` | External content MUST NOT redefine extraction policy, output authority, or permitted decision effects; instruction-like wording alone MUST NOT erase or invalidate preserved source evidence. |

## 4. Validation and transformation order

Where applicable, implementation must preserve this conceptual order:

1. retain supplied raw form or reference;
2. parse source format without inventing meaning;
3. validate required and extra fields and exact accepted runtime types;
4. perform only declared meaning-preserving normalization;
5. enforce field and cross-field semantic invariants;
6. create the complete trusted object only after required checks pass;
7. represent external evidence quality or availability separately from caller-input errors.

A framework MAY combine internal mechanics, but tests and code structure MUST preserve the
observable distinctions.

## 5. Retained M2 semantic contract

This section preserves the contract admitted by the historical M2-S01 plan. It is not a live
activation statement.

### 5.1 Provisional caller input

The historical M2 manual adapter accepted exactly:

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

This mapping was a provisional adapter boundary. It was not the eventual public request or a
permanent semantic identity.

### 5.2 Trusted structure

```text
InitialCaseRecord
├── snapshot_identity: PullRequestSnapshotIdentity
├── dependency_change: DependencyChange
└── changed_file_evidence: ChangedFileEvidence
```

| ID | Requirement |
|---|---|
| `CASE-STRUCT-001` | The trusted case MUST use the nested structure above when this historical contract is evaluated. |
| `CASE-STRUCT-002` | The flat eight-field input MUST NOT become the permanent semantic identity or public interface. |
| `CASE-ATOMIC-001` | No partial trusted `InitialCaseRecord` MAY be returned when required validation fails. |

### 5.3 Pull-request snapshot identity

```text
repository
pr_number
base_sha
head_sha
```

| ID | Requirement |
|---|---|
| `SNAP-REPO-001` | Repository MUST identify one supported GitHub `owner/name` pair. |
| `SNAP-PR-001` | PR number MUST be a positive non-boolean integer. |
| `SNAP-SHA-001` | Base and head revisions MUST contain exactly 40 hexadecimal characters. |
| `SNAP-SHA-002` | Accepted SHA values MUST be stored in lowercase canonical form. |
| `SNAP-REV-001` | Evidence from one head revision MUST NOT be silently reused for another. |
| `SNAP-REMOTE-001` | Format validation MUST NOT be described as proof that the repository, PR, or revision exists remotely. |

### 5.4 Dependency change

```text
dependency
old_version
new_version
```

| ID | Requirement |
|---|---|
| `DEP-NAME-001` | Dependency name MUST be non-empty after permitted normalization. |
| `DEP-VER-001` | Old and new version values MUST be non-empty after permitted normalization. |
| `DEP-VER-002` | Old and new version values MUST differ. |
| `DEP-VER-003` | Source version strings MUST remain source values unless a later explicit parser derives additional meaning. |
| `DEP-SEMVER-001` | Version category MAY be evidence but MUST NOT be presented as compatibility proof. |

### 5.5 Changed-file evidence

| ID | Requirement |
|---|---|
| `PATH-001` | At least one changed-file path MUST exist for the retained M2 case. |
| `PATH-002` | Every accepted path MUST be non-empty after permitted trimming. |
| `PATH-003` | Duplicate normalized paths MUST be rejected rather than silently removed. |
| `PATH-004` | Source path order MUST be preserved. |
| `PATH-005` | Trusted changed-file paths MUST use an immutable collection. |
| `PATH-006` | Changed files MUST remain snapshot-associated evidence, not part of the minimal snapshot identifier. |

## 6. Retained M2 input, normalization, and mutation rules

### 6.1 Shape and types

| ID | Requirement |
|---|---|
| `M2-IN-001` | All eight fields MUST be present. |
| `M2-IN-002` | Unknown top-level fields MUST be rejected. |
| `M2-TYPE-001` | Accepted types MUST be exact at the validated boundary; material values MUST NOT be silently coerced. |
| `M2-TYPE-002` | Boolean MUST NOT be accepted as PR number despite Python's integer subtype relationship. |
| `M2-LIST-001` | `changed_files` MUST be a raw list at the provisional caller boundary. |

### 6.2 Permitted normalization

| ID | Requirement |
|---|---|
| `M2-NORM-001` | Surrounding whitespace MAY be trimmed from declared text fields. |
| `M2-NORM-002` | Surrounding whitespace MAY be trimmed from each changed-file path. |
| `M2-NORM-003` | Valid hexadecimal SHAs MUST be canonicalized to lowercase. |
| `M2-NORM-004` | Repository, dependency, version, and path spelling or casing MUST otherwise be preserved. |

The adapter MUST NOT guess repositories, complete shortened SHAs, correct dependency names,
rewrite version semantics, canonicalize paths beyond trimming, remove duplicates silently,
or invent missing values.

### 6.3 Raw preservation and aliasing

| ID | Requirement |
|---|---|
| `M2-RAW-001` | The supplied raw mapping MUST remain unchanged. |
| `M2-RAW-002` | The supplied raw changed-file list MUST remain unchanged. |
| `M2-ALIAS-001` | Trusted values MUST NOT retain a mutable alias to the raw list. |
| `M2-TRUST-001` | Trusted changed-file paths MUST be immutable. |

### 6.4 Adapter and failures

| ID | Requirement |
|---|---|
| `M2-ADAPTER-001` | Flat-to-nested transformation MUST remain an explicit named adapter, function, or method. |
| `M2-ADAPTER-002` | Complete restructuring MUST NOT be hidden in an opaque broad hook. |
| `M2-CASE-001` | The adapter MUST return the nested trusted record only after all required checks pass. |
| `M2-CASE-002` | Validation failure MUST NOT return a partial trusted record. |
| `M2-ERR-001` | Representative invalid caller input MUST produce structured validation evidence. |
| `M2-ERR-002` | Framework-specific error rendering MAY remain internal and MUST NOT be declared a permanent public error contract without separate admission. |
| `M2-ERR-003` | A project-wide exception hierarchy MUST NOT be added before demonstrated need. |

## 7. Retained M2 proof obligations

| Proof ID | Required evidence |
|---|---|
| `M2-PROOF-001` | Minimal package metadata with the admitted runtime dependency and compatible version range. |
| `M2-PROOF-002` | Editable installation and resolved import path from `src/upgradepilot/`. |
| `M2-PROOF-003` | The historical real case maps into the expected nested trusted record. |
| `M2-PROOF-004` | Permitted whitespace normalization and lowercase SHA canonicalization. |
| `M2-PROOF-005` | Representative strict invalid cases are rejected. |
| `M2-PROOF-006` | Raw mapping and raw changed-file list remain unchanged. |
| `M2-PROOF-007` | Trusted paths are immutable and do not alias the raw list. |
| `M2-PROOF-008` | Malformed head SHA produces structured validation evidence. |
| `M2-PROOF-009` | One Ali-directed central rule, error, behavior, or test change is implemented and tested. |
| `M2-PROOF-010` | One intentional relevant failure is predicted, observed, diagnosed, repaired, and revalidated. |
| `M2-PROOF-011` | Assistance and ownership are recorded conservatively. |

Tests and dated evidence show whether these obligations passed at a particular revision. This
specification does not record pass/fail state.

## 8. Failure categories

Keep distinct:

1. reject caller request;
2. reject proposed trusted record;
3. preserve an external evidence state while continuing;
4. degrade the result;
5. abstain;
6. fail the run because trustworthy continuation is impossible.

The retained M2 contract covered caller and trusted-record validation. Later evidence
degradation and decision behavior require separate admission through the plan selected in
`MEMORY.md`.

## 9. Unadmitted concepts

The following are design needs only until a selected plan admits them:

- acquisition request and raw-source records;
- detailed provenance records;
- source-specific normalized evidence;
- full evidence-state hierarchy;
- repository dependency context;
- decision input and result;
- human- and machine-readable report contracts;
- persistence, replay, evaluation, and experiment records.

Do not define complete field schemas or implement these concepts merely because they are
listed.

## 10. Change control

Change this specification only when stable invariants, the retained M2 contract, failure
semantics, or technical proof obligations change.

Do not update it for:

- one test pass or failure;
- implementation progress;
- session completion;
- stage or plan selection;
- latest commit or exact continuation;
- file reorganization that preserves the contract;
- Career review state.

Reassess an applicable contract when real evidence shows an invariant is wrong, a source
cannot be represented without loss, framework behavior conflicts with required semantics,
hidden coercion or mutation appears, or a selected plan admits a later responsibility.