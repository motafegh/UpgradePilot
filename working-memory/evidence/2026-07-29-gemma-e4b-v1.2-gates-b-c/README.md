# Gemma E4B v1.2 Gates B and C

This directory contains the one-command evidence runner authorized after the
independent Gate A 3-of-3 review.

It runs the frozen Gate B contrast cases once each and stops on the first failed,
truncated, invalid, or unsupported result. Only if all five Gate B cases pass does
it run the frozen Gate C conflicting-support case once.

## Frozen cases

Gate B:

1. `Request retry behavior changed for slow networks.`
2. `This release remains backward compatible with the previous patch release and requires no migration.`
3. `Older environments may be affected.`
4. `Python version support policy changed in this release.`
5. `Documentation examples were reorganized and several spelling errors were corrected.`

Gate C:

```text
This release adds Python 3.13 support. This release drops Python 3.13 support.
```

## Required local state

```text
GPU used <= 2000 MiB
GPU free >= 6000 MiB
no loaded LM Studio model
LM Studio server running on port 12345
```

## Run

From the repository root:

```bash
bash working-memory/evidence/2026-07-29-gemma-e4b-v1.2-gates-b-c/run.sh
```

Do not rerun into this directory or edit generated evidence. Push the first result
for independent review before any broader evaluation or product integration.
