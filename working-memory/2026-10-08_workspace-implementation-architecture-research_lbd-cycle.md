# Investigation Workspace implementation architecture research

**Date:** 2026-10-08. **Operation:** Planning/Design preparation, then authorized experiment Build.
**Branch:** `research/workspace-implementation-architecture-2026-10-08`.
**Baseline:** freshly fetched `main = origin/main = 08243e5b3e455ad26ae1cd142763f4d147269bc6`.
**Predecessor:** [main design cycle](2026-10-07_investigation-workspace-and-investigator-interface-design_lbd-cycle.md), a separate responsibility whose D/E review remains open.

## Cycle progression

```text
A0 — DONE: baseline, governance, native/consumer source and research evidence reconciled.
A1 — DONE proportionately: Ali reviewed experiment 1 and authorized the next experiment.
A2 — DONE for experiment boundary: approval plus concrete comparison/proof model presented;
     learner mastery is not inferred. No repeated gate for this continuous-context step.
B — DONE for experiment 2: stores, faults/isolation/backup/loss comparisons and measured costs.
Verification gate — GREEN scoped: 32 experiment tests, 58 native/report anchors, final runner/static/document checks.
D — CURRENT for experiment 2 result review; experiment 1 review accepted, no learner mastery inferred.
E — PENDING: research gaps/closure; experiments 3–4 remain unactivated.
C — CONTINUOUS: retain meaningful reconciliation, decisions, evidence and handoff here.
```

## Scope and cadence adjustment

Ali explicitly requested a complete first increment: reconcile latest main, identify open decisions/reuse/risks, propose bounded research, then stop before substantial implementation/prototyping. This authorizes branch creation and preparation artifacts, not production adoption.

Circumstance/evidence → explicit preparation-only deliverable and review stop; no technology or executable seam is being selected.
Normal route → separate A1 and A2 stops before substantive analysis/design B.
Why worse here → stopping after onboarding alone would leave the expressly requested review package incomplete and require approval before there is a concrete program to assess.
Override → combine A1/A2 orientation with bounded read-only investigation and program drafting; retain the user-requested stop before any substantial prototype.
Effect → planning artifacts only, no source/test/runtime changes, no inferred understanding or technology acceptance; result review and D/E remain open.
Reconciliation → record this adjustment here and branch-local selection in `MEMORY.md`; future experiment activation requires review of the concrete program.

## Living orientation map

- Continuity: accepted B2 canonical Workspace direction; B3/B4 conceptual lifecycle and recovery proposal; `08243e5b` separates recovery from retained-input replay. ADR-0012 remains Proposed and Core has no §6.4 insertion.
- Upcoming responsibility: turn open representation/storage/seam/migration choices into comparisons with shared inputs and explicit failure or loss outcomes. Native facts and synthesis permission keep their current owners.
- Important bridge: frozen `PublicPullRequestInvestigation` result → evolving canonical Workspace → consumer projections; recovered checkpoint → historical inspection → separately validated continuation.
- Proof boundary: source inspection and documentation checks establish a grounded program, not working persistence, semantic evaluation, replay, or model quality.
- Ownership targets for review: explain which material dependencies must survive a checkpoint and why revision mismatch alone cannot determine staleness.

## Reconciliation observations

- `git fetch origin main` succeeded; `main...origin/main` was `0/0`; new branch starts exactly at main. The unrelated untracked `2026-10-03_broad-project-and-future-plans-audit_lbd-cycle.md` is preserved and excluded.
- User calls main's boundaries reviewed; repository labels ADR-0012 and Core recovery delta Proposed. Research treats them as constraints as instructed, without editing acceptance status or closing main's design cycle.
- The older B4 checklist bullet in the design record still says CURRENT, while its top block, later completed B4 evidence and `MEMORY.md` say DONE. Use the later reconciliation; do not rerun or edit main's historical checklist here.
- Native acquisition/evaluation precedes the frozen result; report save/open persists a selective report, not canonical state. Current synthesis supports explained abstention only.

## Preparation result and evidence

The [research program](../plans/INVESTIGATION_WORKSPACE_IMPLEMENTATION_ARCHITECTURE_RESEARCH_PLAN.md) separates eight open implementation questions from main-owned boundaries. Its reuse ledger traces native producers → fixed orchestration → synthesis/report → offline save/open. Material workflow/environment/source inputs are locally composed rather than retained as a complete bundle; upstream extraction history is also incomplete. These are capture/retention research risks, not authorization for universal raw capture or duplicate validation.

Prioritized program: (1) material dependency closure plus revision representation; (2) file/SQLite checkpoint comparison and conditional hybrid trial, including interruption/fault/concurrency/backup evidence; (3) scripted Investigator seam with material-basis invalidation; (4) replacement migration proof. Recommend activating only the first experiment after review. No technology winner, schema adoption or product capability is established.

The 2026-09-08 persistence proposal is historical: its no-save CLI and export-first entry context do not control the new recovery responsibility. The pinned H1 proposal at `253b48de20b475eada48810d193bd420c51aa7d4` was inspected via Git; its corpus backend is not canonical Workspace and its pure-view/native-input questions inform seam pressure only. No other worktree changed and no messages were sent to that workstream. H1's design-only status is a pinned observation, not a live status refresh.

Fresh verification: `PYTHONPATH=tests:src .venv/bin/python3 -m unittest test_ci_dependency_state test_conditional_pyproject_consumption test_python_support_impact test_impact_applicability test_report test_report_file` — **58 PASS**. This reruns native/report anchors from latest main; it does not exercise Workspace state, durability, crash recovery, concurrency, migration or model quality. No full product/experiment suite, live model, installed-package or hosted verification is warranted by this preparation-only diff.

Document verification: three touched documents, 38 local link occurrences and fenced blocks pass; selective repository internal-link, normative-ID uniqueness and audit-lifecycle checks pass; `git diff --check` passes. No protected executable or accepted-contract owner changed. Full governance doctor is not rerun; main's inherited `examples/` marker finding remains historical debt, not a fresh result or a repair target here.

## Preparation review frontier (superseded by experiment 1 approval)

Review the ordered program and experiment 1's retention/representation boundary before substantial prototyping. Main's formal ADR/Core acceptance stays with main. D/E remain open; agreeing the program does not establish learner ownership or a technology choice. A meaningful ownership discussion can explain why retaining a final assessment without its material evaluation basis is inadequate, and why an unrelated revision update need not invalidate a delayed same-target observation.

## Experiment 1 — authorization, hypothesis and setup

Ali approved experiment 1 only and required progressive, decision-relevant research history in this existing cycle/evidence structure. Preserve hypotheses/setup, attempted approaches, material results, failures/surprises, negative results, rejected alternatives, reasoning changes, limits and next questions; omit routine command logs. This standing branch requirement belongs here and in branch-local `MEMORY.md`, not a new documentation system.

Fresh fetch on resumption: `origin/main` remains `08243e5b`; branch HEAD is preparation `05d427ba`. No owner/source delta changes the experiment. User approval authorizes the already oriented experiment responsibility → normal fresh-cycle gate repetition would interrupt that explicit continuation → continue this same cycle with a concrete pre-change model and preserve proof/ownership limits. No technology/adoption or later experiment is authorized.

**Hypothesis:** immutable record payloads and explicit material-reference closure can preserve the same declared history/basis in both direct immutable successor construction and mutable draft plus frozen publication. Their real difference should be update/publication cost and uncommitted-draft handling, not stronger evidence authority. Both must reject identity collisions, preserve old views, expose missing content and avoid flattening failed/empty/unsupported/interrupted states.

**Setup:** no provider/model calls or production mutations. Use current native CI, dependency/conditional-extra and grounded support-drop/target-relevance paths on disclosed synthetic offline inputs. Preserve native fields/type identities and exact supplied UTF-8 source content at this pinned experiment boundary; avoid asserting real GitHub acquisition. Simulated lifecycle records supply proposal/request/evaluation/view/attempt variation with clearly separate authority. Two stores share the same immutable records and comparison traces; independent expected outcomes complement differential equality.

**Initial simpler-baseline decisions:** compare shallow copies of record indexes with shared immutable payload bytes rather than deep-copying full native content at every revision. Do not add delta/event-store machinery before measuring this adequate baseline. The draft checkpoint is an in-memory versioned encoding, not a file/database persistence implementation or production native-object migration codec. Named consumers determine material roots; arbitrary unreferenced history must not accidentally substitute for a closure declaration.

### First prototype observations and reasoning corrections

Native corpus execution succeeds without model/provider calls: CI contains both `RequirementSatisfiedAtCommandCompletion` and an unresolved `process_environment_value_unresolved` problem; optional selection retains `changed_requirement_marker_not_evaluated`; native support applicability moves `unresolved → established_applicable` only after target relevance. No source acquisition or general interpretation quality is established by these fixtures.

Both revision approaches yield byte-identical in-memory checkpoint closures on the initial trace. Early review strengthened the comparison: the mutable approach now exposes a genuine `stage → publish_pending` boundary, instead of merely wrapping a mutable dictionary in the same publication API. Staged work stays outside historical checkpoints. Material triggering-record links are explicit; a candidate trigger implementation that repeatedly walked closure for every updated record would have distorted comparison with avoidable quadratic work, so closure is computed once per publication. This is source-review correction before measurement, not an observed performance failure.

Three deliberately executed cheaper controls are rejected: a read-only proxy over the mutable draft leaks newly addressable records into old views; retaining only the final runtime result passes structural round-trip validation but omits independently required workflow/source basis; and a content digest cannot distinguish identical empty content under different scopes. The second control changes the reasoning: graph reachability plus successful encoding is not a completeness oracle. Capture ownership/consumer obligations must be checked independently rather than assumed from a green graph validator.

The evolving regression suite has 13 focused tests passing, including independent native outcomes, historical stability, failed-batch rollback, scoped identity/duplicate/annotation behavior, gap-versus-empty preservation, failed/unsupported/unknown outcomes, material invalidation, staged publication, offline/no-model execution and the negative controls. Timing/serialization/allocation measurements and complete evidence review remain pending. Ruff is absent from the repository venv/PATH; resolve only the validation-tool location, without changing product dependencies.

### Unexpected fixture incoherence and correction

A separate exact-source identity probe found **one real setup defect** after the first green comparison: support and optional-extra consumers supplied different `pyproject.toml` bytes at the same repository/head/path. The independent probe and both conflicting texts/digests are preserved in [setup-correction.json](evidence/2026-10-08-workspace-revision-representation/setup-correction.json). Differential equality was insufficient because both representations consumed the same inconsistent corpus.

Repair: construct one shared exact project input and binding for both native consumers; check immutable source identity/content consistency across binding IDs in publication and structural import. Added regression rejects inconsistent content even when IDs differ; same-content aliases remain possible without independent support. Delivery-order variation also preserves native meanings/target identity while retaining original trigger ordering as history. This is an experiment setup/ingestion correction, not a contradiction in main's contract.

Fifteen focused tests now pass; touched Ruff/format checks pass with Ruff 0.16.10 in an invocation-owned `/tmp` validation directory. No project dependency/environment owner changed. The native tagged-field encoding remains tied to inspected code and does not rehydrate trusted native objects. Material edge traversal is a conservative dependency-impact aid, not a semantic stale/adequacy decision; retention/history relations may need finer roles before product adoption.

### Measured result and resulting recommendation

The [experiment evidence](evidence/2026-10-08-workspace-revision-representation/README.md) contains the named-consumer/capture ledger, schema descriptor, concrete checkpoint, setup failure and complete measurements. All five revisions (including zero) preserve identical declared closures across both approaches. Final closure: 36/37 addressable records, 80,115 encoded bytes, 62,410 payload bytes, one explicit simulated method gap. One diagnostic is excluded. Native fields and exact source bytes remain inspectable without native-object hydration or implicit evaluator/provider calls.

Five-trial comparisons use 37/370/1,850 starting records, 30 updates and batches of 1/10. At 1,850 records, immutable/draft total update medians are 14.555/13.025 ms for batch 1 and 1.618/1.381 ms for batch 10; encode/decode medians span 16.906–18.121/12.844–13.385 ms. Separate peak index allocations span 1,864–1,919 KiB for batch 1 and 409–460 KiB for batch 10, excluding prebuilt immutable payload bytes. All raw ranges, environment and exact file/native-tree hashes are pinned in results. This is fixed-order local volume pressure, not semantic generality, a throughput promise, disk or power-loss evidence.

**Reasoning update:** publication granularity affects measured cost more than the choice of draft versus direct immutable successor. Both must freeze an owned index at publication; the draft adds staging/rollback responsibility. Recommend **immutable published revisions with shared immutable native payloads** as a provisional simpler baseline, reserving drafts for a concrete consumer need. No evidence currently earns deltas/event-store machinery. Batching also changes the uncheckpointed progress boundary, so defer cadence to the explicit durability comparison rather than choose it from these timings.

Another pressure correction: exact source-text records are just 1,002 bytes of this fixture's payload; nested native result encodings dominate (runtime 18,849; coverage 14,662). This argues for inspecting native schema/normalization and retained reference roles before assuming blob size earns hybrid persistence. The full pinned tagged-field encoding is useful fidelity evidence, not a stable native migration codec or permission to retain every field universally. Undeclared material edges still evade structural checks; capture completeness must remain an independent consumer obligation.

### Verification and experiment result-review boundary

Fresh proof: 15 focused experiment regressions PASS; the same six native/report anchor modules rerun with 58 PASS. Touched Ruff/format checks pass using isolated validation tooling; source hashes/checkpoint bytes, local documentation links/fences, selective governance and diff checks pass. Production source/tests/dependencies and accepted spec/ADR owners are unchanged. The plan's preparation-only status/stop wording is reconciled to delegate activation/progress to its existing live/cycle owners, without changing experiment scope.

No full suite, live acquisition/model, durable publication, crash/power-loss recovery, concurrency, executable Investigator seam, native-object codec/migration, production cutover or replay is established. No genuine contradiction with main emerged: the inconsistent fixture and insufficient graph oracle were experiment setup/proof discoveries. Detailed parser hardening, metadata integrity, missing provenance, source-family breadth, relation roles and retention policy remain explicit gaps.

The recommendation and reasoning path are ready for **experiment 1 result review**. D learner ownership and E gap repair/closure stay open; no mastery is inferred from test success or approval. Useful review reasoning: why graph round-trip success missed the inconsistent/incomplete fixture; why content digest is distinct from scoped identity; and why batching cannot select the durability promise. Stop before experiment 2/storage prototypes. If separately approved, file/SQLite interruption/publication comparison is next because correct declared closure must survive real store faults, while capture/codec debt remains visible.

## Experiment 2 — authorization, hypothesis and setup

Ali's “Good go and continue next” accepts experiment 1's review boundary and authorizes the next planned checkpoint-store experiment, not the rest of the program or product adoption. Continue the same research cycle/evidence structure; repeating fresh A1/A2 gates would obstruct this explicit continuous-context instruction. Present the concrete failure model before coding, preserve review/ownership limits and stop again at experiment 2 results. Fresh fetch confirms unchanged main `08243e5b`; branch is synchronized at `01c3bc40`; unrelated broad-audit file stays excluded.

**Question/hypothesis:** can self-contained file snapshots and all-in-SQLite native-record snapshots restore the same declared material closure after process interruption, refuse corrupted/incomplete publication, preserve ambiguous attempts, and reject competing stale publication? Compare correctness before costs. Successful database commit is not completeness or semantic authority; an earlier valid fallback is explicit historical inspection, never silent continuation or permission to retry external work.

**Pre-change model:** file content is synced before an immutable revision commit marker, with serialized expected-revision publication and directory sync before acknowledgement. SQLite shares immutable record bodies through revision membership/header rows in one transaction. Both protect the entire encoded checkpoint, validate exact predecessor/target/lineage, preserve experiment 1's declared gaps, and restore opaque historical records without native evaluator/provider/model calls. Two writer processes race the same expected revision; readers observe coherent snapshots; explicit backup creates a separately validated snapshot. No automatic external-operation retries or canonical-state repair.

**Setup/alternatives:** compare file snapshots, SQLite DELETE journal and SQLite WAL on the same corpus plus volume-scaled copies. SQLite documentation inspection corrected a tempting default before implementation: `synchronous=FULL` in rollback mode may lose the last commit on power loss; use DELETE/EXTRA and WAL/FULL, both with foreign keys enabled and recorded runtime/settings. This is setup reasoning, not a measured failure or power-loss proof. WAL requires local-host storage; process kills and injected faults cannot validate actual disk/controller flush behavior. Hybrid remains conditional: experiment 1's 1,002 source-text bytes and dominating nested native payloads do not independently earn an external blob boundary; reconsider only after storage/backup measurements.

**Proof program:** actual SIGKILL at named write/publication/ack boundaries; missing/truncated/damaged content, broken references, schema refusal, unavailable storage, explicit fallback/lost progress; supported file/SQLite backups; observation retained before evaluation; duplicate/competing publishers, lock contention and reader isolation; update/restore/backup latency and retained logical/physical bytes. Disclose incomplete native codec/capture/authority validation, warm-cache/volume-only scope, directory/catalog total loss, power-loss and absent production continuation/migration/replay. The experiment owns storage representation and fault research, not new product recovery semantics.

### First storage observations and corrections

Initial 13 focused storage tests passed: actual process death before publication restores revision 4, after publication restores 5; losing acknowledgement does not undo commit. Five latest-content faults expose explicit revision-3 fallback; version/catalog damage can prevent any recovery. Both SQLite modes refuse real `SQLITE_FULL` induced by a page limit and read-only writes. Supported backups preserve every trace revision after deleting only the experiment-owned original. An executed DB-file-only WAL copy loses the committed catalog while online backup retains revision 4; this rejects the shortcut, not SQLite itself.

Independent historical-identity probe after those green tests found a **real prototype guard mismatch**: drop an annotation from the current declared closure, then reintroduce changed bytes under its older ID. File snapshots admitted it, while normalized SQLite records rejected it. The deliberately narrowed closure is an identity control, not acceptance of incomplete product history. [Pre-repair outcomes/code hash](evidence/2026-10-08-workspace-checkpoint-stores/identity-guard-correction.json) preserve the discovery. Repair: file publication checks new-to-current IDs against retained historical snapshots; no second durable index is added. A regression covers changed and exact-same reintroduction. Historical scanning is now an explicit cost of the simpler file baseline; performance must not reward its previous weaker identity check.

Source review also corrected a misleading batching simulation before measurements: renumbering already-created in-memory revisions would hide skipped lineage. Now accumulate completed local observations and publish one revision per batch without renumbering; simulate losing only pending observations. This demonstrates the lost-progress trade-off, not permission to discard canonical revision history or a selected runtime checkpoint cadence. No main contract contradiction or semantic change is inferred.

### Measurement failure and evidence-preservation repair

The first complete runner reached benchmarking after its fault-family assertions, then failed because `/proc/self/io` is absent in this runtime. A discriminating probe confirms neither self nor explicit-PID I/O file exists although `/proc/self` and CPU data exist. [Measurement correction](evidence/2026-10-08-workspace-checkpoint-stores/measurement-correction.json) pins that failure and the pre-repair runner hash. This is unavailable measurement evidence, not a store failure; do not substitute zero or claim physical write amplification. Record kernel counters as null and compare exact logical retained TEXT/BLOB value growth plus active/quiescent footprints, disclosing engine/index/IO differences.

The failed runner also exposed a preservation weakness: raw fault results were written only after every benchmark completed. Repair the existing runner to flush each meaningful evidence family/benchmark with in-progress/failed/complete status, so a later failure retains earlier evidence rather than requiring retrospective reconstruction. Add a small measurement regression exercising unavailable counters and exact restore equality. Repeat full final comparison after this repair; the first failed run remains separately preserved rather than counted as successful.

### Final fault-boundary review before ranking costs

After a complete preliminary comparison, a direct hook-time probe found the SQL partial-write stage processed old `INSERT OR IGNORE` rows before the fresh observation: the hook fired with no fresh record inserted. [Observed states/pre-repair hash](evidence/2026-10-08-workspace-checkpoint-stores/partial-write-correction.json) preserve the proof weakness. Repair: stage new-to-current identities first and expose the hook after the first record statement. A SQL BLOB insertion is atomic; this is partial record-set staging, not a simulated torn BLOB syscall. The added regression checks fresh uncommitted presence and an independent reader still at revision 4, then committed revision 5. This sharpens the actual SIGKILL control rather than claiming a database failure.

Preliminary volume evidence favours shared SQLite bodies for retained footprint/backup and full files for restore latency; DELETE held-readers block commit while WAL/file readers do not. Do not rank those preliminary timing samples as final: repeat corrected code after test processes finish, avoiding test/benchmark overlap. Final evidence must match exact source hashes and preserve all fault-family outcomes progressively. Native/source/codec authority and total catalog-loss limits remain unchanged.

### Final result, recommendation and experiment 2 review boundary

[Final experiment 2 evidence](evidence/2026-10-08-workspace-checkpoint-stores/README.md) links corrected stores/harness/tests, extracted SQL schema, final raw results and three preserved correction probes. The complete final runner pins branch base `01c3bc40`, native source tree, code hashes, corpus digest, hardware/filesystem and actual SQLite settings; each meaningful result family is progressively preserved. Final timing starts after the test processes finish. The earlier measurement failure/preliminary timings are not promoted as the final comparison.

Fresh focused proof: **17 storage tests + 15 representation tests PASS (32 total)**; a directly rerun hook assertion also passes after its harmless closure-binding lint correction. **58 native/report anchors PASS** on unchanged product source. Final runner completes 21 SIGKILL trials, 21 corruption/schema trials, six writer races, three held readers, three contention trials, nine injected refusals, three all-history backups, six pending-observation loss simulations, two actual SQLITE_FULL cases and one unsafe-WAL-copy control. Touched Ruff/format, exact-source hashes, JSON/schema/document integrity, selective governance and diff checks pass. These are experimental storage/retention proofs, not a full product or experiment suite or production canonical recovery.

Observed outcomes: deaths before publication restore exact revision 4; after publication restore 5, with ambiguous caller outcome until acknowledgement. Missing/damaged latest content gives explicit revision-3 fallback and blocks publication on the corrupt current head; store schema/catalog damage can prevent any internal recovery. Exactly one competing or duplicate-input writer advances. DELETE's held reader prevents commit within the bounded timeout; WAL/file publication proceeds while the old view remains stable. Supported backups preserve every trace revision after original advancement/removal; a raw main-DB-only WAL copy loses the committed catalog. Unknown completion, unsupported evaluation, original native bytes and inherited retention gap remain explicit. No recovery path calls native evaluators/providers/models or gains live continuation permission.

Largest volume (1,800 material records, eight publications, five trials): file/DELETE/WAL publication medians **5,591.103 / 3,624.385 / 3,557.731 ms**; restores **124.956 / 219.278 / 218.905 ms**; backups **1,335.619 / 249.383 / 247.591 ms**. Footprints are **35.879 / 6.046 / 10.036 MB** while active and **35.879 / 6.046 / 6.046 MB** after close. Logical retained-value growth is **31,851,476 bytes** for full files versus **396,240** for either SQLite mode; this excludes SQLite index/integer bytes and does not establish IO amplification. All kernel write counters remain null. Smaller-corpus raw ranges are retained; volume copies, warm caches and differing supported backup/validation paths limit generality.

**Recommendation:** carry **all-in-SQLite WAL/FULL** as a provisional next-experiment candidate. Its global immutable record storage and one transaction reduce history/backup cost, and WAL provides the required reader/writer isolation behavior without DELETE's held-reader commit block. This does not select production technology; file snapshots remain a credible simpler inspection/restore baseline, and their identity-scanning/copy costs might admit alternative indexing later if a concrete need earns it. Hybrid is not activated: nested native result encoding/history duplication, not large raw source bytes, is the observed pressure, and shared SQLite bodies already reduce it without another publication/cleanup/backup boundary. No delta/event-store, compression or compaction machinery is earned by these results alone.

Residual proof/design debt remains native codec/rehydration/versioning, complete material capture/relation roles, authoritative live continuation and semantic staleness, retention/GC/backup publication policy, shared-body corruption across older revisions, hostile DB hardening, total catalog loss, initialization interruption, OS/power loss and random interruption inside commit/fsync, Windows/network-filesystem behavior, simultaneous writing during backup copy, Investigator integration, migration and replay. The batch-loss simulation preserves completed pending observations versus published revisions without rewriting lineage; it is not a selected canonical revision/checkpoint cadence. These are named research limitations, not silently narrowed product responsibility. No genuine contradiction in main's reviewed semantics emerged; discovered guard/hook failures belonged to the prototypes/proof setup.

**Stop for experiment 2 result review.** D review/learner ownership and E gap repair/closure remain open. Useful ownership reasoning: why a transaction cannot substitute for closure validation; how a committed but unacknowledged checkpoint differs from unknown external execution; why a copied SQLite main file can omit committed WAL state; and why missing catalog authority cannot be silently rebuilt. If separately approved, experiment 3's revision-bound Investigator interaction/material-basis revalidation is next. Production source/dependencies/specification/ADR owners and the unrelated broad-audit file stay untouched.

## Provenance

`UP-SKILL:upgradepilot-repository-audit`
`UP-SKILL:upgradepilot-planning-design`
`UP-SKILL:upgradepilot-working-memory`
`UP-SKILL:upgradepilot-build-implement`
