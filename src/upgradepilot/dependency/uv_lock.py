"""Interpret exact package-version changes in complete ``uv.lock`` files.

RESPONSIBILITY
--------------
This module owns one narrow source-specific question:

``exact base/head uv.lock evidence -> one exact file-level package-version transition``

It validates the changed-file shape, binds exact GitHub file provenance, parses the two
complete lockfiles, projects package records into a comparison model, and either returns one
safe file-level transition or an explicit stopping problem. It does *not* decide dependency
environment membership, CI installation/execution, resolver currentness, or behavioral
compatibility; those stronger claims belong to later dependency/CI/product layers.

UPSTREAM / INPUT ORIGIN
-----------------------
The normal caller is ``dependency/analysis.py::analyze_dependency_change(...)``.
``github/pull_request.py`` owns the ``ChangedFile`` input type. After the PR file list shows
a changed path named ``uv.lock``, ``analysis.py`` uses this module's admission predicate and
then asks ``github/repository.py::GitHubRepositoryClient`` for exact base/head file evidence.
``github/repository.py`` owns ``ExactRepositoryFileEvidence``, whose real states are:

``RepositoryTextFile``
    acquisition succeeded and complete UTF-8 text plus immutable-revision provenance exists;

``UnavailableRepositoryFile``
    exact acquisition could not establish that historical file, so unavailability itself is
    preserved as a normal evidence state rather than converted into an exception or guess.

PUBLIC API — START HERE
-----------------------
This module exports two *current* public functions with different responsibilities:

``extract_uv_lock_changes(...)``
    PRIMARY SEMANTIC ENTRY POINT. Start here when reading the implementation. It receives the
    changed-file record plus exact base/head evidence and owns the complete extraction
    pipeline described below.

``is_modified_uv_lock_file(...)``
    AUXILIARY ADMISSION GATE. ``analysis.py`` uses it before expensive exact-file acquisition
    to decide whether this changed-file shape is eligible for the current uv-lock rule.

There is no legacy/transitional public API in this module at present.

INPUT SHAPES
------------
Only fields material to this module are shown; the owning dataclasses retain more metadata.

``ChangedFile`` from ``github/pull_request.py``::

    ChangedFile(
        filename="uv.lock",
        status="modified",
        ...,
    )

Each historical side from ``github/repository.py`` is independently either::

    RepositoryTextFile(
        path="uv.lock",
        revision="<immutable Git commit SHA>",
        blob_sha="<Git blob SHA>",
        content="version = 1\nrevision = ...\n[[package]]\n...",
        ...,
    )

or::

    UnavailableRepositoryFile(
        path="uv.lock",
        revision="<immutable Git commit SHA>",
        reason="...",
        detail="...",
        ...,
    )

INTERNAL PIPELINE
-----------------
The primary entry point is a guard-clause proof pipeline. Passing each important gate earns
permission for the next stage to assume more, while failure returns an explicit evidence
problem instead of guessing:

``ChangedFile + exact base/head file evidence``
    -> path admission
       permits treating the changed path as the supported ``uv.lock`` target
    -> status admission
       permits in-place base/head comparison semantics
    -> exact-file availability
       permits treating both evidence values as complete ``RepositoryTextFile`` objects
    -> provenance validation
       permits the acquired bytes to support semantic parsing
    -> parse/validate base lock
       permits schema-1 package-record interpretation for base
    -> parse/validate head lock
       permits schema-1 package-record interpretation for head
    -> group records by normalized package identity
    -> compare base/head groups conservatively
    -> one file-level extraction result or one typed stopping problem

OUTPUT / PROBLEM STATES
-----------------------
``dependency/change.py`` owns the source-independent output contracts used here.
A supported change leaves as::

    ExtractedDependencyVersionChange(
        package="example-package",
        normalized_package="example-package",
        old_version="1.2.3",
        proposed_version="1.2.4",
        source_evidence=DependencyChangeSourceEvidence(...),
    )

A normal evidence limitation leaves as::

    DependencyChangeProblem(
        reason="<closed problem code>",
        detail="...",
        source_evidence=(DependencyChangeSourceEvidence(...),),
    )

``DependencyChangeExtractionResult`` is therefore a source-independent union of those two
real outcomes: successful file-level extraction or an explicit problem that blocks trust.

DOWNSTREAM
----------
``dependency/analysis.py`` collects this result alongside other admitted dependency-source
results and passes them to
``dependency/change.py::compare_extracted_dependency_changes(...)``. Only that later
consensus boundary may promote agreeing file-level evidence to a PR-wide
``DependencyVersionChange``. ``analysis.py`` then translates trusted provenance into
source contexts such as ``UvLockDependencyContext`` for later environment reasoning.

PROOF BOUNDARY
--------------
Success here proves only one exact textual package-version transition in the admitted
base/head ``uv.lock`` evidence. It does not prove that a selected environment contains the
package, that CI installed or exercised it, that the lock is resolver-current, or that the
upgrade is compatible/safe.
"""

from __future__ import annotations

# Core parsing/comparison mechanisms used by the pipeline above:
# - ``tomllib`` turns exact lockfile text into TOML mappings/lists for bounded validation.
# - ``re`` implements raw distribution-name admission before normalization may create a
#   trusted package identity.
# - ``defaultdict`` groups validated records by normalized package name; ``Counter`` later
#   compares repeated records as an order-independent multiset instead of pairing by index.
# - ``Mapping`` describes TOML-table-like inputs without requiring one concrete dict type;
#   ``Literal["base", "head"]`` constrains the internal historical-side label to the only
#   two states this comparison understands.
import re
import tomllib
from collections import Counter, defaultdict
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, Literal

# Upstream evidence contracts. ``github/pull_request.py`` owns ``ChangedFile``;
# ``github/repository.py`` owns the exact-file success/unavailability evidence union.
from ..github.pull_request import ChangedFile
from ..github.repository import (
    ExactRepositoryFileEvidence,
    RepositoryTextFile,
    UnavailableRepositoryFile,
)

# Shared identity/path rules keep this extractor from inventing independent repository-path
# or package-normalization semantics.
from ..package_identity import normalize_package_name
from ..repository_path import repository_relative_parts

# ``dependency/change.py`` owns these source-independent success/problem contracts. This
# module fills them but does not own PR-wide consensus or later environment/CI conclusions.
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
# extractor is trying to identify. ``_canonical_record(...)`` removes these two fields before
# structural equality checks. This does not claim artifacts are irrelevant globally; later
# artifact/target compatibility responsibilities may care about them independently.
_ARTIFACT_FIELDS = frozenset({"sdist", "wheels"})

# uv can record local project/workspace sources without a conventional textual package
# version. ``editable`` means the environment uses local source directly so source edits are
# reflected without rebuilding a normal installed wheel. ``virtual`` means the local project
# itself is not installed as a package; only its dependencies participate. This extractor
# admits only exactly-one-key source mappings such as ``{"editable": "."}`` or
# ``{"virtual": "."}`` as known versionless shapes. Other versionless records remain
# unsupported instead of being guessed into one of these semantics.
_VERSIONLESS_SOURCE_KEYS = frozenset({"editable", "virtual"})

# Raw package-name admission rule used by ``_validate_package_record(...)`` *before*
# ``normalize_package_name(...)``. A full match accepts an ASCII letter/digit at both ends
# with letters/digits/``.``/``_``/``-`` in the interior. The regex returns a match object or
# no match; it does not transform the name. No match means the record is rejected before
# canonical package identity can be trusted, preventing malformed source spelling from being
# silently legitimized by normalization.
_DISTRIBUTION_NAME_PATTERN = re.compile(
    r"^[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?$"
)

# A unique sentinel distinguishes “the TOML key was absent” from “the key existed with a
# false-like value”. That absence/presence distinction participates in structural decisions,
# so callers test this object by identity rather than substituting a normal data value.
_MISSING = object()


# ---------------------------------------------------------------------------
# Internal comparison models
# ---------------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class _UvPackageRecord:
    """Validated internal shape for one parsed ``[[package]]`` lock record.

    Produced by:
        ``_validate_package_record(...)`` from one item in parsed ``document["package"]``.

    Fields:
        ``package`` preserves lockfile spelling for diagnostics/output.
        ``normalized_package`` is the comparison identity shared with other dependency
        sources.
        ``version`` is a non-empty textual version for ordinary versioned records, or
        ``None`` only after the source has passed the narrow editable/virtual versionless
        admission rule. ``None`` therefore means a specific admitted source state, not
        “version parsing failed”.
        ``record_data`` preserves the complete raw TOML table because source/marker and
        same-version structural changes cannot be judged from name/version alone.

    Consumed by:
        ``_parse_uv_lock(...)`` groups records by normalized package; comparison helpers then
        inspect those groups without losing repeated lock branches.
    """

    package: str
    normalized_package: str
    version: str | None
    record_data: Mapping[str, Any]


@dataclass(frozen=True, slots=True)
class _ParsedUvLock:
    """Validated lockfile projected into the shape needed for base/head comparison.

    ``groups`` maps one normalized distribution identity to every corresponding lock record.
    A universal lock can contain repeated records for one package under different resolution
    branches, so this model preserves all records without inventing positional pairing.

    Produced by:
        ``_parse_uv_lock(...)`` independently for base and head after the respective file has
        passed syntax/schema/record validation.

    Consumed by:
        ``_compare_uv_lock_packages(...)``.
    """

    groups: Mapping[str, tuple[_UvPackageRecord, ...]]


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def is_modified_uv_lock_file(changed_file: ChangedFile) -> bool:
    """Auxiliary gate: decide whether exact uv.lock acquisition should proceed.

    Input ownership/origin:
        ``github/pull_request.py`` owns ``ChangedFile``; GitHub changed-file acquisition
        creates it. This predicate reads only ``filename`` and ``status``.

    Output / permission:
        ``True`` only for an in-place modified repository-relative path whose basename is
        exactly lowercase ``uv.lock``. ``dependency/analysis.py`` uses ``True`` as permission
        to acquire exact base/head contents before the primary semantic entry point runs.
        ``False`` means this helper does not admit the file shape; it makes no statement
        about dependency behavior.
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
    """Primary semantic entry point: extract one safe file-level version transition.

    Normal caller:
        ``dependency/analysis.py::analyze_dependency_change(...)`` after exact base/head
        acquisition by ``GitHubRepositoryClient``.

    Input ownership/states:
        ``github/pull_request.py`` owns ``ChangedFile``.
        ``github/repository.py`` owns ``ExactRepositoryFileEvidence``. Each historical side
        is either ``RepositoryTextFile`` (complete content/provenance available) or
        ``UnavailableRepositoryFile`` (typed acquisition failure). Treating both as normal
        evidence states is why unavailability is handled by a guard rather than an exception.

    Transformation:
        path admission -> status admission -> availability narrowing -> provenance binding
        -> base parse -> head parse -> conservative package-record comparison.

    Output ownership/states:
        ``dependency/change.py`` owns ``DependencyChangeExtractionResult``:
        ``ExtractedDependencyVersionChange`` for exactly one unambiguous textual version
        transition, otherwise ``DependencyChangeProblem`` for a normal unsupported,
        malformed, unavailable, ambiguous, or unchanged evidence state.

    Next handoff:
        ``analysis.py`` passes this file-level result to
        ``change.compare_extracted_dependency_changes(...)`` with other source-specific
        results. Success here is not yet PR-wide truth.
    """

    parts = repository_relative_parts(changed_file.filename)

    # Gate 1 — path admission. Failure means this is not the supported uv.lock source at
    # all. Passing permits the rest of the function to treat the changed path as the exact
    # lockfile target whose base/head evidence should be interpreted together.
    if parts is None or parts[-1] != "uv.lock":
        return DependencyChangeProblem(
            reason="no_supported_dependency_file",
            detail=(
                f"Path {changed_file.filename!r} is not an admitted normalized "
                "repository-relative file whose basename is exactly 'uv.lock'."
            ),
        )

    # Gate 2 — change-shape admission. Addition/deletion/rename needs different evidence
    # semantics from comparing one lockfile in place. Passing ``status == 'modified'`` earns
    # permission to interpret base/head as two revisions of the same repository path.
    if changed_file.status != "modified":
        return DependencyChangeProblem(
            reason="unsupported_dependency_file_status",
            detail=(
                f"The uv.lock file status was {changed_file.status!r}; the first "
                "structured-lockfile rule supports only an in-place modified file."
            ),
        )

    # Gate 3 — historical availability. ``ExactRepositoryFileEvidence`` is a real-state
    # union: complete text or explicit unavailability. If either side is unavailable, parsing
    # the other would invite an invented transition. Passing this gate removes the
    # unavailability branch and permits both values to be narrowed to ``RepositoryTextFile``.
    unavailable = _first_unavailable_file(base_file, head_file)
    if unavailable is not None:
        return DependencyChangeProblem(
            reason="dependency_file_unavailable",
            detail=(
                f"Exact uv.lock text was unavailable at revision "
                f"{unavailable.revision!r}: {unavailable.detail}"
            ),
        )

    assert isinstance(base_file, RepositoryTextFile)
    assert isinstance(head_file, RepositoryTextFile)

    # Gate 4 — exact provenance coherence. A successful evidence record means repository,
    # path, immutable Git revisions, blob identities, and byte counts coherently describe the
    # two historical files. Only after that may their text support semantic parsing.
    evidence_result = _build_source_evidence(changed_file, base_file, head_file)
    if isinstance(evidence_result, DependencyChangeProblem):
        return evidence_result
    evidence = evidence_result

    # Gates 5/6 — parse each historical side independently. ``side`` is restricted to
    # ``Literal["base", "head"]`` because these are the only historical roles this pipeline
    # understands. A successful parse yields ``_ParsedUvLock`` and permits semantic
    # comparison; a malformed/unsupported side blocks the pair rather than letting the other
    # side dominate.
    base_result = _parse_uv_lock(base_file, evidence, side="base")
    if isinstance(base_result, DependencyChangeProblem):
        return base_result

    head_result = _parse_uv_lock(head_file, evidence, side="head")
    if isinstance(head_result, DependencyChangeProblem):
        return head_result

    return _compare_uv_lock_packages(base_result, head_result, evidence)


# ---------------------------------------------------------------------------
# Evidence availability and provenance validation
# ---------------------------------------------------------------------------


def _first_unavailable_file(
    base_file: ExactRepositoryFileEvidence,
    head_file: ExactRepositoryFileEvidence,
) -> UnavailableRepositoryFile | None:
    """Return the first unavailable historical side, otherwise ``None``.

    ``ExactRepositoryFileEvidence`` is owned by ``github/repository.py`` and represents
    either successful exact text acquisition or typed unavailability. The primary entry
    point uses this helper to narrow both values before any semantic parsing. Returning the
    evidence object itself preserves the exact revision/detail needed for the stopping result.
    """

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
        The PR ``ChangedFile`` plus base/head ``RepositoryTextFile`` values that have already
        passed the availability gate. Their path, repository, immutable Git revision, blob
        identity, and byte evidence must coherently describe the same changed ``uv.lock``.

    Output ownership/permission:
        ``dependency/change.py`` owns ``DependencyChangeSourceEvidence`` and
        ``DependencyChangeProblem``. Success binds the historical bytes to one provenance
        record and permits later parsing/comparison to make claims supported by those exact
        bytes. Failure prevents semantic interpretation from becoming detached from source
        identity.

    ``RepositoryTextFile`` permits older/manual fixtures with optional strong provenance
    fields, so this boundary revalidates the identities it relies on rather than assuming
    every instance came from the runtime provider. Blob SHAs are provider-reported identities;
    this function does not recompute Git blob hashes from decoded content.
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

    # Git commit revision versus uv-lock revision: ``repository_file.revision`` below is the
    # immutable Git commit SHA from the acquisition layer. It is unrelated to the top-level
    # integer ``revision`` field parsed later from uv.lock itself.
    #
    # Reported byte count comes from provider metadata; decoded byte count comes from the
    # acquired content. Equality is acquisition-consistency evidence, not a dependency
    # semantic claim. Passing these checks permits the exact bytes to support later parsing.
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


# ---------------------------------------------------------------------------
# Parsing and package-record validation
# ---------------------------------------------------------------------------


def _parse_uv_lock(
    repository_file: RepositoryTextFile,
    evidence: DependencyChangeSourceEvidence,
    *,
    side: Literal["base", "head"],
) -> _ParsedUvLock | DependencyChangeProblem:
    """Convert one exact lockfile text into the internal comparison model.

    Inputs:
        One complete base *or* head ``RepositoryTextFile`` whose provenance already passed
        ``_build_source_evidence(...)``; the shared ``DependencyChangeSourceEvidence``;
        and ``side: Literal["base", "head"]``. The Literal expresses a domain invariant:
        this helper parses exactly one of the two historical PR sides, never an arbitrary
        label/state.

    Transformation:
        TOML parse -> schema/version-shape checks -> ``package`` list admission -> per-record
        validation -> grouping by normalized package identity.

    Output / next permission:
        ``_ParsedUvLock`` means the side fits the bounded schema/record model and may enter
        base/head semantic comparison. A ``DependencyChangeProblem`` means this historical
        side cannot safely support that next stage.

    Terminology collision:
        ``RepositoryTextFile.revision`` is an immutable **Git commit revision/SHA**. The
        top-level ``uv.lock`` field named ``revision`` is uv's **lock-format revision**. They
        are unrelated despite sharing the word “revision”.
    """

    try:
        document = tomllib.loads(repository_file.content)
    except tomllib.TOMLDecodeError as exc:
        return _problem(
            "malformed_dependency_file",
            f"The exact {side} uv.lock file was not valid TOML: {exc}.",
            evidence,
        )

    # Gate — schema version. The top-level ``version`` here is the uv.lock *schema version*,
    # not a package version. This extractor is defined only for schema 1. Passing the gate
    # permits later fields to be interpreted using schema-1 meaning; a newer schema may change
    # those meanings, so guessing would create false confidence.
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

    # Gate — uv lock-format revision shape. This integer is uv metadata, not the Git commit
    # revision attached to ``repository_file``. Passing only establishes that the field has
    # the supported basic shape; this extractor does not derive package semantics from its
    # numeric value.
    revision = document.get("revision", _MISSING)
    if type(revision) is not int or revision < 0:
        return _problem(
            "malformed_dependency_file",
            f"The exact {side} uv.lock field 'revision' must be a non-negative integer.",
            evidence,
        )

    # Gate — package collection shape. Repeated TOML ``[[package]]`` tables parse as a Python
    # list under the top-level ``package`` key. Passing this gate permits safe iteration over
    # package records; it does not yet make any individual record trustworthy.
    raw_packages = document.get("package", _MISSING)
    if not isinstance(raw_packages, list):
        return _problem(
            "invalid_dependency_record",
            f"The exact {side} uv.lock field 'package' must be an array of tables.",
            evidence,
        )

    # ``defaultdict`` is used here because one normalized package may have several lock
    # records. Appending every validated record preserves universal-lock branch ambiguity;
    # silently keeping one record would lose evidence. Successful record validation permits
    # each result to enter the grouped internal comparison model.
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

    Caller/input:
        ``_parse_uv_lock(...)`` passes one item from the parsed top-level package list. The
        ordinary shape is a mapping such as
        ``{"name": "requests", "version": "2.32.5", "source": {...}}``.

    Output contract:
        ``_UvPackageRecord`` means the record fits this extractor's supported local model and
        may be grouped/compared. A string is an intentionally *local* validation explanation;
        ``_parse_uv_lock(...)`` owns conversion into the shared typed problem because it also
        owns exact source provenance.

    Important projection:
        Raw distribution spelling must pass admission before normalization. ``version`` may
        become ``None`` only after the record proves it is one narrow editable/virtual local
        source shape; optionality therefore carries domain meaning rather than uncertainty.
    """

    if not isinstance(raw_record, Mapping):
        return f"The exact {side} uv.lock package record at index {index} was not a TOML table."

    # Gate — raw distribution identity. ``fullmatch`` must accept the entire spelling before
    # normalization. Passing permits ``normalize_package_name(...)`` later to create a trusted
    # canonical comparison identity; failure prevents malformed source text from being
    # “cleaned up” into apparent validity.
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

        # Gate — versionless-source admission. A missing version is not automatically a
        # workspace record. Passing ``_is_admitted_versionless_source`` authorizes the
        # internal ``version = None`` state to mean “recognized editable/virtual source”;
        # failure means absent version data is unsupported rather than guessed.
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
    """Return whether ``source`` is one admitted versionless local-source shape.

    Input examples:
        ``{"editable": "."}`` — local source is used in editable form.
        ``{"virtual": "."}`` — local project is not installed; only dependencies matter.

    Output / permission:
        ``True`` only when the mapping contains exactly one admitted key and one non-empty,
        already-trimmed string value. ``_validate_package_record(...)`` treats ``True`` as
        permission for an absent textual version to become the meaningful internal
        ``version=None`` state. ``False`` blocks that interpretation.

    Requiring exactly one known key prevents mixed/broader source records from being silently
    collapsed into the narrow workspace model this extractor understands.
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


# ---------------------------------------------------------------------------
# Base/head semantic comparison
# ---------------------------------------------------------------------------


def _compare_uv_lock_packages(
    base: _ParsedUvLock,
    head: _ParsedUvLock,
    evidence: DependencyChangeSourceEvidence,
) -> DependencyChangeExtractionResult:
    """Compare parsed base/head locks and require exactly one safe transition.

    Inputs:
        Two ``_ParsedUvLock`` values whose respective files already passed exact provenance,
        TOML/schema, and package-record validation, plus their shared source evidence.

    Comparison model:
        inspect the union of normalized package names -> reject add/remove structural events
        -> compare single-record packages directly -> compare repeated-record groups only as
        complete canonical multisets -> collect textual version transitions.

    Output ownership/states:
        ``dependency/change.py`` owns ``DependencyChangeExtractionResult``. Exactly one
        collected transition becomes ``ExtractedDependencyVersionChange``. Zero transitions,
        several transitions, changed repeated branches, or unsupported structure become
        ``DependencyChangeProblem``.

    Next handoff:
        ``extract_uv_lock_changes(...)`` returns this file-level result to ``analysis.py``;
        PR-wide trust is established only later by ``compare_extracted_dependency_changes``.
    """

    # Set union matters semantically here: inspecting names from *both* historical sides
    # prevents additions/removals from disappearing merely because one side lacks the key.
    # Sorting adds deterministic diagnostic/comparison order; it does not strengthen proof.
    all_names = sorted(set(base.groups) | set(head.groups))
    transitions: list[tuple[_UvPackageRecord, _UvPackageRecord]] = []

    for normalized_name in all_names:
        base_group = base.groups.get(normalized_name)
        head_group = head.groups.get(normalized_name)

        # Addition/removal is a structural event, not a clean in-place version transition.
        # Passing this gate establishes that both historical sides contain the package and
        # therefore permits record-to-record/group-to-group comparison.
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
        # universal lock. Position is not semantic identity. ``Counter``-backed canonical
        # multiset equality discards ordering while retaining duplicate counts. Equality
        # permits the unchanged repeated group to be ignored; inequality is ambiguous because
        # this extractor refuses to invent a base/head branch pairing.
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

    # The shared dependency-change contract requires an actual textual transition. Artifact
    # churn or otherwise unchanged semantic records do not earn permission to manufacture one.
    if not transitions:
        return _problem(
            "version_unchanged",
            (
                "The admitted uv.lock files contained no exact package version "
                "transition after artifact-only differences were removed."
            ),
            evidence,
        )

    # The shared contract represents one package transition. Passing this gate means exactly
    # one candidate remains and permits promotion to the file-level extracted result; several
    # candidates remain ambiguity rather than an invitation to choose the “likely” package.
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

    # A transition is appended only by ``_compare_single_record`` after both sides are proven
    # to be ordinary textual-version records. These assertions encode that internal invariant
    # for type narrowing; they are not additional runtime evidence checks.
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

    Caller/input permission:
        ``_compare_uv_lock_packages(...)`` calls this only after proving exactly one base
        record and one head record exist for the normalized package, so no repeated-branch
        pairing is required here.

    Output type semantics:
        ``(base, head)`` means one clean textual version transition was established and may
        be collected by the caller.
        ``None`` means this package contributes no relevant transition.
        ``DependencyChangeProblem`` means source/marker/versionless/structural context makes
        a simple version pairing unsafe and blocks the enclosing comparison.

    This three-way union expresses three real domain states; it is not incidental typing
    complexity.
    """

    # ``source`` identifies where uv resolves this package from; ``resolution-markers``
    # delimit the resolution context represented by the record. Passing equality permits the
    # two records to be treated as the same semantic branch for this narrow comparison. If
    # either changes, comparing only version strings would manufacture correspondence.
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

    # ``version is None`` has one admitted meaning here: recognized editable/virtual
    # local-source structure. Versionless records are therefore not ordinary published
    # version evidence. Gaining/losing a textual version or changing meaningful structure is
    # a different semantic event, not a normal package-version transition.
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

    # Same package version does not make every structural change irrelevant. Canonical
    # inequality here means meaningful non-artifact structure changed outside this module's
    # narrow version-transition model, so returning ``None`` would erase evidence.
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


# ---------------------------------------------------------------------------
# Canonicalization for structural comparison
# ---------------------------------------------------------------------------


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

    Semantic choice:
        ``sdist``/``wheels`` are removed according to ``_ARTIFACT_FIELDS`` because this
        package-version extractor intentionally ignores artifact-download churn. Every other
        record field is preserved for structural equality, so source/dependency/marker and
        other non-artifact differences remain visible.

    Next stage:
        ``_freeze_toml_value(...)`` turns the remaining nested TOML structure into a hashable
        identity usable by ``Counter``.
    """

    return _freeze_toml_value(
        {key: value for key, value in record.items() if key not in _ARTIFACT_FIELDS}
    )


def _freeze_toml_value(value: object) -> object:
    """Convert nested TOML data into a deterministic hashable comparison identity.

    Why this exists:
        Parsed TOML mappings/lists are mutable and unhashable, so ``Counter`` cannot use a
        whole package record directly as a multiset key.

    Transformation semantics:
        mappings -> tagged sorted tuples of key/frozen-value pairs. Mapping key order is not
        treated as semantic, so sorting removes representation-order noise;
        lists -> tagged tuples preserving list order because list sequence may be meaningful;
        scalars -> tagged ``(type-name, repr(value))`` pairs so values of different runtime
        types cannot collapse into the same identity accidentally.

    Output boundary:
        The frozen object exists only for internal structural equality/hashing. It is not
        serialized TOML, dependency evidence, or a stronger product claim.
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


# ---------------------------------------------------------------------------
# Problem construction and export surface
# ---------------------------------------------------------------------------


def _problem(
    reason: DependencyChangeProblemCode,
    detail: str,
    evidence: DependencyChangeSourceEvidence,
) -> DependencyChangeProblem:
    """Attach validated exact source provenance to one semantic stopping result.

    ``dependency/change.py`` owns the problem code/type. Helpers below the provenance gate
    use this constructor so an abstention never loses the exact source evidence already
    earned earlier in the pipeline.
    """

    return DependencyChangeProblem(
        reason=reason,
        detail=detail,
        source_evidence=(evidence,),
    )


# Current public surface. The primary semantic entry is listed first; the second export is
# the auxiliary pre-acquisition admission gate. No compatibility/legacy export is retained.
__all__ = (
    "extract_uv_lock_changes",
    "is_modified_uv_lock_file",
)