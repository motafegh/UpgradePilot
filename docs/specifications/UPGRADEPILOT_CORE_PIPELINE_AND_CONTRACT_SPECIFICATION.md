# UpgradePilot Core Pipeline and Contract Specification

**Owner:** Ali Rajabi  
**Recorded:** 2026-07-21  
**Status:** Accepted and controlling project-level technical specification  
**Authority:** Subordinate to the canonical Career governance stack and active M2 authorization; controls UpgradePilot's conceptual pipeline, information boundaries, invariants, states, and activated contract requirements  
**Selected runtime-contract method:** Pydantic v2 under `../architecture/ADR-0002-pydantic-runtime-contract-models.md`

## 1. Purpose

UpgradePilot has moved from project selection into implementation. The governing Career artifacts define the mission, evidence doctrine, route, gates, and learning method. This specification defines the technical-contract layer required between those controls and source code:

```text
product charter and roadmap
→ core pipeline and contract specification
→ accepted architecture/method decisions
→ bounded plans and sessions
→ source code, tests, and observed execution
```

It prevents temporary adapters, source formats, or framework conveniences from silently becoming the permanent product model.

## 2. Non-goals

This specification does not:

- pre-create Python source layers or every future model;
- define the database product, relational schema, or ORM;
- define a public CLI or API;
- implement acquisition, decision policy, reporting, persistence, evaluation, ML, graphs, LLMs, agents, queues, services, cloud, or deployment;
- make Pydantic the representation for raw source data, database rows, or every later analytical record;
- claim that the complete internal architecture is known.

## 3. Controlling principles

The following are accepted:

1. **One continuous product flow.** Implemented responsibilities reconnect to a real dependency-update PR and a traceable recommendation or abstention.
2. **Source form and trusted form are separate.** Normalization or interpretation never overwrites raw source data.
3. **Observation, interpretation, evidence quality, and decision are different concepts.**
4. **Snapshot correctness is mandatory.** Evidence and conclusions identify the repository and PR revision to which they apply.
5. **Provenance continuity is central.** Material normalized evidence and report claims eventually resolve to origin, time/revision, and transformation identity.
6. **Degradation is explicit.** Missing, inaccessible, stale, conflicting, invalid, rejected, unsupported, and not-applicable states do not collapse into silent emptiness.
7. **Trusted contracts are strict.** Automatic conversion occurs only in an explicit adapter with declared behavior and tests.
8. **Boundary failures differ.** Invalid caller input, malformed source data, unavailable evidence, and internal defects are not one failure category.
9. **Application, persistence, and report representations remain distinct.**
10. **Persisted or externally serialized contracts become version-aware.**
11. **Only milestone-activated concepts are implemented.**
12. **Accepted methods require implementation proof.** An ADR authorizes a mechanism but does not prove behavior or ownership.

## 4. Conceptual product pipeline

```text
Maintainer or operator request
→ acquisition request validation
→ source acquisition or accepted manual evidence
→ raw source preservation
→ source-specific parsing
→ explicit normalization
→ structural and semantic validation
→ evidence-state classification
→ initial case and evidence assembly
→ repository/dependency context enrichment
→ decision-input assembly
→ deterministic recommendation or abstention
→ human-readable and machine-readable report
→ persistence and replay
→ evaluation corpus and later experiments
```

The stages may be delivered incrementally, but their boundaries remain explicit.

## 5. Core conceptual contracts

### 5.1 AcquisitionRequest

**Status:** Provisional for M2; expanded in M3.

Purpose: identify what the system should inspect or replay.

Initial locator:

```text
repository
pr_number
```

A public acquisition request may contain less information than the complete trusted case because UpgradePilot is responsible for acquiring later facts.

### 5.2 PullRequestSnapshotIdentity

**Status:** Accepted concept; M2 fields activated.

Purpose: identify the exact PR revision to which evidence and conclusions apply.

```text
repository
pr_number
base_sha
head_sha
```

Invariants:

- repository identifies one supported GitHub `owner/name` pair;
- PR number is a positive non-boolean integer;
- base and head revisions use full 40-character hexadecimal identifiers in the current boundary;
- evidence from one head revision is not silently reused for another;
- format validation does not prove remote existence.

### 5.3 DependencyChange

**Status:** Accepted concept; M2 fields activated and later enriched through M4.

```text
dependency
old_version
new_version
```

Invariants:

- all three values are non-empty after permitted normalization;
- old and new versions differ;
- version strings remain source values unless a later explicit parser derives additional meaning;
- version category is evidence, not compatibility proof.

Later context may include declaration/lock source, package format, direct/transitive/optional/runtime/development state, markers, and extras.

### 5.4 ChangedFileEvidence

**Status:** Accepted concept; M2 bounded path collection activated.

Purpose: preserve repository paths changed in the identified snapshot.

Invariants:

- at least one path exists for the selected M2 case;
- every accepted path is non-empty after trimming;
- normalized duplicate paths are rejected rather than silently removed;
- source order is preserved;
- changed files are snapshot-associated evidence, not part of the minimal snapshot identifier.

### 5.5 InitialCaseRecord

**Status:** Accepted and activated for M2.

```text
InitialCaseRecord
├── snapshot_identity: PullRequestSnapshotIdentity
├── dependency_change: DependencyChange
└── changed_file_evidence: ChangedFileEvidence
```

This corrects the former eight-field “case identity” wording. The flat eight-field input remains a provisional M2 adapter, not a permanent semantic identity or eventual public interface.

### 5.6 RawSourceRecord

**Status:** Accepted concept; bounded preservation begins in M2 and expands in M3.

Purpose: preserve what a caller or source supplied before project normalization or interpretation.

Conceptual information includes source type/locator, observation or retrieval time, source revision, raw payload/reference, and acquisition status.

Invariants:

- normalization never overwrites raw form;
- private or secret data is not preserved in the public repository;
- untrusted source content remains data and is not executed merely for inspection;
- large or unsuitable payloads may be referenced rather than embedded.

### 5.7 Provenance

**Status:** Accepted and central; detailed implementation grows in M3.

Purpose: record source identity, locator, retrieval/observation time, revision, raw-record reference, transformation identity/version, and producing run.

Material normalized evidence and factual report claims eventually resolve through provenance. Inferences identify supporting evidence without being mislabeled as source observations.

### 5.8 NormalizedEvidenceRecord

**Status:** Accepted concept; source-specific contracts activate when their milestones require them.

Conceptually contains normalized content, provenance reference, evidence state, validation findings, and contract version when durably serialized or persisted.

Normalization is declared, deterministic, meaning-preserving, and non-inventive.

### 5.9 EvidenceState

**Status:** Accepted; exact later enum hierarchy remains milestone-bounded.

Required conceptual states include:

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

These states are data used by degradation and abstention logic. They are not automatically exceptions.

### 5.10 RepositoryDependencyContext

**Status:** Accepted concept; implementation deferred to M4 except the initial dependency change.

Purpose: represent declaration, resolution path, source usage, tests, workflows, observations, inferred relationships, unresolved paths, and limitations without converting static references into runtime proof.

### 5.11 DecisionInput and DecisionResult

**Status:** Accepted concepts; activated in later M2 sessions and stabilized through M5.

Decision input contains an explicit set of accepted evidence, unresolved states, context, policy/rule version, and limitations. It does not silently read arbitrary global mutable state.

Decision result supports:

```text
merge after normal review
run targeted checks
investigate or block
defer
abstain
```

It may include rationale, targeted checks, uncertainty findings, evidence references, limitations, and rule version.

### 5.12 Report

**Status:** Accepted concept; implementation deferred to the report slice.

Human-readable and machine-readable output preserves traceability and distinguishes observations, interpretations, uncertainty, and recommendation. Passing CI, SemVer, merged status, or a score is never presented as safety proof.

### 5.13 RunRecord, replay, evaluation, and experiment records

**Status:** Accepted conceptual need; implementation deferred to M3–M6.

Later records preserve run/input/source/transformation versions, replay and duplicate behavior, corpus/split/adjudication identity, predictions, metrics and denominators, errors, cost, latency, and adopt/reject/defer decisions.

Historical PR disposition is not objective truth.

## 6. Activated runtime representation decision

`ADR-0002-pydantic-runtime-contract-models.md` is accepted and controls implementation of the activated runtime contracts.

### 6.1 Selected roles

- raw manual/external input remains plain source data or a preserved raw-source record;
- `ManualCaseInput` is the provisional flat Pydantic boundary model for M2;
- `PullRequestSnapshotIdentity`, `DependencyChange`, `ChangedFileEvidence`, and `InitialCaseRecord` are strict nested Pydantic application models;
- a named explicit adapter transforms the flat boundary model into the nested trusted record;
- application models are not database rows or public report schemas.

### 6.2 Model policy

- use Pydantic v2 APIs;
- strict runtime validation by default;
- forbid undeclared fields in validated M2 contracts;
- configure trusted models as frozen;
- use immutable nested collections such as `tuple[str, ...]` for trusted changed-file paths;
- all activated M2 fields remain required;
- use Pydantic `ValidationError` internally during M2;
- do not add a custom project-wide exception hierarchy yet;
- do not expose framework-specific error rendering as a permanent public contract.

### 6.3 Explicit adapter policy

The flat-to-nested transformation remains a named, directly tested function or method.

Do not hide complete restructuring, provenance decisions, or material conversions in one broad pre-validation hook.

## 7. Validation and normalization boundaries

### 7.1 Accepted validation layers

```text
caller/request validation
source parsing validation
normalized evidence validation
cross-record semantic validation
decision sufficiency checks
internal programmer/runtime defects
```

Different layers may use different result or error mechanisms.

### 7.2 Permitted M2 normalization

- trim surrounding whitespace from declared text fields;
- trim each changed-file path;
- canonicalize valid hexadecimal SHAs to lowercase;
- preserve repository, dependency, version, and path spelling/casing otherwise.

Not permitted:

- hidden type coercion;
- repository guessing;
- shortened-SHA completion;
- dependency spelling correction;
- version parsing or rewriting;
- path canonicalization beyond trimming;
- silent duplicate removal;
- invented missing fields.

### 7.3 Failure and degradation categories

1. **Reject request** — the request cannot be interpreted safely.
2. **Reject record** — a proposed trusted record violates required invariants.
3. **Preserve evidence state** — evidence is missing, inaccessible, stale, conflicting, unsupported, rejected, or not applicable and the run may continue.
4. **Degrade result** — available evidence supports only a weaker output or targeted checks.
5. **Abstain** — evidence is insufficient or conflicting beyond the accepted boundary.
6. **Fail run** — configuration, programming, persistence, or unexpected operational failure prevents a trustworthy result.

## 8. M2 manual adapter contract

Required supplied fields:

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

Semantic mapping:

```text
repository + pr_number + base_sha + head_sha
→ PullRequestSnapshotIdentity

dependency + old_version + new_version
→ DependencyChange

changed_files
→ ChangedFileEvidence

all three trusted components
→ InitialCaseRecord
```

Rules:

- all eight fields are required;
- accepted types are exact and not silently coerced;
- unknown top-level fields are rejected;
- repository uses the current basic `owner/name` rule;
- PR number is positive and not boolean;
- SHAs are exactly 40 hexadecimal characters and stored lowercase;
- dependency and versions are non-empty;
- old and new versions differ;
- changed files is a non-empty list at the raw boundary and a tuple in the trusted record;
- every normalized path is non-empty and unique;
- raw input and its list remain unchanged;
- trusted values do not alias raw mutable structures;
- no partial trusted `InitialCaseRecord` is returned when validation fails.

## 9. Required M2 implementation proof

The first implementation must demonstrate:

1. minimal package metadata including the accepted Pydantic dependency;
2. editable installation and import resolution from `src/upgradepilot/`;
3. the real M1 case maps into the expected nested record;
4. whitespace normalization and lowercase SHA canonicalization;
5. strict rejection of malformed or wrong-type representative input;
6. raw dictionary and changed-file list remain unchanged;
7. trusted paths are immutable and do not alias the raw list;
8. malformed head SHA is rejected through structured validation evidence;
9. one Ali-directed rule/error/test change;
10. one intentional failure is diagnosed and repaired;
11. assistance and capability evidence remain conservative.

Passing these tests proves only the bounded activated contract, not remote existence, complete M2, complete architecture, or broad Pydantic ownership.

## 10. Persistence, serialization, and versioning

Pydantic v2 serialization may support internal machine-readable tests and outputs.

Do not add a schema version to every M2 value object. Explicit versioning becomes mandatory at the first durable boundary: persisted normalized records, replay, machine-readable reports, public API contracts, or exported evaluation datasets.

Persistence mappings are designed separately in M3 around keys, relationships, provenance, history, replay, migrations, and queries.

## 11. Milestone activation map

### M2

Activate only the manual input adapter, raw-input preservation, snapshot identity, dependency change, changed-file evidence, nested initial case record, minimum validation failure behavior, and later separately authorized decision/report slices.

### M3

Activate source-specific acquisition contracts, raw source records, provenance, normalized evidence, explicit partial-source failure, evidence states, run/replay records, persistence mappings, versioning, structured diagnostics, and integration/failure/recovery tests.

### M4

Activate declaration/lock evidence, dependency relationships and paths, repository references/tests/workflows, locations/revisions, and reachability limitations.

### M5

Activate versioned decision contracts, decision table and evidence-sufficiency rules, corpus/adjudication/split/metric/error-analysis records.

### M6 and later

Activate only evidence-admitted experiment, model, graph, grounded-LLM, MLOps, queue, service, orchestration, and deployment records.

## 12. Decision status

### Accepted

- semantic separation of acquisition request, snapshot identity, dependency change, changed-file evidence, and aggregate initial case record;
- raw/trusted separation;
- provenance and evidence-state doctrine;
- strict trusted contracts;
- Pydantic v2 for activated runtime application contracts under ADR-0002;
- explicit flat-to-nested adapters;
- frozen trusted models with immutable nested collections;
- application/persistence/report separation;
- milestone-bounded implementation and later version-aware evolution.

### Provisional for M2

- the manually assembled eight-field adapter;
- current class and function names until source implementation verifies them;
- basic repository `owner/name` validation;
- full 40-character SHA requirement;
- duplicate normalized path rejection;
- direct internal use of Pydantic `ValidationError`.

### Deferred

- public CLI/API design;
- complete source-specific response schemas;
- complete evidence hierarchy;
- database/ORM/migration choice;
- report version envelope;
- custom project-wide exception hierarchy;
- semantic version and package-name value types;
- universal Pydantic adoption for later analytical records;
- complete internal package layering.

### Rejected under current evidence

- one permanent flat identity object containing all eight fields;
- Pydantic models as raw evidence;
- hidden trusted-model coercion;
- silent path deduplication;
- one universal exception for all evidence states;
- direct coupling of application models to database tables;
- simultaneous Pydantic and dataclass application object systems without demonstrated need;
- implementing every conceptual contract during M2.

## 13. Reassessment triggers

Revisit this specification or ADR-0002 when:

- an activated source cannot map without losing material meaning;
- Pydantic obscures normalization, provenance, diagnosis, or ownership;
- a legitimate source conversion cannot remain explicit in an adapter;
- performance or memory measurements identify material cost;
- M3 persistence becomes coupled to application models;
- framework errors leak into a public contract;
- a second case reveals a missing non-optional invariant;
- replay requires a different version boundary;
- Pydantic v3 or another breaking upgrade is considered;
- later internal computation materially benefits from framework-independent dataclasses.

Changes must identify affected contracts, compatibility or migration consequences, evidence, and whether a new ADR or plan amendment is required.

## 14. Immediate continuation

1. Treat ADR-0002 as the accepted representation/runtime-validation decision.
2. Update the active M2 plan state and tracker from method selection to implementation activation.
3. Teach only the Pydantic concepts needed to understand and own the first contract implementation.
4. Create the minimum `pyproject.toml` with the reviewed Pydantic v2 dependency range.
5. Create `src/upgradepilot/__init__.py` and verify editable installation/import resolution.
6. Write the first valid nested-contract test before behavioral implementation.
7. Continue through invalid, non-mutation, Ali-directed modification, and diagnosed-failure evidence.