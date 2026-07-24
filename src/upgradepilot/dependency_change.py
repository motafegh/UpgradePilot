"""Bounded dependency-change extraction from validated GitHub patch evidence."""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
import re

from .github_client import ChangedFile

_PINNED_REQUIREMENT_PATTERN = re.compile(
    r"^\s*([A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?)"
    r"==([A-Za-z0-9][A-Za-z0-9.!+_-]*)\s*$"
)
_NORMALIZED_PACKAGE_SEPARATOR = re.compile(r"[-_.]+")


@dataclass(frozen=True, slots=True)
class PinnedDependencyChange:
    """One supported exact pinned Python dependency version change."""

    source_file: str
    package: str
    normalized_package: str
    old_version: str
    proposed_version: str


@dataclass(frozen=True, slots=True)
class UnsupportedDependencyChange:
    """An explicit non-exception result outside the current extraction boundary."""

    reason: str
    detail: str


type DependencyChangeResult = PinnedDependencyChange | UnsupportedDependencyChange


@dataclass(frozen=True, slots=True)
class _PinnedRequirementLine:
    source_file: str
    package: str
    version: str


def extract_pinned_dependency_change(
    changed_files: Sequence[ChangedFile],
) -> DependencyChangeResult:
    """Recognize exactly one same-file ``package==old`` to ``package==new`` change."""

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
                        _PinnedRequirementLine(record.filename, match.group(1), match.group(2))
                    )
            elif line.startswith("-"):
                observed_deletions += 1
                match = _PINNED_REQUIREMENT_PATTERN.fullmatch(line[1:])
                if match:
                    removed.append(
                        _PinnedRequirementLine(record.filename, match.group(1), match.group(2))
                    )

        if (
            observed_additions != record.additions
            or observed_deletions != record.deletions
        ):
            return UnsupportedDependencyChange(
                reason="incomplete_patch_evidence",
                detail=(
                    f"Patch evidence for {record.filename} exposed "
                    f"{observed_additions} additions and {observed_deletions} deletions, "
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
            detail="The removed and added pinned requirements came from different files.",
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


def normalize_package_name(package: str) -> str:
    """Normalize a Python distribution name using the PEP 503 comparison rule."""

    return _NORMALIZED_PACKAGE_SEPARATOR.sub("-", package).lower()
