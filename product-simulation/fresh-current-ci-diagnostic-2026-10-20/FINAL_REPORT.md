# Fresh Current CI diagnostic cohort — final report

Date: 2026-10-20

## Outcome

A three-case exposed real-world diagnostic cohort is retained under `product-simulation/fresh-current-ci-diagnostic-2026-10-20/`. Three cases were sufficient; additional candidates were rejected or stopped once they no longer added a distinct diagnostic responsibility.

No product source code was modified.

A post-closure audit found and repaired additional **cohort-retention** defects and one semantic-description error. The corrected manifests, provider-exact source overlays, verifier and replay record supersede the earlier same-day closure where those defects were not yet detected.

## Admitted cases

### FCI001 — openai/openai-agents-python#5404 — mcp 2.0.0 -> 2.3.0

Classification: `qualified_for_current_ci_diagnostic`.

Why: the exact PR head has current GitHub Actions evidence with a non-empty runtime step array, and the selected `Release Readiness` workflow is an ordinary single-job shape with an explicit literal job display name. Under the current correlation owner's contract it is the positive-path case.

Boundary: both user-defined steps were skipped for this Dependabot PR, and the transition is uv/lockfile shaped. This case can test acquisition/provenance/correlation identity but cannot establish installation or exercise of mcp 2.3.0.

### FCI002 — executablebooks/mdformat-footnote#50 — tox>=4.61.1 -> tox>=4.64.4

Classification: `qualified_as_unresolved_control`.

Why: current GitHub evidence contains rich non-empty steps for executed jobs and `steps: null` for two skipped publish jobs. The workflow contains both unnamed static jobs and a later matrix test job. Under the current correlation owner's actual validation order the **first** expected refusal is `static_job_name_missing` on `pre-commit`; the matrix remains independently unsupported as a secondary shape.

Boundary: the observed workflow does not consume `requirements.txt` or invoke tox. The correct current result is refusal/unresolved correlation plus no dependency-exercise claim.

### FCI003 — PasarGuard/panel#1044 — fastapi>=0.143.2 -> >=0.143.3

Classification: `qualified_as_unresolved_control`.

Why: five exact-head jobs have non-empty runtime steps and there is no matrix, but all static jobs lack an explicit literal job `name:`. This isolates the current owner's intentional static-job-name boundary.

Boundary: successful `make`-driven CI does not itself prove the exact FastAPI requirement was installed/exercised. The selected run payload also had an empty `pull_requests` array; that provider absence is retained rather than repaired by inference.

## Evidence actually retained

For every case the repository preserves a manifest with frozen repository/PR/base/head/dependency transition/acquisition time, request identities, byte sizes, SHA-256 values and Git blob identities. Raw evidence is separate from review notes.

Retained evidence includes, where material:

- structured GitHub PR/run/job/step provider captures;
- exact-head run identity and exact run-attempt job capture;
- provider-exact target-revision workflow source;
- provider-exact PR diff used to establish the dependency transition;
- FCI002 provider-exact base/head `requirements.txt`;
- FCI003 exact base/head `pyproject.toml`.

Previously published flawed raw objects were not overwritten. They remain immutable and explicitly non-authoritative; additive exact overlays are selected by the manifests.

Logs/workflow artifacts were intentionally not retained because the current declared diagnostics consume workflow source plus run/job/step summaries; adding logs would increase size/security/privacy surface without changing the diagnostic claim.

## Capture-fidelity limitation

The available GitHub connector does not export the original HTTP response body and headers byte-for-byte. Provider API retention is therefore a structured provider capture of the fields exposed and used by this diagnostic path, not an HTTP-wire archive.

For repository source and authoritative diff artifacts, byte fidelity is separately protected with byte size, SHA-256 and Git object identity. The corrected FCI001/FCI002 provider-exact source overlays have Git blob IDs identical to the frozen upstream source objects.

## Verification and retention repairs

Corrected offline fresh-process replay passes with no target-repository network values.

Verification found two classes of cohort-construction defect:

1. FCI001 and FCI003's first manually persisted PR-diff reconstructions introduced spaces on blank diff-context lines. The original raw files remain preserved/non-authoritative; additive `pr.provider-exact.diff` files are authoritative.
2. A later audit found that the first FCI001 workflow copy and the first FCI002 workflow/base/head requirements copies lost their final newline during connector-to-text persistence. Those copies were internally self-consistent, which is why the earlier replay did not detect the problem. Additive `*.provider-exact.*` source overlays now match the frozen upstream Git blobs exactly.

The verifier now checks recorded upstream Git object identities rather than treating self-consistent retained hashes as sufficient proof of upstream byte fidelity.

These were **cohort acquisition/retention defects in this capture procedure**, not evidence of a defect in `src/upgradepilot/`.

## Does anything already suggest an UpgradePilot acquisition/retention defect?

Not yet.

The fresh cases show that GitHub currently returns non-empty job step summaries for relevant public PR runs, so the historical glyphsLib empty-step limitation is not a universal current-provider condition. The unresolved controls line up with explicit current correlation-contract exclusions rather than proven acquisition failures.

FCI003's empty run-level `pull_requests` array is a provider wrinkle worth preserving, but current exact-head acquisition is anchored independently by the frozen PR head/query. It is not by itself a product defect.

A real product defect should be recorded only if the next diagnostic shows one of these separations failing: GitHub supplied the necessary evidence but UpgradePilot failed to retain it; retained evidence was correct but the current owner mishandled an admitted supported shape; or an unsupported relationship was guessed instead of staying unresolved.

## Best next current-CI diagnostic

Run the three cases through the current owners in this order:

1. **FCI001 positive path:** reconstruct from retained evidence, parse the provider-exact workflow, and require a supported YAML↔runtime identity-correlation result without upgrading skipped steps into dependency execution.
2. **FCI002 refusal control:** require `static_job_name_missing` as the first unsupported/unresolved result; preserve `steps: null` separately from an empty list. Also retain the later matrix as a secondary unsupported static shape.
3. **FCI003 refusal control:** require explicit unsupported/unresolved handling for missing static job display names despite rich runtime steps.

That diagnostic should consume only retained case inputs first. Live GitHub may be compared later as a separate freshness observation, never as a hidden replay dependency.

## Claim boundary

This cohort is exposed development/diagnostic evidence. It says nothing by itself about general product reliability, unbiased generalization, or product acceptance. Any later qualification/generalization study requires a separately protected cohort that was not used to debug or design these paths.
