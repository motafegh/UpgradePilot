"""Observe bounded direct dependency-install declarations in static workflow run steps.

This dependency-owned responsibility interprets a provider-owned static run declaration
against one independently established repository-relative dependency source path. Its
proof strength stops at visible declaration/configuration: it does not establish command
execution, success, installed versions, general dependency consumption, or package
exercise.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Literal

from ..github.workflow_definition import RunDefaults, RunStepDefinition
from ..repository_path import repository_relative_parts
from .workflow_context import (
    EffectiveWorkingDirectory,
    WorkingDirectorySource,
    WorkingDirectoryState,
    bounded_shell_segments,
    resolve_effective_working_directory,
    resolve_repository_relative_path,
)


type DirectInstallDeclarationState = Literal["observed", "not_observed", "unresolved"]


@dataclass(frozen=True, slots=True)
class DirectInstallDeclarationObservation:
    """Static relation between one run step and one known dependency-source path.

    ``matched_segment_index`` is a zero-based ordinal within the deliberately bounded
    shell-segment split. It is static source structure only; CI may use it to compare
    declaration order inside one run block, but it is not runtime command identity.
    """

    state: DirectInstallDeclarationState
    reason: str
    detail: str
    step_source_index: int
    command: str
    dependency_source_path: str
    working_directory: EffectiveWorkingDirectory
    matched_requirement_path: str | None = None
    matched_segment_index: int | None = None


_DIRECT_PIP_INSTALL_PATTERN = re.compile(
    r"^(?:[A-Za-z_][A-Za-z0-9_]*=[^\s]+\s+)*"
    r"(?:python(?:3)?\s+-m\s+pip|pip(?:3)?)\s+install\b",
    re.IGNORECASE,
)
_REQUIREMENT_PATTERN = re.compile(
    r"(?:^|\s)(?:-r|--requirement)(?:=|\s+)(?P<path>[^\s;&|]+)",
    re.IGNORECASE,
)
_EXPRESSION_MARKER = "${{"


def observe_direct_installation_declaration(
    step: RunStepDefinition,
    *,
    dependency_source_path: str,
    workflow_defaults: RunDefaults | None = None,
    job_defaults: RunDefaults | None = None,
) -> DirectInstallDeclarationObservation:
    """Observe whether one static run step directly names the dependency source file.

    Effective ``working-directory`` follows the shared static dependency-domain context:
    ``step > job defaults.run > workflow defaults.run > repository root``.

    Dynamic or otherwise unsupported path context remains ``unresolved``. A visible
    matching direct pip requirements-file declaration is only static declaration
    evidence; this function never upgrades it to runtime execution/success evidence.
    """

    dependency_parts = repository_relative_parts(dependency_source_path)
    if dependency_parts is None:
        raise ValueError(
            "dependency_source_path must be a normalized repository-relative POSIX path"
        )
    normalized_source = "/".join(dependency_parts)

    working_directory = resolve_effective_working_directory(
        step,
        workflow_defaults=workflow_defaults,
        job_defaults=job_defaults,
    )

    direct_requirement_paths: list[str] = []
    unresolved_path_seen = False

    for segment_index, segment in enumerate(bounded_shell_segments(step.command.text)):
        if _DIRECT_PIP_INSTALL_PATTERN.match(segment) is None:
            continue
        for match in _REQUIREMENT_PATTERN.finditer(segment):
            raw_path = match.group("path").strip("'\"")
            direct_requirement_paths.append(raw_path)

            if _EXPRESSION_MARKER in raw_path:
                unresolved_path_seen = True
                continue
            if working_directory.state == "unresolved":
                unresolved_path_seen = True
                continue

            resolved = resolve_repository_relative_path(
                raw_path,
                working_directory.path,
            )
            if resolved is None:
                unresolved_path_seen = True
                continue
            if resolved == normalized_source:
                return DirectInstallDeclarationObservation(
                    state="observed",
                    reason="direct_requirements_install_declared",
                    detail=(
                        "The static run step directly declares installation from the "
                        "independently established dependency source path."
                    ),
                    step_source_index=step.source_index,
                    command=step.command.text,
                    dependency_source_path=normalized_source,
                    working_directory=working_directory,
                    matched_requirement_path=raw_path,
                    matched_segment_index=segment_index,
                )

    if unresolved_path_seen:
        return DirectInstallDeclarationObservation(
            state="unresolved",
            reason="direct_install_path_context_unresolved",
            detail=(
                "A direct pip requirements-file declaration was visible, but its path "
                "could not be safely resolved against the effective working-directory "
                "context."
            ),
            step_source_index=step.source_index,
            command=step.command.text,
            dependency_source_path=normalized_source,
            working_directory=working_directory,
        )

    if direct_requirement_paths:
        detail = (
            "Direct pip requirements-file declarations were visible, but none resolved "
            "to the independently established dependency source path."
        )
        reason = "dependency_source_not_directly_declared"
    else:
        detail = (
            "The static run step did not contain an admitted direct pip "
            "requirements-file declaration."
        )
        reason = "direct_requirements_install_not_observed"

    return DirectInstallDeclarationObservation(
        state="not_observed",
        reason=reason,
        detail=detail,
        step_source_index=step.source_index,
        command=step.command.text,
        dependency_source_path=normalized_source,
        working_directory=working_directory,
    )


__all__ = (
    "DirectInstallDeclarationObservation",
    "DirectInstallDeclarationState",
    "EffectiveWorkingDirectory",
    "WorkingDirectorySource",
    "WorkingDirectoryState",
    "observe_direct_installation_declaration",
)
