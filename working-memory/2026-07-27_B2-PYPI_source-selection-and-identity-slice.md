# B2 PyPI Source Selection and Identity Slice

**Date:** 2026-07-27  
**Operation:** B2 package/upstream evidence source selection and deterministic package-identity slice  
**Starting revision:** `b614c0d16587a89e433dbc63f1238daf3c3ba78a`  
**Implementation merge:** `a3b416358669035ed9bf5db3e8043bcf49334a6d`  
**Validated repository revision:** `70bc133d3d3d0fbffddfadeb881ae98825f147b7`

## Objective

Choose the smallest credible generalizable source boundary for official Python package evidence,
then implement and validate only the deterministic package/version identity portion without
encoding the pytest control case or interpreting release prose.

## Source comparison and decision

Three strategies from the bounded plan were compared:

1. **PyPI release metadata only** — accepted for exact package/version publication identity,
   release-file presence, retrieval provenance, and publisher-supplied project-link candidates;
   insufficient for compatibility or release-specific semantic claims.
2. **PyPI identity plus a project-controlled release source** — accepted as the product-level
   strategy. PyPI establishes package identity first; a separate bounded resolver must establish
   project control and release specificity before upstream prose is trusted.
3. **Package-specific URL or adapter** — rejected as accepted runtime behavior. It remains
   permissible only as a fixture, manual oracle, or temporary comparison.

The identity slice therefore uses PyPI's release-specific JSON endpoint. This endpoint remains
inside the existing read-only HTTP acquisition responsibility and did not require a cross-cutting
ADR.

## Authority boundary

This slice permits UpgradePilot to claim only that:

- PyPI returned a package identity matching the normalized requested distribution name;
- PyPI returned the exact requested version rather than another release;
- the response satisfied the bounded JSON shape and size contract;
- the recorded project URLs were supplied in PyPI metadata.

It does not permit UpgradePilot to claim that:

- a PyPI project URL is automatically an authoritative release source;
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

## Repository integration

The implementation was initially prepared on `agent/b2-pypi-release-identity` and reviewed in
PR #13. At Ali's direction, PR #13 was squash-merged into `main` as:

```text
commit a3b416358669035ed9bf5db3e8043bcf49334a6d
Add exact PyPI release identity evidence (#13)
```

Repository instructions were then changed so ordinary UpgradePilot development occurs directly
on `main` unless Ali explicitly requests a branch or pull request. That workflow correction does
not change the implementation or its evidence authority.

## Controlled validation

### Isolated implementation harness

Before repository integration, an isolated Python 3.13.5 harness executed seven deterministic
tests covering:

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

### Complete active repository suite

Ali pulled `main`, activated the existing Python 3.12 virtual environment, installed the project
editably, and ran the complete active unittest suite:

```bash
python3 -m pip install -e .
python3 -m unittest discover -s tests -v
```

Observed results:

```text
Successfully installed upgradepilot-0.0.0
Ran 35 tests in 0.006s
OK
```

The 35 passing tests included all seven `PyPIReleaseClient` tests alongside the existing GitHub,
dependency-change, workflow, and CI-authority tests. This establishes controlled deterministic
behavior at repository revision `70bc133d3d3d0fbffddfadeb881ae98825f147b7` in Ali's Python
3.12 environment.

## Live PyPI validation

Ali then executed an explicitly unmocked read-only smoke check:

```python
result = PyPIReleaseClient().get_release("pytest", "9.0.3")
```

Observed output:

```text
result type: PackageReleaseEvidence
state: available
requested: pytest==9.0.3
source: https://pypi.org/pypi/pytest/9.0.3/json
published: pytest==9.0.3
distribution files: 2
PyPI serial: 38199665
project URL candidates:
  - Changelog: https://docs.pytest.org/en/stable/changelog.html
  - Contact: https://docs.pytest.org/en/stable/contact.html
  - Funding: https://docs.pytest.org/en/stable/sponsor.html
  - Homepage: https://docs.pytest.org/en/latest/
  - Source: https://github.com/pytest-dev/pytest
  - Tracker: https://github.com/pytest-dev/pytest/issues
```

This live result establishes for the supported control case that:

- the real PyPI endpoint was reachable through the implemented client;
- PyPI returned the exact requested package and version;
- the response passed the implemented identity and shape validation;
- two distribution-file records were present;
- PyPI supplied several project-link candidates.

It does not establish that any candidate link is release-specific or project-authoritative, nor
that pytest 9.0.3 is compatible, safe, or advisable for the target repository.

## Checks not performed in this operation

- No project-controlled upstream release source was selected or validated.
- No changelog or release-note content was acquired through product code.
- No semantic release claim was interpreted.
- No compatibility, safety, or maintainer recommendation was produced.
- No target repository was mutated.

These are outside the stated identity-slice objective rather than failed checks.

## Result classification

**Completed for the deterministic PyPI package/version identity slice.**

The objective was met through:

- an accepted generalizable source strategy;
- merged reusable source and controlled tests;
- successful editable installation;
- 35 passing active repository tests;
- one successful unmocked live acquisition for the supported control case;
- preserved limitations that prevent PyPI existence or metadata links from being overstated.

The broader B2 package/upstream evidence plan is not completed by this result. Its remaining
material evidence boundary is selecting, binding, and acquiring a supported project-controlled,
release-specific upstream source without package-specific hardcoding.

## Stable owners affected

- `src/upgradepilot/pypi_client.py` and `tests/test_pypi_client.py` own implemented behavior and
  controlled proof.
- `plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md` owns the accepted stable source
  strategy, proof obligations, and stop line.
- `MEMORY.md` owns the resulting live position and continuation.
