# Gemma E4B v1.2 Completion-Recovery Runner

This directory contains the authorized one-response recovery diagnostic selected by:

- `MEMORY.md`
- `working-memory/2026-07-28_B2-gemma-e4b-v1.2-truncation-and-resource-baseline-review.md`

It is dated diagnostic evidence code only. It does not modify UpgradePilot product source, tests, dependencies, networking, LM Studio settings, or `MEMORY.md`.

## Purpose

The previous v1.2 run did not produce a semantic result. The model exhausted the 512-token completion budget in reasoning, emitted no structured content, and ran under a contaminated GPU baseline.

This recovery runner changes only:

```text
max_tokens: 512 -> 1024
```

It keeps the Gemma model, quantization, prompt v1.2, schema, exact ambiguity source, oracle, temperature, seed, endpoint, and deterministic validators unchanged.

## Required pre-load control

The runner refuses scored inference unless:

```text
no LM Studio model is loaded
GPU memory used <= 2000 MiB
GPU memory free >= 6000 MiB
```

Check before running:

```bash
nvidia-smi --query-gpu=memory.used,memory.free,utilization.gpu,temperature.gpu --format=csv
/mnt/c/Users/lenovo/.cache/lm-studio/bin/lms.exe ps --json
```

If the GPU band is not met, do not start the diagnostic. Close or stop the external GPU consumer first.

## Run

From the repository root:

```bash
bash working-memory/evidence/2026-07-29-gemma-e4b-v1.2-completion-recovery/run.sh
```

## Behavior

The runner:

1. compiles and freezes the diagnostic;
2. self-tests the domain validators;
3. checks LM Studio reachability, loaded models, and the GPU control band;
4. captures the pre-load environment;
5. loads the same Gemma E4B configuration;
6. captures the applied runtime and resource state;
7. runs the exact ambiguity source once with `max_tokens=1024`;
8. classifies `finish_reason` and empty content before JSON parsing;
9. validates any complete structured result against the frozen contract and oracle;
10. stops after that one response;
11. unloads the exact model instance in cleanup;
12. captures restoration, product tests, result record, and SHA-256 manifest verification.

A truncation or semantic failure is a valid diagnostic result. Do not rerun into this directory or edit generated evidence.

## Generated outputs

```text
working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-result.md
working-memory/evidence/2026-07-29-gemma-e4b-v1.2-completion-recovery/
```

`MEMORY.md` remains unchanged until independent review.