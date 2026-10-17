# Actual complete r6 cohort

All six selected deployments were loaded/called; all24 sequences finished normally.
[Actual results](actual-results.json) preserve every receipt, proposed action, actual
operation, report-refusal detail and original disposition. All inputs were synthetic.

| Deployment | Calls | Qualified sequences | Actual result |
| --- | ---: | ---: | --- |
| Gemma E2B |8|0/4|Off-mode reasoning-labelled fragments, early finish, ineligible event IDs; long report also copies calibration number into fields.|
| Gemma E4B |16|0/4|Off-mode reasoning-labelled fragments; long reports confuse internal/event IDs with delivered references.|
| MiMo9B |23|0/4|Required operations become usable with complete intent/result history; one report repeats until2048 cap, others repeatedly cite ineligible IDs.|
| Qwen3.5-9B |20|2/4|Both Raw sequences pass; both Structured reports omit citations despite visible eligible evidence.|
| Gemma12B |21|4/4|All required operations/report/reference gates pass; Structured long corrects a mistyped native ID on the sixth call.|
| Qwen3.8-27B |20|4/4|All four sequences pass in five calls each with saved native MTP costs.|

R6 uses108 calls,1,358,562 input/27,399 target-generated/4,182 draft tokens, zero
newly unknown usage. Cumulative through r6:219 calls,known2,475,234 input/37,004
target-generated/7,692 draft; one earlier r4 terminated-call usage remains unknown.
Separate reasoning counts are unreported; draft totals sum reported fields only.

AI-assisted inspection read the actual completed visible reports and rejected report
attempts, rather than treating a completed process or typed JSON as useful analysis:

- Gemma12 Raw short recommends proceeding with the update based on synthetic interface
  checks. That exceeds its evidence despite valid IDs and an interface pass. Its other
  reports distinguish source/search/problem outcomes, but do not establish compatibility.
- Qwen27 generally preserves frozen-capture/runtime uncertainty. Structured long says
  no further operations are available even though other source/tool options remain.
  This unsupported stopping statement is retained, not silently repaired.
- Qwen9's Raw reports overstate negative/missing evidence and mix successful marker
  reads with statements about all outcomes being negative/empty. Both Structured
  reports have no citations; strict withholding is an actual observed result.
- MiMo often describes the scoped observations sensibly but invents update_packet/
  native citation IDs, repeats them after correction, and claims the available evidence
  is exhausted while catalog entries remain unread. Raw short's partial report is
  repetitive, not proof that a larger context/output limit alone would solve it.
- E2B ignores required operations in some sequences and uses event-1 as an eligible
  trial-event citation without its delivered typed reference. E4B similarly cites
  internal32-character IDs or event labels. Guards reject these original outputs.

No hidden reasoning was retained or inspected; a reasoning-labelled-fragment flag
alone does not measure its nonempty byte/token count. Native usage/configuration and
fully rendered prompt-count correspondence are saved separately from output validity.
All original source hashes stayed frozen through normal completion; final inventory
was unloaded. Exact per-call prefixes and receipts remain in owner-only durable r6
storage. R6's SDK/model/runtime/settings remain its original horizon, not newly
reinterpreted as the later2.60.0 native-mode run.

This establishes bounded interface readiness for the two core profiles, not semantic
correctness, independent usefulness, learner ownership or acceptance of a real update.
The later paired two-deployment/eight-case comparison has not run. Native-mode
follow-up is separately admitted/frozen in [r7](../2026-10-17-investigator-model-interface-r7/README.md);
old results are not pooled, repaired or promoted by that follow-up.
