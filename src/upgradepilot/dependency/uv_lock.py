"""Extract one exact dependency-version transition from complete ``uv.lock`` evidence.

RESPONSIBILITY / FLOW
---------------------
``dependency/analysis.py::analyze_dependency_change(...)`` is the normal caller:

``ChangedFile`` + exact base/head repository files
    -> ``extract_uv_lock_changes(...)``  [PRIMARY ENTRY]
    -> admit path/status and exact provenance
    -> parse/validate base and head ``uv.lock``
    -> group records by normalized package identity
    -> compare conservatively
    -> ``ExtractedDependencyVersionChange`` or ``DependencyChangeProblem``
    -> ``dependency/change.py::compare_extracted_dependency_changes(...)``

``github/pull_request.py`` owns ``ChangedFile``. ``github/repository.py`` owns
``ExactRepositoryFileEvidence``: each historical side is either ``RepositoryTextFile``
(complete text/provenance) or ``UnavailableRepositoryFile`` (typed acquisition failure).
``dependency/change.py`` owns the source-independent success/problem output types.

PUBLIC API
----------
``extract_uv_lock_changes(...)`` is the semantic entry point developers should start from.
``is_modified_uv_lock_file(...)`` is only the cheap pre-acquisition admission gate.
There is currently no transitional/legacy public API in this module.

Representative inputs::

    ChangedFile(filename="uv.lock", status="modified", ...)
    RepositoryTextFile(path="uv.lock", revision="<Git SHA>", content="...", ...)

Representative success::

    ExtractedDependencyVersionChange(
        normalized_package="example-package",
        old_version="1.2.3",
        proposed_version="1.2.4",
        ...,
    )

PROOF BOUNDARY
--------------
Success proves one exact textual package-version transition in the admitted base/head lock
files. It does not prove environment membership, CI installation/exercise, resolver
currentness, or upgrade compatibility/safety.
"""

from __future__ import annotations

# Parsing/comparison tools used by this module: TOML parsing; raw-name admission; grouping;
# and multiset comparison for repeated lock records.
import re
import tomllib
from collections import Counter, defaultdict
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, Literal

# Upstream PR/exact-file evidence contracts.
from ..github.pull_request import ChangedFile
from ..github.repository import (
    ExactRepositoryFileEvidence,
    RepositoryTextFile,
    UnavailableRepositoryFile,
)

# Shared path and package-identity rules.
from ..package_identity import normalize_package_name
from ..repository_path import repository_relative_parts

# Source-independent dependency-change outputs/provenance.
from .change import (
    DependencyChangeExtractionResult,
    DependencyChangeProblem,
    DependencyChangeProblemCode,
    DependencyChangeSourceEvidence,
    ExtractedDependencyVersionChange,
)

# Artifact download metadata may churn without changing the package/dependency semantics this
# version-change extractor compares, so canonical structural comparison ignores these fields.
_ARTIFACT_FIELDS = frozenset({"sdist", "wheels"})

# uv local/workspace records may legitimately omit a textual version. ``editable`` uses local
# source directly; ``virtual`` does not install the local project itself. Only these exact
# one-key source shapes are admitted as meaningful versionless records.
_VERSIONLESS_SOURCE_KEYS = frozenset({"editable", "virtual"})

# Raw distribution-name admission before normalization. A match requires an ASCII letter or
# digit at both ends and permits letters/digits/./_/- inside; no match rejects the record.
_DISTRIBUTION_NAME_PATTERN = re.compile(
    r"^[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?$"
)

# Distinguish an absent TOML key from a present false-like value during structural checks.
_MISSING = object()


# ---------------------------------------------------------------------------
# Internal comparison models
# ---------------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class _UvPackageRecord:
    """Validated ``[[package]]`` record used by the comparison stage.

    ``version=None`` has one admitted meaning: a recognized editable/virtual versionless
    source. ``record_data`` retains full structure because name/version alone is insufficient
    for safe base/head pairing.
    """

    package: str
    normalized_package: str
    version: str | None
    record_data: Mapping[str, Any]


@dataclass(frozen=True, slots=True)
class _ParsedUvLock:
    """Validated lock grouped by normalized package identity.

    All records are preserved because a universal lock may contain repeated package records
    for different resolution branches; list position is not trusted branch identity.
    """

    groups: Mapping[str, tuple[_UvPackageRecord, ...]]


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def is_modified_uv_lock_file(changed_file: ChangedFile) -> bool:
    """Return whether this changed file is eligible for exact uv.lock acquisition.

    ``analysis.py`` uses ``True`` to proceed to exact base/head file acquisition. This helper
    reads only the repository-relative path and changed-file status.
    """

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
    """Primary entry point: extract one safe file-level version transition.

    Inputs are the PR ``ChangedFile`` plus exact base/head repository evidence. The result is
    the dependency/change.py-owned extraction union: one extracted transition or one typed
    problem. ``analysis.py`` later combines this result with other dependency sources.
    """

    # These guards progressively establish what later stages may trust:
    # admitted path -> in-place modification -> complete base/head text -> coherent exact
    # provenance -> supported parsed lock models. Failure at any stage returns a typed problem.
    parts = repository_relative_parts(changed_file.filename)
    if parts is None or parts[-1] != "uv.lock":
        return DependencyChangeProblem(
            reason="no_supported_dependency_file",
            detail=(
                f"Path {changed_file.filename!r} is not an admitted normalized "
                "repository-relative file whose basename is exactly 'uv.lock'."
            ),
        )

    # Addition/deletion/rename needs different evidence semantics from in-place comparison.
    if changed_file.status != "modified":
        return DependencyChangeProblem(
            reason="unsupported_dependency_file_status",
            detail=(
                f"The uv.lock file status was {changed_file.status!r}; the first "
                "structured-lockfile rule supports only an in-place modified file."
            ),
        )

    # Parsing one historical side without the other could invent a transition.
    unavailable = _first_unavailable_file(base_file, head_file)
    if unavailable is not None:
        return DependencyChangeProblem(
            reason="dependency_file_unavailable",
            detail=(
                f"Exact uv.lock text was unavailable at revision "
                f"{unavailable.revision!r}: {unavailable.detail}"
            ),
        )

    # The availability guard narrows the evidence union to complete text on both sides.
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


# ---------------------------------------------------------------------------
# Evidence availability and provenance validation
# ---------------------------------------------------------------------------


def _first_unavailable_file(
    base_file: ExactRepositoryFileEvidence,
    head_file: ExactRepositoryFileEvidence,
) -> UnavailableRepositoryFile | None:
    """Return the first unavailable historical side, otherwise ``None``."""

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
    """Validate exact-file identity and bind dependency-change source provenance.

    Success means repository/path/revision/blob/byte metadata coherently identifies the two
    historical files, allowing their content to support later semantic parsing.
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

    # ``repository_file.revision`` is the immutable Git commit SHA, not uv.lock's unrelated
    # top-level integer ``revision`` field. Byte-count equality checks acquisition consistency.
    for side, repository_file in (("base", base_file), ("head", head_file)):
        if not repository_file.revision or not repository_file.blob_sha:
            return DependencyChangeProblem(
                reason="invalid_dependency_record",
                detail=f"The exact {side} uv.lock evidence lacked a revision or blob SHA.",
            )
        if (
            type(repository_file.reported_byte_count) is not int
            or type(repository_file.decoded_byte_count) is not int
            or repository_file.reported_byte_count < 0
            or repository_file.decoded_byte_count < 0
            or repository_file.reported_byte_count
            != repository_file.decoded_byte_count
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


# ---------------------------------------------------------------------------
# Parsing and package-record validation
# ---------------------------------------------------------------------------


def _parse_uv_lock(
    repository_file: RepositoryTextFile,
    evidence: DependencyChangeSourceEvidence,
    *,
    side: Literal["base", "head"],
) -> _ParsedUvLock | DependencyChangeProblem:
    """Parse one exact historical lock into the internal comparison model.

    ``side`` is restricted to the two PR-history roles for diagnostics. Success returns a
    schema/record-validated ``_ParsedUvLock``; malformed or unsupported evidence returns a
    typed problem carrying the already-bound source provenance.
    """

    try:
        document = tomllib.loads(repository_file.content)
    except tomllib.TOMLDecodeError as exc:
        return _problem(
            "malformed_dependency_file",
            f"The exact {side} uv.lock file was not valid TOML: {exc}.",
            evidence,
        )

    # Top-level ``version`` is the uv.lock schema version, not a package version. We only
    # interpret schema 1; guessing newer schema meaning would manufacture confidence.
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

    # uv.lock ``revision`` is lock-format metadata, not the Git commit revision above.
    revision = document.get("revision", _MISSING)
    if type(revision) is not int or revision < 0:
        return _problem(
            "malformed_dependency_file",
            f"The exact {side} uv.lock field 'revision' must be a non-negative integer.",
            evidence,
        )

    # Repeated TOML ``[[package]]`` tables parse as this top-level list.
    raw_packages = document.get("package", _MISSING)
    if not isinstance(raw_packages, list):
        return _problem(
            "invalid_dependency_record",
            f"The exact {side} uv.lock field 'package' must be an array of tables.",
            evidence,
        )

    # Preserve every record for a normalized name; universal-lock branch ambiguity must not
    # be erased by keeping only one record or pairing records by list position.
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
    side: Literal["base", "head"],
    index: int,
) -> _UvPackageRecord | str:
    """Validate one raw ``[[package]]`` table for later grouping/comparison.

    The input is normally a mapping such as
    ``{"name": "requests", "version": "2.32.5", "source": {...}}``. A returned string is
    a local validation explanation that ``_parse_uv_lock(...)`` converts to the shared problem.
    """

    if not isinstance(raw_record, Mapping):
        return f"The exact {side} uv.lock package record at index {index} was not a TOML table."

    # Validate raw spelling before normalization so malformed evidence cannot be “cleaned up”
    # into a trusted package identity.
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

        # Missing version is legitimate only for the admitted editable/virtual source shapes;
        # otherwise absence remains unsupported instead of being guessed as workspace data.
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
        record_data=raw_record,
    )


def _is_admitted_versionless_source(source: object) -> bool:
    """Return whether ``source`` is exactly one admitted versionless local-source shape.

    Examples: ``{"editable": "."}`` and ``{"virtual": "."}``. Requiring one known key and
    one non-empty trimmed value prevents broader/mixed source records from being guessed into
    this narrow model.
    """

    if not isinstance(source, Mapping) or len(source) != 1:
        return False
    key, value = next(iter(source.items()))
    return (
        key in _VERSIONLESS_SOURCE_KEYS
        and isinstance(value, str)
        and bool(value)
        and value == value.strip()
    )


# ---------------------------------------------------------------------------
# Base/head semantic comparison
# ---------------------------------------------------------------------------


def _compare_uv_lock_packages(
    base: _ParsedUvLock,
    head: _ParsedUvLock,
    evidence: DependencyChangeSourceEvidence,
) -> DependencyChangeExtractionResult:
    """Compare parsed base/head locks and require exactly one safe textual transition.

    Repeated groups are compared only as complete canonical multisets; this function never
    invents positional branch pairing. The result remains file-level evidence for analysis.py.
    """

    # Use both name sets so additions/removals remain visible; sorting is only deterministic
    # processing order, not stronger evidence.
    all_names = sorted(set(base.groups) | set(head.groups))
    transitions: list[tuple[_UvPackageRecord, _UvPackageRecord]] = []

    for normalized_name in all_names:
        base_group = base.groups.get(normalized_name)
        head_group = head.groups.get(normalized_name)

        # Addition/removal is structural change, not an in-place version transition.
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

        # Repeated records may be distinct universal-lock resolution branches. Multiset
        # comparison ignores ordering but preserves duplicate counts; changed groups remain
        # ambiguous rather than being heuristically paired.
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

    # The shared dependency-change contract represents one package transition; several
    # candidates remain explicit ambiguity rather than choosing a likely package.
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

    # Only ordinary textual-version pairs are appended as transitions; these assertions expose
    # that invariant to type narrowing rather than adding a new evidence check.
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
    """Classify one unique base/head record pair for the same normalized package.

    Returns ``(base, head)`` for a clean textual version transition, ``None`` for no relevant
    transition, or ``DependencyChangeProblem`` when the records cannot be safely paired.
    """

    # ``source`` and ``resolution-markers`` identify the semantic branch being compared. If
    # either changes, version strings alone cannot safely establish base/head correspondence.
    if (
        base.record_data.get("source", _MISSING)
        != head.record_data.get("source", _MISSING)
        or base.record_data.get("resolution-markers", _MISSING)
        != head.record_data.get("resolution-markers", _MISSING)
    ):
        return _problem(
            "unsupported_uv_lock_structural_change",
            (
                f"The source or resolution-marker context for normalized package "
                f"{base.normalized_package!r} changed across base and head."
            ),
            evidence,
        )

    # ``version=None`` means an admitted editable/virtual local-source record, not an unknown
    # package version, so gaining/losing a version or changing structure is not a normal bump.
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
        if _canonical_record(base.record_data) != _canonical_record(head.record_data):
            return _problem(
                "unsupported_uv_lock_structural_change",
                (
                    f"Versionless workspace package {base.normalized_package!r} "
                    "changed non-artifact structure."
                ),
                evidence,
            )
        return None

    if base.version != head.version:
        return (base, head)

    # Same version does not make other meaningful structural changes irrelevant.
    if _canonical_record(base.record_data) != _canonical_record(head.record_data):
        return _problem(
            "unsupported_uv_lock_structural_change",
            (
                f"Normalized package {base.normalized_package!r} kept version "
                f"{base.version!r} but changed non-artifact structure."
            ),
            evidence,
        )
    return None


# ---------------------------------------------------------------------------
# Canonicalization for structural comparison
# ---------------------------------------------------------------------------


def _canonical_group(records: tuple[_UvPackageRecord, ...]) -> Counter[object]:
    """Return an order-independent multiset of meaningful repeated-record structure.

    Order is discarded because list position is not branch identity; duplicate counts remain
    significant, so ``Counter`` is used instead of a set.
    """

    return Counter(_canonical_record(record.record_data) for record in records)


def _canonical_record(record: Mapping[str, Any]) -> object:
    """Return structural identity while excluding artifact-download churn.

    Only ``sdist``/``wheels`` are ignored; other source/dependency/marker structure remains
    visible to equality checks.
    """

    return _freeze_toml_value(
        {key: value for key, value in record.items() if key not in _ARTIFACT_FIELDS}
    )


def _freeze_toml_value(value: object) -> object:
    """Freeze nested TOML data into a deterministic hashable comparison key.

    Mapping key order is ignored, list order is preserved, and scalar type/value identity is
    retained. The result exists only for internal equality/hashing; it is not domain evidence.
    """

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


# ---------------------------------------------------------------------------
# Problem construction and export surface
# ---------------------------------------------------------------------------


def _problem(
    reason: DependencyChangeProblemCode,
    detail: str,
    evidence: DependencyChangeSourceEvidence,
) -> DependencyChangeProblem:
    """Attach already-validated exact source provenance to one stopping result."""

    return DependencyChangeProblem(
        reason=reason,
        detail=detail,
        source_evidence=(evidence,),
    )


# Current public surface: semantic entry first, auxiliary admission gate second.
__all__ = (
    "extract_uv_lock_changes",
    "is_modified_uv_lock_file",
)