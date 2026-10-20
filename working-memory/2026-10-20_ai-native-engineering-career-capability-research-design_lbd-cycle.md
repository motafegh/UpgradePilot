# AI-native engineering and career capability research/design cycle

**Date:** 2026-10-20

**Branch:** `research/ai-native-career-capability-strategy-2026-10-20`

**Primary operation:** Planning/Design with Learning-by-Doing.

**Branch base:** `ecd11a4a424bd1b6cecc8a8c83e9e17370ab88db` from `main` (`Add FCI001 current CI diagnostic case`).

**Accepted responsibility:** Research and design how UpgradePilot can deliberately strengthen product-relevant AI-native engineering capability, Ali-owned technical capability, career evidence, and employer-facing proof without turning the horizon proposal into a technology backlog. Work remains isolated from `main` until a later fresh reconciliation and explicit integration decision.

## Cycle status

A0 — DONE: reconciled current main, Charter, route, live memory, recent Investigator/product-value work, retained native-CI/baseline comparison, active fresh-current-CI cohort, AI-native career horizon proposal, planning/design procedure, Learning-by-Doing procedure, and plan ownership rules. Created branch from the latest observed main head rather than the earlier `a38f5e1` anchor.

A1 — DONE by justified continuity compression: the immediately preceding strategy discussion already reconstructed the current project/career state and Ali explicitly accepted moving the strategy into a separate research branch. No contradictory new main evidence appeared between that discussion and branch creation except the expected FCI001 progress, which was incorporated into the base.

A2 — DONE by justified scope compression: Ali explicitly selected separate-branch research/design first and deferred any merge/adoption decision until research completes and main is rechecked. The branch responsibility, proof boundary, non-goals, and final reconciliation requirement are formalized in the branch-local research/design plan.

B — CURRENT: initial capability evidence inventory completed; next design responsibility is to turn the highest-value findings into precise integration/ownership/security/external-validation options without creating implementation tasks prematurely.

Verification gate — PARTIAL: repository classifications are source/evidence-backed; current market/security evidence was sampled to test prioritization. Full verification remains pending for the final strategy, particularly after the current `main` FCI/product-value work closes and before any integration recommendation.

D — PENDING: explain the resulting prioritized strategy, rejected/deferred alternatives, and why each retained capability belongs in product, experiment, learning, portfolio/external validation, or nowhere for now.

E — PENDING: repair understanding gaps, reconcile against then-current `main`, and produce the final integration recommendation without automatic merge.

C — CONTINUOUS: preserve branch research decisions, evidence changes, rejected ideas, main-state reconciliation points, ownership findings, and integration consequences.

## Smart situational override used for A1/A2 gates

**Circumstance:** This research cycle begins immediately after a substantive strategy review in the same conversation. Ali then explicitly requested that we work on a separate branch, research/design what and why could be appended, and postpone merge decisions until both research and the later main state are known.

**Normal route:** repeat a full A1 continuity stop and a separate A2 pre-work stop before branch research begins.

**Why that is materially worse here:** it would repeat the just-completed project/career orientation and ask Ali to reconfirm a branch/scope decision he had already made with the relevant mental model in hand. The only main delta was FCI001, and the branch was deliberately anchored after that commit.

**Override:** preserve A1/A2 substance here and in the new plan, then proceed to research inventory rather than repeating conversational gates.

**Effect:** no product implementation authority is gained. The override only compresses repeated onboarding; the branch remains research/design-only, and final integration still requires fresh main reconciliation and explicit decision.

**Reconciliation required:** D/E must teach and review the actual findings before closure. Any proposed product/owner change later returns to its normal specification/ADR/plan/Build route.

## Initial working hypotheses — not conclusions

1. UpgradePilot is already strong in provenance/evidence discipline, bounded uncertainty, experiment rejection, and increasingly in persistence/recovery; the career bottleneck may be proof of Ali-owned capability and external usefulness rather than missing architectural sophistication.
2. Evaluation engineering, AI/agent security, reliability/operability, and external validation appear likely to have high compound value because they align with existing product responsibilities instead of requiring arbitrary technology insertion.
3. Backend/API, cloud, Kubernetes, vector retrieval, multi-agent breadth, and other horizon items may be valuable later but should be rejected or deferred unless a real responsibility and proof path emerges.
4. Career identity should likely remain broader at entry (`Python/AI systems`, trustworthy automation/evaluation/security) than the long-term specialization (`AI Security Automation / Agent Security`) so job targeting is not artificially narrow.
5. A separate capability/ownership/hiring evidence layer may be useful, but it must not become a second product-control system or pollute runtime architecture.

These hypotheses must be challenged against repository evidence and current role evidence; none is admitted merely because it matches the preceding discussion.

## First research responsibility — completed inventory pass

The first pass classified the material capability families from the horizon proposal against current project evidence. The detailed result is preserved in [`../proposals/2026-10-20_AI_NATIVE_ENGINEERING_AND_CAREER_CAPABILITY_RESEARCH_FINDINGS.md`](../proposals/2026-10-20_AI_NATIVE_ENGINEERING_AND_CAREER_CAPABILITY_RESEARCH_FINDINGS.md).

The strongest preliminary pattern is not “UpgradePilot needs more technology.” It is:

```text
substantial existing engineering
+ incomplete Ali-owned qualification
+ incomplete external usefulness evidence
+ several genuine missing evidence classes
```

### Existing strengths that should primarily be qualified/exposed rather than reimplemented

- exact evidence/provenance and authority separation;
- evaluation discipline, baseline comparison and negative-result preservation;
- SQLite-backed immutable Workspace checkpoint/durability work;
- broad deterministic product/experiment testing;
- explicit security/trust policy around untrusted evidence and external action;
- measured model/runtime resource and cost evidence.

### Genuine missing evidence classes with likely high compound value

- explicit AI/agent threat model plus adversarial attack/containment tests;
- independent maintainer/user/open-source validation;
- coherent operational trace/diagnosis evidence;
- concise reviewer-first/employer-facing proof surface.

### Important career capabilities that should not automatically become product features

- independent Python/SQL fluency;
- Linux/process/filesystem diagnosis;
- networking/HTTP/TLS/proxy diagnosis;
- backend/API fundamentals;
- cloud/container fundamentals when useful for deployment practice.

### Explicit current resistance/defer set

Do not treat the following as gaps merely because they appear in job descriptions or the horizon catalog:

- more agents/multi-agent architecture;
- PostgreSQL replacing meaningful SQLite work without a concurrency/query need;
- vector database/RAG without a measured retrieval bottleneck;
- microservices/queues/distributed workers without an operational requirement;
- Kubernetes/multi-cloud;
- large frontend implementation;
- learned ranking/ML before enough data and transparent baselines exist.

## Current-main progression observed while the branch was researching

`main` advanced after branch creation from `ecd11a4a` to observed `862731e0` through two additional Fresh Current CI diagnostic case commits. The changes were confined to `product-simulation/` evidence, not product source/architecture.

Material new evidence:

- FCI002 exposes non-empty current GitHub runtime step data but has matrix/dynamic-name pressure that the current correlator should refuse rather than guess; green pytest does not prove the updated tox dependency was installed/exercised.
- FCI003 also exposes non-empty runtime steps and no matrix, but lacks explicit literal static job `name:` values; the current correlation owner intentionally refuses YAML-job-key → runtime-display-name inference, and green `make` jobs do not by themselves prove exact FastAPI install/exercise.

This is consistent with the branch strategy: trustworthy refusal and located uncertainty can be stronger evidence than forcing a broader positive correlation result. No research-branch rebase/merge is justified merely to ingest these new exposed fixtures; the completed main disposition will be reread at the final reconciliation gate.

## Next research responsibility

Before implementation proposals, design and compare the following at a responsibility level:

1. **Ali-owned capability evidence mechanism** — smallest durable way to record capability claim, exact evidence, current ownership level and next proof without building a second project-management system or proficiency-score bureaucracy.
2. **AI-security signature thread** — smallest 3–5 attack families that naturally exercise current/near-term UpgradePilot trust boundaries, with deterministic invariants, observable blocked/contained effects, residual-risk recording and regression proof.
3. **External validation thread** — maturity trigger, sample size/participant type, structured feedback questions, negative-feedback retention and claim boundary.
4. **Operational diagnosis thread** — operator questions that are currently expensive to answer and the simplest structured event/trace baseline before considering OpenTelemetry or a monitoring stack.
5. **Reviewer-first proof surface** — what an unfamiliar reviewer should understand in approximately 1, 3 and 10 minutes without reading internal governance history.
6. **Separate fundamentals track** — which skills should be practised outside product architecture and how UpgradePilot incidents/data can provide realistic exercises without turning them into product requirements.

Do not create product implementation tasks until these designs make the responsibility, owner, baseline, proof/rejection criteria and career/product boundaries clear.

UP-SKILL:upgradepilot-planning-design
UP-SKILL:upgradepilot-learning-by-doing
