# ADR-0002 — Pydantic for Runtime Contract Models

**Status:** Accepted  
**Date:** 2026-07-21  
**Owner:** Ali Rajabi  
**Scope:** Activated M2 and related M3 boundary/trusted application contracts

## Context

UpgradePilot repeatedly crosses boundaries between untrusted or manually assembled data and trusted application records. The activated contract requires:

- exact required fields and runtime types;
- explicit limited normalization;
- field and cross-field invariants;
- nested semantic composition;
- raw-input preservation;
- mutation-resistant trusted records;
- structured validation failures;
- machine-readable serialization;
- separation from persistence and public report schemas.

The framework-independent requirements are controlled by `../specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`.

## Decision

Adopt **Pydantic v2** for activated boundary and trusted application contracts beginning in M2.

```text
raw/manual or external data
→ preserve raw form
→ boundary validation
→ explicit adapter
→ strict nested trusted Pydantic models
→ later separate persistence/report mappings
```

This is a bounded adoption. Pydantic is not the complete architecture, raw-evidence store, database model, report architecture, or mandatory representation for every future object.

## Model roles

### Raw data

Raw mappings, text, bytes, files, payloads, or references remain source data. A Pydantic instance is not labeled raw after validation, normalization, rejection, or conversion has occurred.

### M2 boundary model

A flat boundary model may represent the provisional eight-field manual input. It is not the permanent public request and not the trusted semantic identity.

### Trusted application models

Use nested trusted models for:

```text
PullRequestSnapshotIdentity
DependencyChange
ChangedFileEvidence
InitialCaseRecord
```

The exact source-module split remains implementation-bounded.

## Accepted policy

- strict runtime validation by default;
- undeclared fields rejected;
- all activated M2 fields required;
- trusted models frozen;
- trusted changed-file paths stored as `tuple[str, ...]`;
- explicit named flat-to-nested adapter;
- permitted normalization limited to declared trimming and lowercase SHA canonicalization;
- raw mapping/list not mutated or aliased;
- Pydantic `ValidationError` may remain internal during M2;
- no project-wide custom exception hierarchy yet;
- application models remain separate from persistence records and permanent report schemas;
- supported Pydantic v2 APIs only;
- an unreviewed major-version transition is excluded.

Detailed field behavior and proof obligations belong to the technical specification and tests, not this ADR.

## Alternatives

### Plain dictionaries plus explicit validation

Retained for raw source data. Not selected as the trusted-contract baseline because repeated manual enforcement of fields, types, nesting, immutability, errors, and serialization would grow across activated boundaries.

### `TypedDict`

Useful for static typing but does not enforce runtime values and remains a mutable dictionary representation.

### Standard-library dataclasses

Useful internal values in some contexts, but normal dataclasses do not provide the required runtime boundary validation and structured errors by themselves.

### Pydantic boundary plus separate dataclass domain layer

Deferred because it would create two application-object systems and another mapping boundary before demonstrated need. It remains available if Pydantic becomes a real limitation for selected internal computation.

## Consequences

### Benefits

- runtime-enforced trusted contracts;
- nested semantic boundaries;
- consistent strictness and unknown-field policy;
- structured validation evidence;
- mutation-resistant trusted values;
- machine-readable serialization;
- less repeated manual validation infrastructure.

### Costs and risks

- runtime dependency and transitive dependency surface;
- framework API and upgrade coupling;
- risk of hiding transformation inside validators;
- risk of confusing application contracts with raw, persistence, or report representations;
- additional learning and diagnosis surface;
- frozen models do not guarantee deep immutability unless nested values are immutable.

### Controls

- explicit adapters;
- framework-independent specification requirements;
- raw/trusted separation;
- immutable nested collections;
- structured tests for strictness, normalization, nesting, mutation, aliasing, and failures;
- framework-specific errors kept inside the application boundary until a public error contract is intentionally designed.

## Dependency policy

Declare Pydantic as an explicit runtime dependency in `pyproject.toml` using the reviewed v2-compatible range supported by the project Python version. A Pydantic v3 or other breaking major transition requires intentional reassessment.

## Proof

ADR acceptance authorizes the method only. Implementation evidence must demonstrate the applicable specification proof IDs through source, tests, installation/import checks, observed failures, and current working evidence.

Learner ownership is assessed separately. AI-generated implementation or passing AI-generated tests do not establish Ali-owned Pydantic capability.

## Reassessment triggers

Reassess when evidence shows:

- the policy is materially harder to understand or test than a credible simpler baseline;
- legitimate source coercion cannot remain explicit in an adapter;
- Pydantic obscures provenance or raw/trusted separation;
- measured performance or memory cost becomes material;
- persistence becomes tightly coupled to application models;
- framework errors leak into a public contract;
- a breaking major upgrade is considered;
- selected internal computation benefits materially from framework-independent values;
- security, maintenance, or dependency evidence changes the cost assessment.

Possible outcomes include retain unchanged, narrow to boundary-only use, introduce selected dataclasses, or replace with explicit standard-library contracts.

## Deliberately undecided

This ADR does not decide:

- complete provenance/evidence-state classes;
- persistence or ORM technology;
- public CLI/API request and response schemas;
- report contract versioning;
- project-wide custom exceptions;
- whether every later analytical object uses Pydantic;
- complete module/package architecture.

## Ownership note

Ali identified the requirements-before-method gap, challenged premature rejection of Pydantic, and approved the bounded decision. The comparison and document were substantially AI-generated. This supports Ali-directed decision participation, not broad implementation ownership.
