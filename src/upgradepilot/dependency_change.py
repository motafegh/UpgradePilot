"""Interpret complete changed-file evidence as one pinned dependency update.

Purpose of this file
--------------------
``github_client.py`` acquires and validates ``ChangedFile`` records, including file
status, GitHub's addition/deletion counts, and optional unified-diff patch text. This
module performs the next deterministic stage: it asks whether those records prove
exactly one supported transition of the form:

``package==old_version`` → ``package==new_version``

The function does not contact GitHub and does not decide upgrade safety. It either
returns a trusted ``PinnedDependencyChange`` or a normal
``UnsupportedDependencyChange`` explaining why the current narrow grammar could not
establish one dependency identity.

How this file relates to the rest of UpgradePilot
-------------------------------------------------
Input:
    A complete tuple of ``ChangedFile`` records from
    ``GitHubReadClient.get_changed_files``.

Output:
    ``cli.py`` checks whether the result is ``PinnedDependencyChange``. Only then can
    later CI stages know which requirements file and package they must look for.

Downstream use:
    ``workflow_commands.py`` receives ``source_file``, ``package``, and
    ``normalized_package`` from the supported result. A wrong or guessed dependency
    identity would therefore contaminate every later CI-authority decision, which is
    why this module preserves ambiguity instead of selecting heuristically.

Interpretation flow
-------------------
1. Reject an empty changed-file collection.
2. Require usable patch evidence for every record.
3. Scan visible added and removed diff lines for exact ``package==version`` pins.
4. Reconcile visible patch counts with GitHub's file metadata.
5. Require exactly one removed and one added pin in the same modified file.
6. Normalize package spellings under the PEP 503 comparison rule.
7. Require the package identity to match and the version to change.
8. Return immutable supported evidence; otherwise return a reasoned abstention.
"""

from __future__ import annotations

import re
from collections.abc import Sequence
from dataclasses import dataclass

from .github_client import ChangedFile

# Supported grammar: the entire requirement line must contain one distribution name,
# exactly ``==``, and one version token. ``fullmatch`` later rejects richer syntax such
# as environment markers, ranges, extras, URLs, comments, or editable installs.
_PINNED_REQUIREMENT_PATTERN = re.compile(
    r"^\s*([A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?)"
    r"==([A-Za-z0-9][A-Za-z0-9.!+_-]*)\s*$"
)

# Python distribution names may use hyphens, underscores, or periods interchangeably
# for comparison. A compiled pattern collapses any consecutive run of those separators.
_NORMALIZED_PACKAGE_SEPARATOR = re.compile(r"[-_.]+")


@dataclass(frozen=True, slots=True)
class PinnedDependencyChange:
    """One proven exact-pin update safe for later evidence stages to consume.

    ``source_file`` identifies the requirements file CI must install. ``package`` keeps
    the added spelling for readable output, while ``normalized_package`` preserves the
    comparison identity used by command matching. The two version fields make the
    observed transition explicit.

    The dataclass is frozen because downstream CI acquisition must not mutate the
    dependency question after it has been established.
    """

    source_file: str
    package: str
    normalized_package: str
    old_version: str
    proposed_version: str


@dataclass(frozen=True, slots=True)
class UnsupportedDependencyChange:
    """Normal abstention when valid evidence lies outside the current rule.

    Unsupported does not automatically mean malformed or unsafe. It means this narrow
    extractor could not prove one exact supported change. ``reason`` is stable for
    program logic; ``detail`` explains the stopping point to the user.
    """

    reason: str
    detail: str


# Making abstention part of the return type forces ``cli.py`` to narrow the union with
# ``isinstance`` before accessing package/version fields.
type DependencyChangeResult = PinnedDependencyChange | UnsupportedDependencyChange


@dataclass(frozen=True, slots=True)
class _PinnedRequirementLine:
    """Private candidate recovered from one added or removed diff line.

    The temporary record keeps file identity beside the package/version pair while all
    patches are scanned. It is private because a candidate is not yet trusted as the
    PR's actual dependency change.
    """

    source_file: str
    package: str
    version: str


def extract_pinned_dependency_change(
    changed_files: Sequence[ChangedFile],
) -> DependencyChangeResult:
    """Recognize one same-file exact-pin version transition.

    Goal:
        Convert complete structural file evidence into one unambiguous dependency
        identity for later exact-head CI analysis.

    ``Sequence`` is accepted because the algorithm needs ordered iteration and length
    semantics, not a particular list or tuple implementation.

    The function separates observation from decision: it first collects every visible
    supported removed/added candidate, then applies global ambiguity and identity
    checks after all files have been examined.
    """

    if not changed_files:
        return UnsupportedDependencyChange(
            reason="no_changed_files",
            detail="No changed-file records were available for dependency extraction.",
        )

    # Mutable lists are appropriate during collection because candidates arrive while
    # patches are scanned. They remain private and are never returned as trusted output.
    removed: list[_PinnedRequirementLine] = []
    added: list[_PinnedRequirementLine] = []

    # The dictionary comprehension creates a direct filename lookup used later to check
    # the source record's GitHub status after the unique pair is known.
    records_by_filename = {record.filename: record for record in changed_files}

    for record in changed_files:
        # ``patch=None`` is a valid acquisition state from ``github_client.py`` but is
        # insufficient for interpretation. Empty/whitespace patch text is equivalent
        # here because no visible diff lines can establish the change.
        if record.patch is None or not record.patch.strip():
            return UnsupportedDependencyChange(
                reason="missing_patch_evidence",
                detail=f"No usable patch evidence was available for {record.filename}.",
            )

        # These counters measure only real changed content lines visible in the patch.
        # They are later compared with GitHub's independently reported metadata.
        observed_additions = 0
        observed_deletions = 0

        for line in record.patch.splitlines():
            # Unified-diff file headers also begin with ``+++`` and ``---``. They name
            # files and must not be counted as content additions/deletions.
            if line.startswith("+++") or line.startswith("---"):
                continue
            if line.startswith("+"):
                observed_additions += 1

                # Slice away the diff marker before applying the requirement grammar.
                # ``fullmatch`` requires the complete remaining line to be one exact pin.
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

        # Completeness invariant: a truncated patch might show one neat dependency line
        # while hiding other edits. Visible addition/deletion counts must therefore equal
        # GitHub's per-file totals before any semantic interpretation is trusted.
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

    # The absence of supported candidate lines is different from malformed acquisition:
    # the patch may be complete but use a dependency form outside this grammar.
    if not removed and not added:
        return UnsupportedDependencyChange(
            reason="no_supported_pinned_change",
            detail=(
                "No removed-and-added exact pinned requirement pair matched the "
                "current package==version boundary."
            ),
        )

    # Exactly one candidate on each side is required. Selecting among several apparent
    # updates would be a heuristic guess and could direct later CI analysis at the wrong
    # package or source file.
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

    # A deletion in one file and addition in another cannot safely be paired from patch
    # proximity alone, so cross-file transitions remain outside the current rule.
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

    # Spelling may differ while identifying the same distribution, for example
    # ``my_package`` versus ``my-package``. Compare only after PEP 503 normalization.
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

    # Removing and adding the identical version is not an upgrade transition even if
    # line spelling changed elsewhere.
    if old.version == new.version:
        return UnsupportedDependencyChange(
            reason="unchanged_version",
            detail="The removed and added requirements specify the same version.",
        )

    # Use the added package spelling for user-facing output, while retaining the
    # normalized identity needed by workflow command matching.
    return PinnedDependencyChange(
        source_file=old.source_file,
        package=new.package,
        normalized_package=normalized_new,
        old_version=old.version,
        proposed_version=new.version,
    )


def normalize_package_name(package: str) -> str:
    """Return the PEP 503 comparison form of a distribution name.

    Consecutive hyphens, underscores, and periods collapse to one hyphen, then the
    string is lowercased. This provides identity comparison only; it does not contact a
    package index, validate that the distribution exists, or resolve aliases/versions.
    """

    return _NORMALIZED_PACKAGE_SEPARATOR.sub("-", package).lower()
