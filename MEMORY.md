# UpgradePilot Current Memory

**Last updated:** 2026-08-03  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, selected continuation, and current learning state.

Stable plans, specifications, ADRs, source, tests, [`ENVIRONMENT.md`](ENVIRONMENT.md), and dated working records retain their own responsibilities. They must not mirror or compete with this file for live status.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Selected parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Selected Step 6 plan:** [`plans/B2_STEP_6_SUPPORT_DROP_EXTRACTION_EVALUATION_PLAN.md`](plans/B2_STEP_6_SUPPORT_DROP_EXTRACTION_EVALUATION_PLAN.md)
- **Behavior-validated:** parent Steps 1–5, Step 6A, and the original Step 6C deterministic harness boundary.
- **Current increment:** Step 6C — obtain the first real WSL→LM Studio support-drop extraction smoke result.
- **Current blocker:** the first live smoke was intercepted by Privoxy before LM Studio.
- **Environment model:** WSL2 is the UpgradePilot control plane; LM Studio runs as a localhost service on the Windows host.
- **Failure record:** [`working-memory/2026-08-03_B2-step-6c-privoxy-transport-failure.md`](working-memory/2026-08-03_B2-step-6c-privoxy-transport-failure.md)

## Last behavior-validated executable boundary

Ali reported:

```text
Ran 318 tests in 0.060s

OK
```

That validates the original Step 6C deterministic harness/test boundary through:

```text
3ff0677bf8da9688e1bb1dc80681b5ec593cef5f
```

The later localhost proxy-isolation runner and its tests are not yet user-validated.

## Closed upstream authority boundary

Step 5 remains fully closed with deterministic and live S001 evidence:

```text
soupsieve 2.6 → 2.8.4
crossed releases: 2.7, 2.8, 2.8.1, 2.8.2, 2.8.3, 2.8.4
resolved tag commit: 28108ab805818c832d9568142a99844fd95a0d39
changelog: docs/src/markdown/about/changelog.md
blob: 6f221b7398681a580fa199044b3d3f1e11b55493
reported/decoded bytes: 17370 / 17370
authority basis: tagged_changelog
GitHub Release bodies admitted: 0
```

Step 5 establishes source authority, not semantic meaning.

## Step 6 responsibility

The semantic path remains intentionally narrow:

```text
AuthoritativeUpstreamIntervalEvidence
→ untrusted candidate extraction
→ CandidateUpstreamClaimResult
→ validate_support_drop_candidates(...)
→ GroundedPythonSupportDropClaim
   or explicit claim problem
```

Only this semantic form is in scope:

```text
category = support_boundary_change
change_state = support_dropped
python_line = explicit X.Y
introduced_in_version = exact trusted crossed release
```

The Step 2 grounding rule still requires the accepted exact quote to contain the claimed Python `X.Y` token. Raised-minimum-only prose cannot silently become a grounded dropped-line claim.

## Step 6A frozen oracle

Frozen corpus:

```text
experiments/step6_support_drop_semantic_corpus.json
```

The 15 cases cover positive drops, paraphrases, support-added/continued controls, negation, future tense, ambiguity, raised-minimum-only abstention, multiple drops, unrelated fixes, instruction-shaped text, and the exact S001 excerpt.

This is the semantic oracle used to judge model meaning separately from schema and grounding.

## Step 6B reusable environment baseline

Read [`ENVIRONMENT.md`](ENVIRONMENT.md) before asking Ali for environment information.

Reusable baseline:

```text
control plane: WSL2
checkout: /home/motafeq/projects/UpgradePilot
Python: 3.12.3
venv: /home/motafeq/projects/UpgradePilot/.venv/bin/python3
GPU: NVIDIA GeForce RTX 3070 Laptop GPU, 8192 MiB nominal VRAM
LM Studio host process: Windows
LM Studio loopback port: 12345
WSL → http://127.0.0.1:12345/v1/models: historically proven
JIT model loading: historically established
model inventory/quantizations: captured
```

Known operational control:

```text
gemma-4-e4b-it-ud
Q4_K_XL
historically proven at 4096 context
strict JSON-Schema route operationally proven
```

Historical PowerShell commands are provenance, not the default workflow. Use WSL Git/Python/tests/curl/requests/`nvidia-smi` unless a demonstrated host-only need exists.

## Step 6C implemented boundary

Experiment harness:

```text
experiments/step6_support_drop_smoke.py
```

Deterministic harness tests:

```text
tests/test_step6_support_drop_smoke_harness.py
```

The smoke isolates:

```text
frozen exact S001 excerpt
→ WSL requests
→ LM Studio
→ strict JSON-Schema response
→ mechanical candidate mapping
→ semantic oracle
→ Step 2 grounding/trust admission
```

No OpenAI SDK, Pydantic, Instructor, LangChain, LM Studio SDK, CLI orchestration, or product semantic adapter was added.

### First live attempt — observed

Ali ran:

```bash
python experiments/step6_support_drop_smoke.py
```

Observed result:

```text
STEP 6C SMOKE: FAIL
stage error: HTTPError: 500 Server Error: Internal Privoxy Error for url: http://127.0.0.1:12345/v1/models
```

Classification:

```text
WSL Python requests
→ intended localhost LM Studio URL
→ inherited proxy behavior / Privoxy
→ HTTP 500
```

This run did **not** establish a result about:

- LM Studio availability;
- `gemma-4-e4b-it-ud` loading;
- `/v1/chat/completions`;
- JSON Schema;
- semantic correctness;
- grounding;
- Step 2 trust admission.

The exact proxy environment variable(s) responsible were not inspected and are not invented.

## Bounded proxy-isolation correction awaiting validation

Added:

```text
tools/run_step6c_support_drop_smoke.py
tests/test_step6c_local_http_runner.py
```

Candidate executable boundary:

```text
f10699aeed496ea09777157070be3b8a55c1db7b
```

The runner changes only the child smoke process environment:

- removes HTTP/HTTPS/ALL proxy variables and lowercase equivalents;
- sets `NO_PROXY` and `no_proxy` to `127.0.0.1,localhost,::1`;
- executes the existing experiment with the active WSL Python interpreter.

It does not change Ali's shell, system proxy configuration, LM Studio configuration, or production source.

## Exact continuation

From the UpgradePilot WSL virtual environment:

```bash
git pull --ff-only

python -m unittest tests.test_step6c_local_http_runner -v
python -m unittest discover -s tests -v

python tools/run_step6c_support_drop_smoke.py
```

Return the complete output of the final smoke runner.

If it still fails before LM Studio, remain inside Step 6C transport diagnosis. Do not begin Step 6D.

If it reaches LM Studio, classify transport, structured generation, semantic oracle, grounding/trust admission, finish reason, latency, and token usage separately.

## Step 6 method constraints

- JSON Schema constrains representation, not semantic truth.
- Exact quote/span grounding does not prove correct interpretation.
- Previous small local deployments produced material false support-drop claims.
- Fixture-shaped regex/phrase repair is not accepted production semantics.
- Manual structured claims remain test oracles, not automated extraction.
- `validate_support_drop_candidates(...)` must not be weakened to accommodate model mistakes.
- First-pass semantic evaluation uses no automatic retries.

No model or adapter is adopted yet.

## Stop line

Until Step 6C reaches an evidence-backed live result, do not begin:

- Step 6D broad model scoring;
- model/adapter product adoption;
- new semantic runtime dependencies;
- target-Python conditional activation;
- CLI orchestration changes;
- full S001 relevance execution;
- compatibility, safety, merge, defer, targeted-check, or recommendation logic.

## Explicitly not established

- a successful current WSL→LM Studio Step 6C request;
- a selected/adopted semantic model;
- a successful narrow support-drop structured-output smoke;
- an adopted support-drop extractor;
- automated live S001 Python 3.8 semantic extraction;
- conditional target-Python activation;
- S001 automated end-to-end relevance;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery of Steps 1–6.

## Learning state

Current Step 6 concepts exposed:

- **semantic oracle** — frozen expected meaning;
- **candidate extraction** — untrusted semantic proposal;
- **structured generation** — output-shape compliance;
- **mechanical grounding** — exact quote/span exists;
- **semantic correctness** — candidate accurately represents source meaning;
- **trust admission** — deterministic validator decides whether candidate becomes evidence;
- **proxy inheritance** — HTTP libraries can inherit shell proxy configuration and redirect intended localhost traffic unless loopback is explicitly excluded.

Current depth:

```text
Steps 1–5 behavior validated
+ Step 6A oracle behavior validated
+ original Step 6C deterministic harness validated
+ first live Step 6C transport failure diagnosed
but
proxy-isolation correction not yet user-validated
no successful live Step 6C semantic result
no model adoption evidence
no formal mastery assessment
not mastered
```

Product validation, environment knowledge, model semantic evidence, and learning mastery remain separate claims.

## State-maintenance rule

When route, selected responsibility, verified executable boundary, blocker, learning state, or exact continuation changes:

1. update `MEMORY.md` only for live state;
2. update `ENVIRONMENT.md` only for reusable environment baseline/rule changes;
3. use dated `working-memory/` for material historical evidence;
4. preserve failures and unknowns rather than inferring success.