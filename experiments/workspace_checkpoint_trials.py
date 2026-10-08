"""Process/fault/backup/volume harness for experiment-local Workspace stores.

Run `python -m experiments.workspace_checkpoint_trials run --output ...`. Native
fixtures are constructed only in the coordinator, never during recovery or child writes.
Workers receive pre-encoded input and pause at named boundaries over pipes; SIGKILL
therefore tests real process death, not a caught exception masquerading as a crash.
Persistent test stores live only in disposable temp directories. JSON evidence is public
synthetic data. This does not test power loss, live continuation or semantic evaluation.
"""

from __future__ import annotations

import argparse
import errno
import json
import os
import platform
import select
import shutil
import signal
import sqlite3
import statistics
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from experiments.workspace_checkpoint_stores import (
    PHASES,
    SQL_SCHEMA,
    STORE_KINDS,
    FileCheckpointStore,
    SQLiteCheckpointStore,
    StoreBusy,
    StoreDamaged,
    canonical_json,
    digest,
    open_store,
    physical_bytes,
)
from experiments.workspace_revision_representation import (
    ImmutableSuccessorHistory,
    TraceRecord,
    encode_checkpoint,
)


def trace_history():
    from experiments.workspace_retention_corpus import build_retention_corpus

    corpus = build_retention_corpus()
    history = ImmutableSuccessorHistory(corpus.target)
    for step in corpus.steps:
        history.publish(*step)
    return history


def successor(history, name="observation:recorded"):
    """A simulated observation is retained before any evaluator is invoked."""
    previous = history.history[-1]
    record = TraceRecord(
        name,
        "experiment.lifecycle",
        "observation",
        "offline",
        b'{"content":"new observation","evaluation":"not_attempted"}',
        ("admission",),
    )
    return history.publish((record,), previous.roots + (name,))


def seed_store(kind, root, history):
    store = open_store(kind, root, create=True)
    for revision in history.history:
        store.publish(encode_checkpoint(revision), expected=revision.number - 1)
    return store


def _emit(value):
    print(json.dumps(value), flush=True)


def worker(args):
    store = open_store(args.kind, args.root)

    def hook(phase):
        _emit({"event": "phase", "phase": phase})
        if phase == args.pause and sys.stdin.readline() == "":
            raise RuntimeError("Coordinator disappeared")

    try:
        if args.action == "publish":
            data = Path(args.checkpoint).read_bytes()
            hook("ready")
            number = store.publish(data, expected=args.expected, hook=hook)
            hook("acknowledged")
            _emit({"event": "result", "status": "published", "revision": number})
        elif args.action == "reader":
            if isinstance(store, SQLiteCheckpointStore):
                connection = store.connect()
                try:
                    connection.execute("BEGIN")
                    before = store.recover_connection(connection).summary()
                    hook("reader_open")
                    held = store.recover_connection(connection).summary()
                finally:
                    connection.close()
            else:
                revision = store.recover().revision
                before = store.recover().summary()
                hook("reader_open")
                held = {
                    "recovered_revision": revision.number,
                    "checkpoint_digest": digest(encode_checkpoint(revision)),
                }
            _emit(
                {
                    "event": "result",
                    "status": "read",
                    "before": before,
                    "held": held,
                    "fresh": store.recover().summary(),
                }
            )
        elif args.action == "hold_writer":
            if isinstance(store, FileCheckpointStore):
                with store.writer_lock():
                    hook("writer_locked")
            else:
                connection = store.connect()
                try:
                    connection.execute("BEGIN IMMEDIATE")
                    hook("writer_locked")
                finally:
                    connection.rollback()
                    connection.close()
            _emit({"event": "result", "status": "released"})
    except (ValueError, RuntimeError, OSError, sqlite3.DatabaseError) as exc:
        _emit({"event": "result", "status": type(exc).__name__, "problem": str(exc)})
    finally:
        store.close()


def start_worker(kind, root, action, *, checkpoint=None, expected=4, pause="ready"):
    args = [
        sys.executable,
        "-m",
        "experiments.workspace_checkpoint_trials",
        "worker",
        "--kind",
        kind,
        "--root",
        str(root),
        "--action",
        action,
        "--expected",
        str(expected),
        "--pause",
        pause,
    ]
    if checkpoint is not None:
        args.extend(("--checkpoint", str(checkpoint)))
    # Binary unbuffered pipes avoid hidden TextIO read-ahead interfering with select.
    return subprocess.Popen(
        args,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=0,
    )


def await_phase(process, target):
    phases, buffer = [], bytearray()
    deadline = time.monotonic() + 10
    while time.monotonic() < deadline:
        ready, _, _ = select.select(
            [process.stdout], [], [], max(0, deadline - time.monotonic())
        )
        if not ready:
            break
        char = process.stdout.read(1)
        if not char:
            raise AssertionError(
                f"Worker exited before {target}: {process.stderr.read().decode()}"
            )
        buffer.extend(char)
        if char == b"\n":
            item = json.loads(buffer)
            buffer.clear()
            if item["event"] == "result":
                raise AssertionError(f"Worker failed before {target}: {item}")
            phases.append(item["phase"])
            if item["phase"] == target:
                return phases
    process.kill()
    process.communicate(timeout=5)
    raise AssertionError(f"Worker timeout before {target}")


def release_worker(process):
    process.stdin.write(b"continue\n")
    output, error = process.communicate(timeout=10)
    assert process.returncode == 0 and not error, (process.returncode, error)
    return [json.loads(line) for line in output.splitlines() if line][-1]


def kill_trial(kind, phase, history):
    with tempfile.TemporaryDirectory(prefix="up-workspace-kill-") as temporary:
        base = Path(temporary)
        root = base / "store"
        with seed_store(kind, root, history):
            pass
        next_revision = successor_history(history)
        data = encode_checkpoint(next_revision)
        input_path = base / "input.json"
        input_path.write_bytes(data)
        process = start_worker(
            kind, root, "publish", checkpoint=input_path, pause=phase
        )
        seen = await_phase(process, phase)
        os.kill(process.pid, signal.SIGKILL)
        output, error = process.communicate(timeout=5)
        assert process.returncode == -signal.SIGKILL and not error, (output, error)
        with open_store(kind, root) as store:
            recovered = store.recover()
        expected_revision = (
            4 if PHASES.index(phase) < PHASES.index("after_publish") else 5
        )
        assert recovered.revision.number == expected_revision, recovered.summary()
        assert encode_checkpoint(recovered.revision) == (
            data if expected_revision == 5 else encode_checkpoint(history.history[-1])
        )
        assert (
            recovered.revision.records["attempt:unknown"].payload
            == history.history[-1].records["attempt:unknown"].payload
        )
        return {
            "kind": kind,
            "kill_phase": phase,
            "exit_code": process.returncode,
            "phases_seen": seen,
            "ack_seen": "acknowledged" in seen,
            "new_checkpoint_visible": expected_revision == 5,
            "unacknowledged_publication": expected_revision == 5
            and "acknowledged" not in seen,
            "unpublished_files": len(list(root.glob(".content-*")))
            + len(list(root.glob(".marker-*"))),
            **recovered.summary(),
        }


def successor_history(history, name="observation:recorded"):
    clone = ImmutableSuccessorHistory(history.history[0].target)
    clone.history = list(history.history)
    return successor(clone, name)


def damage_checkpoint(store, mode):
    """Deliberate local corruption, sometimes rehashed to pressure structural checks."""
    if mode == "store_version":
        if isinstance(store, FileCheckpointStore):
            for marker in store.root.glob("revision-*.commit"):
                body = json.loads(marker.read_bytes())
                body["version"] = 2
                marker.write_bytes(canonical_json(body))
        else:
            with sqlite3.connect(store.path) as connection:
                connection.execute("PRAGMA user_version=2")
        return
    if mode == "catalog_damage":
        if isinstance(store, FileCheckpointStore):
            for marker in store.root.glob("revision-*.commit"):
                marker.write_bytes(b"damaged catalog")
        else:
            with store.path.open("r+b") as stream:
                stream.write(b"damaged catalog!")
        return
    if isinstance(store, FileCheckpointStore):
        data = store._load(4)
    else:
        connection = store.connect()
        try:
            data = store._load(connection, 4)
        finally:
            connection.close()
    body = json.loads(data)
    if mode in ("missing_content", "truncated_content"):
        if isinstance(store, FileCheckpointStore):
            path = store.root / f"content-{digest(data)}.json"
            if mode == "missing_content":
                path.unlink()
            else:
                path.write_bytes(data[: len(data) // 2])
        else:
            with sqlite3.connect(store.path) as connection:
                # Only revision 4 references this annotation; bypass FK for a fault.
                if mode == "missing_content":
                    connection.execute("DELETE FROM records WHERE id='annotation'")
                else:
                    connection.execute(
                        "UPDATE records SET body=? WHERE id='annotation'", (b"{",)
                    )
        return
    if mode == "metadata_damage":
        body["target"] = "changed target"
    elif mode == "checkpoint_version":
        body["version"] = 2
    elif mode == "broken_reference":
        body["records"] = [
            record for record in body["records"] if record["id"] != "ci:workflow-text"
        ]
    else:
        raise ValueError(mode)
    modified = canonical_json(body)
    # Valid hash with invalid structure is distinct from ordinary damaged bytes.
    hash_value = digest(data) if mode == "metadata_damage" else digest(modified)
    if isinstance(store, FileCheckpointStore):
        (store.root / f"content-{hash_value}.json").write_bytes(modified)
        (store.root / "revision-4.commit").write_bytes(
            canonical_json({"version": 1, "revision": 4, "digest": hash_value})
        )
    else:
        with sqlite3.connect(store.path) as connection:
            records = body.pop("records")
            connection.execute(
                "UPDATE revisions SET header=?, digest=?, record_count=? WHERE number=4",
                (canonical_json(body), hash_value, len(records)),
            )
            connection.execute("DELETE FROM membership WHERE revision=4")
            connection.executemany(
                "INSERT INTO membership VALUES (4,?)",
                ((entry["id"],) for entry in records),
            )


DAMAGE_MODES = (
    "missing_content",
    "truncated_content",
    "metadata_damage",
    "checkpoint_version",
    "broken_reference",
    "store_version",
    "catalog_damage",
)


def damage_trial(kind, mode, history):
    with tempfile.TemporaryDirectory(prefix="up-workspace-damage-") as temporary:
        root = Path(temporary) / "store"
        with seed_store(kind, root, history) as store:
            store.close()
            damage_checkpoint(store, mode)
            recovered = store.recover()
            expected = None if mode in ("store_version", "catalog_damage") else 3
            assert (
                None if recovered.revision is None else recovered.revision.number
            ) == expected, recovered.summary()
            assert recovered.rejected
            if expected is not None:
                assert encode_checkpoint(recovered.revision) == encode_checkpoint(
                    history.history[expected]
                )
            try:
                store.publish(encode_checkpoint(successor_history(history)), expected=4)
            except (StoreDamaged, sqlite3.DatabaseError):
                publication_refused = True
            else:
                raise AssertionError("Published on damaged current state")
            return {
                "kind": kind,
                "fault": mode,
                "publication_refused": publication_refused,
                "lost_published_revisions": [4] if expected == 3 else list(range(5)),
                **recovered.summary(),
            }


def race_trial(kind, history, *, duplicate=False):
    with tempfile.TemporaryDirectory(prefix="up-workspace-race-") as temporary:
        base = Path(temporary)
        root = base / "store"
        with seed_store(kind, root, history):
            pass
        paths = []
        for index in range(2):
            path = base / f"writer-{index}.json"
            path.write_bytes(
                encode_checkpoint(
                    successor_history(
                        history,
                        "observation:one"
                        if duplicate or index == 0
                        else "observation:two",
                    )
                )
            )
            paths.append(path)
        processes = [
            start_worker(kind, root, "publish", checkpoint=path) for path in paths
        ]
        for process in processes:
            await_phase(process, "ready")
        for process in processes:
            process.stdin.write(b"continue\n")
        results = []
        for process in processes:
            output, error = process.communicate(timeout=10)
            assert process.returncode == 0 and not error, error
            results.append([json.loads(line) for line in output.splitlines()][-1])
        assert sorted(item["status"] for item in results) == [
            "StalePublication",
            "published",
        ], results
        with open_store(kind, root) as store:
            recovered = store.recover()
        assert recovered.revision.number == 5
        assert (
            sum(
                key in recovered.revision.records
                for key in ("observation:one", "observation:two")
            )
            == 1
        )
        return {
            "kind": kind,
            "duplicate_inputs": duplicate,
            "writers": results,
            **recovered.summary(),
        }


def reader_trial(kind, history):
    with tempfile.TemporaryDirectory(prefix="up-workspace-reader-") as temporary:
        root = Path(temporary) / "store"
        with seed_store(kind, root, history) as store:
            process = start_worker(kind, root, "reader", pause="reader_open")
            await_phase(process, "reader_open")
            try:
                store.publish(encode_checkpoint(successor_history(history)), expected=4)
                write_status = "published"
            except StoreBusy:
                write_status = "blocked_by_reader"
            result = release_worker(process)
            assert (
                result["before"]["recovered_revision"]
                == result["held"]["recovered_revision"]
                == 4
            )
            assert (
                result["before"]["checkpoint_digest"]
                == result["held"]["checkpoint_digest"]
            )
            assert write_status == (
                "blocked_by_reader" if kind == "sqlite-delete" else "published"
            ), result
            if write_status == "blocked_by_reader":
                store.publish(encode_checkpoint(successor_history(history)), expected=4)
            assert store.recover().revision.number == 5
            return {
                "kind": kind,
                "write_while_reader_held": write_status,
                "reader": result,
                "post_release_revision": 5,
            }


def contention_trial(kind, history):
    with tempfile.TemporaryDirectory(prefix="up-workspace-lock-") as temporary:
        root = Path(temporary) / "store"
        with seed_store(kind, root, history) as store:
            process = start_worker(kind, root, "hold_writer", pause="writer_locked")
            await_phase(process, "writer_locked")
            try:
                store.publish(encode_checkpoint(successor_history(history)), expected=4)
            except StoreBusy:
                status = "bounded_busy"
            else:
                raise AssertionError("Competing publication bypassed writer lock")
            result = release_worker(process)
            assert store.recover().revision.number == 4
            return {"kind": kind, "status": status, "holder": result}


def injected_failure_trial(kind, phase, history):
    with (
        tempfile.TemporaryDirectory(prefix="up-workspace-refusal-") as temporary,
        seed_store(kind, Path(temporary) / "store", history) as store,
    ):

        def refuse(current):
            if current == phase:
                raise OSError(
                    errno.ENOSPC, "simulated storage exhaustion at named boundary"
                )

        try:
            store.publish(
                encode_checkpoint(successor_history(history)),
                expected=4,
                hook=refuse,
            )
        except OSError as exc:
            problem = str(exc)
        else:
            raise AssertionError("Refusal did not fail publication")
        recovered = store.recover()
        expected = 5 if phase == "before_ack" else 4
        assert recovered.revision.number == expected
        return {
            "kind": kind,
            "fault": "injected_ENOSPC",
            "phase": phase,
            "acknowledged": False,
            "problem": problem,
            **recovered.summary(),
        }


def backup_trial(kind, history):
    with tempfile.TemporaryDirectory(prefix="up-workspace-backup-") as temporary:
        base = Path(temporary)
        root = base / "store"
        with seed_store(kind, root, history) as store:
            start = time.perf_counter_ns()
            with store.backup(base / "backup") as backup:
                elapsed = time.perf_counter_ns() - start
                original_digest = digest(encode_checkpoint(store.recover().revision))
                restored = backup.recover()
                assert restored.summary()["checkpoint_digest"] == original_digest
                if isinstance(backup, FileCheckpointStore):
                    historical = [digest(backup._load(number)) for number in range(5)]
                else:
                    connection = backup.connect()
                    try:
                        historical = [
                            digest(backup._load(connection, number))
                            for number in range(5)
                        ]
                    finally:
                        connection.close()
                assert historical == [
                    digest(encode_checkpoint(revision)) for revision in history.history
                ]
                store.publish(encode_checkpoint(successor_history(history)), expected=4)
                assert backup.recover().revision.number == 4
                store.close()
                shutil.rmtree(
                    root
                )  # Only the experiment-owned temp store, never user data.
                assert (
                    backup.recover().summary()["checkpoint_digest"] == original_digest
                )
                return {
                    "kind": kind,
                    "backup_ns": elapsed,
                    "backup_bytes": physical_bytes(base / "backup"),
                    "all_history_byte_equal": True,
                    "original_removed": True,
                    **restored.summary(),
                }


def cadence_trial(kind, history, cadence):
    with (
        tempfile.TemporaryDirectory(prefix="up-workspace-cadence-") as temporary,
        seed_store(kind, Path(temporary) / "store", history) as store,
    ):
        clone = ImmutableSuccessorHistory(history.history[0].target)
        clone.history = list(history.history)
        checkpointed = 0
        pending = []
        # Seven completed local observations. Only published batches are revisions;
        # do not renumber skipped canonical revisions to manufacture cadence evidence.
        for update in range(1, 8):
            pending.append(
                TraceRecord(
                    f"observation:{update}",
                    "experiment.lifecycle",
                    "observation",
                    "offline",
                    canonical_json({"completed_observation": update}),
                    ("admission",),
                )
            )
            if update % cadence == 0:
                previous = clone.history[-1]
                revision = clone.publish(
                    tuple(pending),
                    previous.roots + tuple(record.record_id for record in pending),
                )
                store.publish(encode_checkpoint(revision), expected=previous.number)
                pending.clear()
                checkpointed = update
        recovered = store.recover()
        retained = sum(
            f"observation:{i}" in recovered.revision.records for i in range(1, 8)
        )
        assert retained == checkpointed
        return {
            "kind": kind,
            "cadence_updates": cadence,
            "completed_local_updates": 7,
            "checkpoint_acknowledged_through_update": checkpointed,
            "uncheckpointed_updates_lost": 7 - checkpointed,
            "proof_class": "deterministic unpublished-observation loss simulation; no skipped/renumbered canonical revisions",
        }


def _io_write_bytes():
    try:
        return int(
            next(
                line.split(":", 1)[1]
                for line in Path("/proc/self/io").read_text().splitlines()
                if line.startswith("write_bytes:")
            )
        )
    except (OSError, StopIteration, ValueError):
        return None  # Unknown is not zero; storage proof does not need this counter.


def _retained_value_bytes(store):
    """Exact retained TEXT/BLOB lengths; excludes engine indexes/integers and IO writes."""
    if isinstance(store, FileCheckpointStore):
        return physical_bytes(store.root)
    connection = store.connect()
    try:
        return sum(
            connection.execute(query).fetchone()[0]
            for query in (
                "SELECT coalesce(sum(length(CAST(id AS BLOB))+length(body)),0) FROM records",
                "SELECT coalesce(sum(length(header)+length(CAST(digest AS BLOB))),0) FROM revisions",
                "SELECT coalesce(sum(length(CAST(record AS BLOB))),0) FROM membership",
            )
        )
    finally:
        connection.close()


def sqlite_full_trial(kind, history):
    """Real SQLITE_FULL via the engine page limit, not host disk exhaustion."""
    with (
        tempfile.TemporaryDirectory(prefix="up-workspace-full-") as temporary,
        seed_store(kind, Path(temporary) / "store", history) as store,
    ):
        connection = store._writer
        pages = connection.execute("PRAGMA page_count").fetchone()[0]
        connection.execute(f"PRAGMA max_page_count={pages}")
        clone = ImmutableSuccessorHistory(history.history[0].target)
        clone.history = list(history.history)
        record = TraceRecord(
            "storage:pressure",
            "experiment.lifecycle",
            "observation",
            "offline",
            b"x" * 1024 * 1024,
        )
        revision = clone.publish(
            (record,), history.history[-1].roots + (record.record_id,)
        )
        try:
            store.publish(encode_checkpoint(revision), expected=4)
        except sqlite3.OperationalError as exc:
            assert exc.sqlite_errorcode == sqlite3.SQLITE_FULL, exc
            problem = str(exc)
        else:
            raise AssertionError("Engine page bound did not refuse new content")
        assert store.recover().revision.number == 4
        return {
            "kind": kind,
            "engine_error": "SQLITE_FULL",
            "page_limit": pages,
            "problem": problem,
            "recovered_revision": 4,
            "scope": "engine page-limit exhaustion; host filesystem not filled",
        }


def wal_backup_negative_control(history):
    with (
        tempfile.TemporaryDirectory(prefix="up-workspace-unsafe-copy-") as temporary,
        seed_store("sqlite-wal", Path(temporary) / "store", history) as store,
    ):
        destination = Path(temporary) / "db-only"
        destination.mkdir()
        shutil.copyfile(store.path, destination / store.path.name)
        with open_store("sqlite-wal", destination) as copied:
            raw = copied.recover()
            restored_number = None if raw.revision is None else raw.revision.number
        with store.backup(Path(temporary) / "supported-backup") as backup:
            supported = backup.recover().revision.number
        assert restored_number != 4 and supported == 4
        return {
            "question": "Can copying the main SQLite file replace online backup while WAL is live?",
            "wal_bytes": (store.root / "workspace.sqlite3-wal").stat().st_size,
            "raw_main_file_copy": raw.summary(),
            "supported_backup_revision": supported,
            "rejected": True,
            "reason": "Committed state can reside in WAL; DB-file-only copy lost the published catalog.",
        }


def _stats(values):
    return {"median": statistics.median(values), "min": min(values), "max": max(values)}


def storage_benchmark(kind, final, copies, repeats, updates=8):
    from experiments.run_workspace_revision_comparison import _scaled_records

    records, roots = _scaled_records(final, copies)
    history = ImmutableSuccessorHistory(final.target, "storage-volume")
    history.publish(records, roots)
    encoded = [encode_checkpoint(history.history[-1])]
    for i in range(updates):
        previous = history.history[-1]
        record = TraceRecord(
            f"storage-update:{i}",
            "experiment.lifecycle",
            "annotation",
            "offline",
            canonical_json({"update": i}),
            (roots[0],),
        )
        history.publish((record,), previous.roots + (record.record_id,))
        encoded.append(encode_checkpoint(history.history[-1]))
    publications, restores, backups, footprints, writes, quiescent, retained_growth = (
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    )
    settings = None
    for _ in range(repeats):
        with tempfile.TemporaryDirectory(prefix="up-workspace-benchmark-") as temporary:
            base = Path(temporary)
            with open_store(kind, base / "store", create=True) as store:
                if isinstance(store, SQLiteCheckpointStore):
                    settings = store.settings()
                store.publish(encode_checkpoint(history.history[0]), expected=-1)
                store.publish(encoded[0], expected=0)
                before_write = _io_write_bytes()
                before_values = _retained_value_bytes(store)
                durations = []
                for offset, data in enumerate(encoded[1:], start=1):
                    start = time.perf_counter_ns()
                    store.publish(data, expected=offset)
                    durations.append(time.perf_counter_ns() - start)
                publications.append(sum(durations))
                after_write = _io_write_bytes()
                writes.append(
                    None
                    if before_write is None or after_write is None
                    else after_write - before_write
                )
                retained_growth.append(_retained_value_bytes(store) - before_values)
                start = time.perf_counter_ns()
                recovered = store.recover()
                restores.append(time.perf_counter_ns() - start)
                assert encode_checkpoint(recovered.revision) == encoded[-1]
                footprints.append(physical_bytes(base / "store"))
                start = time.perf_counter_ns()
                with store.backup(base / "backup") as backup:
                    backups.append(time.perf_counter_ns() - start)
                    assert encode_checkpoint(backup.recover().revision) == encoded[-1]
            quiescent.append(physical_bytes(base / "store"))
    return {
        "kind": kind,
        "copies": copies,
        "starting_material_records": len(history.history[1].records) - copies,
        "updates": updates,
        "repeats": repeats,
        "total_publish_ns": _stats(publications),
        "restore_ns": _stats(restores),
        "backup_ns": _stats(backups),
        "active_store_bytes": _stats(footprints),
        "closed_store_bytes": _stats(quiescent),
        "kernel_accounted_write_bytes": None if None in writes else _stats(writes),
        "logical_retained_value_bytes_added": _stats(retained_growth),
        "write_measurement_limit": "Logical value growth is not physical write amplification; kernel counters may be unavailable",
        "preencoded_checkpoint_bytes_submitted": sum(len(data) for data in encoded[1:]),
        "settings": settings,
        "scope": "validation + persistence; pre-encoding/initial population excluded, cached writer, warm local filesystem",
    }


def run(output, repeats):
    history = trace_history()
    files = [
        Path("experiments/workspace_checkpoint_stores.py"),
        Path("experiments/workspace_checkpoint_trials.py"),
        Path("experiments/tests/test_workspace_checkpoint_stores.py"),
    ]
    results = {
        "protocol": "checkpoint-store-comparison-v1",
        "git_head_at_run": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "native_source_tree": subprocess.check_output(
            ["git", "rev-parse", "HEAD:src"], text=True
        ).strip(),
        "code_sha256": {str(path): digest(path.read_bytes()) for path in files},
        "corpus_checkpoint_sha256": digest(encode_checkpoint(history.history[-1])),
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "sqlite_runtime": sqlite3.sqlite_version,
            "cpu": next(
                line.split(":", 1)[1].strip()
                for line in Path("/proc/cpuinfo").read_text().splitlines()
                if line.startswith("model name")
            ),
            "logical_cpus": os.cpu_count(),
            "temp_filesystem": subprocess.check_output(
                ["stat", "-f", "-c", "%T", tempfile.gettempdir()], text=True
            ).strip(),
        },
        "status": "in_progress",
        "limits": [
            "SIGKILL and injected faults do not establish power-loss durability",
            "Opaque native codec and declared gaps/capture limits inherited from experiment 1",
            "No automatic repair, live continuation, semantic staleness, migration or replay",
            "Total catalog removal/valid malicious replacement requires external provenance/backup policy",
            "Logical retained-value growth is not IO amplification; unavailable kernel counters are null",
            "Hybrid not activated without a demonstrated blob/backup advantage",
        ],
    }
    output.mkdir(parents=True, exist_ok=True)
    (output / "sqlite-schema.sql").write_text(SQL_SCHEMA)

    def preserve():
        # Research evidence replacement, separate from canonical store publication.
        temporary = output / ".results.tmp"
        temporary.write_text(json.dumps(results, indent=2) + "\n")
        temporary.replace(output / "results.json")

    preserve()
    families = (
        (
            "kill_trials",
            lambda: [
                kill_trial(kind, phase, history)
                for kind in STORE_KINDS
                for phase in PHASES
            ],
        ),
        (
            "damage_trials",
            lambda: [
                damage_trial(kind, mode, history)
                for kind in STORE_KINDS
                for mode in DAMAGE_MODES
            ],
        ),
        (
            "writer_races",
            lambda: [
                race_trial(kind, history, duplicate=duplicate)
                for kind in STORE_KINDS
                for duplicate in (False, True)
            ],
        ),
        ("held_readers", lambda: [reader_trial(kind, history) for kind in STORE_KINDS]),
        (
            "contention",
            lambda: [contention_trial(kind, history) for kind in STORE_KINDS],
        ),
        (
            "injected_failures",
            lambda: [
                injected_failure_trial(kind, phase, history)
                for kind in STORE_KINDS
                for phase in (
                    "after_partial_content_write",
                    "before_publish",
                    "before_ack",
                )
            ],
        ),
        (
            "backup_trials",
            lambda: [backup_trial(kind, history) for kind in STORE_KINDS],
        ),
        (
            "cadence_simulations",
            lambda: [
                cadence_trial(kind, history, count)
                for kind in STORE_KINDS
                for count in (1, 4)
            ],
        ),
        (
            "sqlite_full_trials",
            lambda: [
                sqlite_full_trial(kind, history)
                for kind in STORE_KINDS
                if kind != "files"
            ],
        ),
        ("wal_backup_negative_control", lambda: wal_backup_negative_control(history)),
    )
    try:
        for name, execute in families:
            results["phase"] = name
            preserve()
            results[name] = execute()
            preserve()
        results["benchmarks"] = []
        for copies in (1, 10, 50):
            for kind in STORE_KINDS:
                results["phase"] = f"benchmark:{kind}:{copies}"
                preserve()
                results["benchmarks"].append(
                    storage_benchmark(kind, history.history[-1], copies, repeats)
                )
                preserve()
        results.update(status="complete", phase="complete")
        preserve()
    except (
        AssertionError,
        ValueError,
        RuntimeError,
        OSError,
        sqlite3.DatabaseError,
    ) as exc:
        results.update(status="failed", failure=f"{type(exc).__name__}: {exc}")
        preserve()
        raise
    _emit(
        {
            "output": str(output),
            "kill_trials": len(results["kill_trials"]),
            "damage_trials": len(results["damage_trials"]),
            "benchmark_rows": len(results["benchmarks"]),
        }
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    subcommands = parser.add_subparsers(dest="mode", required=True)
    run_parser = subcommands.add_parser("run")
    run_parser.add_argument("--output", type=Path, required=True)
    run_parser.add_argument("--repeats", type=int, default=5)
    worker_parser = subcommands.add_parser("worker")
    worker_parser.add_argument("--kind", choices=STORE_KINDS, required=True)
    worker_parser.add_argument("--root", type=Path, required=True)
    worker_parser.add_argument(
        "--action", choices=("publish", "reader", "hold_writer"), required=True
    )
    worker_parser.add_argument("--checkpoint", type=Path)
    worker_parser.add_argument("--expected", type=int, default=4)
    worker_parser.add_argument("--pause", required=True)
    args = parser.parse_args()
    if args.mode == "run":
        if args.repeats < 1:
            parser.error("repeats must be positive")
        run(args.output, args.repeats)
    else:
        worker(args)
