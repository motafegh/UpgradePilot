# Stage 7 bounded remediation progress

**Date:** 2026-10-20  
**Status:** ACTIVE  
**Branch:** `audit/project-wide-system-audit-2026-10-20`  
**Latest reconciled main:** `3344982c10e75863b4f4b922984e3b10b63f3b80`  
**Current audit-program input:** [AUDIT-019](../audits/2026-10-20_AUDIT-019_phase-b-product-value-reconciliation-and-audit-program-reprioritization.md)  
**Predecessor order:** [AUDIT-018](../audits/2026-10-20_AUDIT-018_cross-domain-remediation-priorities.md)

## Focused audit-program cadence

`reconcile → correct bounded owner → verify → record → continue`

No mandatory D/E learning ceremony is used for this audit/correction branch unless a specific consequential responsibility needs it.

## Delivered Wave-1 corrections

### Truth/lifecycle/navigation

- corrected README LM Studio base from stale `127.0.0.1:12345` to canonical `127.0.0.1:18080`;
- clarified `PROJECT_CHARTER.md` so 2026-07-20→2026-10-17 is the **initial** 90-day horizon, not automatic Charter/project expiry;
- reconciled audit lifecycle around one current successor audit instead of multiple stale current inputs;
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

GitHub still reports `main` unprotected with no required status checks/rulesets. The connected GitHub tool exposes protection/ruleset reads but no administration write action, so requiring the new `Installed package and deterministic product tests` status on `main` needs an authorized GitHub repository-admin action outside the current connector.

### Python support/proof policy — decided, owner wording pending

Recorded [the Python support/proof disposition](evidence/2026-10-20-python-support-proof-policy.md).

Current claim model:

```text
package metadata admits Python >=3.12
current hosted qualified line = Python 3.12
later Python minors = packaging-admissible but not yet covered by the repository's hosted compatibility matrix
```

Do **not** add an upper Python bound merely to mirror today's one-line CI proof; no evidence currently establishes later minors are incompatible. Also do not present `>=3.12` as though every later minor has been hosted-qualified.

Before branch integration, reconcile README/Product-verification wording with this distinction and record exact interpreter(s) actually proven by the integrated workflow. The current audit-branch README still needs that user-facing proof-scope edit; do not call this correction complete until the owner text and hosted proof are aligned.

## Workspace migration prerequisite delivered — now parked

Created:

`working-memory/evidence/2026-10-20-workspace-migration-audit/LEGACY_TO_WORKSPACE_CONSUMER_LEDGER.md`

The ledger maps every `PublicPullRequestInvestigation` field to:

```text
semantic owner/origin
→ current Workspace family/material status
→ current synthesis/report consumers
→ migration disposition
```

Key result: do not copy the legacy dataclass one-field/one-family into Workspace. Existing CI/Python-support closure is coherent; `workflow_evidence` is derivable from captured `ci_inputs`. The genuine missing closure clusters remain package/upstream material and artifact-serviceability.

**After main Phase B, new architecture work from this ledger is paused rather than selected.** The ledger remains valid preparation evidence if a later product-value result selects Workspace closure.

## Main Phase-B reconciliation

Main `cbba2c88` completed the product-value and transparent-baseline feasibility investigation with no executable product/experiment changes.

Accepted audit observations:

- 16/16 scenarios screened;
- six deeply inspected;
- only S002 and S004 ready for the declared retained-native-CI-output comparison;
- no fresh end-to-end benchmark qualified or executed;
- S004 demonstrates that existing deterministic/native CI owners already preserve important authority/uncertainty boundaries that later semantic interpretation can overstate;
- the proposed next step is a finite two-case component information-value comparison before another interpretation architecture.

AUDIT-019 accepts that recommendation as technically credible, subject to Ali's explicit selection on main.

### Required interpretation boundary

A negative comparison result may establish only:

> the retained native-CI component showed no material incremental information value over transparent baseline v0.1 on the two exposed S002/S004 cases under the frozen October evidence boundary.

It must not be promoted into a project-wide no-value, deterministic-method no-value, Workspace rejection, hybrid-architecture rejection or general reliability conclusion.

A positive result is equally narrow: exposed-case component benefit, not full-product superiority or maintainer usefulness.

## Latest main after Phase B

`main` then advanced to `3344982c` with one new exploratory proposal:

`proposals/2026-10-20_UPGRADEPILOT_AI_NATIVE_ENGINEERING_AND_CAREER_CAPABILITY_HORIZON_PROPOSAL.md`

The proposal explicitly has no controlling authority. Main `MEMORY.md` still retains the product-value feasibility handoff and says the comparison contract requires review/acceptance before execution. Therefore the proposal does not change our supervisory sequencing.

## Current next responsibility on this audit branch

Do **not** enter package/upstream Workspace design yet.

Current branch work is:

1. preserve AUDIT-019 as the current supervisory/reprioritization input;
2. continue only comparison-independent corrections:
   - Smart Override root semantic clarification;
   - README/Product-verification owner wording for the now-decided Python support/proof boundary;
   - deterministic CI hosted proof/integration administration;
   - newly discovered documentation/lifecycle truth defects;
3. supervise/review the main S002/S004 comparison if Ali selects it;
4. once its result exists, audit what it actually changes and select the cheapest justified owner/capability;
5. resume Workspace closure only if that later evidence makes it a priority.

## Explicitly paused pending comparison result

- package/upstream Workspace closure design;
- artifact-serviceability Workspace closure design;
- direct Workspace consumer cutover;
- new deterministic source-relation subsystem;
- new semantic validator;
- prompt/model iteration;
- multi-role interpretation/validation experiment;
- different model/deployment experiment;
- positive action-permission expansion.

## Branch integration boundary

Do not merge this branch wholesale into `main`.

The branches contain overlapping product-value-plan edits plus independent audit/governance/CI work. Integrate later by coherent responsibility after semantic reconciliation and proof, not by commit chronology.

Likely future integration groups:

```text
truth/lifecycle documentation corrections
canonical deterministic CI change + hosted/admin proof
Smart Override clarification
Python support/proof clarification
selected audit records
only those product-value plan distinctions not already superseded by main
```

`UP-SKILL:upgradepilot-repository-audit`
