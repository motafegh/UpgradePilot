"""Interpret exact package-version changes in complete ``uv.lock`` files.

The first bounded structured-lockfile rule accepts only modified ``uv.lock`` files at
normalized repository-relative paths. Complete base/head repository text is parsed with
``tomllib`` and compared conservatively; ambiguous structural changes remain explicit
problems rather than heuristic package pairings.

This module owns a deliberately narrow proposition:

``exact base/head uv.lock evidence -> one exact file-level version transition``

It does *not* decide whether the changed package belongs to a selected dependency
environment, was installed by CI, ran successfully, or is behaviorally compatible.
Those stronger propositions are owned by later dependency/CI layers.

Cross-file route for the uv-lock path:

``src/upgradepilot/dependency/analysis.py``
    discovers an admitted changed ``uv.lock`` and asks
``src/upgradepilot/github/repository.py``
    for exact base/head ``RepositoryTextFile`` evidence, then calls
``extract_uv_lock_changes(...)`` in this module
    to produce one file-level ``ExtractedDependencyVersionChange`` or
    ``DependencyChangeProblem`` owned by
``src/upgradepilot/dependency/change.py``.

After all admitted dependency sources are extracted,
``dependency/change.py::compare_extracted_dependency_changes(...)`` establishes at most
one PR-wide ``DependencyVersionChange``. ``dependency/analysis.py`` then translates that
trusted change/provenance into dependency-owned source contexts such as
``UvLockDependencyContext``. Environment selection, membership, CI consumption, and
runtime evidence are deliberately later responsibilities.
"""

from __future__ import annotations

import re
import tomllib
from collections import Counter, defaultdict
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, Literal

from ..github.pull_request import ChangedFile
from ..github.repository import (
    ExactRepositoryFileEvidence,
    RepositoryTextFile,
    UnavailableRepositoryFile,
)
from ..package_identity import normalize_package_name
from ..repository_path import repository_relative_parts
from .change import (
    DependencyChangeExtractionResult,
    DependencyChangeProblem,
    DependencyChangeProblemCode,
    DependencyChangeSourceEvidence,
    ExtractedDependencyVersionChange,
)

# Artifact download metadata may legitimately churn while package/dependency semantics stay
# unchanged, so this narrow package-record comparison deliberately ignores these fields.
_ARTIFACT_FIELDS = frozenset({"sdist", "wheels"})

# Only these local-workspace source shapes are admitted without a textual package version.
# Other versionless records remain unsupported rather than being interpreted heuristically.
_VERSIONLESS_SOURCE_KEYS = frozenset({"editable", "virtual"})

# Reject malformed raw package spellings before normalization so invalid lock evidence
# cannot become a trusted canonical package identity.
_DISTRIBUTION_NAME_PATTERN = re.compile(
    r"^[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?$"
)

# Distinguish an absent TOML key from a key explicitly present with a false-like value.
# That distinction matters when deciding whether two lock records have the same structure.
_MISSING = object()


@dataclass(frozen=True, slots=True)
class _UvPackageRecord:
    """One validated lock-package record in the shape needed for comparison.

    ``package`` preserves source spelling while ``normalized_package`` provides the
    cross-source comparison identity. ``record_data`` retains the full TOML table because
    source/marker and same-version structural changes cannot be judged from name/version
    alone.
    """

    package: str
    normalized_package: str
    version: str | None
    record_data: Mapping[str, Any]


@dataclass(frozen=True, slots=True)
class _ParsedUvLock:
    """Validated package records grouped by normalized distribution name.

    A normalized name can map to multiple records because a universal lock may contain
    repeated resolution branches. Keeping those records grouped but unpaired prevents a
    positional guess from masquerading as evidence.
    """

    groups: Mapping[str, tuple[_UvPackageRecord, ...]]


def is_modified_uv_lock_file(changed_file: ChangedFile) -> bool:
    """Return whether dependency analysis should acquire exact content for this uv.lock."""

    parts = repository_relative_parts(changed_file.filename)
    return (
        changed_file.status == "modified"
        and parts is not None
        and parts[-1] == "uv.lock"
    )


def extract_uv_lock_changes(
    changed_file: ChangedFile,
    base_file: ExactRepositoryFileEvidence,
    head_file: ExactRepositoryFileEvidence,
) -> DependencyChangeExtractionResult:
    """Extract one safe file-level version transition from exact base/head locks.

    This guard-clause pipeline admits path/status, requires both exact historical files,
    binds coherent provenance, validates the supported lock structure, then compares
    package records conservatively. Expected evidence failures become typed
    ``DependencyChangeProblem`` results rather than guesses.
    """

    parts = repository_relative_parts(changed_file.filename)
    if parts is None or parts[-1] != "uv.lock":
        return DependencyChangeProblem(
            reason="no_supported_dependency_file",
            detail=(
                f"Path {changed_file.filename!r} is not an admitted normalized "
                "repository-relative file whose basename is exactly 'uv.lock'."
            ),
        )

    # Addition/deletion/rename needs different evidence semantics from comparing one lockfile
    # in place, so the first structured-lock rule stops instead of treating those shapes as
    # package-version transitions.
    if changed_file.status != "modified":
        return DependencyChangeProblem(
            reason="unsupported_dependency_file_status",
            detail=(
                f"The uv.lock file status was {changed_file.status!r}; the first "
                "structured-lockfile rule supports only an in-place modified file."
            ),
        )

    # Missing historical content is a normal evidence state. Do not parse one side and infer
    # what the unavailable side might have contained.
    unavailable = _first_unavailable_file(base_file, head_file)
    if unavailable is not None:
        return DependencyChangeProblem(
            reason="dependency_file_unavailable",
            detail=(
                f"Exact uv.lock text was unavailable at revision "
                f"{unavailable.revision!r}: {unavailable.detail}"
            ),
        )

    # The unavailable guard narrows both evidence unions. These assertions make the
    # resulting runtime invariant explicit before provenance or content is trusted.
    assert isinstance(base_file, RepositoryTextFile)
    assert isinstance(head_file, RepositoryTextFile)

    # Bind repository identity, exact revisions, blob identities, and byte evidence before
    # semantic parsing so a later version claim cannot become detached from its source.
    evidence_result = _build_source_evidence(changed_file, base_file, head_file)
    if isinstance(evidence_result, DependencyChangeProblem):
        return evidence_result
    evidence = evidence_result

    base_result = _parse_uv_lock(base_file, evidence, side="base")
    if isinstance(base_result, DependencyChangeProblem):
        return base_result

    head_result = _parse_uv_lock(head_file, evidence, side="head")
    if isinstance(head_result, DependencyChangeProblem):
        return head_result

    return _compare_uv_lock_packages(base_result, head_result, evidence)


def _first_unavailable_file(
    base_file: ExactRepositoryFileEvidence,
    head_file: ExactRepositoryFileEvidence,
) -> UnavailableRepositoryFile | None:
    """Return unavailable evidence itself so the caller can preserve its revision/detail."""

    if isinstance(base_file, UnavailableRepositoryFile):
        return base_file
    if isinstance(head_file, UnavailableRepositoryFile):
        return head_file
    return None


def _build_source_evidence(
    changed_file: ChangedFile,
    base_file: RepositoryTextFile,
    head_file: RepositoryTextFile,
) -> DependencyChangeSourceEvidence | DependencyChangeProblem:
    """Bind semantic comparison to coherent exact-file provenance.

    The resulting ``DependencyChangeSourceEvidence`` survives file-level extraction and
    PR-wide comparison, allowing downstream source-context code to identify exactly which
    base/head files support the change.

    ``RepositoryTextFile`` still permits older/manual fixtures with optional strong
    provenance fields, so this boundary revalidates the identities it relies on rather
    than assuming every instance came from the runtime provider. Blob SHAs are preserved
    provider-reported identities; this function does not recompute Git blob hashes from
    decoded content.
    """

    expected_path = changed_file.filename
    if (
        not base_file.repository
        or base_file.repository != head_file.repository
        or base_file.path != expected_path
        or base_file.returned_path != expected_path
        or head_file.path != expected_path
        or head_file.returned_path != expected_path
    ):
        return DependencyChangeProblem(
            reason="invalid_dependency_record",
            detail=(
                "Exact uv.lock repository/path evidence did not consistently match "
                "the changed-file identity at base and head."
            ),
        )

    # Byte-count equality is acquisition-consistency evidence, not a package/dependency
    # semantic claim; both historical sides must independently satisfy it.
    for side, repository_file in (("base", base_file), ("head", head_file)):
        if not repository_file.revision or not repository_file.blob_sha:
            return DependencyChangeProblem(
                reason="invalid_dependency_record",
                detail=f"The exact {side} uv.lock evidence lacked a revision or blob SHA.",
            )
        if (
            type(repository_file.reported_byte_count) is not int
            or type(repository_file.decoded_byte_count) is not int
            or repository_file.reported_byte_count < 0
            or repository_file.decoded_byte_count < 0
            or repository_file.reported_byte_count
            != repository_file.decoded_byte_count
        ):
            return DependencyChangeProblem(
                reason="invalid_dependency_record",
                detail=(
                    f"The exact {side} uv.lock byte evidence was invalid or "
                    "internally inconsistent."
                ),
            )

    return DependencyChangeSourceEvidence(
        path=expected_path,
        file_format="uv_lock",
        extraction_method="exact_base_head_files",
        base_revision=base_file.revision,
        base_blob_sha=base_file.blob_sha,
        base_byte_count=base_file.decoded_byte_count,
        head_revision=head_file.revision,
        head_blob_sha=head_file.blob_sha,
        head_byte_count=head_file.decoded_byte_count,
    )


def _parse_uv_lock(
    repository_file: RepositoryTextFile,
    evidence: DependencyChangeSourceEvidence,
    *,
    side: Literal["base", "head"],
) -> _ParsedUvLock | DependencyChangeProblem:
    """Parse the complete lock and validate only the structure this extractor can judge.

    This deliberately does not reproduce uv's resolver. The lock document's top-level
    ``revision`` is uv format metadata, not the Git revision carried by
    ``RepositoryTextFile.revision``.
    """

    try:
        document = tomllib.loads(repository_file.content)
    except tomllib.TOMLDecodeError as exc:
        return _problem(
            "malformed_dependency_file",
            f"The exact {side} uv.lock file was not valid TOML: {exc}.",
            evidence,
        )

    # A newer lock schema may assign different meaning to fields this comparison relies on;
    # abstain rather than interpreting it with schema-1 assumptions.
    schema_version = document.get("version", _MISSING)
    if type(schema_version) is not int:
        return _problem(
            "malformed_dependency_file",
            f"The exact {side} uv.lock field 'version' must be an integer.",
            evidence,
        )
    if schema_version != 1:
        return _problem(
            "unsupported_uv_lock_schema",
            (
                f"The exact {side} uv.lock schema version was {schema_version!r}; "
                "the first supported boundary admits only version 1."
            ),
            evidence,
        )

    revision = document.get("revision", _MISSING)
    if type(revision) is not int or revision < 0:
        return _problem(
            "malformed_dependency_file",
            f"The exact {side} uv.lock field 'revision' must be a non-negative integer.",
            evidence,
        )

    raw_packages = document.get("package", _MISSING)
    if not isinstance(raw_packages, list):
        return _problem(
            "invalid_dependency_record",
            f"The exact {side} uv.lock field 'package' must be an array of tables.",
            evidence,
        )

    # Normalize identity for cross-source comparison, but keep every repeated record
    # separately because universal-lock branches cannot be paired safely by position.
    groups: defaultdict[str, list[_UvPackageRecord]] = defaultdict(list)
    for index, raw_record in enumerate(raw_packages):
        record_result = _validate_package_record(raw_record, side=side, index=index)
        if isinstance(record_result, str):
            return _problem("invalid_dependency_record", record_result, evidence)
        groups[record_result.normalized_package].append(record_result)

    return _ParsedUvLock(
        groups={name: tuple(records) for name, records in groups.items()}
    )


def _validate_package_record(
    raw_record: object,
    *,
    side: Literal["base", "head"],
    index: int,
) -> _UvPackageRecord | str:
    """Validate one package table and project it into the internal comparison model.

    Local validation returns a string explanation because ``_parse_uv_lock`` owns the
    boundary that attaches shared typed problem semantics and exact source provenance.
    """

    if not isinstance(raw_record, Mapping):
        return f"The exact {side} uv.lock package record at index {index} was not a TOML table."

    # Validate before normalization so normalization cannot legitimize malformed source
    # spelling and turn it into trusted package identity.
    package = raw_record.get("name", _MISSING)
    if (
        not isinstance(package, str)
        or not package
        or package != package.strip()
        or _DISTRIBUTION_NAME_PATTERN.fullmatch(package) is None
    ):
        return (
            f"The exact {side} uv.lock package record at index {index} had an "
            f"invalid distribution name: {package!r}."
        )

    raw_version = raw_record.get("version", _MISSING)
    if raw_version is _MISSING:
        source = raw_record.get("source", _MISSING)
        # Editable/virtual workspace records can legitimately be versionless; broader
        # versionless shapes remain unsupported rather than being guessed into that model.
        if not _is_admitted_versionless_source(source):
            return (
                f"The exact {side} uv.lock package record at index {index} lacked "
                "a textual 'version' outside the admitted editable/virtual "
                "workspace-record boundary."
            )
        version: str | None = None
    elif (
        not isinstance(raw_version, str)
        or not raw_version
        or raw_version != raw_version.strip()
    ):
        return (
            f"The exact {side} uv.lock package record at index {index} had an "
            "invalid non-empty textual 'version'."
        )
    else:
        version = raw_version

    return _UvPackageRecord(
        package=package,
        normalized_package=normalize_package_name(package),
        version=version,
        record_data=raw_record,
    )


def _is_admitted_versionless_source(source: object) -> bool:
    """Recognize the narrow workspace-source shapes allowed without a version.

    Requiring exactly one admitted source key and one non-empty trimmed value prevents a
    broader or mixed source record from being silently treated as a known workspace shape.
    """

    if not isinstance(source, Mapping) or len(source) != 1:
        return False
    key, value = next(iter(source.items()))
    return (
        key in _VERSIONLESS_SOURCE_KEYS
        and isinstance(value, str)
        and bool(value)
        and value == value.strip()
    )


def _compare_uv_lock_packages(
    base: _ParsedUvLock,
    head: _ParsedUvLock,
    evidence: DependencyChangeSourceEvidence,
) -> DependencyChangeExtractionResult:
    """Compare parsed locks and require exactly one unambiguous version transition.

    Repeated universal-lock branches are accepted only when their complete canonical groups
    are unchanged. A successful result is still file-level extraction; PR-wide trust is
    established later by ``compare_extracted_dependency_changes(...)``.
    """

    # Inspect names from both revisions so additions/removals cannot disappear from the
    # comparison merely because they exist on only one side.
    all_names = sorted(set(base.groups) | set(head.groups))
    transitions: list[tuple[_UvPackageRecord, _UvPackageRecord]] = []

    for normalized_name in all_names:
        base_group = base.groups.get(normalized_name)
        head_group = head.groups.get(normalized_name)

        # Addition/removal is a structural event, not a clean in-place version transition
        # under this extractor's supported boundary.
        if base_group is None or head_group is None:
            return _problem(
                "unsupported_uv_lock_structural_change",
                (
                    f"Normalized package {normalized_name!r} was added or removed; "
                    "the first uv.lock rule supports only version transitions for "
                    "records present at both revisions."
                ),
                evidence,
            )

        if len(base_group) == 1 and len(head_group) == 1:
            comparison = _compare_single_record(base_group[0], head_group[0], evidence)
            if isinstance(comparison, DependencyChangeProblem):
                return comparison
            if comparison is not None:
                transitions.append(comparison)
            continue

        # Repeated records may represent different resolution branches. Pairing them by
        # position would invent correspondence, so changed repeated groups are ambiguous.
        if _canonical_group(base_group) != _canonical_group(head_group):
            return _problem(
                "ambiguous_uv_lock_package_records",
                (
                    f"Repeated uv.lock records for normalized package "
                    f"{normalized_name!r} changed across base and head. The first "
                    "boundary does not pair repeated resolution branches heuristically."
                ),
                evidence,
            )

    # Artifact-only churn or other non-transition changes must not manufacture a dependency
    # version change.
    if not transitions:
        return _problem(
            "version_unchanged",
            (
                "The admitted uv.lock files contained no exact package version "
                "transition after artifact-only differences were removed."
            ),
            evidence,
        )

    # The current dependency-change contract represents one package transition. Several
    # transitions therefore remain explicit ambiguity instead of choosing a likely package.
    if len(transitions) > 1:
        packages = ", ".join(
            sorted({head_record.normalized_package for _, head_record in transitions})
        )
        return _problem(
            "multiple_dependency_version_changes",
            (
                "The admitted uv.lock file established several package version "
                f"transitions ({packages}); B2 requires exactly one."
            ),
            evidence,
        )

    base_record, head_record = transitions[0]
    assert base_record.version is not None
    assert head_record.version is not None
    return ExtractedDependencyVersionChange(
        package=head_record.package,
        normalized_package=head_record.normalized_package,
        old_version=base_record.version,
        proposed_version=head_record.version,
        source_evidence=evidence,
    )


def _compare_single_record(
    base: _UvPackageRecord,
    head: _UvPackageRecord,
    evidence: DependencyChangeSourceEvidence,
) -> tuple[_UvPackageRecord, _UvPackageRecord] | DependencyChangeProblem | None:
    """Decide whether two records safely represent one package changing version.

    Return the pair for a clean textual version transition, ``None`` when no relevant
    transition occurred, or a typed problem when structural context makes that pairing
    unsafe.
    """

    # ``source`` and ``resolution-markers`` help identify what source/resolution branch a
    # record describes. If either changes, the base/head records may not represent the same
    # semantic package record, so treating the version strings as a simple transition would
    # manufacture correspondence.
    if (
        base.record_data.get("source", _MISSING)
        != head.record_data.get("source", _MISSING)
        or base.record_data.get("resolution-markers", _MISSING)
        != head.record_data.get("resolution-markers", _MISSING)
    ):
        return _problem(
            "unsupported_uv_lock_structural_change",
            (
                f"The source or resolution-marker context for normalized package "
                f"{base.normalized_package!r} changed across base and head."
            ),
            evidence,
        )

    # Versionless workspace records are not ordinary published-version records. Gaining or
    # losing a version—or changing their meaningful structure—is a different semantic event,
    # so this extractor abstains instead of coercing it into a version transition.
    if base.version is None or head.version is None:
        if base.version != head.version:
            return _problem(
                "unsupported_uv_lock_structural_change",
                (
                    f"Normalized package {base.normalized_package!r} gained or lost "
                    "an exact textual version across base and head."
                ),
                evidence,
            )
        if _canonical_record(base.record_data) != _canonical_record(head.record_data):
            return _problem(
                "unsupported_uv_lock_structural_change",
                (
                    f"Versionless workspace package {base.normalized_package!r} "
                    "changed non-artifact structure."
                ),
                evidence,
            )
        return None

    if base.version != head.version:
        return (base, head)

    # A same-version structural change is still semantically meaningful. Returning ``None``
    # here would erase evidence the narrow version-transition model cannot safely interpret.
    if _canonical_record(base.record_data) != _canonical_record(head.record_data):
        return _problem(
            "unsupported_uv_lock_structural_change",
            (
                f"Normalized package {base.normalized_package!r} kept version "
                f"{base.version!r} but changed non-artifact structure."
            ),
            evidence,
        )
    return None


def _canonical_group(records: tuple[_UvPackageRecord, ...]) -> Counter[object]:
    """Compare repeated records as a multiset instead of inventing positional pairing.

    Record order is irrelevant, while duplicate counts remain significant. Canonical,
    hashable record identities therefore let ``Counter`` distinguish a genuinely unchanged
    repeated branch set from one whose structure changed.
    """

    return Counter(_canonical_record(record.record_data) for record in records)


def _canonical_record(record: Mapping[str, Any]) -> object:
    """Return meaningful record structure while ignoring artifact download churn.

    The remaining nested TOML structure is frozen so repeated-record groups can be compared
    as hashable multisets.
    """

    return _freeze_toml_value(
        {key: value for key, value in record.items() if key not in _ARTIFACT_FIELDS}
    )


def _freeze_toml_value(value: object) -> object:
    """Build a deterministic hashable identity for nested TOML comparison.

    ``Counter`` cannot compare repeated package groups from mutable/unhashable TOML
    mappings and lists directly. Recursively freezing them preserves structure while making
    each canonical record usable as a multiset key; the result never becomes domain
    evidence or serialized TOML.
    """

    if isinstance(value, Mapping):
        return (
            "mapping",
            tuple(
                sorted(
                    (str(key), _freeze_toml_value(item))
                    for key, item in value.items()
                )
            ),
        )
    if isinstance(value, list):
        return ("list", tuple(_freeze_toml_value(item) for item in value))
    return (type(value).__qualname__, repr(value))


def _problem(
    reason: DependencyChangeProblemCode,
    detail: str,
    evidence: DependencyChangeSourceEvidence,
) -> DependencyChangeProblem:
    """Preserve exact source evidence when a later semantic check must stop."""

    return DependencyChangeProblem(
        reason=reason,
        detail=detail,
        source_evidence=(evidence,),
    )


__all__ = (
    "extract_uv_lock_changes",
    "is_modified_uv_lock_file",
)
