# S015 Candidate Screening — charset-normalizer marker-scoped pytest update

**Date:** 2026-09-22
**Status:** ADMITTED for bounded real-case simulation
**Form:** untouched real public Dependabot proposal + exact matrix/runtime evidence + current-product projection

## Candidate identity

- Repository: `jawah/charset_normalizer`
- PR: `#769` — Dependabot `pytest 7.4.4 → 9.0.3`
- Base: `aa2ddd8fb788b98a815f25c37609e919105d1dbb`
- Head: `fba29ea1027f3c3eaaea8c3cc64b71fbb392251c`
- Observed PR runtime checkout: `ddf477c2e71894890245a780ea17d2368d4ad64d`
- CI run: `28770340437`
- Workflow blob is identical at base/head: `760ab82d9c7a95a9c1d13b72079f864529a32033`

Relevant changed line in `ci-requirements.txt`:

`pytest==8.3.5 ; python_full_version == '3.8.*'`

becomes:

`pytest==9.0.3 ; python_full_version == '3.8.*'`.

## Q — Named question

> When an exact dependency transition is guarded by an environment marker, can file-level direct consumption plus command success establish the proposed version for every consuming matrix row, or must source extraction/applicability remain bound to the exact runtime environment?

## G — Existing-evidence gap

S014 establishes that successful pip execution does not imply fresh installation. It assumes the exact requested version is applicable to the selected command environment.

S015 tests the earlier boundary: the same changed source file is consumed across a Python matrix, but the changed pytest requirement is applicable only to Python 3.8.

Current UpgradePilot source adds an upstream gap: `src/upgradepilot/dependency/requirements.py` recognizes only bare whole-line `package==version` pins. Marker-decorated exact pins do not match `_PINNED_REQUIREMENT_PATTERN`, so this real proposal cannot currently produce the normal exact-requirement transition at all.

## C — Consequence

Two errors are possible if marker semantics are lost:

1. false positive: a successful Python 3.9/3.10/... install from the changed file is credited as proving `pytest==9.0.3` even though that exact marker does not apply;
2. false negative/over-broad failure interpretation: the Python 3.8 row fails on the applicable pytest 9.0.3 requirement and that failure is generalized to rows where the requirement is intentionally ignored.

This is relevant to source extraction, F4/matrix Target composition, and B5 P2.

## E — Evidence feasibility

Exact public evidence is available.

Python 3.9 job `85302679286` succeeds. Its pip log explicitly says:

`Ignoring pytest: markers 'python_full_version == "3.8.*"' don't match your environment`

and installs `pytest-8.4.2`, the Python-3.9-specific requirement.

Python 3.8 job `85302679272` applies the changed marker-scoped line and fails:

`ERROR: Could not find a version that satisfies the requirement pytest==9.0.3`

`ERROR: No matching distribution found for pytest==9.0.3`.

Other matrix rows succeed under their own marker-selected pytest variants.

## S — Safe boundary

All evidence is public/read-only. No rerun, mutation, credential, or private data is required.

## N — Negative-result value

If current UpgradePilot intentionally keeps marker-bearing requirements unsupported, S015 still defines the correct explicit limitation and prevents accidental file-level overclaim. If marker support is later added, S015 becomes a regression/evaluation case for environment applicability.

## L — Claim limit

S015 may establish:

- this exact marker-scoped transition;
- row-specific applicability in the observed CI matrix;
- current extractor non-support for marker-decorated exact pins;
- the need to keep applicability attached to the selected environment if support is added.

It must not establish marker prevalence, universal pip marker behavior beyond documented/observed semantics, package absence after a failed command, update safety, or a required parser architecture.

## T — Stop condition

Stop when source identity, current extractor boundary, unchanged workflow, Python 3.8 applicable failure, Python 3.9 inapplicable success, and the proof limits are preserved.

## F — Case form

Untouched real public evidence is the correct form because the central value is that the matrix/applicability split occurs naturally in a real Dependabot update.

## Admission decision

**PASS.** S015 is materially distinct from S014 and pressures an upstream source/applicability boundary that B5 depends on.

Primary evaluation roles:

- `integration_reality_check`
- `property_invariant`
- `method_comparison`
- `stopping_sufficiency`