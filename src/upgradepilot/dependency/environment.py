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

from packaging.utils import canonicalize_name

from .change import DependencyChangeSourceEvidence


@dataclass(frozen=True, slots=True)
class RequirementsFileDependencyContext:
    """Exact-head context for a changed requirements-family dependency source."""

    repository: str
    revision: str
    normalized_package: str
    source_evidence: DependencyChangeSourceEvidence

    @property
    def source_path(self) -> str:
        return self.source_evidence.path


@dataclass(frozen=True, slots=True)
class ConstraintsFileDependencyContext:
    """Exact-head context for a changed constraints-family dependency source."""

    repository: str
    revision: str
    normalized_package: str
    source_evidence: DependencyChangeSourceEvidence

    @property
    def source_path(self) -> str:
        return self.source_evidence.path


@dataclass(frozen=True, slots=True)
class UvLockDependencyContext:
    """Exact-head context for a dependency transition established from ``uv.lock``.

    A package appearing in the lock is not thereby reachable from every selected root.
    Later bounded uv reachability logic must combine this lock context with an independently
    established environment-selection proposition.
    """

    repository: str
    revision: str
    normalized_package: str
    source_evidence: DependencyChangeSourceEvidence

    @property
    def source_path(self) -> str:
        return self.source_evidence.path


@dataclass(frozen=True, slots=True)
class PyprojectOptionalExtraDependencyContext:
    """Exact-head context for a change established inside one optional extra.

    ``extra`` preserves source spelling for explanation. ``normalized_extra`` follows
    Python packaging extra-name comparison semantics so later workflow selectors can be
    compared without treating ``-``, ``_``, or ``.`` spelling differences as distinct
    environment identities.
    """

    repository: str
    revision: str
    normalized_package: str
    source_evidence: DependencyChangeSourceEvidence
    extra: str

    @property
    def source_path(self) -> str:
        return self.source_evidence.path

    @property
    def normalized_extra(self) -> str:
        """Return the canonical comparison name while preserving ``extra`` unchanged."""

        return str(canonicalize_name(self.extra))


@dataclass(frozen=True, slots=True)
class PyprojectDependencyGroupContext:
    """Exact-head context for a change established inside one dependency group.

    Dependency-group standards require normalized comparison while user-facing tools
    should preserve the original spelling. This context therefore exposes both forms.
    """

    repository: str
    revision: str
    normalized_package: str
    source_evidence: DependencyChangeSourceEvidence
    group: str

    @property
    def source_path(self) -> str:
        return self.source_evidence.path

    @property
    def normalized_group(self) -> str:
        """Return the canonical comparison name while preserving ``group`` unchanged."""

        return str(canonicalize_name(self.group))


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
