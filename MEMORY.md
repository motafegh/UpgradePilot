# UpgradePilot Current Memory

**Last updated:** 2026-08-03  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, selected continuation, and current learning state.

Stable plans, specifications, ADRs, source, tests, [`ENVIRONMENT.md`](ENVIRONMENT.md), and dated working records retain their own responsibilities. They must not mirror or compete with this file for live status.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Selected parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Selected Step 6 plan:** [`plans/B2_STEP_6_SUPPORT_DROP_EXTRACTION_EVALUATION_PLAN.md`](plans/B2_STEP_6_SUPPORT_DROP_EXTRACTION_EVALUATION_PLAN.md)
- **Behavior-validated before current contract-v2 work:** parent Steps 1–5, Step 6A, and Step 6C deterministic/live one-case smoke.
- **Step 6D v1 live evaluation:** completed with 25/25 planned calls and durable evidence committed.
- **Current increment:** Step 6D contract-v2 diagnosis — deterministically replay the exact committed v1 model outputs after removing redundant candidate-state prediction, before spending another 25 model calls.
- **Current contract-v2 code:** implemented but not yet user-validated.
- **No model or semantic adapter is adopted.**

## Last exact user-reported deterministic validation

Before Step 6D v1 implementation, Ali reported:

```text
Ran 322 tests in 0.062s

OK
```

Do not invent a later full-suite count. The new contract-v2 files require fresh focused/full deterministic validation.

## Closed Step 5 authority boundary

Step 5 remains fully closed with deterministic and live S001 public-source evidence:

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

## Step 6 semantic responsibility

The narrow path remains:

```text
AuthoritativeUpstreamIntervalEvidence
→ untrusted semantic selection
→ deterministic candidate construction
→ CandidateUpstreamClaimResult
→ validate_support_drop_candidates(...)
→ GroundedPythonSupportDropClaim
   or explicit claim problem
```

Only this semantic meaning is in scope:

```text
category = support_boundary_change
change_state = support_dropped
python_line = explicit X.Y
introduced_in_version = exact trusted crossed release
```

The model does **not** own dependency identity, source authority, category/direction constants, exact quote reproduction, or quote offsets.

## Step 6A frozen oracle

Frozen corpus:

```text
experiments/step6_support_drop_semantic_corpus.json
```

Fifteen cases cover direct/paraphrased drops, support-added/continued controls, negation, future tense, raised-minimum-only wording, ambiguity, irrelevant text, multiple drops, noisy/instruction-shaped text, and exact S001.

The corpus remains the semantic oracle. Structured output and grounding are not substitutes for semantic correctness.

## Step 6B environment boundary

UpgradePilot's control plane is WSL2.

Reusable baseline:

```text
checkout: /home/motafeq/projects/UpgradePilot
Python: 3.12.3
venv: /home/motafeq/projects/UpgradePilot/.venv/bin/python3
GPU: NVIDIA GeForce RTX 3070 Laptop GPU, 8192 MiB nominal VRAM
LM Studio host process: Windows
LM Studio loopback: http://127.0.0.1:12345
```

Normal local-model work:

```text
WSL Python/tests/tools
→ localhost HTTP
→ LM Studio
```

The validated localhost runner removes inherited HTTP/HTTPS/ALL proxy variables only for its child process and sets:

```text
NO_PROXY=127.0.0.1,localhost,::1
```

Do not switch to PowerShell as the normal project control plane.

## Step 6C closed — one-case smoke

Validation record:

[`working-memory/2026-08-03_B2-step-6c-live-s001-validation.md`](working-memory/2026-08-03_B2-step-6c-live-s001-validation.md)

Observed successful S001 path:

```text
transport/model inventory: PASS
completion HTTP: PASS
structured candidate mapping: PASS
semantic oracle: PASS
Step 2 trust admission: PASS
finish reason: stop
STEP 6C SMOKE: PASS
```

The model selected Python 3.8 / release 2.8 / source line L3 and ignored the Python 3.14 support addition. Exact source quote/offsets were recovered deterministically from the line ID.

LM Studio emitted an outdated-Gemma4-template compatibility warning. The run still passed. Preserve that deployment caveat; do not silently change the model/template while comparing evidence.

Step 6C proves one case only and never justified adoption.

## Step 6D v1 — completed live evaluation

Durable evidence:

```text
working-memory/evidence/2026-08-03-step6d/support-drop-evaluation.json
```

Evidence commit reported by Ali:

```text
a4b2e37
```

Observed summary:

```text
completed: true
runs_completed: 25
runs_planned: 25
passed: 14
failed: 11
semantic_passed: 14
trust_oracle_passed: 14
all_critical_repeats_consistent: true
```

No transport failure stopped the evaluation.

### Failure decomposition

The 11 failures split into two materially different classes.

#### Seven candidate-bearing state-coherence failures

Observed on:

```text
drop_direct r1
drop_paraphrase_no_longer_supported r1
drop_paraphrase_removed r1
valid_drop_plus_unrelated_fix r1
s001_exact_excerpt r1
s001_exact_excerpt r2
s001_exact_excerpt r3
```

These returned candidate records while also returning:

```text
state = unresolved
```

The v1 adapter rejected the contradiction because non-empty candidates require `candidates_available`.

The committed direct/S001 evidence shows the model reasoning and candidate payload selecting the current dropped Python line, release, and source line correctly while the separate top-level state conflicts. This exposed redundant contract encoding rather than sufficient evidence of semantic misunderstanding.

#### Four genuine zero-candidate semantic disagreements

Observed on:

```text
raised_minimum_without_explicit_dropped_line r1
raised_minimum_without_explicit_dropped_line r2
raised_minimum_without_explicit_dropped_line r3
ambiguous_support_wording r1
```

These mapped successfully but returned:

```text
no_relevant_claim
```

where the frozen oracle requires:

```text
unresolved
```

These remain genuine semantic failures unless a later clean contract causes the model itself to choose differently.

Analysis record:

[`working-memory/2026-08-03_B2-step-6d-contract-v1-analysis-and-v2-replay-plan.md`](working-memory/2026-08-03_B2-step-6d-contract-v1-analysis-and-v2-replay-plan.md)

## Contract v2 — current experiment

Contract v1 asked the model to predict both:

```text
candidates = non-empty
state = candidates_available
```

which duplicates the same fact.

Contract v2 model-facing output is:

```text
candidates: [...]
unresolved_if_no_candidates: true | false
detail: string
```

The deterministic adapter derives the existing domain state:

```text
if candidates:
    state = candidates_available
elif unresolved_if_no_candidates:
    state = unresolved
else:
    state = no_relevant_claim
```

Important: the unresolved flag remains a genuine semantic responsibility only when there are zero candidates.

Contract-v2 artifacts:

```text
experiments/step6_support_drop_contract_v2.py
experiments/step6_support_drop_contract_v2_replay.py
tests/test_step6_support_drop_contract_v2.py
```

No Instructor, Pydantic, new runtime dependency, retries, model change, or product integration has been introduced.

## Why offline replay comes before a new live run

The exact 25 v1 structured model outputs are already committed.

The next experiment therefore makes **zero new model calls** and asks only:

```text
historical v1 structured output
→ ignore historical top-level state when candidates exist
→ preserve historical zero-candidate state choice exactly
→ contract-v2 deterministic adapter
→ same semantic oracle
→ same Step 2 validator
```

This isolates the effect of removing duplicated state encoding.

The replay is counterfactual/deterministic evidence, not proof of new live model behavior.

Default replay output:

```text
/tmp/upgradepilot-step6d-contract-v2-replay.json
```

## Exact continuation

From the UpgradePilot WSL virtual environment:

```bash
git pull --ff-only

python -m unittest tests.test_step6_support_drop_contract_v2 -v
python -m unittest discover -s tests -v

python experiments/step6_support_drop_contract_v2_replay.py
```

Return the complete replay summary.

Do **not** run another 25-call LM Studio evaluation yet. First inspect exactly how many historical failures are rescued by the contract-only replay and which failures remain.

## Decision after replay

If the replay shows that candidate-bearing failures disappear while the zero-candidate unresolved/no-relevant disagreements remain, then implement/run one clean live contract-v2 evaluation against the same Gemma deployment with:

```text
temperature = 0
seed = 0
automatic retries = false
```

Only after that should we decide whether to retain/reject Gemma or compare another existing model.

Instructor remains a possible later adapter experiment, not a repair mechanism for this first-pass semantic evaluation.

## Adoption gate remains closed

Allowed eventual dispositions remain:

```text
adopt_bounded_extractor
retain_experiment_only
reject_candidate_deployment
defer_semantic_automation
reconsider_extraction_method
```

Only `adopt_bounded_extractor` can authorize normal-runtime activation, and any durable provider/model/client dependency may require an ADR before product activation.

## Stop line

Do not begin:

- normal-runtime model/adapter integration;
- Instructor/Pydantic or other new semantic runtime dependencies;
- automatic retry/correction loops;
- target-Python conditional activation;
- CLI orchestration changes;
- full S001 relevance execution;
- compatibility, safety, merge, defer, targeted-check, or maintainer-action logic.

## Explicitly not established

- contract-v2 deterministic test success;
- contract-v2 offline replay result;
- live contract-v2 Gemma score;
- a selected/adopted semantic model;
- an adopted support-drop extractor;
- automated live S001 semantic extraction in normal runtime;
- target-Python conditional activation;
- S001 automated end-to-end relevance;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery of Steps 1–6.

## Learning state

Current concepts exposed:

- semantic oracle;
- untrusted semantic selection;
- deterministic exact-source grounding;
- redundant model-output fields versus derived domain state;
- state/candidate coherence;
- canonical domain representation;
- counterfactual replay as experimental isolation;
- repeated critical controls;
- false-positive/false-negative evaluation;
- trust-result scoring versus model-output scoring.

Current depth:

```text
Steps 1–5 behavior validated
+ Step 6A oracle validated
+ Step 6C deterministic/live one-case path validated
+ Step 6D v1 25-call evidence completed and preserved
+ v1 failure classes identified
+ contract-v2/replay implementation available
but
contract-v2 deterministic tests not yet user-validated
contract-v2 replay not yet observed
no model adoption evidence
no formal mastery assessment
not mastered
```

Product behavior validation, model semantic evidence, environment knowledge, and learning mastery remain separate claims.

## State-maintenance rule

When route, selected responsibility, verified executable boundary, blocker, learning state, or exact continuation changes:

1. update `MEMORY.md` only for live state;
2. update `ENVIRONMENT.md` only for reusable environment baseline/rule changes;
3. use dated `working-memory/` for material historical evidence;
4. preserve failures and unknowns rather than inferring success;
5. do not duplicate live status into plans/specifications/ADRs.
