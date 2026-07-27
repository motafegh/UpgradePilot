# B2 PyPI Source Selection and Identity Slice

**Date:** 2026-07-27  
**Operation:** B2 package/upstream evidence source selection and first implementation slice  
**Starting revision:** `b614c0d16587a89e433dbc63f1238daf3c3ba78a`  
**Working branch:** `agent/b2-pypi-release-identity`

## Objective

Choose the smallest credible generalizable source boundary for official Python package evidence,
then implement only the deterministic package/version identity portion without encoding the
pytest control case or interpreting release prose.

## Source comparison and decision

Three strategies from the bounded plan were considered:

1. **PyPI release metadata only** — accepted for exact package/version publication identity,
   release-file presence, retrieval provenance, and publisher-supplied project-link candidates;
   rejected as sufficient proof of compatibility or a release-specific semantic claim.
2. **PyPI identity plus a project-controlled release source** — accepted as the product-level
   direction. PyPI establishes package identity first; a later bounded source resolver must
   establish project control and release specificity before upstream prose is trusted.
3. **Package-specific URL or adapter** — rejected as accepted runtime behavior. It remains
   permissible only as a fixture, manual oracle, or temporary comparison.

The first implementation slice therefore uses the official release-specific PyPI JSON endpoint
for exact identity. The endpoint choice stays inside the existing read-only HTTP acquisition
responsibility and does not require a cross-cutting ADR.

## Authority boundary

This slice permits UpgradePilot to claim only that:

- PyPI returned a package identity matching the normalized requested distribution name;
- PyPI returned the exact requested version rather than another release;
- the response satisfied the bounded JSON shape and size contract;
- the recorded project URLs were supplied in PyPI metadata.

It does not permit UpgradePilot to claim that:

- a project URL is automatically an authoritative release source;
- the release is compatible, safe, or a drop-in replacement;
- release prose has been interpreted;
- the maintainer should merge, defer, or block the update.

## Implemented behavior

`src/upgradepilot/pypi_client.py` adds a reusable `PyPIReleaseClient` that accepts a variable
Python distribution name and exact version. It:

- applies the existing Python package-name normalization rule;
- requests the exact release endpoint;
- validates returned package and version identity;
- caps streamed response bodies before JSON trust;
- preserves retrieval time, source URL, PyPI serial, distribution-file count, and
  publisher-supplied project-link candidates;
- distinguishes `available`, `version_not_found`, `package_not_found_or_inaccessible`,
  `identity_mismatch`, `malformed_response`, and `acquisition_failed`;
- performs a package-level lookup after a release `404` so a missing version is not confused
  with an inaccessible package record.

The controlled tests use the fictional package `friendly-bard`; no pytest name, version,
release wording, S004 answer, or known upstream URL appears in product logic.

## Checks performed

An isolated Python 3.13.5 harness executed seven deterministic tests covering:

- normalized-name success;
- exact-version mismatch;
- absent version with an existing package;
- absent or inaccessible package;
- malformed successful JSON;
- response-size rejection;
- timeout classification.

Observed result:

```text
Ran 7 tests
OK
```

Official PyPI documentation and live public JSON responses for more than one package were also
inspected to confirm the endpoint shape and the distinction between registry identity and
publisher-supplied metadata.

## Checks unavailable

- The complete repository test suite was not executed because the repository could not be
  cloned into the isolated container environment.
- The implemented client was not yet exercised through an unmocked live network request.
- No upstream project-source resolver or semantic release-note interpretation was tested.

## Result classification

**Partial.** The source-selection decision and deterministic PyPI identity slice were completed
on the working branch. Repository-wide and live-client validation remain separate evidence
requirements before this behavior can be treated as fully verified.
