"""Read the bounded visible workflow-command subset used by the current CI rule.

The reader intentionally understands only a shallow indentation-based workflow shape
and visible ``run:`` commands. It does not evaluate general YAML, shell semantics,
reusable workflows, expressions, task runners, or transitive scripts. Ambiguity remains
``unresolved`` rather than being guessed.
"""

from __future__ import annotations

import re
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

type WorkflowCommandStatus = Literal["supported", "unresolved"]


@dataclass(frozen=True, slots=True)
class WorkflowCommandEvidence:
    """Result of applying the direct command rule to one workflow definition."""

    status: WorkflowCommandStatus
    reason: str
    detail: str
    job_count: int
    install_command: str | None = None
    execution_command: str | None = None


@dataclass(frozen=True, slots=True)
class _WorkflowJobDefinition:
    key: str
    commands: tuple[str, ...]


_JOB_KEY_PATTERN = re.compile(r"^(?P<indent>\s*)(?P<key>[A-Za-z0-9_.-]+):\s*(?:#.*)?$")
_RUN_PATTERN = re.compile(r"^(?P<indent>\s*)(?:-\s+)?run:\s*(?P<value>.*)$")
_PIP_INSTALL_PATTERN = re.compile(
    r"(?<![A-Za-z0-9_.-])(?:python(?:3)?\s+-m\s+pip|pip(?:3)?)\s+install\b",
    re.IGNORECASE,
)
_REQUIREMENT_PATTERN = re.compile(
    r"(?:^|\s)(?:-r|--requirement)(?:=|\s+)(?P<path>[^\s;&|]+)",
    re.IGNORECASE,
)


def inspect_workflow_commands(
    text: str,
    *,
    source_file: str,
    package: str,
    normalized_package: str,
) -> WorkflowCommandEvidence:
    """Decide whether one workflow directly installs and invokes the dependency."""

    jobs = _extract_job_definitions(text)
    if jobs is None:
        return WorkflowCommandEvidence(
            status="unresolved",
            reason="workflow_jobs_not_statically_readable",
            detail="The shallow workflow reader could not identify the jobs mapping.",
            job_count=0,
        )
    if len(jobs) != 1:
        return WorkflowCommandEvidence(
            status="unresolved",
            reason="multiple_or_zero_workflow_jobs",
            detail=(
                "The first rule supports one statically identifiable workflow job; "
                f"observed {len(jobs)} job definitions."
            ),
            job_count=len(jobs),
        )

    commands = jobs[0].commands
    install_command = next(
        (
            command
            for command in commands
            if _command_installs_source_file(command, source_file)
        ),
        None,
    )
    execution_command = next(
        (
            command
            for command in commands
            if _command_invokes_package(command, package, normalized_package)
        ),
        None,
    )

    if install_command is None or execution_command is None:
        missing: list[str] = []
        if install_command is None:
            missing.append(f"installation of {source_file!r}")
        if execution_command is None:
            missing.append(f"direct invocation of {package!r}")
        return WorkflowCommandEvidence(
            status="unresolved",
            reason="direct_dependency_exercise_not_proven",
            detail="Workflow commands did not prove " + " and ".join(missing) + ".",
            job_count=1,
            install_command=install_command,
            execution_command=execution_command,
        )

    return WorkflowCommandEvidence(
        status="supported",
        reason="source_installed_and_dependency_invoked",
        detail=(
            "The workflow installs the changed requirements file and directly "
            "invokes the changed package."
        ),
        job_count=1,
        install_command=install_command,
        execution_command=execution_command,
    )


def _extract_job_definitions(text: str) -> tuple[_WorkflowJobDefinition, ...] | None:
    lines = text.splitlines()
    jobs_index: int | None = None
    jobs_indent: int | None = None

    for index, line in enumerate(lines):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped == "jobs:":
            jobs_index = index
            jobs_indent = len(line) - len(line.lstrip())
            break

    if jobs_index is None or jobs_indent is None:
        return None

    starts: list[tuple[int, int, str]] = []
    job_indent: int | None = None
    for index in range(jobs_index + 1, len(lines)):
        line = lines[index]
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())
        if indent <= jobs_indent:
            break
        match = _JOB_KEY_PATTERN.match(line)
        if match is None:
            continue
        if job_indent is None:
            job_indent = indent
        if indent == job_indent:
            starts.append((index, indent, match.group("key")))

    if not starts:
        return ()

    definitions: list[_WorkflowJobDefinition] = []
    for position, (start, indent, key) in enumerate(starts):
        end = starts[position + 1][0] if position + 1 < len(starts) else len(lines)
        definitions.append(
            _WorkflowJobDefinition(
                key=key,
                commands=_extract_run_commands(lines[start + 1 : end], job_indent=indent),
            )
        )
    return tuple(definitions)


def _extract_run_commands(
    lines: Sequence[str],
    *,
    job_indent: int,
) -> tuple[str, ...]:
    commands: list[str] = []
    index = 0
    while index < len(lines):
        match = _RUN_PATTERN.match(lines[index])
        if match is None:
            index += 1
            continue

        run_indent = len(match.group("indent"))
        if run_indent <= job_indent:
            index += 1
            continue

        value = match.group("value").strip()
        if value and not value.startswith(("|", ">")):
            commands.append(_strip_matching_quotes(value))
            index += 1
            continue

        block: list[str] = []
        index += 1
        while index < len(lines):
            candidate = lines[index]
            stripped = candidate.strip()
            indent = len(candidate) - len(candidate.lstrip())
            if stripped and indent <= run_indent:
                break
            if stripped and not stripped.startswith("#"):
                block.append(stripped)
            index += 1
        if block:
            commands.append("\n".join(block))

    return tuple(commands)


def _command_installs_source_file(command: str, source_file: str) -> bool:
    normalized_source = _normalize_command_path(source_file)
    for segment in _shell_segments(command):
        if _PIP_INSTALL_PATTERN.search(segment) is None:
            continue
        for match in _REQUIREMENT_PATTERN.finditer(segment):
            candidate = match.group("path").strip("'\"")
            if _normalize_command_path(candidate) == normalized_source:
                return True
    return False


def _command_invokes_package(
    command: str,
    package: str,
    normalized_package: str,
) -> bool:
    candidates = {
        candidate.lower()
        for candidate in (package, normalized_package)
        if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", candidate)
    }
    prefixes = (
        "",
        "python -m ",
        "python3 -m ",
        "uv run ",
        "poetry run ",
        "pipenv run ",
        "coverage run -m ",
    )

    for segment in _shell_segments(command):
        segment = re.sub(
            r"^(?:[A-Za-z_][A-Za-z0-9_]*=[^\s]+\s+)+",
            "",
            segment.strip(),
        )
        for candidate in candidates:
            for prefix in prefixes:
                expected = f"{prefix}{candidate}"
                if re.match(
                    rf"^{re.escape(expected)}(?=\s|$)",
                    segment,
                    re.IGNORECASE,
                ):
                    return True
    return False


def _shell_segments(command: str) -> tuple[str, ...]:
    return tuple(
        segment.strip()
        for segment in re.split(r"(?:&&|\|\||;|\n)", command)
        if segment.strip()
    )


def _normalize_command_path(path: str) -> str:
    normalized = path.strip().replace("\\", "/")
    while normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized


def _strip_matching_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


__all__ = (
    "WorkflowCommandEvidence",
    "WorkflowCommandStatus",
    "inspect_workflow_commands",
)
