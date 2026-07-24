"""Interpret validated GitHub patch evidence as one pinned dependency update.

The acquisition layer is responsible for obtaining and structurally validating
``ChangedFile`` records. This module owns the next, deterministic step: deciding
whether those records prove exactly one supported ``package==old`` to
``package==new`` transition.

No network I/O occurs here. Evidence outside the deliberately narrow grammar is
returned as an explicit unsupported result rather than guessed into a dependency
identity. This separation keeps transport failures, malformed responses, and
valid-but-unsupported changes distinguishable.
"""

from __future__ import annotations

import re
from collections.abc import Sequence
from dataclasses import dataclass

from .github_client import ChangedFile

# Supported grammar: one complete ``distribution==version`` requirement line.
# ``fullmatch`` is essential: unlike ``match`` or ``search``, it rejects a valid-
# looking fragment embedded in a richer expression such as an environment marker.
_PINNED_REQUIREMENT_PATTERN = re.compile(
    r"^\s*([A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?)"
    r"==([A-Za-z0-9][A-Za-z0-9.!+_-]*)\s*$"
)

# PEP 503 treats every consecutive run of ``-``, ``_``, or ``.`` as the same
# separator for distribution-name comparison.
_NORMALIZED_PACKAGE_SEPARATOR = re.compile(r"[-_.]+")


@dataclass(frozen=True, slots=True)
class PinnedDependencyChange:
    """One proven exact-pin update that downstream decision logic may consume.

    ``frozen=True`` prevents accidental mutation after evidence interpretation.
    ``slots=True`` gives the record a fixed field layout and prevents undeclared
    attributes from being attached later.
    """

    source_file: str
    package: str
    normalized_package: str
    old_version: str
    proposed_version: str


@dataclass(frozen=True, slots=True)
class UnsupportedDependencyChange:
    """A normal abstention result outside the current extraction boundary.

    Unsupported evidence is not automatically malformed or erroneous. ``reason``
    gives callers a stable machine-readable category, while ``detail`` preserves
    the human-readable explanation of where interpretation stopped.
    """

    reason: str
    detail: str


# The union makes abstention part of the function contract: callers cannot assume
# that every valid GitHub response establishes a supported dependency change.
type DependencyChangeResult = PinnedDependencyChange | UnsupportedDependencyChange


@dataclass(frozen=True, slots=True)
class _PinnedRequirementLine:
    """Internal representation of one exact pin recovered from one diff line."""

    source_file: str
    package: str
    version: str


def extract_pinned_dependency_change(
    changed_files: Sequence[ChangedFile],
) -> DependencyChangeResult:
    """Recognize one same-file ``package==old`` to ``package==new`` change.

    The function assumes that the acquisition layer already validated each
    changed-file record's structure. It still checks evidence completeness and
    semantic invariants because a structurally valid response does not prove that
    the visible patch is complete or that its edits describe one dependency.

    Args:
        changed_files: Validated changed-file evidence for one pull request.

    Returns:
        A :class:`PinnedDependencyChange` only when the evidence establishes one
        supported update. Every other valid evidence shape becomes an
        :class:`UnsupportedDependencyChange` with a stable stopping reason.
    """

    if not changed_files:
        return UnsupportedDependencyChange(
            reason="no_changed_files",
            detail="No changed-file records were available for dependency extraction.",
        )

    # Collection is intentionally separate from interpretation. We first observe
    # every exact-pin candidate, then decide whether the complete set is unambiguous.
    removed: list[_PinnedRequirementLine] = []
    added: list[_PinnedRequirementLine] = []
    records_by_filename = {record.filename: record for record in changed_files}

    for record in changed_files:
        # A valid file record may legitimately lack patch text, for example when
        # GitHub omits or truncates it. That is an interpretation boundary rather
        # than a transport or response-schema failure.
        if record.patch is None or not record.patch.strip():
            return UnsupportedDependencyChange(
                reason="missing_patch_evidence",
                detail=f"No usable patch evidence was available for {record.filename}.",
            )

        observed_additions = 0
        observed_deletions = 0

        for line in record.patch.splitlines():
            # Unified-diff file headers begin with ``+++`` and ``---`` too, but
            # they identify files rather than added or removed content lines.
            if line.startswith("+++") or line.startswith("---"):
                continue
            if line.startswith("+"):
                observed_additions += 1
                # Slice off the diff marker before applying the requirement grammar.
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

        # Completeness invariant: the edits visible in ``patch`` must agree with
        # GitHub's per-file totals. Otherwise a truncated patch could look like a
        # simple one-package update while hiding additional edits.
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

    # Preserve ambiguity instead of selecting a candidate heuristically. A wrong
    # dependency identity would contaminate every later evidence lookup.
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

    # Pairing across files is not yet supported because proximity and intent cannot
    # be established safely from two independent patches.
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

    # Raw spellings such as ``my_package`` and ``my-package`` may identify the
    # same Python distribution, so identity is compared only after normalization.
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

    # Prefer the added spelling for presentation while retaining the normalized
    # identity used for reliable comparison and later lookups.
    return PinnedDependencyChange(
        source_file=old.source_file,
        package=new.package,
        normalized_package=normalized_new,
        old_version=old.version,
        proposed_version=new.version,
    )


def normalize_package_name(package: str) -> str:
    """Normalize a distribution name using the PEP 503 comparison rule.

    Runs of hyphens, underscores, and periods collapse to one hyphen, then the
    result is lowercased. This supports identity comparison only; it does not
    resolve packages, versions, aliases, or dependency metadata.
    """

    return _NORMALIZED_PACKAGE_SEPARATOR.sub("-", package).lower()
