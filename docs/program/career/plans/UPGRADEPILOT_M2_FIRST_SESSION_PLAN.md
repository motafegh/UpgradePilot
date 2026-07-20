# UpgradePilot M2 First Session Plan

**Session ID:** M2-S01  
**Owner:** Ali Rajabi  
**Status:** Approved, controlling, and active; pre-code onboarding in progress  
**Route / milestone:** R2 / M2 — First automated vertical slice  
**Case:** `pydantic/pydantic#13432`  
**Authority:** Executes one bounded M2 responsibility under the UpgradePilot charter, capability specification, Learning and Execution Contract, roadmap, staged milestone plan, completed M1 report, and active tracker  
**Activation effect:** Authorizes learning and implementation only for the case-identity normalization responsibility defined here. It does not authorize restoration of the removed scaffold or adoption of retained architecture proposals.

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

Before UpgradePilot can reason about release notes, CI, risks, or recommendations, it needs to distinguish a valid case identity from malformed input. This responsibility is small enough to understand, test, modify, and own without preselecting the full architecture.

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

### Python module and package

- **Module:** one Python file containing names and behavior.
- **Package:** a directory of related importable modules.
- **Depth now:** enough to understand the selected minimal file layout and imports. Defer packaging/build internals.

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

Before any source file is created, Ali must answer and explain:

1. Why is case identity separate from release, CI, and recommendation evidence?
2. Which listed fields are required to identify this exact PR snapshot?
3. What should happen when the head SHA is malformed?
4. Why should the function return a new dictionary instead of modifying the raw one?
5. What does the valid test prove, and what does it not prove?

Then the AI teaches the minimal layout options:

- one root module;
- a small flat `upgradepilot/` package;
- a `src/` layout package.

Ali selects the smallest understandable option for this responsibility. Retained architecture files do not decide the choice. The selected paths are recorded in the active working-memory file before code is written.

## 6. Must deliver

1. UpgradePilot working-memory file:

```text
working-memory/2026-07-20_M2-S01_case-identity-normalization.md
```

Use the actual date if execution starts on another date.

2. One importable Python module implementing the case-identity normalization function.

3. One test module using standard-library `unittest`.

4. Tests covering:

- the real valid Pydantic case;
- malformed or missing head SHA;
- raw input remains unchanged.

5. One small Ali-owned change after the initial passing implementation, such as:

- add and explain validation for equal old/new versions;
- add and explain validation for an empty changed-file path;
- improve one error message and update its test.

6. Reproducible commands recorded in working memory.

7. Honest assistance and ownership labels.

## 7. Execution sequence

### Step 1 — Orient

Read:

- this plan;
- the current Career tracker;
- the completed M1 report Sections 1, 3, 7, and 12;
- UpgradePilot `README.md`, `AGENTS.md`, and `MEMORY.md`.

State:

- the one responsibility being built;
- what remains outside scope;
- why the prior scaffold is not reused.

### Step 2 — Teach and predict

Teach the concepts in Section 4. Preserve Ali's answers to the five pre-code questions and his expected valid/invalid behavior.

### Step 3 — Select the minimal file layout

Compare the three bounded options. Record Ali's choice and rationale. Do not call it the permanent architecture.

### Step 4 — Write the valid test first

Create the real Pydantic input from the M1 report and write assertions for the normalized result and raw-input preservation.

The first test may fail because the implementation does not yet exist. Explain why this is useful rather than hiding the failure.

### Step 5 — Implement the smallest passing behavior

Write only the validation and normalization required by Section 3. Avoid helper layers, abstract interfaces, frameworks, schemas, or configuration systems.

### Step 6 — Add the invalid case

Test malformed or missing head SHA. Require a clear `ValueError` and inspect the actual failure message.

### Step 7 — Ali-owned modification

Ali selects and materially directs one small additional validation or error improvement. Run tests before and after the change.

### Step 8 — Diagnose one changed/failing case

Intentionally change one expected value or input, observe the failure, explain the cause, restore/fix it, and rerun the suite.

### Step 9 — Close

Record:

- files and commands;
- actual test outputs;
- Ali's predictions and corrections;
- selected layout and its temporary boundary;
- assistance labels;
- demonstrated capability depth;
- remaining M2 responsibilities;
- exact next action.

Update the canonical Career tracker.

## 8. Proof commands

The exact import path depends on the pre-code layout decision. At minimum, record and run:

```bash
python -m unittest discover -s tests -v
```

When applicable, also run:

```bash
python -m compileall -q <selected-source-path> tests
```

A clean checkout or equivalent clean-state command must be defined before M2 closes; it is not required to be solved fully in this first session.

## 9. Pass condition

M2-S01 passes when:

- the selected source and test files exist;
- the real Pydantic case normalizes deterministically;
- malformed/missing head SHA is rejected clearly;
- the raw input is unchanged;
- tests pass after one observed failing or changed case is diagnosed;
- Ali can explain the function, data flow, validation, exception, and assertions;
- Ali materially directs or modifies one central behavior;
- assistance and ownership are recorded honestly;
- no forbidden scope was introduced.

Passing M2-S01 does not pass M2. It establishes only the first accepted transformation responsibility.

## 10. Forbidden scope

Do not add during M2-S01:

- live GitHub or PyPI acquisition;
- JSON file contract or schema framework;
- full evidence-item representation;
- recommendation or abstention policy;
- Markdown report generator;
- database, SQL, cache, retry, pagination, or persistence;
- CLI framework or public API;
- external runtime or testing dependencies;
- CI workflow;
- Docker, cloud, services, queues, agents, ML, graph, or LLM components;
- restoration or copying of prior scaffold code/tests/examples;
- permanent architecture claims.

## 11. Assistance and ownership standard

Expected initial label: **AI-assisted**.

M2-S01 may support narrow Ali ownership of the case-identity normalization responsibility only when Ali can:

- locate the implementation and tests;
- explain each required field and validation;
- modify one validation correctly;
- predict and interpret a failing test;
- run and reproduce the behavior with limited assistance.

Do not generalize this to application, testing, packaging, or Python ownership broadly.

## 12. Start message

```text
START M2-S01
Actual date: YYYY-MM-DD
Mode: Green | Yellow | Red
Available focused minutes:
Current responsibility: case-identity normalization for pydantic/pydantic#13432
First expected proof: Ali's answers to the five pre-code decision questions
```