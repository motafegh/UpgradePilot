# HTTPX fallback condition in caller/signature reports

Applied `UP-SKILL:upgradepilot-planning-design` and `UP-SKILL:upgradepilot-working-memory`. This is a completed design comparison and evidence record. The selected continuation belongs to [MEMORY.md](../MEMORY.md).

## Maintainer question

When the first view says both HTTPX versions fit, which import path does that finding cover? The Python-aware selection trial found both a current Python 3.10 candidate with a fallback and a pre-merge candidate with a direct import. If the report cannot distinguish those paths, choosing a more relevant adapter version still leaves a material condition implicit. The comparison reused the default Dashboard API #20 report, its exact Workspace revision and the two tag-to-wheel-qualified Starlette sources. [Source qualification](2026-11-26_python-sample-source-qualification.md) · [First-view comparison method](../plans/MAINTAINER_REPORT_PRESERVATION_AND_USEFULNESS_EVALUATION_PLAN.md#first-view-comparison-on-saved-reports)

## Evidence

| Case | Starlette source | Selected import in HTTPX witnesses | Condition observed in source |
| --- | --- | --- | --- |
| Default saved report | 1.10.0, `source-39` | `import httpx`, line 32 | Runtime branch tries `httpx2 as httpx` at line 29. The line 30 handler catches `ModuleNotFoundError` and reaches the nested HTTPX import. |
| Current candidate for Python 3.10 | 1.7.0 | `import httpx`, line 39 | Same structure at lines 36, 37 and 39. |
| Pre-merge candidate for Python 3.10 | 0.46.2 | `import httpx`, line 30 | The guarded direct HTTPX import raises `RuntimeError` on `ModuleNotFoundError`. There is no preceding HTTPX2 attempt. |

All eight inspected native witnesses found conditional argument fit across HTTPX 0.27.2 and 0.28.1. All eight carried the same two generic try/import premises. In all four saved-report witnesses, the selected path records the HTTPX import at line 32. The witness steps omit the related preferred import at line 29 and the handler at line 30. The saved source bytes contain those lines, and the earlier sample qualification retains a separate independent branch observation. The report's structured witness has no recorded relation between those locations. A rule that treats the generic premises as a fallback indicator mislabels the pre-merge case. [Structured comparison](evidence/2026-11-26-httpx-fallback-witness-design/comparison.json) · [Native correspondence](../src/upgradepilot/caller_signature/correspondence.py#L605) · [Report projection](../src/upgradepilot/report_projection.py#L2168)

An independent diagnostic read the literal sources with Python's AST and matched the selected re-export location to the attempted import, the handler and the shared local binding. It found two fallback paths and one direct path. It covered the runtime arm of `TYPE_CHECKING` and the nested fallback with a warning on successful import, as seen in the two real fallback files. Seven syntax controls checked the supported simple shape, direct guarded import, different binding, different exception, witness selecting the preferred import, wrong source location and wrong compared package. These checks cover source syntax and the selected witness join. Exception identity and matching at runtime, import success, effective class binding and test execution remain unresolved. 'If importing HTTPX2 raises `ModuleNotFoundError`' describes the syntactic condition. The exception can also arise inside an imported dependency.

## Design decision

| Approach | Result |
| --- | --- |
| Keep the current summary and source link | Preserves current proof. The maintainer can recover the condition by opening the exact source. The first view still leaves the branch implicit. |
| Interpret the generic premises as a fallback signal | Misclassifies the pre-merge control. |
| Parse retained source when reopening a report | Could recover syntax but would perform new analysis during a saved-data read, contrary to Core §6.1 and the offline reader contract. |
| Record the import relationship in the native source producer | Gives the report a specific, attributable condition and supports the same explanation when read from a saved report or Workspace. |

The producer should record a structured branch operation for the exact import used in the witness. The minimum evidence is the retained file identity, the preferred and selected import spans and module names, the handler span and exception spelling, and the shared local binding. The selected import needs to match the witness path and compared package. Treat this as a conditional source relationship and retain the existing unresolved premises. Capture it where native correspondence has the AST and chooses the import path. Carry it through native result encoding and validation into the report projection. Existing result decoding checks candidate shape and step identity, so compatibility and round-trip validation are part of the Build. [Native candidate decoder](../src/upgradepilot/caller_signature/result_codec.py#L279) · [Core saved-result boundary](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md#61-evidence-reports-and-saved-result-boundaries)

A possible first-view line is “HTTPX fit applies to Starlette’s fallback when importing HTTPX2 raises `ModuleNotFoundError`.” This is a wording sketch. Display it only when the witnesses behind the paired result agree on the source, binding and branch. Missing or divergent branch information, direct guarded imports, and compatible older saved reports retain the existing conditional summary. A newly produced report can carry the relationship once qualified. The renderer should derive the wording from validated recorded fields. [First-view renderer](../src/upgradepilot/report.py#L372) · [Offline reader contract test](../tests/test_caller_signature_delivery.py#L118)

## Verification and handoff

The source diagnostic ran twice with networking isolated and produced byte-identical output. Offline saved-report and Workspace openings displayed the same report body, with Workspace provenance appended. Both exposed the exact retained source bytes for `source-39`. The current first view still lists FastAPI 0.165.0 and Starlette 1.10.0, both HTTPX versions fit conditionally, and the saved action is `abstain`. The two focused delivery tests and all eleven focused worker tests passed. No fresh provider requests, product runtime changes or target execution took place. The source probe is a local design diagnostic. The repository retains its receipt and input digests.

The bounded Build should first prove producer ownership and structured retention using both real fallback shapes and the real direct-import control. Cover missing or conflicting joins, a paired round trip and a legacy reopen before promoting the first-view cue. Python-aware opt-in admission stays deferred until the end-to-end report can express the condition. The scope is the selected static import branch. The historical runtime and any maintainer-action change remain separate evidence questions. [Native applicability checkpoint](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_AND_QUALIFICATION_PLAN.md#16-combined-evidence-and-runtime-applicability-design-checkpoint)
