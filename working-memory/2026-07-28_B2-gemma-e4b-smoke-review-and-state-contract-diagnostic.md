# B2 Gemma E4B Smoke Review and State-Contract Diagnostic

**Date:** 2026-07-28  
**Operation:** Independently review the first observed Gemma E4B evidence bundle and select the smallest next diagnostic  
**Reviewed result:** [`2026-07-28_B2-gemma-e4b-observed-evaluation-result.md`](2026-07-28_B2-gemma-e4b-observed-evaluation-result.md)  
**Raw evidence:** [`evidence/2026-07-28-gemma-e4b/`](evidence/2026-07-28-gemma-e4b/)  
**Parent plan:** [`../plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md`](../plans/B2_LOCAL_LLM_SEMANTIC_EXTRACTION_REEVALUATION_PLAN.md)  
**Result classification:** Evidence bundle accepted; operational and claim-level smoke passed; state-selection contract under-specified; one prompt-contract diagnostic selected before broader scoring

## 1. Audit conclusion

The pushed evidence is sufficiently complete, internally traceable, and honest to support the next decision.

The bundle preserves:

- the initial rejected CLI invocation and the narrow command-surface correction;
- exact model identity and applied load metadata;
- pre-load, post-load, post-inference, and post-unload resource snapshots;
- the exact prompt, schema, request, outer response, parsed inner response, and validation record;
- model reasoning/output and performance logs;
- exact unload and restoration evidence;
- a manifest of raw evidence artifacts;
- the exact pytest release source acquired but deliberately not sent after the stop condition.

The result record correctly stopped before the larger corpus. It did not hide the failure, silently modify multiple variables, or claim model adoption.

## 2. Verified findings

### Operational deployment

Verified result:

```text
model load: passed
context: 4096
parallelism: 1
Flash Attention: enabled
KV cache: GPU
speculative decoding: disabled
runtime instability: not observed
restoration: passed
```

Observed GPU use increased from 1392 MiB before load to 4759 MiB after load and 4792 MiB after inference. The model retained substantial VRAM headroom and was explicitly unloaded afterward.

Operational conclusion:

> Gemma E4B is a viable local runtime candidate on Ali's current RTX 3070 Laptop environment for this bounded experiment.

This conclusion concerns runtime viability only. It does not establish semantic suitability.

### Structured-output mechanics

Verified result:

```text
HTTP transport: passed
outer JSON parsing: passed
inner JSON parsing: passed
required fields: passed
unknown fields: none
allowed enums: passed
finish reason: stop
truncation: not observed
```

The LM Studio structured-output path therefore works for this model and schema at the selected configuration.

### Claim extraction and grounding

For the source:

> This release fixes a crash when parsing empty configuration files.

The model returned:

```text
category: fix_or_remediation
subject: crash when parsing empty configuration files
change state: fixed
source quotation: exact and contiguous
```

The model's preserved reasoning also correctly recognized the sentence as a direct remediation claim. No recommendation, safety claim, compatibility inference, tool call, or unsupported source statement appeared.

Claim-level conclusion:

> The model understood and grounded the substantive release claim correctly in this smoke case.

### State-selection failure

The model also returned:

```text
state: unresolved
unresolved reasons: empty
```

That combination conflicts with the accepted claim and with itself.

The deterministic evaluator correctly classified the run as failed. The failure is fail-safe because a later trusted layer would refuse or abstain rather than accept an inconsistent semantic result.

## 3. Root-cause assessment

The evidence does not yet justify classifying this as a model-language-understanding failure.

The strongest current diagnosis is **state-contract under-specification**.

### Prompt under-specification

The system prompt explicitly explains when to use:

- `no_decision_relevant_claim`;
- `unresolved`.

It does not explicitly explain when to use:

- `resolved`;
- `conflicting`.

The model's reasoning correctly classified the claim but never reasoned about the result-state choice. That is consistent with a missing state-selection instruction.

### Flat schema under-specification

The current JSON Schema permits every state to coexist structurally with every claims/reasons combination. It allows, for example:

```text
unresolved + accepted claims + no unresolved reasons
resolved + no claims + unresolved reasons
no_decision_relevant_claim + claims
```

The schema therefore enforces field shape and enums, not cross-field state invariants.

### Schema visibility boundary

For GGUF structured output, LM Studio uses llama.cpp grammar-constrained generation. llama.cpp documents that the JSON Schema constrains the generated output but is not itself injected into the model prompt. State meaning must therefore be taught in the prompt, regardless of how much structural restriction the grammar can enforce.

### Deterministic validation remains required

Even a stronger schema cannot replace deterministic post-validation because:

- grammar compliance does not prove semantic correctness;
- llama.cpp supports only a subset of JSON Schema;
- unsupported schema features may be skipped;
- source quotation can be present while interpreted incorrectly;
- model output remains untrusted.

## 4. Decision

Do not reject Gemma E4B at this point.

Do not admit Gemma E4B to the broader semantic corpus yet.

Do not install Instructor, change model, change context, change offload, disable reasoning, or test Qwen yet.

The next diagnostic must test whether explicit state semantics correct the failure while all other material variables remain frozen.

## 5. Selected next diagnostic — state contract version 1.1

Change only the state-selection instructions supplied to the model.

Keep unchanged:

```text
model and quantization
load configuration
4096 context
parallelism
Flash Attention and KV placement
source sentence
authority boundary
claim categories and change states
flat JSON Schema shape
temperature
seed
maximum output budget
non-streaming endpoint
deterministic validator
```

Add explicit plain-English meanings for all four states:

### `resolved`

Use when the source explicitly supports one or more decision-relevant claims, those accepted claims are grounded, and no material ambiguity or conflict remains.

Expected relationship:

```text
one or more accepted claims
zero unresolved reasons
```

### `no_decision_relevant_claim`

Use when the source contains no supported decision-relevant claim.

Expected relationship:

```text
zero claims
zero unresolved reasons
```

### `unresolved`

Use when potentially relevant meaning cannot be responsibly resolved because the source is ambiguous, incomplete, or outside the supported vocabulary.

Expected relationship:

```text
zero accepted claims
one or more unresolved reasons
```

### `conflicting`

Use when the source contains materially opposing grounded claims that cannot responsibly be collapsed into one meaning.

Expected relationship:

```text
multiple grounded conflicting claims
one or more conflict reasons
```

The deterministic validator must enforce these relationships even if the schema accepts the response.

## 6. Execution order for the diagnostic

### Gate A — same clear-fix case

Run the identical clear-fix source once with only the state instructions changed.

Stop immediately if:

- structure fails;
- the claim category or direction changes incorrectly;
- grounding fails;
- the state remains inconsistent;
- a new unsupported claim appears.

If it passes, repeat the identical case two more times under the frozen configuration.

Required pass condition:

```text
three of three runs
state: resolved
one grounded fix_or_remediation/fixed claim
zero unresolved reasons
no unsupported claims
```

### Gate B — four-state micro-suite

Only after Gate A passes, test one bounded example for each remaining state behavior:

1. no decision-relevant claim;
2. materially ambiguous claim;
3. materially conflicting claims.

The existing clear-fix case already covers `resolved`.

This micro-suite checks state selection before the full ten-case semantic corpus.

### Gate C — broader corpus decision

After the four-state micro-suite, review the evidence before running the larger corpus.

Possible outcomes:

- state contract works; proceed to the frozen semantic corpus;
- state contract remains unstable; test a stronger structural schema branch;
- state contract and stronger schema remain unstable; retain Gemma only as an operational control and test Qwen 3.5 9B;
- runtime or model behavior changes materially; diagnose that specific layer.

## 7. Stronger schema branching — deferred diagnostic, not first fix

A stronger schema may later use a top-level branch for each state, with a fixed state value and state-specific array cardinalities.

This is not the first diagnostic because the model must still be told what the states mean. Grammar restrictions alone cannot teach semantic meaning.

If needed after the prompt-contract test, the branch schema must be tested directly because llama.cpp supports only a subset of JSON Schema. Root-level `oneOf` and constant values are candidate mechanisms; conditional `if`/`then`/`else` behavior is not a credible baseline for this engine.

Any stronger schema remains an optimization and additional guard. Deterministic cross-field validation remains mandatory.

## 8. Instructor disposition

Instructor remains a credible later adapter candidate, but it is not relevant to the current failure.

Instructor could:

- generate schemas from Pydantic models;
- parse typed results;
- run deterministic validators;
- expose raw completions and hooks;
- optionally retry invalid results.

It would not teach the missing state meanings or make a semantically weak model correct. Installing it now would add a second variable before the model/contract boundary is understood.

## 9. Onboarding interpretation

This result demonstrates three distinct validation layers:

```text
schema validity
→ Is the response shaped correctly?

cross-field contract validity
→ Do state, claims, and reasons agree with each other?

semantic correctness
→ Does the structured meaning accurately represent the source?
```

The current run passed the first and claim-level semantic interpretation, but failed the second.

This is why typed JSON is not the same as a valid domain object.

## 10. Exact continuation

Ali or the local assistant should produce one new dated evidence record that:

1. references this review and the first observed result;
2. identifies the state-contract prompt as version 1.1;
3. preserves the exact changed state instructions;
4. confirms all other material variables remained unchanged;
5. runs Gate A through its stop condition;
6. runs Gate B only if Gate A passes;
7. preserves raw requests, responses, validation, logs, resources, and restoration;
8. stops before the broader corpus, Instructor, Qwen, Gemma 12B, product integration, or networking changes;
9. reports whether the failure was corrected by explicit state semantics.

No product source or dependency change is authorized by this review.
