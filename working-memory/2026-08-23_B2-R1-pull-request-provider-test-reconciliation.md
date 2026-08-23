# Working Memory — B2 R1 Pull-Request Provider Test Reconciliation

**Date:** 2026-08-23  
**Status:** TRACE COMPLETE; IMPLEMENTATION AUTHORIZED  
**Execution branch:** `agent/r1-exact-file-contract-migration`

## 1. Why this residual is different

`tests/test_pull_request_repository_files.py` is not merely a downstream fixture suite. It tests the GitHub repository provider boundary itself through the PR base/head convenience methods.

Its historical contract still described and asserted:

```text
returned_path
blob SHA
reported byte count
decoded byte count
provider-reported size agreement
```

R1 deliberately removed those values from durable `RepositoryTextFile` evidence and removed GitHub's `size` field from the required response contract.

Therefore this suite needs an ownership reconciliation, not a mechanical fixture substitution.

## 2. Current provider contract

Successful evidence:

```text
RepositoryTextFile
├── repository
├── path
├── revision
└── content
```

Provider admission still establishes:

```text
regular-file response type
returned path == requested normalized path
base64 encoding
textual encoded content
strict base64 validity
bounded encoded representation
bounded decoded bytes
valid UTF-8 text
```

The product no longer trusts or requires GitHub's separate `size` or `sha` response fields for this proposition.

## 3. Test ownership split

`tests/test_exact_commit_repository_files.py` already owns the generic shared exact-file provider boundary, including:

```text
immutable explicit commit identity
path normalization
returned-path mismatch rejection
malformed base64 rejection
oversized content rejection without provider size metadata
strong-type constructor invariants
typed exact-file unavailability
```

`tests/test_github_repository.py` separately protects workflow-run → exact-head workflow-file acquisition.

Therefore `tests/test_pull_request_repository_files.py` should own only what is specific to PR wrappers:

```text
PR base wrapper → identity.base_sha
PR head wrapper → identity.head_sha
same minimum durable RepositoryTextFile contract
404 → exact locator UnavailableRepositoryFile
shared provider still rejects a mismatched returned path / invalid UTF-8
```

It should not duplicate obsolete reported-size/blob representation tests.

## 4. Decision

### KEEP

```text
repository/path/revision/content assertions
base/head ref request assertions
404 locator preservation
returned path admission check
UTF-8 rejection
```

### REMOVE

```text
returned_path evidence assertion
blob_sha evidence assertion
reported_byte_count assertion
decoded_byte_count assertion
reported-size type validation test
reported oversize via size metadata test
reported-vs-decoded size agreement test
missing size field test
sha/size requirements in controlled response payload
```

The content-size protection is not lost: the shared exact-commit suite proves the provider's encoded/decoded bounds without relying on reported `size`.

## 5. Learning point

A test suite is also an architectural consumer. When a contract changes intentionally:

```text
old test asserts retired representation
```

does not imply:

```text
restore retired representation
```

Instead ask:

```text
what unique responsibility does this test file own?
what generic responsibility is already protected elsewhere?
```

This prevents duplicated tests from becoming accidental architecture authority.
