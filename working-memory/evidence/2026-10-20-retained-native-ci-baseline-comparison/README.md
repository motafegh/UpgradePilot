# Retained native CI versus transparent baseline comparison

Accepted scope: [feasibility findings, sections 6–7](../2026-10-20-product-value-and-transparent-baseline-feasibility/FINDINGS.md).

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

Before execution, both comparison rows and semantic review are pending. The baseline's action is recordable; the component's maintainer action is unavailable. Human source-aware review must separately assess supported facts, forbidden reassurance, located unknowns, and whether the additional information can change an investment decision. More detail alone receives no credit.
