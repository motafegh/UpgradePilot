# Controlled installer evidence trial

- [Selected trial plan](../plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md#follow-up-trial-for-target-installer-evidence)
- [Public screening](2026-11-24_target-installer-tag-evidence-screen.md)
- [Manual workflow run](https://github.com/motafegh/UpgradePilot/actions/runs/45444178025)
- UP-SKILL:upgradepilot-build-implement
- UP-SKILL:upgradepilot-working-memory

Ali selected the CI trial as the next execution step. The preceding roadmap and discussion supplied the outcome and evidence boundaries. Use a controlled UpgradePilot fixture with actual CI observations. A historical PR still needs its own environment evidence. Learning stays outside this trial increment.

## Fixture and proof boundary

- Base `ca774c64f0e8ca75fcb58414ed2ee30704bea1c9`, fixture head `c994d875b1f28ad192b47b72033f9bdc7c017beb`.
- The exact `requirements.txt` path changes NumPy `2.2.6` to `2.3.0`. The [diagnostic](../tools/target_installer_trial.py) feeds the exact Git patch and hash-bound public PyPI release bytes through the installed UpgradePilot dependency analyzer, release client and applicability evaluator. This is a controlled comparison rather than a historical PR investigation.
- The [manual workflow](../.github/workflows/target-installer-evidence-trial.yml) selects standard Ubuntu 24.04 x86-64, CPython `3.10.22` and `3.11.18`, and fresh pip `25.3` environments. The jobs collect the full `python -I -m pip --isolated debug --verbose` tag blocks, manifest and digests. NumPy itself is never installed. The verifier retains wheel matches and applicability states for the observed installer environment. It does not derive actual install, source build, affected behavior or action from the result.
- Published inventory hashes retained from the planning preflight are `c8f5ba0488e6785eb676ff66a43bbb810e511e0cfe8a018bb021c89c7f74f25c` for `2.2.6` and `01d309397a4ffff996f95f78a8d5957f9a26b6aa44863cf4a0b7a2bb560c6e75` for `2.3.0`. The separate `Requires-Python` shift from `>=3.10` to `>=3.11` is recorded as metadata. The target comparison uses full wheel inventories and complete actual tags.

## Preflight

Checked that the workflow is manual, read-only and uses full action commit pins. The capture script parses under Python 3.10 syntax. The current local pip tag block passed the parser. Constructed archives exercised both expected applicability outcomes and six refusals. The stored workflow run and raw archive receipts are private under `~/.local/share/upgradepilot/target-installer-ci-trial-20261124.EBYDQR36/`.

## Hosted and offline results

One manual dispatch returned run `45444178025`, attempt `1`. Both jobs succeeded at the frozen head. GitHub reported step `5` successful in each job. The offline verifier matched each archive digest and its manifest to the repository, head, run, attempt and exact job row. Each capture's observation time agreed with its step at the whole-second precision of GitHub's timestamp fields. Exactly two archives were downloaded. Both expanded within the 512 KiB limit.

| Environment | Job and artifact | Complete tags | Compatible old / proposed wheels | Applicability result |
|---|---|---:|---|---|
| CPython `3.10.22`, pip `25.3`, Ubuntu 24.04 image `20261116.376.1` | [Job 138623265785, step 5](https://github.com/motafegh/UpgradePilot/actions/runs/45444178025/job/138623265785#step:5:1), artifact `14944037653` | 910 | `manylinux_2_17` / none | `established_applicable` for loss of the published wheel path |
| CPython `3.11.18`, pip `25.3`, Ubuntu 24.04 image `20261116.133.1` | [Job 138623266346, step 5](https://github.com/motafegh/UpgradePilot/actions/runs/45444178025/job/138623266346#step:5:1), artifact `14945082692` | 989 | `manylinux_2_17` / `manylinux_2_28` | `established_not_applicable` for wheel-path loss in that observed environment |

Direct intersection against both full inventories agreed with the owner evaluator. The no-target-observation baseline remained `unresolved`. Six constructed controls derived from the hosted archives were rejected before evaluation. They exercised an absent artifact, incomplete tag block, oversized archive, incorrect revision, incorrect attempt and a swap across jobs. Each altered archive's digest was recomputed in its control metadata so the test reached identity or completeness checks rather than stopping at a mismatched byte hash.

- 3.10 archive SHA-256 `40d7fa7d42f0cd07dd2ec07cd8c37dcc2cc69880209902a2106a1cbac5fe5680`, tag block SHA-256 `9a40a2932a69c2f602407cdbe677e139908f12da8e28d516aa5f75a115085772`.
- 3.11 archive SHA-256 `856547aa2165b0190fbdb6a4bd7948a2e1c5aaf107d78738ef2deef640ba1991`, tag block SHA-256 `8a0abb68a5b5358bfaebcef57b91aab6d465570655874d29b8707b2ee1331f03`.
- Private `verification.json` SHA-256 `7e52c1d1def52612f2bc2ba3b7c2db8e79ac3cfbdd21cf19808205dec6dc5aa4`. Repeating verification in a fresh network-isolated process reproduced the receipt byte for byte. The hosted archives have one-day retention, with hash-bound copies preserved in the private proof directory.

The installed wheel passed all 27 focused artifact and investigation tests. The experiment boundary checker passed. Product runtime and report interfaces were outside this diagnostic. The simulated dependency transition and genuinely hosted installer observations qualify only the capture-to-evaluator path for the controlled fixture.

## Disposition

Accept the controlled evidence format and the offline diagnostic. An ordinary product adapter requires a real supported update with an equivalent artifact and a decision that needs it. OpenCV and FDApy retain unresolved target applicability. The [static API comparison](../plans/UPSTREAM_API_CHANGE_AND_TARGET_EXPOSURE_FEASIBILITY_PLAN.md#static-api-and-call-site-tool-comparison) is the next scoped trial.
