# Gemma E4B v1.2 Completion-Recovery Load-Flag Correction

This directory contains the corrected one-response runner selected by:

- `working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-load-flag-review.md`

The first completion-recovery attempt is preserved unchanged. It did not load a model because LM Studio rejected the unsupported `--no-speculative-draft-simple` option.

## Only correction

The corrected load command removes:

```text
--no-speculative-draft-simple
```

Everything else remains frozen, including the v1.2 prompt, schema, validators, exact ambiguity source and oracle, Gemma model/configuration, GPU guard, and `max_tokens=1024` request.

## Run

From the repository root:

```bash
bash working-memory/evidence/2026-07-29-gemma-e4b-v1.2-completion-recovery-load-flag-correction/run.sh
```

The runner requires:

```text
GPU used <= 2000 MiB
GPU free >= 6000 MiB
no loaded LM Studio model
```

It runs exactly one model request, then stops and creates:

```text
working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-load-flag-correction-result.md
working-memory/evidence/2026-07-29-gemma-e4b-v1.2-completion-recovery-load-flag-correction/
```

Do not rerun into the same directory or edit generated evidence. Push the first result for independent review.
