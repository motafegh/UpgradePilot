# UpgradePilot M2 First Session Plan

**Session ID:** M2-S01  
**Owner:** Ali Rajabi  
**Status:** Approved, controlling, and active; pre-code onboarding in progress  
**Route / milestone:** R2 / M2 — First automated vertical slice  
**Case:** `pydantic/pydantic#13432`  
**Authority:** Executes one bounded M2 responsibility under the UpgradePilot charter, capability specification, Learning and Execution Contract, roadmap, staged milestone plan, completed M1 report, and active tracker  
**Activation effect:** Authorizes learning and implementation only for the case-identity normalization responsibility and the minimum accepted Python source-layout baseline defined here. It does not authorize restoration of removed code, adoption of the former AI-generated architecture, or creation of speculative internal layers.

## 1. Session outcome

Create the first accepted machine responsibility for UpgradePilot:

> Given manually supplied identity fields for the completed Pydantic dependency-update case, validate and normalize those fields into one deterministic Python record without mutating the raw input.

This is the first bounded transformation in the eventual PR-to-report path. It is not the complete M2 vertical slice.

## 2. Why this responsibility comes first

The M1 report already identifies stable case fields required by every later evidence item and report:

- repository identity;
- pull-request number;
- base and head revisions;
- dependency name;
- old and proposed versions;
- changed files.

Before UpgradePilot can reason about release notes, CI, risks, or recommendations, it needs to distinguish valid case identity from malformed input. This responsibility is small enough to understand, test, modify, and own while establishing only the source/package boundary required for professional Python development—not a complete internal architecture.

## 3. Product behavior

### Input

A plain Python dictionary created manually from the M1 report with these required keys:

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

### Valid behavior

For the real Pydantic case, the implementation must:

- accept the complete required input;
- trim surrounding whitespace from text values;
- preserve repository identity in `owner/name` form;
- require a positive integer PR number;
- require base and head revisions to be 40 hexadecimal characters;
- require non-empty dependency and version values;
- require old and new versions to differ;
- require at least one non-empty changed-file path;
- return a new normalized dictionary;
- leave the original raw dictionary unchanged.

### Invalid behavior

At minimum, the implementation must reject one representative invalid case with a clear exception. The initial required changed case is:

> the head revision is missing or is not a 40-character hexadecimal Git commit identifier.

The session may add another small invalid case only when the first gate passes early.

## 4. Required concepts and current depth

Teach these immediately before they are used.

### Repository, distribution package, import package, and module

- **Repository:** the complete project workspace, named `UpgradePilot`.
- **Distribution package:** installable project metadata, initially named `upgradepilot`.
- **Import package:** the Python namespace imported as `upgradepilot`.
- **Module:** one Python file containing names and behavior, initially `upgradepilot.case_identity`.
- **Depth now:** enough to distinguish these layers, understand why the product/repository can use title case while Python imports use lowercase, and trace the selected import path. Defer publishing and advanced build-backend behavior.

### `src` layout and editable installation

- `src/` separates importable product code from repository documents, tests, and project-management material.
- `src/upgradepilot/` is the import package; `src/` itself is not the project namespace.
- Editable installation makes the package importable from the source tree through project metadata rather than accidental repository-root imports.
- **Depth now:** source-tree boundary, package discovery, editable installation purpose, and import verification. Defer wheel/sdist publication and release automation.

### Function

- A named reusable transformation from inputs to output.
- **Depth now:** parameters, return value, local variables, and deterministic behavior.

### Dictionary and list

- A dictionary maps keys to values; a list stores an ordered collection.
- **Depth now:** read, copy, validate, and return the small structures used here.

### Type hint

- A declared expected type used by people and tools; normal Python does not enforce every hint automatically.
- **Depth now:** basic hints for the central function. Defer generics beyond what this case requires.

### Validation

- Checking that input has the required structure and meaning before accepting it.
- **Depth now:** required keys, value types, SHA shape, non-empty values, and version difference.

### Exception

- A structured signal that normal execution cannot continue with the supplied input.
- **Depth now:** raise and test one clear `ValueError`. Defer custom exception hierarchies.

### Unit test and assertion

- A unit test checks one small behavior; an assertion states what must be true.
- **Depth now:** one valid test, one invalid test, and one raw-input non-mutation assertion using Python's standard `unittest` library.

### Raw versus normalized input

- Raw input preserves what the caller supplied; normalized input is a consistent representation for downstream behavior.
- **Depth now:** keep the raw dictionary unchanged and return a separate normalized dictionary. File snapshots and provenance stores come later.

## 5. Pre-code decision gate

Before any implementation or test file is created, Ali must explain as one connected model:

1. Why is case identity separate from release, CI, and recommendation evidence?
2. Which listed fields are required to identify this exact PR snapshot?
3. What should happen when the head SHA is malformed?
4. Why should the function return a new dictionary instead of modifying the raw one?
5. What does the valid test prove, and what does it not prove?

The initial source-layout decision is now accepted separately from those behavior questions:

```text
UpgradePilot/                  # repository and product workspace
├── pyproject.toml             # minimal installation/build metadata
├── src/
│   └── upgradepilot/          # Python import package
│       ├── __init__.py
│       └── case_identity.py   # first behavioral module
└── tests/
    └── test_case_identity.py
```

Naming and boundary:

- repository/product name: `UpgradePilot`;
- distribution name: `upgradepilot`;
- import package: `upgradepilot`;
- first module: `upgradepilot.case_identity`;
- test root: `tests/`.

Decision status:

- accepted as the initial source-layout baseline for M2 and future growth;
- not a claim that the complete internal architecture is known;
- no speculative `domain/`, `application/`, `adapters/`, `services/`, `scripts/`, CLI, or other source subpackages are pre-created;
- new subpackages appear only when an implemented responsibility demonstrates a real ownership or dependency boundary;
- reassess only when observed import, packaging, distribution, interface, or module-cohesion limitations justify it.

The decision and rationale must be recorded in UpgradePilot's accepted architecture-decision area and active working-memory file before implementation begins. Source and test creation remain blocked until the five behavior questions above pass.

## 6. Must deliver

1. UpgradePilot active working-memory file:

```text
working-memory/2026-07-20_M2-S01_case-identity-normalization.md
```

2. Accepted source-layout decision record:

```text
docs/architecture/ADR-0001-initial-python-source-layout.md
```

3. Minimal project metadata:

```text
pyproject.toml
```

It must contain only the metadata and package discovery needed to install and test the current package. It must not add runtime dependencies, CLI entry points, publication automation, or unrelated tool configuration.

4. Initial package boundary:

```text
src/upgradepilot/__init__.py
src/upgradepilot/case_identity.py
```

5. One test module:

```text
tests/test_case_identity.py
```

6. Tests covering:

- the real valid Pydantic case;
- malformed or missing head SHA;
- raw input remains unchanged.

7. One small Ali-owned change after the initial passing implementation, such as:

- add and explain validation for equal old/new versions;
- add and explain validation for an empty changed-file path;
- improve one error message and update its test.

8. Reproducible commands recorded in working memory.

9. Honest assistance and ownership labels.

## 7. Execution sequence

### Step 1 — Orient

Read:

- this plan;
- the current Career tracker;
- the completed M1 report Sections 1, 3, 7, and 12;
- UpgradePilot `README.md`, `AGENTS.md`, `MEMORY.md`, accepted source-layout decision, and active working record.

State:

- the one responsibility being built;
- what remains outside scope;
- why the removed scaffold and former AI architecture are not reused.

### Step 2 — Teach and close the behavior gate

Teach the concepts in Section 4. Preserve Ali's explanation of the five pre-code questions and his expected valid/invalid behavior as one connected model.

### Step 3 — Confirm the accepted source boundary

Review the accepted decision and require Ali to explain:

- why `UpgradePilot` and `upgradepilot` name different layers;
- why `src/upgradepilot/` is used instead of placing generic modules directly under `src/`;
- why the decision establishes a source/package boundary without pre-creating internal architecture;
- what would trigger later reassessment.

Record this explanation in the active working-memory file. Do not reopen the layout as an unstructured preference poll unless new technical evidence contradicts the decision.

### Step 4 — Create the minimum installable package boundary

After the behavior gate passes:

- create the minimal `pyproject.toml`;
- create `src/upgradepilot/__init__.py`;
- install the project in editable mode;
- verify that `import upgradepilot` resolves from `src/upgradepilot/`.

Do not add behavioral implementation before the valid test is written.

### Step 5 — Write the valid test first

Create the real Pydantic input from the M1 report and write assertions for the normalized result and raw-input preservation.

The first test may fail because `case_identity.py` or its function does not yet exist. Explain why this is useful rather than hiding the failure.

### Step 6 — Implement the smallest passing behavior

Create `src/upgradepilot/case_identity.py` and write only the validation and normalization required by Section 3. Avoid helper layers, abstract interfaces, frameworks, schemas, or configuration systems.

### Step 7 — Add the invalid case

Test malformed or missing head SHA. Require a clear `ValueError` and inspect the actual failure message.

### Step 8 — Ali-owned modification

Ali selects and materially directs one small additional validation or error improvement. Run tests before and after the change.

### Step 9 — Diagnose one changed/failing case

Intentionally change one expected value or input, observe the failure, explain the cause, restore/fix it, and rerun the suite.

### Step 10 — Close

Record:

- files and commands;
- actual installation, import, and test outputs;
- Ali's predictions and corrections;
- the accepted source-layout boundary and its reassessment triggers;
- assistance labels;
- demonstrated capability depth;
- remaining M2 responsibilities;
- exact next action.

Update the canonical Career tracker.

## 8. Proof commands

Record and run from the repository root:

```bash
python -m pip install --editable .
python -c "import upgradepilot; print(upgradepilot.__file__)"
python -m unittest discover -s tests -v
python -m compileall -q src/upgradepilot tests
```

The import-path output must resolve through `src/upgradepilot/` in the active environment.

A clean checkout or equivalent clean-state command must be defined before M2 closes; it is not required to be solved fully in this first session.

## 9. Pass condition

M2-S01 passes when:

- the accepted decision record, minimal project metadata, selected source files, and test file exist;
- editable installation succeeds;
- `import upgradepilot` resolves from `src/upgradepilot/`;
- the real Pydantic case normalizes deterministically;
- malformed/missing head SHA is rejected clearly;
- the raw input is unchanged;
- tests pass after one observed failing or changed case is diagnosed;
- Ali can explain the repository/distribution/import-package distinction, selected import path, function data flow, validation, exception, and assertions;
- Ali materially directs or modifies one central behavior;
- assistance and ownership are recorded honestly;
- no forbidden scope was introduced.

Passing M2-S01 does not pass M2. It establishes the first accepted source/package boundary and transformation responsibility only.

## 10. Forbidden scope

Do not add during M2-S01:

- live GitHub or PyPI acquisition;
- JSON file contract or schema framework;
- full evidence-item representation;
- recommendation or abstention policy;
- Markdown report generator;
- database, SQL, cache, retry, pagination, or persistence;
- CLI framework, CLI entry point, or public API;
- external runtime or testing dependencies;
- CI workflow;
- Docker, cloud, services, queues, agents, ML, graph, or LLM components;
- speculative source subpackages or layered directories;
- publication/release automation;
- restoration or copying of prior scaffold code/tests/examples;
- claims that the complete or permanent architecture has been selected.

## 11. Assistance and ownership standard

Expected initial label: **AI-assisted**.

The source-layout decision is **Ali-directed and AI-recommended**. It is not evidence that Ali owns Python packaging broadly.

M2-S01 may support narrow Ali ownership of the case-identity normalization responsibility only when Ali can:

- locate the package, implementation, and tests;
- explain the import path and minimum `pyproject.toml` responsibility;
- explain each required field and validation;
- modify one validation correctly;
- predict and interpret a failing test;
- run and reproduce the behavior with limited assistance.

Do not generalize this to application architecture, testing, packaging, distribution, or Python ownership broadly.

## 12. Start message

```text
START M2-S01
Actual date: YYYY-MM-DD
Mode: Green | Yellow | Red
Available focused minutes:
Current responsibility: case-identity normalization for pydantic/pydantic#13432
First expected proof: Ali's connected explanation of the five pre-code behavior questions
```