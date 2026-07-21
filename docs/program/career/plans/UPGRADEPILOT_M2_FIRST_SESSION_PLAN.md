# UpgradePilot M2 First Session Plan

**Session ID:** M2-S01  
**Owner:** Ali Rajabi  
**Status:** Approved normative session plan  
**Route / milestone:** R2 / M2 — First automated vertical slice  
**Case:** `pydantic/pydantic#13432`  
**Authority:** Defines one bounded M2 responsibility under the charter, capability specification, Learning and Execution Contract, roadmap, milestone plan, completed M1 evidence, and tracker  
**Controlling correction:** [`UPGRADEPILOT_M2_S01_TECHNICAL_CONTRACT_AMENDMENT.md`](UPGRADEPILOT_M2_S01_TECHNICAL_CONTRACT_AMENDMENT.md)  
**Live state:** The canonical tracker and active UpgradePilot working-memory record control current progress and exact continuation. This plan does not record whether a deliverable is currently complete.

## 1. Bounded outcome

Create the first accepted machine responsibility for UpgradePilot:

> Given a manually assembled eight-field input derived from the M1 evidence report, preserve the raw input, validate and normalize the activated fields, and construct one trusted nested initial case record separating pull-request snapshot identity, dependency change, and changed-file evidence.

This is the first bounded transformation in the eventual PR-to-report path. It is not the complete M2 vertical slice or eventual public input interface.

## 2. Corrected semantic model

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

The flat eight-field mapping is a provisional M2 adapter, not one permanent identity object.

## 3. Why this responsibility comes first

The M1 report identifies stable case facts required by later evidence and reporting:

- repository;
- pull-request number;
- base and head revisions;
- dependency;
- old and proposed versions;
- changed files.

Before acquiring release, CI, repository-context, risk, or recommendation evidence, UpgradePilot needs a strict boundary between supplied raw values and one trusted nested record. The responsibility is small enough to learn, test, modify, and diagnose while establishing only the source/package boundary needed now.

## 4. Authorized source boundary

```text
UpgradePilot/
├── pyproject.toml
├── src/
│   └── upgradepilot/
│       ├── __init__.py
│       └── case_identity.py
└── tests/
    └── test_case_identity.py
```

Naming:

- repository/product: `UpgradePilot`;
- distribution/import package: `upgradepilot`;
- source root: `src/upgradepilot/`;
- test root: `tests/`.

This establishes an initial package/import boundary, not complete internal architecture. Do not pre-create speculative `domain/`, `application/`, `adapters/`, `services/`, repositories, scripts, CLI, or infrastructure trees.

The accepted rationale and reassessment triggers remain controlled by UpgradePilot ADR-0001.

## 5. Representation method boundary

The technical-contract amendment and UpgradePilot ADR-0002 control the selected Pydantic v2 method, dependency authorization, strict configuration, explicit adapter, frozen trusted models, immutable path collection, and framework-version reassessment.

This plan controls the bounded learning, package/test-first execution, ownership actions, proof, and stop lines. It does not duplicate the ADR’s full alternatives or trade-offs.

## 6. Required concepts

Teach immediately before use and only to the required depth:

### Repository, distribution package, import package, and module

Ali must distinguish:

- repository workspace `UpgradePilot`;
- installable distribution metadata `upgradepilot`;
- import namespace `upgradepilot`;
- first behavioral module `upgradepilot.case_identity`.

Defer publishing, wheel/sdist release, and advanced import mechanics.

### `src` layout and editable installation

Understand that `src/upgradepilot/` is the import package; `src/` itself is not the namespace. Editable installation must make imports resolve through project metadata rather than accidental repository-root lookup.

### Pydantic v2 runtime contracts

Minimum concepts:

- `BaseModel`;
- annotated required fields;
- strict validation;
- `ConfigDict`;
- `extra="forbid"`;
- frozen models and immutable nested collections;
- field/model validators;
- `ValidationError`;
- explicit flat-to-nested adapter;
- `model_dump()`/serialization boundaries;
- separation of raw input, application models, persistence records, and public report schemas.

### Validation, normalization, tests, and exceptions

Ali must understand:

- exact required fields and types;
- explicit permitted normalization;
- semantic invariants;
- structured rejection;
- unit tests and assertions;
- raw-input non-mutation;
- what one passing test proves and does not prove.

## 7. Pre-implementation reasoning gate

Before central behavioral implementation, Ali explains as one connected model:

1. Why snapshot identity is separate from dependency change and changed-file evidence.
2. Which fields identify the exact PR snapshot.
3. What should happen when the head SHA is malformed.
4. Why the adapter must not mutate the raw dictionary or raw list.
5. Why the output is nested rather than one flat identity object.
6. What the valid test proves and does not prove.
7. Why Pydantic models are not database rows or permanent public report schemas.

The tracker records whether this gate passed. This plan only defines the gate.

## 8. Must deliver

1. One active UpgradePilot working-memory record for M2-S01.
2. Accepted source-layout and Pydantic method decisions linked from that record.
3. Minimal `pyproject.toml` with only required metadata, package discovery, and reviewed Pydantic v2 dependency range.
4. `src/upgradepilot/__init__.py`.
5. Only source module(s) needed by the activated contract.
6. Bounded tests under `tests/`.
7. Proof of editable installation and import resolution.
8. Valid real-case nested transformation.
9. Representative strict/invalid cases, including malformed head SHA.
10. Raw dictionary and changed-file list remain unchanged.
11. Trusted paths are immutable and do not alias the raw list.
12. One Ali-directed central modification.
13. One intentional failure that Ali observes, diagnoses, repairs, and revalidates.
14. Commands, outputs, evidence, assistance, ownership, limitations, and unresolved work recorded.

## 9. Execution sequence

### Step 1 — Orient

Read only the plan, amendment, tracker, relevant M1 evidence, UpgradePilot memory/working record, core technical specification, ADR-0001, and ADR-0002.

State the bounded responsibility, proof required, and forbidden scope.

### Step 2 — Teach and close the reasoning gate

Teach the minimum concepts and preserve Ali’s connected explanation and predictions for valid, normalized, strict-invalid, and mutation behavior.

### Step 3 — Verify source/package boundary

Ali explains repository/distribution/import/module distinctions, why `src/upgradepilot/` is used, why it does not predefine architecture, and what would trigger reassessment.

### Step 4 — Create minimum installable boundary

- create minimal `pyproject.toml`;
- create `src/upgradepilot/__init__.py`;
- install editable;
- verify `import upgradepilot` resolves through `src/upgradepilot/`.

### Step 5 — Write valid nested-contract test first

Use the real M1 case. Assert nested components, permitted normalization, lowercase SHA storage, trusted tuple paths, and raw-input preservation. Observe and interpret the expected initial failure.

### Step 6 — Implement smallest passing behavior

Implement only the activated boundary model, nested trusted models, validators, and explicit adapter. Do not pre-create all conceptual contracts in the core specification.

### Step 7 — Add strict invalid and non-mutation regressions

At minimum test malformed head SHA, representative wrong type or undeclared field, non-mutation, and no mutable alias.

### Step 8 — Ali-directed modification

Ali selects and materially directs one validation, normalization, error, or test improvement. Compare evidence before and after.

### Step 9 — Diagnose one intentional failure

Change one input or expected value, predict the failure, run it, localize the cause, repair or restore it, and rerun relevant checks.

### Step 10 — Close

Record actual files, commands, outputs, tests, predictions, corrections, assistance, capability evidence, limitations, and unresolved responsibility. Update the canonical tracker only when state or evidence materially changes.

## 10. Proof commands

Use the environment-resolved Python command and record its exact form. Representative proof:

```bash
python3 -m pip install --editable .
python3 -c "import upgradepilot; print(upgradepilot.__file__)"
python3 -m unittest discover -s tests -v
python3 -m compileall -q src/upgradepilot tests
```

If the active environment exposes `python` instead of `python3`, use and record that command. Import output must resolve through `src/upgradepilot/`.

A clean-checkout or equivalent clean-state command is required before M2 closes, but need not be solved fully inside this session.

## 11. Pass condition

M2-S01 passes only when:

- required metadata, source, and test files exist;
- editable installation succeeds;
- `upgradepilot` resolves through `src/upgradepilot/`;
- the real case maps deterministically into the expected nested record;
- malformed/wrong-type representative input is rejected through structured validation;
- raw input remains unchanged;
- trusted paths are immutable and do not alias raw structures;
- tests pass after one intentional failure is diagnosed;
- Ali explains the source boundary, Pydantic role, adapter flow, validation, errors, tests, and proof limits;
- Ali materially directs or modifies one central behavior;
- assistance and ownership are recorded honestly;
- no forbidden scope enters.

Passing M2-S01 does not pass M2. It establishes only the first accepted package boundary and trusted transformation responsibility.

## 12. Forbidden scope

Do not add during M2-S01:

- live GitHub or PyPI acquisition;
- complete raw-source/provenance system;
- all future evidence contracts;
- recommendation/abstention policy or report generation;
- database, SQL, cache, retry, pagination, persistence, or replay;
- public CLI/API framework;
- unrelated runtime dependencies;
- CI, Docker, cloud, services, queues, agents, ML, graph, or LLM components;
- speculative source layers;
- publication/release automation;
- restored or copied prior scaffold;
- claims that complete architecture is selected.

## 13. Assistance and ownership

Expected initial mode is AI-assisted. ADR and source-layout approval may be Ali-directed without establishing broad Python, packaging, Pydantic, or architecture ownership.

Narrow ownership of this responsibility requires Ali to:

- locate package, implementation, and tests;
- explain import resolution and minimum metadata;
- explain each field, invariant, normalization, and error boundary;
- modify one central behavior correctly;
- predict and interpret a failing test;
- reproduce the behavior with limited assistance.

Do not generalize one session to broad application architecture, packaging, testing, debugging, or Python ownership.

## 14. Maintenance

Change this plan only when the bounded M2-S01 responsibility, required concepts, deliverables, proof, ownership gate, or forbidden scope changes.

Do not add current progress, completed deliverables, gate result, active substep, or exact continuation. Those belong to the tracker and active working-memory record.
