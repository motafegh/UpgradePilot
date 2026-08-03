# UpgradePilot Current Memory

**Last updated:** 2026-08-03  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, selected continuation, and current learning state.

Stable plans/specifications/ADRs/source/tests, [`ENVIRONMENT.md`](ENVIRONMENT.md), and dated `working-memory/` records keep their own responsibilities. They must not compete with this file for live status.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Active Step 6 plan:** [`plans/B2_STEP_6_SUPPORT_DROP_EXTRACTION_EVALUATION_PLAN.md`](plans/B2_STEP_6_SUPPORT_DROP_EXTRACTION_EVALUATION_PLAN.md)
- **Behavior-validated product boundary:** parent Steps 1–5 and Step 6A; Step 6C one-case local-model path also passed live.
- **Step 6D v1:** completed 25-call Gemma evaluation; exact JSON evidence committed.
- **Step 6D contract v2:** deterministic adapter validated; offline replay completed; live v2 scorer/runner now implemented and awaiting user deterministic validation + live run.
- **No semantic model/adapter is adopted yet.**

## Last exact user-reported deterministic validation

Ali reported after the contract-v2 implementation:

```text
Ran 332 tests in 0.059s

OK
```

Do not invent a later count before the next run.

## Closed Step 5 authority boundary

S001 upstream authority remains established:

```text
soupsieve 2.6 → 2.8.4
crossed releases: 2.7, 2.8, 2.8.1, 2.8.2, 2.8.3, 2.8.4
resolved tag commit: 28108ab805818c832d9568142a99844fd95a0d39
changelog: docs/src/markdown/about/changelog.md
blob: 6f221b7398681a580fa199044b3d3f1e11b55493
authority basis: tagged_changelog
```

Step 5 establishes exact authority, not natural-language meaning.

## Step 6 semantic path

```text
AuthoritativeUpstreamIntervalEvidence
→ untrusted semantic selection
→ deterministic candidate construction
→ CandidateUpstreamClaimResult
→ validate_support_drop_candidates(...)
→ GroundedPythonSupportDropClaim
   or UpstreamSupportDropClaimProblem
```

Only this positive semantic form is in scope:

```text
category = support_boundary_change
change_state = support_dropped
python_line = explicit X.Y
introduced_in_version = exact trusted crossed release
```

The model does not own package identity, source authority, category/direction constants, exact quote reproduction, or quote offsets.

## Step 6A frozen oracle

Corpus:

```text
experiments/step6_support_drop_semantic_corpus.json
```

Fifteen cases cover direct/paraphrased drops, support-added/continued controls, negation, future tense, raised-minimum-only wording, ambiguity, irrelevant text, multiple drops, noisy/instruction-shaped text, and exact S001.

The frozen exact-state oracle is preserved. It is not rewritten after seeing model results.

## Environment boundary

UpgradePilot control plane is WSL2; LM Studio runs on Windows and is consumed over localhost HTTP.

```text
WSL Python/tests/tools
→ localhost HTTP
→ LM Studio
```

Loopback endpoint:

```text
http://127.0.0.1:12345
```

The validated runners remove inherited HTTP/HTTPS/ALL proxy variables only for their child process and set:

```text
NO_PROXY=127.0.0.1,localhost,::1
```

Do not switch normal project work to PowerShell.

## Step 6C closed — one-case live smoke

Record:

[`working-memory/2026-08-03_B2-step-6c-live-s001-validation.md`](working-memory/2026-08-03_B2-step-6c-live-s001-validation.md)

Observed S001 result:

```text
transport/model inventory: PASS
completion HTTP: PASS
structured candidate mapping: PASS
semantic oracle: PASS
Step 2 trust admission: PASS
finish reason: stop
STEP 6C SMOKE: PASS
```

Gemma selected Python 3.8 / release 2.8 / source line L3 and ignored the Python 3.14 support addition. Exact source quote/offsets were reconstructed deterministically.

LM Studio logged an outdated-Gemma4-template compatibility warning. Preserve that deployment caveat during comparison; do not silently change model/template mid-evaluation.

## Step 6D v1 — completed live evaluation

Durable evidence:

```text
working-memory/evidence/2026-08-03-step6d/support-drop-evaluation.json
```

Evidence commit reported by Ali:

```text
a4b2e37
```

Observed v1 summary:

```text
25 / 25 runs completed
14 passed
11 failed
all critical repeats consistent
```

Seven failures were candidate-bearing state contradictions: the model selected the correct candidate but separately emitted `state=unresolved`. Four failures were zero-candidate `no_relevant_claim` vs frozen-oracle `unresolved` disagreements.

## Contract v2 — validated offline replay

Contract v2 removes redundant positive-state prediction.

Model-facing selection:

```text
candidates: [...]
unresolved_if_no_candidates: bool
detail: string
```

Adapter derives:

```text
non-empty candidates
→ candidates_available

empty + unresolved_if_no_candidates=true
→ unresolved

empty + false
→ no_relevant_claim
```

Artifacts:

```text
experiments/step6_support_drop_contract_v2.py
experiments/step6_support_drop_contract_v2_replay.py
tests/test_step6_support_drop_contract_v2.py
```

Replay record:

[`working-memory/2026-08-03_B2-step-6d-contract-v2-offline-replay-result.md`](working-memory/2026-08-03_B2-step-6d-contract-v2-offline-replay-result.md)

Ali successfully ran:

```bash
python -m experiments.step6_support_drop_contract_v2_replay
```

Observed replay summary:

```text
historical runs: 25
historical passed: 14
contract-v2 replay passed: 21
contract-v2 replay failed: 4
historical failures rescued: 7
remaining failure class: zero_candidate_state_mismatch = 4
all critical repeats consistent: true
new model calls: 0
```

Thus 7/11 v1 failures were representation/contract failures, not failures to select the support-drop candidate.

Remaining strict mismatches:

```text
raised_minimum_without_explicit_dropped_line r1/r2/r3
ambiguous_support_wording r1
```

All produced zero candidates but chose `no_relevant_claim` where the strict frozen oracle expects `unresolved`.

## Why the remaining 4 require two scores

The deterministic Step 2 contract preserves a diagnostic difference:

```text
no_relevant_claim → no_support_drop_claim
unresolved        → candidate_unresolved
```

But current target-Python relevance collapses **any** `UpstreamSupportDropClaimProblem` to:

```text
upstream_claim_unresolved
→ target-Python comparison not activated
```

Therefore the remaining four are genuine strict semantic-classification errors, but they are not currently unsafe admissions of a support-drop claim.

Do not erase this distinction. Use two metrics:

1. **strict oracle score** — exact frozen state/candidate/trust expectation;
2. **adoption-safety score** — exact positive/multiple-claim behavior plus safe zero-candidate abstention (`no_support_drop_claim` or `candidate_unresolved`).

A false positive, wrong positive candidate, wrong release/source, or grounded claim on a zero-candidate oracle case must fail both the relevant strict and safety gates.

## Current increment — live contract-v2 evaluation

New artifacts:

```text
experiments/step6_support_drop_contract_v2_live_evaluation.py
tools/run_step6d_contract_v2_evaluation.py
tests/test_step6_support_drop_contract_v2_live_evaluation.py
```

The live v2 evaluator keeps:

```text
model: gemma-4-e4b-it-ud
temperature: 0
seed: 0
automatic retries: false
same frozen 15 cases
same 25-run schedule
same Step 2 validator
```

It reports strict-oracle and adoption-safety scores separately.

Unlike earlier `/tmp` outputs, its default evidence path is durable in the checkout:

```text
working-memory/evidence/2026-08-03-step6d/contract-v2-live-evaluation.json
```

Running it will intentionally create/modify that evidence file; commit it after review even when semantic failures are recorded.

## Exact continuation

From the WSL checkout:

```bash
git pull --ff-only

python -m unittest tests.test_step6_support_drop_contract_v2_live_evaluation -v
python -m unittest discover -s tests -v
```

If deterministic tests pass, run:

```bash
python tools/run_step6d_contract_v2_evaluation.py
```

Allow the full 25-case schedule to complete unless transport/server failure stops it.

Return the complete final summary, especially:

```text
strict_oracle_passed
strict_oracle_failed
adoption_safety_passed
adoption_safety_failed
critical repeat consistency
```

Do not add Instructor or retries during this first-pass v2 score.

## Adoption gate remains closed

Possible Step 6 dispositions remain:

```text
adopt_bounded_extractor
retain_experiment_only
reject_candidate_deployment
defer_semantic_automation
reconsider_extraction_method
```

Only `adopt_bounded_extractor` authorizes normal-runtime integration. A durable provider/model/client dependency may require an ADR before activation.

## Stop line

Do not begin normal-runtime semantic integration, Instructor/Pydantic dependency work, retry/correction loops, target-Python conditional activation, CLI orchestration changes, full S001 product execution, or compatibility/safety/recommendation logic until the live contract-v2 evidence is reviewed and Step 6 receives an explicit disposition.

## Learning state

Current exposure includes semantic oracle vs adoption gate, structured generation, deterministic exact-source grounding, redundant-output design, counterfactual replay, strict-vs-safety scoring, and downstream abstention semantics.

Current depth:

```text
Steps 1–5 behavior validated
+ Step 6A oracle validated
+ Step 6C one-case live path validated
+ Step 6D v1 live evidence completed/preserved
+ contract-v2 offline replay completed (21/25 strict)
+ v1 contract artifacts separated from genuine semantic mismatches
but
live contract-v2 evaluation not yet observed
no model adoption disposition
no formal mastery assessment
not mastered
```
