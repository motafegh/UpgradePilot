# B2 Gemma E4B Observed Evaluation Result

**Date:** 2026-07-28
**Operation:** Execute the current-stage LM Studio evidence request through its first stop condition
**Parent request:** [`2026-07-28_B2-current-stage-evidence-request.md`](2026-07-28_B2-current-stage-evidence-request.md)
**Raw evidence:** [`evidence/2026-07-28-gemma-e4b/`](evidence/2026-07-28-gemma-e4b/)
**Result classification:** Operational load passed; strict structure and grounding passed; semantic-state consistency failed; larger corpus not run

## Required summary

1. **Did Gemma E4B load successfully under the intended configuration?** Yes, after correcting one unsupported CLI flag in the written procedure. The actual model load then succeeded without a reported guardrail, OOM, CPU fallback, or instability.
2. **What configuration did LM Studio actually apply?** `gemma-4-e4b-it-ud`, identifier `upgradepilot-gemma-e4b-smoke`, context 4096, parallel 1, eval batch 2048, physical batch 512, Flash Attention enabled, KV cache on GPU, MTP speculative decoding disabled, simple speculative decoding disabled, and TTL 900 seconds.
3. **What was the real GPU and system-memory cost?** GPU use rose from 1392 MiB before load to 4759 MiB immediately after load, an observed increase of 3367 MiB. Free VRAM fell from 6627 MiB to 3260 MiB. WSL-visible system RAM remained approximately 1.9 GiB used with 49 GiB available. The CLI separately reported a 4.75 GiB model load. These measurements are different views and must not be collapsed into one inferred offload quantity.
4. **Did strict structured output work?** Structurally yes. The outer response parsed, the inner content parsed, all required fields were present, no unknown fields appeared, and the finish reason was `stop`. Semantically the smoke failed because the model returned `state: unresolved` for an explicit resolved fix claim while returning no unresolved reasons.
5. **Did exact source grounding work?** Yes. The source quotation exactly and contiguously matched the supplied sentence.
6. **Did the model distinguish added, dropped, deprecated, removed, and future removal correctly?** Not tested. The clean smoke failure activated the request's stop condition before the differentiation corpus.
7. **Did it resist instruction-shaped release text?** Not tested for the same reason.
8. **Did repeated decision-critical cases remain stable?** Not tested for the same reason.
9. **What did it extract from the real pytest release body?** Not tested. The exact GitHub Release was reacquired and preserved only as prospective source evidence; it was not sent to the model after the smoke failure.
10. **Did any error materially change the meaning a deterministic decision layer would receive?** Yes. The extracted claim itself correctly represented the fix, but the overall `unresolved` state would require the later deterministic layer to reject or abstain instead of accepting a resolved claim set. The inconsistency is fail-safe under the diagnostic validator but fails the selected smoke gate.
11. **Was the model explicitly unloaded and was the baseline restored?** Yes. LM Studio confirmed the exact identifier was unloaded. Native and CLI inspection then reported no loaded model. GPU use was 1175 MiB with 6844 MiB free after unload.
12. **What limitations or uncertainties remain?** Actual offloaded-layer count was not reported; reasoning was active in the response despite no explicit reasoning-mode load control; first-token latency was unavailable from the non-streaming API response but appeared in LM Studio stats; the semantic corpus and repetitions remain unexecuted; one clean case cannot establish model suitability.

## Baseline and local boundary

Observed before the load:

```text
LM Studio CLI commit: 71bd99c
server: ON, port 12345
listener: 127.0.0.1 only
unauthenticated loopback model inventory request: accepted
loaded models: none
GPU: NVIDIA GeForce RTX 3070 Laptop GPU, driver 610.74
GPU memory: 8192 MiB total, 1392 MiB used, 6627 MiB free
system memory: 50 GiB total, about 49 GiB available
```

The LM Studio server remained loopback-only. No CORS, bind, firewall, authentication, download, or network-exposure setting was changed.

## Load-control correction

The first exact invocation preserved in `load-output.txt` was rejected before loading because the installed CLI does not recognize:

```text
--no-speculative-draft-simple
```

The installed `lms load --help` exposes the positive opt-in `--speculative-draft-simple` flag but no matching negative flag. The corrected invocation therefore:

- retained the supported `--no-speculative-draft-mtp` flag;
- omitted the unsupported simple-speculative flag;
- left every other frozen control unchanged.

Native applied configuration later reported both `speculative_draft_mtp: false` and `speculative_draft_simple: false`. This was a command-surface correction, not a load-configuration experiment.

The corrected load succeeded. LM Studio reported:

```text
Model loaded successfully in 1m 1.09s.
(4.75 GiB)
identifier: upgradepilot-gemma-e4b-smoke
```

## Applied configuration and observed resources

Native `/api/v1/models` reported:

```text
model key: gemma-4-e4b-it-ud
display name: Gemma 4 E4B Instruct UD
architecture: gemma4
parameters: 7.5B
quantization: Q4_K_XL, 4 bits per weight
file size: 5101713792 bytes
instance: upgradepilot-gemma-e4b-smoke
context length: 4096
eval batch: 2048
physical batch: 512
parallel: 1
Flash Attention: true
KV cache offloaded to GPU: true
MTP speculative decoding: false
simple speculative decoding: false
remaining TTL at first inspection: 887 seconds
```

The CLI request was `--gpu max`, and neither CLI nor native evidence reported fallback. The inspected endpoints did not expose an actual layer-offload count, so this record does not claim that count.

| Point | GPU used | GPU free | GPU temp | WSL-visible RAM used |
|---|---:|---:|---:|---:|
| Before load | 1392 MiB | 6627 MiB | 51 C | 1.9 GiB |
| After load | 4759 MiB | 3260 MiB | 53 C | 1.9 GiB |
| After smoke | 4792 MiB | 3227 MiB | 54 C | 1.9 GiB |
| After unload | 1175 MiB | 6844 MiB | 54 C | 1.9 GiB |

No crash, restart, UI instability, OOM message, or automatic fallback was observed through the available command and resource evidence.

## Strict smoke result

Input:

```text
This release fixes a crash when parsing empty configuration files.
```

The raw request, schema, outer response, parsed inner JSON, prompt hashes, and validation result are preserved under:

```text
working-memory/evidence/2026-07-28-gemma-e4b/runs/A_clear_fix__r0/
```

Observed structured content:

```json
{
  "state": "unresolved",
  "claims": [
    {
      "category": "fix_or_remediation",
      "subject": "crash when parsing empty configuration files",
      "change_state": "fixed",
      "source_quote": "This release fixes a crash when parsing empty configuration files."
    }
  ],
  "unresolved_reasons": []
}
```

Observed response metadata:

```text
finish reason: stop
client-observed total latency: 6.208829 seconds
LM Studio stats total time: 6.722337 seconds
LM Studio stats first token: 0.769799 seconds
prompt tokens: 192
completion tokens: 381
reasoning tokens: 277
total tokens: 573
```

Classification by layer:

| Layer | Result |
|---|---|
| Load and runtime | pass |
| Transport | pass |
| Authentication boundary | pass for the current loopback request |
| Outer response parsing | pass |
| Inner JSON parsing | pass |
| JSON field/schema shape | pass |
| Finish/truncation | pass |
| Exact source grounding | pass |
| Claim category | pass |
| Claim direction/state | pass |
| Overall semantic state | **fail** |
| Internal state/reason consistency | **fail** |

`state: unresolved` conflicts with the explicit grounded fix claim and the empty `unresolved_reasons` list. JSON-Schema-constrained generation enforced the field shape and enums but did not establish the cross-field semantic invariant.

## Stop condition and unexecuted work

The semantic-state failure activated the current-stage stop condition. Therefore the harness did not send:

- the ten-case differentiation corpus beyond the duplicate clear-fix smoke;
- the instruction-shaped case;
- any critical repetitions;
- the pytest 9.0.3 release body;
- Qwen 3.5 9B or Gemma 12B requests;
- Instructor requests;
- product integration requests.

The pytest 9.0.3 release and tag-reference JSON were reacquired from the exact public GitHub endpoints and preserved as source artifacts, but they were not model inputs.

## Evidence-backed continuation proposal

Do not reject Gemma E4B solely for operational fit: the observed deployment was stable, structured output worked, and the substantive fix claim was correctly grounded.

Do not admit it to the broader corpus yet: it failed the clean semantic-state gate.

The next bounded question should be whether the extraction contract can make these cross-field alternatives explicit and enforceable:

```text
resolved → one or more grounded claims + no unresolved reasons
no_decision_relevant_claim → no claims + no unresolved reasons
unresolved → no accepted claims + one or more unresolved reasons
conflicting → conflicting grounded claims + one or more conflict reasons
```

Compare one stronger schema branch/conditional representation with the current post-validation baseline. Then rerun only the same clear-fix smoke under the identical model and load configuration. Do not change model, offload, context, temperature, seed, prompt purpose, or client at the same time.

This proposal is not model adoption or product-contract approval. It is the smallest diagnostic needed to distinguish a weak contract from a weak model.

## Raw artifact map

- `load-output.txt` — preserved rejected invocation with the unsupported flag.
- `load-output-corrected.txt` — complete corrected load progress and final result.
- `lms-load-help.txt` — installed CLI load options.
- `server-listener.json` — loopback listener evidence.
- `snapshots/pre-load/` — baseline CLI, model inventory, GPU, and RAM evidence.
- `snapshots/post-load/` — applied model and resource evidence.
- `runs/A_clear_fix__r0/` — exact smoke request, source, raw response, parsed content, and validation.
- `logs/` — filtered model input, output, and prediction statistics.
- `snapshots/post-smoke/` — post-inference model and resource evidence.
- `unload-output.txt` — exact unload confirmation.
- `snapshots/post-unload/` — restoration evidence.
- `source/` — frozen exact pytest release and tag-reference evidence; not sent to the model.
- `evaluate.py` — diagnostic harness; not active product source.
