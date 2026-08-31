# B2/X1 EvidenceGapPlanner R4-A2 — focused runtime failure and test repair

**Date:** 2026-08-31  
**Mode:** Learning-by-Doing / Build validation  
**Scope:** focused R4-A1 + R4-A2 runtime proof and test-quality repair

## 1. First observed runtime result

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

The serialized request contained the legitimate structured planning-evidence fact name:

```text
witness_path
```

It did not expose the hidden exact executable action field:

```text
path
```

## 2. First diagnosis

This was a **test-observation defect**, not an authority-boundary leak.

The old assertion serialized the complete request to JSON text and then checked:

```text
assert hidden substring not in serialized JSON
```

That is too coarse for a hidden field named `path`, because any legitimate data containing the same substring—for example the fact name `witness_path`—produces a false positive.

The implementation evidence from the failed payload still showed the model-visible action descriptor contained only:

```text
action_id
purpose
target_proposition
evidence_yield
```

and no exact action `path`, repository, revision, precondition, mutation, or result-family field was present.

## 3. First repair

The focused R4-A1 projection test was changed to inspect **exact mapping keys recursively** rather than arbitrary substrings in serialized JSON.

First repair commit:

```text
5550b9d9b26da2a462f8fd6ae3669c0bfc65ed49
```

## 4. Second observed runtime result

After pulling the first repair, Ali reran the same focused 23-test command.

Again:

```text
Ran 23 tests in 0.003s
FAILED (failures=1)
```

All 13 R4-A2 tests still passed. The same R4-A1 projection test failed on the newly added assertion:

```text
self.assertIn("witness_path", request_keys)
```

Observed `request_keys` correctly contained dictionary keys such as:

```text
name
value
facts
planning_evidence
...
```

but not `witness_path`.

## 5. Second diagnosis

The recursive key collector was behaving correctly. The new positive assertion misunderstood the actual `PlanningEvidenceFact` wire representation.

A witness-path fact is rendered as:

```json
{
  "name": "witness_path",
  "value": ["mkdocs-llmstxt", "beautifulsoup4", "soupsieve"]
}
```

Therefore:

```text
"name"         → mapping key
"value"        → mapping key
"witness_path" → value carried by the `name` field
```

So `witness_path` should **not** appear in a set that intentionally collects mapping keys only.

This is a second test-model defect, distinct from the first one:

```text
first defect
→ textual substring search was too broad

second defect
→ structural assertion misunderstood the representation
```

The separate test `test_structured_planning_evidence_preserves_witness_path_without_raw_source` already proves that the `witness_path` fact and its value survive the projection.

## 6. Second repair

The projection-boundary test now does only the responsibility it owns:

```text
request
→ recursively collect exact dictionary keys
→ assert exact hidden authority keys are absent
```

The invalid positive assertion that `witness_path` must be a dictionary key was removed. The nearby structured-evidence test remains the owner of proving the witness-path fact is preserved.

Second repair commit:

```text
be97e6d546338bfc67b2867219b1a3af6cb508b3
```

## 7. Learning/model correction

The two failures together establish an important testing lesson:

```text
test failure
!= automatically implementation failure
```

A test has its own observation model and representation assumptions. Good focused tests must measure the exact proposition they claim to prove.

For the projection-boundary test, the actual proposition is:

> No mapping key owned by hidden execution authority crosses the model boundary.

For the structured-evidence test, a separate proposition is:

> The selected `witness_path` planning fact survives the projection with its intended value.

Keeping these proofs separate is clearer than making one test infer both from serialized text or from the wrong structural level.

## 8. Current proof state

After the second observed run and second repair:

```text
R4-A2 admission tests observed PASS
→ YES (13/13 in both supplied runs)

R4-A1 non-projection tests observed PASS
→ YES

projection authority leak established
→ NO

first test defect diagnosed/repaired
→ YES

second representation-assumption defect diagnosed/repaired
→ YES

repaired focused suite runtime PASS
→ PENDING RERUN
```

Do not advance to R4-A3 until the second repaired focused suite is rerun and the result is inspected.
