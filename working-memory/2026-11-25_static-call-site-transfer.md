# Static call-site comparison on VCRTool

This follow-up to the [first offline comparison](2026-11-24_static-api-tool-comparison.md) tests whether the smaller search result seen on AV-Tracer repeats on a separate real update. The [trial plan](../plans/UPSTREAM_API_CHANGE_AND_TARGET_EXPOSURE_FEASIBILITY_PLAN.md#static-api-and-call-site-tool-comparison) requires equivalent source access, preserved call findings and a repeated improvement before considering an adapter.

Ali authorized the follow-up with learning handled separately. We used the documented engineering and evidence checks in place of the interactive teaching gates. The trial started at UpgradePilot revision 26794fae65895c81b6c78c5075775ccdd3d4b1d7.

- UP-SKILL:upgradepilot-repository-audit
- UP-SKILL:upgradepilot-working-memory

## Case selection and freeze

Screened 22 public PRs. Seventeen exact-head source archives were readable. Four leads had incomplete transport responses and one crossed the archive cap. Other readable leads had constructor calls, including gh-mpyl and pdh. SQLFluff and Typer had explicit compatibility work. VCRTool provided a direct imported call, a small complete Python inventory, and an exact lockfile transition. The case is historical and fresh to this evaluation. We had already inspected its source to qualify it and set the expected result. The selection predates both analyzer outputs. [VCRTool PR #61](https://github.com/Tatsh/vcrtool/pull/61) · [Screen summary in the receipt](evidence/2026-11-25-static-call-site-transfer/result.json)

The maintainer question was whether the retained test fixture needs a constructor-call edit after Click removes the `mix_stderr` parameter. The PR changes the direct Click constraint from `^8.1.8` to `^8.2.0` and the lock from 8.1.8 to 8.2.0. All 14 tracked Python files have identical Git blobs at the PR base and head. We searched every one at the head. [Base lockfile](https://github.com/Tatsh/vcrtool/blob/2b6f313b427a224c7af089d741c65b6e9d96259d/poetry.lock) · [Proposed lockfile](https://github.com/Tatsh/vcrtool/blob/4193c3e9f8ec4d975f917b213fab3191c423e445/poetry.lock) · [Click 8.2 changelog](https://github.com/pallets/click/blob/219206a18666624072fdbb803901e5eb7ce575a1/CHANGES.rst)

The [manifest](evidence/2026-11-25-static-call-site-transfer/manifest.json) records revisions, Git tree and blob identities, byte lengths and SHA-256 values for the target packet, both Click definitions and the separate control. Both Click definitions were verified against GitHub's exact-revision contents records. The base archive exceeded the smaller retrieval cap used during verification, so only its two dependency declarations were fetched. A raw base `pyproject.toml` and the raw Click 8.1.8 definition arrived incomplete and failed the blob or native-parse checks. Size- and blob-verified GitHub responses replaced those captures before Griffe or Semgrep received the input. The [final freeze](evidence/2026-11-25-static-call-site-transfer/pre-run.sha256) binds the corrected manifest, [expectations](evidence/2026-11-25-static-call-site-transfer/expectations.json), [local Semgrep rule](evidence/2026-11-25-static-call-site-transfer/calls.yaml) and [constructed controls](evidence/2026-11-25-static-call-site-transfer/controls.txt).

## Observed result

| Search against the same 14 Python files | Candidates | Required site recovered | Local wall time |
|---|---:|---:|---:|
| ripgrep 14.1.0 | 1 matching line | 1 of 1 | 0.006 s |
| Semgrep 1.186.0 | 1 call span | 1 of 1 | 1.460 s |

Both searches found `tests/conftest.py:24`. Its runner fixture calls `CliRunner()` without arguments. An independent native scan of all 14 files found the same sole call with this name or with `click.testing.CliRunner` among its possible origins. The fixture's module-scope import provides the selected origin. Native analysis retains a delayed-global-read limitation, and under that import and ordinary constructor binding the call fits both retained signatures. There is no constructor edit required for this fixture on account of mix_stderr. [Target fixture](https://github.com/Tatsh/vcrtool/blob/4193c3e9f8ec4d975f917b213fab3191c423e445/tests/conftest.py#L23)

Griffe 2.4.1 compared the exact defining files as static text and found the removal of `mix_stderr` from `CliRunner.__init__`. That confirms the upstream change affects calls passing this keyword to the selected constructor. Runtime behavior, including stdout and stderr handling, is a separate question. [Click 8.1.8 definition](https://github.com/pallets/click/blob/934813e4d421071a1b3db3973c02fe2721359a6e/src/click/testing.py#L179) · [Click 8.2.0 definition](https://github.com/pallets/click/blob/219206a18666624072fdbb803901e5eb7ce575a1/src/click/testing.py#L240)

- The constructed call passing `mix_stderr` fit 8.1.8 and was rejected by the proposed signature. The old result recorded a named parameter and the proposed result recorded an unexpected keyword.
- Both searches surfaced the unrelated same-name call and the possibly unbound call. Neither produced a Click pairing. Semgrep dropped one text row for the synthetic local function definition, outside the real-source counts.
- With the real call held fixed, leaving receiver binding unresolved made both comparisons undetermined. With the proposed defining file absent, the old fit remained available and the proposed comparison stayed unresolved.

The raw captures and command receipts are retained privately. The [structured replay receipt](evidence/2026-11-25-static-call-site-transfer/result.json) records exact spans, control results, timings and raw output hashes. Both scans used an isolated network namespace, one local rule, no registry, metrics off, and no autofix. The standalone Semgrep version command stalled under isolation, so the final run read both versions from installed package metadata. Two fresh runs produced identical structured results after removing local timings. Native parsing and Semgrep covered every named Python file. Semgrep reported zero skipped files and zero errors. All 15 focused argument-analysis tests and the experiment boundary check passed.

## Replay the search

Obtain the exact-head source files and verify them against the manifest. Run from the extracted PR root with only the manifest's `python_inventory` paths in the shell array `FILES`, `LOCAL_RULE` set to the absolute path of the frozen YAML, and `TOOL_ENV` set to the separately provisioned pinned environment. Run the synthetic source separately by copying `controls.txt` as scenario.py.

~~~sh
unshare -Urn env -i PATH=/usr/bin:/bin rg --json --sort path -- '\bCliRunner\s*\(' "${FILES[@]}"
unshare -Urn env -i PATH=/usr/bin:/bin HOME="$PRIVATE_SCRATCH" \
  "$TOOL_ENV/bin/semgrep" scan --config "$LOCAL_RULE" --metrics off \
  --disable-version-check --no-git-ignore --disable-nosem --strict \
  --no-rewrite-rule-ids --verbose --json --jobs 1 -- "${FILES[@]}"
~~~

Use `extract_python_source` to match each Semgrep span to a native call and require the retained possible import before applying `compare_arguments` with the selected exact constructor and `one_receiver_assumed`. Leaving the receiver unresolved is a distinct check. Keep an absent defining source unresolved. The private rerun script uses the existing experiment invocation and coordinate helpers.

## Decision

The candidate reduction seen in AV-Tracer did not repeat on VCRTool. Keep native binding as the product path and retain Semgrep and Griffe as optional development diagnostics. A new measured search or evidence gap could justify reopening the comparison. The trial establishes source-level argument fit under the recorded premise. Installed versions, observed test outcomes and independent maintainer time remain unmeasured.
