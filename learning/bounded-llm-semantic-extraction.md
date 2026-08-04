# Bounded LLM Semantic Extraction — Reusable Engineering Lessons

This note captures reusable engineering understanding from UpgradePilot's Step 6 support-drop work. It is not a progress record and does not identify the current project step.

## 1. Split semantic work from trust work

A useful pattern for evidence-backed systems is:

```text
trusted source acquisition
→ untrusted semantic selection
→ deterministic reconstruction / validation
→ trusted domain evidence
```

The LLM should own only the part that genuinely requires language understanding.

For UpgradePilot support-drop extraction, the model can choose:

```text
which explicit Python X.Y line is being dropped
which crossed release states it
which deterministic source line contains the claim
whether a zero-candidate case is ambiguous/unresolved
```

Deterministic code should own:

```text
package identity
version-interval identity
source authority
category/direction constants
canonical source text
exact quote offsets
schema/domain invariants
trust admission
```

This division makes model replacement possible without replacing trusted contracts.

## 2. Structured output constrains shape, not meaning

JSON Schema can prevent malformed representation, but it cannot prove that:

```text
"Add support for Python 3.14"
```

was not misinterpreted as a support drop.

Keep separate checks for:

```text
transport
structured generation
semantic correctness
grounding
trust admission
product activation
```

A response can pass one layer and fail the next.

## 3. Grounding is not semantic correctness

If a model selects a real source line, deterministic quote/span validation can succeed even when the model assigns the wrong meaning to that line.

Therefore:

```text
exact source match
≠ correct interpretation
```

Use a semantic oracle during model evaluation in addition to grounding.

## 4. Prefer selection over transcription

LLMs often normalize whitespace, punctuation, or formatting while preserving meaning. That makes them poor owners of exact-byte evidence.

A stronger design is:

```text
source text
→ deterministic IDs
→ model selects ID
→ code recovers original bytes
```

This preserves exact source evidence without requiring the model to copy it perfectly.

## 5. Canonicalize mechanically where possible

If the source contains explicit domain tokens, enumerate them before prompting and constrain the model to those values.

Example:

```text
source: "Python 3.8" and "Python 3.14"
model enum: ["3.8", "3.14"]
```

The model then selects meaning among valid values instead of inventing domain formatting.

## 6. Do not ask the model to predict derivable state

If a returned candidate list is non-empty, then:

```text
candidates_available
```

is deterministic.

Asking the model to return both facts independently creates a new contradiction surface.

General rule:

> If field B is a pure deterministic function of field A, strongly prefer deriving B outside the model.

## 7. Abstention needs explicit semantics

Zero-candidate outcomes often need a distinction such as:

```text
no relevant claim exists
```

versus:

```text
text may concern the target concept but cannot establish it safely
```

That distinction can be useful diagnostically even when both stop downstream activation.

Keep diagnostic precision visible, but evaluate product safety separately when downstream behavior is intentionally identical.

## 8. Keep strict and safety metrics separate

A strict semantic oracle should not be rewritten after seeing model results.

A second product-safety metric can legitimately ask a different question, such as:

```text
Did any wrong positive claim become trusted?
Did ambiguous/no-claim text safely abstain?
```

Report both.

Do not use the safety metric to hide diagnostic semantic misses.

## 9. Define repeatability at the domain level

Free-text explanations can vary even when the material result is identical.

Repeat signatures should compare things such as:

```text
candidate identities
result state
trusted result kind/state
trusted domain identity
```

not byte-identical explanatory prose unless exact prose is itself part of the contract.

## 10. Replay before rerunning when possible

If raw model outputs are preserved, an offline replay can isolate changes to:

```text
adapter mapping
contract interpretation
validation
scoring
```

without introducing new inference variation.

This is especially useful when diagnosing whether a failure belongs to the model or to the surrounding representation.

## 11. Retries change the system being evaluated

A first-pass model evaluation answers:

```text
How does this deployment behave on one attempt?
```

A validator-feedback retry loop answers:

```text
How does model + correction mechanism behave?
```

Both can be useful, but they are different systems and must be evaluated separately.

Do not enable automatic retries merely to improve a benchmark score.

## 12. Frameworks are not semantic fixes

Instructor, Pydantic, SDKs, and agent frameworks can improve ergonomics, validation, and retries. They do not automatically improve the model's understanding of negation, tense, direction, or ambiguity.

Introduce a framework only when it solves an identified engineering responsibility better than the simpler baseline.

## 13. Local inference still has deployment boundaries

A local model server introduces ordinary distributed-system concerns:

```text
process environment
proxy variables
HTTP transport
timeouts
model identity
chat template
context/token limits
resource availability
```

"Local" does not mean "not a network/service boundary."

## 14. Preserve experimental identity

A model evaluation is only interpretable when the deployment identity is stable enough to reproduce:

```text
provider/server
model identifier
prompt/contract version
temperature
seed
retry policy
token budget
relevant template/runtime behavior
```

Changing any of these can require re-evaluation.

## 15. Bounded input is part of the evaluated contract

A model that succeeds on a bounded release section is not automatically proven on an entire long changelog.

Runtime integration needs a deterministic method for creating bounded semantic windows from trusted source structure.

That windowing layer should preserve source identity and coverage without pre-solving the semantic question assigned to the model.

## Compact mental model

```text
Authority first.
Bound the text.
Let the model select meaning.
Derive what can be derived.
Recover exact evidence deterministically.
Validate before trust.
Abstain on uncertainty.
Score semantics and safety separately.
Preserve raw evidence for replay.
Re-evaluate whenever the deployment contract changes.
```
