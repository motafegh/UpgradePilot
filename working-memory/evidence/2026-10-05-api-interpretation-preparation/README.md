# API interpretation preparation — frozen design evidence

Prepared 2026-10-05 under the [feasibility plan](../../../plans/UPSTREAM_API_CHANGE_AND_TARGET_EXPOSURE_FEASIBILITY_PLAN.md). The [cycle record](../../2026-10-05_1617_api-change-interpretation-preparation_lbd-cycle.md) preserves design reasoning and learning; `MEMORY.md` owns live continuation.

This package contains a proposed source-only role, not implemented inference or model results:

- `output-schema-v1.json`: exact output shape for `source-only-api-change-v1`.
- `prompt-template-v1.md`: generic task instructions and input roles; no assembled request or expected answers.
- `source-inputs-v1.json`: 19 prepared inputs with exact text, provenance and recoverable line maps. Opaque input IDs pair with the separate evaluator file; semantic case names/expected answers do not enter model inputs.
- `evaluation-cases-v1.json`: required/forbidden propositions, omission checks and proof class. This file is evaluator-only. Expected wording is explanatory, not a production keyword oracle or exact-response scoring rule.
- `schema-review-examples.json`: explicitly hand-authored design controls. A correct deprecation and an incorrect removal of the same quoted material both satisfy the schema; an extra compatibility field fails it. These are not model responses or an implemented grounding/evaluation runner.
- `source-provenance.json`, the retained urllib3 release section and license files: source identity and redistribution attribution.
- `freeze-manifest.json`: hashes and sizes for the design inputs above. `README.md` and `verification.json` describe this review and are excluded to avoid circular hashing.
- `verification.json`: measured artifact-review results, with separate non-proof statements.

The corpus has one complete retained HTTPX acquisition window, six authentic HTTPX/urllib3 excerpts, one partial window derived from retained HTTPX evidence, ten constructed controls and one empty-input preflight. The excerpts deliberately isolate calibration questions; the first ordinary interpretation request must instead use the full available acquired window. Neither manually selecting urllib3 RST text nor recovering the saved HTTPX packet establishes a second fresh ordinary target-PR case. That case remains required before broader semantic claims.

HTTPX evidence comes from the saved ordinary packet linked in provenance, not a fresh upstream read. urllib3 text was read anonymously from a fixed revision resolved from tag `2.0.0`. The retained RST section and exact excerpts can be reviewed against the pinned full-file hash; the full upstream file was not published here. Original MIT notices are retained. Constructed text has no external source-authority claim.

The schema's array/string limits are resource guards, not a guarantee that all allowed values fit a 1,536-token completion or that all source changes fit one response. Exact prompt/schema/tokenizer/context fit and provider schema support require later runtime verification. A completion-length stop is a failed output, with no accepted partial salvage. Source completeness and interpreted-change coverage remain separate, and model-reported unassessed spans do not detect every omission.

Verification here checks schema validity, reference-map recovery, provenance, paired cases, evaluator separation and frozen artifact integrity. It does not run the new role, test model accuracy, establish target exposure/compatibility, perform protected independent review or prove maintainer usefulness. Existing product and experiment regression results were not rerun for this documentation/data-only increment.

Publication formatting exception: the exact urllib3 RST section retains its original trailing blank separator, which Git flags as a new blank line at EOF. Its pinned hash is checked without changing the text. The staged whitespace check excludes only that source file; all authored files pass.
