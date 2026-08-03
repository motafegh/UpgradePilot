# B2 Step 5A — Release Index Implementation Record

**Date:** 2026-08-02  
**Parent responsibility:** Step 5 — authoritative upstream interval acquisition  
**Live-state owner:** `MEMORY.md`

## Why this increment exists

Step 1 already defines `CrossedReleaseIndexEvidence`, but until this increment the active runtime had no source-specific mechanism that could earn it from a complete public package release listing.

Step 5A implements only that missing bridge:

```text
PyPI project JSON
→ exact raw package release keys
→ PEP 440 interval selection/order
→ CrossedReleaseIndexEvidence
```

It does not yet resolve Git tags or acquire a changelog.

## Source-specific acquisition

`src/upgradepilot/pypi_client.py` now contains a separate `PyPIReleaseIndexClient` rather than overloading the exact-release client's semantic result.

New source records:

```text
PackageReleaseIndexEvidence
PackageReleaseIndexProblem
PackageReleaseIndexResult
```

Successful evidence preserves:

```text
requested package
normalized package
published package name
PyPI project URL
retrieval time
PyPI last_serial
exact raw release keys
```

The release keys are lexically sorted only for deterministic storage. That ordering has no version meaning.

## Pure crossed-release selection

Created:

```text
src/upgradepilot/upstream_interval_acquisition.py
```

Public flow:

```text
PackageReleaseIndexEvidence
+ DependencyReleaseInterval
+ upstream repository identity
→ select_crossed_release_index
→ SelectedCrossedReleaseIndex
   or CrossedReleaseIndexSelectionProblem
```

`SelectedCrossedReleaseIndex` preserves both:

- the complete source-specific `PackageReleaseIndexEvidence`;
- the trusted Step 1 `CrossedReleaseIndexEvidence`.

This avoids copying away source identity such as the PyPI URL, retrieval time, and serial.

## PEP 440 responsibility

The selector does not implement a home-grown version parser.

It:

1. parses old/proposed dependency bounds through `parse_dependency_release_interval`;
2. uses `packaging.version.Version` for each raw PyPI release key;
3. keeps candidates satisfying `old < release <= proposed`;
4. delegates final interval checking, exact proposed-version presence, equivalent-identity rejection, and deterministic order to `order_crossed_release_versions`.

This keeps Step 5 acquisition aligned with the accepted Step 3 standards method.

## Non-PEP-440 keys

A PyPI project response can contain a legacy raw release key that cannot be ordered by the admitted PEP 440 method.

The selected behavior is:

```text
non-PEP-440 raw key
→ preserve in ignored_non_pep440_versions
→ do not admit to CrossedReleaseIndexEvidence
```

This is intentionally not silent dropping. The Step 1 index means the complete set of **admitted PEP 440 release identities** in the dependency interval, not every arbitrary legacy string that may exist in a registry response.

If the exact proposed release is absent, or selected keys contain PEP 440-equivalent raw identities, the index is not trusted.

## Controlled tests added

Created:

```text
tests/test_pypi_release_index.py
tests/test_upstream_interval_acquisition.py
```

They cover:

- normalized request identity and published identity;
- raw release-key preservation;
- malformed release-index shapes;
- 404, timeout, oversized, and malformed-JSON behavior;
- S001-shaped `2.6 → 2.8.4` selection;
- old-exclusive/proposed-inclusive boundaries;
- exact source provenance preservation;
- non-PEP-440 ignored-key evidence;
- exact proposed raw identity requirement;
- equivalent selected raw identities;
- package identity mismatch;
- invalid dependency interval handling;
- public argument validation.

`tests/test_package_interface.py` also protects the new public contracts.

## Implementation boundary

The Step 5A source/test boundary after package-interface integration is:

```text
4ad56dabf6613f7ad46b096bcda7198ac1baff25
```

No local execution result is claimed yet for this boundary.

## Validation required

Run after fast-forwarding local `main`:

```bash
git pull --ff-only

python -m unittest \
  tests.test_pypi_client \
  tests.test_pypi_release_index \
  tests.test_upstream_interval_acquisition \
  tests.test_package_interface \
  -v

python -m unittest discover -s tests -v
```

Derived counts at this implementation boundary are:

```text
focused: 32 tests
complete: 281 tests
```

Observed terminal output controls truth.

## Stop line

Do not begin Step 5B tag resolution/peeling until this increment passes the focused and complete deterministic suites.

No CLI, model, target-Python, semantic-claim, compatibility, safety, or recommendation logic was changed.
