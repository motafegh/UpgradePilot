"""Establish bounded lock-backed membership for explicitly selected uv environments.

This dependency-owned module combines an exact changed package from ``uv.lock``, exact
project/lock source at one immutable revision, and one static uv environment-selection
declaration. It answers only whether the changed package is reachable from explicitly selected
group/extra roots recorded by uv.

``dependency/uv_lock_structure.py`` now owns shared external lock admission: TOML parsing,
schema/revision checks, package identity/name/version/source rules, and repeated-record
preservation. This module consumes that admitted structure and owns the **reachability-specific
projection** of package dependency edges, optional/dev roots, markers, extras, deterministic
edge resolution, and bounded traversal. Transition comparison remains separate in
``dependency/uv_lock.py``.

Unlike source-specific dependency extractors, this evaluator is also a genuine evidence-
composition boundary. The dependency context, workflow declaration, exact project file, and
exact lock file can be independently valid while referring to different repository snapshots,
source paths, or project roots. The cross-branch joins below therefore remain here; they are not
repeated intrinsic exact-file validation.

The result is static exact-source evidence. It does not establish lock freshness/currentness,
resolver satisfiability, command execution, installation success, runtime version observation,
or behavioral exercise.

``uv.lock`` is universal across marker/platform/Python contexts. The first rule never unions
ambiguous resolution branches or evaluates marker expressions. Only one unconditional,
deterministically resolved path may prove positive membership; material marker/fork ambiguity
yields ``unresolved`` rather than a false negative.
"""

from __future__ import annotations

import posixpath
import re
import tomllib
from collections import deque
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Literal

from packaging.utils import canonicalize_name

from ..github.repository import (
    RepositoryFileEvidence,
    RepositoryTextFile,
    UnavailableRepositoryFile,
)
from ..package_identity import normalize_package_name
from .environment import UvLockDependencyContext
from .environment_selection import (
    AllDependencyGroupsSelector,
    AllOptionalExtrasSelector,
    DependencyGroupSelector,
    OptionalExtraSelector,
    ProjectEnvironmentSelectionDeclaration,
    ProjectEnvironmentSelector,
)
from .uv_lock_structure import (
    UvLockPackageRecord,
    UvLockStructure,
    UvLockStructureProblem,
    parse_uv_lock_structure,
)


type UvSelectedEnvironmentMembershipState = Literal[
    "member",
    "not_established",
    "unresolved",
]
type UvMembershipKind = Literal["direct", "transitive"]

_MAX_VISITED_STATES = 10_000
_MAX_PATH_DEPTH = 100
_DISTRIBUTION_NAME_PATTERN = re.compile(
    r"^[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?$"
)


@dataclass(frozen=True, slots=True)
class UvSelectedEnvironmentMembership:
    """Static exact-source relation between explicit uv roots and one changed package.

    ``witness_path`` begins at one selected group/extra root and ends at the changed package.
    ``not_established`` is deliberately weaker than absence: it states only that the bounded
    explicit roots represented by the current proposition were traversed without a witness.
    """

    state: UvSelectedEnvironmentMembershipState
    reason: str
    detail: str
    normalized_package: str
    project_file_path: str
    lock_file_path: str
    selectors: tuple[ProjectEnvironmentSelector, ...]
    membership_kind: UvMembershipKind | None = None
    witness_root: str | None = None
    witness_path: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class _ReachabilityEdge:
    """One lock dependency edge interpreted only for bounded reachability."""

    package: str
    normalized_package: str
    version: str | None
    source: object | None
    marker: str | None
    extras: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class _ReachabilityPackage:
    """Reachability fields projected from one already admitted shared package record."""

    record: UvLockPackageRecord
    resolution_markers: tuple[str, ...]
    dependencies: tuple[_ReachabilityEdge, ...]
    optional_dependencies: Mapping[str, tuple[_ReachabilityEdge, ...]]
    dev_dependencies: Mapping[str, tuple[_ReachabilityEdge, ...]]

    @property
    def index(self) -> int:
        return self.record.index

    @property
    def normalized_package(self) -> str:
        return self.record.normalized_package


@dataclass(frozen=True, slots=True)
class _ParsedProject:
    normalized_name: str
    optional_extras: frozenset[str]
    dependency_groups: frozenset[str]


@dataclass(frozen=True, slots=True)
class _ReachabilityLock:
    packages: tuple[_ReachabilityPackage, ...]
    by_name: Mapping[str, tuple[_ReachabilityPackage, ...]]


@dataclass(frozen=True, slots=True)
class _TraversalState:
    package: _ReachabilityPackage
    activated_extras: tuple[str, ...]
    path: tuple[str, ...]
    root: str


def evaluate_uv_selected_environment_membership(
    context: UvLockDependencyContext,
    declaration: ProjectEnvironmentSelectionDeclaration,
    *,
    project_file: RepositoryFileEvidence,
    lock_file: RepositoryFileEvidence,
) -> UvSelectedEnvironmentMembership:
    """Evaluate explicit uv group/extra roots against one admitted universal lock.

    Shared lock admission happens once through ``parse_uv_lock_structure``. This semantic
    consumer then parses only the reachability-specific fields it needs. If no unconditional
    witness exists but markers, repeated-record ambiguity, or a safety bound is material, the
    result is ``unresolved`` rather than ``not_established``.
    """

    project_path = project_file.path
    lock_path = lock_file.path

    source_problem = _validate_exact_source_identity(
        context,
        declaration,
        project_file=project_file,
        lock_file=lock_file,
    )
    if source_problem is not None:
        return _result(
            context,
            declaration,
            project_path=project_path,
            lock_path=lock_path,
            state="unresolved",
            reason="uv_membership_source_identity_unresolved",
            detail=source_problem,
        )

    assert isinstance(project_file, RepositoryTextFile)
    assert isinstance(lock_file, RepositoryTextFile)

    project = _parse_project(project_file)
    if isinstance(project, str):
        return _result(
            context,
            declaration,
            project_path=project_file.path,
            lock_path=lock_file.path,
            state="unresolved",
            reason="uv_membership_project_metadata_unresolved",
            detail=project,
        )

    structural_lock = parse_uv_lock_structure(lock_file.content)
    if isinstance(structural_lock, UvLockStructureProblem):
        return _result(
            context,
            declaration,
            project_path=project_file.path,
            lock_path=lock_file.path,
            state="unresolved",
            reason="uv_membership_lock_structure_unresolved",
            detail=structural_lock.detail,
        )

    lock = _build_reachability_lock(structural_lock)
    if isinstance(lock, str):
        return _result(
            context,
            declaration,
            project_path=project_file.path,
            lock_path=lock_file.path,
            state="unresolved",
            reason="uv_membership_lock_structure_unresolved",
            detail=lock,
        )

    workspace = _bind_workspace_package(
        project,
        lock,
        project_path=project_file.path,
        lock_path=lock_file.path,
    )
    if isinstance(workspace, str):
        return _result(
            context,
            declaration,
            project_path=project_file.path,
            lock_path=lock_file.path,
            state="unresolved",
            reason="uv_membership_project_binding_unresolved",
            detail=workspace,
        )

    roots = _selected_roots(project, workspace, declaration.selectors)
    if isinstance(roots, str):
        return _result(
            context,
            declaration,
            project_path=project_file.path,
            lock_path=lock_file.path,
            state="unresolved",
            reason="uv_membership_selected_roots_unresolved",
            detail=roots,
        )
    if not roots:
        return _result(
            context,
            declaration,
            project_path=project_file.path,
            lock_path=lock_file.path,
            state="unresolved",
            reason="uv_membership_no_explicit_roots",
            detail=(
                "The uv declaration did not expose any explicit optional-extra or "
                "dependency-group roots for lock-backed membership evaluation."
            ),
        )

    return _traverse_selected_roots(
        context,
        declaration,
        project_path=project_file.path,
        lock_path=lock_file.path,
        lock=lock,
        roots=roots,
    )


# ---------------------------------------------------------------------------
# Independent evidence composition
# ---------------------------------------------------------------------------


def _validate_exact_source_identity(
    context: UvLockDependencyContext,
    declaration: ProjectEnvironmentSelectionDeclaration,
    *,
    project_file: RepositoryFileEvidence,
    lock_file: RepositoryFileEvidence,
) -> str | None:
    """Bind independently produced dependency, workflow, project, and lock evidence.

    Intrinsic exact-file shape/provider-response truth is already owned upstream. These checks
    retain only role and cross-branch relationships needed to prevent valid evidence from one
    repository/snapshot/source/project being reattached to another.
    """

    if declaration.manager != "uv":
        return "Selected-environment lock membership requires a uv declaration."
    if not declaration.selectors:
        return "The uv declaration contains no explicit positive environment selectors."

    unavailable = next(
        (
            file
            for file in (project_file, lock_file)
            if isinstance(file, UnavailableRepositoryFile)
        ),
        None,
    )
    if unavailable is not None:
        return (
            f"Exact source {unavailable.path!r} was unavailable at revision "
            f"{unavailable.revision!r}: {unavailable.detail}"
        )

    assert isinstance(project_file, RepositoryTextFile)
    assert isinstance(lock_file, RepositoryTextFile)

    if posixpath.basename(project_file.path) != "pyproject.toml":
        return "The exact project source is not a pyproject.toml path."

    expected_revision = context.revision
    if (
        project_file.repository != context.repository
        or lock_file.repository != context.repository
        or project_file.revision != expected_revision
        or lock_file.revision != expected_revision
    ):
        return (
            "Exact project/lock repository or revision identity does not match the uv "
            "dependency context."
        )

    if lock_file.path != context.source_evidence.path:
        return "The supplied lock source does not match the dependency-change source path."

    project_root = posixpath.dirname(project_file.path) or None
    if declaration.project_root != project_root:
        return (
            "The static uv declaration is bound to a different project root than the "
            "supplied exact pyproject.toml."
        )
    return None


# ---------------------------------------------------------------------------
# Exact project metadata used by the current bounded proposition
# ---------------------------------------------------------------------------


def _parse_project(file: RepositoryTextFile) -> _ParsedProject | str:
    try:
        document = tomllib.loads(file.content)
    except tomllib.TOMLDecodeError as exc:
        return f"Exact project metadata is not valid TOML: {exc}."

    project = document.get("project")
    if not isinstance(project, Mapping):
        return "Exact project metadata lacks a valid [project] table."
    name = project.get("name")
    if not _valid_distribution_name(name):
        return "Exact project metadata lacks a valid [project].name."
    assert isinstance(name, str)

    optional = project.get("optional-dependencies", {})
    if not isinstance(optional, Mapping):
        return "[project.optional-dependencies] is present but is not a TOML table."
    optional_names = _normalized_unique_keys(optional, kind="optional extra")
    if isinstance(optional_names, str):
        return optional_names

    groups = document.get("dependency-groups", {})
    if not isinstance(groups, Mapping):
        return "[dependency-groups] is present but is not a TOML table."
    group_names = _normalized_unique_keys(groups, kind="dependency group")
    if isinstance(group_names, str):
        return group_names

    return _ParsedProject(
        normalized_name=normalize_package_name(name),
        optional_extras=frozenset(optional_names),
        dependency_groups=frozenset(group_names),
    )


def _normalized_unique_keys(table: Mapping[object, object], *, kind: str) -> set[str] | str:
    normalized: set[str] = set()
    for raw_name, raw_value in table.items():
        if not isinstance(raw_name, str) or not raw_name.strip():
            return f"Exact project metadata contains an invalid {kind} name: {raw_name!r}."
        if not isinstance(raw_value, list):
            return f"Exact project metadata {kind} {raw_name!r} is not an array."
        value = str(canonicalize_name(raw_name))
        if value in normalized:
            return f"Exact project metadata contains colliding normalized {kind} names."
        normalized.add(value)
    return normalized


# ---------------------------------------------------------------------------
# Reachability-specific projection of admitted lock records
# ---------------------------------------------------------------------------


def _build_reachability_lock(structure: UvLockStructure) -> _ReachabilityLock | str:
    """Project graph/root fields from already admitted package records.

    Package name/version/source admission is intentionally absent here: the shared structural
    owner has already established those facts. This stage validates only fields whose meaning is
    needed by explicit-root reachability.
    """

    packages: list[_ReachabilityPackage] = []
    by_name: dict[str, list[_ReachabilityPackage]] = {}
    for record in structure.packages:
        parsed = _parse_reachability_package(record)
        if isinstance(parsed, str):
            return parsed
        packages.append(parsed)
        by_name.setdefault(record.normalized_package, []).append(parsed)

    return _ReachabilityLock(
        packages=tuple(packages),
        by_name={name: tuple(records) for name, records in by_name.items()},
    )


def _parse_reachability_package(record: UvLockPackageRecord) -> _ReachabilityPackage | str:
    raw = record.record_data
    owner = f"package {record.package!r}"

    resolution_markers = _parse_resolution_markers(
        raw.get("resolution-markers", []),
        owner=owner,
    )
    if isinstance(resolution_markers, str):
        return resolution_markers

    dependencies = _parse_edges(raw.get("dependencies", []), owner=owner)
    if isinstance(dependencies, str):
        return dependencies

    optional = _parse_edge_mapping(
        raw.get("optional-dependencies", {}),
        owner=f"{owner} optional-dependencies",
    )
    if isinstance(optional, str):
        return optional

    dev = _parse_edge_mapping(
        raw.get("dev-dependencies", {}),
        owner=f"{owner} dev-dependencies",
    )
    if isinstance(dev, str):
        return dev

    return _ReachabilityPackage(
        record=record,
        resolution_markers=resolution_markers,
        dependencies=dependencies,
        optional_dependencies=optional,
        dev_dependencies=dev,
    )


def _parse_resolution_markers(raw: object, *, owner: str) -> tuple[str, ...] | str:
    if not isinstance(raw, list) or not all(
        isinstance(marker, str) and marker.strip() for marker in raw
    ):
        return f"{owner} resolution-markers must be an array of non-empty strings."
    return tuple(raw)


def _parse_edge_mapping(
    raw: object,
    *,
    owner: str,
) -> Mapping[str, tuple[_ReachabilityEdge, ...]] | str:
    if raw is None:
        return {}
    if not isinstance(raw, Mapping):
        return f"{owner} must be a TOML table."

    parsed: dict[str, tuple[_ReachabilityEdge, ...]] = {}
    for raw_name, raw_edges in raw.items():
        if not isinstance(raw_name, str) or not raw_name.strip():
            return f"{owner} contains an invalid environment name."
        normalized = str(canonicalize_name(raw_name))
        if normalized in parsed:
            return f"{owner} contains colliding normalized environment names."
        edges = _parse_edges(raw_edges, owner=f"{owner} {raw_name!r}")
        if isinstance(edges, str):
            return edges
        parsed[normalized] = edges
    return parsed


def _parse_edges(raw: object, *, owner: str) -> tuple[_ReachabilityEdge, ...] | str:
    if not isinstance(raw, list):
        return f"{owner} dependency entries must be an array."

    edges: list[_ReachabilityEdge] = []
    for index, raw_edge in enumerate(raw):
        if not isinstance(raw_edge, Mapping):
            return f"{owner} dependency entry {index} is not a TOML table."
        name = raw_edge.get("name")
        if not _valid_distribution_name(name):
            return f"{owner} dependency entry {index} has an invalid package name."
        assert isinstance(name, str)

        version = raw_edge.get("version")
        if version is not None and (not isinstance(version, str) or not version.strip()):
            return f"{owner} dependency entry {index} has an invalid version discriminator."

        marker = raw_edge.get("marker")
        if marker is not None and (not isinstance(marker, str) or not marker.strip()):
            return f"{owner} dependency entry {index} has an invalid marker."

        raw_extras = raw_edge.get("extra", [])
        if not isinstance(raw_extras, list) or not all(
            isinstance(extra, str) and extra.strip() for extra in raw_extras
        ):
            return f"{owner} dependency entry {index} has invalid activated extras."
        extras = tuple(str(canonicalize_name(extra)) for extra in raw_extras)
        if len(set(extras)) != len(extras):
            return f"{owner} dependency entry {index} has duplicate normalized extras."

        edges.append(
            _ReachabilityEdge(
                package=name,
                normalized_package=normalize_package_name(name),
                version=version,
                source=raw_edge.get("source"),
                marker=marker,
                extras=extras,
            )
        )
    return tuple(edges)


# ---------------------------------------------------------------------------
# Project binding and explicit selected roots
# ---------------------------------------------------------------------------


def _bind_workspace_package(
    project: _ParsedProject,
    lock: _ReachabilityLock,
    *,
    project_path: str,
    lock_path: str,
) -> _ReachabilityPackage | str:
    project_root = posixpath.dirname(project_path) or "."
    lock_root = posixpath.dirname(lock_path) or "."
    relative = posixpath.relpath(project_root, lock_root)
    if relative == ".." or relative.startswith("../"):
        return "The selected project is outside the uv.lock workspace root."

    expected_source = _normalize_source_path(relative)
    matches = tuple(
        package
        for package in lock.by_name.get(project.normalized_name, ())
        if _workspace_source_path(package.record.source) == expected_source
    )
    if len(matches) != 1:
        return (
            "The exact uv.lock did not identify exactly one workspace package matching "
            "the selected project name/root."
        )
    if matches[0].resolution_markers:
        return (
            "The bound workspace package itself is resolution-marker scoped; the first "
            "membership rule does not evaluate that conditional project branch."
        )
    return matches[0]


def _selected_roots(
    project: _ParsedProject,
    workspace: _ReachabilityPackage,
    selectors: tuple[ProjectEnvironmentSelector, ...],
) -> tuple[_ReachabilityEdge, ...] | str:
    roots: list[_ReachabilityEdge] = []

    for selector in selectors:
        if isinstance(selector, OptionalExtraSelector):
            name = selector.normalized_name
            if name not in project.optional_extras:
                return (
                    f"Selected optional extra {selector.name!r} is absent from exact "
                    "project metadata."
                )
            selected = workspace.optional_dependencies.get(name)
            if selected is None:
                return (
                    f"Selected optional extra {selector.name!r} is absent from the bound "
                    "uv lock package."
                )
            roots.extend(selected)
            continue

        if isinstance(selector, DependencyGroupSelector):
            name = selector.normalized_name
            if name not in project.dependency_groups:
                return (
                    f"Selected dependency group {selector.name!r} is absent from exact "
                    "project metadata."
                )
            selected = workspace.dev_dependencies.get(name)
            if selected is None:
                return (
                    f"Selected dependency group {selector.name!r} is absent from the bound "
                    "uv lock package."
                )
            roots.extend(selected)
            continue

        if isinstance(selector, AllOptionalExtrasSelector):
            for name in sorted(project.optional_extras):
                selected = workspace.optional_dependencies.get(name)
                if selected is None:
                    return f"Optional extra {name!r} is absent from the bound uv lock package."
                roots.extend(selected)
            continue

        if isinstance(selector, AllDependencyGroupsSelector):
            for name in sorted(project.dependency_groups):
                selected = workspace.dev_dependencies.get(name)
                if selected is None:
                    return f"Dependency group {name!r} is absent from the bound uv lock package."
                roots.extend(selected)
            continue

        return "The uv declaration contains a selector outside the admitted membership rule."

    unique: list[_ReachabilityEdge] = []
    for edge in roots:
        if edge not in unique:
            unique.append(edge)
    return tuple(unique)


# ---------------------------------------------------------------------------
# Bounded universal-lock traversal
# ---------------------------------------------------------------------------


def _traverse_selected_roots(
    context: UvLockDependencyContext,
    declaration: ProjectEnvironmentSelectionDeclaration,
    *,
    project_path: str,
    lock_path: str,
    lock: _ReachabilityLock,
    roots: tuple[_ReachabilityEdge, ...],
) -> UvSelectedEnvironmentMembership:
    target = context.normalized_package
    queue: deque[_TraversalState] = deque()
    ambiguous_branch_seen = False

    for edge in roots:
        if edge.marker is not None:
            ambiguous_branch_seen = True
            continue
        resolved = _resolve_edge(lock, edge)
        if not isinstance(resolved, _ReachabilityPackage):
            ambiguous_branch_seen = True
            continue
        if resolved.resolution_markers:
            ambiguous_branch_seen = True
            continue

        if resolved.normalized_package == target:
            return _result(
                context,
                declaration,
                project_path=project_path,
                lock_path=lock_path,
                state="member",
                reason="uv_selected_environment_direct_member",
                detail="The changed package is an explicit selected group/extra root.",
                membership_kind="direct",
                witness_root=resolved.normalized_package,
                witness_path=(resolved.normalized_package,),
            )

        queue.append(
            _TraversalState(
                package=resolved,
                activated_extras=edge.extras,
                path=(resolved.normalized_package,),
                root=resolved.normalized_package,
            )
        )

    visited: set[tuple[int, tuple[str, ...]]] = set()
    while queue:
        state = queue.popleft()
        state_key = (state.package.index, state.activated_extras)
        if state_key in visited:
            continue
        visited.add(state_key)
        if len(visited) > _MAX_VISITED_STATES or len(state.path) > _MAX_PATH_DEPTH:
            return _result(
                context,
                declaration,
                project_path=project_path,
                lock_path=lock_path,
                state="unresolved",
                reason="uv_membership_traversal_bound_exceeded",
                detail="The bounded uv dependency traversal exceeded its safety limit.",
            )

        outgoing = list(state.package.dependencies)
        for extra in state.activated_extras:
            extra_edges = state.package.optional_dependencies.get(extra)
            if extra_edges is None:
                ambiguous_branch_seen = True
                continue
            outgoing.extend(extra_edges)

        for edge in outgoing:
            if edge.marker is not None:
                ambiguous_branch_seen = True
                continue
            resolved = _resolve_edge(lock, edge)
            if not isinstance(resolved, _ReachabilityPackage):
                ambiguous_branch_seen = True
                continue
            if resolved.resolution_markers:
                ambiguous_branch_seen = True
                continue

            path = (*state.path, resolved.normalized_package)
            if resolved.normalized_package == target:
                return _result(
                    context,
                    declaration,
                    project_path=project_path,
                    lock_path=lock_path,
                    state="member",
                    reason="uv_selected_environment_transitive_member",
                    detail=(
                        "The changed package is transitively reachable from one explicit "
                        "selected group/extra root through exact lock dependency edges."
                    ),
                    membership_kind="transitive",
                    witness_root=state.root,
                    witness_path=path,
                )

            queue.append(
                _TraversalState(
                    package=resolved,
                    activated_extras=edge.extras,
                    path=path,
                    root=state.root,
                )
            )

    if ambiguous_branch_seen:
        return _result(
            context,
            declaration,
            project_path=project_path,
            lock_path=lock_path,
            state="unresolved",
            reason="uv_membership_conditional_or_forked_path_unresolved",
            detail=(
                "No unconditional witness reached the changed package, but one or more "
                "selected branches depended on markers, resolution-scoped packages, "
                "missing lock edges, unresolved extras, or ambiguous repeated records."
            ),
        )

    return _result(
        context,
        declaration,
        project_path=project_path,
        lock_path=lock_path,
        state="not_established",
        reason="uv_selected_environment_membership_not_established",
        detail=(
            "The bounded explicit selected roots were traversed completely without an "
            "exact lock-backed path to the changed package. This is not a runtime or "
            "repository-wide absence claim."
        ),
    )


def _resolve_edge(
    lock: _ReachabilityLock,
    edge: _ReachabilityEdge,
) -> _ReachabilityPackage | str | None:
    candidates = list(lock.by_name.get(edge.normalized_package, ()))
    if edge.version is not None:
        candidates = [
            candidate
            for candidate in candidates
            if candidate.record.version == edge.version
        ]
    if edge.source is not None:
        candidates = [
            candidate
            for candidate in candidates
            if candidate.record.source == edge.source
        ]

    if not candidates:
        return None
    if len(candidates) == 1:
        return candidates[0]
    return (
        f"Dependency edge for {edge.normalized_package!r} maps to several lock records "
        "without enough version/source identity to choose one deterministically."
    )


# ---------------------------------------------------------------------------
# Local path/name helpers and result construction
# ---------------------------------------------------------------------------


def _workspace_source_path(source: object | None) -> str | None:
    if not isinstance(source, Mapping):
        return None
    for key in ("editable", "virtual"):
        value = source.get(key)
        if isinstance(value, str):
            return _normalize_source_path(value)
    return None


def _normalize_source_path(value: str) -> str:
    normalized = value.strip().replace("\\", "/")
    if normalized in {"", ".", "./"}:
        return "."
    while normalized.startswith("./"):
        normalized = normalized[2:]
    return posixpath.normpath(normalized)


def _valid_distribution_name(value: object) -> bool:
    return (
        isinstance(value, str)
        and bool(value)
        and value == value.strip()
        and _DISTRIBUTION_NAME_PATTERN.fullmatch(value) is not None
    )


def _result(
    context: UvLockDependencyContext,
    declaration: ProjectEnvironmentSelectionDeclaration,
    *,
    project_path: str,
    lock_path: str,
    state: UvSelectedEnvironmentMembershipState,
    reason: str,
    detail: str,
    membership_kind: UvMembershipKind | None = None,
    witness_root: str | None = None,
    witness_path: tuple[str, ...] = (),
) -> UvSelectedEnvironmentMembership:
    return UvSelectedEnvironmentMembership(
        state=state,
        reason=reason,
        detail=detail,
        normalized_package=context.normalized_package,
        project_file_path=project_path,
        lock_file_path=lock_path,
        selectors=declaration.selectors,
        membership_kind=membership_kind,
        witness_root=witness_root,
        witness_path=witness_path,
    )


__all__ = (
    "UvMembershipKind",
    "UvSelectedEnvironmentMembership",
    "UvSelectedEnvironmentMembershipState",
    "evaluate_uv_selected_environment_membership",
)
