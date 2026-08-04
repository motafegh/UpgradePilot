"""Extract exact package-version changes from admitted requirements files.

This module owns the bounded source-specific rule for conventional requirements and
constraints paths whose complete GitHub patch contains exactly one removed and one
added ``package==version`` line. It produces the modern file-level dependency result
directly; no legacy ``PinnedDependencyChange`` compatibility model participates in
the extraction path.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from ..github.pull_request import ChangedFile
from ..package_identity import normalize_package_name
from ..repository_path import repository_relative_parts
from .change import (
    DependencyChangeExtractionResult,
    DependencyChangeProblem,
    DependencyChangeSourceEvidence,
    ExtractedDependencyVersionChange,
)

_PINNED_REQUIREMENT_PATTERN = re.compile(
    r"^\s*([A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?)"
    r"==([A-Za-z0-9][A-Za-z0-9.!+_-]*)\s*$"
)
_REQUIREMENTS_FILENAME_PATTERN = re.compile(
    r"^requirements(?:[-_.][A-Za-z0-9][A-Za-z0-9._-]*)?\.(?:txt|in)$"
)
_CONSTRAINTS_FILENAME_PATTERN = re.compile(
    r"^constraints(?:[-_.][A-Za-z0-9][A-Za-z0-9._-]*)?\.(?:txt|in)$"
)


@dataclass(frozen=True, slots=True)
class _PinnedRequirementLine:
    source_file: str
    package: str
    version: str


def is_exact_requirement_file(path: str) -> bool:
    """Return whether a normalized path is admitted dependency-version evidence."""

    parts = repository_relative_parts(path)
    if parts is None:
        return False
    final_name = parts[-1].lower()
    if (
        _REQUIREMENTS_FILENAME_PATTERN.fullmatch(final_name)
        or _CONSTRAINTS_FILENAME_PATTERN.fullmatch(final_name)
    ):
        return True
    suffix = final_name.rpartition(".")[2]
    return suffix in {"txt", "in"} and any(
        part in {"requirements", "constraints"} for part in parts[:-1]
    )


def is_admitted_requirements_file(path: str) -> bool:
    """Return whether an admitted exact-requirement path is requirements-family."""

    parts = repository_relative_parts(path)
    if parts is None:
        return False
    final_name = parts[-1].lower()
    if _REQUIREMENTS_FILENAME_PATTERN.fullmatch(final_name):
        return True
    suffix = final_name.rpartition(".")[2]
    return suffix in {"txt", "in"} and "requirements" in parts[:-1]


def extract_exact_requirement_changes(
    changed_file: ChangedFile,
) -> DependencyChangeExtractionResult:
    """Extract one exact transition from one admitted complete changed-file patch."""

    if not is_exact_requirement_file(changed_file.filename):
        return DependencyChangeProblem(
            reason="no_supported_dependency_file",
            detail=(
                f"Path {changed_file.filename!r} is not an admitted conventional "
                "requirements or constraints file."
            ),
        )

    evidence = DependencyChangeSourceEvidence(
        path=changed_file.filename,
        file_format="exact_requirement",
        extraction_method="changed_file_patch",
    )

    if changed_file.status != "modified":
        return _problem(
            "unsupported_dependency_file_status",
            (
                f"The source file status was {changed_file.status!r}; the current "
                "extractor supports only an in-place modified file."
            ),
            evidence,
        )

    if changed_file.patch is None or not changed_file.patch.strip():
        return _problem(
            "missing_dependency_patch",
            f"No usable patch evidence was available for {changed_file.filename}.",
            evidence,
        )

    removed: list[_PinnedRequirementLine] = []
    added: list[_PinnedRequirementLine] = []
    observed_additions = 0
    observed_deletions = 0

    for line in changed_file.patch.splitlines():
        if line.startswith("+++") or line.startswith("---"):
            continue
        if line.startswith("+"):
            observed_additions += 1
            match = _PINNED_REQUIREMENT_PATTERN.fullmatch(line[1:])
            if match:
                added.append(
                    _PinnedRequirementLine(
                        changed_file.filename,
                        match.group(1),
                        match.group(2),
                    )
                )
        elif line.startswith("-"):
            observed_deletions += 1
            match = _PINNED_REQUIREMENT_PATTERN.fullmatch(line[1:])
            if match:
                removed.append(
                    _PinnedRequirementLine(
                        changed_file.filename,
                        match.group(1),
                        match.group(2),
                    )
                )

    if (
        observed_additions != changed_file.additions
        or observed_deletions != changed_file.deletions
    ):
        return _problem(
            "incomplete_dependency_patch",
            (
                f"Patch evidence for {changed_file.filename} exposed "
                f"{observed_additions} additions and {observed_deletions} deletions, "
                f"but GitHub reported {changed_file.additions} additions and "
                f"{changed_file.deletions} deletions."
            ),
            evidence,
        )

    if not removed and not added:
        return _problem(
            "unsupported_requirement_format",
            (
                "No removed-and-added exact pinned requirement pair matched the "
                "current package==version boundary."
            ),
            evidence,
        )

    if len(removed) != 1 or len(added) != 1:
        return _problem(
            "multiple_dependency_version_changes",
            (
                "The exact-requirement rule requires exactly one removed and one "
                f"added exact pin; observed {len(removed)} removed and "
                f"{len(added)} added candidates."
            ),
            evidence,
        )

    old = removed[0]
    new = added[0]
    normalized_old = normalize_package_name(old.package)
    normalized_new = normalize_package_name(new.package)
    if normalized_old != normalized_new:
        return _problem(
            "multiple_dependency_version_changes",
            (
                f"Removed package {old.package!r} and added package {new.package!r} "
                "do not identify the same normalized package."
            ),
            evidence,
        )

    if old.version == new.version:
        return _problem(
            "version_unchanged",
            "The removed and added requirements specify the same version.",
            evidence,
        )

    return ExtractedDependencyVersionChange(
        package=new.package,
        normalized_package=normalized_new,
        old_version=old.version,
        proposed_version=new.version,
        source_evidence=evidence,
    )


def _problem(
    reason: str,
    detail: str,
    evidence: DependencyChangeSourceEvidence,
) -> DependencyChangeProblem:
    return DependencyChangeProblem(
        reason=reason,  # type: ignore[arg-type]
        detail=detail,
        source_evidence=(evidence,),
    )
