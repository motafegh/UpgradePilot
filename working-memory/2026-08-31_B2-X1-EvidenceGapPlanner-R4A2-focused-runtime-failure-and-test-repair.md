# B2/X1 EvidenceGapPlanner R4-A2 — focused runtime failure and test repair

**Date:** 2026-08-31  
**Mode:** Learning-by-Doing / Build validation  
**Scope:** focused R4-A1 + R4-A2 runtime proof and test-quality repair

## 1. Observed runtime result

Ali ran the focused experiment tests in the normal UpgradePilot WSL checkout.

Observed result:

```text
Ran 23 tests in 0.002s
FAILED (failures=1)
```

All 13 R4-A2 admission tests passed. Nine of ten R4-A1 planner-boundary tests passed. The only failure was:

```text
test_request_projection_contains_only_evidence_refined_boundary
```

Failure excerpt:

```text
AssertionError: 'path' unexpectedly found in ...
```

The serialized request contained the legitimate structured planning-evidence key:

```text
witness_path
```

It did not expose the hidden exact executable action field:

```text
path
```

## 2. Diagnosis

This was a **test-observation defect**, not an authority-boundary leak.

The old assertion serialized the complete request to JSON text and then checked:

```text
assert hidden substring not in serialized JSON
```

That is too coarse for a hidden field named `path`, because any legitimate field containing the same substring—for example `witness_path`—produces a false positive.

The implementation evidence from the failed payload still showed the model-visible action descriptor contained only:

```text
action_id
purpose
target_proposition
evidence_yield
```

and no exact action `path`, repository, revision, precondition, mutation, or result-family field was present.

## 3. Repair

The focused R4-A1 projection test was changed to inspect **exact mapping keys recursively** rather than arbitrary substrings in serialized JSON.

New test logic:

```text
request
→ recursively collect dictionary keys
→ assert `witness_path` is present as legitimate planning evidence
→ assert exact hidden key `path` is absent
→ assert all other hidden authority keys are absent
```

This tests the semantic structure we actually care about.

Repair commit:

```text
5550b9d9b26da2a462f8fd6ae3669c0bfc65ed49
```

## 4. Learning/model correction

This failure adds an important testing lesson:

```text
test failure
!= automatically implementation failure
```

A test has its own observation model. The assertion must discriminate the intended proposition.

Here the real proposition is:

> No mapping key named `path` crosses the model boundary.

The old test instead checked the stronger and incorrect proposition:

> The character substring `path` never occurs anywhere in the serialized request.

Those are not equivalent.

This is an example of a **false positive** caused by an over-broad assertion.

## 5. Current proof state

After the observed run:

```text
R4-A2 admission tests observed PASS
→ YES (13/13 in the supplied run)

R4-A1 tests before repair
→ 9 PASS / 1 false-positive test failure

projection authority leak established
→ NO

test defect diagnosed and repaired
→ YES

repaired focused suite runtime PASS
→ PENDING RERUN
```

Do not advance to R4-A3 until the repaired focused suite is rerun and the result is inspected.
