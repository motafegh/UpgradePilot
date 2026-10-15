"""Immutable retained-source navigation for Workspace consumers.

Trusted preparation binds a frozen catalog of repository text and captured observations.
List/read/literal-search are projections of those bytes, never acquisition or semantic
assessment. ``query`` returns bounded versioned JSON with exact references, coverage and
work counts; ``consumer_access`` publishes actual delivery through the generic host.
No source text, capture label or digest supplies authority to execute code or assert truth.
"""

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import asdict, dataclass
from hashlib import sha256
from types import MappingProxyType
from typing import Literal

from ..github.identity import validate_commit_sha, validate_repository
from ..repository_path import repository_relative_parts
from .native_boundary import ExactInvestigationTarget
from .native_representation import json_bytes, object_fields, parse_json

MAX_SOURCE_FILE_BYTES = 4 * 1024 * 1024
MAX_SOURCE_CATALOG_BYTES = 64 * 1024 * 1024
MAX_SOURCE_FILES = 20_000
MAX_SOURCE_VIEW_BYTES = 256 * 1024
SOURCE_VIEW_REPRESENTATION = "retained-source-view/1"
_SOURCE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,79}\Z")
_REFERENCE = re.compile(r"source:([0-9a-f]{64}):L([1-9][0-9]*):([0-9]+)\Z")


def _path(path: str, *, prefix: bool = False) -> None:
    if prefix and path == "":
        return
    if prefix and path.endswith("/"):
        path = path[:-1]
    parts = repository_relative_parts(path)
    if parts is None or "/".join(parts) != path or len(path) > 512:
        raise ValueError("Source path must be normalized and repository-relative.")


def _text(value: str, maximum: int) -> None:
    if type(value) is not str or not value.strip() or len(value) > maximum:
        raise ValueError("Invalid bounded source label.")


@dataclass(frozen=True, slots=True)
class RetainedSourceScope:
    source_id: str
    repository: str
    revision: str
    kind: Literal["repository_text", "captured_observation"]
    capture_basis: str
    coverage_limit: str

    def __post_init__(self) -> None:
        if type(self.source_id) is not str or not _SOURCE_ID.fullmatch(self.source_id):
            raise ValueError("Invalid source identifier.")
        validate_repository(self.repository)
        validate_commit_sha(self.revision)
        if self.kind not in ("repository_text", "captured_observation"):
            raise ValueError("Unknown source capture kind.")
        _text(self.capture_basis, 2048)
        _text(self.coverage_limit, 4096)

    def descriptor(self) -> dict:
        return {
            "source_id": self.source_id,
            "repository": self.repository,
            "revision": self.revision,
            "kind": self.kind,
            "capture_basis": self.capture_basis,
            "coverage_limit": self.coverage_limit,
        }


@dataclass(frozen=True, slots=True)
class RetainedSourceFile:
    source_id: str
    path: str
    content: str
    capture_metadata: str | None = None

    def __post_init__(self) -> None:
        _path(self.path)
        if (
            type(self.content) is not str
            or len(self.content.encode("utf-8")) > MAX_SOURCE_FILE_BYTES
        ):
            raise ValueError("Unsupported source content capacity.")
        if self.capture_metadata is not None:
            _text(self.capture_metadata, 16384)
            if type(parse_json(self.capture_metadata.encode())) is not dict:
                raise ValueError("Capture metadata must be a bounded object.")


@dataclass(frozen=True, slots=True)
class SourceAccessResult:
    outcome: Literal["observed", "empty", "scoped_negative", "problem"]
    content: bytes
    examined_files: int
    examined_lines: int


@dataclass(frozen=True, init=False)
class RetainedSourceCatalog:
    """Host-prepared immutable data backend, not a second investigation state owner.

    Coverage describes only this admitted capture, including exclusions. A reference is
    addressability of exact retained content, not installed binding or source authenticity.
    """

    scopes: tuple[RetainedSourceScope, ...]
    files: tuple[RetainedSourceFile, ...]
    identity: str
    target: ExactInvestigationTarget | None
    _scopes: Mapping
    _files: Mapping
    _references: Mapping

    def __init__(
        self,
        scopes: tuple[RetainedSourceScope, ...],
        files: tuple[RetainedSourceFile, ...],
        *,
        target: ExactInvestigationTarget | None = None,
    ):
        if (
            type(scopes) is not tuple
            or type(files) is not tuple
            or not scopes
            or len(scopes) > 256
            or len(files) > MAX_SOURCE_FILES
        ):
            raise ValueError("Unsupported source catalog size.")
        scope_map = {scope.source_id: scope for scope in scopes}
        file_map = {(file.source_id, file.path): file for file in files}
        if len(scope_map) != len(scopes) or len(file_map) != len(files):
            raise ValueError("Duplicate source or path.")
        if (
            sum(len(file.content.encode("utf-8")) for file in files)
            > MAX_SOURCE_CATALOG_BYTES
        ):
            raise ValueError("Unsupported aggregate source capacity.")
        if any(file.source_id not in scope_map for file in files):
            raise ValueError("File has no admitted source scope.")
        object.__setattr__(self, "target", target)
        object.__setattr__(
            self, "scopes", tuple(sorted(scopes, key=lambda scope: scope.source_id))
        )
        object.__setattr__(
            self,
            "files",
            tuple(sorted(files, key=lambda file: (file.source_id, file.path))),
        )
        object.__setattr__(self, "_scopes", MappingProxyType(scope_map))
        object.__setattr__(self, "_files", MappingProxyType(file_map))
        descriptors = [self.descriptor(file) for file in self.files]
        object.__setattr__(
            self,
            "identity",
            sha256(
                json_bytes(
                    {
                        "target": asdict(target) if target is not None else None,
                        "scopes": [s.descriptor() for s in self.scopes],
                        "file_descriptor_digests": [
                            sha256(json_bytes(descriptor)).hexdigest()
                            for descriptor in descriptors
                        ],
                    }
                )
            ).hexdigest(),
        )
        object.__setattr__(
            self,
            "_references",
            MappingProxyType(
                {self.descriptor(file)["file_id"]: file for file in self.files}
            ),
        )

    def descriptor(self, file: RetainedSourceFile) -> dict:
        scope = self._scopes[file.source_id]
        body = dict(
            scope.descriptor(),
            path=file.path,
            content_sha256=sha256(file.content.encode()).hexdigest(),
            lines=len(file.content.splitlines()),
            capture_metadata=parse_json(file.capture_metadata.encode())
            if file.capture_metadata is not None
            else None,
            retention_gaps=["additional_capture_metadata_unavailable"]
            if file.capture_metadata is None
            else [],
        )
        return dict(body, file_id=sha256(json_bytes(body)).hexdigest())

    def _result(self, operation, outcome, payload, work=(0, 0)) -> SourceAccessResult:
        body = json_bytes(
            {
                "format": SOURCE_VIEW_REPRESENTATION,
                "catalog_id": self.identity,
                "operation": operation,
                "outcome": outcome,
                "payload": payload,
                "work": {"examined_files": work[0], "examined_lines": work[1]},
                "limit": "Only this frozen capture and the explicitly delivered page; no global absence or semantic conclusion.",
            }
        )
        if len(body) > MAX_SOURCE_VIEW_BYTES:
            if outcome == "problem":
                raise ValueError("Source view capacity cannot hold a problem envelope.")
            return self._result(
                operation,
                "problem",
                {
                    "reason": "source_view_capacity",
                    "detail": "Request a narrower page.",
                },
                work,
            )
        return SourceAccessResult(outcome, body, *work)

    def query(self, operation: str, arguments: dict) -> SourceAccessResult:
        """Closed, bounded navigation. Malformed/unknown scope is a problem, never zero evidence."""
        work = (0, 0)
        if type(operation) is not str or len(operation) > 80:
            return self._result(
                "invalid_operation", "problem", {"reason": "invalid_source_operation"}
            )
        try:
            if type(arguments) is not dict:
                raise ValueError("Arguments must be an object.")
            allowed = {
                "list_sources": set(),
                "list_paths": {"source_id", "prefix", "offset"},
                "read": {"source_id", "path", "start_line", "line_count"},
                "search": {"query", "source_id", "prefix", "offset"},
                "resolve": {"reference"},
            }
            if operation not in allowed or set(arguments) - allowed[operation]:
                raise ValueError("Unknown operation or extra argument.")
            if operation == "list_sources":
                return self._result(
                    operation,
                    "observed",
                    {"sources": [scope.descriptor() for scope in self.scopes]},
                )
            if operation == "resolve":
                reference = arguments["reference"]
                match = (
                    _REFERENCE.fullmatch(reference)
                    if type(reference) is str and len(reference) < 150
                    else None
                )
                if not match or match[1] not in self._references:
                    raise ValueError("Unknown source reference in this catalog.")
                file = self._references[match[1]]
                return self._read(
                    operation, file.source_id, file.path, int(match[2]), int(match[3])
                )
            source = arguments.get("source_id")
            if source is not None and (
                type(source) is not str or source not in self._scopes
            ):
                raise ValueError("Unknown source scope.")
            if operation in ("read", "list_paths") and source is None:
                raise ValueError("An exact source is required.")
            if operation == "read":
                return self._read(
                    operation,
                    source,
                    arguments["path"],
                    arguments.get("start_line", 1),
                    arguments.get("line_count", 20),
                )
            prefix = arguments.get("prefix", "")
            if type(prefix) is not str:
                raise ValueError("Invalid path prefix.")
            _path(prefix, prefix=True)
            offset = arguments.get("offset", 0)
            if type(offset) is not int or not 0 <= offset <= 1_000_000:
                raise ValueError("Invalid page offset.")
            candidates = [
                file
                for file in self.files
                if (source is None or file.source_id == source)
                and file.path.startswith(prefix)
            ]
            if operation == "list_paths":
                items = [self.descriptor(file) for file in candidates]
                work = (len(candidates), 0)
            else:
                query = arguments["query"]
                _text(query, 256)
                items = []
                total_matches = 0
                lines_examined = 0
                for file in candidates:
                    lines = file.content.splitlines()
                    descriptor = self.descriptor(file)
                    lines_examined += len(lines)
                    for number, line in enumerate(lines, 1):
                        if query.casefold() in line.casefold():
                            if offset <= total_matches < offset + 20:
                                items.append(
                                    {
                                        "source_id": file.source_id,
                                        "path": file.path,
                                        "line": number,
                                        "reference": f"source:{descriptor['file_id']}:L{number}:1",
                                        "preview": line[:500],
                                        "preview_omitted_characters": max(
                                            0, len(line) - 500
                                        ),
                                    }
                                )
                            total_matches += 1
                work = (len(candidates), lines_examined)
            total = len(items) if operation == "list_paths" else total_matches
            page = items[offset : offset + 20] if operation == "list_paths" else items
            next_offset = offset + len(page) if offset + len(page) < total else None
            # An offset past a nonempty result is an empty page, not a negative search.
            outcome = "observed" if page else ("empty" if total else "scoped_negative")
            return self._result(
                operation,
                outcome,
                {
                    "items": page,
                    "next_offset": next_offset,
                    "total_matches": total,
                    "source_id": source,
                    "prefix": prefix,
                    "query": arguments.get("query"),
                },
                work,
            )
        except (ValueError, KeyError, TypeError, UnicodeError) as error:
            return self._result(
                operation,
                "problem",
                {"reason": "invalid_source_query", "detail": str(error)},
                work,
            )

    def _read(self, operation, source, path, start, count) -> SourceAccessResult:
        _path(path)
        if (
            type(start) is not int
            or start < 1
            or type(count) is not int
            or not 0 <= count <= 100
        ):
            raise ValueError("Invalid line range.")
        file = self._files.get((source, path))
        if file is None:
            raise ValueError(
                "Path unavailable in this capture; absence outside capture is unknown."
            )
        lines = file.content.splitlines()
        if start > max(1, len(lines)) or (lines and count == 0):
            raise ValueError("Line range is outside retained content.")
        selected = lines[start - 1 : start - 1 + count]
        descriptor = self.descriptor(file)
        reference = f"source:{descriptor['file_id']}:L{start}:{len(selected)}"
        return self._result(
            operation,
            "observed" if selected else "empty",
            {
                "file": descriptor,
                "reference": reference,
                "start_line": start,
                "lines": selected,
                "next_line": start + len(selected)
                if start + len(selected) <= len(lines)
                else None,
            },
            (1, len(selected)),
        )


def read_source_delivery(content: bytes) -> dict:
    """Inspect a retained versioned delivery offline, without querying a backend."""
    if len(content) > MAX_SOURCE_VIEW_BYTES:
        raise ValueError("Unsupported source delivery capacity.")
    body = parse_json(content)
    if (
        type(body) is not dict
        or set(body)
        != {"format", "catalog_id", "operation", "outcome", "payload", "work", "limit"}
        or body.get("format") != SOURCE_VIEW_REPRESENTATION
        or type(body.get("catalog_id")) is not str
        or re.fullmatch(r"[0-9a-f]{64}", body["catalog_id"]) is None
        or type(body.get("operation")) is not str
        or len(body["operation"]) > 80
        or body.get("outcome")
        not in ("observed", "empty", "scoped_negative", "problem")
        or type(body.get("payload")) is not dict
        or type(body.get("work")) is not dict
        or set(body["work"]) != {"examined_files", "examined_lines"}
        or any(type(value) is not int or value < 0 for value in body["work"].values())
        or type(body.get("limit")) is not str
    ):
        raise ValueError("Unsupported source delivery representation.")
    return body


def encode_source_catalog(catalog: RetainedSourceCatalog) -> bytes:
    """Export explicit common input data; this file is not a Workspace checkpoint."""
    if catalog.target is None:
        raise ValueError("A published source profile needs an exact target.")
    return json_bytes(
        {
            "format": "retained-source-catalog/1",
            "target": asdict(catalog.target),
            "scopes": [scope.descriptor() for scope in catalog.scopes],
            "files": [
                {
                    "source_id": file.source_id,
                    "path": file.path,
                    "content": file.content,
                    "capture_metadata": file.capture_metadata,
                }
                for file in catalog.files
            ],
            "catalog_id": catalog.identity,
        }
    )


def read_source_catalog(
    data: bytes, *, expected_target: ExactInvestigationTarget
) -> RetainedSourceCatalog:
    """Read a host-admitted local source profile, not authenticate arbitrary source claims.

    Only fixed constructors are used; model output cannot install a catalog or strengthen
    its capture authority. Workspace recovery independently reads its retained deliveries.
    """
    body = parse_json(data)
    if (
        type(body) is not dict
        or set(body) != {"format", "target", "scopes", "files", "catalog_id"}
        or body["format"] != "retained-source-catalog/1"
        or json_bytes(body["target"]) != json_bytes(asdict(expected_target))
    ):
        raise ValueError("Unsupported or wrong-target source profile.")
    if (
        type(body["scopes"]) is not list
        or type(body["files"]) is not list
        or len(body["scopes"]) > 256
        or len(body["files"]) > MAX_SOURCE_FILES
    ):
        raise ValueError("Unsupported source profile size.")
    catalog = RetainedSourceCatalog(
        tuple(
            RetainedSourceScope(
                **object_fields(
                    item,
                    (
                        "source_id",
                        "repository",
                        "revision",
                        "kind",
                        "capture_basis",
                        "coverage_limit",
                    ),
                )
            )
            for item in body["scopes"]
        ),
        tuple(
            RetainedSourceFile(
                **object_fields(
                    item, ("source_id", "path", "content", "capture_metadata")
                )
            )
            for item in body["files"]
        ),
        target=expected_target,
    )
    if catalog.identity != body["catalog_id"]:
        raise ValueError("Source profile content/identity mismatch.")
    return catalog


def source_reference_was_delivered(reference: str, content: bytes) -> bool:
    """Check a precise line range against retained read bytes, without another source read.

    Search previews provide navigation, not a full untruncated line. Citation admission
    checks identity/delivery only and supplies no claim of semantic support or adequacy.
    """
    body = read_source_delivery(content)
    if body["operation"] not in ("read", "resolve") or body["outcome"] not in (
        "observed",
        "empty",
    ):
        return False
    match = (
        _REFERENCE.fullmatch(reference)
        if type(reference) is str and len(reference) < 150
        else None
    )
    payload = body["payload"]
    if match is None or match[1] != payload["file"]["file_id"]:
        return False
    start, count = int(match[2]), int(match[3])
    first, length = payload["start_line"], len(payload["lines"])
    return (count == 0 and length == 0 and start == first) or (
        count > 0 and first <= start and start + count <= first + length
    )
