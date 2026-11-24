# External tool trials planning

- **Base revision** `6ca47a010d80d2f5605915fae982915d950ced80`
- [Target evidence screening](2026-11-24_target-installer-tag-evidence-screen.md)
- [Target installer evidence trial](../plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md#follow-up-trial-for-target-installer-evidence)
- [Static API tool comparison](../plans/UPSTREAM_API_CHANGE_AND_TARGET_EXPOSURE_FEASIBILITY_PLAN.md#static-api-and-call-site-tool-comparison)
- UP-SKILL:upgradepilot-planning-design
- UP-SKILL:upgradepilot-working-memory

Ali selected the two initial comparisons from the tool discussion. The existing plans now own the trial procedures and adoption gates. Keep their results separate. The CI trial tests acquiring evidence. The API trial tests finding a relevant relationship within evidence already available. Learning stays outside this planning increment.

The fixture preflight checked bounded public PyPI release JSON and parsed wheel filenames offline. NumPy `2.2.6` has Linux x86-64 `manylinux_2_17` wheels for CPython 3.10 and 3.11. The proposed `2.3.0` inventory has no matching CPython 3.10 wheel and its CPython 3.11 Linux x86-64 wheel uses `manylinux_2_28`. The initial common-platform-tag probe missed that replacement, so the trial requires complete live installer tags from a runner supporting both platform levels. The metadata also raises `Requires-Python` from `>=3.10` to `>=3.11`. The release payload SHA-256 values are `c8f5ba0488e6785eb676ff66a43bbb810e511e0cfe8a018bb021c89c7f74f25c` and `01d309397a4ffff996f95f78a8d5957f9a26b6aa44863cf4a0b7a2bb560c6e75`, respectively. These preliminary file checks do not qualify a target environment.

Verified the published AV-Tracer archive digest and both report entries by reading the ZIP as data. The prior glyphsLib evidence record supplies the distinct compatible and unresolved cases for the comparison. Freeze the actual selected source bytes before running either tool. Private preliminary metadata is in `~/.local/share/upgradepilot/external-tool-trials-plan-20261124.s7YFoHnR/`.

Planning is complete. Select the controlled CI evidence capture first because it tests the previously missing observation. The source comparison can use the retained cases in a separate run. No workflow, experiment dependency, third-party analyzer run or product adapter was added in this increment.
