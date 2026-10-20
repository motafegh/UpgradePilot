# Stage 7 bounded remediation progress

**Date:** 2026-10-20  
**Status:** ACTIVE  
**Branch:** `audit/project-wide-system-audit-2026-10-20`  
**Latest reconciled main:** `bfcc8b916fc33523a535f7c5a994d118d09552b8`  
**Selected order:** [AUDIT-018](../audits/2026-10-20_AUDIT-018_cross-domain-remediation-priorities.md)

## Focused audit-program cadence

`reconcile → correct bounded owner → verify → record → continue`

No mandatory D/E learning ceremony is used for this audit/correction branch unless a specific consequential responsibility needs it.

## Delivered Wave-1 corrections

### Truth/lifecycle/navigation

- corrected README LM Studio base from stale `127.0.0.1:12345` to canonical `127.0.0.1:18080`;
- clarified `PROJECT_CHARTER.md` so 2026-07-20→2026-10-17 is the **initial** 90-day horizon, not automatic Charter/project expiry;
- reconciled audit lifecycle: AUDIT-018 is current active audit-program input; superseded AUDIT-009/010/011 and detailed Stage-1→5 audits are indexed as absorbed without rewriting their bodies;
- created `experiments/README.md` distinguishing reusable lab substrate, conditional research, historical/dormant cohort runners and Workspace prototype research superseded as active architecture.

### Still open from Wave 1

Root Smart Situational Override wording should explicitly distinguish adaptable **procedure** from accepted Charter/specification/ADR **semantic requirements and acceptance invariants**. The correction has not been applied yet because `AGENTS.md` is a large always-loaded owner and the available GitHub contents write requires whole-file replacement. Do not risk a lossy/truncated rewrite. Child-Skill boilerplate cleanup remains later P3 work.

## Wave-2 canonical deterministic integration

Updated `.github/workflows/product-verification.yml`:

```text
workflow_dispatch
+ pull_request targeting main
+ push targeting main
```

The job itself remains unchanged in proof responsibility:

- Ubuntu 24.04;
- Python 3.12;
- fresh venv and `pip install .` / `pip check`;
- commit/interpreter/resolved-package recording;
- installed CLI entry points from outside checkout;
- focused investigation composition;
- full deterministic product tests;
- no model/GPU/live acquisition/experiment suite.

### Verification/admin boundary

The workflow-source change is committed on the audit branch, but no new hosted run of this changed trigger has occurred yet. Treat hosted execution as pending proof, not inferred success.

GitHub still reports `main` unprotected with no required status checks/rulesets. The connected GitHub tool exposes protection/ruleset reads but no administration write action, so requiring the new `Installed package and deterministic product tests` status on `main` needs an authorized GitHub repository-admin action outside the current connector (for example Ali's GitHub settings UI).

### Python support policy remains open

Package metadata still declares `requires-python = ">=3.12"`; the deterministic hosted job currently proves Python 3.12 only. Do not narrow or broaden support by guess. Before final integration choose and record one explicit policy:

- a named supported-minor matrix with hosted proof; or
- 3.12 as current qualified line with broader packaging admissibility explicitly described as unqualified; or
- a deliberately narrowed package support range backed by evidence.

Current README's `3.12 or newer` wording therefore remains a proof-scope item to reconcile before integration, even though package metadata permits it syntactically.

## Wave-4 Workspace migration prerequisite delivered

Created:

`working-memory/evidence/2026-10-20-workspace-migration-audit/LEGACY_TO_WORKSPACE_CONSUMER_LEDGER.md`

The ledger maps every `PublicPullRequestInvestigation` field to:

```text
semantic owner/origin
→ current Workspace family/material status
→ current synthesis/report consumers
→ migration disposition
```

### Key result

Do not copy the legacy dataclass one-field/one-family into Workspace.

Already captured:

- exact investigation inputs/PR/dependency/changed files;
- CI inputs/coverage/runtime state;
- upstream authority/support-drop result;
- Python-support pre/selection/target/relevance/post closure.

`workflow_evidence` does not need a new family: captured `ci_inputs` already retains each exact `WorkflowRun` and `WorkflowJob` tuple plus static definition/environment sources. The migrated report can project run/job evidence from that canonical input.

The genuine missing closure clusters are:

1. **package/upstream material closure** — proposed/old package release, upstream repository/provenance, release index/window/tag/changelog intermediates/material needed for current report/stop explanations;
2. **artifact-serviceability closure** — old/new package artifact evidence, source-bound target artifact-environment associations, candidate and impact assessment.

The ledger explicitly warns not to create five separate upstream top-level families merely because five legacy intermediate fields exist. First decide whether exact intermediate source/problem semantics can live as retained input/material closure for `upstream_authority` without information loss.

## Current next responsibility

Design the smallest **package/upstream material closure** representation needed by actual report/synthesis consumers, then the artifact-serviceability closure. This is architecture/design work before source implementation.

Before entering that design, recheck latest `main`; sibling product-value plan edits remain unresolved for final integration but do not block this Workspace owner analysis.

## Non-selected work

Still not selected:

- model calls or new semantic experiment;
- autonomous discovery optimization;
- agent framework;
- Workspace direct-consumer source cutover;
- deterministic replay implementation;
- mass test cleanup;
- automatic merge of this branch into main.
