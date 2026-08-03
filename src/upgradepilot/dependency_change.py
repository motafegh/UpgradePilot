"""Define shared dependency-change records and comparison behavior.

Source-specific parsers produce file-level results. The shared comparison contract then
establishes at most one PR-wide ``DependencyVersionChange``. The active command path
uses ``dependency_analysis.py`` to coordinate those parsers.

The older exact-requirements records and extraction function remain available for
historical package-level compatibility, but no active downstream runtime stage consumes
``PinnedDependencyChange`` or its combined ``source_file`` meaning.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

from .github_client import ChangedFile
from .package_identity import normalize_package_name


type DependencyFileFormat = Literal["exact_requirement", "uv_lock"]
type DependencyEvidenceMethod = Literal[
    "changed_file_patch",
    "exact_base_head_files",
]
type DependencyChangeProblemCode = Literal[
    "no_supported_dependency_file",
    "missing_dependency_patch",
    "incomplete_dependency_patch",
    "unsupported_requirement_format",
    "unsupported_dependency_file_status",
    "dependency_file_unavailable",
    "dependency_file_too_large",
    "malformed_dependency_file",
    "invalid_dependency_record",
    "unsupported_uv_lock_schema",
    "unsupported_uv_lock_structural_change",
    "ambiguous_uv_lock_package_records",
    "version_unchanged",
    "multiple_dependency_version_changes",
    "conflicting_dependency_version_changes",
]

DEPENDENCY_CHANGE_PROBLEM_CODES: tuple[DependencyChangeProblemCode, ...] = (
    "no_supported_dependency_file",
    "missing_dependency_patch",
    "incomplete_dependency_patch",
    "unsupported_requirement_format",
    "unsupported_dependency_file_status",
    "dependency_file_unavailable",
    "dependency_file_too_large",
    "malformed_dependency_file",
    "invalid_dependency_record",
    "unsupported_uv_lock_schema",
    "unsupported_uv_lock_structural_change",
    "ambiguous_uv_lock_package_records",
    "version_unchanged",
    "multiple_dependency_version_changes",
    "conflicting_dependency_version_changes",
)


@dataclass(frozen=True, slots=True)
class DependencyFileEvidence:
    """Identity of one admitted dependency file and its extraction method.

    The path and format identify where dependency evidence came from. They do not prove
    dependency role, installation, CI consumption, compatibility, safety, or a
    maintainer action.
    """

    path: str
    file_format: DependencyFileFormat
    extraction_method: DependencyEvidenceMethod
    base_revision: str | None = None
    base_blob_sha: str | None = None
    base_byte_count: int | None = None
    head_revision: str | None = None
    head_blob_sha: str | None = None
    head_byte_count: int | None = None


@dataclass(frozen=True, slots=True)
class ExtractedDependencyVersionChange:
    """One possible exact version change extracted from one dependency file."""

    package: str
    normalized_package: str
    old_version: str
    proposed_version: str
    source_evidence: DependencyFileEvidence


@dataclass(frozen=True, slots=True)
class DependencyVersionChange:
    """One exact package version change trusted across admitted PR evidence."""

    package: str
    normalized_package: str
    old_version: str
    proposed_version: str
    source_evidence: tuple[DependencyFileEvidence, ...]
    limitations: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class DependencyChangeEvidenceProblem:
    """Normal stopping result when evidence cannot support one trusted change."""

    reason: DependencyChangeProblemCode
    detail: str
    source_evidence: tuple[DependencyFileEvidence, ...] = ()


type DependencyChangeExtractionResult = (
    ExtractedDependencyVersionChange | DependencyChangeEvidenceProblem
)
type DependencyChangeComparisonResult = (
    DependencyVersionChange | DependencyChangeEvidenceProblem
)


def compare_extracted_dependency_changes(
    results: Sequence[DependencyChangeExtractionResult],
) -> DependencyChangeComparisonResult:
    """Compare all source-specific results and establish at most one PR-wide change."""

    source_evidence = _collect_unique_source_evidence(results)

    first_problem = next(
        (
            result
            for result in results
            if isinstance(result, DependencyChangeEvidenceProblem)
        ),
        None,
    )
    if first_problem is not None:
        return DependencyChangeEvidenceProblem(
            reason=first_problem.reason,
            detail=first_problem.detail,
            source_evidence=source_evidence,
        )

    extracted = tuple(
        result
        for result in results
        if isinstance(result, ExtractedDependencyVersionChange)
    )
    if not extracted:
        return DependencyChangeEvidenceProblem(
            reason="no_supported_dependency_file",
            detail=(
                "No extracted dependency version change or recognized dependency-file "
                "problem was available for PR-wide comparison."
            ),
        )

    normalized_packages = {result.normalized_package for result in extracted}
    if len(normalized_packages) != 1:
        return DependencyChangeEvidenceProblem(
            reason="multiple_dependency_version_changes",
            detail=(
                "The admitted dependency evidence established changes for several "
                "normalized packages: "
                + ", ".join(sorted(normalized_packages))
                + "."
            ),
            source_evidence=source_evidence,
        )

    transitions = {
        (result.old_version, result.proposed_version) for result in extracted
    }
    if len(transitions) != 1:
        rendered = ", ".join(
            f"{old_version!r} -> {proposed_version!r}"
            for old_version, proposed_version in sorted(transitions)
        )
        return DependencyChangeEvidenceProblem(
            reason="conflicting_dependency_version_changes",
            detail=(
                "The admitted dependency evidence established conflicting exact "
                f"version transitions for {extracted[0].normalized_package!r}: "
                f"{rendered}."
            ),
            source_evidence=source_evidence,
        )

    representative = extracted[0]
    return DependencyVersionChange(
        package=representative.package,
        normalized_package=representative.normalized_package,
        old_version=representative.old_version,
        proposed_version=representative.proposed_version,
        source_evidence=source_evidence,
    )


def _collect_unique_source_evidence(
    results: Sequence[DependencyChangeExtractionResult],
) -> tuple[DependencyFileEvidence, ...]:
    """Collect source records once while preserving caller-provided order."""

    collected: list[DependencyFileEvidence] = []
    for result in results:
        if isinstance(result, ExtractedDependencyVersionChange):
            candidates = (result.source_evidence,)
        else:
            candidates = result.source_evidence

        for evidence in candidates:
            if evidence not in collected:
                collected.append(evidence)

    return tuple(collected)


@dataclass(frozen=True, slots=True)
class PinnedDependencyChange:
    """Legacy exact-requirements result retained for historical API compatibility.

    ``source_file`` combines dependency evidence with the old direct-requirements CI
    assumption. Active command and downstream code use ``DependencyVersionChange`` and
    separately supplied CI input instead.
    """

    source_file: str
    package: str
    normalized_package: str
    old_version: str
    proposed_version: str


@dataclass(frozen=True, slots=True)
class UnsupportedDependencyChange:
    """Normal abstention returned by the validated legacy extractor."""

    reason: str
    detail: str


type DependencyChangeResult = PinnedDependencyChange | UnsupportedDependencyChange


def extract_pinned_dependency_change(
    changed_files: Sequence[ChangedFile],
) -> DependencyChangeResult:
    """Preserve the validated legacy multi-file exact-pin API."""

    from .exact_requirement_change import _extract_legacy_pinned_dependency_change

    return _extract_legacy_pinned_dependency_change(changed_files)
