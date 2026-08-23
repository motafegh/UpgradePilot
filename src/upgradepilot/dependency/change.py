"""Define source-independent dependency-change evidence and PR-wide comparison.

Each source-specific extractor owns interpretation of one admitted dependency source and
returns either a file-level ``ExtractedDependencyVersionChange`` or a typed
``DependencyChangeProblem``. This module is the consensus boundary: it promotes those
results to one PR-wide ``DependencyVersionChange`` only when every admitted source is
non-problematic and all extracted results agree on normalized package identity and exact
old/proposed versions.

An admitted source problem is therefore blocking evidence, not something to ignore beside
a convenient successful extraction. This module owns no source-specific parsing, network
acquisition, CI interpretation, target-Python logic, compatibility claim, or maintainer
recommendation.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal


type DependencyFileFormat = Literal[
    "exact_requirement",
    "uv_lock",
    "pyproject_optional_extra",
]
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
    "unsupported_pyproject_optional_dependency_change",
    "ambiguous_pyproject_dependency_records",
    "version_unchanged",
    "multiple_dependency_version_changes",
    "conflicting_dependency_version_changes",
]

# Runtime form of the closed problem vocabulary. ``DependencyChangeProblemCode`` gives
# static type checking; this tuple lets tests/callers inspect the supported states as data.
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
    "unsupported_pyproject_optional_dependency_change",
    "ambiguous_pyproject_dependency_records",
    "version_unchanged",
    "multiple_dependency_version_changes",
    "conflicting_dependency_version_changes",
)


@dataclass(frozen=True, slots=True)
class DependencyChangeSourceEvidence:
    """Source provenance for one admitted dependency transition.

    This record explains **where** the package/version fact came from and **how** it was
    extracted. Exact-file extraction retains the base/head immutable revisions because
    later evidence may need to join another source to the same historical side. Provider
    transport metadata such as blob identifiers and byte counts is intentionally absent:
    those values do not establish a separate dependency-domain fact.

    Patch-derived evidence legitimately has no base/head exact-file revisions. This record
    does not establish dependency role, environment membership, installation, CI
    consumption, compatibility, safety, or action.
    """

    path: str
    file_format: DependencyFileFormat
    extraction_method: DependencyEvidenceMethod
    base_revision: str | None = None
    head_revision: str | None = None


# Compatibility surface retained while older callers finish migrating. New code should use
# the owning source-evidence name rather than extending this alias.
DependencyFileEvidence = DependencyChangeSourceEvidence


@dataclass(frozen=True, slots=True)
class ExtractedDependencyVersionChange:
    """One exact file-level transition proposed by a source-specific extractor.

    This is not yet PR-wide truth: another admitted source may disagree or may expose a
    problem that prevents the PR from supporting one trustworthy dependency transition.
    """

    package: str
    normalized_package: str
    old_version: str
    proposed_version: str
    source_evidence: DependencyChangeSourceEvidence


@dataclass(frozen=True, slots=True)
class DependencyVersionChange:
    """One exact package transition trusted across all admitted PR evidence.

    Promotion to this type means every admitted extraction result was non-problematic and
    all extracted sources agreed on normalized package identity and exact version
    transition. ``source_evidence`` preserves the unique agreeing provenance records.

    ``package`` preserves a source spelling for presentation; ``normalized_package`` is the
    cross-source identity used to establish agreement.
    """

    package: str
    normalized_package: str
    old_version: str
    proposed_version: str
    source_evidence: tuple[DependencyChangeSourceEvidence, ...]
    limitations: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class DependencyChangeProblem:
    """Normal abstention result when evidence cannot support one trusted change.

    Problems are evidence states rather than exceptional control flow. During PR-wide
    comparison, the selected problem keeps its reason/detail while source provenance from
    all admitted results is retained where available.
    """

    reason: DependencyChangeProblemCode
    detail: str
    source_evidence: tuple[DependencyChangeSourceEvidence, ...] = ()


# Compatibility alias retained for older imports; new code should use DependencyChangeProblem.
DependencyChangeEvidenceProblem = DependencyChangeProblem

type DependencyChangeExtractionResult = ExtractedDependencyVersionChange | DependencyChangeProblem
type DependencyChangeComparisonResult = DependencyVersionChange | DependencyChangeProblem


def compare_extracted_dependency_changes(
    results: Sequence[DependencyChangeExtractionResult],
) -> DependencyChangeComparisonResult:
    """Establish at most one PR-wide dependency transition from all admitted sources.

    Comparison is intentionally conservative:

    1. preserve unique provenance from every supplied result;
    2. stop on the first admitted problem rather than discarding contradictory/unsafe
       evidence;
    3. require at least one extracted transition;
    4. require one normalized package identity;
    5. require one exact old/proposed version pair;
    6. only then promote the evidence to ``DependencyVersionChange``.

    The first problem supplies the diagnostic reason/detail because result order is already
    caller-owned; provenance from all results is still retained for diagnosis.
    """

    combined_source_evidence = _collect_unique_source_evidence(results)

    # A valid extraction cannot cancel malformed, unavailable, or otherwise unsupported
    # evidence from another admitted dependency source. Ignoring that problem would turn
    # incomplete/contradictory PR evidence into an unjustifiably strong trusted change.
    blocking_problem = next(
        (result for result in results if isinstance(result, DependencyChangeProblem)),
        None,
    )
    if blocking_problem is not None:
        return DependencyChangeProblem(
            reason=blocking_problem.reason,
            detail=blocking_problem.detail,
            source_evidence=combined_source_evidence,
        )

    extracted_changes = tuple(
        result for result in results if isinstance(result, ExtractedDependencyVersionChange)
    )
    if not extracted_changes:
        return DependencyChangeProblem(
            reason="no_supported_dependency_file",
            detail=(
                "No extracted dependency version change or recognized dependency-file "
                "problem was available for PR-wide comparison."
            ),
        )

    normalized_packages = {result.normalized_package for result in extracted_changes}
    if len(normalized_packages) != 1:
        return DependencyChangeProblem(
            reason="multiple_dependency_version_changes",
            detail=(
                "The admitted dependency evidence established changes for several "
                "normalized packages: "
                + ", ".join(sorted(normalized_packages))
                + "."
            ),
            source_evidence=combined_source_evidence,
        )

    exact_transitions = {
        (result.old_version, result.proposed_version) for result in extracted_changes
    }
    if len(exact_transitions) != 1:
        rendered = ", ".join(
            f"{old_version!r} -> {proposed_version!r}"
            for old_version, proposed_version in sorted(exact_transitions)
        )
        return DependencyChangeProblem(
            reason="conflicting_dependency_version_changes",
            detail=(
                "The admitted dependency evidence established conflicting exact "
                f"version transitions for {extracted_changes[0].normalized_package!r}: "
                f"{rendered}."
            ),
            source_evidence=combined_source_evidence,
        )

    # Agreement is established using normalized identity and exact version strings. Raw
    # package spelling may differ legitimately across sources, so preserve the first
    # agreeing source spelling only as the representative presentation form.
    representative_change = extracted_changes[0]
    return DependencyVersionChange(
        package=representative_change.package,
        normalized_package=representative_change.normalized_package,
        old_version=representative_change.old_version,
        proposed_version=representative_change.proposed_version,
        source_evidence=combined_source_evidence,
    )


def _collect_unique_source_evidence(
    results: Sequence[DependencyChangeExtractionResult],
) -> tuple[DependencyChangeSourceEvidence, ...]:
    """Preserve unique provenance without treating duplicate records as stronger proof.

    Source records explain where evidence came from; repeating an identical provenance
    record does not add another independent fact. Caller order is preserved so diagnostics
    and presentation remain deterministic.
    """

    collected: list[DependencyChangeSourceEvidence] = []
    for result in results:
        candidates = (
            (result.source_evidence,)
            if isinstance(result, ExtractedDependencyVersionChange)
            else result.source_evidence
        )
        for evidence in candidates:
            if evidence not in collected:
                collected.append(evidence)
    return tuple(collected)
