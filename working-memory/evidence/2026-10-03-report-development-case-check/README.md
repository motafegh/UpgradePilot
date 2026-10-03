# Report development check — real cases and one projection repair

This is known-case engineering evidence, not a blind study, matched presentation comparison or independent usefulness result. The initial attempts use installed product source at `5aebc19d`; the subsequent repair is identified by exact working-tree source/test hashes in its manifest. All product Python files were checked against the installed package before each acquisition stage. Public GitHub requests were anonymous with process-local token/proxy removal, and the normal console CLI ran outside the checkout in `/tmp`. No target code was executed or changed and no model/deployment configuration was changed.

## Inputs and actual outcomes

| Development pressure | Normal product result | Missing responsibility / disposition |
| --- | --- | --- |
| Soup Sieve support-drop and static CI (S001) | Reused the [earlier ordinary saved report](../2026-10-03-report-model-recovery/live-model-investigation-report.json), with its recorded identity/hash. Grounded Python 3.8 drop is outside target `>=3.10`; static CI/runtime limits and abstention persist. No new model run for this control. | A bounded non-applicability result is available. It does not establish overall compatibility or general impact discovery. |
| HTTPX API/context coverage (S002) | [Normal report](httpx-api-context-report.json): exact HTTPX `0.27.2 → 0.28.1` transition; 17 sources and 9 unknowns; no currently returned exact-head workflow runs; upstream resolver returns `source_unavailable` because no exact distribution file supplied usable PyPI publisher provenance. No HTTPX API-impact analysis was reached or claimed. | Acquisition/source authority plus broader API and target-adapter interpretation. The retained manual case examines removed `app=`, old/fixed Starlette and FastAPI `TestClient`, but those findings are not normally produced today. Resolving upstream identity alone would not make a Python-support-drop-only extractor an API-change analyzer. |
| OpenCV wheel/source fallback (S008) | [Before-repair report](opencv-artifact-report-before-repair.json): exact `4.2.0.32 → 4.8.1.78`; 27 removed tag capabilities and 8 added; source distribution available; target applicability unresolved; source-build outcome unknown; abstain; 18 sources and 11 unknowns. Exact removed/added tags and package file metadata are retained even though the human summary is shorter. | Normal target-environment collection currently depends on CI-supported direct-requirements/workflow relationships. No exact-head runs are currently returned, so no such target associations are produced. The richer manual packet establishes a bounded Python-3.6 Linux context using repository documents/code/configuration, not this normal producer path. |

Both newly acquired PR base/head pairs matched the prior case identities. That does **not** make current CI availability identical to historical captures: both current runs returned no exact-head workflow runs, whereas the manual packets retain earlier CI analysis. No global claim that these projects never had CI is made.

The stored bytes/hashes of the separately attributed retrospective packets are indexed in [archived-input-identities.json](archived-input-identities.json). They are development pressure evidence, not new product inputs or independent labels. Initial normal invocations were recorded before execution in [attempt-manifest.json](attempt-manifest.json); their original output paths remain exact invocation history. Four captured files were subsequently renamed descriptively without changing bytes, and the relocation map is recorded there. [execution-results.json](execution-results.json) records actual outcomes and current stored report names.

## Concrete repair and its owner

The OpenCV normal result exposed a projection defect: `target_artifact_environment_results=()` was rendered as `not activated` even with an established artifact candidate. The application enters environment collection for an established candidate, and an empty association result does not establish that the branch was skipped.

`src/upgradepilot/report_projection.py` now reports `not established` for that shape and explains that no supported target associations were retained and applicability remains unresolved. The no-candidate path retains its existing `not activated` wording, and nonempty associations retain their original behavior. The existing report-file vocabulary already admits this state; no schema, domain analysis, authority, source acquisition or action permission changes were needed.

The existing report regression was extended to reproduce the actual empty-association shape through projection → JSON encode/decode → human rendering. Its first draft mistakenly used the fixture's nonempty association; that setup was corrected before product mutation. The corrected test failed specifically on `not activated` versus `not established`, then passed with the projection repair. No additional test count or fixture-specific product rule was introduced.

After rebuilding, [the new ordinary installed report](opencv-artifact-report-after-repair.json) verifies the corrected state on the same PR base/head, while preserving the artifact candidate, unknown source-build outcome and abstention. The old saved report remains byte-for-byte unchanged; offline opening preserves its earlier recorded content rather than reprojecting it with new code. [Repair attempt manifest](repair-attempt-manifest.json) and [verification](repair-verification.json) separate the fresh acquisition from any same-evidence utility comparison.

## Verification and remaining debt

- Focused report tests: 20/20 before the regression extension and 20/20 after repair.
- Full product regression: 739/739 in checkout and 739/739 against the rebuilt installed package from `/tmp`.
- Installed normal save on the unchanged OpenCV PR revisions; strict saved-record read; offline console/module output parity; unchanged prior report SHA-256: PASS.
- Touched-file Ruff: PASS using the already available developer binary `/home/motafeq/projects/jobhunter/.venv/bin/ruff`; UpgradePilot's venv and PATH had no Ruff binary. No new dependency was installed for linting.
- Focused diff/whitespace and local documentation-link checks: recorded with the publication check.

Neither new contrasting run reached upstream model interpretation, because upstream authority prerequisites were unavailable. The local model endpoint was reachable; these runs do not prove new real-model semantic accuracy. Existing broader experiment/governance debt was not reclassified or repaired by this increment. Independent reviewer/adjudication and a same-evidence baseline/report pair remain entry debt; no independent study has started or passed. The richer manual packets were not injected into production to manufacture a useful result.

Engineering disposition: the reporting defect is repaired. Next capability work needs a bounded source-authority/target-context design for normally reachable impact discovery, with HTTPX as a known development pressure and independent/protected evaluation admitted separately. Do not weaken publisher/source checks to improve apparent coverage, hardcode known diagnoses, substitute polished prose for missing evidence, or automatically add an agent/framework.
