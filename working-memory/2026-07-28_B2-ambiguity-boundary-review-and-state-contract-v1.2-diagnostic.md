# B2 Ambiguity-Boundary Review and State-Contract v1.2 Diagnostic

**Date:** 2026-07-28  
**Operation:** Review the Gemma E4B state-contract v1.1 ambiguity failure, freeze the claim-category and `changed_unspecified` boundary, and select one bounded v1.2 diagnostic  
**Reviewed result:** [`2026-07-28_B2-gemma-e4b-state-contract-v1.1-diagnostic-result.md`](2026-07-28_B2-gemma-e4b-state-contract-v1.1-diagnostic-result.md)  
**Prior contract review:** [`2026-07-28_B2-gemma-e4b-smoke-review-and-state-contract-diagnostic.md`](2026-07-28_B2-gemma-e4b-smoke-review-and-state-contract-diagnostic.md)  
**Raw evidence:** [`evidence/2026-07-28-gemma-e4b-state-contract-v1.1/`](evidence/2026-07-28-gemma-e4b-state-contract-v1.1/)  
**Result classification:** Evidence accepted; state contract v1.1 corrected the original failure; ambiguity oracle revised; category/change-state boundary and one v1.2 diagnostic selected; no model or product adoption

## 1. Audit conclusion

The pushed diagnostic is sufficiently complete and internally traceable to support the next decision.

Verified:

```text
Gate A clear fix: 3/3 passed
Gate B no decision-relevant claim: passed
Gate B ambiguity: failed against the frozen oracle
conflict case: correctly not run after stop condition
all returned objects: structurally valid and cross-field consistent
exact quotation grounding: passed
runtime and restoration: passed
```

The state-contract v1.1 prompt corrected the first clear-fix failure. Gemma selected `resolved` consistently for three identical explicit fix claims and correctly selected `no_decision_relevant_claim` for documentation-only text.

The ambiguity failure is not a repeat of the original cross-field inconsistency. The returned object was internally coherent:

```text
state: resolved
one grounded claim
zero unresolved reasons
```

The remaining disagreement is about the semantic vocabulary and oracle.

## 2. Exact ambiguity result

Source:

> Compatibility behavior was adjusted for older environments.

Observed:

```text
state: resolved
category: compatibility_assurance
change state: changed_unspecified
source quote: exact complete sentence
unresolved reasons: none
```

The preserved model reasoning made two separate judgments:

1. the existence of an adjustment was explicit and grounded;
2. the direction and concrete details of the adjustment were unspecified.

It therefore selected `changed_unspecified` and treated the minimum claim as resolved.

That reasoning is compatible with part of the current prompt. The prompt says to use `changed_unspecified` when a change is explicit but its direction is not. The frozen oracle simultaneously required every such missing direction/detail in this sentence to force `unresolved`.

The oracle and vocabulary therefore overlapped.

## 3. Category finding — the model was wrong

`compatibility_assurance` is not a general category for every sentence containing the word “compatibility.”

Operational definition:

> Use `compatibility_assurance` only when the source explicitly assures continued compatibility, backward compatibility, drop-in replacement behavior, or absence of required migration.

Examples that qualify:

```text
This release is backward compatible with the previous patch release.
This release is a drop-in replacement and requires no migration.
Existing integrations continue to work without changes.
```

The ambiguity source does not provide an assurance. It reports that compatibility-related behavior changed.

Correct category:

```text
interface_or_behavior_change
```

This is a real model classification error under the intended category boundary, but the prompt had not yet defined the categories operationally enough. The next diagnostic must teach and validate that boundary before using it to compare models.

## 4. State and `changed_unspecified` decision

### Semantic-state responsibility

The semantic state describes whether the extractor can responsibly represent the **minimum explicit source meaning**.

It does not decide:

```text
whether the source is detailed enough for a maintainer action
whether evidence is sufficient
whether more investigation is needed
whether an upgrade is compatible or safe
```

Those belong to later deterministic sufficiency, stopping, and action logic.

Therefore:

```text
resolved semantic extraction
≠ sufficient decision evidence
```

### Accepted meaning of `changed_unspecified`

`changed_unspecified` is admitted only when all of the following are true:

1. the source explicitly states that an interface or behavior changed;
2. the changed subject or scope is identifiable from the source;
3. the occurrence of the change is not ambiguous;
4. the direction, effect, or detailed mechanics are not stated;
5. the claim does not require inventing compatibility, safety, support direction, or migration consequences.

Its meaning is deliberately weak:

> An explicit interface or behavior change occurred; the source does not state its direction or effect.

It must not be interpreted as improvement, regression, compatibility assurance, breaking change, or safety evidence.

### When missing information forces `unresolved`

Use `unresolved` when the minimum source meaning cannot be represented by one supported category/change-state pair without invention.

Examples include:

- the text only says something “may be affected” without stating a change;
- the referent or affected subject cannot be identified;
- a support boundary changed but the source does not say whether support was added or dropped, and no neutral support-change state exists;
- current versus future timing cannot be determined where timing changes the claim state;
- the sentence can reasonably map to materially different supported categories;
- the source is incomplete or context-dependent enough that accepting a claim would overstate it.

### Revised oracle for the exact ambiguity source

Expected minimum extraction:

```text
state: resolved
category: interface_or_behavior_change
change state: changed_unspecified
subject: compatibility behavior for older environments, or an equivalent source-faithful subject
source quote: exact complete sentence
unresolved reasons: none
```

Claim limit:

> The release explicitly states that compatibility behavior for older environments was adjusted. It does not state whether compatibility improved or worsened, which environments are affected, what behavior changed, whether migration is needed, or whether the release is safe.

The previous `unresolved + no claims` oracle is superseded for this exact case.

## 5. Frozen category/change-state matrix

The next deterministic validator must enforce these accepted pairs:

```text
fix_or_remediation
→ fixed

compatibility_assurance
→ compatibility_assured

support_boundary_change
→ support_added | support_dropped

interface_or_behavior_change
→ deprecated | removed | future_removal | changed_unspecified
```

Any other pair is invalid even when the flat JSON Schema accepts it.

This would reject the observed combination:

```text
compatibility_assurance + changed_unspecified
```

The matrix is a domain invariant, not a model judgment.

## 6. State-contract prompt version 1.2

Version 1.2 keeps the four state definitions from v1.1 and adds explicit category and weak-change semantics.

The prompt must teach:

1. `compatibility_assurance` requires explicit assurance language; the word “compatibility” alone is insufficient;
2. compatibility-related behavior adjustments belong to `interface_or_behavior_change`, not `compatibility_assurance`;
3. `changed_unspecified` is allowed only for an explicit interface/behavior change with identifiable subject or scope but unspecified direction/effect;
4. `resolved` means the minimum claim was represented responsibly, not that the source is sufficient, safe, compatible, or actionable;
5. `unresolved` is required when no supported category/change-state pair can represent the minimum meaning without invention;
6. support-boundary direction is mandatory because the vocabulary contains only `support_added` and `support_dropped`.

The flat schema remains unchanged for this diagnostic. Deterministic validation gains only the frozen category/change-state matrix and revised case oracles.

## 7. Non-tailored contrast cases

The boundary must be tested with cases not written as paraphrases of the failed sentence.

### A. Exact compatibility-behavior adjustment

Source:

```text
Compatibility behavior was adjusted for older environments.
```

Expected:

```text
resolved
interface_or_behavior_change / changed_unspecified
one exact grounded claim
zero unresolved reasons
```

### B. Generic explicit behavior change with unknown direction

Source:

```text
Request retry behavior changed for slow networks.
```

Expected:

```text
resolved
interface_or_behavior_change / changed_unspecified
one exact grounded claim
zero unresolved reasons
```

### C. Explicit compatibility assurance

Source:

```text
This release remains backward compatible with the previous patch release and requires no migration.
```

Expected:

```text
resolved
compatibility_assurance / compatibility_assured
one exact grounded claim
zero unresolved reasons
```

### D. Genuinely unresolved relevance

Source:

```text
Older environments may be affected.
```

Expected:

```text
unresolved
zero accepted claims
one or more reasons explaining that no explicit change, support direction, or assurance is stated
```

### E. Support boundary without required direction

Source:

```text
Python version support policy changed in this release.
```

Expected:

```text
unresolved
zero accepted claims
one or more reasons explaining that added versus dropped support is not stated
```

### F. No decision-relevant claim regression control

Source:

```text
Documentation examples were reorganized and several spelling errors were corrected.
```

Expected:

```text
no_decision_relevant_claim
zero claims
zero unresolved reasons
```

### G. Conflict completion case

Source:

```text
This release adds Python 3.13 support. This release drops Python 3.13 support.
```

Expected:

```text
conflicting
two grounded support_boundary_change claims
support_added and support_dropped
one or more conflict reasons
```

## 8. Selected bounded diagnostic

Keep frozen:

```text
Gemma E4B model and Q4_K_XL quantization
4096 context and existing load configuration
parallelism 1
Flash Attention and GPU KV-cache placement
temperature 0 and seed 0
512-token output budget
non-streaming /v1/chat/completions endpoint
flat JSON Schema
source-span grounding rules
no Instructor or retry layer
```

Change only:

```text
prompt contract v1.1 → v1.2 category/changed_unspecified clarification
deterministic validator → add category/change-state matrix
case oracle → revise exact ambiguity expectation and add frozen contrasts
```

### Gate A — exact ambiguity boundary

Run the exact failed ambiguity source three times.

Required:

```text
3/3 resolved
3/3 interface_or_behavior_change / changed_unspecified
3/3 exact grounding
3/3 zero unresolved reasons
no compatibility assurance
no invented direction or effect
```

Stop on the first failure.

### Gate B — contrast suite

Only after Gate A passes, run cases B through F once each.

Stop on the first structural, domain-invariant, grounding, state, category, change-state, or semantic failure.

### Gate C — complete the four-state micro-suite

Only after Gate B passes, run the conflict completion case once.

Stop and push the evidence after Gate C. Do not enter the broader ten-case corpus automatically.

## 9. Decision after v1.2

Possible conclusions:

- all gates pass: freeze the extraction vocabulary and consider the broader Gemma corpus;
- category boundary remains unstable: retain Gemma as an operational control and test Qwen 3.5 9B under the same frozen contract;
- state boundary remains unstable: reconsider whether the model should select the global state or whether deterministic code should derive it from validated claims and reasons;
- support-direction or conflict handling fails: diagnose that narrow semantic responsibility before broader scoring;
- runtime changes materially: classify the runtime layer separately.

A model comparison is meaningful only after this contract can judge both models consistently.

## 10. Instructor and product disposition

Instructor remains deferred. It could encode the category/change-state matrix in Pydantic validation, but the current diagnostic concerns the semantic contract and model output, not adapter ergonomics.

No product source, active dependency, model adoption, recommendation method, or network-exposure change is authorized.

## 11. Exact continuation

Ali or the local assistant should create one new dated result record that:

1. references this review and the v1.1 result;
2. identifies the prompt as state contract v1.2;
3. preserves the exact v1.2 prompt addition and complete prompt;
4. preserves the unchanged schema and frozen runtime/model settings;
5. implements and self-tests the deterministic category/change-state matrix;
6. freezes the seven diagnostic cases and revised oracles before inference;
7. runs Gate A through its stop condition;
8. runs Gate B only if Gate A passes;
9. runs Gate C only if Gate B passes;
10. preserves raw requests, responses, reasoning/logs, validation, resources, hashes, and restoration;
11. runs and preserves the existing product test result without changing product source;
12. stops before the broader corpus, pytest release input, Instructor, Qwen, Gemma 12B, networking changes, or product integration;
13. updates `MEMORY.md` with the observed result and exact continuation;
14. pushes the complete evidence bundle for independent review.
