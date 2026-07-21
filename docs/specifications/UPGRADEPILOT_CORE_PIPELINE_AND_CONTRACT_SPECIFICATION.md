# UpgradePilot Core Pipeline and Contract Specification

**Owner:** Ali Rajabi  
**Status:** Accepted and controlling project-level technical specification  
**Responsibility:** Conceptual pipeline, information boundaries, invariants, evidence/failure states, milestone activation, and proof obligations  
**Implementation decisions:** Accepted ADRs under `../architecture/`  
**Actual behavior:** Source, tests, commands, and observed outputs  
**Live state:** Canonical Career tracker and project `MEMORY.md`; this specification does not record the exact next action.

## 1. Purpose

This specification defines the framework-independent technical contracts between the UpgradePilot product charter and implementation.

```text
product charter and route
→ technical requirements and contracts
→ accepted implementation decisions
→ bounded plans/sessions
→ source code, tests, and observed execution
```

It prevents source formats, temporary adapters, persistence schemas, report schemas, or framework conveniences from silently becoming the permanent product model.

## 2. Normative language

- **MUST** — required for acceptance.
- **MUST NOT** — prohibited.
- **SHOULD** — expected unless a documented evidence-based reason exists.
- **MAY** — permitted.

`Accepted`, `Provisional`, `Activated`, and `Deferred` describe contract maturity or milestone status. They do not replace requirement strength.

## 3. Responsibility boundary

This specification controls:

- required concepts and information boundaries;
- externally observable contract behavior;
- invariants and evidence/failure semantics;
- raw/trusted separation;
- milestone activation;
- proof categories required for acceptance.

ADRs control:

- selected framework or mechanism;
- framework-specific configuration and APIs;
- alternatives, trade-offs, version policy, and reassessment triggers.

For the current runtime-contract implementation, `ADR-0002-pydantic-runtime-contract-models.md` controls Pydantic v2 mechanics. This specification requires strict behavior, explicit adapters, immutable trusted structures, undeclared-field rejection, and structured failure evidence without duplicating unnecessary Pydantic APIs.

## 4. Non-goals

This specification does not:

- pre-create every future model or source layer;
- define a database product, relational schema, or ORM;
- define a permanent public CLI/API or report schema;
- implement acquisition, recommendation, reporting, persistence, evaluation, ML, graph, LLM, agent, queue, service, cloud, or deployment systems;
- require raw source data, database rows, or reports to use the runtime application-model framework;
- claim that complete internal architecture is known;
- change Day-90 strategy, capacity, advanced-systems targets, or completion requirements.

## 5. Core principles

| ID | Requirement |
|---|---|
| `FLOW-001` | Implemented responsibilities MUST reconnect to one continuous dependency-update decision flow. |
| `RAW-001` | Source/raw form MUST remain separate from normalized/trusted form. |
| `RAW-002` | Normalization or interpretation MUST NOT overwrite or mutate the supplied raw evidence. |
| `OBS-001` | Observation, interpretation, evidence quality, and decision MUST remain distinct. |
| `SNAP-001` | Material evidence and conclusions MUST identify the repository and PR revision to which they apply. |
| `PROV-001` | Material normalized evidence and factual report claims MUST eventually resolve to origin, time/revision, and transformation identity. |
| `STATE-001` | Missing, inaccessible, stale, conflicting, invalid, rejected, unsupported, and not-applicable states MUST remain explicit. |
| `TRUST-001` | Trusted application contracts MUST NOT silently coerce material values. |
| `FAIL-001` | Invalid caller input, malformed source data, unavailable evidence, and internal defects MUST remain different failure categories. |
| `REP-001` | Application, persistence, and report representations MUST NOT be assumed identical. |
| `VERSION-001` | Persisted or externally serialized contracts MUST become version-aware before compatibility matters. |
| `ACT-001` | Only milestone-activated requirements MAY be implemented as accepted product behavior. |
| `PROOF-001` | An accepted ADR authorizes a mechanism but MUST NOT be treated as proof of implementation or learner ownership. |

## 6. Conceptual product pipeline

```text
Maintainer or operator request
→ acquisition-request validation
→ source acquisition or accepted manual evidence
→ raw-source preservation
→ source-format parsing
→ exact-type and structural boundary validation
→ declared lexical normalization
→ semantic and cross-field validation
→ trusted-object creation
→ evidence-state classification
→ initial case/evidence assembly
→ repository/dependency context enrichment
→ decision-input assembly
→ deterministic recommendation or abstention
→ human-readable and machine-readable report
→ persistence and replay
→ evaluation corpus and later experiments
```

Stages MAY be delivered incrementally, but boundaries MUST remain explicit.

## 7. Validation and transformation order

The following order is controlling where applicable:

1. **Raw preservation** — retain the supplied source form or a reference before project normalization.
2. **Source-format parsing** — decode an external format without assigning unsupported meaning.
3. **Boundary shape and exact-type validation** — check required/extra fields and accepted runtime types.
4. **Declared lexical normalization** — perform only explicitly allowed, meaning-preserving transformations.
5. **Semantic and cross-field validation** — enforce format, range, uniqueness, and relationship invariants.
6. **Trusted-object creation** — assemble the accepted project representation only after all required checks pass.
7. **Evidence-state classification** — represent source availability/quality states without collapsing them into exceptions.

A framework MAY combine internal steps operationally, but tests and code structure MUST preserve the conceptual distinctions and observable behavior.

## 8. Core conceptual contracts

### 8.1 AcquisitionRequest

**Status:** Provisional for M2; expanded in M3.

Purpose: identify what the system should inspect or replay.

Initial locator:

```text
repository
pr_number
```

An acquisition request MAY contain less information than a complete trusted case because the product acquires later facts.

### 8.2 PullRequestSnapshotIdentity

**Status:** Accepted; M2 fields activated.

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
| `SNAP-SHA-001` | Base and head revisions MUST contain exactly 40 hexadecimal characters at the current boundary. |
| `SNAP-SHA-002` | Accepted SHA values MUST be stored in lowercase canonical form. |
| `SNAP-REV-001` | Evidence from one head revision MUST NOT be silently reused for another. |
| `SNAP-REMOTE-001` | Format validation MUST NOT be described as proof that the repository, PR, or revision exists remotely. |

### 8.3 DependencyChange

**Status:** Accepted; M2 fields activated and later enriched.

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

Later context MAY include declaration/lock source, direct/transitive/optional/runtime/development state, markers, extras, and resolution path.

### 8.4 ChangedFileEvidence

**Status:** Accepted; bounded M2 path collection activated.

| ID | Requirement |
|---|---|
| `PATH-001` | At least one changed-file path MUST exist for the activated M2 case. |
| `PATH-002` | Every accepted path MUST be non-empty after permitted trimming. |
| `PATH-003` | Duplicate normalized paths MUST be rejected rather than silently removed. |
| `PATH-004` | Source path order MUST be preserved. |
| `PATH-005` | Trusted changed-file paths MUST use an immutable collection. |
| `PATH-006` | Changed files MUST remain snapshot-associated evidence, not part of the minimal snapshot identifier. |

### 8.5 InitialCaseRecord

**Status:** Accepted and activated for M2.

```text
InitialCaseRecord
├── snapshot_identity: PullRequestSnapshotIdentity
├── dependency_change: DependencyChange
└── changed_file_evidence: ChangedFileEvidence
```

| ID | Requirement |
|---|---|
| `CASE-STRUCT-001` | The trusted case MUST use the nested semantic structure above. |
| `CASE-STRUCT-002` | The flat eight-field input MUST remain a provisional adapter boundary, not the permanent semantic identity or eventual public interface. |
| `CASE-ATOMIC-001` | No partial trusted InitialCaseRecord MAY be returned when required validation fails. |

### 8.6 RawSourceRecord

**Status:** Accepted concept; full implementation expands in M3.

Purpose: preserve what a source supplied before project normalization or interpretation.

Conceptual information includes source type/locator, observation/retrieval time, source revision, raw payload/reference, and acquisition status.

| ID | Requirement |
|---|---|
| `RAW-SOURCE-001` | Raw source content MUST remain untrusted data and MUST NOT be executed merely for inspection. |
| `RAW-SOURCE-002` | Secrets/private data MUST NOT be preserved in public artifacts. |
| `RAW-SOURCE-003` | Large or unsuitable payloads MAY be referenced rather than embedded. |

**M2 scope clarification:** M2 MUST preserve the manually supplied mapping and its changed-file list unchanged. M2 does **not** claim to construct the later complete RawSourceRecord with retrieval time, source revision, storage reference, and acquisition status unless separately activated.

### 8.7 Provenance

**Status:** Accepted and central; detailed implementation grows in M3.

Provenance eventually records source identity, locator, observation time, revision, raw-record reference, transformation identity/version, and producing run.

Inferences MUST identify supporting evidence and MUST NOT be mislabeled as direct source observations.

### 8.8 NormalizedEvidenceRecord

**Status:** Accepted concept; source-specific records activate later.

Normalization MUST be declared, deterministic, meaning-preserving, and non-inventive.

### 8.9 EvidenceState

**Status:** Accepted; exact later hierarchy remains milestone-bounded.

Required conceptual states:

```text
accepted
rejected
missing
invalid
inaccessible
stale
conflicting
unsupported
not_applicable
```

Evidence states are data used by degradation and abstention logic. They MUST NOT automatically be treated as exceptions.

### 8.10 RepositoryDependencyContext

**Status:** Accepted concept; implementation deferred to M4 except the initial dependency change.

It MAY represent declaration, resolution path, source usage, tests, workflows, observations, inferred relationships, unresolved paths, and limitations without converting static references into runtime proof.

### 8.11 DecisionInput and DecisionResult

**Status:** Accepted concepts; later M2/M5 activation.

Decision input MUST contain an explicit evidence set, unresolved states, context, policy/rule version, and limitations. It MUST NOT silently read arbitrary global mutable state.

Decision result supports:

```text
merge after normal review
run targeted checks
investigate or block
defer
abstain
```

It MAY include rationale, targeted checks, uncertainty, evidence references, limitations, and rule version.

### 8.12 Report

**Status:** Accepted concept; deferred to report slice.

Human-readable and machine-readable output MUST preserve traceability and distinguish observations, interpretations, uncertainty, and recommendation.

Passing CI, SemVer, merged status, or a score MUST NOT be presented as safety proof.

### 8.13 Run, replay, evaluation, and experiment records

**Status:** Accepted conceptual need; deferred to M3–M6.

Later records preserve input/source/transformation versions, replay/duplicate behavior, corpus/split/adjudication identity, predictions, metrics and denominators, errors, cost, latency, and adopt/reject/defer decisions.

Historical PR disposition MUST NOT be treated as objective truth by itself.

## 9. M2 manual boundary contract

The provisional M2 caller mapping supplies exactly:

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

### 9.1 Field and type requirements

| ID | Requirement |
|---|---|
| `M2-IN-001` | All eight fields MUST be present. |
| `M2-IN-002` | Unknown top-level fields MUST be rejected. |
| `M2-TYPE-001` | Accepted types MUST be exact at the validated boundary; material values MUST NOT be silently coerced. |
| `M2-TYPE-002` | Boolean MUST NOT be accepted as PR number despite Python's integer subtype relationship. |
| `M2-LIST-001` | `changed_files` MUST be a raw list at the provisional caller boundary. |

### 9.2 Permitted normalization

| ID | Requirement |
|---|---|
| `M2-NORM-001` | Surrounding whitespace MAY be trimmed from declared text fields. |
| `M2-NORM-002` | Surrounding whitespace MAY be trimmed from each changed-file path. |
| `M2-NORM-003` | Valid hexadecimal SHAs MUST be canonicalized to lowercase. |
| `M2-NORM-004` | Repository, dependency, version, and path spelling/casing MUST otherwise be preserved. |

Not permitted:

- hidden type coercion;
- repository guessing;
- shortened-SHA completion;
- dependency spelling correction;
- version parsing/rewriting;
- path canonicalization beyond declared trimming;
- silent duplicate removal;
- invented missing fields.

### 9.3 Raw preservation and aliasing

| ID | Requirement |
|---|---|
| `M2-RAW-001` | The supplied raw mapping MUST remain unchanged. |
| `M2-RAW-002` | The supplied raw changed-file list MUST remain unchanged. |
| `M2-ALIAS-001` | Trusted values MUST NOT retain a mutable alias to the raw list. |
| `M2-TRUST-001` | Trusted changed-file paths MUST be immutable. |

### 9.4 Adapter and trusted assembly

| ID | Requirement |
|---|---|
| `M2-ADAPTER-001` | Flat-to-nested transformation MUST remain an explicit named adapter/function/method. |
| `M2-ADAPTER-002` | Complete restructuring MUST NOT be hidden in an opaque broad hook that makes the semantic mapping untraceable. |
| `M2-CASE-001` | The adapter MUST return the nested InitialCaseRecord only after all required checks pass. |
| `M2-CASE-002` | Validation failure MUST NOT return a partial trusted record. |

### 9.5 Failure evidence

| ID | Requirement |
|---|---|
| `M2-ERR-001` | Representative invalid caller input MUST produce structured validation evidence. |
| `M2-ERR-002` | Framework-specific error rendering MAY remain internal during M2 and MUST NOT be declared a permanent public error contract. |
| `M2-ERR-003` | A project-wide exception hierarchy MUST NOT be added before a demonstrated need. |

## 10. Failure and degradation categories

1. **Reject request** — caller input cannot be interpreted safely.
2. **Reject record** — a proposed trusted record violates invariants.
3. **Preserve evidence state** — external evidence is missing, inaccessible, stale, conflicting, unsupported, rejected, or not applicable and the run may continue.
4. **Degrade result** — evidence supports only a weaker output or targeted checks.
5. **Abstain** — evidence is insufficient or conflicting beyond the accepted boundary.
6. **Fail run** — configuration, programming, persistence, or unexpected operational failure prevents a trustworthy result.

## 11. Required M2 implementation proof

The first accepted implementation MUST demonstrate:

| Proof ID | Required evidence |
|---|---|
| `M2-PROOF-001` | Minimal package metadata with the accepted runtime dependency and compatible version range. |
| `M2-PROOF-002` | Editable installation and resolved import path from `src/upgradepilot/`. |
| `M2-PROOF-003` | Real M1 case maps into the expected nested trusted record. |
| `M2-PROOF-004` | Whitespace normalization and lowercase SHA canonicalization. |
| `M2-PROOF-005` | Strict rejection of representative wrong-type, extra-field, malformed repository/PR/SHA, empty, equal-version, duplicate-path, and empty-path cases as activated. |
| `M2-PROOF-006` | Raw mapping and raw changed-file list remain unchanged. |
| `M2-PROOF-007` | Trusted paths are immutable and do not alias the raw list. |
| `M2-PROOF-008` | Malformed head SHA produces structured validation evidence. |
| `M2-PROOF-009` | One Ali-directed central rule, error, or behavior change is implemented and tested. |
| `M2-PROOF-010` | One intentional relevant failure is predicted, observed, diagnosed, repaired, and revalidated. |
| `M2-PROOF-011` | Assistance and ownership are recorded conservatively; AI-generated implementation alone does not close the gate. |

## 12. Contract-to-proof traceability

| Requirement group | Proof category | Current evidence location |
|---|---|---|
| `SNAP-*`, `M2-IN-*`, `M2-TYPE-*` | valid/invalid boundary tests | Source/tests; tracker summary when accepted |
| `DEP-*` | semantic valid/invalid tests | Source/tests |
| `PATH-*` | empty/duplicate/order/immutability tests | Source/tests |
| `RAW-*`, `M2-RAW-*`, `M2-ALIAS-*` | non-mutation and alias tests | Source/tests |
| `CASE-*`, `M2-ADAPTER-*` | nested structure and no-partial-record tests | Source/tests |
| `M2-ERR-*` | structured error evidence | Test output/working evidence |
| `M2-PROOF-009` | Ali-directed change evidence | Working record and tracker capability entry |
| `M2-PROOF-010` | intentional failure diagnosis | Working record, test history, tracker capability entry |

The specification defines proof obligations. Tests and evidence records show whether they passed.

## 13. Milestone activation

| Milestone | Activated technical responsibility |
|---|---|
| M1 | Manual evidence reasoning and explicit limitations |
| M2 | Provisional manual boundary, nested trusted case, first deterministic decision/report slices as separately authorized |
| M3 | Reliable acquisition, raw-source/provenance expansion, replay/persistence foundations |
| M4 | Repository/dependency context and bounded static evidence |
| M5 | Deterministic baseline, labels/truth, evaluation and error analysis |
| M6 | Admitted analytical/ML experiments when evidence supports them |
| M7 | Existing approved advanced-systems exposure/pilots under unchanged Career strategy and gates |
| M8 | Reproducible final demonstration, limitations, portfolio closure |

This specification revision does not change milestone order, Day-90 capacity, advanced-systems targets, or completion requirements.

## 14. Acceptance and change control

A requirement is accepted only when:

- applicable proof exists;
- failure and limitations are explicit;
- actual assistance is recorded;
- learner ownership evidence matches the claimed depth;
- no higher-authority constraint is violated.

Change this specification when required behavior, contract boundaries, invariants, failure semantics, activation, or proof obligations change.

Change an ADR when the selected framework/mechanism, framework policy, trade-off, or reassessment trigger changes.

Do not update this specification merely because:

- one test passes/fails;
- the exact next action changes;
- a session ends;
- an implementation file is reorganized without changing contracts;
- tracker state changes.

## 15. Reassessment triggers

Reassess the relevant contract or method when evidence shows:

- an activated invariant is wrong or incomplete;
- a source format cannot be represented without loss;
- framework behavior conflicts with required semantics;
- hidden coercion or mutation occurs;
- persistence/report compatibility creates a new boundary;
- error behavior must become public and stable;
- a milestone activates a previously deferred concept;
- operating cost, security, upgrade burden, or ownership materially changes the method decision.

## 16. Immediate implementation boundary

Current implementation work MAY address only the separately authorized M2 requirements.

This specification MUST NOT be used to justify implementing all conceptual contracts, persistence, acquisition, CI, containers, advanced systems, ML, or future architecture before their approved gates.