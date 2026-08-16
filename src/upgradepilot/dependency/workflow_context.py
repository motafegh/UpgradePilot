"""Resolve static workflow path context shared by dependency-domain observers.

GitHub owns the parsed workflow structure. Dependency observers need only a small,
provider-IR-facing interpretation of effective ``working-directory`` and safe
repository-relative paths. Keeping that logic here prevents the direct-requirements and
project-environment observers from independently reimplementing GitHub Actions precedence.

These helpers remain static declaration machinery. They do not establish filesystem
existence, command execution, runtime working directories, or shell semantics.
"""

from __future__ import annotations

import posixpath
import re
from dataclasses import dataclass
from typing import Literal

from ..github.workflow_definition import RunDefaults, RunStepDefinition, StaticScalarValue
from ..repository_path import repository_relative_parts


type WorkingDirectoryState = Literal["repository_root", "literal", "unresolved"]
type WorkingDirectorySource = Literal["repository_root", "workflow", "job", "step"]


@dataclass(frozen=True, slots=True)
class EffectiveWorkingDirectory:
    """Resolved static working-directory context for one run declaration.

    ``path`` is repository-relative when statically usable; ``None`` denotes repository
    root for the root state. ``raw`` preserves the selected declaration for diagnostics.
    """

    state: WorkingDirectoryState
    source: WorkingDirectorySource
    path: str | None
    raw: str | None


def resolve_effective_working_directory(
    step: RunStepDefinition,
    *,
    workflow_defaults: RunDefaults | None = None,
    job_defaults: RunDefaults | None = None,
) -> EffectiveWorkingDirectory:
    """Apply static GitHub Actions precedence: step > job > workflow > repo root.

    A dynamic higher-precedence declaration shadows lower levels. Falling through would
    fabricate a working directory that GitHub Actions may not use, so such a case is
    explicitly unresolved.
    """

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


def resolve_repository_relative_path(
    raw_path: str,
    working_directory: str | None,
) -> str | None:
    """Resolve one literal relative path while keeping the result inside the repository.

    ``working_directory=None`` means repository root. Parent components may be used when
    they normalize back inside the repository, matching the existing requirements-file
    behavior without permitting traversal outside the repository boundary.
    """

    candidate = raw_path.strip().replace("\\", "/")
    while candidate.startswith("./"):
        candidate = candidate[2:]
    if candidate in {"", "."}:
        return working_directory
    if candidate.startswith("/"):
        return None

    base = working_directory or ""
    resolved = posixpath.normpath(posixpath.join(base, candidate))
    if resolved == ".":
        return None
    if resolved == ".." or resolved.startswith("../"):
        return None
    if repository_relative_parts(resolved) is None:
        return None
    return resolved


def bounded_shell_segments(command: str) -> tuple[str, ...]:
    """Split only separators admitted by current static dependency observers.

    This is intentionally not a shell AST. Segment ordinals are useful only for static
    source ordering and must never be treated as runtime command identity.
    """

    return tuple(
        segment.strip()
        for segment in re.split(r"(?:&&|\|\||;|\n)", command)
        if segment.strip()
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


__all__ = (
    "EffectiveWorkingDirectory",
    "WorkingDirectorySource",
    "WorkingDirectoryState",
    "bounded_shell_segments",
    "resolve_effective_working_directory",
    "resolve_repository_relative_path",
)
