# Gemma E4B State-Contract v1.2 Diagnostic Runner

This directory contains the authorized, self-contained evidence harness for:

- `working-memory/2026-07-28_B2-ambiguity-boundary-review-and-state-contract-v1.2-diagnostic.md`

It is diagnostic evidence code only. It does not modify `src/upgradepilot/`, `tests/`, dependencies, networking, LM Studio settings, or `MEMORY.md`.

## What the runner does

The runner:

1. verifies the Python harness compiles;
2. freezes the v1.2 prompt, schema hash, category/change-state matrix, and seven case oracles;
3. self-tests the deterministic validator;
4. checks that LM Studio is reachable and refuses to continue if any model is already loaded;
5. captures the pre-load environment;
6. loads `gemma-4-e4b-it-ud` with the frozen 4096-context configuration;
7. captures applied model and GPU state;
8. starts bounded LM Studio input/output and performance logs;
9. runs Gate A three times and stops on the first failure;
10. runs Gate B only after Gate A passes and stops on the first failure;
11. runs Gate C only after Gate B passes;
12. unloads the exact model identifier in the cleanup path;
13. captures the restored environment;
14. runs the existing deterministic product tests without changing product source;
15. writes a dated Markdown result record, raw evidence, hashes, and manifest verification.

A semantic gate failure is an expected stop condition, not an infrastructure failure. The runner still unloads the model and creates a complete review bundle.

## Run

From the repository root:

```bash
bash working-memory/evidence/2026-07-28-gemma-e4b-state-contract-v1.2/run.sh
```

The runner prefers `.venv/bin/python3`, then the active virtual environment, then `python3` on `PATH`.

The known LM Studio CLI path is:

```text
/mnt/c/Users/lenovo/.cache/lm-studio/bin/lms.exe
```

To override it deliberately:

```bash
LMS_EXE=/your/exact/lms.exe/path \
  bash working-memory/evidence/2026-07-28-gemma-e4b-state-contract-v1.2/run.sh
```

## Safety and repeatability

- Do not load another model before or during the run.
- The runner refuses to overwrite an existing v1.2 result or `runs/` directory.
- It does not call `lms unload --all`; it unloads only `upgradepilot-gemma-e4b-smoke` when this runner loaded it.
- Do not edit generated responses or validators after the run.
- Do not rerun into the same directory. Preserve the first evidence and obtain a new dated directory for any authorized rerun.

## Generated outputs

The run creates:

```text
working-memory/2026-07-28_B2-gemma-e4b-state-contract-v1.2-diagnostic-result.md
working-memory/evidence/2026-07-28-gemma-e4b-state-contract-v1.2/
```

The evidence directory includes frozen prompts and cases, requests, raw and parsed responses, reasoning/logs, validation, snapshots, load/unload output, product-test output, repository status, `MANIFEST.sha256`, and immediate manifest verification.

`MEMORY.md` remains unchanged until independent review.
