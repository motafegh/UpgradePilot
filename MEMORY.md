# UpgradePilot Current Memory

**Last updated:** 2026-08-03  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, selected continuation, and current learning state.

Stable plans, specifications, ADRs, source, tests, [`ENVIRONMENT.md`](ENVIRONMENT.md), and dated working records retain their own responsibilities. They must not mirror or compete with this file for live status.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Selected parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Selected Step 6 plan:** [`plans/B2_STEP_6_SUPPORT_DROP_EXTRACTION_EVALUATION_PLAN.md`](plans/B2_STEP_6_SUPPORT_DROP_EXTRACTION_EVALUATION_PLAN.md)
- **Behavior-validated:** parent Steps 1–5, Step 6A, and the Step 6C proxy-isolation boundary that produced the 320-test complete-suite pass.
- **Current increment:** Step 6C — validate and rerun the redesigned one-case semantic-selection smoke.
- **Environment model:** WSL2 is the UpgradePilot control plane; LM Studio runs as a localhost service on the Windows host.
- **Current Step 6C state:** WSL→LM Studio transport and completion are now observed working; the first model response failed deterministic candidate mapping, which exposed a model-facing contract design problem rather than a transport problem.
- **Latest Step 6C evidence record:** [`working-memory/2026-08-03_B2-step-6c-first-model-response-and-grounding-redesign.md`](working-memory/2026-08-03_B2-step-6c-first-model-response-and-grounding-redesign.md)

## Last user-validated deterministic boundary

Ali reported:

```text
Ran 320 tests in 0.057s

OK
```

That result validates the repository state including the localhost proxy-isolation runner/tests before the later semantic-selection redesign.

The redesigned harness boundaries:

```text
6a69ffcb3f8fe05445ff0ab8acff9a2a71839875

d6af31ef01cc30040127f4fca384161e5a8cc8be
```

are **not behavior-validated yet**. Do not invent a passing count for them.

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
JIT model loading: historically established
model inventory/quantizations: captured
```

Known operational control:

```text
gemma-4-e4b-it-ud
Q4_K_XL
historically proven at 4096 context
```

Historical PowerShell commands are provenance, not the default workflow. Use WSL Git/Python/tests/curl/requests/`nvidia-smi` unless a demonstrated host-only need exists.

## Step 6C transport status

The original direct experiment inherited WSL proxy behavior and failed through Privoxy before LM Studio.

A bounded child-process proxy-isolation runner was then added:

```text
tools/run_step6c_support_drop_smoke.py
```

It removes inherited HTTP/HTTPS/ALL proxy variables only for the child smoke process and sets:

```text
NO_PROXY=127.0.0.1,localhost,::1
```

Ali's later live run established:

```text
transport/model inventory: PASS
completion HTTP: PASS (17.139s)
```

Therefore the Privoxy blocker is closed for this bounded runner and WSL→LM Studio transport is now observed working in the current Step 6C path.

## First real Step 6C model response — observed failure

The first real Gemma response reached LM Studio and returned structured JSON-shaped content, but failed before `CandidateUpstreamClaimResult` construction.

Observed response fields included:

```text
state: unresolved
candidate python_line: Python 3.8
introduced_in_version: 2.8
source_quote: - **NEW**: Drop support for Python 3.8.
```

The exact frozen source line is:

```text
-   **NEW**: Drop support for Python 3.8.
```

The harness correctly failed:

```text
Candidate 0 source_quote occurred 0 times; a unique exact span is required before offsets can be derived.
```

No exact-source rule was weakened.

Three distinct defects were observed:

1. model normalized Markdown whitespace instead of reproducing the exact line;
2. model returned `Python 3.8` instead of canonical `3.8`;
3. model returned `state=unresolved` while also returning a candidate.

The response also ended with:

```text
finish_reason: length
prompt_tokens: 441
completion_tokens: 512
reasoning_tokens: 333
total_tokens: 953
```

so the original 512-token output budget was a demonstrated confound.

## Step 6C model-facing contract redesign

The first response exposed a responsibility mistake:

```text
semantic extraction
!=
exact whitespace reproduction
```

The redesigned harness asks the model only for semantic selections:

```text
state
candidates[]:
  python_line
  introduced_in_version
  source_line_id
detail
```

The adapter deterministically supplies or derives:

```text
package / normalized package / old / proposed identity
category = support_boundary_change
change_state = support_dropped
source_kind = tagged_changelog
exact source_quote from source_line_id
quote_start
quote_end
```

The source is rendered with deterministic IDs such as:

```text
L3 | -   **NEW**: Drop support for Python 3.8.
```

The model therefore selects `L3`; it no longer has to reproduce exact Markdown whitespace.

This is not fuzzy grounding. The adapter recovers the exact original source line and character offsets.

### Canonical Python token bounding

The adapter deterministically gathers explicit `Python X.Y` tokens from the source without interpreting direction.

For the S001 excerpt:

```text
3.8
3.14
```

The model-facing schema allows only those explicit source tokens, preventing forms such as `Python 3.8` while leaving the semantic choice—drop versus add—to the model.

### Candidate-state coherence

The adapter now rejects:

```text
state != candidates_available
+
non-empty candidates
```

before Step 2 admission.

### Output budget

The next one-case smoke uses:

```text
max_tokens = 1024
```

Automatic retries remain disabled. The increase exists only to remove the demonstrated `finish_reason=length` confound.

## Exact continuation

Remain in Step 6C.

From the UpgradePilot WSL virtual environment:

```bash
git pull --ff-only

python -m unittest tests.test_step6_support_drop_smoke_harness -v
python -m unittest tests.test_step6c_local_http_runner -v
python -m unittest discover -s tests -v
```

If those deterministic runs pass, rerun exactly one live smoke:

```bash
python tools/run_step6c_support_drop_smoke.py
```

Return the complete runner output.

The redesigned runner now prints the structured model content before deterministic mapping, so a later mapping failure remains directly observable without relying on LM Studio desktop logs.

Do not begin Step 6D until this redesigned one-case smoke is reviewed.

## Step 6 method constraints

- JSON Schema constrains representation, not semantic truth.
- Exact quote/span grounding does not prove correct interpretation.
- Exact source reproduction is a deterministic adapter responsibility when a stable source locator can be selected instead.
- Previous small local deployments produced material false support-drop claims.
- Fixture-shaped semantic phrase repair is not accepted production semantics.
- Deterministic source-token and source-line bounding may constrain representation without deciding semantic direction.
- `validate_support_drop_candidates(...)` must not be weakened to accommodate model mistakes.
- First-pass semantic evaluation uses no automatic retries.

No model or adapter is adopted yet.

## Stop line

Until the redesigned Step 6C smoke reaches an evidence-backed result, do not begin:

- Step 6D broad model scoring;
- model/adapter product adoption;
- new semantic runtime dependencies;
- target-Python conditional activation;
- CLI orchestration changes;
- full S001 relevance execution;
- compatibility, safety, merge, defer, targeted-check, or recommendation logic.

## Explicitly not established

- behavior validation of the redesigned Step 6C harness;
- a passing redesigned Step 6C live result;
- a selected/adopted semantic model;
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
- **mechanical grounding** — exact source line/span exists;
- **semantic correctness** — candidate accurately represents source meaning;
- **trust admission** — deterministic validator decides whether candidate becomes evidence;
- **source locator** — deterministic identifier such as `L3` used to recover exact source text without asking the model to reproduce formatting;
- **representation bounding** — restrict model outputs to explicit source tokens/IDs without deciding their semantic meaning;
- **proxy inheritance** — HTTP libraries can inherit shell proxy configuration and redirect localhost traffic unless bounded execution isolates it.

Current depth:

```text
Steps 1–5 behavior validated
+ Step 6A oracle behavior validated
+ proxy-isolation boundary validated through complete 320-test run
+ WSL→LM Studio transport/completion observed working
+ first real Gemma candidate failure understood
+ Step 6C semantic-selection / deterministic-grounding redesign implemented
but
redesigned harness not yet user-validated
no passing Step 6C semantic result
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