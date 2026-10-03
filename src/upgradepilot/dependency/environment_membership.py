"""Compare source-established project environments with static project selectors.

Cluster 2 can establish that a changed dependency is declared directly inside one
``pyproject.toml`` optional extra (and the Cluster-1 contract also admits dependency
groups). Cluster 3 can independently establish what extra/group a workflow command
visibly selects. This module owns the small dependency-domain relation between those
facts so CI does not learn PEP 621/735 environment semantics itself.

The result is static source/selection evidence only. ``not_established`` means the
visible selector does not establish selection of the affected environment; it is not a
runtime absence or installation claim.

An optional requirement's marker is preserved by extraction/analysis. This static
selector boundary has no scoped installer marker environment; a selected marked
requirement therefore remains unresolved, rather than evaluating against host defaults
or silently treating a workflow Python setting as the installer's complete environment.
"""

from __future__ import annotations

import posixpath
from dataclasses import dataclass
from typing import Literal

from .environment import (
    PyprojectDependencyGroupContext,
    PyprojectOptionalExtraDependencyContext,
)
from .environment_selection import (
    AllDependencyGroupsSelector,
    AllOptionalExtrasSelector,
    DependencyGroupSelector,
    OptionalExtraSelector,
    ProjectEnvironmentSelectionDeclaration,
)

type ProjectSourceEnvironmentContext = (
    PyprojectOptionalExtraDependencyContext | PyprojectDependencyGroupContext
)
type ProjectSourceEnvironmentMembershipState = Literal[
    "member",
    "not_established",
    "unresolved",
]


@dataclass(frozen=True, slots=True)
class ProjectSourceEnvironmentMembership:
    """Static relation between one affected project environment and one declaration."""

    state: ProjectSourceEnvironmentMembershipState
    reason: str
    detail: str
    normalized_package: str
    project_file_path: str
    affected_environment_kind: Literal["optional_extra", "dependency_group"]
    affected_environment_name: str
    unresolved_conditions: tuple[str, ...] = ()


def evaluate_project_source_environment_membership(
    context: ProjectSourceEnvironmentContext,
    declaration: ProjectEnvironmentSelectionDeclaration,
) -> ProjectSourceEnvironmentMembership:
    """Evaluate whether a visible selector includes the source-established environment."""

    project_root = posixpath.dirname(context.source_path) or None
    if project_root == ".":
        project_root = None
    if declaration.project_root != project_root:
        return _result(
            context,
            state="unresolved",
            reason="project_environment_root_mismatch",
            detail=(
                "The static project declaration is bound to a different project root "
                "than the dependency source context."
            ),
        )

    if isinstance(context, PyprojectOptionalExtraDependencyContext):
        affected = context.normalized_extra
        for selector in declaration.selectors:
            if isinstance(selector, AllOptionalExtrasSelector):
                return _selected_optional_requirement(
                    context,
                    detail="The static declaration explicitly selects all optional extras.",
                )
            if (
                isinstance(selector, OptionalExtraSelector)
                and selector.normalized_name == affected
            ):
                return _selected_optional_requirement(
                    context,
                    detail=(
                        "The static declaration explicitly selects the same normalized "
                        "optional extra that contains the changed dependency."
                    ),
                )

        return _result(
            context,
            state="not_established",
            reason="affected_optional_extra_not_selected",
            detail=(
                "The visible positive selectors do not establish selection of the "
                f"affected optional extra {context.extra!r}."
            ),
        )

    affected = context.normalized_group
    for selector in declaration.selectors:
        if isinstance(selector, AllDependencyGroupsSelector):
            return _result(
                context,
                state="member",
                reason="affected_dependency_group_selected",
                detail="The static declaration explicitly selects all dependency groups.",
            )
        if (
            isinstance(selector, DependencyGroupSelector)
            and selector.normalized_name == affected
        ):
            return _result(
                context,
                state="member",
                reason="affected_dependency_group_selected",
                detail=(
                    "The static declaration explicitly selects the same normalized "
                    "dependency group that contains the changed dependency."
                ),
            )

    return _result(
        context,
        state="not_established",
        reason="affected_dependency_group_not_selected",
        detail=(
            "The visible positive selectors do not establish selection of the affected "
            f"dependency group {context.group!r}."
        ),
    )


def _selected_optional_requirement(
    context: PyprojectOptionalExtraDependencyContext,
    *,
    detail: str,
) -> ProjectSourceEnvironmentMembership:
    """Separate positive extra selection from unevaluated requirement applicability."""

    if context.requirement_marker is not None:
        return _result(
            context,
            state="unresolved",
            reason="changed_requirement_marker_not_evaluated",
            detail=(
                f"{detail} The changed requirement has environment marker "
                f"{context.requirement_marker!r}. Its applicability is unresolved because "
                "no scoped installer marker environment is established at this static "
                "selection boundary. Extra selection alone does not prove consumption."
            ),
            unresolved_conditions=(context.requirement_marker,),
        )
    return _result(
        context,
        state="member",
        reason="affected_optional_extra_selected",
        detail=detail,
    )


def _result(
    context: ProjectSourceEnvironmentContext,
    *,
    state: ProjectSourceEnvironmentMembershipState,
    reason: str,
    detail: str,
    unresolved_conditions: tuple[str, ...] = (),
) -> ProjectSourceEnvironmentMembership:
    if isinstance(context, PyprojectOptionalExtraDependencyContext):
        kind: Literal["optional_extra", "dependency_group"] = "optional_extra"
        name = context.extra
    else:
        kind = "dependency_group"
        name = context.group

    return ProjectSourceEnvironmentMembership(
        state=state,
        reason=reason,
        detail=detail,
        normalized_package=context.normalized_package,
        project_file_path=context.source_path,
        affected_environment_kind=kind,
        affected_environment_name=name,
        unresolved_conditions=unresolved_conditions,
    )


__all__ = (
    "ProjectSourceEnvironmentContext",
    "ProjectSourceEnvironmentMembership",
    "ProjectSourceEnvironmentMembershipState",
    "evaluate_project_source_environment_membership",
)
