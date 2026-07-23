# B1 Current Source and Test Reconciliation

**Status:** AI-authored implemented-truth reconciliation; Ali review pending  
**Date:** 2026-07-23  
**Stage:** B1 — Implementation responsibility freeze  
**Parent:** [`B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md`](B1_IMPLEMENTATION_RESPONSIBILITY_FREEZE_REQUIREMENTS.md)  
**Accepted evidence base:** [`D1_ACCEPTANCE_AND_B1_ACTIVATION.md`](D1_ACCEPTANCE_AND_B1_ACTIVATION.md)

## Purpose

Record what the current UpgradePilot implementation actually contains, how each part
relates to the accepted S001–S005 runtime, and which parts should be retained, corrected,
superseded, or treated as experimental evidence before the B2 responsibility is frozen.

This is a source-reconciliation record, not the B2 implementation plan and not an
architecture selection.

## Inspection method and limitation

Inspected through the GitHub connector at the current default-branch state:

- `pyproject.toml`;
- `docs/architecture/ADR-0001-initial-python-source-layout.md`;
- `src/upgradepilot/__init__.py`;
- `src/upgradepilot/case_identity.py`;
- `src/upgradepilot/evidence.py`;
- `src/upgradepilot/decision.py`;
- `src/upgradepilot/extraction.py`;
- `src/upgradepilot/extraction_validation.py`;
- `src/upgradepilot/llm_extractor.py`;
- `scripts/evaluate_python_support_models.py`;
- current tests for identity, evidence, decision, extraction validation, extraction
  orchestration, and the LM Studio boundary;
- source-bearing commits and the retained M2-S02 implementation/evaluation record.

A clean local clone and fresh test execution could not be performed because the local
execution environment could not resolve `github.com`. Historical working evidence says
50 tests and `compileall` passed after the M2-S02 repairs, but B1 does not treat that
historical result as a fresh current-head execution.

Therefore this record establishes connector-backed structural and behavioral inspection,
not clean-checkout reproducibility or current runtime execution proof.

## Current package shape

The accepted source boundary remains:

```text
pyproject.toml
src/upgradepilot/
    __init__.py
    case_identity.py
    evidence.py
    decision.py
    extraction.py
    extraction_validation.py
    llm_extractor.py
tests/
scripts/evaluate_python_support_models.py
```

Current package metadata:

- Python `>=3.12`;
- setuptools `src/` layout;
- Pydantic dependency;
- OpenAI client dependency;
- no declared command-line entry point;
- no public application API beyond importable modules;
- no persistence, service, queue, graph, or deployment dependency.

## Current executable flow

The implemented application path is currently narrower than the accepted D1 runtime:

```text
flat manual case mapping
→ validated InitialCaseRecord
→ manually constructed EvidenceSet
→ optional LM Studio Python-support candidate extraction
→ deterministic mechanical quote/version grounding
→ attributed model-derived Python-support claim
→ one bounded deterministic policy
→ run_targeted_checks or abstain
```

The code does not currently implement a complete run lifecycle, baseline/full comparison,
reports, operation history, conditional-stage state, follow-up transitions, review state,
or replay command.

## Component reconciliation

### `docs/architecture/ADR-0001-initial-python-source-layout.md`

**Classification:** retain unchanged.

Why:

- the `src/upgradepilot/` and `tests/` boundary is implemented and still adequate;
- the ADR deliberately avoids speculative subpackages;
- no current B1 evidence requires a package-boundary change.

Consequence:

- B2 should continue with cohesive modules in the existing package;
- create subpackages only if the frozen responsibility demonstrates a real cohesion or
  dependency boundary.

### `pyproject.toml`

**Classification:** retain with correction.

Reusable:

- professional `src/` package configuration;
- Python version boundary;
- Pydantic as the current validation mechanism.

Correction question for B1:

- the OpenAI client is required only by the experimental LM Studio path and should not be
  required by the replay-first B2 kernel unless a current packaging constraint proves
  otherwise.

No dependency change is authorized during B1. The B2 plan should decide whether the
OpenAI dependency remains ordinary, becomes optional/development-only, or is left
unchanged temporarily for the smallest safe transition.

### `src/upgradepilot/__init__.py`

**Classification:** retain unchanged.

It is a minimal package marker and exposes no speculative public API.

### `src/upgradepilot/case_identity.py`

**Classification:** retain with material correction.

Reusable behavior:

- strict Pydantic validation;
- exact repository/PR/base/head identity;
- normalized full SHAs;
- explicit dependency/version transition;
- changed-file validation;
- immutable trusted contracts;
- rejection of malformed, partial, duplicate, or equal-version input;
- deterministic JSON serialization.

Mismatch with D1/B2:

- the entry contract is named and documented as a provisional manual M2 input;
- invocation and discovered/frozen identity are collapsed;
- no run ID or record IDs exist;
- no source/provenance exists for how identity was obtained;
- dependency and changed-file shape assumes one selected dependency update;
- changed-boundary/new-run behavior is not represented;
- `InitialCaseRecord` is not a complete runtime aggregate.

B1 consequence:

- retain its validation principles and much of its value-object behavior;
- do not treat `ManualCaseInput` or `InitialCaseRecord` as the final B2 run contract;
- the B2 responsibility must separate replay invocation from accepted frozen identity and
  add stable run/record identity.

### `src/upgradepilot/evidence.py`

**Classification:** retain with material correction.

Reusable behavior:

- evidence has explicit identity;
- accepted evidence must contain an observation;
- missing evidence cannot invent an observation;
- missing evidence must state a limitation;
- evidence IDs are unique;
- evidence is associated with one exact case;
- immutable strict contracts prevent silent coercion.

Mismatch with D1/B2:

- evidence states are only `accepted` and `missing`;
- kinds are fixed to four M2 concerns;
- source is an unstructured string rather than a bounded provenance record;
- raw/reference evidence, acquisition attempt, retention, observation time, and producing
  operation are absent;
- inaccessible, expired, partial, invalid, conflicting, stale, failed-method, and
  superseded states are absent;
- observations, interpretations, and findings are not separate runtime records;
- evidence is embedded directly in `EvidenceSet` rather than participating in a complete
  run state and lineage graph.

B1 consequence:

- retain explicit state, limitation, strictness, immutability, and unique-ID principles;
- replace the narrow state/kind model with the smallest B2 representation that supports
  accepted, degraded, and changed evidence without copying the simulation schemas
  literally.

### `src/upgradepilot/decision.py` — contracts

**Classification:** retain with material correction.

Reusable behavior:

- deterministic policy version is explicit;
- decision reasons have codes, summaries, and evidence references;
- claim-to-evidence references are validated;
- claims cannot cite missing evidence;
- targeted checks and limitations are first-class output;
- abstention exists;
- result contracts are immutable and machine-readable;
- favorable model-derived claims cannot reduce caution.

Mismatch with D1/B2:

- only `run_targeted_checks` and `abstain` outcomes exist;
- only model-derived Python-support claims are admitted;
- claim, interpretation, and finding responsibilities are collapsed;
- no transparent baseline result distinct from the bounded full decision exists;
- no `merge_after_normal_review` or block/investigate outcome exists;
- no conditional-stage activation/non-activation state exists;
- no follow-up, rerun, supersession, or changed-boundary transition exists;
- no machine/human report projection exists;
- the input consumes a narrow evidence set rather than accepted run state.

B1 consequence:

- retain traceable reasons, limitations, policy versioning, abstention, and defensive
  authority controls;
- redesign the decision boundary around accepted findings/run state rather than one
  Python-support claim tuple.

### `src/upgradepilot/decision.py` — `evaluate_decision` M2 rule

**Classification:** experimental evidence only; do not use as the B2 product boundary.

The rule demonstrates a useful deterministic pattern:

```text
model-grounded Python-support drop
+ missing repository support
→ run targeted checks
```

But it is one obsolete M2 responsibility, not the S001–S005 transparent baseline or the
minimum full decision runtime. It may later become one conditional B4 rule after target
context is implemented and evaluated.

### `src/upgradepilot/extraction.py`

**Classification:** experimental evidence only for later semantic automation.

Reusable lessons:

- untrusted candidate output is separate from grounded output;
- provider behavior is behind a small protocol;
- model authority survives conversion into a decision claim;
- unresolved and validation-error states are visible;
- orchestration does not let the model choose the final decision.

Why it is outside B2:

- B2 begins from replay fixtures and does not require live semantic extraction;
- the current responsibility covers only Python-support claims in release notes;
- automatic semantic correctness is not established;
- prepared replay interpretations are permitted when labeled honestly.

### `src/upgradepilot/extraction_validation.py`

**Classification:** experimental evidence with reusable deterministic patterns.

Reusable patterns:

- accepted-source eligibility check;
- exact source-quote grounding;
- version-in-quote grounding;
- duplicate rejection;
- bounded validator claims and explicit non-claims.

Important limitation:

- the validator proves mechanical grounding, not semantic correctness;
- it intentionally accepts an instruction-shaped or semantically wrong claim when the
  literal quote and version are present;
- contradictory source claims are preserved rather than resolved.

B1 consequence:

- preserve the lesson that deterministic validation must state exactly what it proves;
- do not include Python-support extraction in the B2 kernel merely because its validator
  is deterministic.

### `src/upgradepilot/llm_extractor.py`

**Classification:** experimental evidence only; defer from B2.

Useful evidence:

- direct provider boundary without an orchestration framework;
- explicit model/base URL/timeout/token/seed configuration;
- schema-constrained output;
- malformed and empty output failures;
- bounded diagnostics;
- untrusted source content is wrapped as data;
- model identity is preserved.

Blocking limitations:

- no production model was accepted;
- observed small models produced unsafe false positives;
- local LM Studio availability is environment-specific;
- the dependency and runtime path are unnecessary for replay-first B2;
- semantic and prompt-injection reliability remain unproven.

### `scripts/evaluate_python_support_models.py`

**Classification:** retain as experimental evaluation evidence; not product runtime.

It demonstrates:

- repeated case evaluation;
- candidate, grounding, decision-effect, latency, token, and failure measurements;
- adversarial/instruction-shaped cases;
- model metadata capture;
- explicit distinction between expected semantic output and downstream decision effect.

It should not become the B2 command or the primary application interface.

## Test reconciliation

### Identity tests

**Classification:** retain with correction as B2 test seeds.

Strong coverage exists for strict types, normalization, frozen values, malformed identity,
duplicate paths, changed-file ordering, equal versions, JSON serialization, and
non-mutation of raw input.

Missing B2 coverage:

- invocation versus frozen identity;
- run and record IDs;
- changed identity creates a new run;
- provenance and operation association;
- multiple replay cases rather than one Pydantic example.

### Evidence tests

**Classification:** retain with correction as B2 test seeds.

Strong coverage exists for accepted versus missing evidence, limitations, unique IDs,
immutability, case association, and serialization.

Missing B2 coverage:

- inaccessible, expired, partial, conflicting, invalid, failed-method, and superseded
  evidence;
- raw/reference provenance;
- producing operation and lineage references;
- interpretation/finding separation;
- evidence changes and supersession.

### Decision tests

**Classification:** retain selected invariants; supersede M2 policy expectations.

Reusable tests cover evidence-reference validation, immutable contracts, reason codes,
limitations, targeted checks, abstention, and inability of favorable model claims to
reduce caution.

M2-specific expectations such as `m2-v0.1`, model-derived-only authority, and the single
Python-support-drop rule must not define B2 acceptance.

### Extraction and LM Studio tests

**Classification:** retain under experimental scope; not B2 acceptance tests.

They are useful proof for provider boundaries, untrusted output, mechanical grounding,
diagnostics, failure handling, and semantic-evaluation design. They do not prove the
accepted D1 runtime or a production semantic method.

## Missing B2 runtime responsibilities

No current source component owns the complete responsibility for:

- replay invocation;
- stable run identity;
- append-oriented operation history;
- rich evidence state and provenance;
- explicit observation, interpretation, and finding records;
- transparent baseline as a comparator;
- conditional-stage activation and non-activation;
- same-action, action-change, early-stop, and degraded-evidence flow;
- bounded full decision across the accepted action set;
- machine and human reports from the same accepted state;
- follow-up, rerun, supersession, and changed-boundary transitions;
- review, assistance, and ownership state;
- whole-run identity and lineage validation;
- a clean replay command or bounded application interface.

These are not reasons to discard the current implementation. They define the gap the B2
responsibility must cover.

## Initial reconciliation summary

| Component | Classification | B1 consequence |
|---|---|---|
| ADR-0001 source layout | Retain unchanged | Keep current flat package boundary |
| `pyproject.toml` | Retain with correction | Reassess OpenAI as non-core dependency during B2 planning |
| `__init__.py` | Retain unchanged | No public API commitment |
| `case_identity.py` | Retain with material correction | Reuse strict values; add invocation/run/boundary separation |
| `evidence.py` | Retain with material correction | Expand states/provenance/lineage minimally |
| decision contracts | Retain with material correction | Reuse traceability/abstention; redesign full boundary |
| M2 `evaluate_decision` rule | Experimental evidence only | Possible later conditional rule, not B2 boundary |
| extraction contracts/service | Experimental evidence only | Prepared replay interpretations in B2; automate later |
| extraction validator | Experimental with reusable patterns | Reuse bounded-validation doctrine, not the specific task |
| LM Studio client | Experimental evidence only | Exclude from B2 core |
| model evaluator script | Experimental evaluation evidence | Preserve for later X1/B4 work |
| identity/evidence tests | Retain with correction | Seed B2 invariants and negative tests |
| decision tests | Partially retain | Keep invariants; replace M2 policy expectations |
| extraction/LLM tests | Experimental scope | Exclude from B2 acceptance gate |

## Preliminary minimum-direction conclusion

The current implementation should be evolved, not deleted and not continued unchanged.

B2 should reuse:

- the accepted `src/` package boundary;
- strict immutable typed contracts;
- exact case identity validation;
- explicit evidence states and limitations;
- unique IDs and validated references;
- deterministic policy versioning;
- traceable reasons, checks, limitations, and abstention;
- defensive separation of untrusted data from trusted runtime state.

B2 should not inherit as its central boundary:

- the flat `ManualCaseInput`;
- `InitialCaseRecord` as the complete run;
- the two-state/four-kind evidence model;
- model-derived Python-support claims as the only interpretation form;
- the single M2 decision rule;
- live LM Studio extraction;
- the model evaluator script;
- the simulation JSON file layout copied verbatim.

## Next B1 action

Using this reconciliation and S001–S005, freeze the candidate minimum executable
responsibility and the prepared-input versus deterministic-runtime boundary.

Before the B2 plan is created, Ali should be able to explain:

1. why `case_identity.py` is reusable but not a complete run model;
2. why `evidence.py` has the right principle but insufficient states and provenance;
3. why the decision contracts are more reusable than the current decision rule;
4. why the LLM extraction path is valuable evidence but outside B2;
5. why no source should be deleted merely because the old M2 route was superseded.
