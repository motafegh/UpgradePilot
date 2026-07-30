"""Define shared dependency-change records and preserve the legacy runtime entry point.

Purpose of this file
--------------------
Source-specific parsing belongs in focused modules. Step 2 moves conventional exact
requirements and constraints interpretation into ``exact_requirement_change.py`` while
this module remains the format-independent contract boundary accepted by ADR-0004.

The shared records separate:

* evidence from one dependency file;
* one possible version change extracted from that file;
* one version change trusted after all admitted PR evidence is compared;
* an explicit evidence problem that prevents a trusted result.

Current compatibility flow:
    ``cli.py`` still calls ``extract_pinned_dependency_change`` and narrows its legacy
    ``PinnedDependencyChange | UnsupportedDependencyChange`` result. That function now
    delegates to the focused exact-requirement module without changing the caller API.

Future shared flow:
    A source-specific extractor produces ``ExtractedDependencyVersionChange`` or
    ``DependencyChangeEvidenceProblem``. A later comparison step examines all extracted
    results and produces one ``DependencyVersionChange`` or an explicit problem.

Why the distinction matters:
    One file may contain a plausible version change while another admitted dependency
    file is malformed, unavailable, conflicting, or contains another change. An
    extracted result is therefore not yet trusted across the complete pull request.
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
# accepted design. These aliases communicate intent to type-aware readers and tools;
# the runtime tuple below provides one inspectable immutable vocabulary for tests and
# presentation code.
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

# Keep the runtime vocabulary immutable and ordered. Later parsers select from these
# meanings instead of inventing near-duplicate reason strings in separate modules.
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

    ``path`` preserves the complete repository-relative file path. ``file_format``
    names the admitted syntax family, while ``extraction_method`` states whether the
    result came from complete changed-file patch evidence or complete exact base/head
    files.

    Revision, blob, and byte-count fields are optional because patch-based extraction
    does not yet have complete blob-level identity. Structured base/head comparison will
    populate those fields when exact repository files are acquired in a later step.

    This record identifies where evidence came from. It does not prove dependency role,
    installation, CI consumption, compatibility, safety, or a maintainer action.
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
    """One possible exact version change extracted from one dependency file.

    The record is intentionally not the final trusted PR-wide result. Another admitted
    dependency file may agree, conflict, contain another transition, or fail in a way
    that prevents the pull request from producing one trustworthy dependency identity.
    """

    package: str
    normalized_package: str
    old_version: str
    proposed_version: str
    source_evidence: DependencyFileEvidence


@dataclass(frozen=True, slots=True)
class DependencyVersionChange:
    """One exact package version change trusted across all admitted PR evidence.

    ``source_evidence`` is a tuple because several files may independently establish
    the same normalized package and exact raw old/proposed version strings. A tuple is
    immutable and preserves every supporting source without implying that all sources
    have the same dependency role or CI meaning.

    ``limitations`` carries explicit boundaries that downstream presentation may need
    to preserve. It is also a tuple so the trusted question cannot be mutated after
    comparison.
    """

    package: str
    normalized_package: str
    old_version: str
    proposed_version: str
    source_evidence: tuple[DependencyFileEvidence, ...]
    limitations: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class DependencyChangeEvidenceProblem:
    """Normal stopping result when dependency evidence cannot support one trusted change.

    ``reason`` is selected from the accepted machine-readable vocabulary. ``detail`` is
    the human explanation. ``source_evidence`` preserves any dependency files already
    identified before the stopping condition was established.

    A problem does not automatically mean malformed, incompatible, or unsafe. Different
    reasons preserve the exact distinction: unsupported form, missing evidence,
    ambiguity, several changes, conflict, or another bounded failure.
    """

    reason: DependencyChangeProblemCode
    detail: str
    source_evidence: tuple[DependencyFileEvidence, ...] = ()


# These aliases make each future stage's union explicit. An extractor can return one
# file-level possible change or a problem; the comparison stage can return one trusted
# PR-wide change or a problem. Callers must narrow the union before reading change-only
# fields.
type DependencyChangeExtractionResult = (
    ExtractedDependencyVersionChange | DependencyChangeEvidenceProblem
)
type DependencyChangeComparisonResult = (
    DependencyVersionChange | DependencyChangeEvidenceProblem
)


@dataclass(frozen=True, slots=True)
class PinnedDependencyChange:
    """One proven exact-pin update safe for the current evidence stages to consume.

    ``source_file`` identifies the requirements file CI must install. ``package`` keeps
    the added spelling for readable output, while ``normalized_package`` preserves the
    comparison identity used by command matching. The two version fields make the
    observed transition explicit.

    This is the current implemented contract. Its ``source_file`` field combines change
    evidence with one direct-requirements CI assumption, so later steps will migrate it
    only after the broader records and comparison behavior are proven.
    """

    source_file: str
    package: str
    normalized_package: str
    old_version: str
    proposed_version: str


@dataclass(frozen=True, slots=True)
class UnsupportedDependencyChange:
    """Normal abstention when valid evidence lies outside the current legacy rule.

    Unsupported does not automatically mean malformed or unsafe. It means the current
    narrow extractor could not prove one exact supported change. ``reason`` is stable
    for program logic; ``detail`` explains the stopping point to the user.
    """

    reason: str
    detail: str


# Making abstention part of the return type forces ``cli.py`` to narrow the union with
# ``isinstance`` before accessing package/version fields.
type DependencyChangeResult = PinnedDependencyChange | UnsupportedDependencyChange


def extract_pinned_dependency_change(
    changed_files: Sequence[ChangedFile],
) -> DependencyChangeResult:
    """Preserve the validated legacy multi-file exact-pin API.

    The parser implementation moved to ``exact_requirement_change.py`` in Step 2. The
    local import avoids a module-initialization cycle because that focused module imports
    the shared records defined above. Existing CLI, CI, tests, and package-level imports
    therefore keep their current contract while the new file-level API is introduced.
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
