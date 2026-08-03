# UpgradePilot Current Memory

**Last updated:** 2026-08-03  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, selected continuation, and current learning state.

Stable plans/specifications/ADRs/source/tests, [`ENVIRONMENT.md`](ENVIRONMENT.md), and dated `working-memory/` records retain their own responsibilities.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Active Step 6 plan:** [`plans/B2_STEP_6_SUPPORT_DROP_EXTRACTION_EVALUATION_PLAN.md`](plans/B2_STEP_6_SUPPORT_DROP_EXTRACTION_EVALUATION_PLAN.md)
- **Behavior-validated product boundary:** parent Steps 1–5 and Step 6A; Step 6C one-case local-model path passed live.
- **Step 6D v1:** completed 25-call Gemma evaluation; exact evidence committed.
- **Step 6D contract v2:** deterministic adapter validated, offline replay completed, live 25-call evaluation completed and evidence committed.
- **Current increment:** deterministic material-repeat/adoption-gate assessment of the committed live-v2 evidence. No new model calls are needed.
- **No normal-runtime semantic model/adapter is integrated yet.**

## Last exact user-reported deterministic validation

Ali reported:

```text
Ran 336 tests in 0.059s

OK
```

This validates the contract-v2 live evaluator/test boundary that produced the current evidence. The newer deterministic adoption-assessment files still require user validation.

## Step 5 authority boundary

S001 upstream authority remains established:

```text
soupsieve 2.6 → 2.8.4
crossed releases: 2.7, 2.8, 2.8.1, 2.8.2, 2.8.3, 2.8.4
resolved tag commit: 28108ab805818c832d9568142a99844fd95a0d39
changelog: docs/src/markdown/about/changelog.md
blob: 6f221b7398681a580fa199044b3d3f1e11b55493
authority basis: tagged_changelog
```

Step 5 establishes source authority, not semantic meaning.

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

Only this positive meaning is in scope:

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

The 15 cases cover direct/paraphrased drops, raised-minimum controls, support-added/continued controls, negation, future tense, ambiguity, irrelevant text, multiple drops, noisy/instruction-shaped text, and exact S001.

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

Validated runners remove inherited HTTP/HTTPS/ALL proxy variables only for their child process and set:

```text
NO_PROXY=127.0.0.1,localhost,::1
```

LM Studio has emitted an outdated-Gemma4-template compatibility warning. Preserve that deployment caveat; do not silently change template/model while interpreting current evidence.

## Step 6C closed — one-case live smoke

Record:

[`working-memory/2026-08-03_B2-step-6c-live-s001-validation.md`](working-memory/2026-08-03_B2-step-6c-live-s001-validation.md)

S001 passed transport, structured mapping, semantic oracle, deterministic Step 2 grounding, and non-truncated completion. Gemma selected Python 3.8 / release 2.8 / source line L3 and ignored the Python 3.14 support addition.

Step 6C proved one case only and never justified adoption by itself.

## Step 6D v1 — completed live evaluation

Durable evidence:

```text
working-memory/evidence/2026-08-03-step6d/support-drop-evaluation.json
```

Evidence commit reported by Ali:

```text
a4b2e37
```

Observed v1 result:

```text
25 / 25 runs completed
14 passed
11 failed
```

Seven failures were redundant candidate/state contradictions. Four were zero-candidate `no_relevant_claim` vs frozen-oracle `unresolved` disagreements.

## Contract v2 — offline replay

Model-facing shape:

```text
candidates: [...]
unresolved_if_no_candidates: bool
detail: string
```

Adapter derives:

```text
non-empty candidates → candidates_available
empty + unresolved flag → unresolved
empty + clear flag → no_relevant_claim
```

Offline replay of the exact v1 outputs produced:

```text
historical passed: 14 / 25
contract-v2 replay passed: 21 / 25
historical failures rescued: 7
remaining failures: 4 zero-candidate state mismatches
new model calls: 0
```

Thus 7/11 v1 failures were representation/contract failures rather than candidate-selection failures.

## Contract v2 — completed live evaluation

Record:

[`working-memory/2026-08-03_B2-step-6d-contract-v2-live-result.md`](working-memory/2026-08-03_B2-step-6d-contract-v2-live-result.md)

Durable evidence:

```text
working-memory/evidence/2026-08-03-step6d/contract-v2-replay.json
working-memory/evidence/2026-08-03-step6d/contract-v2-live-evaluation.json
```

Evidence commit reported by Ali:

```text
d19f5da
```

Observed live-v2 summary:

```text
completed: true
runs_completed: 25
runs_planned: 25
strict_oracle_passed: 24
strict_oracle_failed: 1
adoption_safety_passed: 25
adoption_safety_failed: 0
strict_all_runs_pass: false
adoption_safety_all_runs_pass: true
```

The only strict failure was:

```text
ambiguous_support_wording
actual: no_relevant_claim
oracle: unresolved
```

It remained a safe abstention: zero candidates and `no_support_drop_claim` from Step 2.

The raised-minimum-only control returned `unresolved` in all three live-v2 trials. S001 returned the correct grounded 3.8 / 2.8 claim in all three trials. Added/negated/future controls abstained in all repeated trials.

## Repeat-consistency metric issue

The live-v2 evaluator marked the raised-minimum repeat inconsistent even though every run had the same material outcome:

```text
candidate state = unresolved
candidate count = 0
trust kind = problem
trust state = candidate_unresolved
adoption safety = pass
```

Only free-text `detail` wording differed.

The Step 6 plan requires **materially consistent trusted outcomes**, not byte-identical prose. Therefore the original repeat-consistency metric is too strict for adoption review.

## Current deterministic adoption assessment

New artifacts:

```text
experiments/step6_support_drop_contract_v2_assessment.py
tests/test_step6_support_drop_contract_v2_assessment.py
```

The assessment:

- makes zero model/network calls;
- ignores free-text detail for material-repeat comparison;
- still treats candidate identity, candidate state, trust problem/claim state, and trusted claim identity as material;
- computes latency summary from all 25 live calls;
- evaluates the ten Step 6 adoption-gate conditions from the committed evidence;
- proposes `adopt_bounded_extractor` only if every gate check passes.

Default output:

```text
working-memory/evidence/2026-08-03-step6d/contract-v2-adoption-assessment.json
```

## Exact continuation

From the WSL checkout:

```bash
git pull --ff-only

python -m unittest tests.test_step6_support_drop_contract_v2_assessment -v
python -m unittest discover -s tests -v

python -m experiments.step6_support_drop_contract_v2_assessment
```

No LM Studio run is required.

If the deterministic assessment passes all ten gate checks, review its proposed Step 6 disposition. Do not silently equate a bounded extractor adoption with general model reliability.

## Step 6 disposition boundary

Possible dispositions remain:

```text
adopt_bounded_extractor
retain_experiment_only
reject_candidate_deployment
defer_semantic_automation
reconsider_extraction_method
```

Only `adopt_bounded_extractor` authorizes subsequent normal-runtime integration work. If selected, record any required ADR/provider-model contract before activation; deterministic Step 2 validation remains mandatory.

## Stop line

Do not begin normal-runtime semantic integration, Instructor/Pydantic dependency work, retry/correction loops, target-Python conditional activation, CLI orchestration changes, full S001 product execution, or compatibility/safety/recommendation logic until the deterministic adoption assessment is validated and Step 6 receives an explicit disposition.

## Learning state

Current exposure includes semantic oracle vs adoption safety, structured generation, deterministic exact-source grounding, redundant-output design, counterfactual replay, strict-vs-safety scoring, abstention semantics, and material vs textual repeat consistency.

Current depth:

```text
Steps 1–5 behavior validated
+ Step 6A oracle validated
+ Step 6C one-case live path validated
+ Step 6D v1 evidence completed/preserved
+ contract-v2 offline replay completed
+ contract-v2 live evaluation completed (24/25 strict; 25/25 safety)
+ material-consistency metric defect identified
but
post-run adoption assessment not yet user-validated
no final Step 6 disposition
no normal-runtime integration
no formal mastery assessment
not mastered
```
