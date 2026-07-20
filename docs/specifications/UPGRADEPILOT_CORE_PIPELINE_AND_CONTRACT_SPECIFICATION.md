# UpgradePilot Core Pipeline and Contract Specification

**Owner:** Ali Rajabi  
**Recorded:** 2026-07-21  
**Status:** Accepted and controlling project-level technical specification; provisional statements are explicitly marked  
**Authority:** Subordinate to the canonical Career governance stack and active M2 authorization; controls UpgradePilot conceptual pipeline, information boundaries, invariants, and method-selection requirements  
**Activation effect:** Clarifies the contracts that current and later implementations must satisfy. It does not by itself authorize broader implementation, select Pydantic or another framework, define a database schema, or establish a complete internal architecture.

## 1. Purpose

UpgradePilot has moved from project selection and planning into implementation. The governing documents define the product mission, evidence doctrine, route, gates, and learning method, but they intentionally do not define the conceptual information boundaries needed to make local implementation decisions coherent.

This specification fills that layer:

```text
product charter and roadmap
→ core pipeline and contract specification
→ architecture/method decisions when required
→ bounded plans and sessions
→ source code, tests, and observed execution
```

It prevents a temporary first-session representation from silently becoming the permanent product model.

## 2. Non-goals

This specification does not:

- pre-create Python classes or source directories;
- select Pydantic, dataclasses, `TypedDict`, plain dictionaries, an Object-Relational Mapper, or another representation mechanism;
- select a database product or persistence schema;
- define a CLI or API design;
- implement acquisition, decision policy, reporting, persistence, evaluation, ML, graphs, LLMs, agents, queues, services, cloud, or deployment;
- require every future concept to be implemented during M2;
- claim that the complete internal architecture is known.

## 3. Controlling principles

The following are **Accepted**.

1. **One continuous product flow.** Every implemented responsibility must reconnect to the path from a real dependency-update PR to a traceable recommendation or abstention.
2. **Separate source form from trusted form.** Raw source data is preserved; normalized or interpreted data does not overwrite it.
3. **Separate observation from interpretation and decision.** A fact acquired from a source, an inferred relationship, an evidence-quality state, and a recommendation are different concepts.
4. **Snapshot correctness.** Evidence and conclusions must identify the repository and PR revision to which they apply.
5. **Provenance continuity.** Material normalized evidence and report claims must resolve to preserved origin, time/revision context, and transformation identity.
6. **Explicit degradation.** Missing, inaccessible, stale, conflicting, invalid, rejected, unsupported, and not-applicable states must not collapse into a silent empty value.
7. **Deterministic baseline.** The same accepted inputs and decision-rule version must produce the same deterministic result.
8. **Boundary-specific validation.** Invalid caller input, malformed source data, unavailable evidence, and internal defects are not one universal failure category.
9. **Strict trusted contracts.** Automatic coercion may occur only in an explicitly named adapter or normalization step. Trusted downstream records must not hide how a value changed type or meaning.
10. **Representation follows responsibility.** A framework or class mechanism is selected only after the required contract, lifecycle, serialization, persistence, and failure behavior are understood.
11. **Persistence separation.** Application contracts and database records may map to one another, but neither is assumed to be the other.
12. **Version-aware evolution.** Persisted or externally serialized records must eventually identify the schema or contract version required for replay.
13. **Implement only activated concepts.** Defining a conceptual object here does not authorize its code during the current milestone.

## 4. Conceptual product pipeline

The complete conceptual flow is:

```text
Maintainer or operator request
→ acquisition request validation
→ source acquisition or accepted manual evidence
→ raw source preservation
→ source-specific parsing
→ normalization
→ structural and semantic validation
→ evidence-state classification
→ case assembly
→ repository/dependency context enrichment
→ decision-input assembly
→ deterministic recommendation or abstention
→ human-readable and machine-readable report
→ persistence and replay
→ evaluation corpus and later experiments
```

The stages may be executed incrementally, but their boundaries must remain explicit.

## 5. Core conceptual contracts

### 5.1 Acquisition Request

**Status:** Provisional for M2; expanded in M3.

Purpose: identify what the system should inspect or replay.

Likely accepted forms:

- repository plus PR number;
- canonical public PR URL;
- a preserved manual/offline evidence package when that interface is admitted.

The acquisition request is not the complete case identity and does not need to contain facts that UpgradePilot is responsible for acquiring.

Minimum provisional M2 locator:

```text
repository
pr_number
```

Open decisions:

- whether URL input is accepted in the first bounded interface;
- whether repository names are canonicalized beyond surrounding-whitespace removal;
- where source-specific convenience conversion occurs.

### 5.2 Pull Request Snapshot Identity

**Status:** Accepted concept; M2 fields are provisional.

Purpose: identify the exact PR revision to which evidence and conclusions apply.

Core fields:

```text
repository
pr_number
base_sha
head_sha
```

Invariants:

- repository identifies one supported GitHub owner/repository pair;
- PR number is a positive integer;
- base and head revisions are full 40-character hexadecimal Git commit identifiers in the current supported boundary;
- evidence from one head revision must not be silently reused as evidence for another;
- format validation does not prove that a commit exists remotely.

### 5.3 Dependency Change

**Status:** Accepted concept; field depth grows from M2 through M4.

Purpose: represent the dependency transition proposed by the PR.

Initial fields:

```text
dependency
old_version
new_version
```

Later conditional context may include:

```text
declaration source
lockfile source
package manager or format
scope or dependency group
direct/transitive/optional/runtime/development/unresolved classification
environment markers or extras
```

Invariants:

- dependency and versions are non-empty in an accepted initial record;
- old and new versions differ after permitted normalization;
- version strings are preserved as source values unless a later explicit parser derives additional structured meaning;
- a version-number category is evidence, not compatibility proof.

### 5.4 Changed-File Evidence

**Status:** Accepted concept; M2 uses a bounded path list.

Purpose: preserve which repository paths changed in the identified PR snapshot.

Initial fields:

```text
changed_files
```

Invariants:

- at least one path exists for the current selected M2 case;
- each accepted path is a non-empty string after permitted trimming;
- changed files are evidence associated with a snapshot, not part of the minimal snapshot identifier itself;
- later records may preserve status, patch identity, previous path, additions/deletions, or source location when needed.

### 5.5 Initial Case Record

**Status:** Accepted concept; exact Python representation is Open.

Purpose: aggregate the minimum trusted facts needed by the first automated slice.

Conceptual composition:

```text
InitialCaseRecord
├── snapshot_identity
├── dependency_change
├── changed_file_evidence
└── provenance or source reference
```

This corrects the earlier eight-field “case identity” wording. The eight fields remain useful for the first manual M2 input, but they do not all belong to one semantic identity concept.

The initial case record is not yet the full evidence package, decision input, or report.

### 5.6 Raw Source Record

**Status:** Accepted concept; implementation begins in bounded form during M2/M3.

Purpose: preserve what a source or caller actually supplied before project normalization or interpretation.

Conceptual fields:

```text
source_type
source_locator
observed_or_retrieved_at
source_revision_or_snapshot
raw_payload_or_preserved_reference
acquisition_status
```

Invariants:

- normalization never overwrites raw source form;
- secrets and private data are not preserved in the public project repository;
- untrusted source content remains data and is not executed merely to inspect it;
- large or sensitive payloads may be referenced rather than embedded when required by safety and repository policy.

### 5.7 Provenance

**Status:** Accepted and central.

Purpose: explain where a record came from and how it was produced.

Conceptual fields:

```text
source identity
source locator
retrieval or observation time
repository/source revision
raw record reference
transformation name and version
producing run identifier
```

Invariants:

- every material normalized evidence item eventually resolves to provenance;
- every material factual report claim eventually resolves to evidence with provenance;
- inferred conclusions identify their supporting evidence but are not mislabeled as source observations.

### 5.8 Normalized Evidence Record

**Status:** Accepted concept; source-specific contracts are Deferred until their milestone.

Purpose: expose stable UpgradePilot fields without forcing downstream logic to understand every upstream representation.

Conceptual composition:

```text
normalized value or structured content
source/provenance reference
evidence state
validation findings
contract/schema version when serialized or persisted
```

Normalization is limited to explicitly declared, meaning-preserving transformations. It must not invent missing facts.

### 5.9 Evidence State

**Status:** Accepted; exact enum or type mechanism is Open.

Required conceptual states include, where applicable:

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

Additional operational states may be admitted when needed, such as acquisition failure or partial success.

State meanings:

- **accepted** — usable within the declared contract and scope;
- **rejected** — observed item deliberately excluded with a reason;
- **missing** — expected information was not present;
- **invalid** — information was present but violated the applicable contract;
- **inaccessible** — the source or item could not be retrieved under the supported method;
- **stale** — available evidence does not match the required time or revision boundary;
- **conflicting** — relevant sources disagree and the conflict is unresolved;
- **unsupported** — the current implementation cannot interpret the format or situation;
- **not_applicable** — the evidence category is legitimately irrelevant to the case.

An evidence state is data used by later degradation and abstention logic. It is not automatically an exception.

### 5.10 Repository and Dependency Context

**Status:** Accepted concept; implementation Deferred to M4 except for the initial dependency change.

Purpose: represent declaration, resolution path, source usage, tests, workflows, and known limitations relevant to the update.

The context may contain observations, inferred relationships, unresolved paths, and limitation records. It must not convert static references into runtime causality proof.

### 5.11 Decision Input

**Status:** Accepted concept; implementation begins later in M2 and stabilizes through M5.

Purpose: provide the deterministic decision responsibility with an explicit, versioned set of accepted evidence and unresolved states.

Conceptual fields:

```text
case reference
accepted evidence references
missing/conflicting/inaccessible states
repository/dependency context
rule or policy version
known limitations
```

The decision input must not silently read arbitrary global or mutable state.

### 5.12 Decision Result

**Status:** Accepted concept; detailed contract Deferred to the decision-path session.

Purpose: represent the bounded maintainer action and its support.

Core result family:

```text
merge after normal review
run targeted checks
investigate or block
defer
abstain
```

Conceptual fields may include:

```text
recommendation class
rationale
named targeted checks
uncertainty or insufficiency findings
material evidence references
limitations
rule version
```

### 5.13 Report

**Status:** Accepted concept; implementation Deferred until the first report slice.

Purpose: expose the result in human-readable and machine-readable forms without losing traceability.

Invariants:

- factual claims resolve to evidence;
- observations, interpretations, uncertainty, and recommendations remain distinguishable;
- machine-readable output has stable field names and eventually an explicit contract version;
- report wording does not claim that passing CI, SemVer, merged status, or one score proves safety.

### 5.14 Run Record and Replay

**Status:** Accepted concept; implementation Deferred to M3.

Purpose: identify one execution, its inputs, source snapshots, transformations, versions, outputs, failures, and replay/duplicate behavior.

The run record links the otherwise separate contracts into a reproducible execution history.

### 5.15 Evaluation Case and Experiment Record

**Status:** Accepted conceptual need; implementation Deferred to M5/M6.

Evaluation records eventually preserve:

- case/corpus identity and version;
- adjudication, disagreement, or unadjudicable state;
- split identity and leakage controls;
- method/rule/model/prompt/feature version;
- prediction or recommendation;
- metrics and denominators;
- error classification;
- cost, latency, and adoption decision.

These contracts must not treat historical PR disposition as objective truth.

## 6. Validation, normalization, and failure boundaries

### 6.1 Boundary validation

**Accepted distinction:**

```text
caller/request validation
source parsing validation
normalized evidence validation
cross-record semantic validation
decision sufficiency checks
internal programmer/runtime defects
```

These may use different error or result mechanisms.

### 6.2 Permitted normalization

A normalization is allowed only when it is:

- explicitly declared;
- deterministic;
- meaning-preserving within the supported boundary;
- traceable when it changes a material representation.

For the provisional M2 manual input, permitted normalization is limited to surrounding-whitespace removal from declared string fields and changed-file paths.

Not permitted in M2 without a new explicit rule:

- guessing missing repository owners or names;
- completing shortened SHAs;
- correcting dependency spelling;
- parsing or rewriting version semantics;
- converting arbitrary strings to integers;
- resolving path separators, `.`/`..`, or repository filesystem meaning;
- silently removing duplicate paths;
- inventing missing fields.

### 6.3 Strictness and coercion

**Accepted principle:** trusted contracts are strict.

**Provisional M2 rule:**

- `pr_number` must arrive as an integer and not a boolean;
- strings are not silently converted into integers at the trusted manual-input boundary;
- any future convenience conversion belongs in an explicit adapter and must have tests and documented behavior.

### 6.4 Failure and degradation categories

The project distinguishes:

1. **Reject request** — the acquisition/manual request itself cannot be interpreted safely.
2. **Reject record** — one proposed trusted record violates required structural or semantic invariants.
3. **Preserve evidence state** — evidence is missing, inaccessible, stale, conflicting, unsupported, rejected, or not applicable, and the run may continue.
4. **Degrade result** — available evidence supports only a weaker report or named targeted checks.
5. **Abstain** — evidence is insufficient or conflicting beyond the accepted decision boundary.
6. **Fail run** — configuration, persistence, programming, or unexpected operational failure prevents a trustworthy result.

A single `ValueError` may be sufficient inside one small M2 implementation, but it is not accepted as the permanent project-wide failure model.

## 7. M2 manual-input contract

### 7.1 Purpose

**Provisional:** M2 begins from a manually assembled input created from the completed M1 evidence report. This is a learning and vertical-slice adapter, not the eventual public maintainer interface.

### 7.2 Required supplied fields

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

### 7.3 Semantic mapping

```text
repository + pr_number + base_sha + head_sha
→ PullRequestSnapshotIdentity

dependency + old_version + new_version
→ DependencyChange

changed_files
→ ChangedFileEvidence

all three + preserved raw/manual source reference
→ InitialCaseRecord
```

### 7.4 Provisional rules

- all eight fields are required for this manual adapter;
- unknown top-level fields are rejected unless the chosen method decision explicitly changes this rule;
- accepted types are exact and not silently coerced;
- declared strings and changed-file paths are trimmed at their boundaries;
- repository uses basic `owner/name` form;
- PR number is a positive integer and not a boolean;
- base/head SHAs are exactly 40 hexadecimal characters;
- dependency and version strings are non-empty;
- old and new versions differ;
- changed files is a non-empty list of non-empty strings;
- output is a separate trusted record and does not mutate the raw input;
- the output's nested mutable structures, if any, do not alias raw mutable structures;
- no partially accepted initial case record is returned when this bounded adapter fails.

### 7.5 Required tests after representation selection

The first implementation must prove at least:

- the real M1 case maps into the expected conceptual components;
- permitted whitespace normalization occurs;
- raw input and its changed-file list remain unchanged;
- a malformed head SHA is rejected;
- equal old/new versions or an empty changed-file path is covered through the Ali-directed modification;
- one changed/failing case is interpreted and repaired.

## 8. Representation and validation method decision

**Status:** Open and required before M2 source implementation.

Candidate mechanisms may include:

- plain dictionaries plus explicit functions;
- `TypedDict` plus runtime validation functions;
- standard-library dataclasses;
- Pydantic models;
- a purpose-specific combination.

The comparison must evaluate:

1. runtime enforcement of required fields and exact types;
2. strict-versus-coercing behavior;
3. field and cross-field validation;
4. normalization order and visibility;
5. immutable or mutation-resistant trusted records;
6. nested conceptual composition;
7. structured error reporting;
8. JSON or machine-readable serialization;
9. schema/contract versioning support;
10. compatibility with later persistence without coupling application models to database rows;
11. dependency, upgrade, security, and maintenance cost;
12. testing clarity and failure diagnosis;
13. Ali's ability to explain, modify, test, and own the selected mechanism;
14. the simplest baseline and reversal path.

A consequential framework adoption should be recorded in an ADR after comparison. A reversible local mechanism that creates no durable cross-project consequence may be recorded in the active plan and working memory instead.

## 9. Milestone activation map

### M2 — First automated vertical slice

Activate only:

- manual acquisition/input adapter;
- raw-input preservation;
- snapshot identity;
- dependency change;
- changed-file evidence;
- initial case record;
- the minimum evidence-state behavior needed by malformed or missing input;
- later bounded decision/report contracts as separate sessions authorize them.

Do not implement the complete object inventory merely because it is defined here.

### M3 — Reliable evidence and persistence

Activate:

- source-specific acquisition contracts;
- raw source records and provenance;
- normalized evidence records;
- explicit partial-source failure and evidence states;
- run records, replay/duplicate semantics;
- persistence mappings and schema versioning;
- structured errors/logs and integration/failure/recovery tests.

### M4 — Repository-specific context

Activate:

- declaration and lock evidence;
- dependency relationships and paths;
- import/reference/test/workflow evidence;
- source locations, revisions, and reachability limitations.

### M5 — Deterministic baseline and evaluation

Activate:

- versioned decision input/result contracts;
- decision table and evidence-sufficiency rules;
- corpus, adjudication, split, metric, and error-analysis records.

### M6 and later

Activate only evidence-admitted experiment, model, graph, grounded-LLM, MLOps, queue, service, orchestration, and deployment records.

## 10. Accepted, provisional, open, deferred, and rejected decisions

### Accepted

- separate acquisition request, snapshot identity, dependency change, changed-file evidence, and aggregate initial case record;
- preserve raw input/source form separately from normalized/trusted form;
- provenance and evidence states are central contracts;
- missing/inaccessible/conflicting evidence is not automatically invalid caller input;
- trusted records do not silently coerce values;
- application, persistence, and report representations are conceptually distinct;
- future serialized/persisted contracts require version-aware evolution;
- implementation remains milestone-activated and bounded.

### Provisional for M2

- manually assembled eight-field input from the M1 report;
- strict exact types at that boundary;
- reject unknown top-level fields;
- whitespace trimming as the only normalization;
- one aggregate initial case record as the trusted output;
- full 40-character SHA requirement.

### Open before M2 implementation

- exact Python representation mechanism;
- whether the trusted output remains nested or uses a small flat compatibility view;
- exact exception/result API for the bounded adapter;
- exact class and function names;
- whether a framework dependency is justified and adopted.

### Deferred

- public CLI/API input design;
- source-specific API response schemas;
- complete evidence model hierarchy;
- database schema and ORM decision;
- report schema version format;
- repository-context, evaluation, and experiment object details;
- custom project-wide exception hierarchy.

### Rejected under current evidence

- treating all eight fields as one permanent semantic identity object;
- allowing normalization to invent missing meaning;
- using one universal failure category for all later evidence states;
- coupling the first application object directly to a future database table;
- implementing every conceptual object during M2;
- choosing a framework solely because it can express the current validation rules.

## 11. Reassessment triggers

Revisit this specification when:

- a real supported source cannot map without losing material meaning;
- the first M2 representation comparison reveals an invariant that is impractical or contradictory;
- replay or persistence requires a different version boundary;
- a second case exposes fields that are not optional but were omitted;
- report claim tracing cannot resolve cleanly through provenance;
- evidence-state semantics create ambiguous decision behavior;
- a later milestone formally expands the supported ecosystem boundary.

Changes must identify the affected contracts, migration or compatibility consequence, evidence, and whether an ADR or plan amendment is required.

## 12. Immediate continuation

1. Treat the original eight-field wording as a provisional manual M2 adapter, not the whole product input or one permanent identity object.
2. Compare the candidate Python representation/validation methods against Section 8.
3. Select the smallest method that satisfies the activated M2 contract while preserving a credible path to M3.
4. Record a durable framework or representation adoption through an ADR when the comparison justifies one.
5. Amend the active test-first sequence to target the `InitialCaseRecord` conceptual contract.
6. Only then create package metadata, source, and tests.
