# UpgradePilot Current Memory

**Last updated:** 2026-08-03  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, selected continuation, and current learning state.

Stable plans, specifications, ADRs, source, tests, [`ENVIRONMENT.md`](ENVIRONMENT.md), and dated working records retain their own responsibilities. They must not mirror or compete with this file for live status.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Selected parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Selected Step 6 plan:** [`plans/B2_STEP_6_SUPPORT_DROP_EXTRACTION_EVALUATION_PLAN.md`](plans/B2_STEP_6_SUPPORT_DROP_EXTRACTION_EVALUATION_PLAN.md)
- **Behavior-validated:** parent Steps 1–5, Step 6A, and Step 6C deterministic/live one-case smoke.
- **Step 6B:** reusable local inference environment baseline established in [`ENVIRONMENT.md`](ENVIRONMENT.md); do not repeat full environment capture.
- **Current increment:** Step 6D — score `gemma-4-e4b-it-ud` against the frozen 15-case support-drop corpus and repeated critical controls.
- **Current Step 6D state:** scorer, localhost runner, and deterministic harness tests implemented; local deterministic validation and live scoring pending.

## Last behavior-validated executable boundary

The Step 6C grounding redesign and deterministic harness are behavior-validated through executable boundary:

```text
d6af31ef01cc30040127f4fca384161e5a8cc8be
```

Ali reported:

```text
Ran 322 tests in 0.062s

OK
```

The Step 6D executable candidate boundary is:

```text
9e17ddf00768f67540ee9355b444eb5b3eb3fadc
```

It is **not** behavior-validated until Ali runs the new focused test and complete suite.

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

Fifteen cases cover:

- direct and paraphrased support drops;
- raised-minimum plus explicit old-line drop;
- raised-minimum-only ungroundable wording;
- support-added and continued-support controls;
- negation and future-drop controls;
- ambiguity;
- irrelevant/no-Python text;
- multiple dropped Python lines;
- valid drop plus unrelated fix;
- instruction-shaped/noisy documentation near a real claim;
- exact S001 excerpt.

This corpus is the semantic oracle. JSON-schema compliance and exact grounding remain separate from semantic correctness.

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
JIT model loading: historically established
```

Normal local model work is:

```text
WSL Python/tests/tools
→ localhost HTTP
→ LM Studio
```

Historical PowerShell commands are provenance, not the default workflow.

The validated localhost runner removes inherited HTTP/HTTPS/ALL proxy variables only for the child process and sets:

```text
NO_PROXY=127.0.0.1,localhost,::1
```

This avoids Privoxy interception without changing Ali's shell/system proxy configuration.

## Step 6C closed — one-case live smoke

Validation record:

[`working-memory/2026-08-03_B2-step-6c-live-s001-validation.md`](working-memory/2026-08-03_B2-step-6c-live-s001-validation.md)

Ali ran:

```bash
python tools/run_step6c_support_drop_smoke.py
```

Observed live result:

```text
transport/model inventory: PASS
completion HTTP: PASS (7.472s)
structured model content:
{
  "state": "candidates_available",
  "candidates": [
    {
      "python_line": "3.8",
      "introduced_in_version": "2.8",
      "source_line_id": "L3"
    }
  ],
  "detail": ""
}
structured candidate mapping: PASS
semantic oracle: PASS
Step 2 trust admission: PASS
finish reason: stop
prompt tokens: 499
completion tokens: 559
reasoning tokens: 475
total tokens: 1058
STEP 6C SMOKE: PASS
```

The deterministic adapter recovered the exact original `L3` source line and offsets rather than asking the model to reproduce source whitespace.

The model correctly distinguished:

```text
Python 3.8 → support drop
Python 3.14 → support addition, not selected
```

### LM Studio reproducibility caveat

The corresponding LM Studio log emitted:

```text
detected an outdated gemma4 chat template, applying compatibility workarounds. Consider updating to the official template.
```

The Step 6C run still passed. Preserve this warning during Step 6D; do not change the template/deployment before the first score because that would make the scoring deployment different from the validated smoke deployment.

Step 6C proves one case only. It does not justify model/product adoption.

## Step 6D implemented boundary awaiting validation

Implementation record:

[`working-memory/2026-08-03_B2-step-6d-support-drop-evaluation-implementation.md`](working-memory/2026-08-03_B2-step-6d-support-drop-evaluation-implementation.md)

Artifacts:

```text
experiments/step6_support_drop_evaluation.py
tools/run_step6d_support_drop_evaluation.py
tests/test_step6_support_drop_evaluation_harness.py
```

### Evaluation schedule

All 15 frozen cases run once.

Five critical controls run three total trials each:

```text
support_added_control
negated_drop_control
future_drop_control
raised_minimum_without_explicit_dropped_line
s001_exact_excerpt
```

Total planned model calls:

```text
15 + (5 × 2) = 25
```

These repetitions are planned evaluation observations, not automatic retries.

### Scoring

Each run records separately:

- transport;
- structured JSON;
- deterministic mapping;
- semantic oracle result;
- Step 2 trust result and oracle match;
- finish reason;
- latency and usage;
- state mismatch;
- false positive;
- false negative;
- wrong Python line;
- wrong introduced release;
- wrong source selection.

Multiple correct candidates may be returned in either order; candidate list order is not treated as semantic meaning.

Case-level semantic/schema/mapping failures are recorded and scoring continues. A transport/server failure stops the run because it contaminates the remaining execution boundary.

The no-Python irrelevant-fix control deterministically constrains `candidates.maxItems = 0` rather than inventing a placeholder Python token.

Default evidence output:

```text
/tmp/upgradepilot-step6d-support-drop-evaluation.json
```

## Exact continuation

From the UpgradePilot WSL virtual environment:

```bash
git pull --ff-only

python -m unittest tests.test_step6_support_drop_evaluation_harness -v
python -m unittest discover -s tests -v
```

If both deterministic runs pass, run:

```bash
python tools/run_step6d_support_drop_evaluation.py
```

Return the complete terminal summary. If individual cases fail semantically, that is valid evaluation evidence; do not interrupt the completed corpus merely because the process exits non-zero.

The evidence JSON in `/tmp` can be inspected only if the terminal summary is insufficient for diagnosis.

## Step 6 adoption gate remains closed

Do **not** adopt a model or runtime adapter merely because Step 6C passed.

After Step 6D, review the evidence against the Step 6 adoption gate and select exactly one disposition:

```text
adopt_bounded_extractor
retain_experiment_only
reject_candidate_deployment
defer_semantic_automation
reconsider_extraction_method
```

Only `adopt_bounded_extractor` can authorize normal-runtime activation, and any durable provider/model/client dependency may require an ADR before product activation.

## Stop line

Until Step 6D scoring is validated, executed, and reviewed, do not begin:

- normal-runtime model/adapter integration;
- new semantic runtime dependencies;
- target-Python conditional activation;
- CLI orchestration changes;
- full S001 relevance execution;
- compatibility, safety, merge, defer, targeted-check, or maintainer-action logic.

## Explicitly not established

- Step 6D deterministic validation;
- Step 6D 25-call scoring result;
- critical-case repeatability;
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
- state/candidate coherence;
- canonical domain representation (`X.Y` vs prose like `Python X.Y`);
- separation of semantic responsibility from formatting/mechanical responsibility;
- repeated critical controls;
- false-positive/false-negative evaluation;
- trust-result scoring versus model-output scoring;
- deployment reproducibility caveats.

Current depth:

```text
Steps 1–5 behavior validated
+ Step 6A oracle validated
+ Step 6C deterministic and live one-case path validated
+ Step 6D scorer implementation exposure
but
Step 6D not yet executed
no model-adoption evidence
no user-owned Step 6 end-to-end explanation recorded
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