"""Extract one exact dependency-version transition from complete ``uv.lock`` evidence.

RESPONSIBILITY / FLOW
---------------------
``dependency/analysis.py::analyze_dependency_change(...)`` is the normal caller::

    ChangedFile
        -> admit path/status
        -> acquire admitted exact base/head repository files
        -> extract_uv_lock_changes(...)  [SEMANTIC ENTRY]
        -> handle typed exact-file availability
        -> uv_lock_structure.parse_uv_lock_structure(...) for each side
        -> compare admitted package groups conservatively
        -> ExtractedDependencyVersionChange or DependencyChangeProblem
        -> dependency/change.py::compare_extracted_dependency_changes(...)

``dependency/uv_lock_structure.py`` owns the shared structural truth for one exact lock:
schema/revision admission, core package-record identity/name/version/source rules, and repeated
record preservation. This module does not duplicate those rules. It owns only base/head
**transition semantics**: which admitted structural differences can establish one exact package
version transition and which differences require abstention.

``dependency/analysis.py`` owns changed-file role/status admission and exact base/head
acquisition from one PR identity. ``github/repository.py`` owns exact repository text evidence.
This module therefore does not re-prove PR repository/path binding or provider transport
invariants. ``dependency/change.py`` owns source-independent success/problem output types.

PUBLIC API
----------
``extract_uv_lock_changes(...)`` is the source-semantic entry used after admission and
acquisition. ``is_modified_uv_lock_file(...)`` is only the cheap pre-acquisition admission gate.

PROOF BOUNDARY
--------------
Success proves one exact textual package-version transition in the admitted base/head lock
files. It does not prove selected-root reachability, environment membership, CI
installation/exercise, resolver currentness, runtime behavior, or upgrade safety.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Mapping
from typing import Any, Literal

from ..github.pull_request import ChangedFile
from ..github.repository import (
    RepositoryFileEvidence,
    RepositoryTextFile,
    UnavailableRepositoryFile,
)
from ..repository_path import repository_relative_parts
from .change import (
    DependencyChangeExtractionResult,
    DependencyChangeProblem,
    DependencyChangeProblemCode,
    DependencyChangeSourceEvidence,
    ExtractedDependencyVersionChange,
)
from .uv_lock_structure import (
    UvLockPackageRecord,
    UvLockStructure,
    UvLockStructureProblem,
    parse_uv_lock_structure,
)

# Artifact download metadata may churn without changing the package/dependency semantics this
# transition consumer compares, so its canonical comparison ignores only these fields.
_ARTIFACT_FIELDS = frozenset({"sdist", "wheels"})
_MISSING = object()


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def is_modified_uv_lock_file(changed_file: ChangedFile) -> bool:
    """Return whether this changed file is eligible for exact uv.lock acquisition."""

    parts = repository_relative_parts(changed_file.filename)
    return (
        changed_file.status == "modified"
        and parts is not None
        and parts[-1] == "uv.lock"
    )


def extract_uv_lock_changes(
    base_file: RepositoryFileEvidence,
    head_file: RepositoryFileEvidence,
) -> DependencyChangeExtractionResult:
    """Extract one safe file-level version transition from admitted exact files.

    The shared structural parser establishes what each exact lock contains. This function then
    compares those two structures under the narrower dependency-transition contract; successful
    structural parsing does not itself imply that any package changed safely.
    """

    unavailable = _first_unavailable_file(base_file, head_file)
    if unavailable is not None:
        return DependencyChangeProblem(
            reason="dependency_file_unavailable",
            detail=(
                f"Exact uv.lock text was unavailable at revision "
                f"{unavailable.revision!r}: {unavailable.detail}"
            ),
        )

    assert isinstance(base_file, RepositoryTextFile)
    assert isinstance(head_file, RepositoryTextFile)

    evidence = DependencyChangeSourceEvidence(
        path=head_file.path,
        file_format="uv_lock",
        extraction_method="exact_base_head_files",
    )

    base_result = _parse_transition_lock(base_file, evidence, side="base")
    if isinstance(base_result, DependencyChangeProblem):
        return base_result

    head_result = _parse_transition_lock(head_file, evidence, side="head")
    if isinstance(head_result, DependencyChangeProblem):
        return head_result

    return _compare_uv_lock_packages(base_result, head_result, evidence)


# ---------------------------------------------------------------------------
# Exact-file availability and shared-structure adaptation
# ---------------------------------------------------------------------------


def _first_unavailable_file(
    base_file: RepositoryFileEvidence,
    head_file: RepositoryFileEvidence,
) -> UnavailableRepositoryFile | None:
    """Return the first unavailable historical side, otherwise ``None``."""

    if isinstance(base_file, UnavailableRepositoryFile):
        return base_file
    if isinstance(head_file, UnavailableRepositoryFile):
        return head_file
    return None


def _parse_transition_lock(
    repository_file: RepositoryTextFile,
    evidence: DependencyChangeSourceEvidence,
    *,
    side: Literal["base", "head"],
) -> UvLockStructure | DependencyChangeProblem:
    """Adapt one shared structural result into dependency-extraction failure semantics.

    The structural owner intentionally knows nothing about PR base/head roles or dependency
    problem codes. This adapter adds that consumer-specific diagnostic/provenance without
    revalidating the lock structure.
    """

    result = parse_uv_lock_structure(repository_file.content)
    if not isinstance(result, UvLockStructureProblem):
        return result

    if result.code == "malformed_uv_lock":
        reason: DependencyChangeProblemCode = "malformed_dependency_file"
    elif result.code == "unsupported_uv_lock_schema":
        reason = "unsupported_uv_lock_schema"
    else:
        reason = "invalid_dependency_record"

    return _problem(
        reason,
        f"The exact {side} uv.lock could not enter the bounded structural model: {result.detail}",
        evidence,
    )


# ---------------------------------------------------------------------------
# Base/head transition semantics
# ---------------------------------------------------------------------------


def _compare_uv_lock_packages(
    base: UvLockStructure,
    head: UvLockStructure,
    evidence: DependencyChangeSourceEvidence,
) -> DependencyChangeExtractionResult:
    """Compare admitted base/head locks and require exactly one safe textual transition.

    Repeated groups are compared only as complete canonical multisets; this semantic consumer
    never invents positional branch pairing merely because the structural owner preserved order.
    """

    all_names = sorted(set(base.by_name) | set(head.by_name))
    transitions: list[tuple[UvLockPackageRecord, UvLockPackageRecord]] = []

    for normalized_name in all_names:
        base_group = base.by_name.get(normalized_name)
        head_group = head.by_name.get(normalized_name)

        if base_group is None or head_group is None:
            return _problem(
                "unsupported_uv_lock_structural_change",
                (
                    f"Normalized package {normalized_name!r} was added or removed; "
                    "the first uv.lock transition rule supports only version transitions "
                    "for records present at both revisions."
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

        # Repeated records may represent distinct universal-lock resolution branches. A
        # complete order-independent multiset can establish an unchanged repeated group, but a
        # changed group remains ambiguous because list position is not branch identity.
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
    base: UvLockPackageRecord,
    head: UvLockPackageRecord,
    evidence: DependencyChangeSourceEvidence,
) -> tuple[UvLockPackageRecord, UvLockPackageRecord] | DependencyChangeProblem | None:
    """Classify one unique base/head record pair for the same normalized package."""

    # Source and resolution-marker context identify the semantic branch being compared. The
    # structural parser establishes record admission; deciding whether changed context still
    # permits a base/head transition remains this consumer's responsibility.
    if (
        base.source != head.source
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

    # ``version=None`` is no longer an ambiguous parser outcome: the shared owner guarantees it
    # means one admitted editable/virtual local-source record. Transition semantics still refuse
    # to manufacture a normal version bump from a versionless structural change.
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
# Transition-only canonical comparison
# ---------------------------------------------------------------------------


def _canonical_group(records: tuple[UvLockPackageRecord, ...]) -> Counter[object]:
    """Return an order-independent multiset of meaningful repeated-record structure."""

    return Counter(_canonical_record(record.record_data) for record in records)


def _canonical_record(record: Mapping[str, Any]) -> object:
    """Return transition identity while excluding artifact-download churn only."""

    return _freeze_toml_value(
        {key: value for key, value in record.items() if key not in _ARTIFACT_FIELDS}
    )


def _freeze_toml_value(value: object) -> object:
    """Freeze nested TOML data into a deterministic hashable comparison key."""

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
    """Attach source provenance to one transition stopping result."""

    return DependencyChangeProblem(
        reason=reason,
        detail=detail,
        source_evidence=(evidence,),
    )


__all__ = (
    "extract_uv_lock_changes",
    "is_modified_uv_lock_file",
)
