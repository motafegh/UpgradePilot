"""Define shared dependency-change records and preserve the legacy entry point.

Source-specific parsing lives in focused modules. Step 2 moves exact
requirements/constraints interpretation into ``exact_requirement_change.py`` while
this module remains the shared contract and comparison boundary accepted by ADR-0004.

Current runtime callers still use ``extract_pinned_dependency_change`` and the legacy
``PinnedDependencyChange`` union. The compatibility function delegates lazily to the
new module so CLI and CI behavior remain unchanged until a later tested migration.
"""

from __future__ import annotations

import re
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

from .github_client import ChangedFile

# Python distribution names may use hyphens, underscores, or periods interchangeably
# for comparison. A compiled pattern collapses any consecutive run of those separators.
_NORMALIZED_PACKAGE_SEPARATOR = re.compile(r"[-_.]+")

# ``Literal`` limits public string vocabularies to the exact values admitted by the
# accepted design. The runtime tuple provides an inspectable immutable vocabulary.
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

    ``path`` preserves the complete repository-relative path. ``file_format`` names the
    admitted syntax family, while ``extraction_method`` states whether the result came
    from complete changed-file patch evidence or complete exact base/head files.

    Optional revision, blob, and byte-count fields support later structured-file
    acquisition. This record does not prove dependency role, installation, CI
    consumption, compatibility, safety, or maintainer action.
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
    """One exact package version change trusted across all admitted PR evidence.

    Several files may independently establish the same transition, so supporting
    evidence and explicit limitations are immutable tuples.
    """

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


# Each source-specific extractor returns one file-level possible change or a problem.
# A later comparison stage returns one trusted PR-wide change or a problem.
type DependencyChangeExtractionResult = (
    ExtractedDependencyVersionChange | DependencyChangeEvidenceProblem
)
type DependencyChangeComparisonResult = (
    DependencyVersionChange | DependencyChangeEvidenceProblem
)


@dataclass(frozen=True, slots=True)
class PinnedDependencyChange:
    """Legacy exact-pin result still consumed by the current CLI and CI rule.

    ``source_file`` combines the file where the transition was observed with the
    requirements file expected by the existing direct-install CI rule. Later migration
    steps will replace this coupling only after shared comparison behavior is proven.
    """

    source_file: str
    package: str
    normalized_package: str
    old_version: str
    proposed_version: str


@dataclass(frozen=True, slots=True)
class UnsupportedDependencyChange:
    """Legacy normal abstention result for the current narrow runtime path."""

    reason: str
    detail: str


type DependencyChangeResult = PinnedDependencyChange | UnsupportedDependencyChange


def extract_pinned_dependency_change(
    changed_files: Sequence[ChangedFile],
) -> DependencyChangeResult:
    """Preserve the validated legacy multi-file exact-pin API.

    The implementation moved to ``exact_requirement_change.py`` in Step 2. The local
    import avoids a module-initialization cycle because that focused module imports the
    shared records defined above.
    """

    from .exact_requirement_change import _extract_legacy_pinned_dependency_change

    return _extract_legacy_pinned_dependency_change(changed_files)


def normalize_package_name(package: str) -> str:
    """Return the PEP 503 comparison form of a distribution name.

    Consecutive hyphens, underscores, and periods collapse to one hyphen, then the
    string is lowercased. This provides identity comparison only; it does not contact a
    package index, validate that the distribution exists, or resolve aliases/versions.
    """

    return _NORMALIZED_PACKAGE_SEPARATOR.sub("-", package).lower()
