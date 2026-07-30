"""Interpret dependency-file evidence and define shared dependency-change records.

Purpose of this file
--------------------
``github_client.py`` acquires and validates ``ChangedFile`` records, including file
status, GitHub's addition/deletion counts, and optional unified-diff patch text. This
module currently performs the next deterministic stage for one narrow grammar:

``package==old_version`` → ``package==new_version``

The module also defines the broader immutable records accepted by ADR-0004. Those
records separate:

* evidence from one dependency file;
* one possible version change extracted from that file;
* one version change trusted after all admitted PR evidence is compared;
* an explicit evidence problem that prevents a trusted result.

The new records are additive in Step 1. The existing
``extract_pinned_dependency_change`` function, ``PinnedDependencyChange`` result, and
``UnsupportedDependencyChange`` result remain the implemented runtime path until later
migration steps prove replacements through tests.

How this file relates to the rest of UpgradePilot
-------------------------------------------------
Current input:
    A complete tuple of ``ChangedFile`` records from
    ``GitHubReadClient.get_changed_files``.

Current output:
    ``cli.py`` checks whether the result is ``PinnedDependencyChange``. Only then can
    later CI stages know which requirements file and package they must look for.

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

# Supported legacy grammar: the entire requirement line must contain one distribution
# name, exactly ``==``, and one version token. ``fullmatch`` later rejects richer syntax
# such as environment markers, ranges, extras, URLs, comments, or editable installs.
_PINNED_REQUIREMENT_PATTERN = re.compile(
    r"^\s*([A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?)"
    r"==([A-Za-z0-9][A-Za-z0-9.!+_-]*)\s*$"
)

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
