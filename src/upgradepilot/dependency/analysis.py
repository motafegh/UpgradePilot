"""Coordinate PR-wide dependency evidence across admitted source formats.

This is the integration boundary between complete GitHub changed-file records and the
format-independent ``DependencyVersionChange`` consumed downstream. Source discovery,
source-specific extraction, and PR-wide comparison remain explicit so unsupported or
ambiguous evidence stops rather than being guessed.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

from ..github_client import ChangedFile, PullRequestIdentity
from ..github_repository import GitHubRepositoryClient
from ..repository_path import repository_relative_parts
from ..uv_lock_change import extract_uv_lock_changes, is_modified_uv_lock_file
from .change import (
    DependencyChangeExtractionResult,
    DependencyChangeProblem,
    DependencyVersionChange,
    ExtractedDependencyVersionChange,
    compare_extracted_dependency_changes,
)
from .requirements import (
    extract_exact_requirement_changes,
    is_admitted_requirements_file,
    is_exact_requirement_file,
)


@dataclass(frozen=True, slots=True)
class DependencyChangeAnalysis:
    """Trusted dependency identity plus optional current-rule CI input."""

    dependency: DependencyVersionChange
    direct_requirements_install_path: str | None


type DependencyChangeAnalysisResult = DependencyChangeAnalysis | DependencyChangeProblem


def is_uv_lock_file(changed_file: ChangedFile) -> bool:
    """Return whether a changed-file path names exact lowercase ``uv.lock``."""

    parts = repository_relative_parts(changed_file.filename)
    return parts is not None and parts[-1] == "uv.lock"


def analyze_dependency_change(
    identity: PullRequestIdentity,
    changed_files: Sequence[ChangedFile],
    repository_client: GitHubRepositoryClient,
) -> DependencyChangeAnalysisResult:
    """Establish at most one trusted dependency transition across the whole PR."""

    extraction_results: list[DependencyChangeExtractionResult] = []
    direct_requirements_candidates: list[str] = []

    for changed_file in changed_files:
        if is_exact_requirement_file(changed_file.filename):
            result = extract_exact_requirement_changes(changed_file)
            extraction_results.append(result)
            if (
                isinstance(result, ExtractedDependencyVersionChange)
                and is_admitted_requirements_file(changed_file.filename)
            ):
                direct_requirements_candidates.append(changed_file.filename)
            continue

        if not is_uv_lock_file(changed_file):
            continue

        if not is_modified_uv_lock_file(changed_file):
            extraction_results.append(
                DependencyChangeProblem(
                    reason="unsupported_dependency_file_status",
                    detail=(
                        f"The uv.lock file status was {changed_file.status!r}; the "
                        "first structured-lockfile rule supports only an in-place "
                        "modified file."
                    ),
                )
            )
            continue

        base_file = repository_client.get_pull_request_base_file(
            identity,
            changed_file.filename,
        )
        head_file = repository_client.get_pull_request_head_file(
            identity,
            changed_file.filename,
        )
        extraction_results.append(
            extract_uv_lock_changes(changed_file, base_file, head_file)
        )

    comparison = compare_extracted_dependency_changes(extraction_results)
    if isinstance(comparison, DependencyChangeProblem):
        return comparison

    distinct_requirements_paths = tuple(dict.fromkeys(direct_requirements_candidates))
    direct_requirements_install_path = (
        distinct_requirements_paths[0]
        if len(distinct_requirements_paths) == 1
        else None
    )

    return DependencyChangeAnalysis(
        dependency=comparison,
        direct_requirements_install_path=direct_requirements_install_path,
    )


__all__ = (
    "DependencyChangeAnalysis",
    "DependencyChangeAnalysisResult",
    "analyze_dependency_change",
    "is_uv_lock_file",
)
