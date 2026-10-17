# Current-runtime completion — progressive actual findings

The bounded r8 cohort is now complete. Earlier checkpoints below retain their original
horizons; the final reconciliation follows them. [MEMORY](../../../MEMORY.md) alone
owns continuation.
All runs use synthetic interface inputs, not the later paired real-case comparison.

[Qwen9 actual checkpoint](qwen9-completed-checkpoint.json): four independent sequences,
five calls each, all4/4 qualify. Actual usage234,721 input/3,339 target-generated tokens,
zero unknown usage; separate reasoning/draft counts are unreported, not asserted zero.
The current2.60.0 off/T0.2/K40/P.95 point is separately frozen; it does not inherit
r6's unexposed sampler defaults or establish a causal improvement over that point.

All four actual visible reports were read. Both short reports use delivered references,
distinguish scoped positive/zero/empty observations and retain synthetic compatibility
uncertainty. Raw long has valid citations but recommends proceeding with the dependency
update assuming the interface-ready marker is sufficient. That inference exceeds the
evidence: a synthetic source marker establishes no update compatibility or permission.
Structured long keeps an unresolved update conclusion and ci_coverage not_evaluated.
Its statement that no evidence was provided for the missing-file read outcome needs
careful interpretation: the failure observation is visible, but no typed failure
reference was delivered. The wording is ambiguous between no citable evidence and
an unknown outcome; an actual contradiction is not established by that phrase alone.

Preserve the original interface passes and these separate semantic defects. No output
is repaired/regraded and no canary result is promoted into product acceptance.
The exact requests/renderings/native metadata/visible streams/reports remain in the
durable owner-only r8 root named in the [pre-run snapshot](README.md).

## Gemma12 completed checkpoint

[Eight completed sequences](qwen9-gemma12-completed-checkpoint.json) retain both
finished configurations. Gemma12 uses20 calls/237,069 input/3,858 target-generated
tokens,zero newly unknown usage; all4/4 qualify with five calls each. The combined
checkpoint is40 calls/471,790 input/7,197 target; it excludes active Qwen27 calls.

All four Gemma12 visible reports were read. Both short reports correctly cite marker,
zero-search and empty-file observations, assert only synthetic task completion and
explicitly disclaim actual compatibility proof. Raw long keeps that compatibility
limit, labels the failed read as inferred and calls the interface confirmed-ready
from the marker alone. Structured long cites correct
native/source references but omits the native record's explicit not_evaluated value,
saying its specific content is not provided in the summary. Its actual delivered
record includes outcome=not_evaluated/payload=null. The report also overstates the
synthetic marker as confirmation that the system is interface-ready. Record existence,
an observed marker and actual system readiness remain different claims. These defects
do not change the frozen interface dispositions or establish semantic acceptance.
The omitted native outcome is an informativeness gap: the delivered payload is null,
so stating that substantive payload content is unavailable is not itself a false claim.

Review correction after checking the exact packed request: the failed read's returned
problem has evidence=[] and contributes no eligible typed reference. Its uncited
description is therefore not a citation-admission failure, and inferred status wording
is a separate descriptive choice rather than a failed frozen gate. Do not penalize a
model for omitting a reference that the interface never delivered or encourage invention
of one. The stronger marker/readiness overstatement and omitted native outcome findings
remain supported by the actual reports. Original4/4 dispositions remain unchanged.
The same correction qualifies the earlier Qwen9 evidence-accounting criticism:
ambiguous wording is not proven failure to see an observation. Keep the clearly
unsupported Raw-long proceed recommendation separate from that weaker interpretation.

## Qwen27 short-sequence checkpoint

[Ten completed sequences](ten-sequence-checkpoint.json) include Qwen27's two short
passes in10 calls/27,665 input/2,161 target/1,878 reported draft tokens,zero new unknown
usage. Both full visible reports were read: they use correct delivered references,
scope the marker/zero/empty observations, avoid actual update compatibility claims,
and explicitly distinguish finish_investigation's ready outcome from unsupported
adequacy. Its two long sequences remain pending; no4/4 deployment qualification yet.
The combined completed-only checkpoint has50 calls/499,455 input/9,358 target/1,878
draft. Currently active long-sequence calls are excluded from those checkpoint totals.

The final packed Structured-short request was also checked against its wording:
finish control history is visible, but the eligible evidence set contains only three
source/search references. A generic control event is not automatically a delivered
typed trial_event evidence reference. Preserve that distinction during semantic review.

The later case baseline remains two deployments/eight assignments and unactivated.
R8's2048 generated-token canary cap differs from the planned8192 case allowance.
Preflight fitting an8192 reserve proves capacity for its inspected shapes, not actual
8192-token generation, real-case report adequacy or a ready case manifest.

## Qwen27 Raw long completed checkpoint

[Eleven completed sequences](eleven-sequence-checkpoint.json): Qwen27 Raw long passes
in five calls; only Structured long remains pending. The combined completed-only ledger
is55 calls/602,254 input/10,206 target/2,673 draft,zero new unknown; active calls excluded.
Its full report correctly uses delivered marker/search IDs, notes no eligible reference
was delivered for the failed read, scopes absence to the capture and recommends no
dependency update action. Other two searched files are explicitly unexamined individually.

The report's no-further-operations wording must be read with its actual report menu:
tools=[] after finish. It is not proof that no unread source data exists. The same
phase check corrects the stronger earlier [r6 stopping criticism](../2026-10-17-investigator-model-interface-r6/ANALYSIS.md),
without changing any qualification disposition. Prescribed interface operations do
not establish autonomous investigation or stopping adequacy.

The report's client elapsed669.323s differs from native total730.057s/TTFT180.035s;
native usage is20,659 input/762 target/723 draft. Preserve original timing fields and
their unestablished measurement relationship. This exact point is slow enough to matter
to a later case-budget decision, without proving a causal runtime/model speed ranking.

## Final completion and all-six current-runtime disposition

[All12 r8 sequences](actual-results.json) finish normally: each candidate20 calls/4
qualified sequences,60 calls total,705,731 input/11,068 target-generated/3,447 reported
draft tokens,zero newly unknown usage. Qwen27's final Structured-long report was read:
correct delivered source/native IDs, explicit not_evaluated/null, scoped failed read
with no delivered evidence ref, no action/compatibility claim. All completed visible
reports/corrections and actual tool events were inspected, not just summary pass counts.

Combining separately frozen [r7](../2026-10-17-investigator-model-interface-r7/ANALYSIS.md)
and r8 points yields the following current2.60.0 observations, without pooling old
failed results or claiming controlled cross-model superiority:

| Candidate | Mode/sampling; generation cap | Calls | Sequences | Disposition |
| --- | --- | ---: | ---: | --- |
| Gemma 4 12B |off,T.2/K40/P.95;2048|20|4/4|Canary-qualified exact point|
| Qwen3.8-27B UD-Q4_K_M |off,T.2/K40/P.95;2048|20|4/4|Canary-qualified exact point|
| Gemma 4 E2B |on,T1/K64/P.95;8192|17|2/4|WITHHELD: early completion/skipped operation/ineligible refs in short sequences|
| Gemma 4 E4B |on,T1/K64/P.95;8192|20|4/4|Canary-qualified exact point|
| MiMo-V2.6-Distill-Qwen-9B |on,T.6/K20/P.95;8192|22|2/4|WITHHELD: ineligible long-report refs after correction|
| Qwen3.5-9B |off,T.2/K40/P.95;2048|20|4/4|Canary-qualified exact point|

[The exact candidate catalog](current-runtime-candidates.json) joins local asset
filename/SHA256, tokenizer/BOS policy, requested load/prediction controls, actual
backend placement/cache/template identities, frozen configuration and original
dispositions. MTP=true is an exposed applied Qwen27 load setting, checked through the
full raw-load identity, with native draft usage saved; it is not an extra deployment.
All use context32768/CPU q8_0 K/V/unified cache with serial single prediction.
Backend weight-layer flags are22/13/all/all/28/28 respectively; those flags do not
independently prove each tensor's physical residency. Auto kernel selection remains
unexposed for the Gemmas. No claim of globally optimal context/offload/settings.

[Observed native controls](observed-applied-controls.json) independently compare all119
current-runtime calls:119 native metadata receipts,zero requested/prediction-setting
mismatches,zero native-load/identity mismatches,zero fully rendered prompt-token
mismatches. Separate reasoning counts remain unreported; hidden fragments were
discarded before accumulation/storage. No hidden-token reconstruction or output salvage.

[Post-batch checks](post-batch-verification.json): runner/sampler exit0,loaded SDK
inventory empty,frozen source hashes unchanged. Earlier r5/r6/r7 completed retention
indexes all reverify:891/1164/720 files respectively. Final r8 retention is summarized
separately below. Existing35 focused and65 nearest product controls remain applicable;
no executable change occurred after their verification. No full/installed/hosted suite
result is used to claim acceptance of these experiment-only changes.

[R8 resource/timing observations](resource-and-latency-summary.json) include3810
samples in the approximate actual-call window: sampled whole-machine peak6319MiB,
minimum host-free18,680,784KiB,zero sample errors. Client call-time sums are
Qwen9 376.37s/Gemma12 844.69s/Qwen27 2701.82s,20 calls each. Qwen27's largest call
is669.32s. Native/client definitions differ; sampled values are not continuous maxima,
process-exclusive allocation or an intrinsic model speed ranking.

Across all revisions there are338 attempts,known3,922,961 input/82,220 target-generated/
11,139 draft tokens,with the one earlier r4 terminated-call usage still unknown.
Current r7+r8 points use119 calls,1,447,727 input/45,216 target/3,447 reported draft;
all new usage is complete. Absence of separate draft/reasoning fields is not zero.
R8 actual60<=72 new; actual cumulative338<=350 revision maximum<=363 aggregate ceiling.

Completed WITHHELD points are negative qualification results, not unattempted jobs.
Four4/4 points demonstrate the bounded interface contract; prescribed operations do
not establish autonomous discovery/stopping adequacy, valid citations do not establish
entailment, and synthetic context fit does not establish real-case report adequacy.
The clear Qwen9 Raw-long proceed inference remains a semantic warning, not a failed
interface grade. Weaker descriptive criticisms were corrected against actual phase/
reference visibility, as recorded above. No intrinsic model ranking or independent
acceptance follows. The later comparison still has two deployments/eight assignments
and has not started; actual case requests/configuration/budgets/review need their own freeze.

[Final r8 retention](retention-summary.json) verifies600 files/22,798,015 bytes, each
size/SHA256/0600 mode checked, all directories0700. Local index SHA256:
`ba54645fd808ca44023ccc306b15afe21ce55cfbce652b42d54484d313dd9613`.
This includes all raw canary requests/renderings/visible outputs/native receipts,
preparations/configuration/source/template snapshots, failed diagnostic/preparation
records, offline analysis code/results and telemetry in this root. No hidden fragments,
full model/runtime binary archive or off-machine backup is claimed. The closed r8 root
is unchanged after indexing; final public record validation writes to the repository.
[Final accounting](final-accounting.json) derives cumulative totals from actual r8
usage plus the immutable pre-run prior-spend ledger, preserving the old unknown.
