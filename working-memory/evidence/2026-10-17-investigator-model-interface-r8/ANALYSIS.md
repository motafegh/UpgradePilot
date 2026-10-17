# Current-runtime completion — progressive actual findings

This checkpoint covers the completed Qwen9 configuration only. Gemma12/Qwen27
results are pending at this horizon; [MEMORY](../../../MEMORY.md) owns continuation.
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
