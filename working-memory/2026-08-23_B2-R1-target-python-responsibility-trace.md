# Working Memory — B2 R1 Target-Python Exact-Source Responsibility Trace

**Date:** 2026-08-23  
**Status:** TRACE COMPLETE; IMPLEMENTATION DECISION FROZEN  
**Execution branch:** `agent/r1-exact-file-contract-migration`  
**Current plan:** `../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`  
**Runtime trigger:** `2026-08-23_B2-R1-local-runtime-validation-checkpoint.md`

## 1. Why this trace exists

Local runtime validation confirmed that `src/upgradepilot/target/python.py` and its tests still consume the retired R1 exact-file `blob_sha` contract. This trace determines ownership before editing rather than patching the resulting test failures mechanically.

Confirmed focused failure:

```text
tests.test_target_python
→ 8 tests / 8 errors
→ stale RepositoryTextFile(blob_sha=...) fixtures
→ stale UnavailableRepositoryFile fixture missing repository
```

Production code also still performs:

```text
RepositoryTextFile.blob_sha
→ TargetPythonDeclaration.blob_sha
→ TargetPythonDeclarationProblem.blob_sha
→ CLI presentation/tests
```

## 2. Exact proposition

`target/python.py` owns only:

> From the admitted exact-head target `pyproject.toml`, establish the exact textual `[project].requires-python` declaration, or one explicit problem state explaining why that declaration could not be established.

It does not own:

```text
GitHub response authenticity
exact-file provider transport metadata
PR identity
upstream support-drop truth
Python-line relevance
compatibility/safety/action
```

## 3. Normal producer → orchestration → consumer flow

```text
PullRequestIdentity(repository, head_sha)
+ grounded upstream support-drop claim
→ PythonSupportDropImpactCandidate(
     target_repository=pull_request.repository,
     target_revision=pull_request.head_sha
   )
→ pre-acquisition applicability remains unresolved
→ select_python_support_drop_investigation(...)
→ PythonSupportDropInvestigationSelection(
     repository,
     revision,
     path="pyproject.toml"
   )
→ investigation.py verifies selection.repository/revision == PR repository/head
→ repository_client.get_exact_head_text_file(pull_request, path)
→ RepositoryFileEvidence
→ interpret_target_python_declaration(...)
→ TargetPythonEvidence
→ evaluate_target_python_relevance(...)
→ TargetPythonRelevanceResult
→ evaluate_python_support_drop_impact(candidate, relevance)
```

The final impact boundary performs a real independent relation check:

```text
target_evidence.revision == candidate.target_revision
```

because a `TargetPythonRelevanceResult` can be supplied separately from the candidate to that composition boundary.

## 4. Field-by-field decision

### `requires_python` — KEEP

This is the semantic proposition owned by the interpreter and is consumed by `evaluate_python_line_specifier(...)`.

### `revision` — KEEP

This is not merely presentation provenance. `evaluate_python_support_drop_impact(...)` uses it to ensure target relevance refers to the candidate's exact target revision.

Removing it would lose a genuine cross-object coherence check at a later independent composition boundary.

### `path` — KEEP

Current interpreter admits only `pyproject.toml` and rejects another repository path. Keeping the source path preserves the narrow exact-source/domain provenance used by problems and CLI presentation without retaining provider transport metadata.

The fixed path role remains a semantic source-role check:

```text
evidence.path == "pyproject.toml"
```

A structurally valid `RepositoryTextFile` path does not by itself mean the file is the target project metadata source this interpreter owns.

### `blob_sha` — REMOVE

No Target-Python proposition depends on the provider blob ID.

It is not used by:

```text
requires-python parsing
Target Python relevance
specifier evaluation
impact applicability
revision coherence
```

Its current downstream use is only propagation, presentation, and tests. Those uses are circular retention pressure, not independent justification.

### `repository` on TargetPythonEvidence — DO NOT ADD

The normal route already binds target repository before interpretation:

```text
impact candidate / PR identity owns target_repository
→ investigation verifies selection repository/revision against PR
→ exact-head acquisition uses that PullRequestIdentity
```

The later impact composition needs revision equality, but currently has no separate Target-Python repository proposition requiring another repository field.

Adding repository merely because `RepositoryTextFile` has it would copy upstream context without a current consumer/proof need.

## 5. Type-strength decision

Do not introduce a new generic validation framework or broaden this step into a full redesign of `TargetPythonDeclaration` construction.

The current product route constructs Target-Python evidence through `interpret_target_python_declaration(...)`. Direct test construction of domain evidence is not by itself authority to add new defensive mechanisms.

Therefore this step will keep the bounded contract change focused on removing obsolete provider metadata and migrating direct consumers/tests.

## 6. Problem states

Keep current semantic problem states:

```text
file_unavailable
malformed_toml
project_table_absent
requires_python_absent
invalid_requires_python
```

`TargetPythonDeclarationProblem` should retain:

```text
state
path
revision
detail
```

and remove `blob_sha`.

Typed `UnavailableRepositoryFile` still supplies repository/path/revision/reason/detail; Target-Python needs path/revision/detail from it but does not need to copy repository under the current proposition.

## 7. Immediate consumer decisions

### `target/relevance.py`

No production semantic change required. It consumes `requires_python` and preserves Target evidence in its result.

### `impact/python_support.py`

No production semantic change required. Preserve:

```text
target_evidence.revision == candidate.target_revision
```

This is a genuine independent composition invariant.

### `cli.py`

Remove Target Python blob-SHA rendering. Keep:

```text
Target Python source: path @ revision
Target requires-python: ...
problem detail
```

### tests

Migrate fixtures to current strong exact-file constructors:

```text
RepositoryTextFile(repository, path, revision, content)
UnavailableRepositoryFile(repository, path, revision, reason, detail)
```

Remove assertions/constructors whose only purpose is the retired blob field.

Retain tests for every Target-Python semantic state, wrong source path, revision preservation, relevance behavior, and impact revision mismatch.

## 8. Frozen implementation target

```text
TargetPythonDeclaration
├── path
├── revision
└── requires_python

TargetPythonDeclarationProblem
├── state
├── path
├── revision
└── detail
```

No repository field added. No new compatibility alias. No semantic-state changes.

## 9. Scope guard

This step must not change:

```text
TOML parsing semantics
[project] table meaning
requires-python text admission
PEP 440 comparison semantics
upstream support-drop semantics
impact applicability policy
investigation selection policy
```

It is only the Target-Python exact-source ownership migration confirmed by runtime evidence.

## 10. Next action

Implement this frozen contract, migrate direct tests/CLI fixtures, statically review the diff, and record implementation status. Runtime validation can be rerun in the next available local batch together with residual full-suite regrouping.