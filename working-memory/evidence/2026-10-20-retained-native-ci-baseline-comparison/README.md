# Retained native CI versus transparent baseline comparison

Accepted scope: [feasibility findings, sections 6–7](../2026-10-20-product-value-and-transparent-baseline-feasibility/FINDINGS.md).

Delivered: two completed rows, one execution, no retries. [Source-aware review](COMPARISON_REVIEW.md) finds no material CI increment for HTTPX and limited useful specificity for glyphsLib. No full-product/action/usefulness verdict follows. See [raw outputs](execution/results.json), [review overlay](review.json), and [identity/resource verification](verification.json).

This packet starts with a pre-execution [input/source-span/executable/rubric freeze](freeze.json). It compares exactly two exposed October 16 retained CI outputs with the unchanged four-input baseline. Preparation computes no baseline outcome and invokes no native decoder. It grants no full-investigation, positive-action, independent-usefulness or fresh-product-derivation claim.

The experiment is [retained_native_ci_baseline_comparison.py](../../../experiments/retained_native_ci_baseline_comparison.py); its [focused tests](../../../experiments/tests/test_retained_native_ci_baseline_comparison.py) use synthetic/mock capture inputs, not the retained comparison rows. Eleven focused tests pass. Three existing durable reconstruction tests also pass: complete native-value preservation through store/backup; unsupported codec/semantic-version refusal; storage integrity/schema/target/selection refusal (13.233 seconds). No product source changed. No full suite or Ruff result is claimed.

Commands, run from the repository root with the existing virtual environment:

```sh
PYTHONPATH=src:tests:. .venv/bin/python3 -m unittest experiments.tests.test_retained_native_ci_baseline_comparison -v

PYTHONPATH=src:. .venv/bin/python3 -m experiments.retained_native_ci_baseline_comparison prepare \
  --root /home/motafeq/.local/share/upgradepilot/investigator-inputs/common-freeze-2026-10-16-2025 \
  --freeze working-memory/evidence/2026-10-20-retained-native-ci-baseline-comparison/freeze.json
```

The freeze already exists and must not be overwritten. The authorized run uses a new output directory and a new owner-only private directory outside Git, with an outer 300-second watchdog in addition to per-child/aggregate deadlines. No failed-row rerun or further comparison is automatic. Original checkpoints are copied before opening product APIs; all 17 original inventory members are verified before/after. Full native output remains private; public output retains state summaries, exact inputs/source identities, keyword matches, timing, record/method/owner identities and payload hashes.

The single execution, after implementation/freeze publication at `305ba04d`, was:

```sh
timeout --signal=TERM --kill-after=5s 300s env PYTHONPATH=src:. .venv/bin/python3 -m experiments.retained_native_ci_baseline_comparison run \
  --freeze working-memory/evidence/2026-10-20-retained-native-ci-baseline-comparison/freeze.json \
  --output working-memory/evidence/2026-10-20-retained-native-ci-baseline-comparison/execution \
  --private /home/motafeq/.local/share/upgradepilot/retained-ci-baseline-runs/2026-10-20-comparison-r1
```

This is execution provenance, not a request to rerun. Whole run: 0.586444 seconds; all case/aggregate ceilings respected. Both baseline evaluations and native reconstructions completed. Zero new project model/provider predictions, GPU/model loading, network acquisition, target commands or installs. Two full native projections and two baseline preservation files remain owner-only outside Git; the public packet references their identities. Partial baseline files are preservation checkpoints, not extra executions.

The baseline's action is recordable; the component's maintainer action remains unavailable. Review separately credits supported facts, locates unknowns, rejects reassurance and assesses narrower information value. More detail alone receives no credit. Written D explanation is delivered; learner ownership and E closure remain pending. The recommended next responsibility is a separate design decision about preserving existing CI/report authority in experimental final presentation, with no automatic new implementation or inference.
