"""Observe bounded direct dependency-install declarations in static workflow run steps.

This dependency-owned responsibility interprets a provider-owned static run declaration
against one independently established repository-relative dependency source path.  Its
proof strength stops at visible declaration/configuration: it does not establish command
execution, success, installed versions, general dependency consumption, or package
exercise.
"""

from __future__ import annotations

import posixpath
import re
from dataclasses import dataclass
from typing import Literal

from ..github.workflow_definition import RunDefaults, RunStepDefinition, StaticScalarValue
from ..repository_path import repository_relative_parts


type DirectInstallDeclarationState = Literal["observed", "not_observed", "unresolved"]
type WorkingDirectoryState = Literal["repository_root", "literal", "unresolved"]
type WorkingDirectorySource = Literal["repository_root", "workflow", "job", "step"]


@dataclass(frozen=True, slots=True)
class EffectiveWorkingDirectory:
    state: WorkingDirectoryState
    source: WorkingDirectorySource
    path: str | None
    raw: str | None


@dataclass(frozen=True, slots=True)
class DirectInstallDeclarationObservation:
    state: DirectInstallDeclarationState
    reason: str
    detail: str
    step_source_index: int
    command: str
    dependency_source_path: str
    working_directory: EffectiveWorkingDirectory
    matched_requirement_path: str | None = None


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

    Effective ``working-directory`` follows GitHub Actions declaration precedence for
    the inputs represented by the bounded IR:

    ``step > job defaults.run > workflow defaults.run > repository root``.

    Dynamic or otherwise unsupported path context remains ``unresolved``.  A visible
    matching direct pip requirements-file declaration is only static declaration
    evidence; this function never upgrades it to runtime execution/success evidence.
    """

    dependency_parts = repository_relative_parts(dependency_source_path)
    if dependency_parts is None:
        raise ValueError(
            "dependency_source_path must be a normalized repository-relative POSIX path"
        )
    normalized_source = "/".join(dependency_parts)

    working_directory = _effective_working_directory(
        step,
        workflow_defaults=workflow_defaults,
        job_defaults=job_defaults,
    )

    direct_requirement_paths: list[str] = []
    unresolved_path_seen = False

    for segment in _shell_segments(step.command.text):
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

            resolved = _resolve_requirement_path(raw_path, working_directory.path)
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


def _effective_working_directory(
    step: RunStepDefinition,
    *,
    workflow_defaults: RunDefaults | None,
    job_defaults: RunDefaults | None,
) -> EffectiveWorkingDirectory:
    candidates: tuple[tuple[WorkingDirectorySource, StaticScalarValue | None], ...] = (
        ("step", step.working_directory),
        ("job", job_defaults.working_directory if job_defaults is not None else None),
        (
            "workflow",
            workflow_defaults.working_directory if workflow_defaults is not None else None,
        ),
    )

    for source, value in candidates:
        if value is None:
            continue
        if value.contains_expression:
            return EffectiveWorkingDirectory(
                state="unresolved",
                source=source,
                path=None,
                raw=value.text,
            )

        path = _normalize_literal_working_directory(value.text)
        if path is None:
            return EffectiveWorkingDirectory(
                state="unresolved",
                source=source,
                path=None,
                raw=value.text,
            )
        return EffectiveWorkingDirectory(
            state="literal",
            source=source,
            path=path,
            raw=value.text,
        )

    return EffectiveWorkingDirectory(
        state="repository_root",
        source="repository_root",
        path=None,
        raw=None,
    )


def _normalize_literal_working_directory(value: str) -> str | None:
    normalized = value.strip().replace("\\", "/")
    while normalized.startswith("./"):
        normalized = normalized[2:]
    if not normalized or normalized.startswith("/"):
        return None

    parts = tuple(normalized.split("/"))
    if any(not part or part in {".", ".."} for part in parts):
        return None
    return "/".join(parts)


def _resolve_requirement_path(
    raw_path: str,
    working_directory: str | None,
) -> str | None:
    candidate = raw_path.strip().replace("\\", "/")
    while candidate.startswith("./"):
        candidate = candidate[2:]
    if not candidate or candidate.startswith("/"):
        return None

    base = working_directory or ""
    resolved = posixpath.normpath(posixpath.join(base, candidate))
    if resolved in {"", ".", ".."} or resolved.startswith("../"):
        return None
    if repository_relative_parts(resolved) is None:
        return None
    return resolved


def _shell_segments(command: str) -> tuple[str, ...]:
    return tuple(
        segment.strip()
        for segment in re.split(r"(?:&&|\|\||;|\n)", command)
        if segment.strip()
    )


__all__ = (
    "DirectInstallDeclarationObservation",
    "DirectInstallDeclarationState",
    "EffectiveWorkingDirectory",
    "WorkingDirectorySource",
    "WorkingDirectoryState",
    "observe_direct_installation_declaration",
)
