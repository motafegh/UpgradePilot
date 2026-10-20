# Fresh Current CI diagnostic cohort — final report

Date: 2026-10-20

## Outcome

A three-case exposed real-world diagnostic cohort is now retained under `product-simulation/fresh-current-ci-diagnostic-2026-10-20/`. Three cases were sufficient; additional candidates were rejected or stopped once they no longer added a distinct diagnostic responsibility.

No product source code was modified.

## Admitted cases

### FCI001 — openai/openai-agents-python#5404 — mcp 2.0.0 -> 2.3.0

Classification: `qualified_for_current_ci_diagnostic`.

Why: the exact PR head has current GitHub Actions evidence with a non-empty runtime step array, and the selected `Release Readiness` workflow is an ordinary single-job shape with an explicit literal job display name. Under the current correlation owner's contract it is the best positive-path case.

Boundary: both user-defined steps were skipped for this Dependabot PR, and the transition is uv/lockfile shaped. This case can test acquisition/provenance/correlation identity but cannot establish installation or exercise of mcp 2.3.0.

### FCI002 — executablebooks/mdformat-footnote#50 — tox>=4.61.1 -> tox>=4.64.4

Classification: `qualified_as_unresolved_control`.

Why: current GitHub evidence contains rich non-empty steps for executed jobs and `steps: null` for two skipped publish jobs. The static workflow contains a test matrix, which the current correlation owner intentionally excludes.

Boundary: the observed workflow does not consume `requirements.txt` or invoke tox. The correct current result is refusal/unresolved correlation, plus no dependency-exercise claim.

### FCI003 — PasarGuard/panel#1044 — fastapi>=0.143.2 -> >=0.143.3

Classification: `qualified_as_unresolved_control`.

Why: five exact-head jobs have non-empty runtime steps and there is no matrix, but all static jobs lack an explicit literal job `name:`. This isolates the current owner's intentional static-job-name boundary.

Boundary: successful `make`-driven CI does not itself prove the exact FastAPI requirement was installed/exercised. The selected run payload also had an empty `pull_requests` array; that provider absence is retained rather than repaired by inference.

## Evidence actually retained

For every case the repository now preserves a manifest with frozen repository/PR/base/head/dependency transition/acquisition time, request identities, byte sizes, SHA-256 values and Git blob identities. Raw evidence is separate from review notes.

Retained evidence includes, where material:

- structured GitHub PR/run/job/step provider captures;
- exact-head run identity and exact run-attempt job capture;
- exact target-revision workflow source;
- exact provider PR diff used to establish the dependency transition;
- FCI002 base/head `requirements.txt`;
- FCI003 base/head `pyproject.toml`.

Logs/workflow artifacts were intentionally not retained because the current declared diagnostics consume workflow source plus run/job/step summaries; adding logs would increase size/security/privacy surface without changing the diagnostic claim.

## Capture-fidelity limitation

The available GitHub connector does not export the original HTTP response body and headers byte-for-byte. Provider API retention is therefore a structured provider capture of the fields exposed and used by this diagnostic path, not an HTTP-wire archive. Source/diff bytes retained as authoritative source artifacts are lossless. This limitation is explicit in every manifest.

## Verification and retention repair

Offline fresh-process replay passes with no target-repository network values. The retained Git objects were independently re-read from UpgradePilot and cross-checked against computed object identities.

Verification caught two cohort-construction defects before closure: FCI001 and FCI003's first manually persisted PR-diff reconstructions contained introduced spaces on blank diff-context lines. Those raw files were not overwritten. They remain marked non-authoritative, while additive `pr.provider-exact.diff` files now match the original captured bytes exactly and are the manifest-selected producer inputs. FCI002's first retained diff was exact.

This was a **cohort acquisition/retention defect in this capture procedure**, not evidence of a defect in `src/upgradepilot/`.

## Does anything already suggest an UpgradePilot acquisition/retention defect?

Not yet.

The fresh cases show that GitHub currently returns non-empty job step summaries for relevant public PR runs, so the historical glyphsLib empty-step limitation is not a universal current-provider condition. The two unresolved cases line up with explicit current correlation-contract exclusions (matrix expansion and missing static display names), not with proven acquisition failures.

FCI003's empty run-level `pull_requests` array is a provider wrinkle worth preserving, but current exact-head acquisition is anchored independently by the frozen PR head/query. It is not by itself a product defect.

A real product defect should be recorded only if the next diagnostic shows one of these separations failing: GitHub supplied the necessary evidence but UpgradePilot failed to retain it; retained evidence was correct but the current owner mishandled an admitted supported shape; or an unsupported relationship was guessed instead of staying unresolved.

## Best next current-CI diagnostic

Run the three cases through the current owners in this order:

1. **FCI001 positive path:** acquire/reconstruct from retained evidence, parse the workflow, and require a supported YAML↔runtime identity-correlation result without upgrading skipped steps into dependency execution.
2. **FCI002 refusal control:** require explicit unsupported/unresolved matrix handling; preserve `steps: null` separately from an empty list.
3. **FCI003 refusal control:** require explicit unsupported/unresolved handling for missing static job display names despite rich runtime steps.

That diagnostic should consume only retained case inputs first. Live GitHub may be compared later as a separate freshness observation, never as a hidden replay dependency.

## Claim boundary

This cohort is exposed development/diagnostic evidence. It says nothing by itself about general product reliability, unbiased generalization, or product acceptance. Any later qualification/generalization study requires a separately protected cohort that was not used to debug or design these paths.
