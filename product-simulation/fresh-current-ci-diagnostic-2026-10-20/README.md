# Fresh Current CI Diagnostic Cohort — 2026-10-20

This is the exposed `FCI` (Fresh Current CI) development/diagnostic cohort for UpgradePilot. It is deliberately separate from historical S001–S016 and must not be described as a holdout, protected evaluation set, unbiased generalization evidence, or product-acceptance evidence.

## Purpose

The cohort preserves current public GitHub Actions evidence so deterministic diagnostics can ask whether UpgradePilot correctly acquires workflow runs/jobs/steps, preserves exact target provenance, correlates workflow YAML with runtime execution only where the current contract supports it, and keeps unsupported or missing relationships unresolved.

A green GitHub job is not evidence that an updated dependency was installed, imported, exercised, or behaviorally compatible. Correlation evidence establishes identity only within its own contract.

## Cohort

| Case | Transition | Diagnostic role | Qualification |
| --- | --- | --- | --- |
| `FCI001-openai-agents-mcp` | `mcp 2.0.0 -> 2.3.0` | Positive current YAML↔runtime correlation shape with non-empty GitHub step summaries | `qualified_for_current_ci_diagnostic` |
| `FCI002-mdformat-footnote-tox` | `tox>=4.61.1 -> >=4.64.4` | tox-oriented matrix refusal control; executed jobs have steps while skipped publish jobs retain unavailable/null steps | `qualified_as_unresolved_control` |
| `FCI003-pasarguard-fastapi` | `fastapi>=0.143.2 -> >=0.143.3` | Rich non-empty runtime steps but no explicit static job display names; correlator must refuse rather than guess | `qualified_as_unresolved_control` |

Three cases are sufficient for the selected responsibilities; the objective is discrimination and reproducibility, not case count.

## Organization

Each admitted case keeps:

- `manifest.json` — frozen identity, qualification, request identities, byte sizes, SHA-256 and Git blob identities;
- `raw/` — immutable provider/source evidence;
- `review/` — human/AI qualification notes kept outside producer inputs.

Cohort-level records:

- `CANDIDATE_SELECTION.md` — admitted/rejected candidates and stop decision;
- `READINESS_MATRIX.md` — what each case can diagnose and where unresolved boundaries are expected;
- `REPLAY_VERIFICATION.md` — fresh-process/offline replay method, results and capture-repair audit;
- `FINAL_REPORT.md` — concise outcome, limitations and recommended next diagnostic;
- `verify_bundle.py` — no-network integrity/identity verifier for a fresh checkout.

## Raw/provider separation and immutability

Files below `raw/` are immutable after publication. Verification found that the first manually persisted PR-diff reconstructions for FCI001 and FCI003 had whitespace introduced on otherwise blank context lines. Those files were **not overwritten**: they remain preserved and explicitly marked non-authoritative. Additive `pr.provider-exact.diff` files match the original captured provider bytes and are the manifest-selected producer inputs. FCI002's original diff was exact.

## Capture-fidelity limitation

The available GitHub connector exposes structured provider fields used by the current diagnostic path plus repository source/diff text, but it does not export the original HTTP response body and headers byte-for-byte. Provider API captures are therefore **structured provider captures**, not HTTP-wire archives. Manifests make this limitation explicit; no unexposed field is claimed as retained.

Source and authoritative diff artifacts are retained losslessly, with byte size, SHA-256 and Git object identity.

## Logs and workflow artifacts

Logs/workflow artifacts were not retained for these cases because they are not material to the current declared correlation responsibilities and would increase size/security/privacy surface. If a later diagnostic demonstrates a concrete need, that evidence must be captured explicitly rather than assumed to have existed.

## Exposure boundary

All cases were inspected and selected during development. They are exposed diagnostic fixtures only. A later qualification/generalization study needs a separately protected cohort that was not used to design or debug this pipeline.
