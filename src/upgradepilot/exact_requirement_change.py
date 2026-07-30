"""Interpret exact-version changes in admitted requirements and constraints files.

This module owns the source-specific rules for conventional requirements and
constraints paths whose complete GitHub patch contains one exact
``package==old`` to ``package==new`` transition. It does not establish dependency
role, installation, CI consumption, compatibility, safety, or maintainer action.

The public Step 2 API is:

``is_exact_requirement_file``
    Decide whether one repository-relative path is an admitted exact-requirement
    evidence source.

``extract_exact_requirement_changes``
    Interpret one admitted ``ChangedFile`` and return one file-level extracted
    change or one explicit dependency-evidence problem.

The private legacy entry point preserves the existing multi-file
``PinnedDependencyChange`` behavior while CLI and CI callers remain unmigrated.
"""

from __future__ import annotations

import re
from collections.abc import Sequence
from dataclasses import dataclass

from .dependency_change import (
    DependencyChangeEvidenceProblem,
    DependencyChangeExtractionResult,
    DependencyChangeProblemCode,
    DependencyFileEvidence,
    ExtractedDependencyVersionChange,
    PinnedDependencyChange,
    UnsupportedDependencyChange,
    normalize_package_name,
)
from .github_client import ChangedFile

# The whole requirement line must be one distribution name, exactly ``==``, and
# one version token. ``fullmatch`` rejects ranges, markers, extras, URLs,
# comments, editable installs, and other richer requirement forms.
_PINNED_REQUIREMENT_PATTERN = re.compile(
    r"^\s*([A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?)"
    r"==([A-Za-z0-9][A-Za-z0-9.!+_-]*)\s*$"
)

# Conventional descriptive filenames include requirements.txt/requirements.in,
# constraints.txt/constraints.in, and a non-empty description introduced by
# one hyphen, underscore, or period.
_DESCRIPTIVE_FILENAME_PATTERN = re.compile(
    r"^(?:requirements|constraints)"
    r"(?:[-_.][A-Za-z0-9][A-Za-z0-9._-]*)?"
    r"\.(?:txt|in)$"
)

# Translate the legacy stopping vocabulary into ADR-0004's shared vocabulary.
# Two states are defensive: a one-file public extraction call cannot produce an
# empty-input or cross-file result, but their mapping prevents an arbitrary
# string from escaping if the private compatibility function changes later.
_LEGACY_PROBLEM_CODES: dict[str, DependencyChangeProblemCode] = {
    "no_changed_files": "invalid_dependency_record",
    "missing_patch_evidence": "missing_dependency_patch",
    "incomplete_patch_evidence": "incomplete_dependency_patch",
    "no_supported_pinned_change": "unsupported_requirement_format",
    "ambiguous_pinned_changes": "multiple_dependency_version_changes",
    "cross_file_change": "invalid_dependency_record",
    "unsupported_file_status": "unsupported_dependency_file_status",
    "package_mismatch": "multiple_dependency_version_changes",
    "unchanged_version": "version_unchanged",
}


@dataclass(frozen=True, slots=True)
class _PinnedRequirementLine:
    """Private exact-pin candidate recovered from one diff content line."""

    source_file: str
    package: str
    version: str


def is_exact_requirement_file(path: str) -> bool:
    """Return whether a normalized relative path is an admitted source file.

    Accepted paths have either:

    * a conventional requirements/constraints descriptive final filename; or
    * a ``.txt``/``.in`` final filename beneath an exact lowercase
      ``requirements`` or ``constraints`` directory component.

    The complete path is preserved elsewhere. Eligibility means only that the
    path may supply package/version evidence.
    """

    parts = _relative_path_parts(path)
    if parts is None:
        return False

    final_name = parts[-1].lower()
    if _DESCRIPTIVE_FILENAME_PATTERN.fullmatch(final_name):
        return True

    suffix = final_name.rpartition(".")[2]
    return suffix in {"txt", "in"} and any(
        part in {"requirements", "constraints"} for part in parts[:-1]
    )


def extract_exact_requirement_changes(
    changed_file: ChangedFile,
) -> DependencyChangeExtractionResult:
    """Extract one exact version transition from one admitted changed file.

    This is a file-level result, not a pull-request-wide trusted result. A later
    comparison stage must consider every admitted dependency file and recognized
    evidence problem before producing ``DependencyVersionChange``.
    """

    if not is_exact_requirement_file(changed_file.filename):
        return DependencyChangeEvidenceProblem(
            reason="no_supported_dependency_file",
            detail=(
                f"Path {changed_file.filename!r} is not an admitted conventional "
                "requirements or constraints file."
            ),
        )

    evidence = DependencyFileEvidence(
        path=changed_file.filename,
        file_format="exact_requirement",
        extraction_method="changed_file_patch",
    )
    legacy_result = _extract_legacy_pinned_dependency_change((changed_file,))

    if isinstance(legacy_result, PinnedDependencyChange):
        return ExtractedDependencyVersionChange(
            package=legacy_result.package,
            normalized_package=legacy_result.normalized_package,
            old_version=legacy_result.old_version,
            proposed_version=legacy_result.proposed_version,
            source_evidence=evidence,
        )

    reason = _LEGACY_PROBLEM_CODES.get(legacy_result.reason)
    if reason is None:
        return DependencyChangeEvidenceProblem(
            reason="invalid_dependency_record",
            detail=(
                "The exact-requirement compatibility parser returned an unknown "
                f"problem reason {legacy_result.reason!r}."
            ),
            source_evidence=(evidence,),
        )

    return DependencyChangeEvidenceProblem(
        reason=reason,
        detail=legacy_result.detail,
        source_evidence=(evidence,),
    )


def _relative_path_parts(path: str) -> tuple[str, ...] | None:
    """Return validated POSIX repository-relative components or ``None``."""

    if not path or path.startswith("/") or "\\" in path:
        return None

    parts = tuple(path.split("/"))
    if any(not part or part in {".", ".."} for part in parts):
        return None
    return parts


def _extract_legacy_pinned_dependency_change(
    changed_files: Sequence[ChangedFile],
) -> PinnedDependencyChange | UnsupportedDependencyChange:
    """Preserve the validated legacy multi-file exact-pin behavior unchanged."""

    if not changed_files:
        return UnsupportedDependencyChange(
            reason="no_changed_files",
            detail="No changed-file records were available for dependency extraction.",
        )

    removed: list[_PinnedRequirementLine] = []
    added: list[_PinnedRequirementLine] = []
    records_by_filename = {record.filename: record for record in changed_files}

    for record in changed_files:
        if record.patch is None or not record.patch.strip():
            return UnsupportedDependencyChange(
                reason="missing_patch_evidence",
                detail=f"No usable patch evidence was available for {record.filename}.",
            )

        observed_additions = 0
        observed_deletions = 0

        for line in record.patch.splitlines():
            if line.startswith("+++") or line.startswith("---"):
                continue
            if line.startswith("+"):
                observed_additions += 1
                match = _PINNED_REQUIREMENT_PATTERN.fullmatch(line[1:])
                if match:
                    added.append(
                        _PinnedRequirementLine(
                            record.filename, match.group(1), match.group(2)
                        )
                    )
            elif line.startswith("-"):
                observed_deletions += 1
                match = _PINNED_REQUIREMENT_PATTERN.fullmatch(line[1:])
                if match:
                    removed.append(
                        _PinnedRequirementLine(
                            record.filename, match.group(1), match.group(2)
                        )
                    )

        if (
            observed_additions != record.additions
            or observed_deletions != record.deletions
        ):
            return UnsupportedDependencyChange(
                reason="incomplete_patch_evidence",
                detail=(
                    f"Patch evidence for {record.filename} exposed "
                    f"{observed_additions} additions and "
                    f"{observed_deletions} deletions, "
                    f"but GitHub reported {record.additions} additions and "
                    f"{record.deletions} deletions."
                ),
            )

    if not removed and not added:
        return UnsupportedDependencyChange(
            reason="no_supported_pinned_change",
            detail=(
                "No removed-and-added exact pinned requirement pair matched the "
                "current package==version boundary."
            ),
        )

    if len(removed) != 1 or len(added) != 1:
        return UnsupportedDependencyChange(
            reason="ambiguous_pinned_changes",
            detail=(
                "The current extractor requires exactly one removed and one added "
                f"exact pinned requirement; observed {len(removed)} removed and "
                f"{len(added)} added candidates."
            ),
        )

    old = removed[0]
    new = added[0]

    if old.source_file != new.source_file:
        return UnsupportedDependencyChange(
            reason="cross_file_change",
            detail=(
                "The removed and added pinned requirements came from different files."
            ),
        )

    source_record = records_by_filename[old.source_file]
    if source_record.status != "modified":
        return UnsupportedDependencyChange(
            reason="unsupported_file_status",
            detail=(
                f"The source file status was {source_record.status!r}; the current "
                "extractor supports only an in-place modified file."
            ),
        )

    normalized_old = normalize_package_name(old.package)
    normalized_new = normalize_package_name(new.package)
    if normalized_old != normalized_new:
        return UnsupportedDependencyChange(
            reason="package_mismatch",
            detail=(
                f"Removed package {old.package!r} and added package {new.package!r} "
                "do not identify the same normalized package."
            ),
        )

    if old.version == new.version:
        return UnsupportedDependencyChange(
            reason="unchanged_version",
            detail="The removed and added requirements specify the same version.",
        )

    return PinnedDependencyChange(
        source_file=old.source_file,
        package=new.package,
        normalized_package=normalized_new,
        old_version=old.version,
        proposed_version=new.version,
    )
