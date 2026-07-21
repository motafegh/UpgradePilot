# ADR-0002 — Pydantic for Runtime Contract Models

**Status:** Accepted  
**Date:** 2026-07-21  
**Owner:** Ali Rajabi  
**Decision scope:** M2 and M3 runtime application contracts  
**Authority:** Implements the representation-method decision required by `../specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md` and the active Career M2-S01 amendment. It is subordinate to the UpgradePilot charter and canonical Career governance.

## 1. Context

UpgradePilot must repeatedly cross boundaries between untrusted or manually assembled data and trusted application records. The accepted core specification requires:

- exact required fields and runtime types;
- explicit, meaning-preserving normalization;
- field-level and cross-field invariants;
- nested composition of distinct concepts;
- raw-input preservation;
- mutation-resistant trusted records;
- structured validation failures;
- machine-readable serialization;
- a credible path to M3 provenance, evidence states, replay, and diagnostics;
- separation between application contracts, persistence records, and report schemas.

The first M2 input is a flat, manually assembled eight-field mapping, but the trusted result is not one flat semantic identity. It contains:

```text
PullRequestSnapshotIdentity
+ DependencyChange
+ ChangedFileEvidence
→ InitialCaseRecord
```

The method comparison considered plain dictionaries, `TypedDict`, standard-library dataclasses, Pydantic, and combinations.

## 2. Decision

Adopt **Pydantic v2** as UpgradePilot's runtime validation and trusted application-contract framework beginning with the activated M2 contracts and continuing into M3 where the same boundary needs recur.

This is a bounded adoption. Pydantic is not the whole architecture, the raw-evidence store, the database model, the report architecture, or a mandatory representation for every later analytical object.

The accepted data flow is:

```text
raw/manual or external source data
→ preserve raw form
→ source-specific boundary model or adapter
→ explicit transformation
→ strict nested trusted Pydantic models
→ later separate persistence/report mappings
```

## 3. Accepted model roles

### 3.1 Raw data

Raw manual input and later raw source payloads remain plain source data or preserved source records, such as JSON-compatible mappings, text/bytes, files, or references.

A Pydantic model must not be labeled raw when model creation has already validated, normalized, rejected, or converted the supplied values.

```text
raw source
≠ validated boundary input
≠ trusted application record
```

### 3.2 M2 manual boundary

Create one flat boundary model provisionally named:

```text
ManualCaseInput
```

It represents only the current M2 manual adapter contract. It is not `CaseIdentity` and not the permanent public product input.

### 3.3 Trusted application contracts

Create nested trusted Pydantic models provisionally named:

```text
PullRequestSnapshotIdentity
DependencyChange
ChangedFileEvidence
InitialCaseRecord
```

Conceptual composition:

```text
InitialCaseRecord
├── snapshot_identity: PullRequestSnapshotIdentity
├── dependency_change: DependencyChange
└── changed_file_evidence: ChangedFileEvidence
```

The exact source module split remains implementation-bounded. Do not pre-create speculative package layers.

## 4. Model policy

### 4.1 Strict trusted contracts

Trusted and boundary models use strict runtime validation by default.

Accepted behavior includes:

```text
pr_number = 13432     → acceptable subject to remaining rules
pr_number = "13432"   → rejected at this boundary
pr_number = True      → rejected
```

Convenience conversion may exist later only in an explicitly named source adapter with declared behavior and tests.

### 4.2 Unknown fields

Validated M2 boundary and trusted models forbid undeclared fields.

Unknown fields remain preserved in raw source records when applicable, but they must not silently enter or disappear from a trusted contract.

### 4.3 Mutation resistance

Trusted models are configured as frozen. Because framework-level freezing is not absolute deep immutability, nested collections use immutable types where practical.

For M2:

```text
ChangedFileEvidence.paths: tuple[str, ...]
```

The manual input may contain a list. The adapter creates a new tuple and must not mutate or alias that raw list.

### 4.4 Required versus optional fields

All current M2 fields are required. A field becomes optional only when the containing record remains valid without it and absence has a defined semantic meaning.

For example, `head_sha` is not optional in an accepted `PullRequestSnapshotIdentity` because the record must identify an exact PR snapshot.

## 5. Normalization policy

Permitted M2 normalization is explicit and limited:

- trim surrounding whitespace from declared text fields;
- trim surrounding whitespace from each changed-file path;
- canonicalize accepted hexadecimal SHAs to lowercase;
- preserve repository, dependency, version, and path spelling/casing otherwise.

Not permitted:

- type coercion hidden inside trusted models;
- repository-owner guessing;
- shortened-SHA completion;
- dependency spelling correction;
- Semantic Versioning parsing or rewriting;
- path canonicalization beyond trimming;
- silent duplicate removal;
- invented missing values.

Duplicate changed-file paths after normalization are rejected rather than silently deduplicated. Source order is preserved.

## 6. Validation placement

Use the framework for declared field/type constraints and focused field or model invariants.

Keep flat-to-nested assembly explicit:

```text
ManualCaseInput validation
→ named adapter/transformation function
→ PullRequestSnapshotIdentity
→ DependencyChange
→ ChangedFileEvidence
→ InitialCaseRecord
```

Do not hide the complete flat-to-nested transformation inside one broad pre-validation hook. The transformation must remain directly testable, traceable, and replaceable.

Representative invariants include:

- repository has one non-empty `owner/name` pair in the current basic boundary;
- PR number is a positive non-boolean integer;
- base and head SHAs contain exactly 40 hexadecimal characters;
- dependency and versions are non-empty;
- old and new versions differ after normalization;
- changed-file paths are non-empty and unique after normalization.

Format validation does not prove that a repository, PR, commit, dependency, or path exists remotely.

## 7. Error policy

During M2, validation failures may surface as Pydantic `ValidationError` internally.

Tests should prefer stable structured properties such as:

- error location;
- error type/code;
- failed contract or field;
- relevant message meaning.

Tests should avoid coupling to the complete rendered error string when a structured assertion is available.

Do not create a project-wide custom exception hierarchy during the first implementation.

Before a public CLI/API/report error boundary is accepted, translate framework-specific errors into an UpgradePilot-owned error/result contract. Public behavior must not become permanently coupled to Pydantic's exact error rendering.

Invalid manual input remains distinct from later evidence states such as missing, inaccessible, stale, conflicting, rejected, unsupported, or not applicable.

## 8. Serialization and versioning

Pydantic serialization may be used for internal machine-readable output and tests through supported v2 APIs such as `model_dump()` and `model_dump_json()`.

Do not add a schema-version field to every M2 internal value object yet.

Explicit contract versioning becomes mandatory when a representation first crosses a durable boundary, including:

- persisted normalized records;
- replay of earlier runs;
- machine-readable report contracts;
- public API requests or responses;
- exported evaluation datasets.

Version the appropriate persisted or serialized envelope rather than automatically versioning every nested value object.

## 9. Persistence separation

Pydantic application contracts are not relational table definitions or Object-Relational Mapper entities.

```text
Pydantic application contract
≠ persistence row/entity
≠ public report schema
```

M3 must design explicit mappings based on relational keys, relationships, provenance, history, replay, and query requirements. Similar field names do not make the responsibilities identical.

## 10. Dependency policy

The implementation will add Pydantic as an explicit runtime dependency in `pyproject.toml`.

Use the Pydantic v2 API family and exclude an unreviewed major-version transition. The exact compatible lower bound will be selected during package setup against the project's Python version and verified installation; Pydantic v3 requires reassessment and an intentional dependency update.

Do not rely on deprecated Pydantic v1 APIs.

Primary documentation reviewed for this decision:

- Pydantic model configuration and strict mode;
- field/model validators;
- validation errors;
- model serialization;
- current PyPI release and Python support metadata.

## 11. Alternatives considered

### 11.1 Plain dictionaries plus explicit functions

**Advantages**

- no runtime dependency;
- mechanics are fully visible;
- easy to start.

**Reasons not selected as the trusted-contract baseline**

- repeated manual enforcement of fields, types, nesting, immutability, errors, and serialization;
- weak protection against callers bypassing validation;
- growing duplication across M3 source and evidence contracts;
- higher risk that raw and trusted dictionaries become confused.

Plain dictionaries remain accepted for raw source payloads and narrow intermediate data where no trusted contract is claimed.

### 11.2 `TypedDict` plus runtime validation

**Advantages**

- improves static readability while retaining dictionary behavior;
- no runtime dependency.

**Reasons not selected alone**

- `TypedDict` does not enforce runtime values;
- still requires a separate validation, normalization, error, and immutability layer;
- trusted values remain mutable dictionaries.

### 11.3 Standard-library dataclasses

**Advantages**

- concise typed value objects;
- `frozen=True` supports mutation resistance;
- no external runtime dependency.

**Reasons not selected alone**

- normal dataclasses do not enforce annotated types at runtime;
- substantial manual boundary validation and structured error handling would still be required;
- repeated conversion/validation code would grow across M3.

### 11.4 Pydantic boundary models plus separate dataclass domain models

**Advantages**

- very strict separation between input validation and internal domain values;
- dataclasses can remain framework-independent.

**Reasons deferred**

- creates two application object systems and an additional conversion boundary before demonstrated need;
- increases implementation and learning surface in the first vertical slice;
- later introduction remains possible if Pydantic becomes a real limitation for internal computation-heavy models.

## 12. Consequences

### Positive

- runtime-enforced trusted contracts;
- clear nested semantic boundaries;
- structured validation failures;
- consistent strictness and extra-field policy;
- built-in machine-readable serialization;
- credible reuse for M3 acquisition and normalized evidence boundaries;
- less repeated validation infrastructure;
- explicit dependency decision rather than accidental framework use.

### Costs and risks

- external runtime dependency and transitive dependency surface;
- Pydantic API and upgrade coupling;
- risk of hiding transformations inside validators;
- risk of confusing Pydantic models with raw evidence or persistence entities;
- framework concepts add learning and diagnosis requirements;
- frozen models provide only framework-level or shallow protection unless nested values are immutable.

### Controls

- explicit adapters for source transformation;
- raw/trusted separation;
- immutable nested collections;
- no deprecated v1 APIs;
- framework-specific errors remain internal;
- separate persistence/report design;
- implementation tests must prove strictness, normalization, nesting, non-mutation, and failure behavior.

## 13. Implementation proof required

ADR acceptance authorizes the dependency and method, but it does not prove the decision works.

M2-S01 must demonstrate:

1. editable installation with the selected Pydantic dependency;
2. import resolution from `src/upgradepilot/`;
3. a valid manual input producing the expected nested `InitialCaseRecord`;
4. strict rejection of a string PR number and boolean PR number, when covered by the bounded test set;
5. whitespace normalization and lowercase SHA canonicalization;
6. malformed head-SHA rejection;
7. raw dictionary and raw changed-file list remain unchanged;
8. trusted paths are stored without mutable aliasing;
9. equal old/new versions or duplicate/empty changed paths are rejected through the authorized changed case;
10. one intentionally failing test is diagnosed and repaired;
11. Ali can locate, explain, modify, test, and reproduce a representative central behavior at the depth claimed.

## 14. Reassessment triggers

Reassess this ADR when:

- M2 implementation shows the selected policy is materially harder to understand or test than the baseline;
- a supported source requires legitimate coercion that cannot remain explicit in an adapter;
- Pydantic behavior obscures provenance or raw/trusted separation;
- performance or memory measurements show material cost in a real workload;
- M3 persistence becomes tightly coupled to application models;
- framework-specific errors leak into a public contract;
- Pydantic v3 or another breaking upgrade is considered;
- a later internal computation path benefits materially from framework-independent dataclasses;
- security, maintenance, or dependency evidence changes the cost assessment.

Possible outcomes are adopt unchanged, narrow scope, retain as a boundary-only framework, introduce dataclasses for selected internal values, replace with explicit standard-library contracts, or defer further expansion.

## 15. Deliberately undecided

This ADR does not decide:

- exact Python module/file names beyond the activated contract;
- complete provenance or evidence-state classes;
- database, ORM, or migration technology;
- public CLI/API request and response schemas;
- report contract version format;
- Semantic Versioning or package-name value types;
- a project-wide custom exception hierarchy;
- whether every M4–M6 analytical record uses Pydantic;
- complete internal package layering.

## 16. Assistance and ownership

The method recommendation and ADR wording are substantially AI-generated. Ali:

- proposed Pydantic as a serious candidate;
- challenged its premature rejection based only on the earlier narrow session scope;
- required the decision to be evaluated against the whole project trajectory;
- reviewed and explicitly approved the proposed design direction.

This establishes an **Ali-directed architecture decision**, not practical Pydantic, packaging, testing, or application ownership. Ownership evidence remains an implementation requirement.