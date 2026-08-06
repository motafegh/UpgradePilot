# B2 Step 7F — Live Upstream Repository Generality Gap

**Date:** 2026-08-05  
**Status:** Correction implemented; WSL regression and normal-path live rerun pending

## Trigger

After Step 7E and the Step 7F controlled/full regressions were reported green, the normal product CLI was run against the selected S001 proof case:

```bash
time env -u GITHUB_TOKEN python -m upgradepilot pydantic/pydantic 13432
```

The active product correctly established:

- exact PR identity for `pydantic/pydantic` PR `13432`;
- `soupsieve 2.6 -> 2.8.4` from exact base/head `uv.lock` evidence;
- independent exact-head CI evidence, with the bounded dependency-exercise result remaining `unresolved`;
- exact PyPI package evidence for `soupsieve==2.8.4`.

The run then stopped before crossed-release acquisition, changelog construction, or LM Studio inference with:

```text
Upstream repository: unsupported_source
Upstream detail: PyPI metadata contains no well-known Source candidate.
```

This is an honest product stop, not an LLM/runtime failure.

## Root cause

The exact PyPI release metadata for Soup Sieve 2.8.4 identifies its GitHub repository through:

```text
Homepage -> https://github.com/facelessuser/soupsieve
```

The current resolver admitted only normalized labels:

```text
Source
Repository
Source Code
GitHub
```

The earlier scenario-specific Step 5 live acquisition tool had supplied `facelessuser/soupsieve` explicitly because that tool was validating later acquisition components, so that earlier proof did not establish generic product repository resolution for S001.

The normal Step 7F product run therefore exposed a real minimum-useful-generality gap in the repository-association input boundary.

## Correction

The resolver now admits `Homepage` alongside the existing repository-bearing project URL labels, but the authority boundary is unchanged:

```text
admitted PyPI project-link candidate
+ canonical HTTPS github.com/owner/repository URL
+ usable exact-distribution PyPI provenance
+ one supported GitHub publisher repository
+ metadata/provenance repository agreement
-> UpstreamRepositoryEvidence
```

`Homepage` is not trusted by itself.

The correction also preserves ambiguity:

```text
Source -> repository A
Homepage -> repository B
-> ambiguous_source
```

and preserves `source_unavailable` when a Homepage candidate exists but no usable exact-file provenance is available.

Implementation commits:

```text
8f652d4e8e4e8bf274b5e8f838117319a99cbaa4
6fdf55749950be38908995ba8d99c7249a459f88
```

## Why this remains inside the accepted B2 boundary

The controlling upstream-evidence plan accepts publisher-supplied PyPI project-link candidates as discovery evidence and separately requires validated project-controlled upstream identity. It does not require the literal `Source` label as the only admissible metadata spelling.

The correction therefore broadens a bounded metadata-label input class while preserving the stronger provenance-backed trust rule. It does not hardcode Soup Sieve, Pydantic, a repository name, a version, or a final answer.

## Required continuation

1. Run focused upstream-repository tests.
2. Run the full active product regression.
3. Rerun the normal S001 CLI proof.
4. If repository identity becomes available, continue observing the same normal run through crossed releases, exact changelog, real local semantic extraction, deterministic grounding, conditional target acquisition, and target relevance.
5. Do not close Step 7 or the parent Target-Python responsibility until the normal-path live result reaches the bounded expected relevance outcome.
