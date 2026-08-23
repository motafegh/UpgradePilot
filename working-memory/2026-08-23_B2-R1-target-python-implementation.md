# Working Memory — B2 R1 Target-Python Exact-Source Migration

**Date:** 2026-08-23  
**Status:** IMPLEMENTED + STATICALLY REVIEWED; POST-CHANGE RUNTIME VALIDATION PENDING  
**Execution branch:** `agent/r1-exact-file-contract-migration`  
**Parent trace:** `2026-08-23_B2-R1-target-python-responsibility-trace.md`  
**Runtime trigger:** `2026-08-23_B2-R1-local-runtime-validation-checkpoint.md`

## 1. Why this step was implemented

Local runtime validation confirmed that the Target-Python family still depended on the retired R1 exact-file `blob_sha` contract. The focused Target-Python suite failed 8/8 before semantic cases could execute because tests still constructed old `RepositoryTextFile` / `UnavailableRepositoryFile` shapes.

The responsibility trace established that Target-Python owns only the exact-head `pyproject.toml` source role, its immutable revision/path provenance, the parsed `[project].requires-python` declaration, and explicit semantic problem states.

## 2. Final Target-Python contract

Successful evidence:

```text
TargetPythonDeclaration
├── path
├── revision
└── requires_python
```

Problem evidence:

```text
TargetPythonDeclarationProblem
├── state
├── path
├── revision
└── detail
```

Removed:

```text
blob_sha
```

No repository field was added.

## 3. Ownership reasoning preserved in code

`RepositoryTextFile` already owns structural repository/path/revision/content validity. `target/python.py` still checks:

```text
evidence.path == "pyproject.toml"
```

because this is a semantic source-role check, not a repeat of structural path validation.

`revision` remains durable because `impact/python_support.py` later performs the genuine independent relation:

```text
target_evidence.revision == candidate.target_revision
```

This prevents a separately supplied Target relevance result from being rebound to a different target head.

`blob_sha` was removed because it contributes to no Target-Python parsing, relevance, specifier, impact, or revision-coherence proposition.

## 4. Production changes

### `src/upgradepilot/target/python.py`

Removed `blob_sha` from both result dataclasses and all propagation. Parsing/problem semantics are unchanged.

Commit:

```text
d00a813d7499556aee99aba236f9fad457c692e5
```

### `src/upgradepilot/cli.py`

Removed Target Python blob-SHA presentation. CLI still renders:

```text
Target Python source: path @ revision
Target requires-python: ...
problem detail
```

Commit:

```text
e1ef3174ea220ea4ed3855f86abce12f87e10ca7
```

No changes were made to `target/relevance.py` or `impact/python_support.py`; their semantic logic remains authoritative and unchanged.

## 5. Test migration

Updated:

```text
tests/test_target_python.py
tests/test_target_python_relevance.py
tests/test_python_support_impact.py
tests/test_cli.py
```

Key changes:

- exact-file fixtures now construct `RepositoryTextFile(repository, path, revision, content)`;
- unavailable fixtures include repository identity;
- Target-Python domain fixtures no longer fabricate blob IDs;
- blob assertions/rendering expectations were removed;
- path/revision preservation remains covered;
- wrong semantic source path remains covered;
- Target relevance states remain covered;
- impact revision mismatch remains covered;
- CLI explicitly verifies blob-SHA presentation is absent.

## 6. Static review

Comparison from the frozen trace commit:

```text
e0fbabed88fd7f70f24158e447c7ece212018b63
→ current branch
```

showed only six intended files changed:

```text
src/upgradepilot/target/python.py
src/upgradepilot/cli.py
tests/test_target_python.py
tests/test_target_python_relevance.py
tests/test_python_support_impact.py
tests/test_cli.py
```

No Target relevance, PEP 440 specifier, impact applicability, investigation-selection, upstream, CI, dependency, or provider semantics were modified.

## 7. Proof status

```text
responsibility trace                 COMPLETE
production migration                 COMPLETE
direct/downstream test migration     COMPLETE
static diff review                   COMPLETE
post-change runtime validation       NOT YET PERFORMED
```

The pre-change local runtime evidence remains useful as the trigger/diagnosis, but this new implementation must not be called runtime-green until the focused Target-Python/downstream tests are rerun.

## 8. Exact continuation

Do not merge `main` yet and do not jump to R2.

Next actions:

```text
1. continue R1 remaining-contract inventory from the previous 507-test / 5-failure / 51-error full-suite result;
2. identify the next earliest stale exact-file contract family rather than patching terminal failures;
3. when local execution is next available, rerun:
   tests.test_target_python
   tests.test_target_python_relevance
   tests.test_python_support_impact
   tests.test_cli
   nearest investigation tests
   then full suite;
4. only after the current migration branch is full-suite green, merge current main into this SAME branch and revalidate.
```
