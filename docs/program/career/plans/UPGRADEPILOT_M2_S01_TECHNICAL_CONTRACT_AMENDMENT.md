# UpgradePilot M2-S01 Technical Contract Amendment

**Session ID:** M2-S01  
**Owner:** Ali Rajabi  
**Recorded:** 2026-07-21  
**Status:** Approved, controlling, and active amendment  
**Authority:** Read with `UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md`; this amendment supersedes conflicting M2-S01 wording and stop lines only  
**Selected method:** UpgradePilot `docs/architecture/ADR-0002-pydantic-runtime-contract-models.md`

## 1. Amendment effect

The original M2-S01 plan remains controlling for:

- the selected real case;
- the accepted `src/upgradepilot/` source boundary;
- learning and ownership method;
- test-first execution;
- bounded implementation and stop lines;
- installation, import, testing, diagnosis, and evidence requirements.

This amendment controls the corrected conceptual contract, representation method, runtime-dependency authorization, and conflicting framework/dependency prohibitions.

The controlling UpgradePilot technical artifacts are:

```text
UpgradePilot/docs/specifications/
UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md

UpgradePilot/docs/architecture/
ADR-0002-pydantic-runtime-contract-models.md
```

## 2. Corrected M2-S01 outcome

> Given a manually assembled eight-field input derived from the completed M1 evidence report, preserve the raw input, validate and normalize the activated fields, and construct one trusted nested initial case record that separates pull-request snapshot identity, dependency change, and changed-file evidence.

This remains the first bounded transformation in the PR-to-report path. It is not the complete M2 vertical slice and not the eventual public maintainer input interface.

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

Accepted correction:

- repository, PR number, base SHA, and head SHA identify the exact PR snapshot;
- dependency and version transition describe the proposed dependency change;
- changed files are snapshot-associated evidence;
- the complete trusted result is a nested initial case record;
- the flat eight-field mapping remains a provisional M2 manual adapter only.

## 4. Accepted representation method

The representation-method comparison is complete.

**Decision:** adopt Pydantic v2 for strict runtime boundary and trusted application contracts beginning in M2 and continuing into the corresponding M3 path.

Accepted data flow:

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

Accepted policy:

- raw source payloads remain plain source data or raw-source records;
- use strict Pydantic v2 validation;
- forbid undeclared fields in activated validated contracts;
- configure trusted models as frozen;
- store trusted changed-file paths as `tuple[str, ...]`;
- keep every current M2 field required;
- keep flat-to-nested assembly explicit and directly tested;
- use Pydantic `ValidationError` internally during M2;
- defer a project-wide custom exception hierarchy;
- keep application contracts separate from persistence records and public report schemas;
- reassess before Pydantic v3 or another breaking major upgrade.

## 5. Method comparison result

### Plain dictionaries plus explicit validation

Retained for raw source data, but rejected as the trusted-contract baseline because required fields, runtime typing, nested composition, mutation protection, structured errors, and serialization would require repeated manual infrastructure across M2 and M3.

### `TypedDict`

Retained as a possible static typing aid, but rejected alone because it does not enforce runtime values and trusted records remain mutable dictionaries.

### Standard-library dataclasses

Deferred for later selected internal value objects. Not selected alone because normal dataclasses do not enforce annotated field types at runtime and would still require substantial boundary-validation/error infrastructure.

### Pydantic plus separate dataclass domain models

Deferred because it creates two application object systems and another transformation boundary before demonstrated need.

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

Rules:

- all fields required;
- unknown top-level fields rejected;
- exact accepted types; no silent coercion;
- trim surrounding whitespace from declared strings and changed-file paths;
- canonicalize valid hexadecimal SHAs to lowercase;
- repository uses basic `owner/name` form;
- PR number is positive and not boolean;
- base/head SHAs contain exactly 40 hexadecimal characters;
- dependency and versions are non-empty;
- old/new versions differ;
- raw changed files is a non-empty list;
- normalized paths are non-empty and unique;
- source order is preserved;
- trusted paths become a tuple;
- raw dictionary and raw list remain unchanged;
- trusted values do not alias raw mutable structures;
- no partial trusted `InitialCaseRecord` is returned on failure.

This validates supplied values. It does not prove remote repository, PR, commit, dependency, or path existence.

## 7. Evidence-state boundary

```text
invalid manual input
≠ missing external evidence
≠ inaccessible source
≠ stale evidence
≠ conflicting evidence
≠ internal runtime/programmer failure
```

Pydantic validation errors are an internal mechanism for this bounded adapter. They are not the permanent project-wide evidence-state or public-error model.

## 8. Pre-implementation gate result

The amended pre-code gate is now **Pass — decision only** because:

- the public acquisition request is distinguished from the complete trusted record;
- exact PR snapshot identity is separated from dependency and changed-file evidence;
- raw and trusted forms are separated;
- invalid input is distinguished from degraded evidence states;
- the first test boundary and limitations are defined;
- the representation methods were compared;
- Ali reviewed and approved the Pydantic recommendation;
- ADR-0002 records the durable framework decision.

This pass does not establish installation, behavior, tests, debugging, or capability ownership.

## 9. Amended deliverables

Completed before source implementation:

1. accepted core pipeline and contract specification;
2. this controlling amendment;
3. corrected working memory and current-state files;
4. completed representation comparison;
5. accepted ADR-0002.

Remaining M2-S01 deliverables:

- teach the minimum Pydantic v2 concepts required to read and direct the implementation;
- create minimal `pyproject.toml` with a reviewed Pydantic v2 dependency range;
- create `src/upgradepilot/__init__.py`;
- create only the source module(s) needed by the activated contract;
- create the bounded test module under `tests/`;
- verify editable installation and import resolution;
- prove valid nested mapping, normalization, strict invalid behavior, and non-mutation;
- complete one Ali-directed central change;
- observe, diagnose, and repair one intentional failure;
- record commands, output, evidence, assistance, and capability state.

Do not pre-create every conceptual contract from the specification.

## 10. Amended execution sequence

### Step A — Minimum Pydantic onboarding

Teach only what is needed now:

- `BaseModel`;
- field annotations and required fields;
- `ConfigDict`;
- strict validation;
- `extra="forbid"`;
- frozen models and immutable nested collections;
- field/model validators;
- `ValidationError` and structured errors;
- `model_dump()` / `model_dump_json()` boundaries;
- why raw data and database rows remain separate.

Ali predicts representative valid, coerced, invalid, normalized, and mutation behavior before implementation.

### Step B — Package boundary

- select the compatible Pydantic v2 dependency range against the project Python version;
- create the minimum `pyproject.toml`;
- create `src/upgradepilot/__init__.py`;
- install editable;
- verify `import upgradepilot` resolves from `src/upgradepilot/`.

### Step C — Valid test first

Write the real M1 case test before behavioral implementation. Assert the nested conceptual components, permitted normalization, lowercase SHA canonicalization, trusted tuple paths, and raw-input preservation.

Observe and interpret the expected initial failure.

### Step D — Smallest passing implementation

Implement only:

- the flat manual boundary model;
- the three trusted component models;
- the nested initial case record;
- the explicit adapter/transformation;
- the activated constraints and normalization.

### Step E — Invalid/non-mutation/ownership evidence

- cover malformed head SHA;
- cover representative strict type behavior;
- prove raw dictionary/list non-mutation and no mutable aliasing;
- complete one Ali-directed rule, error, or test change;
- intentionally create, diagnose, and repair one failing case.

### Step F — Close

Record actual files, commands, installation/import/test output, limitations, assistance labels, capability evidence, remaining M2 work, and exact continuation. Update the canonical tracker.

## 11. Dependency authorization

The original blanket prohibition on external runtime dependencies is superseded for this decision.

Pydantic is authorized as an explicit runtime dependency because:

- the accepted project contract demonstrates recurring runtime-boundary needs;
- simpler baselines were compared;
- costs, failure modes, maintenance/security burden, and reversal triggers are recorded;
- Ali approved the recommendation;
- ADR-0002 is accepted.

Use the Pydantic v2 API family and prevent an unreviewed major upgrade. The exact lower bound is selected during package setup and verified in the active environment.

## 12. Still prohibited during M2-S01

- implementing every conceptual contract;
- live multi-source acquisition beyond a separately authorized bounded example;
- persistence/database/ORM/SQL/cache/retry/pagination/replay implementation;
- recommendation policy or report generation beyond separately authorized later M2 work;
- public CLI/API framework adoption;
- CI, containers, cloud, services, queues, ML, graphs, LLMs, or agents;
- speculative source subpackages;
- restoration or copying of removed scaffold files.

## 13. Amended pass condition

M2-S01 passes only when:

- the specification, amendment, and ADR-0002 remain synchronized;
- the reviewed Pydantic dependency is declared and installs successfully;
- the import path resolves through `src/upgradepilot/`;
- implementation models the corrected nested boundary;
- the real case normalizes deterministically;
- malformed/wrong-type representative input is rejected clearly;
- raw input and nested mutable values remain unchanged;
- trusted paths do not alias the raw list;
- tests pass after one Ali-directed modification and one diagnosed failure;
- assistance and capability evidence are recorded conservatively;
- no unreviewed framework or broader architecture is introduced.

Passing M2-S01 still does not pass M2.

## 14. Exact continuation

Teach the minimum Pydantic v2 concepts, then create and verify the minimal package boundary and dependency, write the valid nested-contract test first, observe the expected failure, and implement the smallest passing behavior.