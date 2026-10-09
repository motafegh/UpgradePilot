# Checkpoint persistence, interruption and recovery

**Snapshot:** research `7ae80a07d5fb9180ddb30145ea389bebe6553c5f`, 2026-10-09. See the [package horizon](README.md). This note starts with note 1's encoded material closure. It teaches disposable local stores, not production durability guarantees.

## Three boundaries to keep separate

A Workspace publication declares a coherent revision. A storage engine makes its writes visible according to its transaction protocol. An acknowledgement tells the caller that publication returned successfully. None of these proves that an external acquisition finished or that its result was semantically evaluated.

The useful failure question is: **what coherent state is actually present, and what does the caller know?** A committed revision can exist even if the caller died before receiving acknowledgement. Conversely, an external operation may have completed while its observation was never checkpointed. Recovery cannot infer the missing external outcome from storage success or failure.

Recovery restores recorded historical state without acquisition or native evaluation. Explicit continuation is a separate current-target/premise/authority decision. Deterministic retained-input replay is another separate capability: it executes admitted processing from retained inputs. A restored report is neither canonical recovery nor replay.

## Read the common application boundary first

Open [workspace_checkpoint_stores.py](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/experiments/workspace_checkpoint_stores.py). Both stores use `validate_checkpoint`, `_check_successor` and `RecoveryOutcome`.

`validate_checkpoint` checks bounded non-executing JSON, canonical encoding, the experiment schema, graph/reference integrity and exact re-encoding. This is stronger envelope handling than the original in-memory reader. Its size bounds are research implementation choices, not product retention policy. Hashes detect mismatching bytes; they do not authenticate an evidence producer against malicious replacement.

`_check_successor` requires an explicit expected predecessor. The first publication uses expected `-1` and revision zero; subsequent publication must advance by one. It rejects a changed target/lineage and inconsistent retained identities. It also refuses publication on a corrupt current head, even when an older checkpoint can be inspected. Selecting an old readable revision is not permission to silently resume writing from it.

`RecoveryOutcome` preserves the recovered revision, latest surviving declared revision and rejected candidates. Its summary exposes fallback and retained gaps. If all catalog authority is lost, the store cannot know every declaration that used to exist. An empty catalog must not be interpreted as successful restoration of a complete investigation.

## The file publication protocol

`FileCheckpointStore.publish` follows this order under a bounded Linux writer lock:

```text
validate candidate and expected predecessor
→ check immutable identities against retained historical snapshots
→ write/sync complete temporary checkpoint content
→ link immutable content file and sync its directory
→ write/sync a temporary commit marker
→ link revision-N.commit as publication
→ sync directory, then acknowledge
```

The marker contains the revision and full-checkpoint digest. Content without a marker is unpublished staging and is ignored; recovery does not invent a commit by finding a plausible orphan file. `os.link` supplies non-replacing publication. `os.fsync` requests file persistence, while directory synchronization covers directory-entry changes. These explain the protocol; tested process death does not verify disk/controller behavior under power loss.

The marker catalog is append-only, with no second mutable latest pointer. Recovery enumerates declared candidates newest-first, loads the digest-named content, validates it and returns the first usable complete checkpoint with explicit rejection history. It does not merge fragments from several revisions.

The important historical-ID correction occurred after early green tests. Comparing only against the latest closure allowed an ID omitted from that closure to return with different bytes. The file store now scans older retained snapshots for new-to-current IDs. SQLite's global record table already rejected that change. This makes the file comparison fairer, while exposing the historical-scanning cost of its simpler baseline. The control does not authorize dropping material product history.

## The SQLite publication protocol

The research schema has three tables:

| Table | Meaning |
| --- | --- |
| `records(id, body)` | One immutable serialized record body per retained ID. |
| `revisions(number, header, digest, record_count)` | Revision metadata and expected full-checkpoint integrity. |
| `membership(revision, record)` | The declared records belonging to each checkpoint closure. |

This is an internal storage representation, not the Investigator contract. Foreign keys protect membership references; full reconstructed checkpoint validation remains an application responsibility.

`SQLiteCheckpointStore.publish` validates the candidate, starts `BEGIN IMMEDIATE`, reads the current state in that transaction and checks the expected predecessor. It compares existing record bytes before insertion, inserts new bodies, writes the revision header/membership and commits once. A failure before commit rolls back the transaction. A failure after commit cannot undo the publication merely because the caller has no acknowledgement.

The expected-revision check inside the writer transaction prevents two publishers from advancing from the same predecessor. This protects canonical publication; it does not tell whether a request's evidence basis is still valid. Note 3 supplies that second check.

A recovery reader opens one transaction, reconstructs sorted membership bodies, checks count/digest and validates the full closure. The reader therefore observes one coherent database snapshot rather than mixing successive reads. The writer connection has explicit cached lifetime; readers are independent connections. Opening an existing store uses `mode=rw`, permitting SQLite's own hot-journal recovery without creating a missing database or running domain owners. Historical-only recovery does not mean the engine never writes internally.

The actual configurations were **DELETE/EXTRA** and **WAL/FULL**, with foreign keys enabled, bounded contention and recorded runtime/settings. WAL means write-ahead logging: committed changes can reside in a sidecar before being transferred to the main database. FULL/EXTRA name synchronization settings; they do not by themselves certify this application's durability. In the held-reader trial, DELETE commit timed out, while WAL publication proceeded and the old reader kept its earlier snapshot.

A SQLite WAL checkpoint transfers engine state toward the main database. A Workspace checkpoint declares recoverable investigation knowledge. Their names overlap, but their responsibilities and cadence are different.

## Interpret the interruption evidence precisely

The [trial harness](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/experiments/workspace_checkpoint_trials.py) pauses child processes at named hooks, sends actual SIGKILL and reopens stores. [Recorded E2 evidence](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/working-memory/evidence/2026-10-08-workspace-checkpoint-stores/README.md) reports:

| Stimulus | What was observed, and what it means |
| --- | --- |
| Death before publication of revision 5 | Exact revision 4 returns. Staged work is not canonical. |
| Death after publication, before acknowledgement | Exact revision 5 returns, but the caller's outcome was uncertain. Inspect before considering another effect. |
| Death after acknowledgement | Revision 5 survives this process-death experiment. This is not a power-loss test. |
| Damaged latest content/reference/schema | Reject the damaged revision and expose an earlier valid checkpoint with loss information. Do not publish on the damaged head. |
| Unsupported/damaged store catalog | No usable internal recovery in the tested controls. A separately valid backup may be needed. |
| Competing publishers | Exactly one successor publishes; the other receives stale-publication conflict. No automatic merge/retry. |
| Actual SQLite page-limit exhaustion | `SQLITE_FULL` leaves the prior published state intact. The host disk was not filled. |

The file partial-write hook means half the checkpoint bytes. The SQL partial-write hook means a new record exists inside an uncommitted record set; a BLOB insert is not split into simulated half-bytes. An early SQL hook fired after processing old ignored rows, before fresh data existed. The correction stages new-to-current IDs first, and its independent test observes the fresh uncommitted row while another reader remains at revision 4. A named hook is not sufficient proof that its intended stimulus occurred.

## Backup, progress loss and cost

SQLite backup uses `Connection.backup`, then validates the restored checkpoint. An executed control copied only the main DB while committed state was in WAL and recovered no revision. Supported online backup recovered the declared state. This rejects that demonstrated shortcut; it does not say every raw DB copy always fails.

File backup locks the writer and copies/validates the declared catalog and content. Both supported backup trials preserve every historical trace revision, stay at their captured revision after original advancement and work after removing the temporary original. Simultaneous publication during file copying, backup rotation and production backup policy were not established.

Batching illustrates loss without choosing policy: seven completed local observations checkpointed individually retain seven; publication after batches of four retains four and leaves three pending. The simulation does not renumber old revisions. Lower publication cost comes with a different uncheckpointed progress boundary; main must choose an admitted loss policy before cadence becomes a promise.

Largest-volume medians, for 1,800 material records and eight publications, were:

| Store | Publication total | Restore | Backup |
| --- | ---: | ---: | ---: |
| Files | 5,591.103 ms | 124.956 ms | 1,335.619 ms |
| SQLite DELETE/EXTRA | 3,624.385 ms | 219.278 ms | 249.383 ms |
| SQLite WAL/FULL | 3,557.731 ms | 218.905 ms | 247.591 ms |

The structural explanation matters more than a speed ranking: files duplicate full checkpoint bodies and scan history; SQLite shares immutable bodies and reconstructs membership. File backup validates copied checkpoints, while SQLite's API snapshots engine state followed by application validation. These are different supported application protocols, not isolated engine benchmarks.

Trials used copied corpus volumes, warm local runs and fixed approach order. Copies increase volume, not semantic diversity. `/proc/self/io` was unavailable; physical-write counters are **null**, not zero. Logical TEXT/BLOB growth and footprint do not measure physical write amplification. The runner was corrected to preserve evidence progressively when a later benchmark fails.

The provisional WAL/FULL recommendation follows shared-history/backup savings and reader behavior. Files remain credible and restored faster here. Hybrid, compaction and compression were not measured losing options; they have not earned extra publication/cleanup boundaries from this evidence.

## Proof, depth and fast return

Read [storage tests](https://github.com/motafegh/UpgradePilot/blob/7ae80a07d5fb9180ddb30145ea389bebe6553c5f/experiments/tests/test_workspace_checkpoint_stores.py), especially `test_sigkill_boundaries_distinguish_publication_from_acknowledgement`, `test_identity_guard_survives_disappearance_from_the_current_closure` and `test_sql_partial_stage_hook_follows_the_fresh_uncommitted_record`. The recorded 17 storage tests cover bounded faults, backup, identity and independent stimuli; inherited representation/native anchors add their own scopes.

Missing proof includes power/OS crashes, random interruption inside fsync/commit, network-filesystem/Windows behavior, full native capture/codec, retention cleanup, production continuation and replay. Shared record corruption can affect several SQLite revisions. Hashes and a coherent transaction cannot recover absent material or certify authority.

**Own:** publication versus acknowledgement, recovery versus continuation/replay, complete-state validation and expected-revision coordination. **Understand operationally:** transactions, reader snapshots, sync/link publication, backup and fallback. **Lookup:** SQL/PRAGMA syntax and exact lock timing. **Defer:** engine internals and device durability qualification until a concrete product promise requires them.

Fast return: locate `COMMIT` and marker publication; inspect `_check_successor`; trace one killed writer; inspect `RecoveryOutcome`; compare supported backup with the failed raw-WAL-copy control.

### Transfer questions

1. Why can an unacknowledged revision be present after restart without granting permission to retry an external acquisition?
2. Which failure can an earlier valid checkpoint handle, and which catalog failure prevents discovering it?
3. Why must a returning historical ID be checked beyond the current closure?
4. What does the corrected SQL hook prove that its earlier version did not?
5. What additional policy/proof would be needed before promising users a maximum amount of lost progress?
