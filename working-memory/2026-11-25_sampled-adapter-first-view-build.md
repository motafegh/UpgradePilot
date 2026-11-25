# Show sampled adapter versions beside the paired outcome

Ali selected the renderer Build after the saved-view comparison. The existing conditional result could require a maintainer to open the detailed source records to identify the FastAPI and Starlette versions. Giving the exact sampled versions beside the result makes that assumption visible in Dashboard API and AV-Tracer, where the choice of adapter can change which arguments reach HTTPX. Learning remains in the separate workstream, with the six-part engineering handoff in chat. [Design comparison](2026-11-25_sampled-adapter-first-view-comparison.md) · [Dashboard API qualification](2026-11-25_dashboard-httpx-source-qualification.md)

- UP-SKILL:upgradepilot-build-implement
- UP-SKILL:upgradepilot-working-memory

## Build

Renderer 9 uses the same old and proposed witnesses the opening already admits. It follows their saved source IDs to retained dependency text explicitly marked as a constraint sample. The renderer compares the package, version, repository and revision identities across every displayed witness. One complete, shared set with at most one identity per package produces the sorted version line. Several modules from a single identity produce one label. Missing, incomplete or conflicting identity evidence leaves the cue absent. Existing display handling applies to the new line. The source and dispatch qualification follows immediately below it. [Renderer](../src/upgradepilot/report.py#L372) · [Witness projection](../src/upgradepilot/report_projection.py#L2175)

This is presentation over the current saved-report schema. The same renderer supplies fresh investigations, saved files and retained Workspace views. Sample identities, compared calls, rejection details, the independent historical CI excerpt and the saved action still come from the original evidence.

## Verification

The first focused run rejected the constructed controls at the saved-report validator. I had updated the witness references without mirroring them in their findings. I corrected the fixture so a finding and its assessment cite the same sources. The three focused tests then passed. The new saved-reader test covers a shared pair, deduplicated modules, an unrelated sample, version and revision disagreement, a shared set containing conflicting versions of the same package, missing metadata, a reference without retained text, and mixed call roots. It also checks the controlled live direct call, saved file bytes and abstain. [Regression test](../tests/test_caller_signature_delivery.py)

Built and installed a clean wheel offline using cached build and dependency wheels. All 120 installed product modules matched the candidate checkout byte for byte, and pip check passed. The experiment boundary check passed. The wheel SHA-256 is bf48517bf6440a118948ece47cfaaed8fd24e431b68db3abbad538b77092601d.

| Saved input | Installed report opening |
|---|---|
| Dashboard API #20 | Line 26 names FastAPI 0.165.0 and Starlette 1.10.0 beside the two conditional arguments-fit results. |
| AV-Tracer #11 source-only | Line 27 names FastAPI 0.104.1 and Starlette 0.27.0 beside the proposed-version rejection of app=. |
| AV-Tracer #11 source and CI | Same source cue. The independent job-log observation remains present. |
| Controlled direct call | The adapter line is absent. |

The four installed report outputs match the selected sketches after accounting for the renderer version. The three exact Workspace revisions match those openings and the prior Workspace output after accounting for the new line and renderer version. All five literal source views match their baseline bytes. All four saved inputs match their recorded digests. The displayed action remains abstain. These checks use fresh offline reader processes and retained evidence. [Frozen comparison](evidence/2026-11-25-sampled-adapter-first-view/comparison.json)

The ordinary OpenCV, MapProxy and Dashboard API report displays match renderer 8 after normalizing the renderer version in the header. Each keeps its saved abstention.

The first installed suite reported one harness failure. My `077` umask turned the Workspace test's intended `0755` directory into `0700`, so it exercised a valid private location. I corrected the test-process umask to `022` inside the owner-only verification directory and reran the affected check and the suite on the same wheel.

The full installed suite passed **1,199 tests with zero skips** in 249.698 seconds. It ran from the private checkout with only loopback available, as the normal user with namespace privileges dropped. [Build verification receipt](evidence/2026-11-25-sampled-adapter-first-view/build-verification.json)

## Handoff

The opening now answers which adapter sources the displayed result assumes. Which packages were installed, whether the affected code ran, and independent usefulness remain open. Dashboard API supplies the next bounded design case. Compare sample eligibility for that workflow's declared Python 3.10 with the existing selector. Keep an actual observed interpreter and a workflow declaration distinct, and preserve unknown eligibility where metadata is absent. The design comparison should establish the necessary evidence before changing source acquisition.
