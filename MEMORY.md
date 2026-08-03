# UpgradePilot Current Memory

**Last updated:** 2026-08-03  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, selected continuation, and current learning state.

Stable plans, specifications, ADRs, source, tests, [`ENVIRONMENT.md`](ENVIRONMENT.md), and dated working records retain their own responsibilities. They must not mirror or compete with this file for live status.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Selected parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Selected Step 6 plan:** [`plans/B2_STEP_6_SUPPORT_DROP_EXTRACTION_EVALUATION_PLAN.md`](plans/B2_STEP_6_SUPPORT_DROP_EXTRACTION_EVALUATION_PLAN.md)
- **Behavior-validated:** parent-plan Steps 1–5 and Step 6A.
- **Step 6B:** reusable local inference environment baseline recovered and documented; do not repeat full environment capture.
- **Environment operating model:** WSL2 is the UpgradePilot control plane; LM Studio runs as a localhost service on the Windows host.
- **Current increment:** Step 6C — WSL-side direct-HTTP/JSON-Schema support-drop extraction smoke.
- **Current Step 6C state:** experiment harness and deterministic harness tests implemented; local deterministic validation and one live LM Studio smoke are required before review/adoption work.
- **Step 6C implementation record:** [`working-memory/2026-08-03_B2-step-6c-support-drop-smoke-implementation.md`](working-memory/2026-08-03_B2-step-6c-support-drop-smoke-implementation.md)

## Last behavior-validated executable boundary

Step 6A corpus/oracle behavior is validated through:

```text
41b74eda85bbf554b746eac30e6c1a6ca39ddceb
```

Ali reported that both requested Step 6A validation runs passed. Exact counts/timings were not supplied and are not invented.

Step 6C is **not** behavior-validated yet.

## Closed upstream authority boundary

Step 5 remains fully closed with deterministic and live S001 public-source evidence.

The live S001 authority established:

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

The current semantic path remains intentionally narrow:

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

The existing Step 2 grounding rule still requires the accepted exact source quote itself to contain the claimed Python `X.Y` token. Raised-minimum-only prose cannot silently become a grounded dropped-line claim.

## Step 6A frozen oracle

Frozen corpus:

```text
experiments/step6_support_drop_semantic_corpus.json
```

The 15 cases include positive drops, paraphrases, support-added/continued controls, negation, future tense, ambiguity, raised-minimum-only abstention, multiple dropped lines, unrelated fixes, instruction-shaped text, and the exact S001 excerpt.

This corpus is the semantic oracle used to judge model meaning separately from schema and grounding.

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
WSL → http://127.0.0.1:12345/v1/models: proven
JIT model loading: established active
model inventory/quantizations: captured
```

Known operational control:

```text
gemma-4-e4b-it-ud
Q4_K_XL
historically proven at 4096 context
strict JSON-Schema route operationally proven
```

Historical PowerShell `lms` commands are provenance, not the default workflow. Use WSL Git/Python/tests/curl/requests/`nvidia-smi`; use Windows-side tooling only for a demonstrated host-only need.

## Step 6C implemented boundary awaiting validation

New experiment harness:

```text
experiments/step6_support_drop_smoke.py
```

Harness implementation commit:

```text
2e839a2cd429349777991073ddb6b4af8592b018
```

New deterministic harness tests:

```text
tests/test_step6_support_drop_smoke_harness.py
```

Test implementation commit:

```text
3ff0677bf8da9688e1bb1dc80681b5ec593cef5f
```

The harness uses only the already-installed `requests` dependency. No OpenAI, Pydantic, Instructor, LangChain, or LM Studio SDK dependency was added.

### Smoke flow

```text
frozen exact S001 excerpt
+ frozen trusted interval context
→ WSL requests
→ http://127.0.0.1:12345/v1/chat/completions
→ gemma-4-e4b-it-ud
→ strict JSON-Schema response
→ mechanical candidate mapping
→ deterministic unique quote offsets
→ CandidateUpstreamClaimResult
→ validate_support_drop_candidates(...)
```

The smoke deliberately uses the Step 6A frozen exact S001 excerpt instead of reacquiring PyPI/GitHub. This isolates model/semantic failure from external-source acquisition failure and does not claim a new live Step 5 proof.

Default evidence output is outside the repository:

```text
/tmp/upgradepilot-step6c-support-drop-smoke.json
```

### Critical architectural test

The deterministic harness tests explicitly prove:

```text
exact quote/span grounding
!=
correct natural-language interpretation
```

For example, the frozen source contains an **add support for Python 3.14** statement. If a model incorrectly labels that exact quote as `support_dropped`, mechanical Step 2 grounding can still find the exact quote and Python token. The semantic oracle must catch the wrong direction.

Therefore Step 6 must preserve separate layers:

```text
transport
→ structured generation
→ semantic correctness
→ mechanical grounding
→ trust admission
→ product adoption
```

## Exact continuation

From the UpgradePilot WSL checkout:

```bash
git pull --ff-only

python -m unittest tests.test_step6_support_drop_smoke_harness -v
python -m unittest discover -s tests -v
```

If both deterministic runs pass, run the live local-model smoke:

```bash
python experiments/step6_support_drop_smoke.py
```

The runner should be allowed to fail honestly. Preserve the complete terminal output.

It will separately report:

```text
transport/model inventory
completion HTTP
structured candidate mapping
semantic oracle
Step 2 trust admission
finish reason / usage
overall Step 6C smoke result
```

No expected deterministic test count or live result is asserted before Ali supplies observed output.

## After the Step 6C result

If the smoke passes:

1. record the exact model/response/latency/trust evidence;
2. close Step 6C only as a one-case transport/schema/semantic smoke;
3. activate Step 6D frozen 15-case semantic scoring and critical repetitions;
4. do **not** adopt the model from one passing case.

If the smoke fails:

- diagnose only the demonstrated layer: transport, HTTP/schema, mapping, semantic meaning, grounding, or trust admission;
- do not change several model/prompt/runtime variables at once;
- do not weaken `validate_support_drop_candidates(...)` to force success.

## Stop line

Until Step 6C evidence is reviewed, do not begin:

- full model scoring;
- model/adapter product adoption;
- new semantic runtime dependencies;
- target-Python conditional activation;
- CLI orchestration changes;
- full S001 relevance execution;
- compatibility, safety, merge, defer, targeted-check, or recommendation logic.

## Explicitly not established

- passing Step 6C deterministic harness tests;
- passing Step 6C live LM Studio smoke;
- a selected/adopted semantic model;
- an adopted support-drop extractor;
- automated live S001 Python 3.8 semantic extraction;
- conditional target-Python activation in CLI runtime;
- S001 automated end-to-end relevance result;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery of Steps 1–6.

## Learning state

Current depth:

```text
Steps 1–5 behavior validated
+ Step 6A oracle behavior validated
+ Step 6 environment/model baseline documented
+ WSL-first control boundary established
+ Step 6C model/schema/trust data flow exposed in code/tests
but
Step 6C local execution not yet observed
no model adoption evidence
no user-owned Step 6 end-to-end explanation recorded
no formal mastery assessment
not mastered
```

Product behavior validation, environment knowledge, model semantic evidence, and learning mastery remain separate claims.

## State-maintenance rule

When route, selected responsibility, verified executable boundary, blocker, learning state, or exact continuation changes:

1. update `MEMORY.md` only for live state;
2. update `ENVIRONMENT.md` only for reusable environment baseline/rule changes;
3. use dated `working-memory/` for material historical evidence;
4. do not duplicate live status into plans/specifications/ADRs;
5. preserve failures and unknowns rather than inferring success.
