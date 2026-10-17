# Current-runtime completion — progressive actual findings

The first checkpoint covered Qwen9; the appended checkpoint now includes Gemma12.
Qwen27's appended short-sequence checkpoint is complete; its two long sequences
remain pending at this horizon. [MEMORY](../../../MEMORY.md) owns continuation.
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
