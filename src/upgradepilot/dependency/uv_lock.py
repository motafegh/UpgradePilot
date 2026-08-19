"""Interpret exact package-version changes in complete ``uv.lock`` files.

START HERE — NORMAL CALL PATH
-----------------------------
This file has two public functions with different roles:

``is_modified_uv_lock_file(...)``
    is the cheap pre-acquisition gate. ``dependency/analysis.py`` uses it after recognizing
    a changed path named ``uv.lock`` to decide whether exact base/head file content should
    be acquired.

``extract_uv_lock_changes(...)``
    is the primary semantic entry point. Start there when reading the implementation.
    ``dependency/analysis.py::analyze_dependency_change(...)`` calls it after
    ``github/repository.py::GitHubRepositoryClient`` has fetched exact base/head evidence.

Representative input shape
--------------------------
Only the relevant fields are shown here; the owning dataclasses contain more provenance:

``ChangedFile`` from ``github/pull_request.py``::

    ChangedFile(
        filename="uv.lock",
        status="modified",
        ...,
    )

Exact historical files from ``github/repository.py`` arrive independently for base/head::

    RepositoryTextFile(
        path="uv.lock",
        revision="<immutable Git SHA>",
        blob_sha="<Git blob SHA>",
        content="version = 1\nrevision = ...\n[[package]]\n...",
        ...,
    )

or, when acquisition cannot establish the text::

    UnavailableRepositoryFile(
        path="uv.lock",
        revision="<immutable Git SHA>",
        reason="...",
        detail="...",
        ...,
    )

Main internal data flow
-----------------------
The primary entry point is deliberately a guard-clause pipeline:

``ChangedFile + exact base/head file evidence``
    -> path/status admission
    -> exact-file availability check
    -> exact source/provenance binding
    -> parse complete base ``uv.lock``
    -> parse complete head ``uv.lock``
    -> validate/package-group records by normalized package identity
    -> compare base/head groups conservatively
    -> one file-level extraction result or one typed problem

Representative output shape
---------------------------
A supported change leaves this module as the source-independent contract owned by
``dependency/change.py``::

    ExtractedDependencyVersionChange(
        package="example-package",
        normalized_package="example-package",
        old_version="1.2.3",
        proposed_version="1.2.4",
        source_evidence=DependencyChangeSourceEvidence(...),
    )

Any normal evidence limitation leaves as::

    DependencyChangeProblem(
        reason="<closed problem code>",
        detail="...",
        source_evidence=(DependencyChangeSourceEvidence(...),),
    )

Where the result goes next
--------------------------
``dependency/analysis.py`` collects this file-level result alongside results from other
admitted dependency sources and passes them to
``dependency/change.py::compare_extracted_dependency_changes(...)``. Only that later
comparison may promote agreeing file-level evidence to one PR-wide
``DependencyVersionChange``. ``analysis.py`` then converts trusted provenance into source
contexts such as ``UvLockDependencyContext``.

Proof boundary
--------------
This module owns only:

``exact base/head uv.lock evidence -> one exact file-level package-version transition``

It does *not* decide whether the changed package belongs to a selected dependency
environment, whether CI installed or executed it, whether the lock is resolver-current,
or whether the upgrade is behaviorally compatible. Those stronger propositions belong to
later dependency/CI/product layers.
"""

from __future__ import annotations

# Core parsing/comparison mechanisms used by the pipeline above:
# - ``tomllib`` turns each exact lockfile text into TOML mappings/lists that this module can
#   validate against its bounded schema assumptions.
# - ``re`` implements the raw distribution-name admission rule before package-name
#   normalization is allowed to create a trusted comparison identity.
# - ``defaultdict`` groups validated records by normalized package name; ``Counter`` later
#   compares repeated records as an order-independent multiset instead of pairing by index.
import re
import tomllib
from collections import Counter, defaultdict
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, Literal

# Upstream evidence contracts. ``ChangedFile`` comes from PR changed-file acquisition;
# repository evidence comes from exact immutable-revision file acquisition.
from ..github.pull_request import ChangedFile
from ..github.repository import (
    ExactRepositoryFileEvidence,
    RepositoryTextFile,
    UnavailableRepositoryFile,
)

# Shared identity/path rules keep this extractor from inventing its own repository-path or
# package-normalization semantics.
from ..package_identity import normalize_package_name
from ..repository_path import repository_relative_parts

# Downstream source-independent contracts. This module fills these records; it does not own
# PR-wide consensus, environment membership, CI interpretation, or compatibility decisions.
from .change import (
    DependencyChangeExtractionResult,
    DependencyChangeProblem,
    DependencyChangeProblemCode,
    DependencyChangeSourceEvidence,
    ExtractedDependencyVersionChange,
)

# ``sdist`` is uv's source-distribution artifact entry and ``wheels`` contains built wheel
# artifact entries. URLs, hashes, sizes, upload metadata, or the available artifact list can
# change without changing the package name/version/dependency structure this *version-change*
# extractor is trying to identify. ``_canonical_record(...)`` therefore removes these two
# fields before structural comparison. This does not claim artifacts are unimportant; later
# artifact/target compatibility responsibilities may care about them independently.
_ARTIFACT_FIELDS = frozenset({"sdist", "wheels"})

# uv can record local project/workspace sources without a conventional textual package
# version. ``editable`` means the environment uses the local source directly so source edits
# are reflected without rebuilding a normal installed wheel. ``virtual`` means the local
# project/dependency itself is not installed as a package; only its dependencies participate.
# For this extractor, only exactly-one-key source mappings such as ``{"editable": "."}`` or
# ``{"virtual": "."}`` are admitted as known versionless shapes. Other versionless records
# remain unsupported instead of being guessed into one of these semantics.
_VERSIONLESS_SOURCE_KEYS = frozenset({"editable", "virtual"})

# Raw package-name admission rule used by ``_validate_package_record(...)`` *before*
# ``normalize_package_name(...)``. A full match accepts an ASCII letter/digit at both ends
# with letters/digits/``.``/``_``/``-`` in the interior. ``fullmatch(...) is None`` means
# reject the record; the regex does not normalize or transform the name. This prevents
# malformed source spelling (whitespace, leading/trailing punctuation, etc.) from becoming a
# trusted canonical package identity merely because normalization could produce one.
_DISTRIBUTION_NAME_PATTERN = re.compile(
    r"^[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?$"
)

# A unique sentinel distinguishes “the TOML key was absent” from “the key existed with a
# false-like value such as None/False/empty data”. Structural comparison needs that
# distinction, so callers test this object by identity rather than using a normal value.
_MISSING = object()


@dataclass(frozen=True, slots=True)
class _UvPackageRecord:
    """Validated internal shape for one ``[[package]]`` lock record.

    Input origin:
        ``_validate_package_record(...)`` projects one raw mapping from the parsed
        ``document["package"]`` list into this shape.

    Fields:
        ``package`` preserves lockfile spelling for diagnostics/output.
        ``normalized_package`` is the cross-source comparison identity.
        ``version`` is textual when present, or ``None`` only for the narrowly admitted
        editable/virtual versionless source shapes.
        ``record_data`` keeps the full validated mapping because source/marker and
        same-version structural changes cannot be judged from name/version alone.

    Next handoff:
        ``_parse_uv_lock(...)`` groups these records by ``normalized_package`` before the
        base/head comparison stage.
    """

    package: str
    normalized_package: str
    version: str | None
    record_data: Mapping[str, Any]


@dataclass(frozen=True, slots=True)
class _ParsedUvLock:
    """Validated lockfile projected into the shape needed for base/head comparison.

    ``groups`` maps one normalized distribution identity to every corresponding lock
    record. A universal lock can contain repeated records for one package under different
    resolution branches, so this model deliberately preserves all records without inventing
    positional pairing.

    Produced by:
        ``_parse_uv_lock(...)`` independently for base and head.

    Consumed by:
        ``_compare_uv_lock_packages(...)``.
    """

    groups: Mapping[str, tuple[_UvPackageRecord, ...]]


def is_modified_uv_lock_file(changed_file: ChangedFile) -> bool:
    """Return whether exact uv.lock acquisition should proceed for this changed file.

    Input:
        One validated ``ChangedFile`` produced by GitHub PR changed-file acquisition.
        This predicate reads only ``filename`` and ``status``.

    Output / next step:
        ``True`` only for an in-place modified repository-relative path whose basename is
        exactly lowercase ``uv.lock``. ``dependency/analysis.py`` uses that result to decide
        whether to fetch exact base/head file contents before calling
        ``extract_uv_lock_changes(...)``.
    """

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
    """Primary entry point: extract one safe file-level version transition.

    Normal caller:
        ``dependency/analysis.py::analyze_dependency_change(...)`` after exact base/head
        acquisition by ``GitHubRepositoryClient``.

    Inputs:
        ``changed_file`` identifies the PR path/status being interpreted.
        ``base_file`` and ``head_file`` are exact-revision evidence unions: each is either a
        ``RepositoryTextFile`` with complete UTF-8 content/provenance or an
        ``UnavailableRepositoryFile`` describing why that historical side could not be
        established.

    Transformation owned here:
        path/status admission -> availability -> provenance binding -> base parse -> head
        parse -> conservative package-record comparison.

    Output:
        ``ExtractedDependencyVersionChange`` for exactly one unambiguous textual version
        transition, otherwise a typed ``DependencyChangeProblem`` for a normal unsupported,
        malformed, unavailable, ambiguous, or unchanged evidence state.

    Next handoff:
        ``analysis.py`` passes the result to
        ``change.compare_extracted_dependency_changes(...)`` with other source-specific
        results. Success here is therefore file-level evidence, not PR-wide truth.
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

    # Each historical side is independent evidence. If either side is unavailable, parsing
    # only the other side would invite an invented transition, so unavailability is returned
    # as a normal evidence problem before any semantic comparison begins.
    unavailable = _first_unavailable_file(base_file, head_file)
    if unavailable is not None:
        return DependencyChangeProblem(
            reason="dependency_file_unavailable",
            detail=(
                f"Exact uv.lock text was unavailable at revision "
                f"{unavailable.revision!r}: {unavailable.detail}"
            ),
        )

    # ``ExactRepositoryFileEvidence`` is a union. The guard above removes the unavailable
    # branch, making complete ``RepositoryTextFile`` evidence the invariant for the rest of
    # this function.
    assert isinstance(base_file, RepositoryTextFile)
    assert isinstance(head_file, RepositoryTextFile)

    # Bind repository/path/revision/blob/byte provenance before parsing. This keeps any
    # later package-version statement attached to the exact historical bytes that support it.
    evidence_result = _build_source_evidence(changed_file, base_file, head_file)
    if isinstance(evidence_result, DependencyChangeProblem):
        return evidence_result
    evidence = evidence_result

    # Parse base and head independently into the same internal shape. The first malformed or
    # unsupported historical side stops the comparison rather than letting the other side
    # dominate the result.
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
    """Return unavailable evidence itself so the caller can preserve revision/detail."""

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
    """Bind the exact historical files into dependency-owned source provenance.

    Inputs:
        The PR ``ChangedFile`` plus already-available base/head ``RepositoryTextFile``
        objects. Their path, repository, revision, blob identity, and byte evidence must all
        coherently describe the same changed ``uv.lock``.

    Output:
        ``DependencyChangeSourceEvidence`` containing the exact base/head provenance, or an
        ``invalid_dependency_record`` problem when those identities cannot be trusted.

    Next handoff:
        The successful evidence object is passed into parsing/comparison and is attached to
        every later success/problem so source provenance survives this module.

    ``RepositoryTextFile`` still permits older/manual fixtures with optional strong
    provenance fields, so this boundary revalidates the identities it relies on rather than
    assuming every instance came from the runtime provider. Blob SHAs are provider-reported
    identities; this function does not recompute Git blob hashes from decoded content.
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

    # Reported byte count comes from provider metadata; decoded byte count comes from the
    # acquired content. Equality is an acquisition-consistency check, not a dependency
    # semantic claim, and both historical sides must satisfy it independently.
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
    """Convert one exact lockfile text into the internal comparison model.

    Input:
        One complete base *or* head ``RepositoryTextFile`` whose provenance has already
        passed ``_build_source_evidence(...)``. ``repository_file.content`` is the raw TOML
        text; ``side`` is only the diagnostic label identifying which historical revision
        is being parsed.

    Transformation:
        TOML parse -> schema/revision checks -> ``package`` list validation -> per-record
        validation -> grouping by normalized package identity.

    Output / next handoff:
        ``_ParsedUvLock(groups={normalized_name: (...)})`` for comparison by
        ``_compare_uv_lock_packages(...)``, or a typed ``DependencyChangeProblem`` carrying
        the already-bound source evidence.

    This deliberately does not reproduce uv's resolver. The lock document's top-level
    ``revision`` is uv-format metadata, not the Git revision carried by
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

    # uv version-controls the lockfile schema. This extractor was written against schema 1;
    # a newer schema can change field meaning, so interpreting it with schema-1 assumptions
    # would manufacture confidence rather than provide backward compatibility.
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

    # ``revision`` is uv's backwards-compatible lock-format revision counter. It is checked
    # for valid shape here but is not confused with the immutable Git revision in the input
    # evidence.
    revision = document.get("revision", _MISSING)
    if type(revision) is not int or revision < 0:
        return _problem(
            "malformed_dependency_file",
            f"The exact {side} uv.lock field 'revision' must be a non-negative integer.",
            evidence,
        )

    # In TOML, repeated ``[[package]]`` tables parse as a Python list of mappings under the
    # top-level ``package`` key. This list is the raw package-record input for the next stage.
    raw_packages = document.get("package", _MISSING)
    if not isinstance(raw_packages, list):
        return _problem(
            "invalid_dependency_record",
            f"The exact {side} uv.lock field 'package' must be an array of tables.",
            evidence,
        )

    # Normalize names for cross-source identity, but retain *every* record belonging to one
    # normalized name. A universal lock may contain several resolution branches for the same
    # package; silently keeping one or pairing them by list position would destroy ambiguity.
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
    """Validate/project one raw ``[[package]]`` table for later comparison.

    Input:
        One item from the parsed lockfile's top-level ``package`` list. The normal shape is
        a mapping such as ``{"name": "requests", "version": "2.32.5", "source": {...}}``.

    Output:
        ``_UvPackageRecord`` when the record fits this extractor's supported boundary, or a
        local explanatory string when the record is invalid/unsupported. ``_parse_uv_lock``
        owns conversion of that local explanation into the shared typed problem carrying
        exact source provenance.

    Important projection:
        Raw spelling is validated before normalization; a missing version is accepted only
        for the narrowly defined editable/virtual local-source shapes.
    """

    if not isinstance(raw_record, Mapping):
        return f"The exact {side} uv.lock package record at index {index} was not a TOML table."

    # ``fullmatch`` must accept the entire raw spelling before normalization. Otherwise a
    # malformed value could be “cleaned up” into a trusted normalized identity and obscure
    # that the source evidence itself was invalid.
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
        # A versionless record is not automatically a workspace record. Require the exact
        # admitted source mapping so missing version data from another source kind cannot be
        # silently interpreted as a legitimate editable/virtual package shape.
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
    """Return whether a ``source`` mapping is one admitted versionless local shape.

    Input examples:
        ``{"editable": "."}`` — local source is used in editable form.
        ``{"virtual": "."}`` — local project is not installed; only dependencies matter.

    Output / use:
        ``True`` only when the mapping contains exactly one admitted key and one non-empty,
        already-trimmed string value. ``_validate_package_record(...)`` uses this Boolean to
        decide whether an absent textual ``version`` is legitimate or must become an
        ``invalid_dependency_record`` problem.

    Requiring exactly one known key prevents mixed/broader source records from being silently
    collapsed into the narrow workspace model understood by this extractor.
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
    """Compare parsed base/head locks and require exactly one safe transition.

    Inputs:
        Two ``_ParsedUvLock`` values produced independently from the exact base/head files,
        plus their shared exact source provenance.

    Comparison model:
        inspect the union of normalized package names -> reject add/remove structural events
        -> compare single-record packages directly -> compare repeated-record groups only as
        complete canonical multisets -> collect textual version transitions.

    Output:
        Exactly one collected transition becomes ``ExtractedDependencyVersionChange``.
        Zero transitions, several transitions, changed repeated branches, or unsupported
        structural events become typed ``DependencyChangeProblem`` results.

    Next handoff:
        The caller ``extract_uv_lock_changes(...)`` returns this file-level result to
        ``dependency/analysis.py``; PR-wide trust is established only later by
        ``compare_extracted_dependency_changes(...)``.
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

        # Repeated records can represent distinct marker/resolution branches in uv's
        # universal lock. Position is not semantic identity, so a changed repeated group is
        # ambiguous unless the complete canonical multisets remain equal.
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

    # Artifact-only churn or other changes that do not establish a textual version
    # transition must not manufacture a dependency-version change.
    if not transitions:
        return _problem(
            "version_unchanged",
            (
                "The admitted uv.lock files contained no exact package version "
                "transition after artifact-only differences were removed."
            ),
            evidence,
        )

    # The shared dependency-change contract represents one package transition. If this one
    # lockfile changes several packages, this extractor preserves that ambiguity instead of
    # choosing the package that looks most likely to matter.
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
    """Classify one base/head record pair for the same normalized package.

    Caller/input:
        ``_compare_uv_lock_packages(...)`` calls this only when exactly one base record and
        one head record exist for a normalized package, so no repeated-branch pairing is
        required here.

    Output:
        ``(base, head)`` means one clean textual version transition was established.
        ``None`` means no relevant transition occurred.
        ``DependencyChangeProblem`` means source/marker/versionless/structural context makes
        a simple version pairing unsafe.
    """

    # ``source`` identifies where uv resolves this package from; ``resolution-markers``
    # delimit the resolution context represented by the record. If either changes, the two
    # records may no longer represent the same semantic branch, so comparing only their
    # version strings would manufacture base/head correspondence.
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

    # Versionless editable/virtual records are local-source structure, not ordinary
    # published-version evidence. Gaining/losing a version or changing meaningful structure
    # is therefore a different semantic event, not a normal version transition.
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

    # Keeping the same version does not make all structural change irrelevant. If meaningful
    # non-artifact structure changed, returning ``None`` would erase evidence outside this
    # extractor's narrow version-transition model.
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
    """Turn repeated records into an order-independent multiset for equality checks.

    Input/output:
        A tuple of repeated records becomes ``Counter({canonical_record: count, ...})``.
        Record order is discarded because list position is not trusted branch identity;
        duplicate counts are retained because two identical records are not the same shape
        as one identical record.

    Used by:
        ``_compare_uv_lock_packages(...)`` to accept a repeated package group only when the
        entire meaningful group is unchanged across base/head.
    """

    return Counter(_canonical_record(record.record_data) for record in records)


def _canonical_record(record: Mapping[str, Any]) -> object:
    """Build meaningful structural identity while excluding artifact-download churn.

    ``sdist``/``wheels`` are removed according to ``_ARTIFACT_FIELDS``; the remaining TOML
    mapping is recursively frozen by ``_freeze_toml_value(...)`` so it can participate in
    hashable multiset comparison.
    """

    return _freeze_toml_value(
        {key: value for key, value in record.items() if key not in _ARTIFACT_FIELDS}
    )


def _freeze_toml_value(value: object) -> object:
    """Convert nested TOML data into a deterministic hashable comparison identity.

    Why this exists:
        Parsed TOML mappings/lists are mutable and unhashable, so ``Counter`` cannot use a
        whole package record directly as a multiset key.

    Transformation:
        mappings -> tagged sorted tuples of key/frozen-value pairs;
        lists -> tagged tuples preserving list order;
        scalars -> tagged ``(type-name, repr(value))`` pairs.

    Output boundary:
        The frozen object exists only for internal structural equality/hashing. It is not
        serialized TOML, package evidence, or a stronger domain claim.
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
    """Attach the already-validated exact source provenance to one stopping result."""

    return DependencyChangeProblem(
        reason=reason,
        detail=detail,
        source_evidence=(evidence,),
    )


__all__ = (
    "extract_uv_lock_changes",
    "is_modified_uv_lock_file",
)