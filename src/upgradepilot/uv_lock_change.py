"""Interpret exact package-version changes in complete ``uv.lock`` files.

This module owns the first bounded structured-lockfile rule accepted by ADR-0004.
It receives one modified ``ChangedFile`` plus exact base/head repository text already
validated by ``github_repository.py``. It parses TOML with Python's standard
``tomllib``, validates the admitted schema, groups package records by normalized
Python distribution name, and returns one file-level extracted transition or one
explicit dependency-evidence problem.

The module does not acquire GitHub content, compare several dependency files across a
pull request, perform PEP 440 ordering, infer dependency role or CI consumption, or
decide compatibility, safety, and maintainer action.
"""

from __future__ import annotations

import re
import tomllib
from collections import Counter, defaultdict
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from .dependency_change import (
    DependencyChangeEvidenceProblem,
    DependencyChangeExtractionResult,
    DependencyChangeProblemCode,
    DependencyFileEvidence,
    ExtractedDependencyVersionChange,
    normalize_package_name,
)
from .github_client import ChangedFile
from .github_repository import (
    ExactRepositoryFileEvidence,
    ExactRepositoryTextFile,
    UnavailableRepositoryFile,
)

_ARTIFACT_FIELDS = frozenset({"sdist", "wheels"})
_DISTRIBUTION_NAME_PATTERN = re.compile(
    r"^[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?$"
)
_MISSING = object()


@dataclass(frozen=True, slots=True)
class _UvPackageRecord:
    """One validated package table with normalized comparison identity."""

    package: str
    normalized_package: str
    version: str
    data: Mapping[str, Any]


@dataclass(frozen=True, slots=True)
class _ParsedUvLock:
    """Validated lock data grouped by normalized package name."""

    groups: Mapping[str, tuple[_UvPackageRecord, ...]]


def is_modified_uv_lock_file(changed_file: ChangedFile) -> bool:
    """Return whether one changed file is an admitted modified ``uv.lock``.

    Admission requires a normalized repository-relative POSIX path, the exact
    lowercase basename ``uv.lock``, and GitHub status ``modified``.
    """

    parts = _relative_path_parts(changed_file.filename)
    return (
        changed_file.status == "modified"
        and parts is not None
        and parts[-1] == "uv.lock"
    )


def extract_uv_lock_changes(
    changed_file: ChangedFile,
    base_file: ExactRepositoryFileEvidence,
    head_file: ExactRepositoryFileEvidence,
) -> DependencyChangeExtractionResult:
    """Extract at most one exact version transition from one modified lockfile.

    This remains a file-level result. A later PR-wide comparison must combine it with
    every other admitted dependency-file result before downstream work receives a
    trusted ``DependencyVersionChange``.
    """

    parts = _relative_path_parts(changed_file.filename)
    if parts is None or parts[-1] != "uv.lock":
        return DependencyChangeEvidenceProblem(
            reason="no_supported_dependency_file",
            detail=(
                f"Path {changed_file.filename!r} is not an admitted normalized "
                "repository-relative file whose basename is exactly 'uv.lock'."
            ),
        )

    if changed_file.status != "modified":
        return DependencyChangeEvidenceProblem(
            reason="unsupported_dependency_file_status",
            detail=(
                f"The uv.lock file status was {changed_file.status!r}; the first "
                "structured-lockfile rule supports only an in-place modified file."
            ),
        )

    unavailable = _first_unavailable_file(base_file, head_file)
    if unavailable is not None:
        return DependencyChangeEvidenceProblem(
            reason="dependency_file_unavailable",
            detail=(
                f"Exact uv.lock text was unavailable at revision "
                f"{unavailable.revision!r}: {unavailable.detail}"
            ),
        )

    assert isinstance(base_file, ExactRepositoryTextFile)
    assert isinstance(head_file, ExactRepositoryTextFile)

    evidence_result = _build_source_evidence(changed_file, base_file, head_file)
    if isinstance(evidence_result, DependencyChangeEvidenceProblem):
        return evidence_result
    evidence = evidence_result

    base_result = _parse_uv_lock(base_file, evidence, side="base")
    if isinstance(base_result, DependencyChangeEvidenceProblem):
        return base_result

    head_result = _parse_uv_lock(head_file, evidence, side="head")
    if isinstance(head_result, DependencyChangeEvidenceProblem):
        return head_result

    return _compare_uv_lock_packages(base_result, head_result, evidence)


def _first_unavailable_file(
    base_file: ExactRepositoryFileEvidence,
    head_file: ExactRepositoryFileEvidence,
) -> UnavailableRepositoryFile | None:
    """Preserve deterministic base-before-head unavailability precedence."""

    if isinstance(base_file, UnavailableRepositoryFile):
        return base_file
    if isinstance(head_file, UnavailableRepositoryFile):
        return head_file
    return None


def _build_source_evidence(
    changed_file: ChangedFile,
    base_file: ExactRepositoryTextFile,
    head_file: ExactRepositoryTextFile,
) -> DependencyFileEvidence | DependencyChangeEvidenceProblem:
    """Reconcile exact file identity before parsed data becomes evidence."""

    expected_path = changed_file.filename
    if (
        not base_file.repository
        or base_file.repository != head_file.repository
        or base_file.path != expected_path
        or base_file.returned_path != expected_path
        or head_file.path != expected_path
        or head_file.returned_path != expected_path
    ):
        return DependencyChangeEvidenceProblem(
            reason="invalid_dependency_record",
            detail=(
                "Exact uv.lock repository/path evidence did not consistently match "
                "the changed-file identity at base and head."
            ),
        )

    for side, file in (("base", base_file), ("head", head_file)):
        if not file.revision or not file.blob_sha:
            return DependencyChangeEvidenceProblem(
                reason="invalid_dependency_record",
                detail=(
                    f"The exact {side} uv.lock evidence lacked a revision or blob SHA."
                ),
            )
        if (
            type(file.reported_byte_count) is not int
            or type(file.decoded_byte_count) is not int
            or file.reported_byte_count < 0
            or file.decoded_byte_count < 0
            or file.reported_byte_count != file.decoded_byte_count
        ):
            return DependencyChangeEvidenceProblem(
                reason="invalid_dependency_record",
                detail=(
                    f"The exact {side} uv.lock byte evidence was invalid or "
                    "internally inconsistent."
                ),
            )

    return DependencyFileEvidence(
        path=expected_path,
        file_format="uv_lock",
        extraction_method="exact_base_head_files",
        base_revision=base_file.revision,
        base_blob_sha=base_file.blob_sha,
        base_byte_count=base_file.decoded_byte_count,
        head_revision=head_file.revision,
        head_blob_sha=head_file.blob_sha,
        head_byte_count=head_file.decoded_byte_count,
    )


def _parse_uv_lock(
    file: ExactRepositoryTextFile,
    evidence: DependencyFileEvidence,
    *,
    side: str,
) -> _ParsedUvLock | DependencyChangeEvidenceProblem:
    """Parse and validate one file under the first supported uv schema."""

    try:
        document = tomllib.loads(file.content)
    except tomllib.TOMLDecodeError as exc:
        return _problem(
            "malformed_dependency_file",
            f"The exact {side} uv.lock file was not valid TOML: {exc}.",
            evidence,
        )

    schema_version = document.get("version", _MISSING)
    if type(schema_version) is not int:
        return _problem(
            "malformed_dependency_file",
            f"The exact {side} uv.lock field 'version' must be an integer.",
            evidence,
        )
    if schema_version != 1:
        return _problem(
            "unsupported_uv_lock_schema",
            (
                f"The exact {side} uv.lock schema version was {schema_version!r}; "
                "the first supported boundary admits only version 1."
            ),
            evidence,
        )

    revision = document.get("revision", _MISSING)
    if type(revision) is not int or revision < 0:
        return _problem(
            "malformed_dependency_file",
            (
                f"The exact {side} uv.lock field 'revision' must be a "
                "non-negative integer."
            ),
            evidence,
        )

    raw_packages = document.get("package", _MISSING)
    if not isinstance(raw_packages, list):
        return _problem(
            "invalid_dependency_record",
            f"The exact {side} uv.lock field 'package' must be an array of tables.",
            evidence,
        )

    groups: defaultdict[str, list[_UvPackageRecord]] = defaultdict(list)
    for index, raw_record in enumerate(raw_packages):
        record_result = _validate_package_record(raw_record, side=side, index=index)
        if isinstance(record_result, str):
            return _problem(
                "invalid_dependency_record",
                record_result,
                evidence,
            )
        groups[record_result.normalized_package].append(record_result)

    return _ParsedUvLock(
        groups={name: tuple(records) for name, records in groups.items()}
    )


def _validate_package_record(
    raw_record: object,
    *,
    side: str,
    index: int,
) -> _UvPackageRecord | str:
    """Validate package identity while preserving every parsed field."""

    if not isinstance(raw_record, Mapping):
        return (
            f"The exact {side} uv.lock package record at index {index} "
            "was not a TOML table."
        )

    package = raw_record.get("name", _MISSING)
    version = raw_record.get("version", _MISSING)
    if (
        not isinstance(package, str)
        or not package
        or package != package.strip()
        or _DISTRIBUTION_NAME_PATTERN.fullmatch(package) is None
    ):
        return (
            f"The exact {side} uv.lock package record at index {index} had an "
            f"invalid distribution name: {package!r}."
        )
    if (
        not isinstance(version, str)
        or not version
        or version != version.strip()
    ):
        return (
            f"The exact {side} uv.lock package record at index {index} had an "
            "invalid non-empty textual 'version'."
        )

    return _UvPackageRecord(
        package=package,
        normalized_package=normalize_package_name(package),
        version=version,
        data=raw_record,
    )


def _compare_uv_lock_packages(
    base: _ParsedUvLock,
    head: _ParsedUvLock,
    evidence: DependencyFileEvidence,
) -> DependencyChangeExtractionResult:
    """Compare normalized groups and establish at most one transition."""

    all_names = sorted(set(base.groups) | set(head.groups))
    transitions: list[tuple[_UvPackageRecord, _UvPackageRecord]] = []

    for normalized_name in all_names:
        base_group = base.groups.get(normalized_name)
        head_group = head.groups.get(normalized_name)
        if base_group is None or head_group is None:
            return _problem(
                "unsupported_uv_lock_structural_change",
                (
                    f"Normalized package {normalized_name!r} was added or removed; "
                    "the first uv.lock rule supports only version transitions for "
                    "records present at both revisions."
                ),
                evidence,
            )

        if len(base_group) == 1 and len(head_group) == 1:
            comparison = _compare_single_record(
                base_group[0],
                head_group[0],
                evidence,
            )
            if isinstance(comparison, DependencyChangeEvidenceProblem):
                return comparison
            if comparison is not None:
                transitions.append(comparison)
            continue

        if _canonical_group(base_group) != _canonical_group(head_group):
            return _problem(
                "ambiguous_uv_lock_package_records",
                (
                    f"Repeated uv.lock records for normalized package "
                    f"{normalized_name!r} changed across base and head. The first "
                    "boundary does not pair repeated resolution branches heuristically."
                ),
                evidence,
            )

    if not transitions:
        return _problem(
            "version_unchanged",
            (
                "The admitted uv.lock files contained no exact package version "
                "transition after artifact-only differences were removed."
            ),
            evidence,
        )

    if len(transitions) > 1:
        packages = ", ".join(
            sorted({head_record.normalized_package for _, head_record in transitions})
        )
        return _problem(
            "multiple_dependency_version_changes",
            (
                "The admitted uv.lock file established several package version "
                f"transitions ({packages}); B2 requires exactly one."
            ),
            evidence,
        )

    base_record, head_record = transitions[0]
    return ExtractedDependencyVersionChange(
        package=head_record.package,
        normalized_package=head_record.normalized_package,
        old_version=base_record.version,
        proposed_version=head_record.version,
        source_evidence=evidence,
    )


def _compare_single_record(
    base: _UvPackageRecord,
    head: _UvPackageRecord,
    evidence: DependencyFileEvidence,
) -> (
    tuple[_UvPackageRecord, _UvPackageRecord]
    | DependencyChangeEvidenceProblem
    | None
):
    """Compare one unambiguous record under exact resolution-context rules."""

    if (
        base.data.get("source", _MISSING)
        != head.data.get("source", _MISSING)
        or base.data.get("resolution-markers", _MISSING)
        != head.data.get("resolution-markers", _MISSING)
    ):
        return _problem(
            "unsupported_uv_lock_structural_change",
            (
                f"The source or resolution-marker context for normalized package "
                f"{base.normalized_package!r} changed across base and head."
            ),
            evidence,
        )

    # A version transition may legitimately change attached dependency/package
    # metadata. Source and resolution context remain the pairing boundary.
    if base.version != head.version:
        return (base, head)

    if _canonical_record(base.data) != _canonical_record(head.data):
        return _problem(
            "unsupported_uv_lock_structural_change",
            (
                f"Normalized package {base.normalized_package!r} kept version "
                f"{base.version!r} but changed non-artifact structure."
            ),
            evidence,
        )

    return None


def _canonical_group(
    records: tuple[_UvPackageRecord, ...],
) -> Counter[object]:
    """Compare repeated records as an unordered multiset with multiplicity."""

    return Counter(_canonical_record(record.data) for record in records)


def _canonical_record(record: Mapping[str, Any]) -> object:
    """Remove only top-level artifact fields and freeze every other value."""

    return _freeze_toml_value(
        {key: value for key, value in record.items() if key not in _ARTIFACT_FIELDS}
    )


def _freeze_toml_value(value: object) -> object:
    """Convert parsed TOML data into deterministic hashable structure."""

    if isinstance(value, Mapping):
        return (
            "mapping",
            tuple(
                sorted(
                    (str(key), _freeze_toml_value(item))
                    for key, item in value.items()
                )
            ),
        )
    if isinstance(value, list):
        return ("list", tuple(_freeze_toml_value(item) for item in value))
    return (type(value).__qualname__, repr(value))


def _problem(
    reason: DependencyChangeProblemCode,
    detail: str,
    evidence: DependencyFileEvidence,
) -> DependencyChangeEvidenceProblem:
    """Build one source-attached normal stopping result."""

    return DependencyChangeEvidenceProblem(
        reason=reason,
        detail=detail,
        source_evidence=(evidence,),
    )


def _relative_path_parts(path: str) -> tuple[str, ...] | None:
    """Return normalized POSIX repository-relative components or ``None``."""

    if not isinstance(path, str) or not path or path.startswith("/") or "\\" in path:
        return None
    parts = tuple(path.split("/"))
    if any(not part or part in {".", ".."} for part in parts):
        return None
    return parts
