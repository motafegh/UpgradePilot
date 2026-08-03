# B2 Step 6C — Support-Drop Smoke Implementation

**Date:** 2026-08-03  
**Parent:** [`../plans/B2_STEP_6_SUPPORT_DROP_EXTRACTION_EVALUATION_PLAN.md`](../plans/B2_STEP_6_SUPPORT_DROP_EXTRACTION_EVALUATION_PLAN.md)  
**Result classification:** Experiment harness implemented; deterministic and live execution still required; no model or adapter adopted

## Implemented boundary

Added:

```text
experiments/step6_support_drop_smoke.py
tests/test_step6_support_drop_smoke_harness.py
```

Executable commits:

```text
harness: 2e839a2cd429349777991073ddb6b4af8592b018
tests:   3ff0677bf8da9688e1bb1dc80681b5ec593cef5f
```

No normal product runtime source, CLI orchestration, target-Python logic, or dependency set changed.

## Smoke data flow

```text
frozen Step 6A s001_exact_excerpt
+ trusted dependency/crossed-release context
→ WSL requests
→ http://127.0.0.1:12345/v1/chat/completions
→ gemma-4-e4b-it-ud
→ strict JSON-Schema structured content
→ mechanical candidate mapping
→ unique exact quote-offset derivation
→ CandidateUpstreamClaimResult
→ validate_support_drop_candidates(...)
→ grounded claim or explicit Step 2 problem
```

The smoke uses the frozen exact S001 excerpt rather than reacquiring PyPI/GitHub sources. This deliberately isolates the model/semantic boundary from external acquisition failures. It does not claim a new live Step 5 proof.

## Model-facing responsibility

The model may propose only:

```text
candidate state
trusted-context echoes
support_boundary_change
support_dropped
Python X.Y
introduced crossed release
source kind = tagged_changelog
exact source quote
optional unresolved detail
```

The adapter deterministically derives quote offsets only when the proposed quote occurs exactly once in the admitted source text. It does not ask the model to count character offsets.

No retries are enabled.

## Why semantic oracle and grounding are separate

A deliberate deterministic test proves the important boundary:

```text
source contains: Add support for Python 3.14.
model incorrectly labels it: support_dropped
```

The quote can still be mechanically exact and contain the Python line, so Step 2 quote/span grounding alone can admit the candidate structure. The frozen semantic oracle must therefore separately detect the wrong direction.

This is expected architecture, not a test bug:

```text
JSON/schema correctness
!= semantic correctness

exact quote grounding
!= correct natural-language interpretation
```

The Step 6 adoption gate exists precisely because a model is responsible for the semantic interpretation that deterministic Step 2 does not perform.

## Controlled authority fixture

For the smoke only, the harness wraps the frozen exact S001 excerpt in controlled `AuthoritativeUpstreamIntervalEvidence` / `TaggedChangelogEvidence` records. Synthetic commit/blob identities are used deliberately so the fixture cannot be mistaken for a new live acquisition record.

The real Step 5 S001 authority remains separately behavior-validated.

## Runtime configuration

Defaults:

```text
control plane: WSL
base URL: http://127.0.0.1:12345
model: gemma-4-e4b-it-ud
timeout: 180 seconds
model-list timeout: 15 seconds
temperature: 0
seed: 0
max output tokens: 512
streaming: false
automatic retries: false
```

Optional environment overrides:

```text
UPGRADEPILOT_LM_STUDIO_BASE_URL
UPGRADEPILOT_LM_STUDIO_MODEL
UPGRADEPILOT_STEP6C_OUTPUT
```

Default evidence output is outside the repository:

```text
/tmp/upgradepilot-step6c-support-drop-smoke.json
```

This avoids creating uncommitted repository evidence before the run has been reviewed.

## Validation still required

First deterministic harness tests:

```bash
python -m unittest tests.test_step6_support_drop_smoke_harness -v
```

Then complete deterministic suite as required by the project validation cadence:

```bash
python -m unittest discover -s tests -v
```

Only after those pass, run the live local-model smoke:

```bash
python experiments/step6_support_drop_smoke.py
```

No pass counts, timings, model output, or live success are claimed until Ali supplies observed terminal output.

## Stop line

Do not move from this record directly into:

- full 15-case model scoring;
- Qwen/Gemma comparison;
- model or adapter adoption;
- new runtime dependencies;
- CLI orchestration;
- target-Python relevance execution;
- compatibility, safety, or maintainer-action logic.

Review the Step 6C deterministic and live smoke evidence first.
