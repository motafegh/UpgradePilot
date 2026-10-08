"""Disposable local checkpoint stores for the approved Workspace storage comparison.

Upstream: experiment 1's encoded, declared material closure. Start at publish/recover
on FileCheckpointStore or SQLiteCheckpointStore. Each publication binds an expected
predecessor; recovery returns inspectable historical records plus rejection/fallback
information. Neither store executes native evaluators, repairs content, admits live
continuation, authenticates provenance, or promises exactly-once external effects.

Files publish synced content then an immutable commit marker under a local writer lock.
SQLite shares record bodies and commits header/membership together. Full-checkpoint
hashes detect accidental damage, not adversarial replacement. Hooks expose deterministic
process-kill/injected-fault boundaries to workspace_checkpoint_trials; they are not a
production API. Linux/local filesystem only; no power-loss proof or retention/GC policy.
"""

from __future__ import annotations

import fcntl
import hashlib
import json
import os
import re
import sqlite3
import tempfile
import time
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path

from experiments.workspace_revision_representation import (
    PublishedRevision,
    decode_checkpoint,
    encode_checkpoint,
    retention_gaps,
)

MAX_CHECKPOINT_BYTES = 16 * 1024 * 1024  # Bounded research input; not product policy.
STORE_VERSION = 1
APPLICATION_ID = 0x55505753
PHASES = (
    "before_content_write",
    "after_partial_content_write",
    "after_content_write",
    "before_publish",
    "after_publish",
    "before_ack",
    "acknowledged",
)
SQL_SCHEMA = """
CREATE TABLE records (id TEXT PRIMARY KEY, body BLOB NOT NULL);
CREATE TABLE revisions (
    number INTEGER PRIMARY KEY, header BLOB NOT NULL,
    digest TEXT NOT NULL, record_count INTEGER NOT NULL
);
CREATE TABLE membership (
    revision INTEGER NOT NULL REFERENCES revisions(number),
    record TEXT NOT NULL REFERENCES records(id),
    PRIMARY KEY (revision, record)
);
"""


class StalePublication(ValueError):
    """CAS conflict; caller must inspect/revalidate, never silently overwrite/retry."""


class StoreDamaged(ValueError):
    """Storage/schema/closure damage; earlier history is not a writable current head."""


class StoreBusy(RuntimeError):
    """Bounded local lock contention; no new checkpoint was acknowledged."""


def canonical_json(value):
    return json.dumps(
        value, sort_keys=True, ensure_ascii=False, allow_nan=False
    ).encode()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise StoreDamaged(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def bounded_json(data):
    """Non-executing parsing with size/depth/duplicate-key bounds for local trials."""
    if type(data) is not bytes or len(data) > MAX_CHECKPOINT_BYTES:
        raise StoreDamaged("Checkpoint exceeds experiment byte bound")
    try:
        text = data.decode("utf-8")
        depth, quoted, escaped = 0, False, False
        for char in text:
            if quoted:
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == '"':
                    quoted = False
            elif char == '"':
                quoted = True
            elif char in "[{":
                depth += 1
                if depth > 128:
                    raise StoreDamaged("Checkpoint exceeds experiment depth bound")
            elif char in "]}":
                depth -= 1
        return json.loads(text, object_pairs_hook=_unique_object)
    except (ValueError, UnicodeError, RecursionError) as exc:
        raise StoreDamaged(str(exc)) from exc


def validate_checkpoint(data):
    """Stronger storage envelope checks around the pinned opaque experiment codec."""
    try:
        body = bounded_json(data)
        if canonical_json(body) != data:
            raise StoreDamaged("Noncanonical experiment encoding")
        revision = decode_checkpoint(data)
        if (
            type(revision.lineage) is not str
            or not revision.lineage
            or type(body["roots"]) is not list
            or type(body["triggering_records"]) is not list
            or encode_checkpoint(revision) != data
        ):
            raise StoreDamaged("Invalid experiment header/closure")
        bounded_json(revision.target)
        return revision
    except (ValueError, TypeError, KeyError, AttributeError, UnicodeError) as exc:
        raise StoreDamaged(str(exc)) from exc


@dataclass(frozen=True)
class RecoveryOutcome:
    revision: PublishedRevision | None
    latest_declared: int | None
    rejected: tuple[tuple[int | None, str], ...] = ()

    def summary(self):
        return {
            "latest_declared": self.latest_declared,
            "recovered_revision": None
            if self.revision is None
            else self.revision.number,
            "fallback": self.revision is not None and bool(self.rejected),
            "rejected": self.rejected,
            "checkpoint_digest": None
            if self.revision is None
            else digest(encode_checkpoint(self.revision)),
            "retention_gaps": {}
            if self.revision is None
            else retention_gaps(self.revision),
            "authority": "historical inspection only; continuation not implemented",
        }


def _select_valid(numbers, load):
    rejected = []
    for number in numbers:
        try:
            revision = validate_checkpoint(load(number))
            if revision.number != number:
                raise StoreDamaged("Catalog/revision identity mismatch")
            return RecoveryOutcome(revision, numbers[0], tuple(rejected))
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            sqlite3.DatabaseError,
        ) as exc:
            rejected.append((number, str(exc)))
    return RecoveryOutcome(None, numbers[0] if numbers else None, tuple(rejected))


def _check_successor(revision, expected, recovered):
    if type(expected) is not int or expected < -1:
        raise ValueError("Explicit expected predecessor required")
    if recovered.rejected or (
        recovered.latest_declared is not None and recovered.revision is None
    ):
        raise StoreDamaged("Cannot publish on an incomplete/corrupt current head")
    current = -1 if recovered.revision is None else recovered.revision.number
    if current != expected or revision.number != expected + 1:
        raise StalePublication(
            f"Expected {expected}, found {current}; successor {revision.number}"
        )
    if recovered.revision and (
        revision.target != recovered.revision.target
        or revision.lineage != recovered.revision.lineage
    ):
        raise StoreDamaged("Target/lineage changed without a new investigation store")
    if recovered.revision and any(
        revision.records[key] != old
        for key, old in recovered.revision.records.items()
        if key in revision.records
    ):
        raise StoreDamaged(
            "Immutable historical record changed under the same identity"
        )


def _sync_directory(path):
    descriptor = os.open(path, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


class FileCheckpointStore:
    """Full closure files; immutable marker is the sole publication catalog.

    Content-addressed filenames are storage references, not native observation identities.
    Missing content behind a surviving marker is detectable; total catalog deletion is
    not. Unpublished files are ignored, never reconstructed into a canonical revision.
    """

    def __init__(self, root, *, create=False):
        self.root = Path(root)
        if create:
            self.root.mkdir(parents=True, exist_ok=False)
            (self.root / "writer.lock").touch()
            _sync_directory(self.root)
        if not (self.root / "writer.lock").is_file():
            raise StoreDamaged("File store absent; no silent initialization")

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def close(self):
        pass

    @contextmanager
    def writer_lock(self):
        with (self.root / "writer.lock").open("rb") as stream:
            deadline = time.monotonic() + 0.25
            while True:
                try:
                    fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    break
                except BlockingIOError:
                    if time.monotonic() >= deadline:
                        raise StoreBusy("File writer lock timeout")
                    time.sleep(0.005)
            try:
                yield
            finally:
                fcntl.flock(stream, fcntl.LOCK_UN)

    def _numbers(self):
        return sorted(
            (
                int(path.stem.split("-")[1])
                for path in self.root.glob("revision-*.commit")
            ),
            reverse=True,
        )

    def _load(self, number):
        marker = bounded_json((self.root / f"revision-{number}.commit").read_bytes())
        if (
            type(marker) is not dict
            or set(marker) != {"version", "revision", "digest"}
            or type(marker["version"]) is not int
            or marker["version"] != STORE_VERSION
            or type(marker["revision"]) is not int
            or marker["revision"] != number
            or type(marker["digest"]) is not str
            or re.fullmatch("[0-9a-f]{64}", marker["digest"]) is None
        ):
            raise StoreDamaged("Unsupported/damaged commit marker")
        with (self.root / f"content-{marker['digest']}.json").open("rb") as stream:
            data = stream.read(MAX_CHECKPOINT_BYTES + 1)
        if digest(data) != marker["digest"]:
            raise StoreDamaged("Full checkpoint digest mismatch")
        return data

    def recover(self):
        try:
            # Append-only marker enumeration fixes the candidate set for this read.
            return _select_valid(self._numbers(), self._load)
        except (ValueError, OSError) as exc:
            return RecoveryOutcome(None, None, ((None, str(exc)),))

    def publish(self, data, *, expected, hook=lambda phase: None):
        revision = validate_checkpoint(data)
        with self.writer_lock():
            recovered = self.recover()
            _check_successor(revision, expected, recovered)
            # Latest-view overlap is not historical identity admission. A previously
            # omitted ID can reappear; compare it with retained old snapshots as well.
            # This intentionally simple baseline rescans history rather than invent a
            # second durable index. Its cost belongs in the storage comparison.
            known = {} if recovered.revision is None else recovered.revision.records
            new_ids = set(revision.records) - set(known)
            for number in self._numbers()[1:] if new_ids else ():
                historical = validate_checkpoint(self._load(number))
                found = new_ids & set(historical.records)
                if any(
                    revision.records[key] != historical.records[key] for key in found
                ):
                    raise StoreDamaged(
                        "Immutable historical record identity/content collision"
                    )
                new_ids -= found
                if not new_ids:
                    break
            hook("before_content_write")
            temporary = None
            marker_temp = None
            try:
                with tempfile.NamedTemporaryFile(
                    dir=self.root, prefix=".content-", delete=False
                ) as stream:
                    temporary = stream.name
                    halfway = len(data) // 2
                    stream.write(data[:halfway])
                    stream.flush()
                    hook("after_partial_content_write")
                    stream.write(data[halfway:])
                    stream.flush()
                    os.fsync(stream.fileno())
                content_path = self.root / f"content-{digest(data)}.json"
                try:
                    os.link(temporary, content_path)
                except FileExistsError:
                    if content_path.read_bytes() != data:
                        raise StoreDamaged("Existing content digest collision/damage")
                _sync_directory(self.root)
                hook("after_content_write")
                marker = canonical_json(
                    {
                        "version": STORE_VERSION,
                        "revision": revision.number,
                        "digest": digest(data),
                    }
                )
                with tempfile.NamedTemporaryFile(
                    dir=self.root, prefix=".marker-", delete=False
                ) as stream:
                    marker_temp = stream.name
                    stream.write(marker)
                    stream.flush()
                    os.fsync(stream.fileno())
                hook("before_publish")
                os.link(marker_temp, self.root / f"revision-{revision.number}.commit")
                hook("after_publish")
                _sync_directory(self.root)
                hook("before_ack")
            finally:
                for path in (temporary, marker_temp):
                    if path is not None:
                        os.unlink(path)
        return revision.number

    def backup(self, destination):
        """Copy a locked, validated catalog/content set; partial backup isn't adopted."""
        with self.writer_lock():
            if self.recover().rejected:
                raise StoreDamaged("Refuse backup of damaged current catalog")
            destination = Path(destination)
            destination.mkdir(exist_ok=False)
            (destination / "writer.lock").touch()
            for number in self._numbers():
                data = self._load(number)
                validate_checkpoint(data)
                for path in (
                    self.root / f"content-{digest(data)}.json",
                    self.root / f"revision-{number}.commit",
                ):
                    with (destination / path.name).open("xb") as stream:
                        stream.write(path.read_bytes())
                        stream.flush()
                        os.fsync(stream.fileno())
            _sync_directory(destination)
        return FileCheckpointStore(destination)


class SQLiteCheckpointStore:
    """Native record bodies share storage; header/membership publish in one transaction.

    Connection lifetime is explicit: cached writer until close, independent transactional
    readers. Recovery opens an existing local DB in rw mode so SQLite can roll back a hot
    journal after a killed writer; it never creates a missing DB or runs domain evaluators.
    Engine consistency and app-level full checkpoint validation remain separate.
    """

    def __init__(self, root, *, create=False, journal="DELETE"):
        if journal not in ("DELETE", "WAL"):
            raise ValueError("Only declared research configurations are supported")
        self.root, self.journal = Path(root).resolve(), journal
        self.path = self.root / "workspace.sqlite3"
        self._writer = None
        if create:
            self.root.mkdir(parents=True, exist_ok=False)
            with sqlite3.connect(self.path) as connection:
                connection.execute(f"PRAGMA journal_mode={journal}")
                connection.execute(
                    f"PRAGMA synchronous={3 if journal == 'DELETE' else 2}"
                )
                connection.executescript(SQL_SCHEMA)
                connection.execute(f"PRAGMA application_id={APPLICATION_ID}")
                connection.execute(f"PRAGMA user_version={STORE_VERSION}")
            connection.close()
            _sync_directory(self.root)
        if not self.path.is_file():
            raise StoreDamaged("SQLite store absent; no silent initialization")

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def close(self):
        if self._writer is not None:
            self._writer.close()
            self._writer = None

    def connect(self):
        connection = sqlite3.connect(
            self.path.as_uri() + "?mode=rw",
            uri=True,
            timeout=0.25,
            isolation_level=None,
        )
        try:
            connection.execute("PRAGMA foreign_keys=ON")
            connection.execute(
                f"PRAGMA synchronous={3 if self.journal == 'DELETE' else 2}"
            )
            if (
                connection.execute("PRAGMA application_id").fetchone()[0]
                != APPLICATION_ID
                or connection.execute("PRAGMA user_version").fetchone()[0]
                != STORE_VERSION
                or connection.execute("PRAGMA journal_mode").fetchone()[0].upper()
                != self.journal
            ):
                raise StoreDamaged(
                    "Unsupported SQLite store identity/version/configuration"
                )
            return connection
        except Exception:
            connection.close()
            raise

    def settings(self):
        with self.connect() as connection:
            result = {
                key: connection.execute(f"PRAGMA {key}").fetchone()[0]
                for key in (
                    "journal_mode",
                    "synchronous",
                    "foreign_keys",
                    "busy_timeout",
                    "page_size",
                    "wal_autocheckpoint",
                )
            }
        connection.close()
        return {"sqlite_version": sqlite3.sqlite_version, **result}

    def _load(self, connection, number):
        header, expected_digest, count = connection.execute(
            "SELECT header, digest, record_count FROM revisions WHERE number=?",
            (number,),
        ).fetchone()
        body = bounded_json(header)
        entries = connection.execute(
            "SELECT r.body FROM membership m JOIN records r ON r.id=m.record WHERE m.revision=? ORDER BY r.id",
            (number,),
        ).fetchall()
        if type(count) is not int or len(entries) != count:
            raise StoreDamaged("Missing checkpoint membership/content")
        body["records"] = [bounded_json(entry[0]) for entry in entries]
        data = canonical_json(body)
        if digest(data) != expected_digest:
            raise StoreDamaged("Full checkpoint digest mismatch")
        return data

    def recover_connection(self, connection):
        """Caller owns one read/write transaction; used also by held-reader trials."""
        numbers = [
            row[0]
            for row in connection.execute(
                "SELECT number FROM revisions ORDER BY number DESC"
            )
        ]
        return _select_valid(numbers, lambda number: self._load(connection, number))

    def recover(self):
        connection = None
        try:
            connection = self.connect()
            connection.execute("BEGIN")
            return self.recover_connection(connection)
        except (sqlite3.DatabaseError, StoreDamaged, OSError) as exc:
            return RecoveryOutcome(None, None, ((None, str(exc)),))
        finally:
            if connection is not None:
                connection.close()

    def publish(self, data, *, expected, hook=lambda phase: None):
        revision = validate_checkpoint(data)
        if self._writer is None:
            self._writer = self.connect()
        connection = self._writer
        try:
            connection.execute("BEGIN IMMEDIATE")
            recovered = self.recover_connection(connection)
            _check_successor(revision, expected, recovered)
            body = bounded_json(data)
            entries = body.pop("records")
            previous_ids = (
                set() if recovered.revision is None else set(recovered.revision.records)
            )
            # A stage containing only existing INSERT OR IGNORE rows is a weak crash
            # control. Process new-to-current IDs first so the trace's fresh observation
            # exists uncommitted at the first-row hook. A SQL BLOB insert is indivisible;
            # this is partial record-set staging, unlike the file half-byte hook.
            entries.sort(key=lambda entry: entry["id"] in previous_ids)
            hook("before_content_write")
            for index, entry in enumerate(entries):
                encoded = canonical_json(entry)
                old = connection.execute(
                    "SELECT body FROM records WHERE id=?", (entry["id"],)
                ).fetchone()
                if old is not None and old[0] != encoded:
                    raise StoreDamaged(
                        "Immutable stored record identity/content collision"
                    )
                connection.execute(
                    "INSERT OR IGNORE INTO records VALUES (?,?)", (entry["id"], encoded)
                )
                if index == 0:
                    hook("after_partial_content_write")
            # Empty revision zero still exposes the same interruption boundary.
            if not entries:
                hook("after_partial_content_write")
            hook("after_content_write")
            connection.execute(
                "INSERT INTO revisions VALUES (?,?,?,?)",
                (revision.number, canonical_json(body), digest(data), len(entries)),
            )
            connection.executemany(
                "INSERT INTO membership VALUES (?,?)",
                ((revision.number, entry["id"]) for entry in entries),
            )
            hook("before_publish")
            connection.execute("COMMIT")
            hook("after_publish")
            hook("before_ack")
            return revision.number
        except Exception as exc:
            if connection.in_transaction:
                connection.rollback()
            if isinstance(exc, sqlite3.OperationalError) and "locked" in str(exc):
                raise StoreBusy(str(exc)) from exc
            raise

    def backup(self, destination):
        """Use SQLite's online snapshot API, not copying a possibly WAL-dependent DB."""
        destination = Path(destination)
        destination.mkdir(exist_ok=False)
        source = self.connect()
        target = sqlite3.connect(destination / self.path.name)
        try:
            source.backup(target)
        finally:
            target.close()
            source.close()
        with (destination / self.path.name).open("rb") as stream:
            os.fsync(stream.fileno())
        _sync_directory(destination)
        # Backup output can have WAL journal identity; open it with the same config.
        result = SQLiteCheckpointStore(destination, journal=self.journal)
        if result.recover().rejected:
            result.close()
            raise StoreDamaged("Backup failed checkpoint validation")
        return result


STORE_KINDS = ("files", "sqlite-delete", "sqlite-wal")


def open_store(kind, root, *, create=False):
    if kind == "files":
        return FileCheckpointStore(root, create=create)
    if kind not in STORE_KINDS:
        raise ValueError("Unknown research store")
    return SQLiteCheckpointStore(
        root, create=create, journal=kind.split("-")[1].upper()
    )


def physical_bytes(root):
    return sum(path.stat().st_size for path in Path(root).iterdir() if path.is_file())
