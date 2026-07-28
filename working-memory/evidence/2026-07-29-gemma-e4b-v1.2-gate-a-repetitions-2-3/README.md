# Gemma E4B v1.2 Gate A Repetitions 2 and 3

This directory contains the authorized continuation after independent review of the corrected completion-recovery result.

Accepted prior result:

```text
Gate A repetition 1 of 3: passed
commit: 154d83a3ad0741dc60262f0deaafed07d0536669
```

## Purpose

Run the exact frozen ambiguity case two more times under independently checked clean pre-load conditions. Each repetition receives its own preflight, model load, request, validation, unload, and resource snapshots.

The runner stops immediately after the first failed repetition. Gate B is not included here.

## Frozen variables

```text
model: gemma-4-e4b-it-ud
quantization: Q4_K_XL
context: 4096
GPU request: max
parallelism: 1
TTL: 900
identifier: upgradepilot-gemma-e4b-smoke
speculative MTP: disabled
state-contract prompt: v1.2
flat JSON Schema: frozen
category/change-state matrix: frozen
source and oracle: frozen
max_tokens: 1024
temperature: 0
seed: 0
stream: false
Instructor: not used
retries: none
```

Required before **each** repetition:

```text
GPU used <= 2000 MiB
GPU free >= 6000 MiB
no loaded LM Studio model
```

## Run

First update the local checkout:

```bash
git pull --ff-only origin main
```

Then, from the repository root:

```bash
bash working-memory/evidence/2026-07-29-gemma-e4b-v1.2-gate-a-repetitions-2-3/run.sh
```

Do not rerun into this directory. Preserve and push the first generated result even if repetition 2 or 3 fails.

The runner creates:

```text
working-memory/2026-07-29_B2-gemma-e4b-v1.2-gate-a-repetitions-2-3-result.md
working-memory/evidence/2026-07-29-gemma-e4b-v1.2-gate-a-repetitions-2-3/
```

It does not modify `MEMORY.md`. Independent review must decide whether Gate A reached 3/3 and whether Gate B becomes authorized.