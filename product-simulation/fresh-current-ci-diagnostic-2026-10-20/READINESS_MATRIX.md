# FCI diagnostic readiness matrix

This matrix states what each exposed case can diagnose now. It does not predict a desired product result and does not upgrade successful CI into dependency-exercise evidence.

| Diagnostic responsibility | FCI001 — openai agents / mcp | FCI002 — mdformat-footnote / tox | FCI003 — PasarGuard / fastapi |
| --- | --- | --- | --- |
| Exact frozen PR base/head | Yes | Yes | Yes |
| Dependency transition retained | Yes — provider-exact PR diff | Yes — provider-exact PR diff plus provider-exact base/head requirements | Yes — exact base/head pyproject plus provider-exact PR diff; lock transition also in diff |
| Current exact-head workflow acquisition evidence | Yes | Yes | Yes |
| Exact run-attempt identity retained | Yes — run `39372679381`, attempt `1` | Yes — run `36798375619`, attempt `1` | Yes — run `39445488948`, attempt `1` |
| Job acquisition retained | Yes — 1 job | Yes — 13 jobs | Yes — 5 jobs |
| Runtime-step availability | `non_empty_array` | Mixed: executed jobs `non_empty_array`; two skipped publish jobs `field_absent_or_unavailable` (`null`), not `[]` | All five jobs `non_empty_array` |
| Static workflow bytes retained | Yes — provider-exact overlay matches frozen upstream Git blob | Yes — provider-exact overlay matches frozen upstream Git blob | Yes — original retained copy already matches frozen upstream Git blob |
| Static workflow parse relevance | Ordinary single job; explicit literal display name | First job lacks explicit display name; later test job also uses matrix | Ordinary non-matrix jobs, but static job display names are absent |
| YAML ↔ runtime correlation eligibility under current owner | **Eligible** | **Intentionally unsupported** — first expected reason `static_job_name_missing`; matrix is a secondary unsupported shape | **Intentionally unsupported** — missing explicit static job names |
| Dependency/runtime-state eligibility | Not eligible for current narrow supported family; uv/lockfile shaped and relevant user steps were skipped | Not established: observed workflow does not consume `requirements.txt` or invoke tox | Not established from retained step summaries: workflow invokes make targets; exact FastAPI install/exercise is not proven |
| Legitimate unresolved boundary expected | Correlation may establish identity only; it must not imply install/exercise | Correlator should first refuse the unnamed static job rather than guess; later matrix also remains unsupported; skipped-job missing steps stay unavailable; tox exercise remains unresolved | Correlator should refuse missing static names rather than map YAML keys by assumption; dependency exercise remains unresolved |
| Best immediate use | Positive current-correlation-path diagnostic | Negative/refusal control + mixed provider step-state diagnostic + secondary matrix shape | Negative/refusal control with rich runtime evidence and no matrix |

## Provider/source-retention corrections

A post-publication audit found that the first FCI001 workflow copy and the first FCI002 workflow/base/head requirements copies lost their final newline during connector-to-text persistence. The original raw objects remain immutable and explicitly non-authoritative. Additive `*.provider-exact.*` overlays are now the authoritative source inputs; their Git blob IDs are identical to the frozen upstream source blobs. FCI003 source copies were already exact.

This matters because self-consistent hashes prove retained-file integrity, while equality to the frozen upstream Git blob proves source-byte fidelity.

## Provider wrinkle retained in FCI003

The selected FCI003 workflow run is exact-head and was discovered through the frozen PR head, but the generic run payload exposed an empty `pull_requests` array. The case keeps that fact as provider evidence rather than fabricating a missing relationship. Current exact-head acquisition does not need to convert the empty array into a false PR binding.

## Recommended next diagnostic order

1. Start with FCI001 to test the current supported acquisition → static parse → runtime identity-correlation path while keeping dependency exercise out of the claim.
2. Run FCI002 next and require `static_job_name_missing` as the first explicit unsupported/unresolved result; also verify `steps: null` is not normalized into an empty step array. The later matrix remains a separately unsupported static shape.
3. Run FCI003 and require explicit unsupported/unresolved static-job-name handling despite rich runtime steps.

Only after these identity/correlation diagnostics should a separate investigation ask whether any case has enough evidence for dependency runtime-state evaluation.
