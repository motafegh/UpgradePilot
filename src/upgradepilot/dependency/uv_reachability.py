"""Establish bounded lock-backed reachability from explicitly selected uv roots.

R4 narrows the former selected-environment membership proposition to the fact the
implementation can actually prove:

    changed package from exact uv.lock
    + admitted explicit uv selector/scope
    + admitted exact lock structure
    -> is the changed package reachable from one selected lock root?

This module deliberately does not claim complete uv environment formation, lock
currentness, resolver satisfiability, command execution, installation success, runtime
version observation, direct package exercise, or behavioral compatibility.

``environment_selection.py`` owns the static uv selector and bounded package scope.
``uv_lock_structure.py`` owns shared external uv.lock structural admission.  The current
R4 migration reuses the already-tested reachability projection primitives in
``uv_membership.py`` so it does not create a second lock-format interpretation while the
legacy membership surface remains temporarily available for the R5 CI-consumer migration.
The public contract for new code is this module.

A positive result is existential: one unconditional selected-root witness is enough.
``not_established`` is stronger and is returned only when every root represented by the
modeled proposition was exhausted.  In particular, an ``all_workspace_packages`` command
with no witness from the currently bound lock package remains ``unresolved`` because R3/R4
do not invent complete workspace-member discovery.
"""

from __future__ import annotations

import posixpath
from collections import deque
from dataclasses import dataclass
from typing import Literal

from ..github.repository import RepositoryFileEvidence, RepositoryTextFile, UnavailableRepositoryFile
from .environment import UvLockDependencyContext
from .environment_selection import (
    AllDependencyGroupsSelector,
    AllOptionalExtrasSelector,
    DependencyGroupSelector,
    OptionalExtraSelector,
    ProjectEnvironmentSelectionDeclaration,
    ProjectEnvironmentSelector,
)
from .uv_lock_structure import UvLockStructureProblem, parse_uv_lock_structure
from .uv_membership import (
    _MAX_PATH_DEPTH,
    _MAX_VISITED_STATES,
    _ReachabilityEdge,
    _ReachabilityLock,
    _ReachabilityPackage,
    _TraversalState,
    _build_reachability_lock,
    _normalize_source_path,
    _resolve_edge,
    _workspace_source_path,
)


type UvSelectedRootReachabilityState = Literal[
    "reachable",
    "not_established",
    "unresolved",
]
type UvReachabilityKind = Literal["direct", "transitive"]


@dataclass(frozen=True, slots=True)
class UvSelectedRootReachability:
    """Static exact-lock evidence for one explicit selected-root reachability proposition.

    ``reachable`` means at least one admitted selected root has one unconditional,
    deterministically resolved lock-backed path to the changed package.

    ``not_established`` means the complete root domain represented by this bounded result
    was traversed without a witness.  It is not a repository-wide, runtime, or complete
    command-environment absence claim.

    ``unresolved`` means the available evidence cannot safely establish either result,
    for example because of marker/fork ambiguity, resource bounds, unsupported binding,
    or an unexhausted all-workspace package scope.
    """

    state: UvSelectedRootReachabilityState
    reason: str
    detail: str
    normalized_package: str
    project_root: str | None
    lock_file_path: str
    selectors: tuple[ProjectEnvironmentSelector, ...]
    reachability_kind: UvReachabilityKind | None = None
    witness_root: str | None = None
    witness_path: tuple[str, ...] = ()


def evaluate_uv_selected_root_reachability(
    context: UvLockDependencyContext,
    declaration: ProjectEnvironmentSelectionDeclaration,
    *,
    lock_file: RepositoryFileEvidence,
) -> UvSelectedRootReachability:
    """Evaluate explicit uv group/extra roots against one admitted exact universal lock.

    ``pyproject.toml`` content is intentionally not an input to this proposition.  The
    declaration already owns the selected project root and selectors, while the admitted
    lock materializes the local package source, selected optional/dev roots, and graph.
    Project-source environment evidence and project/lock currentness remain separate
    responsibilities.
    """

    lock_path = lock_file.path
    source_problem = _validate_reachability_inputs(context, declaration, lock_file=lock_file)
    if source_problem is not None:
        return _result(
            context,
            declaration,
            lock_path=lock_path,
            state="unresolved",
            reason="uv_selected_root_source_identity_unresolved",
            detail=source_problem,
        )

    assert isinstance(lock_file, RepositoryTextFile)

    structural_lock = parse_uv_lock_structure(lock_file.content)
    if isinstance(structural_lock, UvLockStructureProblem):
        return _result(
            context,
            declaration,
            lock_path=lock_file.path,
            state="unresolved",
            reason="uv_selected_root_lock_structure_unresolved",
            detail=structural_lock.detail,
        )

    lock = _build_reachability_lock(structural_lock)
    if isinstance(lock, str):
        return _result(
            context,
            declaration,
            lock_path=lock_file.path,
            state="unresolved",
            reason="uv_selected_root_lock_structure_unresolved",
            detail=lock,
        )

    bound_package = _bind_selected_project_root(
        lock,
        project_root=declaration.project_root,
        lock_path=lock_file.path,
    )
    if isinstance(bound_package, str):
        return _result(
            context,
            declaration,
            lock_path=lock_file.path,
            state="unresolved",
            reason="uv_selected_root_project_binding_unresolved",
            detail=bound_package,
        )

    roots = _selected_lock_roots(bound_package, declaration.selectors)
    if isinstance(roots, str):
        return _result(
            context,
            declaration,
            lock_path=lock_file.path,
            state="unresolved",
            reason="uv_selected_root_selection_unresolved",
            detail=roots,
        )
    if not roots:
        return _result(
            context,
            declaration,
            lock_path=lock_file.path,
            state="unresolved",
            reason="uv_selected_root_no_explicit_roots",
            detail=(
                "The admitted uv declaration did not resolve to any explicit optional-extra "
                "or dependency-group roots in the bound lock package."
            ),
        )

    return _traverse_selected_roots(
        context,
        declaration,
        lock_path=lock_file.path,
        lock=lock,
        roots=roots,
    )


def _validate_reachability_inputs(
    context: UvLockDependencyContext,
    declaration: ProjectEnvironmentSelectionDeclaration,
    *,
    lock_file: RepositoryFileEvidence,
) -> str | None:
    """Validate only relations needed by the selected-root lock proposition."""

    if declaration.manager != "uv":
        return "Selected-root reachability requires a uv selection declaration."
    if not declaration.selectors:
        return "The uv declaration contains no explicit positive environment selectors."
    if declaration.package_scope not in {"bound_project", "all_workspace_packages"}:
        return "The uv declaration contains a package scope outside the admitted rule."

    if isinstance(lock_file, UnavailableRepositoryFile):
        return (
            f"Exact lock source {lock_file.path!r} was unavailable at revision "
            f"{lock_file.revision!r}: {lock_file.detail}"
        )

    assert isinstance(lock_file, RepositoryTextFile)
    if lock_file.repository != context.repository or lock_file.revision != context.revision:
        return "Exact lock repository/revision identity does not match the dependency context."
    if lock_file.path != context.source_evidence.path:
        return "The supplied lock source does not match the dependency-change source path."
    return None


def _bind_selected_project_root(
    lock: _ReachabilityLock,
    *,
    project_root: str | None,
    lock_path: str,
) -> _ReachabilityPackage | str:
    """Bind the declaration's project root directly to one local package in the lock.

    R4 removes the former project-name cross-check because it did not establish lock
    currentness and was not needed for this narrow reachability proposition.  The material
    relation is the selected project root to the lock package's exact editable/virtual
    source path.
    """

    selected_root = project_root or "."
    lock_root = posixpath.dirname(lock_path) or "."
    relative = posixpath.relpath(selected_root, lock_root)
    if relative == ".." or relative.startswith("../"):
        return "The selected project root is outside the uv.lock workspace root."

    expected_source = _normalize_source_path(relative)
    matches = tuple(
        package
        for package in lock.packages
        if _workspace_source_path(package.record.source) == expected_source
    )
    if len(matches) != 1:
        return (
            "The exact uv.lock did not identify exactly one local workspace package matching "
            "the selected project root."
        )
    if matches[0].resolution_markers:
        return (
            "The bound workspace package itself is resolution-marker scoped; the bounded "
            "selected-root rule does not evaluate that conditional project branch."
        )
    return matches[0]


def _selected_lock_roots(
    workspace: _ReachabilityPackage,
    selectors: tuple[ProjectEnvironmentSelector, ...],
) -> tuple[_ReachabilityEdge, ...] | str:
    """Resolve explicit selector names directly against roots materialized in uv.lock.

    ``include`` versus ``only`` remains preserved by the declaration, but this narrow
    proposition asks only whether the explicitly named roots reach the changed package;
    it does not model the rest of the command-selected environment.
    """

    roots: list[_ReachabilityEdge] = []
    for selector in selectors:
        if isinstance(selector, OptionalExtraSelector):
            selected = workspace.optional_dependencies.get(selector.normalized_name)
            if selected is None:
                return (
                    f"Selected optional extra {selector.name!r} is absent from the bound "
                    "uv lock package."
                )
            roots.extend(selected)
            continue

        if isinstance(selector, DependencyGroupSelector):
            selected = workspace.dev_dependencies.get(selector.normalized_name)
            if selected is None:
                return (
                    f"Selected dependency group {selector.name!r} is absent from the bound "
                    "uv lock package."
                )
            roots.extend(selected)
            continue

        if isinstance(selector, AllOptionalExtrasSelector):
            for name in sorted(workspace.optional_dependencies):
                roots.extend(workspace.optional_dependencies[name])
            continue

        if isinstance(selector, AllDependencyGroupsSelector):
            for name in sorted(workspace.dev_dependencies):
                roots.extend(workspace.dev_dependencies[name])
            continue

        return "The uv declaration contains a selector outside the admitted reachability rule."

    unique: list[_ReachabilityEdge] = []
    for edge in roots:
        if edge not in unique:
            unique.append(edge)
    return tuple(unique)


def _traverse_selected_roots(
    context: UvLockDependencyContext,
    declaration: ProjectEnvironmentSelectionDeclaration,
    *,
    lock_path: str,
    lock: _ReachabilityLock,
    roots: tuple[_ReachabilityEdge, ...],
) -> UvSelectedRootReachability:
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
                lock_path=lock_path,
                state="reachable",
                reason="uv_selected_root_direct_reachability",
                detail="The changed package is itself one explicit selected lock root.",
                reachability_kind="direct",
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
                lock_path=lock_path,
                state="unresolved",
                reason="uv_selected_root_traversal_bound_exceeded",
                detail="The bounded uv selected-root traversal exceeded its safety limit.",
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
                    lock_path=lock_path,
                    state="reachable",
                    reason="uv_selected_root_transitive_reachability",
                    detail=(
                        "The changed package is transitively reachable from one explicit "
                        "selected root through exact lock dependency edges."
                    ),
                    reachability_kind="transitive",
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
            lock_path=lock_path,
            state="unresolved",
            reason="uv_selected_root_conditional_or_forked_path_unresolved",
            detail=(
                "No unconditional witness reached the changed package, but one or more "
                "selected branches depended on markers, resolution-scoped packages, missing "
                "lock edges, unresolved extras, or ambiguous repeated records."
            ),
        )

    if declaration.package_scope == "all_workspace_packages":
        return _result(
            context,
            declaration,
            lock_path=lock_path,
            state="unresolved",
            reason="uv_selected_root_workspace_scope_not_exhausted",
            detail=(
                "The explicit roots of the bound lock package were traversed without a "
                "witness, but the uv command applies those selectors to all workspace "
                "packages. The complete in-scope workspace root domain was not exhausted."
            ),
        )

    return _result(
        context,
        declaration,
        lock_path=lock_path,
        state="not_established",
        reason="uv_selected_root_reachability_not_established",
        detail=(
            "The complete bounded selected-root domain was traversed without an exact "
            "lock-backed path to the changed package. This is not a runtime, repository-wide, "
            "or complete command-environment absence claim."
        ),
    )


def _result(
    context: UvLockDependencyContext,
    declaration: ProjectEnvironmentSelectionDeclaration,
    *,
    lock_path: str,
    state: UvSelectedRootReachabilityState,
    reason: str,
    detail: str,
    reachability_kind: UvReachabilityKind | None = None,
    witness_root: str | None = None,
    witness_path: tuple[str, ...] = (),
) -> UvSelectedRootReachability:
    return UvSelectedRootReachability(
        state=state,
        reason=reason,
        detail=detail,
        normalized_package=context.normalized_package,
        project_root=declaration.project_root,
        lock_file_path=lock_path,
        selectors=declaration.selectors,
        reachability_kind=reachability_kind,
        witness_root=witness_root,
        witness_path=witness_path,
    )


__all__ = (
    "UvReachabilityKind",
    "UvSelectedRootReachability",
    "UvSelectedRootReachabilityState",
    "evaluate_uv_selected_root_reachability",
)
