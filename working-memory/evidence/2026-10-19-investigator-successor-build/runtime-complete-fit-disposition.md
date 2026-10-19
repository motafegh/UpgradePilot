# Complete supplied-input measurement and presentation disposition

October 19, 2026. This is the directed measurement-only continuation of the [same Build cycle](../../2026-10-19_investigator-successor-build_lbd-cycle.md), under the [successor plan](../../../plans/INVESTIGATOR_RUN_CONTROL_COMPLETION_AND_CAPABILITY_DIAGNOSTIC_PLAN.md). It records a negative preparation result and a bounded design decision. It is not an inference result, semantic review or experiment activation.

## Exact observations

One corrected preflight used the unchanged intended Gemma12 profile and current-source-bound r5 packets. It completed all six actual render/tokenizer measurements in 13.302348389 seconds, with no omitted events. Actual loaded identity, backend checks, full packed/rendered requests, token counts/hashes and every preparation host's terminal ID are retained before disposition. The command exited with the expected failed-fit error after retaining the complete results. It produced no executable freeze and made zero prediction attempts. Owned unload confirmed no remaining loaded identifiers; SDK client release confirmed.

| Role | Fully rendered tokens | Declared input cap | Cap result | Headroom after 8,192 output + 256 margin in 32,768 context |
| --- | ---: | ---: | --- | ---: |
| Cancellation probe | 3,314 | 4,096 | Fits | 21,006 |
| Report-reference probe | 3,294 | 4,096 | Fits | 21,026 |
| HTTPX PR / packet-a | 23,449 | 16,000 | Exceeds by 7,449 | 871 |
| Newer captured consumer / packet-b | 8,250 | 16,000 | Fits | 16,070 |
| glyphsLib PR / packet-c | 26,603 | 16,000 | Exceeds by 10,603 | **−2,283** |
| Older captured consumer / packet-d | 8,259 | 16,000 | Fits | 16,061 |

The context input envelope is `32,768 − 8,192 − 256 = 24,320`. glyphsLib therefore fails a second, independent gate. Its current request needs 2,283 fewer input tokens even if the input cap were raised to that envelope. Reducing output to 5,909 or enlarging context to 35,051 would only meet the arithmetic boundary for this exact request, without fresh-host headroom, and would change the selected resource/operating contract. Neither is selected.

All six measured inputs total **73,169 tokens**, which is **977 above** the 72,192 prospective aggregate input ceiling. This is a sum of zero-generation measurements, **not consumed prediction usage**. Existing per-attempt gates already refuse the large cases. Any later redistribution needs prospective role limits, aggregate enforcement and actual fresh-host measurements; smaller cases' unused allowances are not permission to overspend another case.

These are runtime-r2 measurements. The original runtime-r1 HTTPX count remains unknown within its recorded interval; r2 does not recover or rewrite it. Remaining-time fields and host-minted reference spelling can change later exact token counts. Preparation speed does not establish prediction speed or cancellation behavior.

## What the presentation trace establishes

The model presentation inserts the outer observation JSON directly, but its `content` field remains a JSON string containing another complete source/native delivery. Thus source quoting, newlines and nested native envelopes still pay an escaping layer. This is a concrete representation issue. It does not establish that all metadata is unnecessary or that escaping alone explains the token totals.

| Packet | Current user-presentation bytes | Source-line text bytes, excluding separators | Source file-descriptor bytes | Native payload JSON bytes | Byte saving from the one-layer decode candidate |
| --- | ---: | ---: | ---: | ---: | ---: |
| HTTPX | 64,312 | 21,767 | 11,681 | 1,995 | 3,974 |
| Newer consumer | 25,248 | 11,761 | 2,653 | 0 | 1,136 |
| glyphsLib | 77,649 | 15,206 | 9,405 | 26,578 | 5,160 |
| Older consumer | 25,252 | 11,767 | 2,653 | 0 | 1,136 |

The system message/template contributes another 2,247 bytes for each retained rendering. Byte columns are overlapping structural measures, not a token-cost partition. glyphsLib's large native payload contains real coverage/runtime observations and uncertainties; it cannot simply be labelled disposable overhead. Some native consumption subtrees repeat across their distinct coverage/runtime owners. Metadata interning or native-codec redesign would introduce a more consequential representation mechanism; neither is required to test the simpler baseline.

The [offline analysis](runtime-complete-fit-analysis.json) validates original code and artifact hashes and tests one specific reversible candidate: decode only the recognized source/native delivery-content strings, retain every structured value, and re-encode both layers on inverse reconstruction. **All 33 typed deliveries across all six roles reproduce their original event bytes exactly.** Event metadata, chronology, request text, references, selected source lines and native values remain present. No expected answers, source reduction, summary or repaired ID enters the candidate. Its byte savings are measured offline; **its tokenizer counts and fit are unmeasured**, and runtime code still uses the existing presentation. This is a feasibility probe for a design, not an implemented or qualified replacement.

## Decision and alternatives

The engineering recommendation is a common, experiment-owned lossless presentation correction before another resource expansion. Begin with the proven reversible one-layer baseline and preserve the original canonical evidence outside the model view. Its first acceptance question is whether it can be implemented without evidence/authority loss; its second is actual token cost. Do not promise that this small correction alone will satisfy 16,000.

| Alternative | Consequence for the diagnostic | Disposition |
| --- | --- | --- |
| Raise the input cap alone | HTTPX may pass, but glyphsLib still exceeds the retained context envelope; aggregate ceilings also need a decision | Insufficient correction |
| Reduce output reserve or enlarge context/change model | Alters output capacity or the frozen operating point before interpretation is tested | Defer; not justified as the first response |
| Remove native evidence, source ranges or obligations; split the case | Makes a different capability question and can hide contradictory/limiting evidence | Not selected |
| Add metadata interning, reference aliases or native-codec flattening | May save more, but creates extra decoding/authority obligations | Defer until a measured simpler baseline is inadequate |
| Reversible presentation, then prospective role-specific reservations if needed | Preserves complete evidence and can avoid a blanket aggregate increase | Recommended bounded route; fit remains unproved |

An illustrative allocation of 23,000/9,000/23,000/9,000 plus two 4,096 probes preserves 72,192 aggregate tokens. **It does not fit the current large requests:** HTTPX would still need 449 fewer tokens and glyphsLib 3,603 fewer. The smaller cases have only 750/741 tokens of measured headroom under 9,000. This example shows why allocation is a real prospective design choice, not a presently admitted workaround. Measure the corrected presentation and justify fresh-host headroom before choosing numbers.

The [plan's complete-input presentation subsection](../../../plans/INVESTIGATOR_RUN_CONTROL_COMPLETION_AND_CAPABILITY_DIAGNOSTIC_PLAN.md) specifies the bounded implementation/proof sequence, one declared measurement preparation, allowance decision and stopping consequences. It keeps existing calls, model, output reserve, input caps and aggregate ceiling unchanged pending a concrete versioned decision. It admits no new model, discovery/navigation change or inference from this negative result.

## Evidence and reproduction

Private runtime root: `/home/motafeq/.local/share/upgradepilot/investigator-runs/supplied-evidence-2026-10-19-runtime-r2`. Its `runtime-preflight.json` SHA256 is `aaff856531ce555085e0ec596f5bc4a29ac6084357895fd92d859449e6491901`. The [measurement/byte analysis JSON](runtime-complete-fit-analysis.json) binds the reproduction script and exact runtime-preflight hash. A separate immutable disposition/source archive and [retention summary](runtime-complete-fit-retention.json) cover this continuation; prior completed indexes and original experiment roots remain unchanged.

Offline reproduction from repository root, at the retained source horizon:

```sh
PYTHONPATH=src:. .venv/bin/python working-memory/evidence/2026-10-19-investigator-successor-build/analyze-complete-fit.py /home/motafeq/.local/share/upgradepilot/investigator-runs/supplied-evidence-2026-10-19-runtime-r2
```

This reads retained data and checks exact reconstruction. It does not construct an SDK client, load a model, tokenize or predict. A future source change deliberately makes its current-source admission check fail; the exact source snapshot and original measured artifacts remain retained for historical reconstruction.

Verification also checked analysis syntax, unchanged runtime ceilings, budget/headroom arithmetic, current r5 preparation admission and 76 local Markdown links. New retention binds 39 files / 824,570 bytes excluding its index; exact membership, SHA256, size and 0700/0600 mode checks pass. The prior 200 retained files and completed index revalidate unchanged. The preceding 158 focused and 65 nearest Workspace tests remain historical implementation evidence; this evidence/design-only continuation did not rerun that suite.

The complete measurement objective is achieved. Diagnostic readiness remains withheld; backend cancellation, prediction accounting under that real cancellation probe, interpretation adequacy and usefulness remain unproved. The Build cycle remains at its verification/disposition gate with D/E and learner ownership pending.
