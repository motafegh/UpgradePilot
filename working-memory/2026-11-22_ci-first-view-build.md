# CI first-view Build

- **Starting revision:** `90601aa156913ed12afe683f27e15fe64990a185`
- [Offline design comparison](2026-11-22_ci-first-view-comparison.md)
- UP-SKILL:upgradepilot-build-implement
- UP-SKILL:upgradepilot-working-memory

Ali selected the bounded implementation. Learning stays in the parallel workstream. The report renderer owns the concise view over an existing record. CI owners still establish execution and package state, and the saved record and action contracts still own their respective meanings.

## Implementation and proof

The [first-view renderer](../src/upgradepilot/report.py) admits a single recorded successful attempt. It binds each supported command to its run, attempt, source job index, instance kind and expansion slot, then checks the exact job, head and recorded step in the same saved source. It uses the retained command span to extract the admitted command from a multi-command script. The job candidate counts check completeness before the renderer groups a shared command and manager-environment limit. The preview shows up to eight jobs, with remaining jobs and detailed evidence available below. ApplyPilot and cases with conflicting, absent or mixed proof continue to render their detailed records.

The report generator and saved codec stay at their existing versions. Renderer version 6 identifies the new human view. Action synthesis, evidence producers, and source access continue to use their existing records.

- **39 focused matrix/runtime and report tests passed.** The added projection/round-trip check uses the retained MapProxy fixture and preserves both the scoped commands and unchanged command-state detail. Omitted attempt step rows and the mixed matrix case both withhold the opening.
- All seven affected experiment presentation tests passed. The experiment dependency-boundary check passed. A separate controlled case shifted the run and job IDs and verified that the summary followed the supplied identities.
- The candidate wheel was built and installed offline using cached build and dependency wheels. `pip check` passed, and all 120 installed product modules matched the candidate. Candidate product/test patch SHA-256 `c4396b4bee2d61abd13e25b502fe44387499117e3bffa2e74d52e97df9362a7f`. Wheel SHA-256 `da0d7fa69a620e32fc30ff59bdc67eb72d8f8ba07950936bf154d61a455a2f6b`.
- Fresh offline opens compared five saved reports against renderer 5. MapProxy gained the opening. Its detailed text and selected facts matched the previous render after accounting for the new opening and renderer version. ApplyPilot, explicit-skip, missing-install, and the older October HTTPX report retained their detailed text apart from the renderer version. All four selected-facts outputs matched byte-for-byte. The MapProxy opening SHA-256 is `b7d7c23386dfb8223c20402ac9ac35ca50083b87c7f079d3f41518335f795fc9`. [Matrix acceptance evidence](evidence/2026-11-21-matrix-final-acceptance/RESULTS.md)
- The installed console replayed all 16 frozen MapProxy transport responses under an offline request guard. It saved and rendered the expected seven-observation overview, preserved `abstain` and the detailed report, and reopened the exact run/job facts through `--show-facts source-4`. The console comparison accounts for the save-confirmation footer and generated identity/timestamps. Saved replay SHA-256 `c1a5e6efb467d2d565c59087aad237dee23c639977641e7193686969cc67990d`.
- **All 1,192 product tests passed with zero skips** on the clean installed wheel, under loopback-only network isolation as the normal user. Full regression log SHA-256 `aea369a910c7838e458e30ee356e419e41d0c69d50d013a6ecda471a74feb5d1`.

The verification establishes rendering fidelity and the exact saved-source route. Independent usefulness, elapsed-time improvement, and generalized failure summaries remain separate.
