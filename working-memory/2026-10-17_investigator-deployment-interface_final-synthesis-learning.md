# Investigator deployment/interface — final synthesis learning

**Branch:** `learning/deployment-interface-d-prep-2026-10-17`
**Date:** October 17, 2026
**Status:** ACTIVE learning/D-preparation only; not canonical D and not an experiment outcome owner.

## Learner-owned synthesis

Ali's answers, reviewed October 17:

1. A deployment can pass the Investigator interface while still failing semantic correctness. Correct tool use, valid references and schema-valid output do not establish that the final dependency-update claims are actually supported by the evidence.
2. When the same model moves from failure in one deployment configuration to success in another, a single changed feature such as thinking mode cannot be credited if other material parameters/runtime conditions changed too. The later result establishes behavior for that tested deployment configuration, not a causal explanation for the improvement.
3. Qualification is bound to the runtime/configuration under which it was observed. A material backend/runtime change means prior passes cannot silently be inherited as current-runtime qualification; the new operating point must be measured separately.
4. The core lesson of the cycle is that declared/requested/intended settings are not observations. UpgradePilot must separately verify the actually applied runtime state and the model's actual behavior, preserve differences between configurations, and avoid pooling materially different conditions.

These conclusions are owned at the current learning depth.

## Current reconciliation boundary

Do not finalize per-model synthesis yet. Main advanced during this learning session: current-runtime Qwen3.5-9B and Gemma 12B canaries completed 4/4 each, and Qwen3.8-27B short sequences passed while its two long sequences were still pending at the latest checked horizon. The final per-model/current-state synthesis must be reconciled after that active bounded completion is finished and published.

Do not use revision-number shorthand as the primary teaching language. Prefer descriptive labels such as `earlier thinking-off six-model qualification`, `native thinking-on smaller-model qualification`, and `current-runtime completion` so the learner does not need to memorize revision IDs.
