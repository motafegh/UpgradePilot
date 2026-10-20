# FCI diagnostic readiness matrix

This matrix describes exposed diagnostic shapes and retained evidence. Correlation expectations below are conditional on explicit input admission; neither eligibility nor a passing byte verifier is an executed product-owner result. Successful CI is not dependency-exercise evidence.

| Diagnostic responsibility | FCI001 — openai agents / mcp | FCI002 — mdformat-footnote / tox | FCI003 — PasarGuard / fastapi |
| --- | --- | --- | --- |
| Exact frozen PR base/head | Yes | Yes | Yes |
| Dependency transition retained | Yes — provider-exact PR diff | Yes — provider-exact PR diff plus provider-exact base/head requirements | Yes — exact base/head pyproject plus provider-exact PR diff; lock transition also in diff |
| Current exact-head workflow acquisition evidence | Structured selected-run evidence; not a complete provider-response replay | Structured selected-run evidence; not a complete provider-response replay | Structured selected-run evidence; not a complete provider-response replay |
| Declared selected run/attempt association | Run `39372679381`, attempt `1`; structured capture provenance | Run `36798375619`, attempt `1`; structured capture provenance | Run `39445488948`, attempt `1`; structured capture provenance |
| Job records retained | 1 record; job-level `head_sha` absent | 13 records; job-level `head_sha` absent | 5 records; job-level `head_sha` absent |
| Unmodified current job-parser admission | Input unavailable: required `head_sha` missing | Input unavailable: required `head_sha` missing | Input unavailable: required `head_sha` missing |
| Runtime-step availability | `non_empty_array` | Mixed: executed jobs `non_empty_array`; two skipped publish jobs `field_absent_or_unavailable` (`null`), not `[]` | All five jobs `non_empty_array` |
| Static workflow bytes retained | Yes — provider-exact overlay matches frozen upstream Git blob | Yes — provider-exact overlay matches frozen upstream Git blob | Yes — original retained copy already matches frozen upstream Git blob |
| Static workflow parse relevance | Ordinary single job; explicit literal display name | First job lacks explicit display name; later test job also uses matrix | Ordinary non-matrix jobs, but static job display names are absent |
| YAML ↔ runtime correlation shape under current owner, after input admission | **Candidate positive identity path**; skipped statuses must remain skipped | **Expected unresolved** — first reason `static_job_name_missing`; matrix is secondary | **Expected unresolved** — missing explicit static job names |
| Dependency/runtime-state eligibility | Not eligible for current narrow supported family; uv/lockfile shaped and relevant user steps were skipped | Not established: observed workflow does not consume `requirements.txt` or invoke tox | Not established from retained step summaries: workflow invokes make targets; exact FastAPI install/exercise is not proven |
| Legitimate unresolved boundary expected | Correlation may establish identity only; it must not imply install/exercise | Correlator should first refuse the unnamed static job rather than guess; later matrix also remains unsupported; skipped-job missing steps stay unavailable; tox exercise remains unresolved | Correlator should refuse missing static names rather than map YAML keys by assumption; dependency exercise remains unresolved |
| Best immediate use | Positive current-correlation-path diagnostic | Negative/refusal control + mixed provider step-state diagnostic + secondary matrix shape | Negative/refusal control with rich runtime evidence and no matrix |

## Record admission and proof qualification

The [2026-10-20 main re-entry review](../../working-memory/2026-10-20_2156_fresh-current-ci-reentry-and-owner-admission-review.md) found a different boundary from the repaired source-byte defects. All selected-run objects omit `workflow_id`, but each exact-head run list retains it on a unique matching run ID; an explicit source join can recover that field. All 19 job records omit the `head_sha` required by the current job parser. Narrow parser probes refuse those records; no provider observation was filled in.

The reduced run lists and job captures also omit normal `total_count`/page envelopes and cover selected workflows only. Recorded job-attempt association is retained in provenance text, without a literal attempt-endpoint request/response archive. Therefore these bundles are not complete normal acquisition replays. They remain useful retained workflow/job/step shapes for a separately scoped diagnostic. A correlation-only typed projection must disclose any derived scope premise and cannot count as acquisition correctness or independently verified job-head observation.

The byte/source-identity verifier checks retained identities and declared expected roles. It does not invoke the product acquisition parser, correlator, runtime-state evaluator or maintainer synthesis. Existing qualification labels retain that narrower interpretation; they do not erase the admission gap.

## Provider/source-retention corrections

A post-publication audit found that the first FCI001 workflow copy and the first FCI002 workflow/base/head requirements copies lost their final newline during connector-to-text persistence. The original raw objects remain immutable and explicitly non-authoritative. Additive `*.provider-exact.*` overlays are now the authoritative source inputs; their Git blob IDs are identical to the frozen upstream source blobs. FCI003 source copies were already exact.

This matters because self-consistent hashes prove retained-file integrity, while equality to the frozen upstream Git blob proves source-byte fidelity.

## Provider wrinkle retained in FCI003

The selected FCI003 workflow run is exact-head and was discovered through the frozen PR head, but the generic run payload exposed an empty `pull_requests` array. The case keeps that fact as provider evidence rather than fabricating a missing relationship. Current exact-head acquisition does not need to convert the empty array into a false PR binding.

## Recommended next diagnostic order

First settle retained-record admission and the diagnostic proof seam. On admitted original inputs, or in a separately labelled conditional correlation-only projection, use this order:

1. Start with FCI001 to test the ordinary static parse → runtime identity-correlation path while preserving skipped statuses and excluding acquisition/dependency-exercise claims from any premise-dependent projection.
2. Run FCI002 next and require `static_job_name_missing` as the first explicit unsupported/unresolved result; also verify `steps: null` is not normalized into an empty step array. The later matrix remains a separately unsupported static shape.
3. Run FCI003 and require explicit unsupported/unresolved static-job-name handling despite rich runtime steps.

Only after these identity/correlation diagnostics should a separate investigation ask whether any case has enough evidence for dependency runtime-state evaluation.
