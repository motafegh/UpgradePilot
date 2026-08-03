# ADR-0006 — Bounded Local Support-Drop Semantic Extractor

**Status:** Accepted  
**Date:** 2026-08-03  
**Owning responsibility:** B2 target-Python support relevance, upstream semantic candidate extraction  
**Evidence:** Step 6 frozen corpus, live contract-v2 evaluation, deterministic adoption assessment

## Context

UpgradePilot needs one narrow semantic capability after authoritative upstream interval evidence is established:

```text
admitted authoritative upstream text
→ identify explicit CURRENT Python X.Y support-drop claim(s)
→ untrusted structured candidate(s)
→ deterministic Step 2 validation
→ grounded support-drop claim or explicit problem
```

The deterministic validator already owns package/version identity, source authority, exact quote/span grounding, allowed category/direction, normalized Python line, interval membership, and multiple-claim handling. Natural-language direction and meaning remain the missing responsibility.

Earlier deterministic phrase/regex ideas were not selected as the product semantic architecture because support-drop meaning has equivalent wording, negation, future tense, continued-support statements, raised-minimum wording, and nearby instruction-shaped text. Earlier small-model deployments also produced false support-drop claims and were rejected.

Step 6 therefore evaluated a bounded local LLM deployment behind the existing deterministic trust boundary.

## Decision

Adopt the following method **only for the bounded Python support-drop extraction role**:

```text
runtime/provider: LM Studio local HTTP service
model: gemma-4-e4b-it-ud
model-facing contract: Step 6 contract v2
HTTP client: existing requests dependency
first-pass temperature: 0
seed: 0
automatic retries: disabled
structured generation: strict JSON Schema
source authority: deterministic; never model-selected
exact quote/span reconstruction: deterministic
trust admission: validate_support_drop_candidates(...) is mandatory
```

### Contract v2

The model does not predict a redundant top-level `candidates_available` state. It returns:

```text
candidates[]
  python_line
  introduced_in_version
  source_line_id

unresolved_if_no_candidates: bool
detail: string
```

The adapter derives the existing domain result state:

```text
non-empty candidates
→ candidates_available

empty candidates + unresolved_if_no_candidates=true
→ unresolved

empty candidates + false
→ no_relevant_claim
```

Trusted/fixed fields remain deterministic:

```text
package identity
old/proposed dependency versions
category = support_boundary_change
change_state = support_dropped
source authority/source kind
exact source text
quote_start / quote_end
```

A model-selected line ID is resolved back to exact authoritative source bytes before the candidate reaches Step 2.

## Scope boundary

This ADR does **not** authorize the model to perform:

- source discovery or source-authority selection;
- arbitrary documentation search;
- dependency identity or version ordering;
- target Python acquisition or `requires-python` interpretation;
- target-range comparison;
- general release-note summarization;
- compatibility or safety claims;
- merge/defer/recommendation decisions;
- target-repository mutation;
- agent/tool calling.

A schema-valid model response remains untrusted until deterministic validation admits it.

## Evidence supporting the decision

### Contract-v1 live evaluation

The first 25-call scored run completed all calls but passed only 14/25. Seven failures were not semantic candidate-selection failures: the model selected the correct candidate while redundantly emitting `state="unresolved"`. Four remaining failures were zero-candidate `no_relevant_claim` versus frozen-oracle `unresolved` disagreements.

### Contract-v2 counterfactual replay

Replaying the exact same 25 historical structured outputs while deriving candidate availability mechanically produced:

```text
21 / 25 strict passes
7 historical failures rescued
4 remaining zero-candidate state mismatches
0 new model calls
```

This isolated duplicated state encoding as a contract-design defect.

### Contract-v2 live evaluation

A new 25-call live run using the actual v2 schema produced:

```text
strict oracle: 24 / 25
adoption safety: 25 / 25
```

The single strict miss classified ambiguous wording as `no_relevant_claim` instead of `unresolved`. Both outcomes contained zero candidates and both stop downstream target-Python activation.

Critical controls produced no false current support-drop admission:

```text
support-added: abstained
negated drop: abstained
future drop: abstained
raised-minimum-only: abstained
S001: grounded Python 3.8 @ release 2.8
```

### Material repeatability

The first live-v2 scorer incorrectly treated different free-text unresolved explanations as inconsistent. A deterministic post-run assessment compared material candidate/trust identities instead of prose and established material consistency across all repeated critical cases.

### Final adoption gate

The deterministic assessment reported all ten Step 6 adoption-gate checks true, including exact positive grounding, no wrong-direction admissions, no inferred unstated Python line, correct S001 behavior, safe abstention, material repeatability, recorded latency, improvement over rejected baselines, and explicit deployment identity.

Observed latency over 25 live calls:

```text
mean:   8.852445 s
median: 8.414366 s
min:    5.355407 s
max:   12.549101 s
```

This is accepted for the current read-only single-dependency investigation slice, not as a universal latency target.

## Why direct HTTP remains selected

`requests` is already a runtime dependency and LM Studio exposes the required OpenAI-compatible structured-output endpoint. Direct HTTP keeps the request/response boundary visible and adds no new framework dependency.

Instructor/Pydantic were considered but are not required for the adopted baseline. In particular, automatic validator-driven retries during Step 6 would have changed the experiment from measuring first-pass model behavior into measuring model-plus-correction-loop behavior.

Instructor may be reconsidered later only if it materially improves runtime contract maintenance or diagnostics without weakening observability or trust boundaries.

## Alternatives considered

### Deterministic phrase/regex extractor

Rejected as the selected semantic method. It risks growing fixture-shaped phrase tables and handling paraphrase, negation, tense, and ambiguous wording poorly.

### Contract-v1 model output

Rejected. `state` plus `candidates` encoded the same fact twice and created avoidable incoherent outputs.

### Automatic retries

Not selected for the baseline. Retries can hide first-pass semantic/representation failures and add latency and changed evidence semantics. A retry experiment requires a separate explicit evaluation.

### Instructor/Pydantic

Deferred. They are adapter choices, not semantic authority, and the current baseline already has strict JSON Schema plus deterministic domain validation.

### Another local model before adoption

Not required by current evidence. Existing candidate models remain available for reassessment if the selected deployment regresses, becomes unavailable, or fails broader future evidence.

### Cloud fallback

Not selected. The current slice is intentionally local and no cloud semantic provider is authorized by this decision.

## Operational constraints

Normal project control remains WSL-first:

```text
UpgradePilot WSL process
→ localhost HTTP
→ LM Studio on Windows host
```

Loopback HTTP must bypass inherited external proxy variables at the process boundary. Global proxy configuration must not be disabled merely to reach LM Studio.

The model/template identity used for validation must remain reproducible. LM Studio emitted a compatibility warning that the loaded Gemma 4 model used an outdated chat template and that LM Studio applied compatibility workarounds. This warning did not break the validated runs, but changing the template is a deployment change and requires re-evaluation rather than silent substitution.

## Source-windowing constraint before normal runtime activation

Step 6 validated bounded release-text inputs, including the exact S001 release section. The real tagged changelog is materially larger.

Therefore normal runtime must **not** simply send an entire authoritative changelog to the model and call that equivalent evidence. The integration step must define and test a deterministic bounded source-windowing method tied to trusted crossed-release structure before model invocation. Source-windowing may reduce text but may not assign support-drop semantics or silently omit relevant crossed releases.

This is a Step 7 integration obligation, not a reason to reopen Step 6 model selection.

## Security and trust consequences

- upstream text and model output are untrusted data;
- no model tool execution is allowed;
- source authority remains deterministic;
- exact source reconstruction and Step 2 validation remain mandatory;
- malformed, unsupported, ambiguous, or ungroundable outcomes stop rather than guess;
- no target repository is mutated.

## Reassessment triggers

Re-run the frozen corpus and adoption assessment before retaining this decision if any of the following materially change:

- model identifier or quantization/deployment identity;
- LM Studio structured-output behavior;
- Gemma chat template;
- model-facing contract or prompt semantics;
- automatic retry policy;
- provider/client framework;
- admitted source-windowing semantics;
- a false positive or wrong-direction claim appears in real use;
- deterministic Step 2 grounding contract changes;
- latency/resource behavior becomes unacceptable for the selected product slice.

## Consequences

### Positive

- fills the bounded natural-language gap with measured evidence;
- preserves deterministic authority and grounding;
- avoids a new runtime dependency;
- keeps failure and abstention visible;
- supports S001 without package-specific semantic hardcoding.

### Costs and limitations

- requires a local LM Studio service and the selected model deployment;
- adds approximately several seconds of inference latency per extraction under the measured environment;
- one frozen ambiguous case remains a strict diagnostic miss despite safe abstention;
- runtime source-windowing still requires integration proof;
- this decision does not establish general semantic-model reliability.

## Reversal

The model/provider adapter is deliberately outside the trusted domain contracts. UpgradePilot can replace or remove it while preserving `CandidateUpstreamClaimResult`, `validate_support_drop_candidates(...)`, and downstream target-relevance contracts, provided the replacement passes the same or stronger evidence gate.
