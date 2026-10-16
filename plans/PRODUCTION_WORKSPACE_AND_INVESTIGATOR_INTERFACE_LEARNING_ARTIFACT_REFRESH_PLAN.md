# Production Workspace and Investigator Interface Learning Artifact Refresh Plan

**Responsibility:** Create a current, evidence-grounded learning package for the production Workspace, lifecycle host, common Investigator evidence interfaces, and current migration frontier; update the learning index so historical snapshots remain clearly historical and the new package becomes the current relearning reference for this responsibility.

**Plan type:** Compact bounded learning-artifact refresh plan. This plan coordinates artifact work only; it does not select product continuation, authorize engineering changes, or replace `MEMORY.md`.

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
- `plans/INVESTIGATOR_INTEGRATION_AND_COMPARATIVE_EVALUATION_PLAN.md` and `working-memory/2026-10-16_2045_investigator-adapter-and-mechanical-qualification_lbd-cycle.md` only to state the future boundary: the adapter cycle is prepared but not started;
- the Oct 9 research package only as historical predecessor/rationale evidence, never current implementation authority.

Do not use `MEMORY.md` as implementation proof. It may be consulted only to avoid misrepresenting live position or future work.

## 3. Planned learning package

### [ ] Artifact 1 — Production native capture, reconstruction and checkpoint publication

Create:

```text
01_native_capture_reconstruction_and_checkpoint_publication.md
```

Must cover proportionately:

- why native owners remain semantic owners while capture preserves their exact meaning/material basis;
- `NativeInvestigationCapture`, native representation/codecs and native projection roles;
- partial coherent capture and `not_evaluated` versus empty/negative;
- immutable Workspace revision/publication model;
- SQLite checkpoint publication, predecessor conflict and cold reconstruction;
- version/input/target/resource refusals;
- checkpoint versus saved report;
- recovery proof and explicit non-claims such as power-loss/exactly-once/full-family recovery;
- meaningful Stage 1–2 implementation corrections and what they taught;
- fast relearning route and 3–5 transfer questions.

### [ ] Artifact 2 — Lifecycle host, material validity and execution truth

Create:

```text
02_lifecycle_host_material_validity_and_execution_truth.md
```

Must cover proportionately:

- generic host responsibility versus native/domain truth ownership;
- purpose/need/request/admission/attempt/observation/interruption/evaluation lifecycle;
- Basis ≠ Validity ≠ Authority ≠ Publication predecessor;
- intent-before-effect and the difference between `not_started`, completion unknown, completed observation/problem;
- stale/unsupported/valid material basis;
- proposal versus truth and stopping proposal versus procedural termination/adequacy;
- recovery versus continuation/retry/replay;
- first production caller and partial native reassessment;
- real implementation repairs from Stage 3 and their engineering lesson;
- fast relearning route and 3–5 transfer questions.

### [ ] Artifact 3 — Frozen sources, native views, delivery and citations

Create:

```text
03_frozen_sources_native_views_delivery_and_citations.md
```

Must cover proportionately:

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
- the later October 16 retention sequence: original research corpus retained durably, old October 15 enriched bundle explicitly unrecovered, then a new qualified shared freeze established with separate profiles/checkpoints/validated backup and guarded cold reads. Teach this as input/provenance lifecycle evidence, not as a new product-interface implementation;
- fast relearning route and 3–5 transfer questions.

### [ ] Artifact 4 — Current end-to-end flow and Workspace migration frontier

Create:

```text
04_current_product_flow_and_workspace_migration_status.md
```

Must cover proportionately:

- current top-level production flow from providers/native owners into canonical Workspace;
- coexistence of canonical Workspace state with the still-live `PublicPullRequestInvestigation` compatibility/consumer path;
- current synthesis/report/CLI dependency on the legacy result where still true at the pinned horizon;
- Stage 1/2/3 completed responsibility versus Stage 4/5/6 remaining migration responsibility;
- why legacy removal before parity/coverage would be fake migration;
- how future Investigator work connects without implying full migration is required first;
- the new Investigator integration/comparison plan only as a future owner, with its adapter/mechanical-qualification cycle explicitly prepared but not started at this horizon;
- historical Oct 9 research package as predecessor, not current implementation;
- explicit distinction between current fact, accepted target architecture and future work;
- fast relearning route and 3–5 transfer questions.

### [ ] Package README — educational map

Create:

```text
learning/2026-10-16-production-workspace-and-investigator-interface/README.md
```

It should contain only what improves relearning:

- exact repository/evidence horizon `5187f40...` and the unchanged product implementation horizon it contains;
- authority map;
- four-note reading order and learning outcome;
- relationship to the Oct 9 research package;
- current implementation versus historical-research distinction;
- one short fast-return route;
- explicit non-claim that the package selects live project continuation or proves mastery.

## 4. Learning index maintenance

### [ ] Update `learning/README.md`

Make only index/interpretation changes needed by the new package:

- add the new Oct 16 production package as the current production Workspace/Investigator-interface relearning reference;
- keep the Oct 9 package and describe it as the frozen research predecessor;
- revise the Sept 19 `current-end-to-end-product-flow` index description so it is clearly a frozen Sept 19 snapshot, not today's architecture reference;
- preserve all historical package paths and snapshot contents;
- do not turn the index into a current-project tracker or study-order owner.

## 5. Evidence collection checklist

Before drafting each artifact, record/verify the minimum exact anchors needed for its claims.

### [ ] Production foundation anchors

Inspect current pinned versions of the relevant native capture/codec/projection/checkpoint/store source and focused reconstruction/publication tests plus Stage 1–2 evidence/learning records.

### [ ] Lifecycle-host anchors

Inspect current pinned `lifecycle_records.py`, `lifecycle_host.py`, `material_validity.py`, first production caller, host integration tests, Stage 3 cycle and closed D companion.

### [ ] Source/consumer-interface anchors

Inspect current pinned `investigation_inputs.py`, `workspace/preparation.py`, `source_access.py`, `consumer_access.py`, lifecycle delivery/citation records, new consumer tests, the Oct 15 public-safe evidence packet, and the Oct 16 retained/new-freeze qualification evidence. Preserve their distinct horizons and claims.

### [ ] Migration/current-flow anchors

Inspect current pinned `investigation.py`, `maintainer_action.py`, `report_projection.py`, `cli.py`, relevant migration-plan sections and tests that prove the compatibility/current-consumer boundary. Read the new integration plan/prepared adapter record only to delimit future work; do not import its model/protocol details into current implementation claims.

## 6. Quality and proof checklist

For every note:

- [ ] pin the exact repository/evidence horizon;
- [ ] distinguish current fact, evidenced rationale, engineering judgment and future/deferred work;
- [ ] use current source/tests as implementation truth rather than working memory alone;
- [ ] preserve native/domain authority boundaries;
- [ ] include at least one representative real flow/case where it materially helps;
- [ ] include important failure/refusal states and proof/non-proof;
- [ ] use `must master / understand operationally / lookup / deferred` depth calibration where useful;
- [ ] include a fast relearning route;
- [ ] avoid copying large owner contracts or session chronology;
- [ ] avoid implying future Investigator/model work is implemented;
- [ ] avoid silently strengthening historical evidence or conflating the unrecovered October 15 bundle with the newly qualified October 16 freeze.

Package/index QA:

- [ ] all relative links resolve on the task branch;
- [ ] all snapshot-horizon statements are consistent;
- [ ] the four notes do not contradict accepted ADR/spec/plan owners;
- [ ] Oct 9 and Sept 19 artifacts remain intact as frozen snapshots;
- [ ] no product source/tests/specifications/ADRs are modified;
- [ ] branch diff contains only this plan plus `learning/` artifact/index work unless a separately justified artifact correction is required.

## 7. Completion and merge-readiness condition

This task is complete when:

1. all four notes and package README are authored and grounded at one declared repository/evidence horizon;
2. `learning/README.md` points to the new package and accurately labels superseded/historical snapshots without rewriting them;
3. link/snapshot/authority/proof-boundary QA passes;
4. no unresolved factual contradiction remains in the new learning material;
5. the branch diff is limited to the learning responsibility and this plan;
6. a final comparison against then-current `main` determines whether another reconciliation is needed before merge;
7. the final branch can be merged without claiming or activating the separately prepared future Investigator engineering cycle.

If `main` advances materially while this package is being authored, do not silently mix horizons. Either keep the package pinned to `5187f40` and label it explicitly, or deliberately reconcile to a newer single horizon before final QA and update all affected snapshot statements consistently.

## 8. Stop line and prohibited scope

STOP after the package/index is merge-ready. Do not:

- start the prepared Investigator adapter cycle;
- implement or run the future Investigator;
- select or qualify a model/framework/topology;
- modify production code/tests;
- implement migration Stages 4–6;
- rewrite historical snapshots to current behavior;
- merge to `main` until the package has passed final branch-vs-main reconciliation and Ali requests/approves the merge step.
