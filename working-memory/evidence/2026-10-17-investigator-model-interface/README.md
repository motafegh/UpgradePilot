# Actual deployment and model-interface evidence

The [active cycle](../../2026-10-16_2247_investigator-deployment-and-model-interface-qualification_lbd-cycle.md)
owns dated progression; [MEMORY](../../../MEMORY.md) alone owns live position. The
[qualification guide](../../../experiments/INVESTIGATOR_MODEL_INTERFACE_QUALIFICATION.md)
explains the real transport/reference/budget boundary.

- [Preflight](preflight.json) records fresh asset identity, measured request fit and proof limits.
- [Execution freeze r3](canary-freeze-r3.json) freezes two deployments, eight independent
  canary assignments/order, at most 48 calls and exact profile/code/asset/runtime identities.
  Later semantic comparison is explicitly unactivated. [r1](canary-freeze-r1.json) is retained
  as an unexecuted pre-inference freeze; [r2](canary-freeze-r2.json) completes repository/SDK/runtime provenance, and r3 adds the tested fresh-load actual-GGUF/backend placement guard. Neither earlier freeze ran.
- Durable owner-only retention root:
  `/home/motafeq/.local/share/upgradepilot/investigator-runs/deployment-interface-2026-10-16-r1`.
  It contains the initial SDK load/configuration, failed `gemma-preflight-a`, corrected
  earlier `gemma-preflight-b`/`qwen-preflight-a`, final `gemma-preflight-c`/`qwen-preflight-b`
  profiles/renderings/packed requests/backend template files/source snapshots, exact SDK
  copy, full asset/metadata inventory and hashing script, mechanical regression and telemetry.
  Earlier artifacts are preserved; the final rendering/tokenization/preparation code matches the profiles. The later r3 post-load guard is separately bound and tested, with AST correspondence retained.
- The original SDK source files were copied intact from ignored `.tmp/api-eval-sdk` into
  `sdk-1.5.0`; new commands select its `lib/python3.12/site-packages` via `--sdk-site`.
  No project dependency or product source changed. Pinned Ruff 0.17.1 tooling/wheel and its
  hash are retained outside the project after the previous `/tmp` tool disappeared.

The final Gemma preflight measured 12 shapes, 1,817–22,460 input tokens; Qwen measured
12, 1,706–22,280. Initial profile maxima differed by a few tokens because fresh lifecycle
IDs are tokenized too; every actual request is remeasured. The 256 margin exceeds this
observed variation. Worst final input + 8192 reserve + 256 margin = 30,908 within 32,768.
This justifies the declared envelope, not a globally optimal context/offload setting.

Full fresh hashes resolve Gemma weight plus projector separately and confirm the selected
Qwen file. Profiles retain actual requested/applied load records and backend flags. Flash
attention remains requested/reported true versus backend `auto`; no kernel-choice claim.
The first failed preparation was a server-schema mismatch: loaded template omitted
`stopStrings`, required for explicit prediction. The corrected freeze declares no extra
stop strings and keeps the original load response unchanged. No inference occurred during
preparation, including the failed attempt. Unreported reasoning usage remains unknown.

Pre-batch proof: 24 experiment controls, 65 nearest product tests, four real retained-input
mechanical assignments (zero model calls), touched Ruff/check/format and 96-file import
direction pass. Full product/installed/hosted suites were not rerun for experiment-only code.
The previous mechanical cycle's proof remains historical and bounded; it is CLOSED through E.

Actual preparation command form (six named loads/unloads in total, no predictions):

```sh
PYTHONPATH=src:. .venv/bin/python -m experiments.qualify_investigator_model_interface \
  --sdk-site /home/motafeq/.local/share/upgradepilot/investigator-runs/deployment-interface-2026-10-16-r1/sdk-1.5.0/lib/python3.12/site-packages \
  --model google/gemma-4-12b --identifier up-investigator-qualified-gemma12 \
  --load-config /home/motafeq/.local/share/upgradepilot/investigator-runs/deployment-interface-2026-10-16-r1/gemma-requested-load.json \
  --output /absolute/new-owner-only-preparation-directory
```

Qwen uses key `qwen3.8-27b-ud`, owned identifier `up-investigator-qualified-qwen38` and
`qwen-requested-load.json`. Execution requires the retained r3 freeze's exact SHA256 and
another new output directory; no placeholder manifest is admitted. Read-only GPU/Windows
host-memory telemetry samples machine allocation at about 1s/5s, not continuous or
process-exclusive peaks. Exact visible response originals, applied configuration, usage,
failed attempts, emitted events and final reports are retained separately from review.

A backend process command-line inspection unexpectedly exposed an internal ephemeral
credential in tool output. It was not used or retained; the owned initial instance was
unloaded. Later process inspection emits only allowlisted settings. Do not copy entire
backend command lines or full server logs into evidence. Local owner-only retention is
not off-machine backup, and no hidden reasoning content is retained.

The r3 post-load guard is a pre-inference source correction: it validates the actual backend
model file, placement/cache/template and model identity against inspected profiles. Source
snapshots/AST correspondence establish unchanged preparation/rendering/tokenization/fixtures;
only execution guarding changed. Current execution source is additionally retained in
`execution-code/`. No profile or model output was silently relabeled.

## Actual first result and revised bounded freeze

[r3 result](canary-r3-result.json) retains five attempted calls: Gemma stopped on a verified
automatic-BOS prompt-count mismatch; Qwen's exact prompt counts matched, but visible outputs
failed the wire and exhausted corrections. Totals are 10,676 input,72 target generated and
36 additionally reported Qwen draft tokens. No configuration qualifies and no semantic case
ran in r3. Native MTP was already present in Qwen's frozen raw load record; it is not a proved
cause of its output failure. All original outputs remain rejected in private retention.

[Revised preflight](revision-r4.json) and [r4 freeze](canary-freeze-r4.json) bind verified
actual BOS spelling/id and runtime JSON grammar from the existing offered contracts. No
old output is repaired. Five-call sequences preserve all plan gate responsibilities while
defering separate model note/readback probes:40 new maximum+5 spent=45 within the original48.
Actual source_id/path arguments in synthetic instructions are now explicit. Final profiles
are `gemma-preflight-r4b`/`qwen-preflight-r4b`; earlier r4 profiles remain retained. Current
CLI preparation additionally requires the retained `gemma-tokenizer-policy.json` or
`qwen-tokenizer-policy.json` via `--tokenizer-policy`. The schema/BOS preflight produced no
new predictions; only execution under the exact r4 hash is admitted. Final focused controls
are26; product source and the earlier65-test proof horizon are unchanged.

## Final interrupted-run disposition and retention verification

[Actual scalar results](actual-results.json), [separate interruption reconciliation](reconciled-interrupted-r4.json)
and [final verification](verification.json) preserve the outcome without overwriting any
original request/response/receipt. There was no original final `canary-r4/summary.json`;
`canary-r4/reconciled-summary.json` is explicitly a later reconciliation. No qualifier or
sampler process remained, and both core models were observed unloaded; no run was restarted.

Gemma is withheld for skipping the empty read despite a completed valid cited report.
Qwen passed structured/short, then raw/short report call5 terminated with unknown usage;
its long sequences are withheld. This interruption does not diagnose model semantic
quality. Total19 attempted calls are below48: known reported44,124 input/2,443 target
generated plus1,551 additional draft tokens, with one call's usage unknown. Native versus
client timing for Qwen's completed report differs(657.84s versus603.08s); preserve both,
without inferring a precise ranking. Actual near-envelope model inference remains unproved.

The interrupted report prefix was unavailable because the old binding retained text only
on success. The repaired source now writes visible fragments before completion and filters
reasoning before persistence. Its discriminating interruption test proves prefix retention,
no hidden-text retention, no partial-response salvage and unknown-usage blocking. All27
focused controls,65 nearest product tests and four final offline retained-input scripts
pass. No live prediction was made after the repair; old freezes refuse its changed code.
Future inference needs a fresh explicit freeze/re-entry, never selective replay of r4.

All consequential private files are indexed by `retention-index.json` under the durable
root, including the exact preserved SDK, source snapshots, original outputs/failed
receipts, rendered inputs, current retention repair, preparation scripts/metadata,
mechanical regressions and sampled telemetry. Owner-only modes and hashes are validated;
public `retention.json` points to the private index without publishing bodies. Model
weights remain at their recorded durable `/mnt/f/LLM/` paths. Local retention is not
off-machine backup. The current cycle remains at B/Verification with both deployments
withheld; its D/E and later semantic comparison are not silently completed.
