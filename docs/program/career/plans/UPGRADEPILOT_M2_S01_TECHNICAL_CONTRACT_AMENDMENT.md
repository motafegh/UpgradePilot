# UpgradePilot M2-S01 Technical Contract Amendment

**Session ID:** M2-S01  
**Owner:** Ali Rajabi  
**Recorded:** 2026-07-21  
**Status:** Approved and controlling amendment  
**Authority:** Read with [`UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md`](UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md); supersedes conflicting M2-S01 conceptual, method, dependency, deliverable, and stop-line wording only  
**Selected method:** UpgradePilot `docs/architecture/ADR-0002-pydantic-runtime-contract-models.md`  
**Live state:** The canonical tracker and active UpgradePilot working-memory record control gate results, implementation progress, and exact continuation. This amendment defines requirements and consequences, not current completion state.

## 1. Amendment effect

The M2-S01 plan remains controlling for:

- selected real case;
- accepted `src/upgradepilot/` source boundary;
- learning and ownership method;
- test-first execution;
- bounded implementation and forbidden scope;
- installation, import, testing, diagnosis, and evidence requirements.

This amendment controls:

- corrected conceptual contract;
- selected runtime representation method;
- Pydantic v2 dependency authorization;
- strict validation and trusted-model policy;
- flat-to-nested adapter requirement;
- conflicting framework/dependency prohibitions;
- proof obligations created by the method decision.

The controlling UpgradePilot technical artifacts are:

- `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`;
- `docs/architecture/ADR-0002-pydantic-runtime-contract-models.md`.

## 2. Corrected M2-S01 outcome

> Given a manually assembled eight-field input derived from the completed M1 evidence report, preserve the raw input, validate and normalize the activated fields, and construct one trusted nested initial case record separating pull-request snapshot identity, dependency change, and changed-file evidence.

This is the first bounded transformation in the PR-to-report path. It is not the complete M2 vertical slice or eventual public maintainer input interface.

## 3. Corrected conceptual model

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

Required interpretation:

- repository, PR number, base SHA, and head SHA identify the exact PR snapshot;
- dependency and version transition describe the proposed dependency change;
- changed files are snapshot-associated evidence;
- the complete trusted result is a nested initial case record;
- the flat eight-field mapping is a provisional M2 manual adapter only.

## 4. Accepted representation method

**Decision:** Use Pydantic v2 for strict runtime boundary and trusted application contracts beginning in M2 and continuing into the corresponding M3 path.

```text
raw manual or external data
→ preserve raw form
→ ManualCaseInput
→ explicit adapter/transformation
→ PullRequestSnapshotIdentity
→ DependencyChange
→ ChangedFileEvidence
→ InitialCaseRecord
```

Accepted method policy:

- raw payloads remain plain source data or raw-source records;
- activated boundary and trusted application contracts use Pydantic v2;
- validation is strict by default;
- undeclared fields are rejected;
- trusted models are frozen;
- trusted changed-file paths use `tuple[str, ...]`;
- every current M2 field remains required;
- flat-to-nested assembly is explicit, named, and directly tested;
- Pydantic `ValidationError` may remain internal during M2;
- no project-wide custom exception hierarchy is required yet;
- application contracts remain separate from persistence records and public report schemas;
- Pydantic v3 or another breaking major version requires reassessment.

ADR-0002 owns framework-specific API/configuration choices, alternatives, trade-offs, version policy, and reassessment triggers. The technical specification owns framework-independent behavior and invariants.

## 5. Method alternatives and disposition

### Plain dictionaries plus explicit validation

Retained for raw source data. Not selected as the trusted-contract baseline because required fields, runtime typing, nested composition, mutation protection, structured errors, and serialization would require repeated manual infrastructure.

### `TypedDict`

May support static typing but does not enforce runtime values and remains a mutable dictionary representation.

### Standard-library dataclasses

May be used later for selected internal values. Not selected alone because normal dataclasses do not enforce annotated field types at runtime and would still require boundary validation/error infrastructure.

### Pydantic boundary plus separate dataclass domain layer

Deferred because it creates two application object systems and another mapping boundary before demonstrated need.

## 6. Activated manual-input contract

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

Required rules:

- all fields are required;
- unknown top-level fields are rejected;
- accepted types are exact and not silently coerced;
- surrounding whitespace is trimmed from declared strings and changed-file paths;
- valid hexadecimal SHAs are stored lowercase;
- repository follows the current basic `owner/name` rule;
- PR number is positive and not boolean;
- base/head SHAs contain exactly 40 hexadecimal characters;
- dependency and versions are non-empty;
- old and new versions differ;
- raw changed files is a non-empty list;
- normalized paths are non-empty and unique;
- source path order is preserved;
- trusted paths become a tuple;
- raw dictionary and raw list remain unchanged;
- trusted values do not alias raw mutable structures;
- no partial trusted `InitialCaseRecord` is returned on failure.

This validates supplied values. It does not prove remote repository, PR, commit, dependency, or path existence.

## 7. Evidence-state and failure boundary

```text
invalid manual input
≠ missing external evidence
≠ inaccessible source
≠ stale evidence
≠ conflicting evidence
≠ internal runtime or programmer failure
```

Pydantic validation errors are an internal mechanism for this bounded adapter. They are not the permanent project-wide evidence-state or public-error model.

The required semantic order is:

```text
preserve supplied raw mapping
→ exact-type and structural boundary validation
→ permitted normalization
→ field and cross-field semantic validation
→ explicit nested trusted-object creation
```

No partial trusted record is produced after a failed step.

## 8. Method-gate requirements

The representation-method gate is satisfied only when evidence establishes that:

- public acquisition request is distinguished from the complete trusted record;
- exact PR snapshot identity is separated from dependency change and changed-file evidence;
- raw and trusted forms are separate;
- invalid input is distinct from degraded external-evidence states;
- first test boundary and limitations are defined;
- credible representation methods were compared;
- Ali reviewed and approved the selected method at the demonstrated assistance level;
- ADR-0002 records the durable decision.

The tracker records whether and when the gate passed. Passing this decision gate does not establish installation, executable behavior, testing/debugging capability, or ownership.

## 9. Post-amendment required deliverables

The active M2-S01 implementation must:

- teach the minimum Pydantic v2 concepts required to read and direct the implementation;
- establish a reviewed Pydantic v2 dependency range compatible with the project Python version;
- create minimal `pyproject.toml` and `src/upgradepilot/__init__.py`;
- create only source module(s) required by the activated contract;
- create bounded tests under `tests/`;
- verify editable installation and import resolution;
- prove valid nested mapping and permitted normalization;
- prove representative strict invalid behavior;
- prove raw-input non-mutation and no mutable alias;
- complete one Ali-directed central change;
- observe, diagnose, and repair one intentional failure;
- record commands, output, evidence, assistance, capability state, and limitations.

Do not pre-create every conceptual contract in the core specification.

## 10. Required implementation sequence

1. Minimum Pydantic onboarding and representative predictions.
2. Package/dependency boundary and editable-install/import proof.
3. Valid real-case nested-contract test before central behavior.
4. Smallest passing activated models and explicit adapter.
5. Strict invalid, semantic, and non-mutation regression tests.
6. One Ali-directed change.
7. One intentional failure diagnosis and repair.
8. Evidence, assistance, limitations, and state update through the tracker/working record.

The exact current substep is not stored in this amendment.

## 11. Proof obligations

At minimum, evidence must cover:

- package installation and import path;
- exact required field/type behavior;
- unknown-field rejection;
- repository and PR-number rules;
- base/head SHA validation and lowercase storage;
- non-empty dependency/version/path rules;
- differing old/new versions;
- unique normalized changed-file paths with source order preserved;
- nested trusted-record assembly;
- frozen trusted models and immutable path tuple;
- raw mapping/list non-mutation and no alias;
- no partial trusted record on failure;
- structured malformed-head-SHA evidence;
- one Ali-directed change and diagnosed failure.

The technical specification’s stable requirement IDs should be cited by tests or evidence where practical.

## 12. Forbidden expansion

This amendment does not authorize:

- live acquisition;
- database/persistence/report schemas;
- project-wide exception hierarchy;
- public API error contract;
- recommendation or abstention policy;
- generalized source layers;
- unrelated runtime dependencies;
- CLI/API framework;
- CI, Docker, cloud, services, queues, agents, ML, graph, or LLM work;
- restoration of removed scaffold;
- a claim that complete architecture or practical ownership is established.

## 13. Maintenance

Change this amendment only when the corrected M2-S01 conceptual contract, Pydantic method authorization, activated validation rules, deliverables, proof obligations, or superseded plan wording changes.

Do not add completed/remaining status, gate-result state, active substep, implementation progress, or exact next action.
