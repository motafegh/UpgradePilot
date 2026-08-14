"""Interpret one static GitHub Actions job as partial artifact-environment evidence.

The first slice preserves exact repository/workflow/job provenance plus literal runner,
literal setup-python version, and visible installation of the changed dependency source.
It deliberately does not infer exact wheel tags from broad environment labels.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Literal

from ..github.repository import RepositoryFileEvidence, RepositoryTextFile, UnavailableRepositoryFile

type TargetArtifactEnvironmentFormationState = Literal["established", "not_observed"]
type TargetArtifactEnvironmentProblemState = Literal[
    "file_unavailable",
    "insufficient_file_provenance",
    "unsupported_workflow_path",
    "workflow_jobs_not_statically_readable",
    "multiple_or_zero_workflow_jobs",
    "unsupported_or_ambiguous_job_shape",
]


@dataclass(frozen=True, slots=True)
class TargetArtifactEnvironmentFact:
    value: str
    source: str


@dataclass(frozen=True, slots=True)
class TargetArtifactEnvironmentEvidence:
    repository: str
    revision: str
    workflow_path: str
    workflow_blob_sha: str
    job: str
    runner: TargetArtifactEnvironmentFact | None
    python_version: TargetArtifactEnvironmentFact | None
    dependency_environment_formation: TargetArtifactEnvironmentFormationState
    formation_source: str | None
    limitations: tuple[str, ...]
    exact_wheel_compatibility_state: Literal["unresolved"] = "unresolved"


@dataclass(frozen=True, slots=True)
class TargetArtifactEnvironmentProblem:
    state: TargetArtifactEnvironmentProblemState
    revision: str
    workflow_path: str
    detail: str
    repository: str | None = None
    job: str | None = None


type TargetArtifactEnvironmentResult = (
    TargetArtifactEnvironmentEvidence | TargetArtifactEnvironmentProblem
)

_JOB_PATTERN = re.compile(r"^(?P<indent>\s*)(?P<key>[A-Za-z0-9_.-]+):\s*(?:#.*)?$")
_RUN_PATTERN = re.compile(r"^(?P<indent>\s*)(?:-\s+)?run:\s*(?P<value>.*)$")
_PIP_INSTALL_PATTERN = re.compile(
    r"(?<![A-Za-z0-9_.-])(?:python(?:3)?\s+-m\s+pip|pip(?:3)?)\s+install\b",
    re.IGNORECASE,
)
_REQUIREMENT_PATTERN = re.compile(
    r"(?:^|\s)(?:-r|--requirement)(?:=|\s+)(?P<path>[^\s;&|]+)",
    re.IGNORECASE,
)


def interpret_target_artifact_environment(
    evidence: RepositoryFileEvidence,
    *,
    dependency_source_file: str,
) -> TargetArtifactEnvironmentResult:
    """Return bounded partial evidence for one statically readable workflow job."""

    source_file = _normalize_path(dependency_source_file)
    if not source_file:
        raise ValueError("dependency source file must be non-empty.")

    if isinstance(evidence, UnavailableRepositoryFile):
        return TargetArtifactEnvironmentProblem(
            state="file_unavailable",
            repository=evidence.repository,
            revision=evidence.revision,
            workflow_path=evidence.path,
            detail=evidence.detail,
        )

    assert isinstance(evidence, RepositoryTextFile)
    if not evidence.path.startswith(".github/workflows/") or not evidence.path.endswith(
        (".yml", ".yaml")
    ):
        return _problem(
            evidence,
            "unsupported_workflow_path",
            "Evidence must come from a GitHub Actions workflow YAML file.",
        )
    if (
        evidence.repository is None
        or evidence.returned_path != evidence.path
        or evidence.reported_byte_count is None
        or evidence.decoded_byte_count is None
        or evidence.retrieved_at is None
    ):
        return _problem(
            evidence,
            "insufficient_file_provenance",
            "Strong exact-revision RepositoryTextFile provenance is required.",
        )

    job_result = _single_job(evidence.content)
    if job_result is None:
        return _problem(
            evidence,
            "workflow_jobs_not_statically_readable",
            "The shallow reader could not identify the jobs mapping.",
        )
    if isinstance(job_result, int):
        return _problem(
            evidence,
            "multiple_or_zero_workflow_jobs",
            f"The first slice supports one job; observed {job_result}.",
        )

    job, job_indent, lines = job_result
    child_indent = _child_indent(lines, job_indent)
    if child_indent is None:
        return _problem(
            evidence,
            "unsupported_or_ambiguous_job_shape",
            "The identified job had no statically readable body.",
            job=job,
        )
    unsupported = _unsupported_shape(lines, child_indent)
    if unsupported is not None:
        return _problem(
            evidence,
            "unsupported_or_ambiguous_job_shape",
            unsupported,
            job=job,
        )

    limitations: list[str] = []
    runner = _read_runner(lines, child_indent, limitations)
    python_version, setup_problem = _read_setup_python(lines, limitations)
    if setup_problem is not None:
        return _problem(
            evidence,
            "unsupported_or_ambiguous_job_shape",
            setup_problem,
            job=job,
        )

    install_command = next(
        (
            command
            for command in _run_commands(lines, job_indent)
            if _installs_source_file(command, source_file)
        ),
        None,
    )
    if install_command is None:
        limitations.append("changed_dependency_environment_not_directly_observed")
        formation: TargetArtifactEnvironmentFormationState = "not_observed"
    else:
        formation = "established"

    return TargetArtifactEnvironmentEvidence(
        repository=evidence.repository,
        revision=evidence.revision,
        workflow_path=evidence.path,
        workflow_blob_sha=evidence.blob_sha,
        job=job,
        runner=runner,
        python_version=python_version,
        dependency_environment_formation=formation,
        formation_source=install_command,
        limitations=tuple(limitations),
    )


def _single_job(text: str) -> tuple[str, int, tuple[str, ...]] | int | None:
    lines = text.splitlines()
    jobs_index = next(
        (i for i, line in enumerate(lines) if line.strip() == "jobs:"),
        None,
    )
    if jobs_index is None:
        return None

    jobs_indent = len(lines[jobs_index]) - len(lines[jobs_index].lstrip())
    starts: list[tuple[int, int, str]] = []
    job_indent: int | None = None
    for index in range(jobs_index + 1, len(lines)):
        line = lines[index]
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())
        if indent <= jobs_indent:
            break
        match = _JOB_PATTERN.match(line)
        if match is None:
            continue
        if job_indent is None:
            job_indent = indent
        if indent == job_indent:
            starts.append((index, indent, match.group("key")))

    if len(starts) != 1:
        return len(starts)
    start, indent, key = starts[0]
    end = len(lines)
    for index in range(start + 1, len(lines)):
        line = lines[index]
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if len(line) - len(line.lstrip()) <= jobs_indent:
            end = index
            break
    return key, indent, tuple(lines[start + 1 : end])


def _child_indent(lines: tuple[str, ...], job_indent: int) -> int | None:
    return min(
        (
            len(line) - len(line.lstrip())
            for line in lines
            if line.strip()
            and not line.lstrip().startswith("#")
            and len(line) - len(line.lstrip()) > job_indent
        ),
        default=None,
    )


def _unsupported_shape(lines: tuple[str, ...], child_indent: int) -> str | None:
    direct = {
        line.strip().split(":", 1)[0]
        for line in lines
        if line.strip()
        and len(line) - len(line.lstrip()) == child_indent
        and ":" in line
    }
    if "uses" in direct:
        return "Reusable-workflow jobs are outside the first slice."
    if "container" in direct:
        return "Container jobs are outside the first slice."
    if any(line.strip().startswith("matrix:") for line in lines):
        return "Matrix jobs are outside the first slice."
    return None


def _read_runner(
    lines: tuple[str, ...],
    child_indent: int,
    limitations: list[str],
) -> TargetArtifactEnvironmentFact | None:
    matches = [
        line.strip()
        for line in lines
        if len(line) - len(line.lstrip()) == child_indent
        and line.strip().startswith("runs-on:")
    ]
    if len(matches) != 1:
        limitations.append("runner_not_statically_identified")
        return None

    source = matches[0]
    value = _literal(source.split(":", 1)[1].strip())
    if value is None:
        limitations.append("runner_not_literal")
        return None
    return TargetArtifactEnvironmentFact(value=value, source=source)


def _read_setup_python(
    lines: tuple[str, ...],
    limitations: list[str],
) -> tuple[TargetArtifactEnvironmentFact | None, str | None]:
    indexes = [
        index
        for index, line in enumerate(lines)
        if "uses:" in line and "actions/setup-python@" in line.lower()
    ]
    if len(indexes) > 1:
        return None, "Multiple setup-python steps are outside the first slice."
    if not indexes:
        limitations.append("setup_python_version_not_observed")
        return None, None

    start = indexes[0]
    step_indent = len(lines[start]) - len(lines[start].lstrip())
    for line in lines[start + 1 :]:
        if line.strip() and len(line) - len(line.lstrip()) <= step_indent and line.lstrip().startswith("-"):
            break
        stripped = line.strip()
        if stripped.startswith("python-version:"):
            value = _literal(stripped.split(":", 1)[1].strip())
            if value is None:
                limitations.append("setup_python_version_not_literal")
                return None, None
            return TargetArtifactEnvironmentFact(value=value, source=stripped), None

    limitations.append("setup_python_version_not_observed")
    return None, None


def _run_commands(lines: tuple[str, ...], job_indent: int) -> tuple[str, ...]:
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
            commands.append(_strip_quotes(value))
            index += 1
            continue

        block: list[str] = []
        index += 1
        while index < len(lines):
            line = lines[index]
            stripped = line.strip()
            indent = len(line) - len(line.lstrip())
            if stripped and indent <= run_indent:
                break
            if stripped and not stripped.startswith("#"):
                block.append(stripped)
            index += 1
        if block:
            commands.append("\n".join(block))
    return tuple(commands)


def _installs_source_file(command: str, source_file: str) -> bool:
    for segment in re.split(r"(?:&&|\|\||;|\n)", command):
        if _PIP_INSTALL_PATTERN.search(segment) is None:
            continue
        for match in _REQUIREMENT_PATTERN.finditer(segment):
            if _normalize_path(match.group("path").strip("'\"")) == source_file:
                return True
    return False


def _literal(value: str) -> str | None:
    value = value.split(" #", 1)[0].strip()
    if not value or "${{" in value or value.startswith(("[", "{", "|", ">")):
        return None
    return _strip_quotes(value)


def _normalize_path(path: str) -> str:
    path = path.strip().replace("\\", "/")
    while path.startswith("./"):
        path = path[2:]
    return path


def _strip_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def _problem(
    evidence: RepositoryTextFile,
    state: TargetArtifactEnvironmentProblemState,
    detail: str,
    *,
    job: str | None = None,
) -> TargetArtifactEnvironmentProblem:
    return TargetArtifactEnvironmentProblem(
        state=state,
        repository=evidence.repository,
        revision=evidence.revision,
        workflow_path=evidence.path,
        detail=detail,
        job=job,
    )


__all__ = (
    "TargetArtifactEnvironmentEvidence",
    "TargetArtifactEnvironmentFact",
    "TargetArtifactEnvironmentFormationState",
    "TargetArtifactEnvironmentProblem",
    "TargetArtifactEnvironmentProblemState",
    "TargetArtifactEnvironmentResult",
    "interpret_target_artifact_environment",
)
