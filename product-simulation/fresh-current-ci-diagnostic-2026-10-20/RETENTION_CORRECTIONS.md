# FCI retention and semantic corrections

Date: 2026-10-20.

This record is additive. Previously published `raw/` objects are not overwritten.

## Source-byte corrections

Post-publication comparison against the target repositories' Git object identities found that three source copies were content-equivalent for parsing but not byte-identical to the target-revision source: their final newline had been lost during connector-to-text persistence.

- FCI001 `raw/workflow.yml`: 1189 bytes, blob `63f5ee224190db7a3c59d7c16129a373ed864396`; upstream exact source is 1190 bytes, blob `fb2110166d4df410cea5f181d0e75a55b92824a4`.
- FCI002 `raw/workflow.yml`: 4353 bytes, blob `a4eca8f90e09255f960d1047f60dd645cf65d6ca`; upstream exact source is 4354 bytes, blob `9643a4ea975e7182c548e4bc8e94accb93aa0056`.
- FCI002 `raw/requirements.base.txt` / `raw/requirements.head.txt`: 78-byte persisted copies omitted the final newline; exact upstream blobs are `994653111f7abfd53b8e4e0f932a1696dcf87189` and `b6afd3da9c4d83bbf7c82b2c1e9c7d900c03b790`, 79 bytes each.

Exact additive replacements are retained as `*.provider-exact.*`. Their Git blob IDs are identical to the source blobs in the frozen target revisions. The earlier copies remain immutable but are non-authoritative for byte-exact replay.

FCI003 workflow and base/head `pyproject.toml` copies already match the frozen source Git blobs exactly and require no source-byte repair.

## FCI002 correlation-boundary correction

FCI002 contains both unsupported static shapes: jobs without explicit literal `name:` values and a matrix test job. The current correlation owner checks each job in workflow order and rejects a missing static job name before it reaches the later matrix job. Therefore the expected first current-owner result is `static_job_name_missing` for `pre-commit`; `static_job_strategy_unsupported` remains a valid secondary unsupported property of the same workflow, not the first expected reason.

This distinction matters because the cohort is intended to test the current contract exactly rather than merely assert that some unsupported shape exists.

## Verification implication

A verifier that only compares retained bytes to their own manifest hashes proves internal persistence integrity, not fidelity to the frozen upstream source. The authoritative source artifacts must also carry the expected upstream Git blob identity. Offline verification should enforce those expected source identities for the provider-exact overlays.
