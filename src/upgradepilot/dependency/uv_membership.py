"""Establish bounded lock-backed membership for explicitly selected uv environments.

This module combines four already-separated facts:

* an exact changed package established from ``uv.lock``;
* an exact ``pyproject.toml`` project identity;
* an exact lockfile at the same repository/revision;
* one static uv project-environment selection declaration.

It answers only whether the changed normalized package is reachable from the explicitly
selected optional-extra/dependency-group roots recorded by uv. It does not establish
lock freshness, resolver satisfiability, command execution, installation success, runtime
version observation, or behavioral exercise.

``uv.lock`` is universal across marker/platform/Python contexts. This first rule therefore
never unions ambiguous resolution branches or evaluates marker expressions. An
unconditional witness path can prove positive membership; otherwise material marker/fork
ambiguity yields ``unresolved`` rather than a false negative.
"""

from __future__ import annotations

import posixpath
import tomllib
from collections import deque
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Literal

from packaging.utils import canonicalize_name

from ..github.repository import (
    ExactRepositoryFileEvidence,
    RepositoryTextFile,
    UnavailableRepositoryFile,
)
from ..package_identity import normalize_package_name
from ..repository_path import repository_relative_parts
from .environment import UvLockDependencyContext
from .environment_selection import (
    AllDependencyGroupsSelector,
    AllOptionalExtrasSelector,
    DependencyGroupSelector,
    OptionalExtraSelector,
    ProjectEnvironmentSelectionDeclaration,
    ProjectEnvironmentSelector,
)


type UvSelectedEnvironmentMembershipState = Literal[
    "member",
    "not_established",
    "unresolved",
]
type UvMembershipKind = Literal["direct", "transitive"]

_MAX_VISITED_STATES = 10_000
_MAX_PATH_DEPTH = 100
_MISSING = object()


@dataclass(frozen=True, slots=True)
class UvSelectedEnvironmentMembership:
    """Static exact-source relation between explicit uv roots and one changed package.

    ``witness_path`` begins at one selected group/extra root package and ends at the
    changed package. ``not_established`` is deliberately weaker than package absence: it
    only states that the bounded explicit roots were completely traversed without a
    witness. Runtime/default/base-project roots may still differ.
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
class _DependencyEdge:
    package: str
    normalized_package: str
    version: str | None
    source: object
    marker: str | None
    extras: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class _LockPackage:
    index: int
    package: str
    normalized_package: str
    version: str | None
    source: object
    dependencies: tuple[_DependencyEdge, ...]
    optional_dependencies: Mapping[str, tuple[_DependencyEdge, ...]]
    dev_dependencies: Mapping[str, tuple[_DependencyEdge, ...]]


@dataclass(frozen=True, slots=True)
class _ParsedProject:
    normalized_name: str
    optional_extras: frozenset[str]
    dependency_groups: frozenset[str]


@dataclass(frozen=True, slots=True)
class _ParsedLock:
    packages: tuple[_LockPackage, ...]
    by_name: Mapping[str, tuple[_LockPackage, ...]]


@dataclass(frozen=True, slots=True)
class _TraversalState:
    package: _LockPackage
    activated_extras: tuple[str, ...]
    path: tuple[str, ...]
    root: str


def evaluate_uv_selected_environment_membership(
    context: UvLockDependencyContext,
    declaration: ProjectEnvironmentSelectionDeclaration,
    *,
    project_file: ExactRepositoryFileEvidence,
    lock_file: ExactRepositoryFileEvidence,
) -> UvSelectedEnvironmentMembership:
    """Evaluate explicit uv group/extra roots against an exact universal lock graph.

    Only Cluster-3 positive selectors are consumed. A positive result requires one
    unconditional, deterministically resolved path. If no witness exists but marker/fork
    ambiguity or a safety bound was encountered, the result is ``unresolved`` rather
    than ``not_established``.
    """

    project_path = _evidence_path(project_file, fallback="pyproject.toml")
    lock_path = _evidence_path(lock_file, fallback=context.source_path)

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

    project_result = _parse_project(project_file)
    if isinstance(project_result, str):
        return _result(
            context,
            declaration,
            project_path=project_file.path,
            lock_path=lock_file.path,
            state="unresolved",
            reason="uv_membership_project_metadata_unresolved",
            detail=project_result,
        )

    lock_result = _parse_lock(lock_file)
    if isinstance(lock_result, str):
        return _result(
            context,
            declaration,
            project_path=project_file.path,
            lock_path=lock_file.path,
            state="unresolved",
            reason="uv_membership_lock_structure_unresolved",
            detail=lock_result,
        )

    workspace_package = _bind_workspace_package(
        project_result,
        lock_result,
        project_path=project_file.path,
        lock_path=lock_file.path,
    )
    if isinstance(workspace_package, str):
        return _result(
            context,
            declaration,
            project_path=project_file.path,
            lock_path=lock_file.path,
            state="unresolved",
            reason="uv_membership_project_binding_unresolved",
            detail=workspace_package,
        )

    roots_result = _selected_roots(
        project_result,
        workspace_package,
        declaration.selectors,
    )
    if isinstance(roots_result, str):
        return _result(
            context,
            declaration,
            project_path=project_file.path,
            lock_path=lock_file.path,
            state="unresolved",
            reason="uv_membership_selected_roots_unresolved",
            detail=roots_result,
        )

    roots = roots_result
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
        lock=lock_result,
        roots=roots,
    )


def _validate_exact_source_identity(
    context: UvLockDependencyContext,
    declaration: ProjectEnvironmentSelectionDeclaration,
    *,
    project_file: ExactRepositoryFileEvidence,
    lock_file: ExactRepositoryFileEvidence,
) -> str | None:
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

    project_parts = repository_relative_parts(project_file.path)
    if project_parts is None or project_parts[-1] != "pyproject.toml":
        return "The exact project source is not a normalized pyproject.toml path."
    lock_parts = repository_relative_parts(lock_file.path)
    if lock_parts is None or lock_parts[-1] != "uv.lock":
        return "The exact lock source is not a normalized uv.lock path."

    if project_file.returned_path != project_file.path or lock_file.returned_path != lock_file.path:
        return "Exact project/lock returned paths do not match requested repository paths."

    expected_revision = context.revision
    if (
        project_file.repository != context.repository
        or lock_file.repository != context.repository
        or project_file.revision != expected_revision
        or lock_file.revision != expected_revision
    ):
        return "Exact project/lock repository or revision identity does not match the uv context."

    evidence = context.source_evidence
    if lock_file.path != evidence.path or evidence.head_revision != expected_revision:
        return "The supplied uv.lock does not match the dependency-change source evidence."
    if evidence.head_blob_sha is not None and lock_file.blob_sha != evidence.head_blob_sha:
        return "The supplied uv.lock blob SHA does not match the dependency-change evidence."
    if (
        evidence.head_byte_count is not None
        and lock_file.decoded_byte_count != evidence.head_byte_count
    ):
        return "The supplied uv.lock byte count does not match the dependency-change evidence."

    for label, file in (("project", project_file), ("lock", lock_file)):
        if not file.blob_sha:
            return f"The exact {label} source lacks a blob SHA."
        if (
            type(file.reported_byte_count) is not int
            or type(file.decoded_byte_count) is not int
            or file.reported_byte_count < 0
            or file.reported_byte_count != file.decoded_byte_count
        ):
            return f"The exact {label} source has inconsistent byte-count evidence."

    project_root = "/".join(project_parts[:-1]) or None
    if declaration.project_root != project_root:
        return (
            "The static uv declaration is bound to a different project root than the "
            "supplied exact pyproject.toml."
        )
    return None


def _parse_project(file: RepositoryTextFile) -> _ParsedProject | str:
    try:
        document = tomllib.loads(file.content)
    except tomllib.TOMLDecodeError as exc:
        return f"Exact project metadata is not valid TOML: {exc}."

    project = document.get("project")
    if not isinstance(project, Mapping):
        return "Exact project metadata lacks a valid [project] table."
    name = project.get("name")
    if not isinstance(name, str) or not name.strip():
        return "Exact project metadata lacks a valid [project].name."

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
    for raw_name in table:
        if not isinstance(raw_name, str) or not raw_name.strip():
            return f"Exact project metadata contains an invalid {kind} name: {raw_name!r}."
        value = str(canonicalize_name(raw_name))
        if value in normalized:
            return f"Exact project metadata contains colliding normalized {kind} names."
        normalized.add(value)
    return normalized


def _parse_lock(file: RepositoryTextFile) -> _ParsedLock | str:
    try:
        document = tomllib.loads(file.content)
    except tomllib.TOMLDecodeError as exc:
        return f"Exact uv.lock is not valid TOML: {exc}."

    if document.get("version") != 1:
        return "The bounded membership parser supports only uv.lock schema version 1."
    revision = document.get("revision")
    if type(revision) is not int or revision < 0:
        return "The uv.lock revision field must be a non-negative integer."

    raw_packages = document.get("package")
    if not isinstance(raw_packages, list):
        return "The uv.lock package field must be an array of tables."

    packages: list[_LockPackage] = []
    by_name: dict[str, list[_LockPackage]] = {}
    for index, raw_package in enumerate(raw_packages):
        parsed = _parse_lock_package(raw_package, index=index)
        if isinstance(parsed, str):
            return parsed
        packages.append(parsed)
        by_name.setdefault(parsed.normalized_package, []).append(parsed)

    return _ParsedLock(
        packages=tuple(packages),
        by_name={name: tuple(records) for name, records in by_name.items()},
    )


def _parse_lock_package(raw: object, *, index: int) -> _LockPackage | str:
    if not isinstance(raw, Mapping):
        return f"uv.lock package record at index {index} is not a TOML table."

    name = raw.get("name")
    if not isinstance(name, str) or not name.strip():
        return f"uv.lock package record at index {index} has an invalid name."

    raw_version = raw.get("version")
    if raw_version is not None and (not isinstance(raw_version, str) or not raw_version.strip()):
        return f"uv.lock package {name!r} has an invalid version value."

    source = _freeze(raw.get("source", _MISSING))
    dependencies = _parse_edges(raw.get("dependencies", []), owner=f"package {name!r}")
    if isinstance(dependencies, str):
        return dependencies
    optional = _parse_edge_mapping(
        raw.get("optional-dependencies", {}),
        owner=f"package {name!r} optional-dependencies",
    )
    if isinstance(optional, str):
        return optional
    dev = _parse_edge_mapping(
        raw.get("dev-dependencies", {}),
        owner=f"package {name!r} dev-dependencies",
    )
    if isinstance(dev, str):
        return dev

    return _LockPackage(
        index=index,
        package=name,
        normalized_package=normalize_package_name(name),
        version=raw_version,
        source=source,
        dependencies=dependencies,
        optional_dependencies=optional,
        dev_dependencies=dev,
    )


def _parse_edge_mapping(raw: object, *, owner: str) -> Mapping[str, tuple[_DependencyEdge, ...]] | str:
    if raw is None:
        return {}
    if not isinstance(raw, Mapping):
        return f"{owner} must be a TOML table."

    parsed: dict[str, tuple[_DependencyEdge, ...]] = {}
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


def _parse_edges(raw: object, *, owner: str) -> tuple[_DependencyEdge, ...] | str:
    if not isinstance(raw, list):
        return f"{owner} dependency entries must be an array."

    edges: list[_DependencyEdge] = []
    for index, raw_edge in enumerate(raw):
        if not isinstance(raw_edge, Mapping):
            return f"{owner} dependency entry {index} is not a TOML table."
        name = raw_edge.get("name")
        if not isinstance(name, str) or not name.strip():
            return f"{owner} dependency entry {index} has an invalid package name."

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
            _DependencyEdge(
                package=name,
                normalized_package=normalize_package_name(name),
                version=version,
                source=_freeze(raw_edge.get("source", _MISSING)),
                marker=marker,
                extras=extras,
            )
        )
    return tuple(edges)


def _bind_workspace_package(
    project: _ParsedProject,
    lock: _ParsedLock,
    *,
    project_path: str,
    lock_path: str,
) -> _LockPackage | str:
    project_root = posixpath.dirname(project_path) or "."
    lock_root = posixpath.dirname(lock_path) or "."
    relative = posixpath.relpath(project_root, lock_root)
    if relative == ".." or relative.startswith("../"):
        return "The selected project is outside the uv.lock workspace root."

    expected_source = _normalize_source_path(relative)
    matches = tuple(
        package
        for package in lock.by_name.get(project.normalized_name, ())
        if _workspace_source_path(package.source) == expected_source
    )
    if len(matches) != 1:
        return (
            "The exact uv.lock did not identify exactly one workspace package matching "
            "the selected project name/root."
        )
    return matches[0]


def _selected_roots(
    project: _ParsedProject,
    workspace: _LockPackage,
    selectors: tuple[ProjectEnvironmentSelector, ...],
) -> tuple[_DependencyEdge, ...] | str:
    roots: list[_DependencyEdge] = []

    for selector in selectors:
        if isinstance(selector, OptionalExtraSelector):
            name = selector.normalized_name
            if name not in project.optional_extras:
                return f"Selected optional extra {selector.name!r} is absent from exact project metadata."
            selected = workspace.optional_dependencies.get(name)
            if selected is None:
                return f"Selected optional extra {selector.name!r} is absent from the bound uv lock package."
            roots.extend(selected)
            continue

        if isinstance(selector, DependencyGroupSelector):
            name = selector.normalized_name
            if name not in project.dependency_groups:
                return f"Selected dependency group {selector.name!r} is absent from exact project metadata."
            selected = workspace.dev_dependencies.get(name)
            if selected is None:
                return f"Selected dependency group {selector.name!r} is absent from the bound uv lock package."
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

    # Preserve first occurrence/order for deterministic witnesses without treating repeated
    # roots as separate semantic evidence.
    unique: list[_DependencyEdge] = []
    for edge in roots:
        if edge not in unique:
            unique.append(edge)
    return tuple(unique)


def _traverse_selected_roots(
    context: UvLockDependencyContext,
    declaration: ProjectEnvironmentSelectionDeclaration,
    *,
    project_path: str,
    lock_path: str,
    lock: _ParsedLock,
    roots: tuple[_DependencyEdge, ...],
) -> UvSelectedEnvironmentMembership:
    target = context.normalized_package
    queue: deque[_TraversalState] = deque()
    ambiguous_branch_seen = False

    for edge in roots:
        if edge.marker is not None:
            ambiguous_branch_seen = True
            continue
        resolved = _resolve_edge(lock, edge)
        if isinstance(resolved, str):
            ambiguous_branch_seen = True
            continue
        if resolved is None:
            return _result(
                context,
                declaration,
                project_path=project_path,
                lock_path=lock_path,
                state="unresolved",
                reason="uv_membership_lock_edge_unresolved",
                detail=(
                    f"Selected root {edge.package!r} did not resolve to a lock package "
                    "record."
                ),
            )

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
            if isinstance(resolved, str):
                ambiguous_branch_seen = True
                continue
            if resolved is None:
                return _result(
                    context,
                    declaration,
                    project_path=project_path,
                    lock_path=lock_path,
                    state="unresolved",
                    reason="uv_membership_lock_edge_unresolved",
                    detail=(
                        f"Dependency edge {state.package.package!r} -> {edge.package!r} "
                        "did not resolve to a lock package record."
                    ),
                )

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
                "selected dependency branches depended on markers, unresolved extras, "
                "or ambiguous repeated lock records."
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


def _resolve_edge(lock: _ParsedLock, edge: _DependencyEdge) -> _LockPackage | str | None:
    candidates = list(lock.by_name.get(edge.normalized_package, ()))
    if edge.version is not None:
        candidates = [candidate for candidate in candidates if candidate.version == edge.version]
    if edge.source != _freeze(_MISSING):
        candidates = [candidate for candidate in candidates if candidate.source == edge.source]

    if not candidates:
        return None
    if len(candidates) == 1:
        return candidates[0]
    return (
        f"Dependency edge for {edge.normalized_package!r} maps to several lock records "
        "without enough version/source identity to choose one deterministically."
    )


def _workspace_source_path(source: object) -> str | None:
    if not isinstance(source, tuple) or len(source) != 2 or source[0] != "mapping":
        return None
    entries = dict(source[1])
    for key in ("editable", "virtual"):
        frozen = entries.get(key)
        if not isinstance(frozen, tuple) or len(frozen) != 2 or frozen[0] != "str":
            continue
        return _normalize_source_path(frozen[1])
    return None


def _normalize_source_path(value: str) -> str:
    normalized = value.strip().replace("\\", "/")
    if normalized in {"", ".", "./"}:
        return "."
    while normalized.startswith("./"):
        normalized = normalized[2:]
    return posixpath.normpath(normalized)


def _freeze(value: object) -> object:
    if value is _MISSING:
        return ("missing", "")
    if isinstance(value, Mapping):
        return (
            "mapping",
            tuple(sorted((str(key), _freeze(item)) for key, item in value.items())),
        )
    if isinstance(value, list):
        return ("list", tuple(_freeze(item) for item in value))
    if isinstance(value, str):
        return ("str", value)
    if value is None:
        return ("none", "")
    return (type(value).__qualname__, repr(value))


def _evidence_path(file: ExactRepositoryFileEvidence, *, fallback: str) -> str:
    return file.path if isinstance(file, (RepositoryTextFile, UnavailableRepositoryFile)) else fallback


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
