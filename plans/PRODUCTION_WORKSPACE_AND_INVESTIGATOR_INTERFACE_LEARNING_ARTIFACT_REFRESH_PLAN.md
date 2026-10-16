# Production Workspace and Investigator Interface Learning Artifact Refresh Plan

**Responsibility:** Create a current, evidence-grounded learning package for the production Workspace, lifecycle host, common Investigator evidence interfaces, and current migration frontier; update the learning index so historical snapshots remain clearly historical and the new package becomes the current relearning reference for this responsibility.

**Plan type:** Compact bounded learning-artifact refresh plan. This plan coordinates artifact work only; it does not select product continuation, authorize engineering changes, or replace `MEMORY.md`.

**Artifact-task status:** COMPLETE and merge-ready on `learning/production-workspace-artifact-refresh-2026-10-16`; merge remains explicitly pending Ali's instruction. This status describes this plan artifact only and does not select the live product workstream.

**Working snapshot for this task:** repository base `main@5187f40ba974341eb29d765363f093922a881803`. Product `src/` and `tests/` remain unchanged from the verified common-interface implementation horizon `77d33dc1`; later main commits add planning, input-retention/qualification evidence and prepared future-cycle records. The package therefore teaches the same implemented production architecture while using the newer single repository/evidence horizon for current supporting evidence.

**Procedures:** `UP-SKILL:upgradepilot-planning-design`; `UP-SKILL:upgradepilot-learning-artifact`.

## 1. Outcome and boundaries

Produce one small ordered package under:

```text
learning/2026-10-16-production-workspace-and-investigator-interface/
```

The package should let Ali return later and accurately relearn:

```text
production native capture / reconstruction / publication
→ lifecycle host, material validity and execution truth
→ frozen raw-source + structured native delivery/citation interfaces
→ current end-to-end product flow and migration frontier
```

The package must teach pinned implementation truth, meaningful engineering corrections, real-case evidence and explicit proof/non-proof without becoming a second live-state owner.

### In scope

- current production Workspace Stages 1–3 and their admitted CI/Python-support/native-input scope;
- shared common-input/source-interface preparation implemented for future Investigator work;
- Stage 3 D ownership lessons and common-preparation D1–D4 lessons already preserved in working memory;
- the October 16 durable input-retention repair and newly qualified shared common-input snapshot as current evidence for source-profile/checkpoint availability and fair-comparison inputs;
- current transitional product/migration state, including continued legacy synthesis/report/CLI consumers;
- current accepted owners and directly relevant implementation/migration plans;
- HTTPX and glyphsLib real-case evidence where it materially improves learning;
- `learning/README.md` maintenance needed to point readers to the new package and mark older snapshots accurately.

### Out of scope

- starting, implementing or evaluating the prepared Investigator adapter cycle;
- model/framework/prompt/multi-agent selection or inference runs;
- teaching the selected Qwen/Gemma deployment protocol except where a one-sentence future-boundary note prevents confusion;
- product source/test changes;
- specification/ADR semantic changes;
- Stages 4–6 implementation;
- rewriting historical frozen learning artifacts to match current code;
- merging independent branch-local mastery records as product proof;
- new audio/quiz/flashcard derivatives.

## 2. Authority and evidence route

Use the smallest sufficient chain for each claim:

```text
accepted specification / ADR / implementation plan when it owns the rule
→ pinned production source and focused tests/evidence
→ directly relevant working-memory D/E history and corrections
→ representative real case where useful
→ learning artifact
```

Primary current owners/evidence include:

- `docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md`;
- `docs/architecture/ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md`;
- `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md` §6.4 and related evidence/authority sections;
- `plans/INVESTIGATION_WORKSPACE_IMPLEMENTATION_AND_MIGRATION_PLAN.md`;
- production Workspace/native/host/source-interface source and focused tests at the pinned horizon;
- `working-memory/2026-10-13_2030_workspace-lifecycle-admission-and-material-basis_lbd-cycle.md`;
- `working-memory/2026-10-15_stage3-deferred-d-learning-todo.md`;
- `working-memory/2026-10-14_2345_common-investigator-inputs-and-source-interfaces_lbd-cycle.md`;
- `working-memory/evidence/2026-10-15-common-investigator-preparation/`;
- `working-memory/2026-10-16_1930_project-reentry-and-critical-continuation_lbd-cycle.md` and `working-memory/evidence/2026-10-16-investigator-input-retention/` for durable raw-input retention and the explicit old enriched-bundle loss;
- `working-memory/2026-10-16_2025_common-investigator-input-snapshot_lbd-cycle.md` and `working-memory/evidence/2026-10-16-common-investigator-input-snapshot/` for the new qualified shared freeze and cold-read proof;
- `plans/INVESTIGATOR_INTEGRATION_AND_COMPARATIVE_EVALUATION_PLAN.md` and `working-memory/2026-10-16_2045_investigator-adapter-and-mechanical-qualification_lbd-cycle.md` only to state the future boundary at the pinned horizon; live later progression belongs to `MEMORY.md` and its owning cycle, not this frozen package;
- the Oct 9 research package only as historical predecessor/rationale evidence, never current implementation authority.

Do not use `MEMORY.md` as implementation proof. It may be consulted only to avoid misrepresenting live position or future work.

## 3. Planned learning package

### [x] Artifact 1 — Production native capture, reconstruction and checkpoint publication

Created:

```text
01_native_capture_reconstruction_and_checkpoint_publication.md
```

Covers proportionately:

- why native owners remain semantic owners while capture preserves their exact meaning/material basis;
- `NativeInvestigationCapture`, native representation/codecs and native projection roles;
- partial coherent capture and `not_evaluated` versus empty/negative;
- immutable Workspace revision/publication model;
- SQLite checkpoint publication, predecessor conflict and cold reconstruction;
- version/input/target/resource refusals;
- checkpoint versus saved report;
- recovery proof and explicit non-claims such as power-loss/exactly-once/full-family recovery;
- meaningful Stage 1–2 implementation corrections and what they taught;
- fast relearning route and transfer questions.

### [x] Artifact 2 — Lifecycle host, material validity and execution truth

Created:

```text
02_lifecycle_host_material_validity_and_execution_truth.md
```

Covers proportionately:

- generic host responsibility versus native/domain truth ownership;
- purpose/need/request/admission/attempt/observation/interruption/evaluation lifecycle;
- Basis ≠ Validity ≠ Authority ≠ Publication predecessor;
- intent-before-effect and the difference between `not_started`, completion unknown, completed observation/problem;
- stale/unsupported/valid material basis;
- proposal versus truth and stopping proposal versus procedural termination/adequacy;
- recovery versus continuation/retry/replay;
- first production caller and partial native reassessment;
- real implementation repairs from Stage 3 and their engineering lesson;
- fast relearning route and transfer questions.

### [x] Artifact 3 — Frozen sources, native views, delivery and citations

Created:

```text
03_frozen_sources_native_views_delivery_and_citations.md
```

Covers proportionately:

- shared dependency/CI native preparation and why future treatments share semantic producers;
- `RetainedSourceScope`, `RetainedSourceCatalog` and frozen profile identity;
- source catalog ≠ Workspace and retained content ≠ acquisition;
- `list_sources`, `list_paths`, `search`, `read`, `resolve` strengths and limits;
- `observed`, `empty`, `scoped_negative`, `problem` distinctions;
- search preview ≠ complete delivered evidence;
- `WorkspaceEvidenceAccess`, native whole-view omission and `native_page`;
- `ViewDelivery`, `ContentCitation`, operation receipts/accounting;
- available ≠ delivered ≠ observably used ≠ cited ≠ evaluated support ≠ sufficient ≠ action permission;
- HTTPX and glyphsLib real-case evidence-strength examples;
- common-freeze/fair-comparison rule without designing the next experiment;
- profile versus checkpoint retention/recovery boundary;
- the October 16 retention sequence: original research corpus retained durably, old October 15 enriched bundle explicitly unrecovered, then a new qualified shared freeze established with separate profiles/checkpoints/validated backup and guarded cold reads;
- fast relearning route and transfer questions.

### [x] Artifact 4 — Current end-to-end flow and Workspace migration frontier

Created:

```text
04_current_product_flow_and_workspace_migration_status.md
```

Covers proportionately:

- current top-level production flow from providers/native owners into canonical Workspace;
- coexistence of canonical Workspace state with the still-live `PublicPullRequestInvestigation` compatibility/consumer path;
- current synthesis/report/CLI dependency on the legacy result at the pinned horizon;
- Stage 1/2/3 completed responsibility versus Stage 4/5/6 remaining migration responsibility;
- why legacy removal before parity/coverage would be fake migration;
- how future Investigator work connects without implying full migration is required first;
- the Investigator integration/comparison plan only as a future owner at this snapshot;
- historical Oct 9 research package as predecessor, not current implementation;
- explicit distinction between current fact, accepted target architecture and future work;
- fast relearning route and transfer questions.

### [x] Package README — educational map

Created:

```text
learning/2026-10-16-production-workspace-and-investigator-interface/README.md
```

It contains:

- exact repository/evidence horizon `5187f40...` and the unchanged product implementation horizon it contains;
- authority map;
- four-note reading order and learning outcome;
- relationship to the Oct 9 research package;
- current implementation versus historical-research distinction;
- a fast-return route;
- explicit non-claims that the package selects live project continuation or proves mastery.

## 4. Learning index maintenance

### [x] Update `learning/README.md`

Completed only the index/interpretation changes needed by the new package:

- added the Oct 16 production package as the current production Workspace/Investigator-interface relearning reference;
- kept the Oct 9 package and explicitly described it as the frozen research predecessor;
- revised the Sept 19 `current-end-to-end-product-flow` index description so it is clearly a frozen Sept 19 snapshot, not today's production-architecture reference;
- preserved historical package paths and snapshot contents;
- did not turn the index into a live project tracker or study-order owner.

## 5. Evidence collection checklist

### [x] Production foundation anchors

Inspected pinned native capture/codec/projection/checkpoint/store source, reconstruction/publication tests, ADR-0013 and the Stage 1–2 implementation/proof record.

### [x] Lifecycle-host anchors

Inspected pinned `lifecycle_records.py`, `lifecycle_host.py`, `material_validity.py`, the first production caller, host integration tests, Stage 3 cycle and closed D companion.

### [x] Source/consumer-interface anchors

Inspected pinned `investigation_inputs.py`, `workspace/preparation.py`, `source_access.py`, `consumer_access.py`, lifecycle delivery/citation records, Oct 15 interface qualification, Oct 16 retained-input evidence and the new qualified shared freeze. Their distinct horizons/claims remain explicit.

### [x] Migration/current-flow anchors

Inspected pinned `investigation.py`, `maintainer_action.py`, `report_projection.py`, `cli.py`, Workspace migration plan sections and the future integration plan/prepared adapter record only to delimit future work.

## 6. Quality and proof checklist

For every note:

- [x] pin the exact repository/evidence horizon;
- [x] distinguish current fact, evidenced rationale, engineering judgment and future/deferred work;
- [x] use pinned source/tests as implementation truth rather than working memory alone;
- [x] preserve native/domain authority boundaries;
- [x] include a representative real flow/case where it materially helps;
- [x] include important failure/refusal states and proof/non-proof;
- [x] use `must master / understand operationally / lookup / deferred` depth calibration where useful;
- [x] include a fast relearning route;
- [x] avoid copying owner contracts or session chronology as the artifact body;
- [x] avoid implying future Investigator/model work is implemented;
- [x] avoid silently strengthening historical evidence or conflating the unrecovered October 15 bundle with the newly qualified October 16 freeze.

Package/index QA:

- [x] package-local and owner-relative link targets used by the package were checked against the branch/pinned repository paths; the package directory contains all five intended files;
- [x] snapshot-horizon statements consistently identify `5187f40...`, with older proof counts explicitly labelled by their actual horizons;
- [x] the four notes preserve accepted ADR/spec/plan ownership and do not promote working-memory history over those owners;
- [x] Oct 9 and Sept 19 artifacts remain untouched as frozen snapshots; only their root-index descriptions changed where needed;
- [x] no product source/tests/specifications/ADRs are modified by the learning branch;
- [x] branch diff against `5187f40...` contains only this plan, the new learning package and `learning/README.md`.

## 7. Completion and merge-readiness condition

All seven conditions are satisfied for this artifact task:

1. all four notes and package README are authored and grounded at the declared `5187f40...` horizon;
2. `learning/README.md` points to the new package and accurately labels the relevant historical snapshots without rewriting them;
3. link/snapshot/authority/proof-boundary QA is complete at the bounded artifact scope;
4. no unresolved factual contradiction was found in the new learning material;
5. the branch diff is limited to the learning responsibility and this plan;
6. final comparison against current `main@ea8c2b6bd551e8a7745a17bc02983329892ddf00` shows only later `MEMORY.md`, future Investigator-plan/cycle and local-model-evidence changes after the package horizon—**no `src/` or `tests/` change**. The package therefore remains intentionally pinned to `5187f40...` rather than silently mixing the later live A-phase into this educational snapshot;
7. the branch is merge-ready without claiming or activating the separate future Investigator engineering cycle.

### Final reconciliation disposition

`main` advanced after this package's chosen horizon. The later delta activates and advances the separate Investigator adapter cycle through A0/A1 into A2 and records local-model planning evidence. Those are live/future-work records, not changes to the production Workspace/source-interface implementation taught here. Because `learning/README.md` and this package explicitly treat `MEMORY.md` as the sole live-position owner, retaining the single `5187f40...` snapshot is more truthful than rewriting all learning links/status language to chase the parallel session.

A future production/source change that materially changes one of these responsibilities should earn a new or explicitly revised newer learning snapshot under the normal learning policy.

## 8. Stop line and prohibited scope

STOP now with the branch merge-ready. Do not:

- enter or modify the separately active Investigator adapter cycle from this learning branch;
- implement or run the future Investigator;
- select/qualify models or change its experimental protocol;
- modify production code/tests;
- implement migration Stages 4–6;
- rewrite historical snapshots to current behavior;
- merge to `main` until Ali explicitly requests/approves the merge step.
