# Build the Python-ranked adapter opt-in

Applied `UP-SKILL:upgradepilot-build-implement` and `UP-SKILL:upgradepilot-working-memory`. This continues the [qualified ranked provider route](2026-11-26_ranked-adapter-provider-qualification.md) under the doing-only cadence. The milestone joins an early exact-head workflow declaration, bounded PyPI index ranking, an exact-release file check, and preserved report and Workspace evidence through the normal CLI. [Integration plan](../plans/CALLER_SIGNATURE_NATIVE_ADOPTION_AND_QUALIFICATION_PLAN.md#integration-after-the-bounded-route-qualification)

## Implementation

`--rank-adapter-samples` requires the existing workflow and job flags. It establishes the declared Python line at the exact PR head before any ranked index read. If that declaration is unavailable, the ranked branch stops with an explicit reason. Direct old/new source work remains independent. The unscoped profile preserves ordinary registry selection. The annotation-only profile continues reading its optional workflow after source work. [CLI](../src/upgradepilot/cli.py) · [Source acquisition composition](../src/upgradepilot/caller_signature/source_progress.py)

The ranked branch reads one bounded PyPI Simple JSON observation per package using the existing shared acquisition session. It preserves the response digest, serial, file count and observation time. For each visible adapter constraint it checks stable version groups in descending order, using the existing Python-line evaluator on exact non-yanked file declarations. A known overlap supports a candidate, while an unclassified in-scope release ahead of it prevents promotion. An exact release response must agree on the filename, SHA-256, Requires-Python text and yank state before repository provenance or source work starts. A missing or unadmitted exact file has its own unresolved reason. The checked scope and unclassifiable filename count remain visible. [PyPI Simple client](../src/upgradepilot/pypi/simple_index.py) · [Ranked selection and file join](../src/upgradepilot/caller_signature/sample_python.py)

Workspace source representation version 4 binds the workflow declaration, each checked constraint, its selection and exact release file join to the admitted source sample. Existing source representations remain readable. The first view shows joined ranks and whether their source was retained. The detailed evidence retains disagreements and joins, while saved readers reconstruct recorded decisions. The static proof still leaves actual resolver choice, installed versions, loaded backend and execution unknown. [Source codec](../src/upgradepilot/caller_signature/source_codec.py) · [Report projection](../src/upgradepilot/report_projection.py) · [Renderer](../src/upgradepilot/report.py)

## Discriminating proof

The installed CLI ran against the frozen Dashboard API provider responses from the previous qualification, with production ranking enabled through the public flags. The result used the same route as the ordinary source pipeline. Index time and report/revision IDs were created in each replay. No provider requests or target execution took place during this Build's qualification.

| Control | Result |
| --- | --- |
| Python 3.10 ranked | FastAPI 0.162.5 and Starlette 1.7.0 joined their exact published files after checking eight and four stable version groups respectively. Both tagged TestClient files and the HTTPX fallback explanation were retained. |
| Newer candidate metadata missing | FastAPI 0.165.0 became unclassified. The ranked branch made no request for the otherwise eligible FastAPI 0.162.5 exact release. |
| Exact release digest disagreement | The selected FastAPI wheel and its exact release response exposed different digests. The branch withheld that sample before any FastAPI repository read. |
| Wrong job and missing CLI scope | The wrong job made no Simple Index request. A ranked CLI invocation without the workflow and job flags returned input error 2. |
| Shared provider cap 50 | The session stopped at 50 physical requests. The already confirmed adapter file joins were retained, along with partial native comparison material. |
| Unscoped and annotation-only | Both kept FastAPI 0.165.0 and Starlette 1.10.0. Annotation still showed exclusion of the declared 3.10 line. Neither path fetched a Simple Index. |

The modified FastAPI controls used an explicit unavailable pytest response for the independent exploration slot reached after FastAPI did not qualify. The positive path charged 46 GitHub and 64 total provider requests with no stops, preserved the conditional old/new HTTPX comparison and retained action `abstain`. The current result establishes evidence fitness on the frozen example. The exact packages and backend loaded by the target remain unknown.

## Installed verification and handoff

The installed CLI reopened the ranked JSON report and Workspace with matching report bodies. It exposed the exact Starlette source bytes and the recorded PyPI index serial and fingerprint. The historical annotation-only checkpoint also reopened. The new and historical native source-family packets re-encoded to their exact stored bytes with provider access, ranking and Python analysis blocked. The offline-built wheel matched all 122 installed product modules to source. Package consistency and the experiment boundary check passed. **All 1,203 installed product tests passed with zero skips.** [Verification receipt](evidence/2026-11-27-ranked-python-adapter-sampling-build/verification.json)

One contrasting adapter-chain qualification can test whether the frozen workflow, ranking, source and report composition transfers to a materially different case. Compare the three modes and retain the evidence coverage and cost outcomes. The Dashboard case informed the method and remains development qualification.
