# Workspace migration scope for API evidence delivery — third-subject discussion

## Responsibility and artifact boundary

This is the substantive record for the third subject Ali requested separately after the [intentional-limits/migration review](2026-10-26_intentional-limits-and-workspace-migration_review-cycle.md): what remains of Workspace migration, which parts the chosen product milestone needs, and when deferred parts must be revisited. The [integration design cycle](2026-10-28_pr-driven-caller-signature-integration_design-cycle.md) owns the active phase progression; this record is supporting discussion evidence, not another live-position or cycle-status owner.

Ali has selected integration **design**. The recommendations below are reviewable proposals, not acceptance of a new product family, report schema, full migration sequence or implementation. No source/store/frozen result is changed by this record.

## What migration means here

The accepted target is native producers/evaluators → one canonical Workspace with retained material/history → direct consumer/report projections. Migration is incomplete because substantial report/synthesis work still consumes legacy result fields and several native/delivery responsibilities are unfinished. It is not a second independent investigation producing competing conclusions: current native owners run once, and existing legacy result fields are still delivered alongside the native revision.

At the inspected f55d7108 source horizon, initial dependency/CI/runtime/upstream/Python-support material and PR description have native capture/reconstruction, with specific direct consumers. There is no API caller/signature native family or full API report consumer. Frozen source catalogs are data backends, not canonical investigation state. Native immutable revisions/store/backup/recovery foundations exist, while normal default publication remains volatile and public full-investigation continuation/recovery delivery is not complete.

Authority remains [ADR0012](../docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md), [ADR0013](../docs/architecture/ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md), Core recovery semantics and the [migration plan](../plans/INVESTIGATION_WORKSPACE_IMPLEMENTATION_AND_MIGRATION_PLAN.md). Do not replace those owners with an experiment bundle or a new architecture in this discussion.

## Recommended distinction

| Delivery responsibility | Requirement / proposed disposition |
| --- | --- |
| Ordinary experimental source discovery and comparison | May use existing experiment catalog/saved result mechanisms with explicit ordinary proof class, full needed source closure and offline inspection; does not claim canonical recovery/product adoption |
| Normal product use of API evidence | Requires product-owned admitted types/method, native family/codec/material-input closure, direct Workspace consumer and report compatibility proof before it is called implemented product behavior |
| All-domain artifact/synthesis/full-report cutover | Remains named migration debt. The API feature does not complete it, but it is not shown to be a prerequisite for proving an isolated ordinary source path |
| Public durable recovery/continuation delivery | Separate user-facing capability; local experiment files or library checkpoint support are insufficient |
| Deterministic replay | Separate execution/proof boundary; neither offline report/source opening nor Workspace recovery discharges it |
| Legacy retirement | Requires actual consumer cutover, preserved native semantics, supported cold reconstruction and no remaining independent compatibility obligation |

The recommendation is to earn one useful bounded ordinary experimental path, then perform a deliberate minimal native/API consumer adoption contract. Do not import experiments into product, add parallel API fields to PublicPullRequestInvestigation as permanent truth, wrap everything in a generic evidence blob or require all Workspace migration before the source method can be evaluated.

## Minimum product-adoption contract to settle

1. **Native responsibility and material basis:** product-owned source association/observations, source units, correspondence candidates and conditional binding outcomes. Reuse existing native dependency inputs and preserve role/version/dispatch conditions. Decide family boundaries by ownership/versioning, not one family per file or one universal wrapper.
2. **Retained closure:** exact source text or an explicitly supported retained material reference, source/target identity, source-chain and receiver premises, method/configuration identity, attempts/problems/omissions and historical conclusions. Missing bytes remain unavailable; a path/hash alone cannot support offline source inspection.
3. **Explicit reconstruction:** fixed owner/version/type tables under ADR0013; no source imports, AST reanalysis, checker/synthesis rerun, dynamic class hydration or live fallback on restore. API unsupported history must remain inspectable/refused at the affected boundary without corrupting other families.
4. **One-way consumer:** native source/evaluation records → API evidence projection → ordinary report/source view. Do not re-evaluate bindings in each renderer or convert source candidates into accepted findings/action permission.
5. **Compatibility and actual delivery:** settle report representation/method version and old-report handling; prove the normal CLI/PR path reaches the admitted consumer and saved reopening preserves evidence/unknowns. A separate experimental text view does not satisfy this.

Exact family layout, source packing versus references, report/version compatibility and consumer-cutover changes need their own concrete review before product Build. This cycle does not invent those schema decisions. The first explanation milestone may still emit abstain; stronger maintainer actions are not prerequisites for meaningful evidence delivery.

## Alternatives and product consequences

- Completing all Workspace migration first would address broader delivery debt, but has not been shown necessary to establish ordinary source discovery. It expands the immediate responsibility to unrelated domains and postpones evidence about whether the source path is useful.
- Immediate product adoption before ordinary discovery proof would add native/schema/consumer maintenance before the producer responsibility is demonstrated. ADR0011 calls for experimental qualification before promotion; better presentation cannot compensate for missing ordinary sources.
- Ordinary experimental proof with an explicit adoption gate is the recommended sequence. Its cost is that the next trial is still not the full product milestone. That cost is visible and time-bounded by concrete pass/reject/stop conditions, rather than an excuse for endless experiments.

This is a staged path to the existing canonical target, not a reduced replacement architecture. If source discovery fails, preserve the exact missing owner/premise and decide repair/narrow/defer rather than automatically add another model trial or source archive.

## Re-entry and stopping triggers

- **Before any normal-product API adoption:** resolve the minimum native/consumer contract above. Missing closure or report access is a blocker to claiming the agreed milestone complete.
- **After useful ordinary proof:** explicitly choose native/report adoption versus a reasoned defer/reject disposition before selecting more capability experiments. Reconcile the parent plan/live owner; do not silently defer delivery indefinitely.
- **Before claiming whole-investigation recovery or removing legacy plumbing:** return to the full migration ledger, artifact/synthesis/full-report coverage, durable user delivery and supported history/continuation tests.
- **On real contradictory truth, dropped source or inability to recover a required consumer:** investigate the earliest sufficient owner and repair a demonstrated defect. Partial migration alone is not proof of such a defect.

Outstanding learning: source catalog versus canonical state, recovery versus continuation/replay, and why product adoption needs an explicit native consumer. Guided explanation can progress with the current design; no independent mastery or completed migration is inferred from agreement.
