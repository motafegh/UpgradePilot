# B2 Target Python Relevance Step 2 — Support-drop claim contract validation

**Recorded:** 2026-07-31 22:58 +03:30  
**Route:** B2 — Public PR vertical slice  
**Selected plan:** [`../plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](../plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)  
**Focused Step 2 plan:** [`../plans/B2_STEP_2_SUPPORT_DROP_CLAIM_CONTRACT_PLAN.md`](../plans/B2_STEP_2_SUPPORT_DROP_CLAIM_CONTRACT_PLAN.md)  
**Status:** Complete and behavior-validated

## Validated implementation boundary

The Step 2 product/test revision remains:

```text
c023a3b09e5dc5d31e3bd0a55820b9d83a51f4db
```

Later implementation-record, validation, and memory commits do not alter that source/test boundary.

## Deterministic validation

The user reported that both required Step 2 validation gates passed:

```text
focused Step 2 suite: passed
complete deterministic suite: passed
```

The focused command covered:

```text
tests.test_upstream_claim
tests.test_upstream_claim_edges
tests.test_package_interface
```

The exact terminal summary lines, test counts, and timings were not supplied in the final message, so this record does not invent them. The pass result is recorded from the user's explicit report.

## Validated trust boundary

Behavior-validated:

```text
AuthoritativeUpstreamIntervalEvidence
+ untrusted CandidateUpstreamClaimResult
→ GroundedPythonSupportDropClaim
   or explicit UpstreamSupportDropClaimProblem
```

The validated boundary establishes:

- exact dependency-context echo validation;
- candidate state invariants;
- only `support_boundary_change` / `support_dropped` admission;
- canonical major/minor Python-line validation;
- trusted crossed-release membership;
- exact release-body or tagged-changelog source resolution;
- exact quote/span equality against immutable Step 1 source text;
- quote-to-normalized-Python-line correspondence;
- equivalent evidence aggregation and duplicate removal;
- invalid-candidate precedence;
- explicit ambiguity for several distinct support-drop claims;
- no model, network, target comparison, compatibility, safety, or recommendation behavior.

## Step 2 stop-line result

Step 2 is complete and behavior-validated.

The next authorized parent-plan responsibility is:

```text
Step 3 — Record and freeze the packaging method
```

That step must decide and test:

- the exact runtime `packaging` dependency bound;
- PEP 440 parsing and ordering for dependency versions;
- old-exclusive/proposed-inclusive crossed-release ordering;
- stable Python-line semantics;
- standards-based `requires-python` specifier parsing;
- supported operators and explicit unsupported forms;
- a complete non-enumerative line-overlap method;
- invalid, equivalent, backwards, unsatisfiable, and unsupported results.

Do not begin model integration, network interval acquisition, full target-relevance mapping, or CLI orchestration during Step 3.

## Learning state

Step 2 concepts are behavior-validated at product level:

- candidate schema versus trusted domain evidence;
- exact source and span grounding;
- normalized field correspondence;
- interval membership;
- ambiguity and invalid-candidate precedence.

No user-owned explanation, independent implementation, or formal mastery assessment is recorded. Product validation and learning mastery remain separate claims.
