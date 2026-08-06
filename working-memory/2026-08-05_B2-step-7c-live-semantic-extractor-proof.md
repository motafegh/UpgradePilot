# B2 Step 7C Live Semantic Extractor Proof

**Date:** 2026-08-05  
**Scope:** Real S001 Step 7C product-adapter live proof after loopback proxy isolation  
**Result:** PASS

## Proven flow

```text
real public S001 upstream evidence
→ trusted Soup Sieve crossed releases 2.7 through 2.8.4
→ exact tag commit 28108ab805818c832d9568142a99844fd95a0d39
→ exact changelog docs/src/markdown/about/changelog.md
→ Step 7B bounded source window
→ Step 7C LocalSupportDropExtractor
→ LM Studio localhost / gemma-4-e4b-it-ud
→ contract-v2 candidate result
→ deterministic exact-line reconstruction
→ validate_support_drop_candidates(...)
→ grounded Python support-drop claim
```

## Live observations

Trusted source context:

```text
package interval: soupsieve 2.6 -> 2.8.4
crossed releases: 2.7, 2.8, 2.8.1, 2.8.2, 2.8.3, 2.8.4
exact commit: 28108ab805818c832d9568142a99844fd95a0d39
changelog blob: 6f221b7398681a580fa199044b3d3f1e11b55493
source-order sections: 2.8.4, 2.8.3, 2.8.2, 2.8.1, 2.8, 2.7
bounded window: 1450 / 4096 characters
```

Provider preflight after proxy isolation:

```text
GET /v1/models: HTTP 200
selected model visible: gemma-4-e4b-it-ud
automatic retries: disabled
ambient proxy inheritance: disabled for LM Studio loopback traffic
```

Observed inference:

```text
POST /v1/chat/completions: HTTP 200
elapsed: 20.682 seconds
adapter return: 20.683 seconds
```

Model candidate after deterministic reconstruction:

```text
state: candidates_available
candidate count: 1
python_line: 3.8
introduced_in_version: 2.8
source_kind: tagged_changelog
source_quote: -   **NEW**: Drop support for Python 3.8.
exact offsets: 729:770
```

Deterministic trust admission:

```text
state: grounded
python_line: 3.8
introduced_in_version: 2.8
grounded sources: 1
```

## Interpretation

This closes Step 7C's live proof obligation for the selected S001 case. It establishes that the accepted local model adapter can consume the real Step 7B bounded window, return the expected narrow semantic candidate, reconstruct the exact authoritative source line, and pass the existing deterministic trust boundary.

It does **not** establish target-Python relevance, dependency compatibility, upgrade safety, or merge readiness.

The next bounded increment is Step 7D: compose source-window construction, candidate extraction, and deterministic claim admission behind one upstream-domain runtime function. Target-Python activation remains deferred to Step 7E.
