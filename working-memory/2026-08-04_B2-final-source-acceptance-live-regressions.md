# B2 Final Source Acceptance — Live Regression Results

**Date:** 2026-08-04  
**Scope:** final source-structure acceptance live-source regressions only; no new product capability

## Step 7A exact-commit changelog discovery

Ali reran the final-tree Step 7A public proof after the flat compatibility modules were removed.

Result:

```text
LIVE STEP 7A PROOF: PASS
repository: facelessuser/soupsieve
exact commit: 28108ab805818c832d9568142a99844fd95a0d39
tree SHA: 183f563a271635247327f1f0b1dddb158e0add39
path: docs/src/markdown/about/changelog.md
admitted candidate count: 1
```

This confirms that the final GitHub provider topology preserves the generic exact-commit changelog discovery behavior and does not depend on any removed flat module or product path constant.

## Initial Step 5 proof failure

The first final-tree Step 5 upstream acquisition rerun stopped at Git tag-to-commit resolution:

```text
LIVE STEP 5 PROOF: FAIL
stage: Git tag-to-commit resolution
state: acquisition_failed
detail: GitHub returned HTTP 401 while acquiring tag-reference evidence.
```

This was not a tag-identity, interval, changelog, or source-structure logic failure. The scenario proof read an optional `GITHUB_TOKEN` from the shell and passed it into `GitHubTagCommitClient` and `GitHubRepositoryClient`. The shared GitHub API client sends `Authorization: Bearer <token>` whenever a token is present. A stale or invalid inherited token can therefore make an otherwise public read fail with HTTP 401 before tag identity is evaluated.

Step 7A did not reproduce this failure because its live proof deliberately used anonymous public GitHub reads.

## Correction

The Step 5 scenario proof was changed to use anonymous GitHub reads as well. This change is limited to public validation tooling; product authentication semantics were not changed.

Reasoning:

```text
public historical proof
+ public GitHub repository
+ optional unrelated shell credential

must not become

false structural regression due to stale Authorization header
```

The proof now prints that GitHub authentication mode is anonymous/public and constructs both GitHub clients with `token=None`.

## Step 5 rerun after correction

Ali pulled the correction and reran:

```text
LIVE STEP 5 PROOF: PASS
```

Exact observed evidence:

```text
PyPI source: https://pypi.org/pypi/soupsieve/json
crossed releases: 2.7, 2.8, 2.8.1, 2.8.2, 2.8.3, 2.8.4
ignored non-PEP-440 release keys: none
tag ref: refs/tags/2.8.4
direct tag object: commit 28108ab805818c832d9568142a99844fd95a0d39
resolved commit: 28108ab805818c832d9568142a99844fd95a0d39
annotated-tag peel depth: 0
changelog path: docs/src/markdown/about/changelog.md
changelog blob SHA: 6f221b7398681a580fa199044b3d3f1e11b55493
changelog bytes: reported=17370, decoded=17370
authority basis: tagged_changelog
GitHub Release bodies admitted: 0
```

This validates the final source topology across:

```text
PyPI release-index acquisition
→ crossed-release selection
→ GitHub tag resolution
→ immutable commit identity
→ exact changelog file acquisition
→ byte agreement
→ tagged changelog composition
→ upstream interval authority
```

No changelog semantics, model inference, target-Python relevance, compatibility, safety, merge, or recommendation behavior was evaluated by this proof.

## Classification of the 401 incident

Final classification:

```text
environment/authentication contamination in scenario validation tooling
```

Not:

```text
source-structure regression
Git tag-resolution algorithm defect
upstream interval authority defect
changelog acquisition defect
```

Reusable lesson: a public regression proof should isolate itself from optional ambient credentials unless authenticated behavior is itself part of the proof. Otherwise a stale credential can reduce reproducibility by overriding a valid anonymous public access path.

## Remaining final acceptance work

The two live-source regressions are now green. Final source reconciliation must still not be marked fully accepted until the post-cleanup deterministic and interface checks are reported green:

```bash
python -m unittest discover -s tests -v
python -m unittest discover -s experiments/tests -v
python -m upgradepilot --help
upgradepilot --help
git status
git log -1 --oneline
```
