# Fresh Current CI Diagnostic Cohort — 2026-10-20

This is the exposed `FCI` (Fresh Current CI) development/diagnostic cohort for UpgradePilot. It is deliberately separate from historical S001–S016 and must not be described as a holdout, protected evaluation set, unbiased generalization evidence, or product-acceptance evidence.

## Immediate purpose

These cases preserve current public GitHub Actions evidence so a later deterministic diagnostic can ask whether UpgradePilot correctly acquires workflow runs/jobs/steps, preserves exact target provenance, correlates workflow YAML with runtime execution only where the current contract supports it, and keeps unsupported or missing relationships unresolved.

The cohort is intentionally small and discriminating rather than representative.

## Exposure and claim boundary

All cases here were inspected and selected while developing/debugging the pipeline. They are exposed diagnostic fixtures only. A later qualification/generalization study needs a separately protected cohort that was not used to design or debug this path.

A green GitHub job is not evidence that the updated dependency was installed, imported, exercised, or behaviorally compatible. Correlation evidence establishes identity only within its own contract.

## Raw/provider separation and retention

Each admitted case keeps frozen identity/provenance in `manifest.json`, provider/source material below `raw/`, and qualification/interpretation below `review/`. Files below `raw/` become immutable at their publication commit; later repairs or interpretations must be additive outside `raw/`.

The available GitHub connector exposes structured provider fields used by the current diagnostic path plus repository source text and PR diffs, but it does not provide an export mechanism for the original HTTP response body and headers byte-for-byte. Therefore provider captures in this cohort are explicitly **structured provider captures**, not HTTP-wire archives. Manifests record this limitation; no unexposed provider field is claimed as retained.

Logs and workflow artifacts are retained only if they materially change the declared diagnostic after size/security/privacy review. The current cases do not require them because the relevant owner consumes workflow source plus run/job/step summaries.
