"""Extract exact version changes from ``pyproject.toml`` optional dependencies.

This module owns one deliberately bounded PEP 621 source rule: compare complete exact
base/head ``pyproject.toml`` files and establish at most one ``package==version`` change
inside one ``[project.optional-dependencies]`` extra. General unchanged PEP 508
requirements are allowed, but broader optional-dependency edits remain explicit problems.

``dependency/analysis.py`` owns admission of the changed-file role/status and exact
base/head acquisition from one PR identity. This extractor therefore consumes already-
admitted exact-file evidence; it does not re-prove PR repository/path binding or provider
transport invariants.

A pyproject file also owns abundant non-dependency metadata, so an unchanged optional-
dependency surface is a neutral result rather than a dependency error. The extracted
extra name is dependency-source evidence only; it does not say that a workflow selected
the extra, that an environment was formed, or that the dependency ran.
"""

from __future__ import annotations

import tomllib
from collections import Counter
from collections.abc import Mapping
from dataclasses import dataclass

from packaging.requirements import InvalidRequirement, Requirement

from ..github.pull_request import ChangedFile
from ..github.repository import (
    RepositoryFileEvidence,
    RepositoryTextFile,
    UnavailableRepositoryFile,
)
from ..package_identity import normalize_package_name
from ..repository_path import repository_relative_parts
from .change import (
    DependencyChangeProblem,
    DependencyChangeProblemCode,
    DependencyChangeSourceEvidence,
    ExtractedDependencyVersionChange,
)


@dataclass(frozen=True, slots=True)
class ExtractedPyprojectOptionalExtraChange:
    """One canonical file-level change plus its source-established optional extra."""

    change: ExtractedDependencyVersionChange
    extra: str


@dataclass(frozen=True, slots=True)
class PyprojectOptionalExtraNoChange:
    """Neutral result when exact optional-dependency content did not change.

    This is not evidence that the whole pyproject is unchanged and not evidence of
    dependency absence. It only prevents unrelated project metadata edits from becoming
    false dependency-analysis failures.
    """

    source_evidence: DependencyChangeSourceEvidence


type PyprojectOptionalExtraExtractionResult = (
    ExtractedPyprojectOptionalExtraChange
    | PyprojectOptionalExtraNoChange
    | DependencyChangeProblem
)


@dataclass(frozen=True, slots=True)
class _RequirementRecord:
    """Parsed requirement identity used only for conservative base/head comparison."""

    package: str
    normalized_package: str
    extras: tuple[str, ...]
    specifier: str
    marker: str | None
    url: str | None

    @property
    def comparison_key(self) -> tuple[object, ...]:
        return (
            self.normalized_package,
            self.extras,
            self.specifier,
            self.marker,
            self.url,
        )


@dataclass(frozen=True, slots=True)
class _ParsedOptionalDependencies:
    extras: Mapping[str, tuple[_RequirementRecord, ...]]


def is_modified_pyproject_file(changed_file: ChangedFile) -> bool:
    """Return whether this is an in-place modified exact ``pyproject.toml`` path."""

    parts = repository_relative_parts(changed_file.filename)
    return (
        changed_file.status == "modified"
        and parts is not None
        and parts[-1] == "pyproject.toml"
    )


def extract_pyproject_optional_extra_change(
    changed_file: ChangedFile,
    base_file: RepositoryFileEvidence,
    head_file: RepositoryFileEvidence,
) -> PyprojectOptionalExtraExtractionResult:
    """Establish one exact optional-extra pin transition from admitted exact files.

    The normal caller is ``dependency/analysis.py`` after ``is_modified_pyproject_file``
    admits the source and the repository provider acquires both historical sides from the
    same pull-request identity and requested path. This function owns availability plus
    pyproject parsing/comparison semantics, not repeated PR-binding validation.
    """

    unavailable = _first_unavailable_file(base_file, head_file)
    if unavailable is not None:
        return DependencyChangeProblem(
            reason="dependency_file_unavailable",
            detail=(
                f"Exact pyproject.toml text was unavailable at revision "
                f"{unavailable.revision!r}: {unavailable.detail}"
            ),
        )

    assert isinstance(base_file, RepositoryTextFile)
    assert isinstance(head_file, RepositoryTextFile)

    evidence = DependencyChangeSourceEvidence(
        path=changed_file.filename,
        file_format="pyproject_optional_extra",
        extraction_method="exact_base_head_files",
    )

    base_result = _parse_optional_dependencies(base_file, evidence, side="base")
    if isinstance(base_result, DependencyChangeProblem):
        return base_result
    head_result = _parse_optional_dependencies(head_file, evidence, side="head")
    if isinstance(head_result, DependencyChangeProblem):
        return head_result

    return _compare_optional_dependencies(base_result, head_result, evidence)


def _first_unavailable_file(
    base_file: RepositoryFileEvidence,
    head_file: RepositoryFileEvidence,
) -> UnavailableRepositoryFile | None:
    if isinstance(base_file, UnavailableRepositoryFile):
        return base_file
    if isinstance(head_file, UnavailableRepositoryFile):
        return head_file
    return None


def _parse_optional_dependencies(
    file: RepositoryTextFile,
    evidence: DependencyChangeSourceEvidence,
    *,
    side: str,
) -> _ParsedOptionalDependencies | DependencyChangeProblem:
    """Parse general unchanged PEP 508 entries without widening the change rule."""

    try:
        document = tomllib.loads(file.content)
    except tomllib.TOMLDecodeError as exc:
        return _problem(
            "malformed_dependency_file",
            f"The exact {side} pyproject.toml file was not valid TOML: {exc}.",
            evidence,
        )

    project = document.get("project")
    if project is None:
        return _ParsedOptionalDependencies(extras={})
    if not isinstance(project, Mapping):
        return _problem(
            "invalid_dependency_record",
            f"The exact {side} [project] value was present but was not a TOML table.",
            evidence,
        )

    optional = project.get("optional-dependencies")
    if optional is None:
        return _ParsedOptionalDependencies(extras={})
    if not isinstance(optional, Mapping):
        return _problem(
            "invalid_dependency_record",
            (
                f"The exact {side} [project.optional-dependencies] value was not a "
                "TOML table."
            ),
            evidence,
        )

    parsed: dict[str, tuple[_RequirementRecord, ...]] = {}
    for extra, raw_requirements in optional.items():
        if not isinstance(extra, str) or not extra or extra != extra.strip():
            return _problem(
                "invalid_dependency_record",
                f"The exact {side} optional-dependency extra name was invalid: {extra!r}.",
                evidence,
            )
        if not isinstance(raw_requirements, list) or not all(
            isinstance(item, str) for item in raw_requirements
        ):
            return _problem(
                "invalid_dependency_record",
                (
                    f"Optional extra {extra!r} in exact {side} pyproject.toml must be "
                    "an array of PEP 508 requirement strings."
                ),
                evidence,
            )

        records: list[_RequirementRecord] = []
        normalized_seen: set[str] = set()
        for index, raw_requirement in enumerate(raw_requirements):
            try:
                requirement = Requirement(raw_requirement)
            except InvalidRequirement as exc:
                return _problem(
                    "invalid_dependency_record",
                    (
                        f"Optional extra {extra!r} requirement at index {index} in "
                        f"exact {side} pyproject.toml was invalid: {exc}."
                    ),
                    evidence,
                )

            normalized = normalize_package_name(requirement.name)
            # Repeated declarations for one package can encode legitimate marker forks.
            # Pairing a changed record safely would require stronger marker-aware scope
            # semantics, so the first rule deliberately abstains instead of unioning them.
            if normalized in normalized_seen:
                return _problem(
                    "ambiguous_pyproject_dependency_records",
                    (
                        f"Optional extra {extra!r} in exact {side} pyproject.toml "
                        f"declared normalized package {normalized!r} more than once."
                    ),
                    evidence,
                )
            normalized_seen.add(normalized)

            records.append(
                _RequirementRecord(
                    package=requirement.name,
                    normalized_package=normalized,
                    extras=tuple(sorted(requirement.extras)),
                    specifier=str(requirement.specifier),
                    marker=str(requirement.marker) if requirement.marker is not None else None,
                    url=requirement.url,
                )
            )
        parsed[extra] = tuple(records)

    return _ParsedOptionalDependencies(extras=parsed)


def _compare_optional_dependencies(
    base: _ParsedOptionalDependencies,
    head: _ParsedOptionalDependencies,
    evidence: DependencyChangeSourceEvidence,
) -> PyprojectOptionalExtraExtractionResult:
    if set(base.extras) != set(head.extras):
        return _problem(
            "unsupported_pyproject_optional_dependency_change",
            (
                "Optional-extra names were added or removed; the first rule supports "
                "only one exact pin transition inside an extra present at both revisions."
            ),
            evidence,
        )

    removed: list[tuple[str, _RequirementRecord]] = []
    added: list[tuple[str, _RequirementRecord]] = []

    for extra in sorted(base.extras):
        base_by_key = {record.comparison_key: record for record in base.extras[extra]}
        head_by_key = {record.comparison_key: record for record in head.extras[extra]}

        base_counter = Counter(record.comparison_key for record in base.extras[extra])
        head_counter = Counter(record.comparison_key for record in head.extras[extra])

        for key, count in (base_counter - head_counter).items():
            removed.extend((extra, base_by_key[key]) for _ in range(count))
        for key, count in (head_counter - base_counter).items():
            added.extend((extra, head_by_key[key]) for _ in range(count))

    if not removed and not added:
        return PyprojectOptionalExtraNoChange(source_evidence=evidence)

    if len(removed) != 1 or len(added) != 1:
        return _problem(
            "multiple_dependency_version_changes",
            (
                "The first pyproject optional-extra rule requires exactly one removed "
                f"and one added requirement; observed {len(removed)} removed and "
                f"{len(added)} added records."
            ),
            evidence,
        )

    base_extra, old = removed[0]
    head_extra, new = added[0]
    if base_extra != head_extra:
        return _problem(
            "unsupported_pyproject_optional_dependency_change",
            (
                f"The removed requirement belonged to extra {base_extra!r} while the "
                f"added requirement belonged to {head_extra!r}; cross-extra moves are "
                "outside the first exact-transition rule."
            ),
            evidence,
        )

    if old.normalized_package != new.normalized_package:
        return _problem(
            "multiple_dependency_version_changes",
            (
                f"Removed package {old.package!r} and added package {new.package!r} "
                "do not identify the same normalized package."
            ),
            evidence,
        )

    if old.extras != new.extras or old.marker != new.marker or old.url != new.url:
        return _problem(
            "unsupported_pyproject_optional_dependency_change",
            (
                "The changed optional dependency also changed dependency extras, marker, "
                "or direct-reference identity; only an exact version pin may differ in "
                "the first rule."
            ),
            evidence,
        )

    if old.url is not None or new.url is not None:
        return _problem(
            "unsupported_pyproject_optional_dependency_change",
            "Direct URL/reference transitions are outside the first optional-extra rule.",
            evidence,
        )

    old_version = _single_exact_version(old.specifier)
    new_version = _single_exact_version(new.specifier)
    if old_version is None or new_version is None:
        return _problem(
            "unsupported_requirement_format",
            (
                "The changed optional dependency must use exactly one non-wildcard "
                "'==version' specifier on both base and head."
            ),
            evidence,
        )
    if old_version == new_version:
        return _problem(
            "version_unchanged",
            "The changed optional-dependency records specify the same exact version.",
            evidence,
        )

    change = ExtractedDependencyVersionChange(
        package=new.package,
        normalized_package=new.normalized_package,
        old_version=old_version,
        proposed_version=new_version,
        source_evidence=evidence,
    )
    return ExtractedPyprojectOptionalExtraChange(change=change, extra=head_extra)


def _single_exact_version(specifier_text: str) -> str | None:
    """Return one textual exact pin without silently accepting wildcard equality."""

    # Reparse through Requirement so exactness follows packaging's PEP 440 model rather
    # than a second hand-written version-specifier parser.
    try:
        requirement = Requirement(f"placeholder{specifier_text}")
    except InvalidRequirement:
        return None
    specifiers = tuple(requirement.specifier)
    if len(specifiers) != 1:
        return None
    specifier = specifiers[0]
    if specifier.operator != "==" or "*" in specifier.version:
        return None
    return specifier.version


def _problem(
    reason: DependencyChangeProblemCode,
    detail: str,
    evidence: DependencyChangeSourceEvidence,
) -> DependencyChangeProblem:
    return DependencyChangeProblem(
        reason=reason,
        detail=detail,
        source_evidence=(evidence,),
    )


__all__ = (
    "ExtractedPyprojectOptionalExtraChange",
    "PyprojectOptionalExtraExtractionResult",
    "PyprojectOptionalExtraNoChange",
    "extract_pyproject_optional_extra_change",
    "is_modified_pyproject_file",
)
