# S015 — charset-normalizer pytest: marker-scoped dependency applicability

**Date:** 2026-09-22
**Status:** Complete at admitted simulation depth
**Form:** untouched real Dependabot proposal + exact matrix/runtime evidence

## Case identity

Target: `jawah/charset_normalizer#769`

Relevant transition in `ci-requirements.txt`:

`pytest==8.3.5 ; python_full_version == '3.8.*'`

to:

`pytest==9.0.3 ; python_full_version == '3.8.*'`.

Frozen revisions:

- base: `aa2ddd8fb788b98a815f25c37609e919105d1dbb`
- head: `fba29ea1027f3c3eaaea8c3cc64b71fbb392251c`
- observed PR runtime merge checkout: `ddf477c2e71894890245a780ea17d2368d4ad64d`

The CI workflow blob is identical at base/head: `760ab82d9c7a95a9c1d13b72079f864529a32033`.

## Owned question

> Does direct consumption of a changed requirements file plus successful command execution establish the changed exact version for every consuming matrix row when that requirement is guarded by an environment marker?

## Current-product projection

Current UpgradePilot does not yet reach that question for this proposal.

`src/upgradepilot/dependency/requirements.py` uses a whole-line exact-pin regex that accepts bare `package==version` only. A marker-bearing line such as:

`pytest==9.0.3 ; python_full_version == '3.8.*'`

does not match the current exact-requirement extraction boundary.

So today the proposal is conservatively unsupported at source extraction. S015 preserves what must remain true if marker-bearing exact requirements are admitted later.

## Exact CI sequence

The unchanged tests job consumes the same file across Python 3.7 through 3.14:

`python -m pip install -r ci-requirements.txt --require-hashes`.

### Python 3.9 row

Job `85302679286` succeeds.

The pip log explicitly states:

`Ignoring pytest: markers 'python_full_version == "3.8.*"' don't match your environment`

and later installs `pytest-8.4.2`, which is the requirement applicable to Python 3.9.

Therefore the changed file is consumed and the command succeeds, but the proposed `pytest==9.0.3` requirement is not applicable to that row.

### Python 3.8 row

Job `85302679272` reaches the same requirements command, where the changed marker applies.

pip attempts `pytest==9.0.3` and fails:

`ERROR: Could not find a version that satisfies the requirement pytest==9.0.3`

`ERROR: No matching distribution found for pytest==9.0.3`.

The overall CI run fails because of this row while several other Python rows succeed.

## Core distinction

`changed source file consumed`

is not equivalent to:

`changed exact requirement applies in this selected environment`.

Likewise:

`same requirements command succeeded in another matrix row`

does not establish:

`the proposed marker-scoped version was satisfied there`.

Source identity, marker applicability, and selected runtime environment must compose before B5 state proof.

## Relationship to B5

S015 validates why B5 P2 must be stronger than file identity alone:

`exact source/environment relation` must establish that the exact proposed requirement is actually required in this exact workflow/runtime context.

Only after that can command semantics/success participate in a satisfaction-at-completion claim.

## Relationship to B5 asymmetry

The Python 3.8 command failure means this command-derived positive proposition is unavailable.

It does **not** establish that pytest 9.0.3 was absent before command start or that pytest was absent in general.

The Python 3.9 success likewise proves only its applicable requirements, not the inapplicable 3.8-specific requirement.

## What S015 establishes

- marker-scoped exact dependency updates occur in real Dependabot proposals;
- the same changed requirements file can have different dependency applicability across matrix rows;
- command success at file level is insufficient without requirement-to-environment applicability;
- current UpgradePilot exact-requirement extraction intentionally/structurally does not support marker-bearing exact pins;
- if support is added, marker semantics must remain attached to the dependency proposition and selected environment.

## What S015 does not establish

Do not infer:

- marker prevalence;
- package absence from the failed Python 3.8 command;
- that all matrix rows need separate product objects in every design;
- a required parser implementation;
- compatibility or maintainer action.

## Evidence bundle

1. `artifacts/CASE_IDENTITY_AND_SOURCE.json`
2. `artifacts/PY39_INAPPLICABLE_SUCCESS.json`
3. `artifacts/PY38_APPLICABLE_FAILURE.json`
4. `artifacts/CURRENT_PRODUCT_PROJECTION.json`

Supporting analysis:

- `../../S015_CANDIDATE_SCREENING.md`
- `../../S015_POST_CASE_SYNTHESIS.md`

## Stop

S015 stops after establishing the source/applicability split and current extractor boundary. Reopen only for a concrete marker-support design, matrix-instance Target composition, or B5 implementation transfer.