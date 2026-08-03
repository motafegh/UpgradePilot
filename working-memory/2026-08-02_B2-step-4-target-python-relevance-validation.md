# B2 Step 4 — Target-Python Relevance Validation

**Date:** 2026-08-02  
**Responsibility:** Preserve observed validation evidence for parent-plan Step 4 without becoming a live-state owner.

## Validated boundary

Step 4 adds the pure deterministic mapping:

```text
UpstreamSupportDropClaimResult
+ conditional TargetPythonEvidence
→ TargetPythonRelevanceResult
```

The product/test implementation boundary is commit:

```text
cceb8da55e5908f346141545eacdca4672f7d977
```

The user pulled repository `main` through the later documentation/state commit:

```text
9d09a669fe8f7ba31fdd326baa119f6ec2e1559a
```

The commits between the Step 4 product/test boundary and that pulled head changed only repository documentation/state records, not executable source or tests.

## Observed validation

After the pull, the user reported the complete deterministic repository suite result:

```text
Ran 263 tests in 0.058s

OK
```

The complete discovery suite contains `tests/test_target_python_relevance.py` and `tests/test_package_interface.py`, so the focused Step 4 subset does not need to be rerun merely to establish the same executable behavior.

No separate focused-suite pass is claimed because the user did not report its terminal summary.

## What this validates

The observed complete-suite pass behavior-validates Step 4's controlled responsibilities, including:

- S001-shaped Python `3.8` support drop plus target `requires-python >=3.10` mapping to `outside_declared_python_range`;
- positive declared-line overlap with exact stable witness preservation;
- target parser problem states mapping to `target_declaration_unresolved`;
- unresolved upstream results stopping before target comparison;
- invalid activation sequencing being rejected as caller misuse;
- valid-but-unsupported PEP 440 forms mapping to `comparison_unsupported`;
- invalid or contradictory target declarations remaining target-unresolved;
- defensive malformed grounded-claim Python-line handling;
- the public Step 4 package interface.

## What this does not validate

This result does not establish:

- upstream interval network acquisition;
- tagged-changelog discovery or acquisition;
- model/Instructor extraction;
- conditional CLI acquisition order;
- live S001 end-to-end behavior;
- compatibility, safety, recommendation, or maintainer action;
- user mastery.

## Closure

Step 4 satisfies its controlled implementation gate and may be closed as behavior-validated.

The next parent-plan responsibility is Step 5 — authoritative upstream interval acquisition. `MEMORY.md` alone owns that live activation and exact continuation.
