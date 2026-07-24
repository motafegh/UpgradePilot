# 07 — Tests, Diagnosis, and Claim Discipline

## SMART objective

Within 30–40 minutes, map every active test file to its protected boundary, diagnose six hypothetical failures, and state the exact claims permitted by deterministic and live evidence.

## Why tests exist here

The active suite is not mainly checking Python syntax. It protects product invariants:

- exact identity;
- complete evidence;
- explicit failure categories;
- bounded interpretation;
- honest unresolved states;
- no cross-job or cross-revision inference.

A test name should tell you what contract would be damaged if it failed.

## Active test map

### `test_github_client.py`

Protects:

- PR identity construction;
- ambiguous `404` classification;
- changed-file record validation;
- multi-page acquisition;
- final count reconciliation;
- rejection of malformed successful responses.

Failure localizes to the PR/changed-file acquisition boundary.

### `test_dependency_change.py`

Protects:

- supported exact pinned update;
- different-package rejection;
- missing patch handling;
- incomplete patch detection;
- range syntax abstention;
- multiple-candidate ambiguity.

Failure localizes to deterministic patch interpretation.

### `test_github_actions.py`

Protects:

- exact-head and `pull_request` event binding;
- explicit empty workflow evidence;
- workflow-run pagination;
- run/job identity linkage;
- step-summary parsing.

Failure localizes to Actions acquisition, not CI authority.

### `test_github_repository.py`

Protects:

- exact run-detail identity;
- workflow path resolution;
- exact-head repository-file acquisition;
- base64 decoding;
- explicit unavailable workflow definition.

Failure localizes to the execution-definition linkage.

### `test_workflow_commands.py`

Protects:

- reading named-step `run` blocks;
- reading direct list-item command forms;
- narrow static command extraction.

Failure localizes to the shallow workflow reader.

### `test_ci_authority.py`

Protects:

- direct sufficient authority;
- tox-only unresolved state;
- multi-job non-combination;
- unavailable definition unresolved state;
- no-successful-job insufficiency.

Failure localizes to authority classification.

## Deterministic tests versus live proof

### Deterministic mocked tests prove

Given controlled inputs:

- functions enforce expected contracts;
- failure states are classified as designed;
- pagination and identity checks behave consistently;
- interpretation rules return the expected bounded state.

They do not prove:

- GitHub currently returns the expected real schema;
- public network access works;
- authentication/rate limits are adequate;
- S004 really has those workflows;
- all real repositories fit the supported grammar.

### Live S004 run proves

For one public PR at the observed time:

- editable installation worked in Ali's WSL2 environment;
- the real GitHub request path worked without authentication;
- exact dependency identity was recovered;
- exact-head workflows/jobs were acquired;
- exact-head workflow definitions were read;
- the direct authority rule found sufficient evidence.

It does not prove generality beyond the supported case.

## The observed proof

```text
28 deterministic tests passed
PR: googlefonts/glyphsLib#1145
head: f3cda8a94600e58d27f1bc17c99b7693718b6350
dependency: pytest 9.0.2 → 9.0.3
Regression Tests: sufficient
Test + Deploy: unresolved
overall CI authority: sufficient
```

Permitted claim:

> For the exact observed S004 head commit, at least one successful workflow directly installed the changed requirements file and invoked pytest.

Forbidden claims:

- pytest 9.0.3 is safe in every environment;
- all repository tests cover the changed behavior;
- every workflow exercised pytest;
- the PR should be merged;
- UpgradePilot supports arbitrary Dependabot PRs;
- Ali independently owns the implementation.

## Test anatomy to understand

Most focused tests follow:

```text
Arrange
→ construct raw response or validated input

Act
→ call one focused behavior

Assert
→ check result, exception, request parameters, or invariant
```

When reading a test, identify:

1. Which single variable is changed?
2. Which boundary is being isolated?
3. What result is expected?
4. What stronger claim is the test not making?

## Diagnosing by first failing boundary

The pipeline is sequential. Diagnose the earliest failed stage.

### CLI reports `Input rejected`

Inspect local locator validation. Do not debug GitHub networking first.

### CLI reports acquisition timeout

Inspect network/session/timeout behavior. Dependency rules have not run.

### CLI says successful response cannot establish evidence

Inspect response shape, field types, identity, or count reconciliation.

### Dependency is unsupported

Acquisition may be correct. Inspect patch evidence and supported grammar.

### Exact-head workflows are empty

Do not call this green CI. Inspect event/head filters and real repository state.

### Workflow definition is unavailable

Run/job acquisition may be correct. Inspect exact-run path and exact-head file retrieval.

### Authority is unresolved

The system worked but current interpretation could not prove enough. Inspect reason:

- tox indirection;
- multiple jobs;
- unavailable definition;
- unsupported workflow syntax;
- missing direct install or invocation.

### Authority is insufficient

Evidence supports a negative bounded conclusion, such as no successful exact-head job.

## Failure diagnosis drill

1. `test_rejects_run_for_different_head` fails because no exception is raised.
2. `test_patch_count_disagreement_is_incomplete_evidence` returns a supported change.
3. `test_multiple_jobs_remain_unresolved` returns sufficient.
4. Live CLI gets `404` for workflow definition but crashes.
5. All deterministic tests pass, but live run receives rate-limit error.
6. Regression workflow becomes unresolved after command syntax changes.

Expected diagnosis:

1. exact-head Actions identity invariant is broken;
2. truncated/partial patch can contaminate dependency identity;
3. unsafe cross-job authority inference was introduced;
4. unavailable repository evidence is not being preserved as unresolved;
5. deterministic logic is intact; live acquisition capacity/authentication is the problem;
6. shallow command grammar no longer recognizes the real form or evidence genuinely changed.

## How to review an AI-generated test

Reject or revise the test if it:

- duplicates implementation instead of asserting behavior;
- asserts only that no exception occurred;
- hardcodes S004 into runtime behavior;
- changes multiple variables at once without necessity;
- mocks away the invariant it claims to test;
- asserts green status but not exact SHA;
- treats unresolved as failure without product justification;
- verifies output text while ignoring the underlying result contract.

A strong test names one protected rule and fails for one meaningful class of defect.

## Useful commands

```bash
python3 -m unittest discover -s tests -v
```

Run one module:

```bash
python3 -m unittest tests.test_ci_authority -v
```

Run one test method:

```bash
python3 -m unittest \
  tests.test_ci_authority.CIAuthorityTests.test_sufficient_when_single_job_installs_and_invokes_dependency -v
```

The exact import path may depend on package discovery. The important skill is narrowing validation to the affected boundary, then running the complete suite.

## Current learning-depth statement

After today's work:

- product behavior through CI authority: implemented and live-validated for S004;
- concepts: introduced to operationally understood through discussion and execution;
- independent code ownership: not yet established;
- deferred normalized-package ownership exercise: still unpassed.

Do not mark a topic “complete” merely because its test passed.

## Completion evidence

This file is mastered when you can diagnose the six failures, explain what each test file protects, and state the permitted live claim without adding safety or recommendation language.