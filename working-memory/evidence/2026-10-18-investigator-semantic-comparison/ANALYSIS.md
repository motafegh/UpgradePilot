# Revised Investigator interface qualification — completed negative admission result

**Evidence horizon:** the frozen pipeline ran from 2026-10-17 23:17:25 UTC to 2026-10-18 00:59:19 UTC. Final read-only verification and retention indexing completed October 18 at approximately 11:16 UTC. This record describes that experiment, not live continuation. [MEMORY](../../../MEMORY.md) owns continuation; [the existing cycle](../../2026-10-17_2256_investigator-real-case-semantic-comparison_lbd-cycle.md) owns progression.

The budget-observation implementation and complete pre-inference freeze were delivered. The revised interface qualification then completed all 12 independent sequences, with **10 qualified and two withheld**. Because the frozen admission rule requires every selected point to qualify, **no real-case semantic assignment was attempted**. The experiment has no Raw-versus-Structured semantic result.

## Delivered responsibility and proof

The experiment driver now exposes its actual remaining invocations, operation units, observation capacity, corrections and sampled deadline. The model boundary adds its own validated call/token allowance before rendering, keeping the snapshot stable across repacking. The complete request preserves this control metadata even when evidence events are omitted. It distinguishes completion cost from discovery capacity: finish and report require separate invocations; finish costs three operation units, report four plus unique references, and procedural termination one. Only termination is enforced as reserved. These facts support informed allocation; they neither choose a stopping policy nor prove adequacy.

The semantic entry point binds source, common inputs, exact profiles, protocols, review obligations, budgets and the complete balanced schedule. It checks all required revised-contract qualifications before loading any semantic model or creating semantic outputs. A fresh host and model instance would be used for each admitted semantic assignment. That execution path remains unexercised by this live run because its admission gate failed; the focused tests cover the gate and schedule controls.

Implementation validation was **40 focused experiment tests and 65 nearest Workspace tests**, plus Ruff check/format and whitespace checks. These were run for the implementation increment before freezing; they were not repeated for this final documentation-only publication. Product source/tests were unchanged. No full product, installed-package or hosted suite was run. The older planner's four inherited fixture errors remain separately owned and were not repaired or counted as a semantic planner failure.

## Exact revised-point outcomes

All points use context 32768 and generation reserve 8192 under the revised budget-visible request contract. Exact sampling, thinking, load, template, model-asset and runtime identities remain in [the frozen entry](README.md). Prior 2048 or older-contract qualifications retain their historical meaning and cannot replace these results.

| Deployment | Raw short | Structured short | Raw near-envelope | Structured near-envelope | Calls | Input tokens | Target-generated tokens |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| Gemma 4 12B | WITHHELD | Qualified | Qualified | Qualified | 21 | 250,836 | 4,933 |
| Qwen3.8-27B UD | Qualified | Qualified | Qualified | Qualified | 20 | 242,203 | 3,870 |
| Gemma 4 E4B | Qualified | Qualified | WITHHELD | Qualified | 21 | 268,717 | 14,320 |
| **Total** | | | | | **62** | **761,756** | **23,123** |

Each qualified sequence took five calls. Each withheld sequence took six, including its one allowed terminal report correction; the original and correction remain distinct retained outputs. Four report refusals remain recorded. All independent sequences continued as frozen; no failed sequence was retried after its budget, no output repaired, no validator weakened and no deployment substituted. The actual 62 calls remain below the separate 72-call qualification ceiling. The 192-call semantic allowance was not spent.

[The complete checkpoint](completed-matrix-checkpoint.json) retains per-call costs and timing. [Final results](final-results.json) retain aggregate costs, failure-artifact identities, resource observations and verification scope. Known usage is complete for all 62 calls. Qwen reports 3,462 speculative draft tokens, including 2,702 accepted and 760 rejected; these remain separate from its target-generated count and must not be added as unique generation. Other draft counts and separate reasoning-token counts are unreported, hence unknown. Hidden reasoning content was not retained or examined.

## Two different evidence-reference failures

**Gemma12 Raw-short:** both report attempts 5 and 6 use the same 60-character value where a delivered 64-character source-line reference was required. It appears on both a claim and the recommendation's evidence list. The other cited source/search IDs are eligible. All three eligible references are present in each actual report request, and no events are omitted. Comparing the values shows a mangled copy, with multiple edits rather than simple suffix truncation. This is a reference reproduction failure; the retained payload does not establish its internal cause.

**E4B Raw near-envelope:** both report attempts 5 and 6 cite a 32-character **delivery ID** as a `source_line` reference for the unavailable `missing.txt` read. That delivered problem observation explicitly contains `evidence: []`; it reports path unavailability in this frozen capture, without establishing absence outside the capture. The delivery ID identifies an observation, not citable source evidence. The report's other source/search references are eligible, both actual report requests contain all offered references, and neither omits events. The error is an authority/type confusion, rather than a corrupted copy of an offered reference.

The shared strict resolver correctly refuses these reports. A correction event does not turn an ID repeated in model-authored intent into eligible evidence. Source availability, delivery identity, offered typed reference, claim support and semantic acceptance remain separate facts. The completed negative result is useful interface evidence; it does not show budget visibility caused either failure, that 8192 generation improved or degraded the model, or that one treatment/model is semantically better. There is one sample per condition, and the synthetic task prescribes its sequence.

## Timing and sampled resources

| Timing measure | Gemma12 | Qwen27 | E4B | Total |
| --- | ---: | ---: | ---: | ---: |
| Sum of client prediction durations, seconds | 1,085.65 | 3,642.86 | 767.86 | 5,496.38 |
| Sum of native-reported durations, seconds | 1,181.66 | 4,027.30 | 851.46 | 6,060.42 |

Pipeline wall time is **6,113.80 seconds (101.90 minutes)**. Native and client times are separate measurements with an unestablished relationship; subtracting their totals does not identify overhead. Preparation, zero-generation model loads, human/reviewer effort and the earlier 338 prediction attempts are not included in these totals. The earlier unknown-usage call remains historical rather than being relabeled known by this cohort.

The allowlisted resource sampler produced 547 observations from 23:17:44 UTC to 00:59:14 UTC, with no recorded sample errors. Maximum sampled whole-machine GPU use was **5,650 MiB of 8,192 MiB**, maximum sampled GPU utilization 93%, and minimum WSL `MemAvailable` 51,781,292 KiB. These nominal ten-second samples begin after pipeline initialization; they do not prove continuous peaks, process-exclusive consumption, peak WSL memory used or preparation resource cost. Both pipeline and sampler exited successfully; a final SDK inventory found zero loaded models.

## Final integrity and retention

Final verification revalidated the exact private freeze hashes, all six frozen experiment-source files, 37 bound files, 17 retained input files and the 96-file product-source hash set. All 62 request/rendering/packed-input/visible-output/receipt sets verify, including their actual pre-call budget counters. There are zero inspected requested/applied prediction-setting, rendered-prompt-token or instance mismatches. Each of the three saved backend/load observations matches its frozen profile. A direct recheck of semantic admission raises the expected withheld-matrix error before any model load.

The local [retention summary](completed-retention.json) identifies a final index over **749 files / 25,816,105 bytes**, excluding the index itself. Every indexed file revalidates by size and SHA256; directories are 0700 and files 0600. The private index is 137,990 bytes, SHA256 `31b955ee5e200d29ba117f56cca0fba04b3111e5780aa2c481aac9347ceb59b7`. Raw requests, visible outputs, failures, telemetry, source snapshots and reviewer obligations remain in the owner-only root named there. Public reports contain scoped results and artifact identities rather than raw model payloads. No further writes inside that completed private root are intended.

Model-weight full hashes were inherited from earlier full-hash receipts and current size/mtime bindings were rechecked; this successor did not hash all weights anew. Small backend metadata/launcher bytes were hashed before freezing. External model/runtime/common-input assets are referenced bindings, not copies inside this retention index. Local retention is not off-machine backup, a full runtime-binary archive or power-loss proof.

## Bounded interpretation and decision handoff

The semantic question remains **unanswered / withheld at admission**. Qwen27's 4/4 alone cannot activate a reduced comparison under the three-deployment freeze. Green mechanics and a correct negative gate do not create semantic acceptance. D/E and the narrow A2 budget-allocation ownership question remain pending in the existing cycle; this result does not close it.

My engineering recommendation is to use these two distinct failures to frame a bounded reference-presentation design review before another inference version. Candidate mechanisms include trusted short aliases or constrained selection of the typed references actually offered in the current request. Such a mapping must preserve exact request-local authority and strict resolution, and must keep a problem observation without evidence from acquiring invented source-line authority. Shorter IDs alone do not resolve that second distinction or establish entailment. The first step is the design/proof decision, not implementing either mechanism from this suggestion.

Retaining the frozen negative result without further inference is also valid. Any selected repair would need its own explicit contract/version, source and tests, budget, admission freeze and affected-point requalification; failed originals stay rejected. No automatic parameter sweep, validator relaxation, arm removal, cloud/model fallback or selective retry is justified by this record.
