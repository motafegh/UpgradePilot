"""Host-owned local immutable checkpoint publication; start at ``CheckpointStore.publish``.

One transaction publishes payloads, scoped records/references, ordered revision membership
and a conditional lineage head. Revisions share immutable material within a lineage;
retention has no expiry/prune/delete operation. WAL/FULL is validated, not a power-loss
claim. SQL is private to this persistence owner; callers exchange ``CheckpointRevision``.

``read_revision`` restores encoded material only, with no codec/domain execution, and
discloses excluded successor progress. ``backup`` uses SQLite online backup and validates
the whole declared catalog before acknowledgement. Opening a host-owned store/backup is
not authentication or an arbitrary untrusted import surface. Normal orchestration and
combined durable native reconstruction remain separate integration responsibilities.
"""

from __future__ import annotations

import os
import sqlite3
import stat
import time
from contextlib import contextmanager
from hashlib import sha256
from pathlib import Path
from typing import Iterator, Literal

from .checkpoint_revision import (
    BackupReceipt,
    CheckpointRevision,
    CheckpointStorageError,
    PublicationConflict,
    PublicationReceipt,
    StoredCheckpoint,
    UnconfirmedPublication,
)
from .native_boundary import (
    ExactInvestigationTarget,
    encode_native_boundary,
    read_native_boundary,
)
from .native_representation import (
    MAX_NATIVE_JSON_BYTES,
    NativeReconstructionError,
    json_bytes,
    parse_json,
)

_APPLICATION_ID = 0x55504350
_SCHEMA_VERSION = 1
_DATABASE_NAME = "workspace.sqlite3"
_MAX_RECORDS = 4096

# The catalog is an explicit versioned layout. Unexpected tables/triggers/views are not
# accepted by a version label alone; no SQL supplied by a checkpoint is executed.
_TABLES = (
    """CREATE TABLE payloads (
        lineage_id TEXT NOT NULL, digest TEXT NOT NULL, body BLOB NOT NULL,
        PRIMARY KEY (lineage_id, digest)) STRICT""",
    """CREATE TABLE records (
        lineage_id TEXT NOT NULL, record_id TEXT NOT NULL, metadata BLOB NOT NULL,
        metadata_digest TEXT NOT NULL, payload_digest TEXT NOT NULL,
        PRIMARY KEY (lineage_id, record_id),
        FOREIGN KEY (lineage_id, payload_digest) REFERENCES payloads(lineage_id, digest)) STRICT""",
    """CREATE TABLE record_inputs (
        lineage_id TEXT NOT NULL, record_id TEXT NOT NULL, position INTEGER NOT NULL,
        input_id TEXT NOT NULL, PRIMARY KEY (lineage_id, record_id, position),
        FOREIGN KEY (lineage_id, record_id) REFERENCES records(lineage_id, record_id),
        FOREIGN KEY (lineage_id, input_id) REFERENCES records(lineage_id, record_id)) STRICT""",
    """CREATE TABLE revisions (
        lineage_id TEXT NOT NULL, revision_id TEXT NOT NULL, predecessor_id TEXT,
        target BLOB NOT NULL, digest TEXT NOT NULL, PRIMARY KEY (lineage_id, revision_id),
        FOREIGN KEY (lineage_id, predecessor_id) REFERENCES revisions(lineage_id, revision_id)) STRICT""",
    """CREATE TABLE revision_members (
        lineage_id TEXT NOT NULL, revision_id TEXT NOT NULL, position INTEGER NOT NULL,
        record_id TEXT NOT NULL, PRIMARY KEY (lineage_id, revision_id, position),
        UNIQUE (lineage_id, revision_id, record_id),
        FOREIGN KEY (lineage_id, revision_id) REFERENCES revisions(lineage_id, revision_id),
        FOREIGN KEY (lineage_id, record_id) REFERENCES records(lineage_id, record_id)) STRICT""",
    """CREATE TABLE heads (
        lineage_id TEXT PRIMARY KEY, revision_id TEXT NOT NULL,
        FOREIGN KEY (lineage_id, revision_id) REFERENCES revisions(lineage_id, revision_id)) STRICT""",
)
_IMMUTABLE_TABLES = (
    "payloads",
    "records",
    "record_inputs",
    "revisions",
    "revision_members",
)
_SCHEMA = _TABLES + tuple(
    f"CREATE TRIGGER immutable_{table}_{operation.lower()} BEFORE {operation} ON {table} "
    "BEGIN SELECT RAISE(ABORT, 'immutable checkpoint material'); END"
    for table in _IMMUTABLE_TABLES
    for operation in ("UPDATE", "DELETE")
)
_SCHEMA_SQL = {" ".join(statement.split()) for statement in _SCHEMA}


def _refuse(reason: str, detail: str) -> CheckpointStorageError:
    return CheckpointStorageError(reason, detail)


def _storage_error(error: sqlite3.Error | OSError) -> CheckpointStorageError:
    code = getattr(error, "sqlite_errorcode", 0) & 255
    reason = {
        sqlite3.SQLITE_BUSY: "storage_busy",
        sqlite3.SQLITE_LOCKED: "storage_busy",
        sqlite3.SQLITE_READONLY: "storage_read_only",
        sqlite3.SQLITE_FULL: "storage_full",
        sqlite3.SQLITE_CORRUPT: "invalid_checkpoint_storage",
        sqlite3.SQLITE_NOTADB: "invalid_checkpoint_storage",
    }.get(code, "storage_io_error")
    return _refuse(reason, str(error))


def _owned_directory(directory: Path, *, create: bool) -> Path:
    directory = directory.absolute()
    if directory.is_symlink() or directory.resolve() != directory:
        raise _refuse(
            "unsupported_store_location", "Store path must not traverse symlinks."
        )
    if any(
        (ancestor / ".git").exists() for ancestor in (directory, *directory.parents)
    ):
        raise _refuse(
            "unsupported_store_location", "Checkpoints must stay outside Git checkouts."
        )
    if create:
        directory.mkdir(mode=0o700, exist_ok=True)
    info = directory.stat()
    if (
        not stat.S_ISDIR(info.st_mode)
        or info.st_uid != os.geteuid()
        or info.st_mode & 0o077
    ):
        raise _refuse(
            "unsupported_store_location",
            "Store directory must be owner-only and host-owned.",
        )
    return directory


def _check_database_file(path: Path) -> None:
    info = path.lstat()
    if (
        not stat.S_ISREG(info.st_mode)
        or info.st_uid != os.geteuid()
        or info.st_mode & 0o077
    ):
        raise _refuse(
            "unsupported_store_location", "Database must be an owner-only regular file."
        )


def _verify_schema(connection: sqlite3.Connection) -> None:
    if connection.execute("PRAGMA application_id").fetchone()[0] != _APPLICATION_ID:
        raise _refuse("unsupported_storage_schema", "Unknown Workspace store identity.")
    if connection.execute("PRAGMA user_version").fetchone()[0] != _SCHEMA_VERSION:
        raise _refuse(
            "unsupported_storage_schema", "Only storage schema version 1 is supported."
        )
    sql = {
        " ".join(row[0].split())
        for row in connection.execute(
            "SELECT sql FROM sqlite_schema WHERE sql IS NOT NULL AND name NOT LIKE 'sqlite_%'"
        )
    }
    if sql != _SCHEMA_SQL:
        raise _refuse(
            "invalid_checkpoint_storage",
            "Declared storage catalog differs from version 1.",
        )


class CheckpointStore:
    """Explicit create/open on an admitted local directory; no implicit initialization.

    Each operation opens its own connection and snapshot. Contention is bounded to at most
    five seconds; a competing writer gets conflict/busy, never an implicit semantic retry.
    Host provenance is an admission precondition, not inferred from permissions/checksums.
    """

    def __init__(
        self, directory: Path, *, read_only: bool, busy_timeout_ms: int
    ) -> None:
        if type(busy_timeout_ms) is not int or not 0 <= busy_timeout_ms <= 5000:
            raise _refuse(
                "unsupported_storage_settings", "Writer wait must be 0..5000 ms."
            )
        self.directory = directory
        self._path = directory / _DATABASE_NAME
        self._read_only = read_only
        self._busy_timeout_ms = busy_timeout_ms

    @classmethod
    def create(cls, directory: Path, *, busy_timeout_ms: int = 1000) -> CheckpointStore:
        """Create a new host store; never initialize or replace an existing database."""
        store = cls(Path(directory), read_only=False, busy_timeout_ms=busy_timeout_ms)
        reserved = False
        initialized = False
        try:
            store.directory = _owned_directory(store.directory, create=True)
            store._path = store.directory / _DATABASE_NAME
            if any(
                os.path.lexists(store.directory / (_DATABASE_NAME + suffix))
                for suffix in ("-wal", "-shm")
            ):
                raise _refuse(
                    "store_already_exists",
                    "Existing SQLite sidecars cannot be replaced.",
                )
            descriptor = os.open(
                store._path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600
            )
            reserved = True
            os.close(descriptor)
            with store._connection(verify=False) as connection:
                connection.execute("BEGIN IMMEDIATE")
                for statement in _SCHEMA:
                    connection.execute(statement)
                connection.execute(f"PRAGMA application_id={_APPLICATION_ID}")
                connection.execute(f"PRAGMA user_version={_SCHEMA_VERSION}")
                connection.execute("COMMIT")
                _verify_schema(connection)
            initialized = True
        except FileExistsError as error:
            raise _refuse(
                "store_already_exists", "Existing stores require explicit open."
            ) from error
        except (sqlite3.Error, OSError) as error:
            raise _storage_error(error) from error
        finally:
            # The connection has closed first. Never remove the directory, user files or
            # a preexisting store; admission above excludes preexisting SQLite sidecars.
            if reserved and not initialized:
                for suffix in ("", "-wal", "-shm"):
                    (store.directory / (_DATABASE_NAME + suffix)).unlink(
                        missing_ok=True
                    )
        return store

    @classmethod
    def open(
        cls, directory: Path, *, read_only: bool = False, busy_timeout_ms: int = 1000
    ) -> CheckpointStore:
        try:
            directory = _owned_directory(Path(directory), create=False)
            store = cls(directory, read_only=read_only, busy_timeout_ms=busy_timeout_ms)
            _check_database_file(store._path)
            with store._connection():
                pass
            return store
        except (sqlite3.Error, OSError) as error:
            raise _storage_error(error) from error

    @contextmanager
    def _connection(self, *, verify: bool = True) -> Iterator[sqlite3.Connection]:
        connection = None
        try:
            _owned_directory(self.directory, create=False)
            _check_database_file(self._path)
            mode = "ro" if self._read_only else "rw"
            connection = sqlite3.connect(
                self._path.as_uri() + f"?mode={mode}",
                uri=True,
                isolation_level=None,
                timeout=self._busy_timeout_ms / 1000,
            )
            connection.setlimit(
                sqlite3.SQLITE_LIMIT_LENGTH, MAX_NATIVE_JSON_BYTES + 1024 * 1024
            )
            connection.execute("PRAGMA trusted_schema=OFF")
            if verify:
                _verify_schema(connection)
            # Check schema before any writable PRAGMA, so incompatible stores are not migrated.
            if self._read_only:
                journal = connection.execute("PRAGMA journal_mode").fetchone()[0]
            else:
                journal = connection.execute("PRAGMA journal_mode=WAL").fetchone()[0]
            connection.execute("PRAGMA synchronous=FULL")
            connection.execute("PRAGMA foreign_keys=ON")
            connection.execute(f"PRAGMA busy_timeout={self._busy_timeout_ms}")
            if (
                journal != "wal"
                or connection.execute("PRAGMA synchronous").fetchone()[0] != 2
                or connection.execute("PRAGMA foreign_keys").fetchone()[0] != 1
                or connection.execute("PRAGMA busy_timeout").fetchone()[0]
                != self._busy_timeout_ms
            ):
                raise _refuse(
                    "unsupported_storage_settings",
                    "Required SQLite settings are unavailable.",
                )
            yield connection
        except (sqlite3.Error, OSError) as error:
            raise _storage_error(error) from error
        except (NativeReconstructionError, UnicodeError) as error:
            reason = (
                "wrong_target"
                if getattr(error, "reason", None) == "wrong_target"
                else "invalid_checkpoint_storage"
            )
            raise _refuse(reason, str(error)) from error
        finally:
            if connection is not None:
                connection.close()

    @staticmethod
    def _validate_staged_revision(revision: CheckpointRevision) -> str:
        """Validate supplied identity/material before publication or absence certainty."""
        try:
            digest = revision.digest()
        except NativeReconstructionError as error:
            raise _refuse("invalid_revision", str(error)) from error
        if not 1 <= len(revision.boundary.records) <= _MAX_RECORDS:
            raise _refuse(
                "storage_resource_limit", "Revision must have 1..4096 records."
            )
        return digest

    def publish(self, revision: CheckpointRevision) -> PublicationReceipt:
        """Commit a successor once. Acknowledgement follows commit, never precedes it.

        On commit/acknowledgement uncertainty, ``inspect_publication`` is the only storage
        reconciliation: do not republish or perform a capability automatically. A process
        killed after commit cannot receive a receipt; the staged identity still resolves it.
        """
        if self._read_only:
            raise _refuse("storage_read_only", "Inspection store cannot publish.")
        digest = self._validate_staged_revision(revision)
        try:
            encoded = parse_json(encode_native_boundary(revision.boundary))
        except NativeReconstructionError as error:
            raise _refuse("invalid_revision", str(error)) from error
        commit_attempted = False
        try:
            with self._connection() as connection:
                connection.execute("BEGIN IMMEDIATE")
                head = connection.execute(
                    "SELECT revision_id FROM heads WHERE lineage_id=?",
                    (revision.lineage_id,),
                ).fetchone()
                actual = head[0] if head else None
                if actual != revision.predecessor_id:
                    raise PublicationConflict(revision.predecessor_id, actual)
                if connection.execute(
                    "SELECT 1 FROM revisions WHERE lineage_id=? AND revision_id=?",
                    (revision.lineage_id, revision.revision_id),
                ).fetchone():
                    raise _refuse(
                        "immutable_identity_conflict",
                        "Revision identity is already published.",
                    )
                if (
                    actual is not None
                    or connection.execute(
                        "SELECT 1 FROM revisions WHERE lineage_id=?",
                        (revision.lineage_id,),
                    ).fetchone()
                ):
                    # A successor extends retained history, not just an intact head.
                    # Inspect encoded closure only; unrelated lineages remain unaffected.
                    for retained_id in self._history(connection, revision.lineage_id):
                        self._read(
                            connection,
                            revision.lineage_id,
                            retained_id,
                            revision.boundary.target,
                        )
                for item in encoded["records"]:
                    body = item.pop("payload").encode("utf-8")
                    metadata = json_bytes(item)
                    self._insert_immutable(
                        connection,
                        "payloads",
                        ("lineage_id", "digest"),
                        (revision.lineage_id, item["payload_digest"]),
                        ("body",),
                        (body,),
                    )
                    self._insert_immutable(
                        connection,
                        "records",
                        ("lineage_id", "record_id"),
                        (revision.lineage_id, item["record_id"]),
                        ("metadata", "metadata_digest", "payload_digest"),
                        (
                            metadata,
                            sha256(metadata).hexdigest(),
                            item["payload_digest"],
                        ),
                    )
                # All referenced identities now exist. Edges are immutable ordered material,
                # checked against metadata on read, and must remain inside this revision.
                for item in encoded["records"]:
                    for position, input_id in enumerate(item["input_record_ids"]):
                        self._insert_immutable(
                            connection,
                            "record_inputs",
                            ("lineage_id", "record_id", "position"),
                            (revision.lineage_id, item["record_id"], position),
                            ("input_id",),
                            (input_id,),
                        )
                connection.execute(
                    "INSERT INTO revisions VALUES (?,?,?,?,?)",
                    (
                        revision.lineage_id,
                        revision.revision_id,
                        revision.predecessor_id,
                        json_bytes(encoded["target"]),
                        digest,
                    ),
                )
                for position, item in enumerate(encoded["records"]):
                    connection.execute(
                        "INSERT INTO revision_members VALUES (?,?,?,?)",
                        (
                            revision.lineage_id,
                            revision.revision_id,
                            position,
                            item["record_id"],
                        ),
                    )
                if actual is None:
                    connection.execute(
                        "INSERT INTO heads VALUES (?,?)",
                        (revision.lineage_id, revision.revision_id),
                    )
                else:
                    updated = connection.execute(
                        "UPDATE heads SET revision_id=? WHERE lineage_id=? AND revision_id=?",
                        (revision.revision_id, revision.lineage_id, actual),
                    )
                    if updated.rowcount != 1:
                        raise PublicationConflict(revision.predecessor_id, actual)
                # Re-read through the same validation as offline inspection before commit.
                self._read(
                    connection,
                    revision.lineage_id,
                    revision.revision_id,
                    revision.boundary.target,
                )
                commit_attempted = True
                connection.execute("COMMIT")
            return PublicationReceipt(revision.lineage_id, revision.revision_id, digest)
        except BaseException as error:
            if commit_attempted:
                raise UnconfirmedPublication(
                    revision.lineage_id, revision.revision_id
                ) from error
            raise

    @staticmethod
    def _insert_immutable(
        connection: sqlite3.Connection,
        table: str,
        keys: tuple[str, ...],
        identity: tuple,
        columns: tuple[str, ...],
        values: tuple,
    ) -> None:
        # Table/column names are private static call-site constants, never checkpoint inputs.
        where = " AND ".join(f"{key}=?" for key in keys)
        for column in columns:
            if column in ("body", "metadata"):
                size = connection.execute(
                    f"SELECT length({column}) FROM {table} WHERE {where}", identity
                ).fetchone()
                if size is not None and size[0] > MAX_NATIVE_JSON_BYTES:
                    raise _refuse(
                        "storage_resource_limit",
                        "Immutable comparison exceeds read capacity.",
                    )
        old = connection.execute(
            f"SELECT {','.join(columns)} FROM {table} WHERE {where}", identity
        ).fetchone()
        if old is not None:
            if old != values:
                raise _refuse(
                    "immutable_identity_conflict",
                    f"Changed immutable {table} identity.",
                )
            return
        connection.execute(
            f"INSERT INTO {table} ({','.join(keys + columns)}) VALUES "
            f"({','.join('?' for _ in keys + columns)})",
            identity + values,
        )

    @staticmethod
    def _bounded_blob(
        connection: sqlite3.Connection, query: str, identity: tuple
    ) -> bytes:
        row = connection.execute(query, identity).fetchone()
        if row is None:
            raise _refuse("missing_checkpoint_material", "Missing retained body.")
        # LENGTH is selected separately: do not allocate an oversized stored blob first.
        size = row[0]
        if type(size) is not int or not 0 <= size <= MAX_NATIVE_JSON_BYTES:
            raise _refuse(
                "storage_resource_limit", "Stored body exceeds supported read capacity."
            )
        body = connection.execute(
            query.replace("length(body)", "body")
            .replace("length(metadata)", "metadata")
            .replace("length(target)", "target"),
            identity,
        ).fetchone()[0]
        if type(body) is not bytes:
            raise _refuse(
                "invalid_checkpoint_storage", "Retained bodies must be blobs."
            )
        return body

    def _read(
        self,
        connection: sqlite3.Connection,
        lineage_id: str,
        revision_id: str,
        expected_target: ExactInvestigationTarget,
    ) -> CheckpointRevision:
        row = connection.execute(
            "SELECT predecessor_id,digest FROM revisions WHERE lineage_id=? AND revision_id=?",
            (lineage_id, revision_id),
        ).fetchone()
        if row is None:
            raise _refuse("missing_checkpoint_revision", "No such declared revision.")
        identity = (lineage_id, revision_id)
        target = self._bounded_blob(
            connection,
            "SELECT length(target) FROM revisions WHERE lineage_id=? AND revision_id=?",
            identity,
        )
        count = connection.execute(
            "SELECT count(*) FROM revision_members WHERE lineage_id=? AND revision_id=?",
            identity,
        ).fetchone()[0]
        if not 1 <= count <= _MAX_RECORDS:
            raise _refuse(
                "missing_checkpoint_material",
                "Unsupported or empty revision membership.",
            )
        material_size = connection.execute(
            "SELECT coalesce(sum(length(r.metadata)+length(p.body)),0) FROM revision_members m "
            "JOIN records r USING(lineage_id,record_id) "
            "JOIN payloads p ON p.lineage_id=r.lineage_id AND p.digest=r.payload_digest "
            "WHERE m.lineage_id=? AND m.revision_id=?",
            identity,
        ).fetchone()[0]
        if len(target) + material_size > MAX_NATIVE_JSON_BYTES:
            raise _refuse(
                "storage_resource_limit", "Revision exceeds supported read capacity."
            )
        records = []
        total = len(target)
        for position, record_id in connection.execute(
            "SELECT position,record_id FROM revision_members WHERE lineage_id=? AND revision_id=? ORDER BY position",
            identity,
        ):
            if position != len(records):
                raise _refuse(
                    "invalid_checkpoint_storage", "Noncontiguous revision membership."
                )
            key = (lineage_id, record_id)
            metadata = self._bounded_blob(
                connection,
                "SELECT length(metadata) FROM records WHERE lineage_id=? AND record_id=?",
                key,
            )
            metadata_digest, payload_digest = connection.execute(
                "SELECT metadata_digest,payload_digest FROM records WHERE lineage_id=? AND record_id=?",
                key,
            ).fetchone()
            if sha256(metadata).hexdigest() != metadata_digest:
                raise _refuse(
                    "invalid_checkpoint_storage", "Corrupted record metadata."
                )
            item = parse_json(metadata)
            body = self._bounded_blob(
                connection,
                "SELECT length(body) FROM payloads WHERE lineage_id=? AND digest=?",
                (lineage_id, payload_digest),
            )
            total += len(metadata) + len(body)
            if total > MAX_NATIVE_JSON_BYTES:
                raise _refuse(
                    "storage_resource_limit",
                    "Revision exceeds supported read capacity.",
                )
            reference_count = connection.execute(
                "SELECT count(*) FROM record_inputs WHERE lineage_id=? AND record_id=?",
                key,
            ).fetchone()[0]
            if reference_count > _MAX_RECORDS:
                raise _refuse(
                    "storage_resource_limit",
                    "Record reference count exceeds read capacity.",
                )
            refs = list(
                connection.execute(
                    "SELECT position,input_id FROM record_inputs WHERE lineage_id=? AND record_id=? ORDER BY position",
                    key,
                )
            )
            if (
                type(item) is not dict
                or item.get("record_id") != record_id
                or item.get("payload_digest") != payload_digest
                or type(item.get("input_record_ids")) is not list
                or sha256(body).hexdigest() != payload_digest
                or refs != list(enumerate(item.get("input_record_ids", [])))
            ):
                raise _refuse(
                    "invalid_checkpoint_storage",
                    "Record identity, digest or references disagree.",
                )
            item["payload"] = body.decode("utf-8")
            records.append(item)
        boundary = read_native_boundary(
            json_bytes(
                {"format_version": 1, "target": parse_json(target), "records": records}
            ),
            expected_target=expected_target,
        )
        revision = CheckpointRevision(lineage_id, revision_id, row[0], boundary)
        if revision.digest() != row[1]:
            raise _refuse(
                "invalid_checkpoint_storage",
                "Revision identity/material digest disagrees.",
            )
        return revision

    @staticmethod
    def _history(connection: sqlite3.Connection, lineage_id: str) -> tuple[str, ...]:
        head = connection.execute(
            "SELECT revision_id FROM heads WHERE lineage_id=?", (lineage_id,)
        ).fetchone()
        parents = dict(
            connection.execute(
                "SELECT revision_id,predecessor_id FROM revisions WHERE lineage_id=?",
                (lineage_id,),
            )
        )
        if head is None:
            # Retained history without its declared head is damage, not absence.
            if parents:
                raise _refuse(
                    "invalid_checkpoint_storage", "Lineage has revisions but no head."
                )
            raise _refuse("missing_checkpoint_revision", "No declared lineage head.")
        history = []
        visited: set[str] = set()
        current = head[0]
        while current is not None:
            if current not in parents or current in visited:
                raise _refuse("invalid_checkpoint_storage", "Broken or cyclic lineage.")
            history.append(current)
            visited.add(current)
            current = parents[current]
        if len(history) != len(parents):
            raise _refuse(
                "invalid_checkpoint_storage",
                "Unreachable or competing declared revision.",
            )
        if (
            connection.execute(
                "SELECT 1 FROM revisions WHERE lineage_id=? AND target != "
                "(SELECT target FROM revisions WHERE lineage_id=? AND revision_id=?)",
                (lineage_id, lineage_id, head[0]),
            ).fetchone()
            is not None
        ):
            raise _refuse(
                "wrong_target", "Lineage revisions declare different exact targets."
            )
        return tuple(reversed(history))

    def read_revision(
        self,
        lineage_id: str,
        revision_id: str,
        *,
        expected_target: ExactInvestigationTarget,
    ) -> StoredCheckpoint:
        """Inspect one declared encoded boundary; explicitly disclose later excluded progress."""
        try:
            with self._connection() as connection:
                connection.execute("BEGIN")
                history = self._history(connection, lineage_id)
                if revision_id not in history:
                    raise _refuse(
                        "missing_checkpoint_revision",
                        "Selected revision is not in this lineage.",
                    )
                revision = self._read(
                    connection, lineage_id, revision_id, expected_target
                )
                return StoredCheckpoint(
                    revision, history[-1], history[history.index(revision_id) + 1 :]
                )
        except (NativeReconstructionError, UnicodeError) as error:
            raise _refuse("invalid_checkpoint_storage", str(error)) from error

    def inspect_publication(
        self, revision: CheckpointRevision
    ) -> Literal["published", "not_published"]:
        """Inspect staged identity in a coherent lineage; errors remain unknown.

        Absence also requires an intact current head. Selected published identities remain
        inspectable where unrelated damaged material blocks further publication; neither
        result certifies every retained historical revision.
        """
        self._validate_staged_revision(revision)
        with self._connection() as connection:
            connection.execute("BEGIN")
            head = connection.execute(
                "SELECT revision_id FROM heads WHERE lineage_id=?",
                (revision.lineage_id,),
            ).fetchone()
            if (
                head is not None
                or connection.execute(
                    "SELECT 1 FROM revisions WHERE lineage_id=?", (revision.lineage_id,)
                ).fetchone()
            ):
                self._history(connection, revision.lineage_id)
            found = connection.execute(
                "SELECT 1 FROM revisions WHERE lineage_id=? AND revision_id=?",
                (revision.lineage_id, revision.revision_id),
            ).fetchone()
            if found is None:
                if head is not None:
                    self._read(
                        connection,
                        revision.lineage_id,
                        head[0],
                        revision.boundary.target,
                    )
                return "not_published"
            retained = self._read(
                connection,
                revision.lineage_id,
                revision.revision_id,
                revision.boundary.target,
            )
            if retained != revision:
                raise _refuse(
                    "immutable_identity_conflict",
                    "Identity resolves to different retained material.",
                )
            return "published"

    def _validate_catalog(self, connection: sqlite3.Connection) -> BackupReceipt:
        _verify_schema(connection)
        if connection.execute("PRAGMA integrity_check").fetchone() != ("ok",):
            raise _refuse(
                "invalid_checkpoint_storage", "SQLite integrity check failed."
            )
        if connection.execute("PRAGMA foreign_key_check").fetchone() is not None:
            raise _refuse("missing_checkpoint_material", "Broken catalog reference.")
        # No staged/orphan rows may be mistaken for declared retained history.
        for query in (
            "SELECT 1 FROM revisions r LEFT JOIN heads h USING(lineage_id) WHERE h.lineage_id IS NULL",
            "SELECT 1 FROM records r LEFT JOIN revision_members m USING(lineage_id,record_id) WHERE m.record_id IS NULL",
            "SELECT 1 FROM payloads p LEFT JOIN records r ON p.lineage_id=r.lineage_id AND p.digest=r.payload_digest WHERE r.record_id IS NULL",
        ):
            if connection.execute(query).fetchone() is not None:
                raise _refuse(
                    "invalid_checkpoint_storage",
                    "Undeclared orphan material in catalog.",
                )
        count = 0
        heads = tuple(
            connection.execute(
                "SELECT lineage_id,revision_id FROM heads ORDER BY lineage_id"
            )
        )
        for lineage_id, _ in heads:
            target = None
            for revision_id in self._history(connection, lineage_id):
                raw_target = self._bounded_blob(
                    connection,
                    "SELECT length(target) FROM revisions WHERE lineage_id=? AND revision_id=?",
                    (lineage_id, revision_id),
                )
                # Fixed target layout is already validated by the encoded boundary owner.
                declared = ExactInvestigationTarget(**parse_json(raw_target))
                if target is None:
                    target = declared
                self._read(connection, lineage_id, revision_id, target)
                count += 1
        return BackupReceipt(count, heads)

    def backup(
        self, destination: Path, *, timeout_seconds: float = 30
    ) -> BackupReceipt:
        """New validated online backup; never overwrite/copy just the DB/rotate live history.

        Validation is of the coherent backup snapshot, not a comparison with a moving live
        head. No checkpoint-supplied code or native evaluator runs. On failure only newly
        reserved destination files are removed; the source remains intact.
        """
        if not 0 < timeout_seconds <= 300:
            raise _refuse(
                "unsupported_storage_settings",
                "Backup deadline must be 0..300 seconds.",
            )
        reserved = False
        validated = False
        target_connection = None
        destination = Path(destination)
        try:
            destination = _owned_directory(destination, create=True)
            path = destination / _DATABASE_NAME
            descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
            os.close(descriptor)
            reserved = True
            deadline = time.monotonic() + timeout_seconds

            def progress(status: int, remaining: int, total: int) -> None:
                if time.monotonic() > deadline:
                    raise _refuse(
                        "storage_busy", "Online backup exceeded its deadline."
                    )

            with self._connection() as source:
                target_connection = sqlite3.connect(path, isolation_level=None)
                source.backup(
                    target_connection, pages=128, progress=progress, sleep=0.01
                )
                self._validate_catalog(target_connection)
                target_connection.close()
                target_connection = None
            # Reopen through the ordinary supported settings boundary before success.
            restored = self.open(
                destination, read_only=True, busy_timeout_ms=self._busy_timeout_ms
            )
            with restored._connection() as connection:
                connection.execute("BEGIN")
                receipt = restored._validate_catalog(connection)
                validated = True
                return receipt
        except FileExistsError as error:
            raise _refuse(
                "store_already_exists", "Backup destination already contains a store."
            ) from error
        except (sqlite3.Error, OSError) as error:
            raise _storage_error(error) from error
        except (NativeReconstructionError, UnicodeError, TypeError) as error:
            raise _refuse("invalid_checkpoint_storage", str(error)) from error
        finally:
            if target_connection is not None:
                target_connection.close()
            if reserved and not validated:
                for suffix in ("", "-wal", "-shm"):
                    (destination / (_DATABASE_NAME + suffix)).unlink(missing_ok=True)
