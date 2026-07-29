# B2 Target Python Declaration — Step 1 Execution Evidence

**Date:** 2026-07-29  
**Scope:** `plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`, Step 1 only  
**Position at execution:** B2 transparent-decision work; local-LLM prompt tuning paused

## Authorized responsibility

Implement only:

```text
exact-head pyproject.toml acquisition
→ tomllib parsing of [project].requires-python
→ typed target evidence
→ CLI presentation
```

The execution did not authorize or implement a Python version-range evaluator, upstream support-drop adapter, renewed prompt tuning, model integration, relevance-to-decision policy, or a new runtime dependency.

## Implemented source

### `src/upgradepilot/target_python.py`

Added one focused deterministic interpreter for the admitted target source:

```text
pyproject.toml at PullRequestIdentity.head_sha
→ [project].requires-python
```

The interpreter accepts only `pyproject.toml` evidence and preserves these result states:

- `available`;
- `file_unavailable`;
- `malformed_toml`;
- `project_table_absent`;
- `requires_python_absent`;
- `invalid_requires_python`.

Available evidence retains path, immutable revision, blob SHA, and the non-empty textual declaration. The module does not evaluate the declaration as a version range and does not infer support from workflows, classifiers, documentation, tool configuration, or repository age.

### `src/upgradepilot/cli.py`

The supported pinned-dependency path now:

1. requests `pyproject.toml` through `GitHubRepositoryClient.get_exact_head_text_file`;
2. passes the returned exact-revision evidence to `interpret_target_python_declaration`;
3. presents the typed target evidence before CI, package, and upstream evidence;
4. reports `Target Python declaration: not evaluated` when dependency extraction is unsupported.

The existing repository client remains acquisition-only. No source-specific TOML semantics were added to `github_repository.py`.

## Controlled tests

Added `tests/test_target_python.py` with eight focused cases:

1. available declaration with provenance;
2. unavailable file;
3. malformed TOML;
4. absent `[project]` table;
5. absent `requires-python` field;
6. non-text field;
7. empty textual field;
8. rejection of a non-admitted repository path.

Updated `tests/test_cli.py` to prove:

- exact-head `pyproject.toml` acquisition is requested for a supported dependency change;
- the interpreter receives that acquisition result;
- available target evidence is presented;
- unsupported dependency extraction skips target acquisition and reports `not evaluated`;
- package and upstream presentation behavior remains intact in the controlled path.

A controlled local package reconstruction executed the eight parser tests and four CLI orchestration tests:

```text
12 tests passed
```

The new source and test files were also syntax-compiled successfully under Python 3.12-compatible syntax.

## Public exact-revision evidence check

A connector-backed read-only check acquired:

```text
repository: googlefonts/glyphsLib
revision: f3cda8a94600e58d27f1bc17c99b7693718b6350
path: pyproject.toml
blob: 38d6a9efc4b94e2b733d3bbb848156449814ec94
```

The file was valid TOML but contained no `[project]` table. The interpreter returned:

```text
project_table_absent
```

This is the intended distinction: the file exists and parses, but it does not establish a PEP 621 `requires-python` declaration. Tool-specific data such as Black's `target-version` was not promoted into target declaration evidence.

This check validates the parser against one real exact-revision file. It was not a complete execution of the installed UpgradePilot command.

## Validation limitation

The execution environment could not create a direct Git checkout, and the repository has no workflow run associated with the direct commits. Therefore the complete repository test suite and a full live CLI execution were not run in this session.

The previous fully reported product-suite result remains 64 passing tests at the earlier behavior-validated revision. The new Step 1 commits must not be called fully behavior-validated until the actual repository suite and one complete read-only command are run from the repository environment.

## Revisions

```text
target parser:
89cb0ea4fa827aec6ed5504370d4c2a9e6f3a6e0

target parser tests:
5cf20e1281598933a20d7832a178895e624d6a42

CLI integration:
44628e625d9cb9d4aa6a73d8c229f732611fe63a

CLI orchestration tests:
bc028f28be629717c634a3cb4b79895ddaac5fc2
```

## Closed scope

Step 1 source and controlled-test implementation is complete. The next evidence task is full-repository validation of these exact commits. Do not proceed from this record into range evaluation, upstream support-drop extraction, LLM product work, or a relevance decision.
