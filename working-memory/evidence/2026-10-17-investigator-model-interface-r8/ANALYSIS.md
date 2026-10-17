# Current-runtime completion — progressive actual findings

The first checkpoint covered Qwen9; the appended checkpoint now includes Gemma12.
Qwen27 results remain pending at this horizon; [MEMORY](../../../MEMORY.md) owns continuation.
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
Structured long keeps an unresolved update conclusion and ci_coverage not_evaluated,
but says no evidence was provided for the missing-file read outcome while elsewhere
acknowledging its visible returned problem. This is an evidence-accounting inconsistency.

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
limit, but labels an observed read failure as inferred without a citation and calls
the interface confirmed-ready from the marker alone. Structured long cites correct
native/source references but omits the native record's explicit not_evaluated value,
saying its specific content is not provided in the summary. Its actual delivered
record includes outcome=not_evaluated/payload=null. The report also overstates the
synthetic marker as confirmation that the system is interface-ready. Record existence,
an observed marker and actual system readiness remain different claims. These defects
do not change the frozen interface dispositions or establish semantic acceptance.
