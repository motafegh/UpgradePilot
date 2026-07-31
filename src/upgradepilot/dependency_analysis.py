"""Coordinate PR-wide dependency evidence across admitted source formats.

This module is the single integration boundary between complete GitHub changed-file
records and the canonical ``DependencyVersionChange`` consumed downstream. It performs
source discovery, invokes source-specific acquisition and extraction, preserves every
recognized problem, and delegates trust comparison to
``compare_extracted_dependency_changes``.

The coordinator is intentionally static and visible. Adding another source format with
the same canonical meaning should add one explicit branch here plus focused tests; it
must not spread format conditions through the CLI or downstream evidence stages.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

from .dependency_change import (
    DependencyChangeEvidenceProblem,
    DependencyChangeExtractionResult,
    DependencyVersionChange,
    ExtractedDependencyVersionChange,
    compare_extracted_dependency_changes,
)
from .exact_requirement_change import (
    extract_exact_requirement_changes,
    is_admitted_requirements_file,
    is_exact_requirement_file,
)
from .github_client import ChangedFile, PullRequestIdentity
from .github_repository import GitHubRepositoryClient
from .uv_lock_change import extract_uv_lock_changes, is_modified_uv_lock_file


@dataclass(frozen=True, slots=True)
class DependencyChangeAnalysis:
    """Trusted dependency identity plus optional current-rule CI input.

    ``dependency`` is format-independent package/version evidence.

    ``direct_requirements_install_path`` is separate operational input for the current
    direct ``pip -r`` CI rule. ``None`` means the PR-wide evidence did not establish
    exactly one admitted requirements-family path that may be checked by that rule.
    Constraints and ``uv.lock`` never populate this field.
    """

    dependency: DependencyVersionChange
    direct_requirements_install_path: str | None


type DependencyChangeAnalysisResult = (
    DependencyChangeAnalysis | DependencyChangeEvidenceProblem
)


def is_uv_lock_file(changed_file: ChangedFile) -> bool:
    """Return whether a changed-file path names exact lowercase ``uv.lock``.

    This is path recognition only. Status admission remains separate so added,
    deleted, and renamed lockfiles are recognized as explicit unsupported-status
    problems rather than silently ignored.
    """

    parts = _relative_path_parts(changed_file.filename)
    return parts is not None and parts[-1] == "uv.lock"


def analyze_dependency_change(
    identity: PullRequestIdentity,
    changed_files: Sequence[ChangedFile],
    repository_client: GitHubRepositoryClient,
) -> DependencyChangeAnalysisResult:
    """Establish at most one trusted dependency transition across the whole PR.

    Every admitted source result and every recognized source problem reaches the shared
    comparator. Arbitrary files are ignored. Exact repository-file acquisition occurs
    only for recognized modified ``uv.lock`` records.
    """

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
                DependencyChangeEvidenceProblem(
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
            extract_uv_lock_changes(
                changed_file,
                base_file,
                head_file,
            )
        )

    comparison = compare_extracted_dependency_changes(extraction_results)
    if isinstance(comparison, DependencyChangeEvidenceProblem):
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


def _relative_path_parts(path: str) -> tuple[str, ...] | None:
    """Return validated POSIX repository-relative components or ``None``."""

    if not path or path.startswith("/") or "\\" in path:
        return None

    parts = tuple(path.split("/"))
    if any(not part or part in {".", ".."} for part in parts):
        return None
    return parts
