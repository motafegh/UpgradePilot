# UpgradePilot Current Memory

**Last updated:** 2026-08-03  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, selected continuation, and current learning state.

Stable plans, specifications, ADRs, source, tests, environment reference, and dated working records retain their own responsibilities. They must not mirror or compete with this file for live status.

## Single-live-state rule

`MEMORY.md` is replacement state, not append-only history. It alone answers what is selected now, what behavior is verified, what remains open, what happens next, and what learning depth is established.

## Live position

- **Execution branch:** `main`. No separate implementation branch is selected.
- **Route:** B2 — Public PR vertical slice.
- **Selected parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Behavior-validated:** parent-plan Steps 1–5 and Step 6A.
- **Selected focused Step 6 plan:** [`plans/B2_STEP_6_SUPPORT_DROP_EXTRACTION_EVALUATION_PLAN.md`](plans/B2_STEP_6_SUPPORT_DROP_EXTRACTION_EVALUATION_PLAN.md)
- **Current parent responsibility:** Step 6 — evaluate the candidate extraction/model path only where semantic interpretation is needed.
- **Environment owner:** [`ENVIRONMENT.md`](ENVIRONMENT.md).
- **Step 6B disposition:** existing project evidence already establishes the reusable LM Studio/WSL2/GPU/model baseline; Ali explicitly directed assistants to reuse it instead of asking for another full environment recapture.
- **Current increment:** Step 6C — smallest direct-HTTP/JSON-Schema support-drop extraction smoke using the established local inference baseline, before any model/adapter adoption.
- **Step 6A validation record:** [`working-memory/2026-08-03_B2-step-6a-support-drop-corpus-validation.md`](working-memory/2026-08-03_B2-step-6a-support-drop-corpus-validation.md)

## Last behavior-validated executable boundary

Step 6A corpus/test behavior is validated through:

```text
41b74eda85bbf554b746eac30e6c1a6ca39ddceb
```

The user reported that both requested validation runs passed completely.

The exact focused/full counts and timings were not supplied in that message and are not invented.

## Step 5 closure remains established

Step 5 is fully closed with deterministic and live S001 public-source evidence.

Observed live source facts remain:

```text
package: soupsieve
interval: 2.6 → 2.8.4
crossed releases: 2.7, 2.8, 2.8.1, 2.8.2, 2.8.3, 2.8.4
ignored non-PEP-440 keys: none

tag ref: refs/tags/2.8.4
direct tag object: commit 28108ab805818c832d9568142a99844fd95a0d39
resolved commit: 28108ab805818c832d9568142a99844fd95a0d39
peel depth: 0

changelog path: docs/src/markdown/about/changelog.md
changelog blob SHA: 6f221b7398681a580fa199044b3d3f1e11b55493
reported bytes: 17370
decoded bytes: 17370

authority basis: tagged_changelog
GitHub Release bodies admitted: 0
```

This establishes authoritative upstream interval evidence only; semantic interpretation remains Step 6.

## Step 6 responsibility

The active semantic path is intentionally narrow:

```text
AuthoritativeUpstreamIntervalEvidence
→ untrusted semantic candidate extraction
→ CandidateUpstreamClaimResult
→ validate_support_drop_candidates(...)
→ GroundedPythonSupportDropClaim
   or explicit claim problem
```

Only this semantic form is in scope:

```text
category = support_boundary_change
change_state = support_dropped
python_line = explicit normalized X.Y
introduced_in_version = exact trusted crossed release
```

Do not reopen general release-note summarization or the older four-category semantic proposal during this slice.

## Step 6A closure

Frozen corpus:

```text
experiments/step6_support_drop_semantic_corpus.json
```

Deterministic oracle tests:

```text
tests/test_step6_support_drop_semantic_corpus.py
```

The 15-case corpus covers direct and paraphrased support drops, support added/continued controls, negation, future tense, ambiguity, raised-minimum-only ungroundable text, multiple distinct drops, unrelated fixes, inert instruction-shaped text, and the exact S001 excerpt.

Step 6A validation proves the oracle itself agrees with the already behavior-validated Step 2 trust boundary before any model is scored.

The important existing grounding invariant remains:

```text
accepted source quote must itself contain the claimed Python X.Y token
```

Therefore text that only raises a minimum version without explicitly naming the dropped line cannot become a trusted dropped-line claim under the current contract.

## Step 6B environment baseline — recovered, do not recapture by default

A new environment interrogation is not required merely because Step 6 reached the local-model boundary.

The repository already contains dated exact evidence establishing the reusable baseline, now consolidated in [`ENVIRONMENT.md`](ENVIRONMENT.md).

Material established facts include:

```text
Windows host + WSL2 development topology
UpgradePilot checkout: /home/motafeq/projects/UpgradePilot
Python 3.12.3
venv interpreter: /home/motafeq/projects/UpgradePilot/.venv/bin/python3

GPU: NVIDIA GeForce RTX 3070 Laptop GPU
nominal VRAM: 8192 MiB
last recorded driver: 610.74

LM Studio CLI identity: commit 71bd99c
server port: 12345
listener: 127.0.0.1
WSL2 → http://127.0.0.1:12345/v1/models: proven
native model endpoint: http://127.0.0.1:12345/api/v1/models

model inventory/quantizations: captured
known Gemma E4B 4096-context load: operationally proven
strict JSON-Schema route: operationally proven
```

The known Gemma E4B control used:

```text
model: gemma-4-e4b-it-ud
quantization: Q4_K_XL
context: 4096
parallel: 1
Flash Attention: true
KV cache: GPU
MTP speculative: false
simple speculative: false
```

That historical broader semantic smoke had a semantic-state inconsistency. It is therefore an operational control, not an adopted semantic model.

### Re-check rule

Do not ask Ali to repeat the full LM Studio/GPU/WSL2 inventory.

Use `ENVIRONMENT.md` first. Request a fresh observation only if:

- a task depends materially on an instantaneous value such as free VRAM or the currently loaded instance;
- an observed failure contradicts the baseline;
- Ali reports an environment/model change;
- or the selected proof explicitly requires a new reproducibility snapshot.

A new conversation is not evidence that the environment changed.

## Step 6 method constraints

Existing B2 evidence remains controlling:

- JSON Schema constrains output representation, not semantic truth;
- exact quote/span grounding does not prove correct interpretation;
- previous small local deployments produced material false support-drop claims;
- fixture-shaped regex/phrase repair is not accepted production semantics;
- manual structured claims remain test oracles, not automated extraction.

The current evaluation direction remains:

```text
bounded structured LLM extraction
→ deterministic Step 2 grounding/validation
```

but no model or adapter is adopted yet.

For the first Step 6C smoke, prefer direct HTTP through the already-installed `requests` dependency. Do not add OpenAI, Pydantic, Instructor, LangChain, or LM Studio SDK dependencies merely to perform the smoke.

## Exact continuation

Proceed to Step 6C without another full environment capture.

1. Inspect the Step 6 candidate-output contract and current Step 2 dataclasses/validator.
2. Build the smallest experiment-only direct-`requests` JSON-Schema smoke harness; do not modify normal CLI/runtime orchestration.
3. Reuse the established loopback endpoint `http://127.0.0.1:12345/v1/chat/completions`.
4. Prefer the already operationally proven `gemma-4-e4b-it-ud` 4096-context deployment as the first transport/schema control unless a concrete current failure proves it unavailable.
5. Feed only a narrow Step 6 support-drop case and map the untrusted response mechanically into `CandidateUpstreamClaimResult`.
6. Pass that candidate through `validate_support_drop_candidates(...)`; do not weaken deterministic validation to accommodate model output.
7. Preserve transport, schema, semantic, grounding, and trust-admission results as separate evidence.
8. Stop after the bounded smoke result is reviewed; do not jump directly to scored corpus/model adoption.

If the known loopback/model load unexpectedly fails, preserve the exact failure and then request only the smallest freshness-sensitive observation needed to diagnose it.

## Stop line

Until Step 6C smoke evidence is reviewed, do not begin:

- broad model scoring;
- adapter/product adoption;
- new semantic runtime dependencies;
- target-Python conditional activation;
- CLI orchestration changes;
- full S001 relevance execution;
- compatibility, safety, merge, defer, targeted-check, or recommendation logic.

## Explicitly not established

- a currently loaded LM Studio model at this exact moment;
- current instantaneous free VRAM at this exact moment;
- a selected/adopted semantic model;
- Step 6 narrow support-drop structured-output smoke success;
- an adopted support-drop extractor;
- automated grounded S001 Python 3.8 support-drop extraction;
- conditional target-Python activation in CLI runtime;
- S001 automated end-to-end relevance result;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery of Steps 1–6.

The first two are intentionally freshness-sensitive values. Their absence does not justify repeating the whole environment inventory.

## Learning state

Steps 1–5 and Step 6A are behavior-validated at product level. Step 6B reusable environment knowledge is established from prior exact project evidence and consolidated for future assistants.

Current Step 6 concepts exposed:

- **semantic oracle:** frozen expected meaning used to score an extractor;
- **candidate extraction:** untrusted semantic proposal from prose;
- **structured generation:** output-shape compliance only;
- **mechanical grounding:** exact quote/span exists in trusted source text;
- **semantic correctness:** whether the candidate accurately represents the source meaning;
- **trust admission:** deterministic Step 2 validation decides whether a candidate becomes domain evidence;
- **deployment boundary:** model server, model identity, transport, schema, semantics, and product adoption are separate concerns;
- **reusable baseline versus instantaneous state:** stable/last-observed environment facts can be reused while free memory/current load may require targeted freshness checks only when material.

Current depth:

```text
Steps 1–5 behavior validated
+ Step 6A corpus/oracle behavior validated
+ Step 6 environment/model baseline recovered and documented
+ historical operational Gemma E4B load/schema evidence available
but
no current narrow Step 6C smoke result
no model adoption evidence
no user-owned Step 6 end-to-end explanation recorded
no formal mastery assessment
not mastered
```

Product validation, environment knowledge, and learning mastery remain separate claims.

## State-maintenance rule

When route, selected responsibility, verified executable boundary, blocker, learning state, or exact continuation changes:

1. update `MEMORY.md` only for live state;
2. update `ENVIRONMENT.md` only when a reusable local environment baseline materially changes;
3. preserve freshness-sensitive one-run environment evidence in dated `working-memory/` records;
4. replace obsolete live statements instead of accumulating them;
5. change plans/specifications/ADRs only when their stable responsibility actually changes;
6. create dated working-memory only for material historical evidence or reasoning, never as another status owner;
7. keep navigation READMEs non-state-bearing.