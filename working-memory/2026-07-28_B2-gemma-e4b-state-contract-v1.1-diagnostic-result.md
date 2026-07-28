# B2 Gemma E4B State-Contract v1.1 Diagnostic Result

**Date:** 2026-07-28
**Operation:** Execute the selected prompt-state diagnostic through Gate A and the first Gate B stop condition
**Selected diagnostic:** [`2026-07-28_B2-gemma-e4b-smoke-review-and-state-contract-diagnostic.md`](2026-07-28_B2-gemma-e4b-smoke-review-and-state-contract-diagnostic.md)
**Prior observed result:** [`2026-07-28_B2-gemma-e4b-observed-evaluation-result.md`](2026-07-28_B2-gemma-e4b-observed-evaluation-result.md)
**Raw evidence:** [`evidence/2026-07-28-gemma-e4b-state-contract-v1.1/`](evidence/2026-07-28-gemma-e4b-state-contract-v1.1/)
**Result classification:** Gate A passed 3/3; Gate B no-claim passed; ambiguity failed; conflict case not run; broader corpus remains blocked

## Compact result

```text
operational load: passed
frozen variable comparison: passed
Gate A clear fix: 3/3 passed
Gate B no relevant claim: passed
Gate B ambiguity: failed
Gate B conflict: not run due stop condition
structure and cross-field invariants: passed for every returned response
restoration: passed
```

The explicit four-state prompt corrected the original clean clear-fix state-selection failure. It did not establish the complete four-state semantic boundary.

## Frozen diagnostic change

The diagnostic reused the first observed-run harness and flat schema. It changed only:

1. the system prompt gained explicit meanings and claims/reasons relationships for `resolved`, `no_decision_relevant_claim`, `unresolved`, and `conflicting`;
2. deterministic validation gained the corresponding state/claims/reasons invariant.

The exact v1.1 prompt addition is preserved in:

```text
working-memory/evidence/2026-07-28-gemma-e4b-state-contract-v1.1/state-contract-v1.1-addition.txt
```

The canonical schema hash remained:

```text
32bb4fde057436c5c51f7d0288b7e028d9f094642bab93be290cbdb1849cdf96
```

The frozen comparison confirmed the prior and diagnostic schemas were equal. The model identifier, source sentence, claim categories, change states, 4096 context, parallelism, load request, temperature 0, seed 0, 512-token output budget, non-streaming endpoint, and base shape/grounding validator remained unchanged.

## Operational evidence

LM Studio applied:

```text
model: gemma-4-e4b-it-ud
identifier: upgradepilot-gemma-e4b-smoke
architecture: gemma4
parameters: 7.5B
quantization: Q4_K_XL
context: 4096
eval batch: 2048
physical batch: 512
parallel: 1
Flash Attention: true
KV cache on GPU: true
MTP speculative decoding: false
simple speculative decoding: false
TTL: 900 seconds
```

The CLI reported a successful 4.75 GiB load in 6.20 seconds. No guardrail, OOM, fallback, crash, restart, or observed instability occurred.

| Point | GPU used | GPU free | Temperature | WSL-visible RAM used |
|---|---:|---:|---:|---:|
| Before load | 1168 MiB | 6851 MiB | 50 C | 2.1 GiB |
| After load | 4574 MiB | 3445 MiB | 50 C | 2.1 GiB |
| After diagnostic | 4605 MiB | 3414 MiB | 57 C | 2.0 GiB |
| After unload | 1238 MiB | 6781 MiB | 57 C | 2.0 GiB |

## Gate A — identical clear-fix case

Source in all three runs:

```text
This release fixes a crash when parsing empty configuration files.
```

Required result:

```text
state: resolved
one fix_or_remediation/fixed claim
exact grounded quotation
zero unresolved reasons
```

Observed result:

| Run | Result | State | Claims | Reasons | Client latency | Reasoning tokens |
|---|---|---|---:|---:|---:|---:|
| 1 | pass | resolved | 1 | 0 | 6.891972 s | 304 |
| 2 | pass | resolved | 1 | 0 | 6.475020 s | 314 |
| 3 | pass | resolved | 1 | 0 | 6.404390 s | 314 |

Every claim used `fix_or_remediation`, `fixed`, and the exact complete source sentence. All outer responses and inner JSON parsed, every finish reason was `stop`, and the deterministic cross-field invariant accepted every run.

Gate A conclusion:

> Explicit state semantics corrected the original clear-fix state-selection failure for three consecutive runs under the frozen deployment.

This is bounded evidence for that case, not proof of general semantic suitability.

## Gate B — no decision-relevant claim

Source:

```text
Documentation examples were reorganized and several spelling errors were corrected.
```

Observed:

```text
state: no_decision_relevant_claim
claims: []
unresolved_reasons: []
finish reason: stop
client latency: 7.160188 seconds
```

The structural, cross-field, and case-specific validators passed.

## Gate B — ambiguity failure

Source:

```text
Compatibility behavior was adjusted for older environments.
```

Expected by the frozen oracle:

```text
state: unresolved
claims: []
one or more unresolved reasons
```

Observed:

```json
{
  "state": "resolved",
  "claims": [
    {
      "category": "compatibility_assurance",
      "subject": "Compatibility behavior",
      "change_state": "changed_unspecified",
      "source_quote": "Compatibility behavior was adjusted for older environments."
    }
  ],
  "unresolved_reasons": []
}
```

Response metadata:

```text
finish reason: stop
client latency: 6.844200 seconds
prompt tokens: 335
completion tokens: 454
reasoning tokens: 360
total tokens: 789
```

Classification:

| Layer | Result |
|---|---|
| Transport and parsing | pass |
| Flat schema | pass |
| Exact quotation grounding | pass |
| State/claims/reasons invariant | pass |
| Frozen expected state | fail |
| Frozen expected claim set | fail |
| Category support | fail |

The output was internally consistent, but `compatibility_assurance` was not supported by wording that merely reported an adjustment. The model also treated the existence of the adjustment as resolved rather than preserving the unspecified behavior, affected environments, and direction as unresolved.

## Contract/oracle overlap exposed by the failure

The failure is not safely explained as a cross-field schema problem. Stronger state branches would permit the observed internally consistent `resolved + one claim + zero reasons` shape.

The current vocabulary also contains an overlap that must be resolved before another model run:

```text
changed_unspecified
→ current prompt: use when a change is explicit but its direction is not

unresolved
→ state contract v1.1: use when relevant meaning is ambiguous or incomplete
```

The sentence explicitly reports an adjustment while leaving its direction, concrete behavior, and exact older environments unspecified. The model's use of `changed_unspecified` follows one part of the prompt, while the frozen oracle expects the missing meaning to force `unresolved`.

This does not excuse the unsupported `compatibility_assurance` category. It shows that the state failure and category failure must be separated:

1. **Category failure:** adjustment is not an assurance; `compatibility_assurance` was too strong.
2. **State/oracle question:** decide whether a grounded but materially underspecified behavior-change claim is admitted as `resolved + changed_unspecified` or rejected as `unresolved`.

## Stop condition

The diagnostic stopped immediately after the ambiguity failure. Therefore it did not send:

- the opposing Python 3.13 support claims;
- the broader ten-case semantic corpus;
- the pytest release body;
- any Qwen or Gemma 12B request;
- any Instructor request;
- any product integration request.

The exact Gemma instance was unloaded and LM Studio reported no models loaded afterward.

## Evidence-backed continuation proposal

Do not rerun the ambiguity case yet. Do not test stronger schema branching yet: the observed response already satisfies the proposed branch cardinalities, so branching cannot resolve the semantic disagreement.

First review and freeze:

1. the operational distinction between `compatibility_assurance` and `interface_or_behavior_change`;
2. the minimum meaning required to accept `changed_unspecified`;
3. which missing details force `unresolved` rather than a weak grounded claim;
4. the expected result for the exact ambiguity case;
5. at least one contrast that proves the chosen boundary is not tailored to this sentence.

After that contract/oracle decision, choose one bounded continuation:

- correct the oracle and run a contrast micro-suite if `resolved + interface_or_behavior_change/changed_unspecified` is admitted;
- refine the semantic instructions and rerun only ambiguity contrasts if missing direction must force `unresolved`;
- test another model only after the same frozen boundary can judge it fairly.

This result does not admit Gemma E4B to the broader corpus and does not reject it as an operational control.

## Raw artifact map

- `diagnostic.py` — wrapper harness reusing the prior request/schema/runtime code.
- `system-prompt-v1.0.txt` — exact prior system prompt.
- `state-contract-v1.1-addition.txt` — exact diagnostic-only prompt addition.
- `system-prompt-v1.1.txt` — exact complete diagnostic prompt.
- `schema.json` — unchanged flat schema.
- `frozen-variable-comparison.json` — hashes and changed/unchanged variables.
- `gate-a-case.json` and `gate-b-cases.json` — frozen diagnostic inputs and oracles.
- `load-output.txt` — complete controlled load output.
- `snapshots/` — pre-load, post-load, post-diagnostic, and post-unload state.
- `runs/` — exact request, source, raw outer response, parsed response, and validation for every sent case.
- `gate-a-summary.json` and `gate-b-summary.json` — stop-controlled gate outcomes.
- `logs/` — filtered model input, output, reasoning, and timing statistics.
- `unload-output.txt` — exact unload confirmation.
