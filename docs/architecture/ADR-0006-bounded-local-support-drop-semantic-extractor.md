# ADR-0006 — Bounded Local Support-Drop Semantic Extractor

**Status:** Accepted  
**Date:** 2026-08-03  
**Owning responsibility:** Target-Python support relevance, bounded upstream semantic candidate extraction  
**Evidence:** Step 6 frozen corpus, contract-v2 live evaluation, deterministic adoption assessment

## Context

After authoritative crossed-release source evidence is established, UpgradePilot needs one narrow natural-language capability:

```text
admitted authoritative upstream text
→ identify explicit current Python X.Y support-drop candidate(s)
→ untrusted structured candidate(s)
→ deterministic source reconstruction and validation
→ grounded support-drop claim or explicit problem
```

Deterministic code already owns source authority, package/version identity, exact grounding, allowed category/direction, normalized Python line, interval membership, and permitted downstream effect. Natural-language direction/meaning is the missing responsibility.

Phrase/regex approaches were not selected as product semantic architecture because the responsibility must handle paraphrase, negation, future tense, continued-support wording, raised-minimum wording, and misleading instruction-shaped text without growing a fixture-shaped interpreter.

## Decision

Adopt the following method **only for this bounded semantic role**:

```text
provider/runtime: LM Studio localhost HTTP
model: gemma-4-e4b-it-ud
model-facing contract: contract v2
HTTP client: existing requests dependency
temperature: 0
seed: 0
automatic retries: disabled
structured generation: strict JSON Schema
source authority: deterministic
exact source reconstruction: deterministic
trust admission: validate_support_drop_candidates(...) mandatory
```

### Model-facing contract

The model returns only semantic candidate data needed for the bounded responsibility:

```text
candidates[]
  python_line
  introduced_in_version
  source_line_id

unresolved_if_no_candidates: bool
detail: string
```

The adapter derives candidate-availability state mechanically:

```text
non-empty candidates → candidates_available
empty + unresolved flag → unresolved
empty + no unresolved flag → no_relevant_claim
```

Trusted/fixed values—including package/version identity, category, change direction, source authority, exact source text, and exact offsets—remain deterministic rather than model-selected.

A model-selected source line is resolved back to exact authoritative source bytes before candidate validation.

## Scope boundary

This ADR does **not** authorize the model to perform:

- source discovery or source-authority selection;
- arbitrary documentation search;
- dependency identity/version ordering;
- target Python acquisition or `requires-python` interpretation;
- target-range comparison;
- general release-note summarization;
- compatibility or safety claims;
- recommendation/merge/defer policy;
- external mutation;
- tool/agent execution.

Schema-valid model output remains untrusted until deterministic validation admits it.

## Adoption evidence summary

The decision was made from a frozen scored evaluation rather than model preference.

The important adoption evidence was:

```text
contract-v2 live strict oracle: 24 / 25
adoption safety: 25 / 25
material critical repeats consistent: true
all defined adoption-gate checks: true
```

The one strict miss produced a safe zero-candidate disagreement (`no_relevant_claim` versus `unresolved`) rather than a false support-drop admission.

Critical controls produced no admitted false current support-drop claim, while the positive proof case grounded the expected Python support drop.

Detailed case-by-case outputs, latency statistics, contract-v1 failure analysis, counterfactual replay, and evaluation machinery remain in the Step 6 evidence/experiment records rather than being reproduced as architecture.

## Why direct HTTP remains selected

`requests` was already a runtime dependency and LM Studio exposed the required structured-output endpoint. Direct HTTP keeps provider requests/responses visible and avoids adding an adapter framework merely for schema handling.

Instructor/Pydantic are not rejected, but they were unnecessary for the accepted baseline. Automatic validator-driven retries were also excluded because they would change the measured responsibility from first-pass extraction into a model-plus-correction-loop system.

## Runtime source-window requirement

Step 6 evaluated bounded source text. Normal runtime must therefore not send an arbitrary entire changelog and call it equivalent evidence.

Before model invocation, deterministic product code must construct a complete bounded source window tied to trusted crossed-release structure. Windowing may reduce text structurally but may not assign support-drop semantics or silently omit a required crossed release.

The detailed construction/proof of that bridge belongs to the selected Step 7 integration plan, not this ADR.

## Security and transport boundary

Normal control remains:

```text
UpgradePilot in WSL
→ loopback HTTP
→ LM Studio on Windows host
```

External source text and model output are untrusted data. No model tools/external actions are allowed. Local transport must not silently broaden provider exposure or turn source text into remote disclosure.

Provider errors, malformed structured output, ambiguous meaning, failed grounding, or unsupported candidates must stop/degrade explicitly rather than becoming a positive claim.

Reusable environment/deployment facts belong to `../../ENVIRONMENT.md`; stable credential/privacy/external-action rules belong to `../../SECURITY.md`.

## Alternatives considered

### Deterministic phrase/regex product extractor

Rejected as the selected semantic architecture because it creates a phrase-enumeration/generalization cliff for the owning natural-language responsibility. It may remain a disposable baseline/oracle where useful.

### Contract v1

Rejected because candidate presence and a separately model-predicted state redundantly encoded the same fact and produced avoidable incoherence.

### Automatic retries

Not selected for the baseline because retries change evidence semantics, hide first-pass failures, and add latency. A retry/correction loop requires separate evaluation.

### Instructor/Pydantic adapter

Deferred. They may be reconsidered only if they materially improve runtime contract maintenance/diagnostics without weakening observability or trust boundaries.

### Additional model or cloud fallback before adoption

Not required by the evidence supporting this bounded role. A replacement or fallback requires a new comparative/evidence gate.

## Consequences

### Benefits

- fills one measured natural-language gap;
- deterministic code retains authority and grounding;
- no new runtime framework dependency;
- failure/abstention remains visible;
- the known positive case can be supported without package-specific semantic hardcoding.

### Costs and limitations

- requires a local LM Studio deployment and selected model identity;
- adds local inference latency/resource use;
- semantic reliability is established only for the bounded evaluated role;
- source-window integration must remain behavior-valid;
- provider/model/template/deployment drift can invalidate the evidence basis.

## Reversal

The provider/model adapter remains outside trusted domain contracts. It may be replaced or removed while preserving candidate/trust boundaries if a replacement passes the same or stronger evidence gate.

## Reassessment triggers

Re-evaluate before retaining this decision when any of these materially change:

- model identifier, quantization, or deployment identity;
- LM Studio structured-output behavior;
- model chat template;
- model-facing contract or prompt semantics;
- retry/correction policy;
- provider/client framework;
- admitted source-windowing semantics;
- deterministic grounding contract;
- a false positive/wrong-direction real-use claim;
- latency/resource behavior becoming unacceptable for the owning slice.

## Proof boundary

The Step 6 evidence and selected Step 7 plan/tests own detailed proof. Product acceptance must continue to demonstrate bounded candidate generation, deterministic exact-source recovery, mandatory validation, safe abstention on negative/ambiguous controls, reproducible deployment identity, and no model ownership of authority or downstream decision policy.

Acceptance of this ADR authorizes one bounded method. It does not establish general model trust, product correctness, or learner mastery.
