"""Parse the bounded ``uv.lock`` structure shared by current uv consumers.

RESPONSIBILITY / FLOW
---------------------
Exact repository-file acquisition is owned upstream by ``github/repository.py``. This module
starts from admitted text and establishes only the uv-format facts that both current semantic
consumers need to trust before they interpret the lock differently::

    exact uv.lock text
        -> parse TOML
        -> admit schema/revision
        -> admit package-record identity/name/version/source shape
        -> preserve every package record and repeated normalized-name group
        -> UvLockStructure | UvLockStructureProblem

``dependency/uv_lock.py`` then compares two admitted structures to derive dependency-transition
semantics. ``dependency/uv_membership.py`` separately projects one admitted structure into the
edge/root fields needed for explicit-root reachability.

The split is deliberate: dependency edges, selected groups/extras, traversal, base/head pairing,
and artifact-only comparison rules are consumer semantics, not facts that need duplicate
admission here. Unknown package fields are preserved in ``record_data`` so consumers can retain
or interpret them without this module pretending to implement the complete uv lock format.

This is uv-specific structural admission. It is not a generic dependency graph, package-manager
abstraction, uv runtime/configuration interpreter, lock-currentness check, or resolver proof.
"""

from __future__ import annotations

import re
import tomllib
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, Literal

from ..package_identity import normalize_package_name


type UvLockStructureProblemCode = Literal[
    "malformed_uv_lock",
    "unsupported_uv_lock_schema",
    "invalid_uv_lock_package_record",
]

_VERSIONLESS_SOURCE_KEYS = frozenset({"editable", "virtual"})
_DISTRIBUTION_NAME_PATTERN = re.compile(
    r"^[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?$"
)
_MISSING = object()


@dataclass(frozen=True, slots=True)
class UvLockStructureProblem:
    """Explain why exact lock text could not enter the bounded structural model."""

    code: UvLockStructureProblemCode
    detail: str


@dataclass(frozen=True, slots=True)
class UvLockPackageRecord:
    """One admitted ``[[package]]`` record before consumer-specific interpretation.

    ``version=None`` has exactly one admitted meaning: the record is a versionless local
    editable/virtual package with the narrow source shape validated by this module.
    ``record_data`` preserves the complete TOML table because the transition and reachability
    consumers intentionally need different additional fields from the same record.
    """

    index: int
    package: str
    normalized_package: str
    version: str | None
    source: object | None
    record_data: Mapping[str, Any]


@dataclass(frozen=True, slots=True)
class UvLockStructure:
    """Bounded admitted structure for one exact ``uv.lock`` document.

    Record order is preserved in ``packages`` for source fidelity. ``by_name`` preserves every
    repeated record for a normalized package; it never treats list position as universal-lock
    branch identity.
    """

    schema_version: int
    revision: int
    packages: tuple[UvLockPackageRecord, ...]
    by_name: Mapping[str, tuple[UvLockPackageRecord, ...]]


def parse_uv_lock_structure(content: str) -> UvLockStructure | UvLockStructureProblem:
    """Parse exact ``uv.lock`` text into the smallest shared admitted structure.

    Success authorizes consumers to rely on schema/revision and core package-record admission
    only. It does not establish any dependency transition, selected-root reachability, lock
    currentness, resolver result, installation, or runtime behavior.
    """

    try:
        document = tomllib.loads(content)
    except tomllib.TOMLDecodeError as exc:
        return UvLockStructureProblem(
            code="malformed_uv_lock",
            detail=f"Exact uv.lock text is not valid TOML: {exc}.",
        )

    # bool is a subclass of int in Python, so exact type checks prevent TOML ``true`` from
    # being silently admitted as schema version 1 or as a lock revision.
    schema_version = document.get("version", _MISSING)
    if type(schema_version) is not int:
        return UvLockStructureProblem(
            code="malformed_uv_lock",
            detail="The uv.lock field 'version' must be an integer.",
        )
    if schema_version != 1:
        return UvLockStructureProblem(
            code="unsupported_uv_lock_schema",
            detail=(
                f"The uv.lock schema version was {schema_version!r}; "
                "the bounded structural parser admits only version 1."
            ),
        )

    revision = document.get("revision", _MISSING)
    if type(revision) is not int or revision < 0:
        return UvLockStructureProblem(
            code="malformed_uv_lock",
            detail="The uv.lock field 'revision' must be a non-negative integer.",
        )

    raw_packages = document.get("package", _MISSING)
    if not isinstance(raw_packages, list):
        return UvLockStructureProblem(
            code="invalid_uv_lock_package_record",
            detail="The uv.lock field 'package' must be an array of tables.",
        )

    packages: list[UvLockPackageRecord] = []
    by_name: dict[str, list[UvLockPackageRecord]] = {}
    for index, raw_record in enumerate(raw_packages):
        parsed = _parse_package_record(raw_record, index=index)
        if isinstance(parsed, UvLockStructureProblem):
            return parsed
        packages.append(parsed)
        by_name.setdefault(parsed.normalized_package, []).append(parsed)

    return UvLockStructure(
        schema_version=schema_version,
        revision=revision,
        packages=tuple(packages),
        by_name={name: tuple(records) for name, records in by_name.items()},
    )


def _parse_package_record(
    raw_record: object,
    *,
    index: int,
) -> UvLockPackageRecord | UvLockStructureProblem:
    if not isinstance(raw_record, Mapping):
        return _invalid_record(
            f"uv.lock package record at index {index} is not a TOML table."
        )

    package = raw_record.get("name", _MISSING)
    if not _valid_distribution_name(package):
        return _invalid_record(
            f"uv.lock package record at index {index} has an invalid distribution name: "
            f"{package!r}."
        )
    assert isinstance(package, str)

    raw_version = raw_record.get("version", _MISSING)
    source = raw_record.get("source")
    if raw_version is _MISSING:
        # uv can omit a package version for local editable/virtual workspace records. Keeping
        # this exception here prevents transition and reachability consumers from drifting on
        # what a versionless package record means.
        if not _is_admitted_versionless_source(source):
            return _invalid_record(
                f"uv.lock package record at index {index} for {package!r} lacks a textual "
                "'version' outside the admitted editable/virtual local-source boundary."
            )
        version: str | None = None
    elif (
        not isinstance(raw_version, str)
        or not raw_version
        or raw_version != raw_version.strip()
    ):
        return _invalid_record(
            f"uv.lock package record at index {index} for {package!r} has an invalid "
            "non-empty textual 'version'."
        )
    else:
        version = raw_version

    return UvLockPackageRecord(
        index=index,
        package=package,
        normalized_package=normalize_package_name(package),
        version=version,
        source=source,
        record_data=raw_record,
    )


def _valid_distribution_name(value: object) -> bool:
    return (
        isinstance(value, str)
        and bool(value)
        and value == value.strip()
        and _DISTRIBUTION_NAME_PATTERN.fullmatch(value) is not None
    )


def _is_admitted_versionless_source(source: object) -> bool:
    """Return whether ``source`` is exactly one admitted versionless local-source shape."""

    if not isinstance(source, Mapping) or len(source) != 1:
        return False
    key, value = next(iter(source.items()))
    return (
        key in _VERSIONLESS_SOURCE_KEYS
        and isinstance(value, str)
        and bool(value)
        and value == value.strip()
    )


def _invalid_record(detail: str) -> UvLockStructureProblem:
    return UvLockStructureProblem(
        code="invalid_uv_lock_package_record",
        detail=detail,
    )


__all__ = (
    "UvLockPackageRecord",
    "UvLockStructure",
    "UvLockStructureProblem",
    "UvLockStructureProblemCode",
    "parse_uv_lock_structure",
)
