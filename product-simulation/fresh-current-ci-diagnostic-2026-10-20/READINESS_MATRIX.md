# FCI diagnostic readiness matrix

This matrix states what each exposed case can diagnose now. It does not predict a desired product result and does not upgrade successful CI into dependency-exercise evidence.

| Diagnostic responsibility | FCI001 — openai agents / mcp | FCI002 — mdformat-footnote / tox | FCI003 — PasarGuard / fastapi |
| --- | --- | --- | --- |
| Exact frozen PR base/head | Yes | Yes | Yes |
| Dependency transition retained | Yes — provider-exact PR diff | Yes — exact base/head requirements plus PR diff | Yes — exact base/head pyproject plus provider-exact PR diff; lock transition also in diff |
| Current exact-head workflow acquisition evidence | Yes | Yes | Yes |
| Exact run-attempt identity retained | Yes — run `39372679381`, attempt `1` | Yes — run `36798375619`, attempt `1` | Yes — run `39445488948`, attempt `1` |
| Job acquisition retained | Yes — 1 job | Yes — 13 jobs | Yes — 5 jobs |
| Runtime-step availability | `non_empty_array` | Mixed: executed jobs `non_empty_array`; two skipped publish jobs `field_absent_or_unavailable` (`null`), not `[]` | All five jobs `non_empty_array` |
| Static workflow bytes retained | Yes | Yes | Yes |
| Static workflow parse relevance | Ordinary single job; explicit literal display name | Matrix job is present; several jobs also lack explicit display names | Ordinary non-matrix jobs, but static job display names are absent |
| YAML ↔ runtime correlation eligibility under current owner | **Eligible** | **Intentionally unsupported** — matrix | **Intentionally unsupported** — missing explicit static job names |
| Dependency/runtime-state eligibility | Not eligible for current narrow supported family; uv/lockfile shaped and relevant user steps were skipped | Not established: observed workflow does not consume `requirements.txt` or invoke tox | Not established from retained step summaries: workflow invokes make targets; exact FastAPI install/exercise is not proven |
| Legitimate unresolved boundary expected | Correlation may establish identity only; it must not imply install/exercise | Correlator should refuse matrix rather than guess; skipped-job missing steps stay unavailable; tox exercise remains unresolved | Correlator should refuse missing static names rather than map YAML keys by assumption; dependency exercise remains unresolved |
| Best immediate use | Positive current-correlation-path diagnostic | Negative/refusal control + mixed provider step-state diagnostic | Negative/refusal control with rich runtime evidence and no matrix |

## Provider wrinkle retained in FCI003

The selected FCI003 workflow run is exact-head and was discovered through the frozen PR head, but the generic run payload exposed an empty `pull_requests` array. The case keeps that fact as provider evidence rather than fabricating a missing relationship. Current exact-head acquisition does not need to convert the empty array into a false PR binding.

## Recommended next diagnostic order

1. Start with FCI001 to test the current supported acquisition → static parse → runtime identity-correlation path while keeping dependency exercise out of the claim.
2. Run FCI002 next and require an explicit unsupported/unresolved matrix result. Also verify `steps: null` is not normalized into an empty step array.
3. Run FCI003 and require an explicit unsupported/unresolved static-job-name result despite rich runtime steps.

Only after these identity/correlation diagnostics should a separate investigation ask whether any case has enough evidence for dependency runtime-state evaluation.
