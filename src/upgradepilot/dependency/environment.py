"""Represent dependency-owned source context before workflow or runtime interpretation.

These types answer a deliberately narrow question: what exact dependency source established
this changed package, and which source-scoped environment identity is already known from
that evidence? They do **not** say that a workflow selected the environment, that a command
executed, that resolution/installation succeeded, or that the changed package was exercised.

Concrete variants are preferred over one generic record with many optional fields so later
consumers cannot accidentally combine facts that were never established together.
"""

from __future__ import annotations

from dataclasses import dataclass

from .change import DependencyChangeSourceEvidence


@dataclass(frozen=True, slots=True)
class RequirementsFileDependencyContext:
    """Exact-head context for a changed requirements-family dependency source.

    The requirements file is a source that the existing direct-install observer may later
    match against workflow text. This record itself is only dependency-source evidence; it
    does not claim that any workflow installs the file.
    """

    repository: str
    revision: str
    normalized_package: str
    source_evidence: DependencyChangeSourceEvidence

    @property
    def source_path(self) -> str:
        """Return the repository-relative dependency-source path."""

        return self.source_evidence.path


@dataclass(frozen=True, slots=True)
class ConstraintsFileDependencyContext:
    """Exact-head context for a changed constraints-family dependency source.

    Constraints can establish a dependency transition without being a directly installed
    requirements environment. Keeping this context distinct prevents the old ``None``
    handoff from erasing that difference.
    """

    repository: str
    revision: str
    normalized_package: str
    source_evidence: DependencyChangeSourceEvidence

    @property
    def source_path(self) -> str:
        """Return the repository-relative dependency-source path."""

        return self.source_evidence.path


@dataclass(frozen=True, slots=True)
class UvLockDependencyContext:
    """Exact-head context for a dependency transition established from ``uv.lock``.

    A package appearing in the lock is not thereby a member of every project group/extra.
    Later bounded uv membership logic must combine this lock context with exact project
    metadata and an independently established environment-selection proposition.
    """

    repository: str
    revision: str
    normalized_package: str
    source_evidence: DependencyChangeSourceEvidence

    @property
    def source_path(self) -> str:
        """Return the repository-relative lockfile path."""

        return self.source_evidence.path


@dataclass(frozen=True, slots=True)
class PyprojectOptionalExtraDependencyContext:
    """Exact-head context for a change established inside one optional extra.

    Cluster 1 defines the contract shape only. Trusted instances become product evidence
    only after the pyproject extractor in the following cluster establishes ``extra`` from
    exact base/head source; callers must not infer it from workflow text.
    """

    repository: str
    revision: str
    normalized_package: str
    source_evidence: DependencyChangeSourceEvidence
    extra: str

    @property
    def source_path(self) -> str:
        """Return the repository-relative ``pyproject.toml`` path."""

        return self.source_evidence.path


@dataclass(frozen=True, slots=True)
class PyprojectDependencyGroupContext:
    """Exact-head context for a change established inside one dependency group.

    The group identity is source evidence, not proof that a workflow selected or formed
    that group. Static project-environment selection is a later responsibility.
    """

    repository: str
    revision: str
    normalized_package: str
    source_evidence: DependencyChangeSourceEvidence
    group: str

    @property
    def source_path(self) -> str:
        """Return the repository-relative ``pyproject.toml`` path."""

        return self.source_evidence.path


type DependencySourceContext = (
    RequirementsFileDependencyContext
    | ConstraintsFileDependencyContext
    | UvLockDependencyContext
    | PyprojectOptionalExtraDependencyContext
    | PyprojectDependencyGroupContext
)


__all__ = (
    "ConstraintsFileDependencyContext",
    "DependencySourceContext",
    "PyprojectDependencyGroupContext",
    "PyprojectOptionalExtraDependencyContext",
    "RequirementsFileDependencyContext",
    "UvLockDependencyContext",
)
