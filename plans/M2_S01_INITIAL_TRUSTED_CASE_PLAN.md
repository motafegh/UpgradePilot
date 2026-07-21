# M2-S01 — Initial Trusted Case Plan

**Status:** Controlling current project plan  
**Owner:** Ali Rajabi  
**Milestone:** M2 — First automated vertical slice  
**Case:** `pydantic/pydantic#13432`  
**Responsibility:** Establish the first trusted input-to-record transformation and prove it through executable evidence

## 1. Bounded outcome

Given the manually assembled eight-field M1 case input:

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

preserve the supplied raw mapping, validate and normalize only the activated fields, and construct:

```text
PullRequestSnapshotIdentity
+ DependencyChange
+ ChangedFileEvidence
→ InitialCaseRecord
```

This plan does not complete M2. It establishes the first accepted package boundary and trusted transformation responsibility.

## 2. Applicable controls

- Project operation: `../OPERATING_GUIDE.md`
- Project route and M2 gate: `UPGRADEPILOT_90_DAY_PLAN.md`
- Activated requirements: `../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`
- Source layout: `../docs/architecture/ADR-0001-initial-python-source-layout.md`
- Pydantic method: `../docs/architecture/ADR-0002-pydantic-runtime-contract-models.md`
- Current continuation: `../MEMORY.md`
- Detailed evidence: current record under `../working-memory/`

The specification owns required behavior. ADRs own accepted methods. This plan does not restate their complete content.

## 3. Required understanding

Before claiming ownership, Ali must be able to explain:

1. why PR snapshot identity is separate from dependency change and changed-file evidence;
2. which fields identify the exact PR snapshot;
3. why the flat mapping is only a provisional adapter;
4. why raw mapping/list mutation or aliasing is prohibited;
5. why exact-type validation differs from semantic validation;
6. what valid and invalid tests prove and do not prove;
7. why Pydantic application contracts are not database rows or permanent public report schemas;
8. how the source package, distribution metadata, import namespace, module, and tests relate.

Teach these only to the depth needed to inspect, direct, modify, test, and diagnose the current responsibility.

## 4. Deliverables

1. Minimal `pyproject.toml` with reviewed Pydantic v2 dependency range.
2. `src/upgradepilot/__init__.py` and only the source module(s) required for this responsibility.
3. Explicit flat-to-nested adapter.
4. Trusted nested models required by the activated M2 contract.
5. Tests for:
   - real M1 case transformation;
   - exact required fields and representative wrong types;
   - malformed repository, PR number, and SHA values;
   - permitted whitespace normalization and lowercase SHA storage;
   - non-empty/different dependency versions;
   - empty or duplicate changed paths;
   - raw mapping/list non-mutation;
   - immutable trusted paths and no mutable alias;
   - no partial trusted result on failure;
   - structured validation evidence.
6. Editable installation and import-resolution proof.
7. One Ali-directed central validation, normalization, error, or test change.
8. One intentional relevant failure predicted, observed, localized, repaired, and revalidated.
9. Concise working evidence recording commands, outputs, assistance, limitations, and unresolved work.

## 5. Execution order

### Step 1 — Inspect current truth

Read `MEMORY.md`, inspect current source/tests/environment, and rerun the narrow relevant checks before assuming the reported state remains true.

### Step 2 — Close understanding gaps

Use the standard learning-session flow from the Operating Guide only for concepts that still block inspection, modification, testing, or diagnosis.

### Step 3 — Verify package boundary

Confirm:

```bash
python3 -m pip install --editable .
python3 -c "import upgradepilot; print(upgradepilot.__file__)"
```

Use the actual environment-resolved Python command and record it.

### Step 4 — Verify and improve the activated contract

Run the bounded tests, inspect implementation against the specification requirement IDs, and correct only demonstrated gaps.

### Step 5 — Ali-directed change

Ali selects and materially directs one central improvement. Preserve before/after evidence and explain why the change belongs at the chosen boundary.

### Step 6 — Failure diagnosis

Introduce or use one relevant failing case. Predict the failure, run it, identify the responsible boundary, repair or restore it, and rerun narrow plus required broader checks.

### Step 7 — Close or continue

Update `MEMORY.md` only with the concise continuation. Update the working record with material evidence. Do not update Career unless Ali explicitly requests a Career review.

## 6. Proof commands

Representative proof:

```bash
python3 -m pip install --editable .
python3 -c "import upgradepilot; print(upgradepilot.__file__)"
python3 -m unittest discover -s tests -v
python3 -m compileall -q src/upgradepilot tests
python3 -m pip check
```

A clean-checkout or equivalent clean-state reproduction is required before M2 closes, but does not need to be completed in this single responsibility if the current continuation remains bounded and explicit.

## 7. Pass condition

M2-S01 passes when:

- package installation and import resolution succeed;
- the real case maps deterministically into the expected nested record;
- representative invalid input is rejected through structured validation;
- permitted normalization is explicit and tested;
- raw input remains unchanged;
- trusted paths are immutable and do not alias raw structures;
- no partial trusted record is returned on failure;
- one Ali-directed central change is implemented and tested;
- one relevant failure is diagnosed and repaired;
- Ali can locate and explain the package, adapter, models, validators, errors, and tests;
- assistance and ownership are recorded conservatively;
- no forbidden expansion enters.

Passing this plan does not pass M2. The remaining M2 vertical-slice responsibilities continue through later project-local plans or bounded continuations.

## 8. Forbidden expansion

Do not add through this plan:

- live GitHub/PyPI acquisition;
- complete provenance or raw-source system;
- persistence, SQL, cache, retry, pagination, or replay;
- recommendation/abstention policy or report generator;
- public CLI/API framework;
- project-wide exception hierarchy;
- CI, Docker, cloud, services, queues, agents, ML, graph, or LLM components;
- speculative source layers or placeholder directories;
- unrelated dependencies;
- claims that complete architecture or broad Pydantic/Python/testing ownership is established.

## 9. Maintenance

Change this plan only when its bounded outcome, deliverables, proof, ownership action, stop condition, or forbidden scope changes.

Do not add current substep, completed-item status, command output, or exact continuation. Those belong in `MEMORY.md`, source/tests, and working evidence.
