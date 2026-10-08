# Experiment 2 — checkpoint stores, interruption and recovery

**Provisional recommendation for review:** carry all-in-SQLite with WAL/FULL into the next comparison. Shared immutable records reduce retained history and backup cost, and WAL permits publication while an older reader remains open. Files remain a credible self-contained snapshot baseline with faster restore here. This is a research recommendation, not product adoption, a selected checkpoint cadence or power-loss proof. Hybrid storage has not earned a trial from this corpus.

## Question, setup and implementations

Can files and SQLite preserve experiment 1's identical declared closure across write/publication/acknowledgement interruption, reject damaged state, support explicit backup and avoid lost updates under competing publishers? The [cycle](../../2026-10-08_workspace-implementation-architecture-research_lbd-cycle.md) preserves the progressive path; the [program](../../../plans/INVESTIGATION_WORKSPACE_IMPLEMENTATION_ARCHITECTURE_RESEARCH_PLAN.md) owns scope. [Experiment 1](../2026-10-08-workspace-revision-representation/README.md) still owns the native corpus/capture limitations. No acquisition, model, evaluator or target code runs during recovery.

The [stores](../../../experiments/workspace_checkpoint_stores.py) accept pre-encoded opaque native records. Files sync a complete closure, link immutable content, sync the directory, then link a revision commit marker and sync again before returning acknowledgement. A bounded Linux `flock` serializes writers; append-only markers/content permit readers to inspect immutable snapshots. Commit markers are the publication catalog, not a second mutable latest pointer. New-to-current IDs are checked against retained older snapshots; this simple baseline pays for history scanning rather than adding a durable identity index.

SQLite stores immutable record bodies once, with revision headers and membership in a single `BEGIN IMMEDIATE` transaction. Full-checkpoint checksums/reference validation remain application duties after commit. Independent transactional readers keep one consistent snapshot; a cached writer has explicit lifetime. [The extracted SQL schema](sqlite-schema.sql) is a research schema; the native codec is still pinned tagged fields without trusted-object hydration/migration.

Three configurations share the same corpus and expected-revision guard: files, DELETE/EXTRA, and WAL/FULL. SQLite 3.45.1 uses foreign keys ON, 250 ms busy timeout, 4,096-byte pages and the recorded default WAL autocheckpoint. EXTRA was chosen for rollback mode after [SQLite synchronization guidance](https://www.sqlite.org/pragma.html#pragma_synchronous) exposed FULL's filesystem-dependent last-commit loss boundary. [WAL guidance](https://www.sqlite.org/wal.html) supplies local-host and reader/checkpoint constraints; these engine descriptions are not application durability evidence. Runtime/settings and raw trials are in [results.json](results.json).

## Correctness and failure evidence

The [process harness](../../../experiments/workspace_checkpoint_trials.py) pauses child processes over pipes, sends actual SIGKILL, reaps them and opens the store afresh. Content/record staging, publication and acknowledgement are separate boundaries. File partial staging means half the bytes; SQL partial staging means a fresh record inserted into an uncommitted record set, not a torn BLOB write. Neither simulates power failure during a filesystem/engine syscall.

| Evidence family | Observed outcome across tested configurations |
| --- | --- |
| 21 SIGKILL trials: seven boundaries × three stores | Before publication: exact revision 4. After publication: exact revision 5. After publication but before acknowledgement: new state exists with uncertain caller outcome. Acknowledged checkpoint survives tested process death. Stored completion unknown/retry permission remains unchanged. |
| 15 latest-content faults: missing/truncated content, changed metadata, unsupported checkpoint version, broken references | Reject revision 4 and expose exact revision 3 with rejection/lost-published-progress information. Rehashed invalid structures still fail. Publication on that damaged current head is refused. |
| Six store-version/catalog faults | No usable checkpoint; no automatic reconstruction. SQLite catalog damage prevents internal earlier-revision fallback; valid separate backup remains necessary. File total catalog damage is also fatal in this control. |
| Six competing/duplicate-input writer races | Exactly one publishes revision 5; the other receives a stale-publication conflict. Duplicate input does not create another revision or independent support. No automatic retry/merge. |
| Three held-reader and three writer-contention trials | All old reads remain revision 4. File/WAL publication proceeds; DELETE commit times out while reader is held, then explicit local publication succeeds after release. A competing writer lock produces bounded busy without advancement. |
| Nine injected storage-refusal trials; two actual SQLITE_FULL controls | Failure before publication leaves revision 4; failure before acknowledgement can leave unacknowledged revision 5. SQLite page-limit exhaustion returns actual SQLITE_FULL and preserves revision 4. Read-only SQLite refusal is covered separately by tests. Host disk was not filled. |
| Three supported backups | Every original trace revision is byte-equal; backup stays at 4 after original advances to 5 and after removing only the temporary original store. SQLite uses the [online backup API](https://www.sqlite.org/backup.html), not DB-file-only copying. |
| Six batching/loss simulations | Of seven completed local observations, batching every observation retains seven; batches of four retain four and lose three pending observations. No already-published revision is renumbered or discarded. This does not select runtime publication/checkpoint cadence. |

Native meanings, explicit gaps, unsupported evaluation and unknown completion survive exact round trips. A newly stored observation remains `not_attempted` for evaluation. Recovery provides historical inspection only; it does not certify semantic sufficiency, restore present authority, or continue external work. The inherited simulated method gap remains visible.

## Failures, rejected shortcuts and reasoning changes

- **Historical identity defect after early green tests:** file snapshots accepted changed bytes when an ID disappeared from the current closure and returned; SQLite rejected them. [Pre-repair control](identity-guard-correction.json) pins both outcomes. File history admission was repaired; same-content reintroduction still succeeds. The deliberately narrowed closure is a guard control, not an admitted product retention policy.
- **Unavailable measurement:** the first full runner failed because `/proc/self/io` was absent. [Probe/failure](measurement-correction.json) is retained. Kernel write counters are now null, never zero. Exact logical retained-value growth and live/closed footprints are measured, with no physical write-amplification claim. The runner now progressively saves each family/benchmark, including failed status, so later failures retain earlier evidence.
- **Weak SQL interruption hook:** [direct probe](partial-write-correction.json) showed the partial hook could fire before inserting the fresh observation. New identities now stage first; the regression checks their uncommitted presence while another reader still sees revision 4. Final trials/timings were rerun on corrected code after tests finished.
- **Executed unsafe WAL backup control:** copying only the main DB while committed state resided in WAL produced no recovered revision; supported backup recovered 4. The raw control in results rejects this shortcut. It does not prove every raw DB copy fails.
- **Unmeasured alternatives:** hybrid blobs, an additional file identity index/cache, compaction, compression, delta/event storage and alternative SQLite membership encodings were deferred, not benchmarked losers. A metadata/blob split would add publication, cleanup and backup boundaries without an observed benefit over shared all-in-SQLite records here.

## Cost evidence and interpretation

Final timings compare 36/360/1,800 material records (1/10/50 corpus copies), eight publications and five trials. Inputs are pre-encoded; initial population is excluded. Publication includes structural validation, identity admission and persistence, not engine-only speed. Restore includes opaque-record validation. Backup includes each store's supported snapshot operation. Copies add volume, not semantic diversity. Fixed approach order/warm caches and this WSL2/Linux i7-12700H environment limit generality.

Largest-volume medians, at 1,800 material records:

| Store | Eight publications (ms) | Restore (ms) | Backup (ms) | Active / closed footprint (decimal MB) |
| --- | ---: | ---: | ---: | ---: |
| Files | 5,591.103 | 124.956 | 1,335.619 | 35.879 / 35.879 |
| SQLite DELETE/EXTRA | 3,624.385 | 219.278 | 249.383 | 6.046 / 6.046 |
| SQLite WAL/FULL | 3,557.731 | 218.905 | 247.591 | 10.036 / 6.046 |

Across those eight publications, exact logical retained-value growth is 31,851,476 bytes for files and 396,240 for either SQLite mode. These measure stored file bytes versus SQLite TEXT/BLOB value lengths; SQLite indexes/integers are excluded from logical growth but included in footprint. They are not physical write counts. At 36 material records, total publication medians are 230.948/163.559/105.306 ms and restore 2.964/5.109/4.604 ms, respectively. Raw ranges and medium-volume rows remain in results. All code hashes and the corpus digest match the final corrected files.

Interpret the comparison structurally: full files duplicate checkpoint bodies and scan historical IDs; SQLite shares native bodies but still stores membership/header history and validates the reconstructed closure. File restore avoids relational reconstruction. File backup validates each copied checkpoint; the SQLite backup API copies the database snapshot, followed by latest-closure validation. These are supported application protocols, not isolated engine benchmarks; the separate trace-backup trial verifies all historical checkpoint bytes. WAL's active footprint includes sidecars and can shrink on close; its periodic engine checkpoint is distinct from a declared Workspace checkpoint. No physical write counter was available, and no throughput requirement or device-durability promise is inferred.

Operational cost remains visible: files need coordinated content/marker sync, writer locking, orphan cleanup and locked backup; SQLite needs explicit settings, schema/version migration, bounded contention, WAL growth management and its supported backup API. Neither implements garbage collection, retention duration, backup publication/rotation, native-codec migration or continuation admission. Shared record corruption may affect several SQLite revisions; self-contained files duplicate that content but can still lose their catalog. Checksums detect accidental damage, not authenticated provenance or malicious rehashing.

## Verification and stop boundary

**17 storage tests + 15 representation tests pass**, plus **58 native/report anchors** and touched Ruff/format/document checks. [Tests](../../../experiments/tests/test_workspace_checkpoint_stores.py) cover independent byte fidelity, exact failure outcomes, real process death, offline/no-evaluator recovery, historical identity, actual engine-full/read-only refusal, target/lineage refusal, held-reader semantics, backups, bounded JSON and progressive failure-evidence preservation. No production source/dependencies/specification/ADR changed.

Rerun from the repository root:

```sh
PYTHONPATH=src .venv/bin/python3 -m unittest experiments.tests.test_workspace_checkpoint_stores experiments.tests.test_workspace_revision_representation -v
PYTHONPATH=src .venv/bin/python3 -m experiments.workspace_checkpoint_trials run --output /tmp/upgradepilot-workspace-experiment-2 --repeats 5
```

Residual boundaries: no power/OS crash, random kill inside commit/fsync, network-filesystem/Windows proof, simultaneous writing during backup copying, arbitrary hostile DB hardening, storage initialization interruption, full product/experiment suite, native hydration, semantic staleness, Investigator integration, product migration or replay. Missing content behind a surviving catalog entry is detected; total catalog deletion can hide the last published revision. No consumer can treat an empty/failed recovery as recovered canonical state. Loss detection beyond surviving metadata requires a separately designed backup/provenance policy.

**Stop at experiment 2 result review.** If separately activated, experiment 3 should test revision-bound Investigator interactions and material-basis revalidation using this provisional store candidate, retaining file comparison evidence and codec/capture debt. Main owns final technology and product decisions; no seam implementation or production integration begins here.
