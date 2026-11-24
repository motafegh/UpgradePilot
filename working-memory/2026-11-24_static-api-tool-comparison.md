# Static API and call-site tool comparison

Dated engineering record for the [fixed-input experiment](../plans/UPSTREAM_API_CHANGE_AND_TARGET_EXPOSURE_FEASIBILITY_PLAN.md#static-api-and-call-site-tool-comparison) selected after the [controlled installer trial](2026-11-24_controlled-installer-evidence-trial.md).

## Pre-run freeze

The packet was reconstructed from the published AV-Tracer archive and the previously frozen glyphsLib source and selections. Every extracted source digest was checked. The [manifest](evidence/2026-11-24-static-api-tool-comparison/manifest.json) records the repositories, revisions, checkout-relative paths and content digests. The [required and forbidden findings](../experiments/static_api_tools/expectations.json) are separate from the [Semgrep rules](../experiments/static_api_tools/calls.yaml). The [pre-run checksums](evidence/2026-11-24-static-api-tool-comparison/pre-run.sha256) were recorded before either analyzer received case input.

Ali asked to handle learning in parallel with the audit and engineering work. This comparison uses direct experiment execution, validation and a dated handoff in place of the interactive Learning-by-Doing gates. The selected scope and evidence requirements still apply.

- Baseline project revision `64e2249fac3963ec38b5231163909ce1fe38fe02`.
- UP-SKILL:upgradepilot-repository-audit
- UP-SKILL:upgradepilot-build-implement
- UP-SKILL:upgradepilot-working-memory

## Method and coverage

The packet contains 36 retained files, including 32 Python files. AV-Tracer retains exact PR-head target files, sampled FastAPI 0.104.1 and Starlette 0.27.0 adapter definitions, and HTTPX 0.25.2 and 0.28.1 definition files. Its base revision is recorded in the expectations for provenance. The glyphsLib packet includes two PR-head test files, the base and head dependency declarations, and the same four selected pytest source paths for 9.0.2 and 9.0.3. The packet also includes one constructed same-name control.

UpgradePilot parsed all 32 retained Python files and the control and repeated the eight selected bindings. The lexical and Semgrep searches used the same explicit file lists and candidate names. The AV-Tracer search covered 10 target Python files, two adapter files and the control. The glyphsLib search covered the two target test files. Griffe read exact old and new declaration sources from the same packet. The reported call links reuse the documented AV-Tracer source chain and the frozen glyphsLib pairings. Span discovery leaves callable resolution with UpgradePilot. [AV-Tracer evidence](../examples/av-tracer/README.md) · [glyphsLib selection freeze](evidence/2026-10-28-caller-signature-second-real-case/freeze.json)

Griffe 2.4.1 and Semgrep 1.186.0 were installed in a separate environment from pinned wheels. The comparison and both analyzers ran inside a network namespace through `unshare -Urn`. The Griffe package-loader attempt disabled inspection and external alias resolution. The defining-file comparisons used Griffe's static visitor. Semgrep used one enabled local rule per case, with metrics, version checks and inline suppressions disabled. No target code, runtime dependency evidence, model call, remote rules, or autofix ran. The private evidence includes exact commands, raw outputs, all three attempt runners, wheel hashes and the installed-tool dependency freeze. The [result receipt](evidence/2026-11-24-static-api-tool-comparison/result.json) includes raw artifact digests and line-level evidence.

## Results

| Case | Existing UpgradePilot baseline | Griffe defining-file comparison | Lexical search | Semgrep plus native verification |
|---|---|---|---:|---:|
| AV-Tracer #11 | The target test's selected Starlette constructor fits. The sample forwarding call fits old HTTPX and is rejected on proposed HTTPX because of `app=`. | Found removed `app` and `proxies` parameters. The sampled forwarded call uses `app=` only. | 11 matching lines, 2 required sites | 3 call spans, 2 required sites |
| glyphsLib #1145 | The selected `pytest.raises` and `parametrize` calls fit both signatures under the frozen premises. The unresolved-receiver alternative stays undetermined. | No reported change on the two selected declarations. | 3 matching lines, 2 required sites | 3 call spans, 2 required sites |

AV-Tracer's cited path starts in [the target test](https://github.com/ivaronkun-Ahey/AV-Tracer/blob/25e7205f39103456e7efbc4e9f503f3debc7b5d8/backend/tests/test_app.py#L6), goes through the [FastAPI re-export](https://github.com/fastapi/fastapi/blob/7e5afe2cb9bf1fa30c04a4dd393ea397a46db29b/fastapi/testclient.py#L1), and reaches [Starlette's forwarding call](https://github.com/Kludex/starlette/blob/0c4b68ac4e179a788e38bac28f299dcad0f36e99/starlette/testclient.py#L399). The old HTTPX definition starts at line 620 and the proposed one at line 639. [Old declaration](https://github.com/encode/httpx/blob/cc206cf2dad42600479962ac1daaa44675cfaf56/httpx/_client.py#L620) · [Proposed declaration](https://github.com/encode/httpx/blob/26d48e0634e6ee9cdc0533996db289ce4b430177/httpx/_client.py#L639)

In AV-Tracer, Semgrep removed seven unneeded real-source rows and one unneeded control row from the lexical review set. The one remaining extra span was the synthetic `other.TestClient(...)` call. Both searches found it. Native analysis found no established HTTPX origin, and the span produced zero paired findings. For glyphsLib, both searches also found a second `parametrize` call at line 78 outside the frozen reviewed pair. Semgrep supplied no additional required relationship in either set. It scanned all 15 named files with zero skipped paths or parse errors.

- **Missing definition.** Removing the proposed HTTPX defining file made its comparison inconclusive. The runner did not fall back to the installed HTTPX dependency of the analyzer environment.
- **Unresolved receiver.** The glyphsLib decorator span still has an `undetermined` case, even though `ids` could enter the signature's variadic keywords.
- **Broader Griffe coverage.** The partial public HTTPX package comparison failed at a cyclic `httpx.__version__` alias and recorded 57 unresolved alias names in the old snapshot. The first direct load also failed to reach the selected submodules. Switching to the static file visitor loaded the definitions. A second attempt passed the functions as comparison roots and produced empty output because Griffe compares members of the supplied objects. The final attempt passed the owning class or module and kept only findings on the selected declarations. The frozen sources, case names, expectations and rule patterns stayed fixed. The final scan explicitly enabled only each case's corresponding rule to match the lexical query.

| Measured work | Wall time in the final run |
|---|---:|
| Existing parser and eight selected bindings, with the control | 2.140 s |
| Griffe process, including four attempted comparisons | 0.148 s |
| Lexical AV-Tracer / glyphsLib | 0.006 s / 0.005 s |
| Semgrep AV-Tracer / glyphsLib | 0.994 s / 1.008 s |

These are local process measurements for different operations. Lines and spans measure candidate review volume. Human time and independent usefulness were outside this experiment, as were ordinary evidence acquisition and target runtime applicability.

## Verification and replay

A fresh isolated run reproduced all six structured receipts after removing timings and sorting lexical results. The receipt check compared file coverage, exact four required call spans, eight binding outcomes, both removed HTTPX parameters and all three controls. The experiment boundary checker passed. All 141 relevant tests passed, with 119 caller/signature product tests and 22 experiment tests.

With the retained glyphsLib `sources.json` and `selections.json`, an installed project environment, and a separate tool environment provisioned from the [requirements](../experiments/static_api_tools/requirements.txt), run from the project root. Supply existing private parent directories and new paths for the packet and result.

```sh
sha256sum -c working-memory/evidence/2026-11-24-static-api-tool-comparison/pre-run.sha256
.venv/bin/python -I experiments/static_api_tools/prepare.py "$packet" "$glyph_inputs"
unshare -Urn env -i PATH=/usr/bin:/bin HOME="$proof_root" \
  "$PWD/.venv/bin/python" -I "$PWD/experiments/static_api_tools/compare.py" \
  "$packet" "$toolenv" "$trial_output"
```

## Decision

Keep native source binding as the product path. Retain Semgrep as a development diagnostic candidate for definition-heavy searches, based on the reduction in AV-Tracer. Keep Griffe's exact-definition comparison as a cross-check on supported captures. Across these two exposed cases neither added a verified material relationship to the existing results. If a separate, less-exposed real update presents a decision-relevant source search problem, freeze that case and repeat the candidate-volume comparison before considering an adapter.
