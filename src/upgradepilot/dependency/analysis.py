"""Coordinate PR-wide dependency evidence across admitted source formats.

This is the integration boundary between complete GitHub changed-file records and the
format-independent ``DependencyVersionChange`` consumed downstream. Source discovery,
source-specific extraction, and PR-wide comparison remain explicit so unsupported or
ambiguous evidence stops rather than being guessed.

The analysis result also preserves dependency-owned source context for later environment
selection/consumption reasoning. That context is still source evidence: it does not claim
that a workflow selected, executed, or successfully formed an environment.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

from ..github.pull_request import ChangedFile, PullRequestIdentity
from ..github.repository import GitHubRepositoryClient
from ..repository_path import repository_relative_parts
from .change import (
    DependencyChangeExtractionResult,
    DependencyChangeProblem,
    DependencyChangeSourceEvidence,
    DependencyVersionChange,
    ExtractedDependencyVersionChange,
    compare_extracted_dependency_changes,
)
from .environment import (
    ConstraintsFileDependencyContext,
    DependencySourceContext,
    PyprojectOptionalExtraDependencyContext,
    RequirementsFileDependencyContext,
    UvLockDependencyContext,
)
from .pyproject import (
    ExtractedPyprojectOptionalExtraChange,
    extract_pyproject_optional_extra_change,
    is_modified_pyproject_file,
)
from .requirements import (
    extract_exact_requirement_changes,
    is_admitted_requirements_file,
    is_exact_requirement_file,
)
from .uv_lock import extract_uv_lock_changes, is_modified_uv_lock_file


@dataclass(frozen=True, slots=True)
class DependencyChangeAnalysis:
    """Trusted dependency identity plus dependency-owned exact source contexts.

    ``source_contexts`` is the source of truth for downstream dependency-environment
    reasoning. ``direct_requirements_install_path`` remains only as a derived compatibility
    projection until CI is migrated in a later cluster; it deliberately cannot represent
    uv, constraints, or pyproject environment semantics.
    """

    dependency: DependencyVersionChange
    source_contexts: tuple[DependencySourceContext, ...]

    @property
    def direct_requirements_install_path(self) -> str | None:
        """Project the one old-style direct requirements path when unambiguous."""

        requirements_paths = tuple(
            context.source_path
            for context in self.source_contexts
            if isinstance(context, RequirementsFileDependencyContext)
        )
        return requirements_paths[0] if len(requirements_paths) == 1 else None


type DependencyChangeAnalysisResult = DependencyChangeAnalysis | DependencyChangeProblem


def is_uv_lock_file(changed_file: ChangedFile) -> bool:
    """Return whether a changed-file path names exact lowercase ``uv.lock``."""

    parts = repository_relative_parts(changed_file.filename)
    return parts is not None and parts[-1] == "uv.lock"


def is_pyproject_file(changed_file: ChangedFile) -> bool:
    """Return whether a changed-file path names exact lowercase ``pyproject.toml``."""

    parts = repository_relative_parts(changed_file.filename)
    return parts is not None and parts[-1] == "pyproject.toml"


def analyze_dependency_change(
    identity: PullRequestIdentity,
    changed_files: Sequence[ChangedFile],
    repository_client: GitHubRepositoryClient,
) -> DependencyChangeAnalysisResult:
    """Establish at most one trusted dependency transition across the whole PR."""

    extraction_results: list[DependencyChangeExtractionResult] = []
    pyproject_optional_extras: dict[DependencyChangeSourceEvidence, str] = {}

    for changed_file in changed_files:
        if is_exact_requirement_file(changed_file.filename):
            extraction_results.append(extract_exact_requirement_changes(changed_file))
            continue

        if is_pyproject_file(changed_file):
            if not is_modified_pyproject_file(changed_file):
                extraction_results.append(
                    DependencyChangeProblem(
                        reason="unsupported_dependency_file_status",
                        detail=(
                            f"The pyproject.toml file status was {changed_file.status!r}; "
                            "the first optional-extra rule supports only an in-place "
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
            pyproject_result = extract_pyproject_optional_extra_change(
                changed_file,
                base_file,
                head_file,
            )
            if isinstance(pyproject_result, ExtractedPyprojectOptionalExtraChange):
                extraction_results.append(pyproject_result.change)
                pyproject_optional_extras[
                    pyproject_result.change.source_evidence
                ] = pyproject_result.extra
            else:
                extraction_results.append(pyproject_result)
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

    return DependencyChangeAnalysis(
        dependency=comparison,
        source_contexts=_source_contexts(
            identity,
            comparison,
            pyproject_optional_extras=pyproject_optional_extras,
        ),
    )


def _source_contexts(
    identity: PullRequestIdentity,
    dependency: DependencyVersionChange,
    *,
    pyproject_optional_extras: dict[DependencyChangeSourceEvidence, str],
) -> tuple[DependencySourceContext, ...]:
    """Translate trusted change provenance into source-scoped dependency contexts.

    Only source facts already established by extraction are translated here. In
    particular, an optional-extra name comes from exact pyproject evidence, not workflow
    text; a uv-lock context does not invent a project group/extra; and a constraints file
    does not become a directly installable requirements environment.
    """

    contexts: list[DependencySourceContext] = []
    for evidence in dependency.source_evidence:
        common = {
            "repository": identity.repository,
            "revision": identity.head_sha,
            "normalized_package": dependency.normalized_package,
            "source_evidence": evidence,
        }

        if evidence.file_format == "uv_lock":
            contexts.append(UvLockDependencyContext(**common))
            continue

        if evidence.file_format == "pyproject_optional_extra":
            extra = pyproject_optional_extras.get(evidence)
            if extra is None:
                raise RuntimeError(
                    "trusted pyproject optional-extra evidence lost its source scope"
                )
            contexts.append(
                PyprojectOptionalExtraDependencyContext(extra=extra, **common)
            )
            continue

        if is_admitted_requirements_file(evidence.path):
            contexts.append(RequirementsFileDependencyContext(**common))
        else:
            contexts.append(ConstraintsFileDependencyContext(**common))

    return tuple(contexts)


__all__ = (
    "DependencyChangeAnalysis",
    "DependencyChangeAnalysisResult",
    "analyze_dependency_change",
    "is_pyproject_file",
    "is_uv_lock_file",
)
