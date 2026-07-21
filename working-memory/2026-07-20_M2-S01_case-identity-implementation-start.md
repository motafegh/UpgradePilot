# M2-S01 Working Memory — Initial Case Contract and Pydantic Decision

**Date:** 2026-07-20 to 2026-07-21  
**Session:** M2-S01 continuation  
**Status:** Active  
**Route / milestone:** R2 / M2 — First automated vertical slice  
**Mode:** Green  
**Focused minutes:** Not recorded

## Current objective

Implement the first trusted UpgradePilot case transformation under the accepted core specification and ADR-0002:

> Receive a manually assembled input derived from the M1 case, preserve the raw input, validate and normalize the activated fields, and construct one strict nested `InitialCaseRecord` that separates PR snapshot identity, dependency change, and changed-file evidence.

The representation-method decision is closed. The active work now moves to minimum Pydantic learning, package setup, valid-test-first implementation, failure diagnosis, and ownership evidence.

## Starting state

At activation of this continuation:

- the initial source/package layout was accepted through `docs/architecture/ADR-0001-initial-python-source-layout.md`;
- the repository/product name was `UpgradePilot`;
- the Python distribution and import package name was `upgradepilot`;
- no `pyproject.toml`, source package, implementation module, or test module existed;
- the original M2 plan described eight fields as one case-identity dictionary;
- no representation method or runtime dependency had been selected.

## Calibration and correction evidence

Ali stated that validation, cleaning, and rule-definition methods felt familiar conceptually and that the session should not manufacture difficulty merely because Python syntax or implementation details remained unproven.

Ali proposed Pydantic as a possible way to provide:

- required-field checks;
- runtime type validation;
- normalization order;
- field and cross-field validation;
- new-output construction;
- non-mutation;
- structured failure behavior.

The first AI response rejected Pydantic because the narrow pre-implementation plan prohibited schema frameworks and external dependencies. Ali challenged that reasoning correctly:

- the project should not preserve a weaker method merely because an earlier plan assumed one;
- method selection must consider the full UpgradePilot trajectory;
- rules and product contracts must precede framework mechanics;
- assessment should allow Ali to complete his reasoning before the AI supplies alternatives.

This exposed a missing project-level technical-contract layer and led to the accepted core specification and Career amendment.

## Accepted semantic correction

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

The flat eight-field mapping remains a provisional M2 manual adapter. It is not the eventual public input and not one permanent identity object.

## Whole-project boundaries retained

The specification records and separates:

- acquisition request;
- PR snapshot identity;
- dependency change;
- changed-file evidence;
- initial case record;
- raw source record;
- provenance;
- normalized evidence;
- evidence states;
- repository/dependency context;
- decision input and result;
- report;
- run/replay record;
- evaluation and experiment records.

Only the activated M2 contracts are implemented now.

## Representation comparison completed

Candidates examined:

- plain dictionaries plus explicit validation functions;
- `TypedDict` plus runtime validation;
- standard-library dataclasses;
- Pydantic models;
- Pydantic boundary models plus separate dataclass domain models.

### Plain dictionaries

Useful for preserving raw source data, but not selected as the trusted-contract baseline because required fields, runtime types, nesting, mutation protection, structured errors, and serialization would need repeated manual infrastructure across M2 and M3.

### `TypedDict`

Useful for static readability, but not selected alone because it does not enforce runtime values and trusted records would remain mutable dictionaries.

### Dataclasses

Useful for framework-independent value objects and frozen instances, but not selected alone because normal dataclasses do not enforce annotated types at runtime and would still require a substantial boundary-validation layer.

### Pydantic plus separate dataclasses

Technically credible, but deferred because it creates two application object systems and an additional conversion boundary before demonstrated need.

### Selected method

Pydantic v2 is accepted for strict runtime boundary and trusted application contracts beginning in M2 and continuing into M3 where the same needs recur.

The decision is recorded in:

- `docs/architecture/ADR-0002-pydantic-runtime-contract-models.md`.

## Accepted runtime-contract design

```text
raw manual/external data
→ preserve raw form
→ ManualCaseInput
→ explicit adapter/transformation
→ PullRequestSnapshotIdentity
→ DependencyChange
→ ChangedFileEvidence
→ InitialCaseRecord
```

### Raw data

Raw dictionaries, lists, JSON payloads, text, bytes, files, or references remain outside Pydantic trusted models. A model is not called raw after validation or normalization has occurred.

### M2 boundary model

Provisionally:

```text
ManualCaseInput
```

It accepts the flat M2 fields and represents only this manual adapter.

### Trusted models

Provisionally:

```text
PullRequestSnapshotIdentity
DependencyChange
ChangedFileEvidence
InitialCaseRecord
```

They are nested according to the accepted semantic responsibilities.

### Model policy

- Pydantic v2 APIs;
- strict runtime validation;
- undeclared fields forbidden;
- trusted models frozen;
- changed-file paths stored as `tuple[str, ...]`;
- all activated fields required;
- no hidden trusted-model coercion;
- Pydantic `ValidationError` may remain internal during M2;
- no project-wide custom exception hierarchy yet.

### Adapter policy

The flat-to-nested transformation remains a named, directly tested function or method. Do not hide the complete restructuring in one broad pre-validation hook.

### Persistence and output boundary

```text
Pydantic application contract
≠ database row or ORM entity
≠ permanent public report schema
```

M3 will design explicit persistence mappings from actual relational, provenance, replay, and query needs.

## Activated M2 rules

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

Accepted behavior:

- all fields required;
- exact accepted types; no silent coercion;
- unknown top-level fields rejected;
- trim surrounding whitespace from declared text and paths;
- canonicalize valid SHAs to lowercase;
- basic `owner/name` repository rule;
- positive integer PR number, excluding booleans;
- full 40-character hexadecimal base/head SHAs;
- non-empty dependency and versions;
- old/new versions differ;
- non-empty changed-file input list;
- normalized paths are non-empty and unique;
- source order preserved;
- trusted paths become a tuple;
- raw dictionary and raw path list remain unchanged;
- no mutable alias from raw list to trusted record;
- no partial trusted record after validation failure.

Invalid manual input remains distinct from later missing, inaccessible, stale, conflicting, rejected, unsupported, and not-applicable evidence states.

## Error and test policy

During M2, Pydantic `ValidationError` may surface internally. Tests should assert stable structured details such as error location and type rather than coupling to every character of the rendered message.

A future CLI/API/report boundary must translate framework-specific errors into an UpgradePilot-owned error/result representation.

The first implementation must prove:

1. the real M1 case maps into the nested `InitialCaseRecord`;
2. whitespace normalization and lowercase SHA canonicalization;
3. malformed head SHA rejection;
4. representative strict-type rejection;
5. raw dictionary and list non-mutation;
6. trusted tuple paths do not alias raw mutable data;
7. one Ali-directed change;
8. one intentional test failure is diagnosed and repaired.

## Dependency decision

Pydantic becomes an explicit runtime dependency in `pyproject.toml`.

Use the Pydantic v2 API family and prevent an unreviewed major upgrade. The exact lower bound will be selected during package setup after the project Python version and installation behavior are checked. Pydantic v3 requires reassessment.

Do not use deprecated v1 APIs.

## Assistance and ownership

- Ali identified the missing requirements-before-method problem.
- Ali proposed Pydantic as a serious candidate and challenged its premature rejection.
- The AI produced the detailed comparison, recommendation, and most ADR/specification wording.
- Ali explicitly approved the proposed design direction and authorized it to be recorded.
- The decision is Ali-directed and substantially AI-generated.
- Practical Pydantic, packaging, test, diagnosis, and implementation ownership remain unproven.

## Scope and stop line

In scope now:

- teach the minimum Pydantic v2 mental model needed for this implementation;
- select the initial compatible dependency range;
- create the minimum installable package boundary;
- verify installation and import resolution;
- write the valid nested-contract test first;
- implement only the activated models and adapter;
- test invalid and non-mutation behavior;
- complete one Ali-directed modification and diagnosed failure.

Still out of scope:

- implementing every conceptual contract;
- live multi-source acquisition;
- persistence/database/ORM work;
- full evidence hierarchy;
- recommendation or report responsibilities not separately authorized;
- public CLI/API framework;
- CI, containers, cloud, services, queues, ML, graphs, LLMs, or agents;
- speculative source subpackages;
- restoration of prior scaffold files.

## Exact continuation

### Implementation-onboarding evidence — 2026-07-21

Created:

- `pyproject.toml` with Python `>=3.12`, setuptools build metadata, and `pydantic>=2.13.4,<3`;
- `src/upgradepilot/__init__.py`;
- `src/upgradepilot/case_identity.py`;
- `tests/test_case_identity.py`.

Observed execution:

- the system exposes Python 3.12.3 as `python3`, not `python`;
- `.venv` creation and editable installation succeeded;
- Pydantic 2.13.4 installed and `pip check` reported no broken requirements;
- `upgradepilot` resolved from `src/upgradepilot/__init__.py`;
- the initial test first failed with `ModuleNotFoundError` because `upgradepilot.case_identity` did not exist;
- after the AI-generated full first draft, the real M1 valid-case/non-mutation test passed;
- `compileall` passed;
- a direct invalid-input probe produced structured `int_type` and `extra_forbidden` findings.

Assistance and ownership:

- Ali requested a complete first draft to learn through the real implementation rather than a partial scaffold;
- the package metadata, test, and implementation draft are AI-generated;
- Ali correctly explained strict type rejection and unknown-field rejection;
- practical tracing, invalid-case tests, code modification, and failure diagnosis remain required before ownership or acceptance increases.

## Exact continuation

Trace the full draft through raw preservation, `ManualCaseInput`, field/model validators, explicit nested assembly, trusted frozen models, structured `ValidationError`, and serialization. Then add malformed-head-SHA and representative strict/non-mutation regression tests, complete one Ali-directed code change, and diagnose one intentional failure before accepting the M2-S01 behavior.
