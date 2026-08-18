"""Interpret exact package-version changes in complete ``uv.lock`` files.

The first bounded structured-lockfile rule accepts only modified ``uv.lock`` files at
normalized repository-relative paths. Complete base/head repository text is parsed with
``tomllib`` and compared conservatively; ambiguous structural changes remain explicit
problems rather than heuristic package pairings.

This module owns a deliberately narrow proposition:

``exact base/head uv.lock evidence -> one exact file-level version transition``

It does *not* decide whether the changed package belongs to a selected dependency
environment, was installed by CI, ran successfully, or is behaviorally compatible.
Those stronger propositions are owned by later dependency/CI layers.
"""

from __future__ import annotations

import re
import tomllib
from collections import Counter, defaultdict
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from ..github.pull_request import ChangedFile
from ..github.repository import (
    ExactRepositoryFileEvidence,
    RepositoryTextFile,
    UnavailableRepositoryFile,
)
from ..package_identity import normalize_package_name
from ..repository_path import repository_relative_parts
from .change import (
    DependencyChangeExtractionResult,
    DependencyChangeProblem,
    DependencyChangeProblemCode,
    DependencyChangeSourceEvidence,
    ExtractedDependencyVersionChange,
)

_ARTIFACT_FIELDS = frozenset({"sdist", "wheels"})
_VERSIONLESS_SOURCE_KEYS = frozenset({"editable", "virtual"})
_DISTRIBUTION_NAME_PATTERN = re.compile(
    r"^[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?$"
)
_MISSING = object()


@dataclass(frozen=True, slots=True)
class _UvPackageRecord:
    """One validated lock-package record in the shape needed for comparison.

    ``package`` preserves the spelling from the lockfile; ``normalized_package`` is
    the comparison key. ``version`` may be absent only for the admitted workspace
    record shapes validated below.
    """

    package: str
    normalized_package: str
    version: str | None
    data: Mapping[str, Any]


@dataclass(frozen=True, slots=True)
class _ParsedUvLock:
    """Validated package records grouped by normalized distribution name.

    A normalized name can map to more than one record because a universal lock may
    contain repeated resolution branches. Repeated records therefore cannot be paired
    by position or guessed heuristically later.
    """

    groups: Mapping[str, tuple[_UvPackageRecord, ...]]


def is_modified_uv_lock_file(changed_file: ChangedFile) -> bool:
    """Return whether a changed file is admitted by the first uv.lock boundary."""

    parts = repository_relative_parts(changed_file.filename)
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
    """Extract one safe file-level version transition from exact base/head locks.

    The function is a guard-clause pipeline. Each stage earns permission for the next:
    path/status admission -> exact-file availability -> provenance -> parsing ->
    conservative comparison. Expected evidence failures return ``DependencyChangeProblem``
    instead of being guessed through.
    """

    parts = repository_relative_parts(changed_file.filename)
    if parts is None or parts[-1] != "uv.lock":
        return DependencyChangeProblem(
            reason="no_supported_dependency_file",
            detail=(
                f"Path {changed_file.filename!r} is not an admitted normalized "
                "repository-relative file whose basename is exactly 'uv.lock'."
            ),
        )

    # The initial rule compares one lockfile in place. Addition/deletion/rename would
    # require different semantics, so those shapes stop explicitly instead of being
    # treated as ordinary package-version transitions.
    if changed_file.status != "modified":
        return DependencyChangeProblem(
            reason="unsupported_dependency_file_status",
            detail=(
                f"The uv.lock file status was {changed_file.status!r}; the first "
                "structured-lockfile rule supports only an in-place modified file."
            ),
        )

    unavailable = _first_unavailable_file(base_file, head_file)
    if unavailable is not None:
        return DependencyChangeProblem(
            reason="dependency_file_unavailable",
            detail=(
                f"Exact uv.lock text was unavailable at revision "
                f"{unavailable.revision!r}: {unavailable.detail}"
            ),
        )

    # ExactRepositoryFileEvidence is a union of available text and typed-unavailable
    # evidence. The early return above removes the unavailable case; these assertions
    # make that control-flow invariant explicit before content/provenance is trusted.
    assert isinstance(base_file, RepositoryTextFile)
    assert isinstance(head_file, RepositoryTextFile)

    evidence_result = _build_source_evidence(changed_file, base_file, head_file)
    if isinstance(evidence_result, DependencyChangeProblem):
        return evidence_result
    evidence = evidence_result

    base_result = _parse_uv_lock(base_file, evidence, side="base")
    if isinstance(base_result, DependencyChangeProblem):
        return base_result
    head_result = _parse_uv_lock(head_file, evidence, side="head")
    if isinstance(head_result, DependencyChangeProblem):
        return head_result
    return _compare_uv_lock_packages(base_result, head_result, evidence)


def _first_unavailable_file(
    base_file: ExactRepositoryFileEvidence,
    head_file: ExactRepositoryFileEvidence,
) -> UnavailableRepositoryFile | None:
    """Return the first unavailable exact file so extraction can stop explicitly."""

    if isinstance(base_file, UnavailableRepositoryFile):
        return base_file
    if isinstance(head_file, UnavailableRepositoryFile):
        return head_file
    return None


def _build_source_evidence(
    changed_file: ChangedFile,
    base_file: RepositoryTextFile,
    head_file: RepositoryTextFile,
) -> DependencyChangeSourceEvidence | DependencyChangeProblem:
    """Bind the semantic comparison to coherent exact-file provenance.

    ``RepositoryTextFile`` still permits older/manual fixtures with optional strong
    provenance fields. This stricter semantic boundary therefore revalidates the fields
    it depends on instead of assuming every constructed instance came from the runtime
    GitHub provider.

    Blob SHAs here are provider-reported identities. This function requires/preserves
    them; it does not recompute a Git blob hash from the decoded file content.
    """

    expected_path = changed_file.filename
    if (
        not base_file.repository
        or base_file.repository != head_file.repository
        or base_file.path != expected_path
        or base_file.returned_path != expected_path
        or head_file.path != expected_path
        or head_file.returned_path != expected_path
    ):
        return DependencyChangeProblem(
            reason="invalid_dependency_record",
            detail=(
                "Exact uv.lock repository/path evidence did not consistently match "
                "the changed-file identity at base and head."
            ),
        )

    # Apply the same exact-identity checks to both historical sides. Byte-count equality
    # is acquisition-consistency evidence, not a package/dependency semantic claim.
    for side, file in (("base", base_file), ("head", head_file)):
        if not file.revision or not file.blob_sha:
            return DependencyChangeProblem(
                reason="invalid_dependency_record",
                detail=f"The exact {side} uv.lock evidence lacked a revision or blob SHA.",
            )
        if (
            type(file.reported_byte_count) is not int
            or type(file.decoded_byte_count) is not int
            or file.reported_byte_count < 0
            or file.decoded_byte_count < 0
            or file.reported_byte_count != file.decoded_byte_count
        ):
            return DependencyChangeProblem(
                reason="invalid_dependency_record",
                detail=(
                    f"The exact {side} uv.lock byte evidence was invalid or "
                    "internally inconsistent."
                ),
            )

    return DependencyChangeSourceEvidence(
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
    file: RepositoryTextFile,
    evidence: DependencyChangeSourceEvidence,
    *,
    side: str,
) -> _ParsedUvLock | DependencyChangeProblem:
    """Parse and validate the bounded uv.lock structure required by comparison.

    The document's top-level ``revision`` is uv's own lock-format metadata. It is not
    the Git commit revision stored on ``RepositoryTextFile.revision``.
    """

    try:
        document = tomllib.loads(file.content)
    except tomllib.TOMLDecodeError as exc:
        return _problem(
            "malformed_dependency_file",
            f"The exact {side} uv.lock file was not valid TOML: {exc}.",
            evidence,
        )

    # Admit only the lock schema that this comparison logic was designed/tested for;
    # a newer schema must not be interpreted using assumptions from schema version 1.
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
            f"The exact {side} uv.lock field 'revision' must be a non-negative integer.",
            evidence,
        )

    raw_packages = document.get("package", _MISSING)
    if not isinstance(raw_packages, list):
        return _problem(
            "invalid_dependency_record",
            f"The exact {side} uv.lock field 'package' must be an array of tables.",
            evidence,
        )

    # Group by normalized distribution name so spelling variants such as Demo_Pkg and
    # demo-pkg compare as one package identity. Multiple records remain separate within
    # the group because universal-lock branches may make pairing ambiguous.
    groups: defaultdict[str, list[_UvPackageRecord]] = defaultdict(list)
    for index, raw_record in enumerate(raw_packages):
        record_result = _validate_package_record(raw_record, side=side, index=index)
        if isinstance(record_result, str):
            return _problem("invalid_dependency_record", record_result, evidence)
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
    """Validate one package table and project it into the comparison model."""

    if not isinstance(raw_record, Mapping):
        return f"The exact {side} uv.lock package record at index {index} was not a TOML table."

    package = raw_record.get("name", _MISSING)
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

    raw_version = raw_record.get("version", _MISSING)
    if raw_version is _MISSING:
        source = raw_record.get("source", _MISSING)
        # Editable/virtual workspace records may legitimately be versionless. Other
        # versionless shapes are outside this extractor's first supported boundary.
        if not _is_admitted_versionless_source(source):
            return (
                f"The exact {side} uv.lock package record at index {index} lacked "
                "a textual 'version' outside the admitted editable/virtual "
                "workspace-record boundary."
            )
        version: str | None = None
    elif (
        not isinstance(raw_version, str)
        or not raw_version
        or raw_version != raw_version.strip()
    ):
        return (
            f"The exact {side} uv.lock package record at index {index} had an "
            "invalid non-empty textual 'version'."
        )
    else:
        version = raw_version

    return _UvPackageRecord(
        package=package,
        normalized_package=normalize_package_name(package),
        version=version,
        data=raw_record,
    )


def _is_admitted_versionless_source(source: object) -> bool:
    """Recognize the narrow workspace-source shapes allowed without a version."""

    if not isinstance(source, Mapping) or len(source) != 1:
        return False
    key, value = next(iter(source.items()))
    return (
        key in _VERSIONLESS_SOURCE_KEYS
        and isinstance(value, str)
        and bool(value)
        and value == value.strip()
    )


def _compare_uv_lock_packages(
    base: _ParsedUvLock,
    head: _ParsedUvLock,
    evidence: DependencyChangeSourceEvidence,
) -> DependencyChangeExtractionResult:
    """Compare parsed locks and require exactly one unambiguous version transition.

    This is still file-level change extraction. It does not classify the changed package
    as direct/transitive or establish membership in any selected project environment.
    """

    # Union both key sets so package additions/removals cannot disappear merely because
    # iteration started from one side of the comparison.
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
            comparison = _compare_single_record(base_group[0], head_group[0], evidence)
            if isinstance(comparison, DependencyChangeProblem):
                return comparison
            if comparison is not None:
                transitions.append(comparison)
            continue

        # Repeated records can represent distinct resolution branches. We only accept
        # them when the canonical groups are unchanged; otherwise pairing one base
        # branch to one head branch would be a heuristic guess.
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

    # B2's current dependency-change contract represents one package transition. A
    # lockfile that changes several packages is therefore explicit ambiguity at this
    # boundary, not a request to pick a likely candidate.
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
    assert base_record.version is not None
    assert head_record.version is not None
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
    evidence: DependencyChangeSourceEvidence,
) -> tuple[_UvPackageRecord, _UvPackageRecord] | DependencyChangeProblem | None:
    """Compare one base/head record without losing structural context.

    Returns the record pair only for a clean textual version transition, ``None`` for
    no relevant transition, or a typed problem when another semantic field changed in
    a way that makes simple version pairing unsafe.
    """

    # A version change is not safe to pair as "same package, new version" when the
    # package source or resolution branch itself also changed.
    if (
        base.data.get("source", _MISSING) != head.data.get("source", _MISSING)
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

    if base.version is None or head.version is None:
        if base.version != head.version:
            return _problem(
                "unsupported_uv_lock_structural_change",
                (
                    f"Normalized package {base.normalized_package!r} gained or lost "
                    "an exact textual version across base and head."
                ),
                evidence,
            )
        if _canonical_record(base.data) != _canonical_record(head.data):
            return _problem(
                "unsupported_uv_lock_structural_change",
                (
                    f"Versionless workspace package {base.normalized_package!r} "
                    "changed non-artifact structure."
                ),
                evidence,
            )
        return None

    # This pair is merely an exact file-level version transition. Later environment
    # code, not this comparison, decides whether the package is direct/transitive or
    # belongs to the selected dependency environment.
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


def _canonical_group(records: tuple[_UvPackageRecord, ...]) -> Counter[object]:
    """Return order-insensitive structural identities for repeated package records."""

    return Counter(_canonical_record(record.data) for record in records)


def _canonical_record(record: Mapping[str, Any]) -> object:
    """Return semantic record structure while ignoring artifact download churn.

    Wheel/sdist metadata can change while the package version and relevant dependency
    structure remain the same, so those artifact fields are excluded from this narrow
    version-transition comparison.
    """

    return _freeze_toml_value(
        {key: value for key, value in record.items() if key not in _ARTIFACT_FIELDS}
    )


def _freeze_toml_value(value: object) -> object:
    """Convert nested TOML values into deterministic, hashable structural values."""

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
    evidence: DependencyChangeSourceEvidence,
) -> DependencyChangeProblem:
    """Attach already-established source provenance to a later semantic stop."""

    return DependencyChangeProblem(
        reason=reason,
        detail=detail,
        source_evidence=(evidence,),
    )


__all__ = (
    "extract_uv_lock_changes",
    "is_modified_uv_lock_file",
)
