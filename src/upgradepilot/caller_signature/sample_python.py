"""One explicit workflow declaration and file-level predicates for existing samples.

The selected job supplies a static scenario. PyPI supplies exact-file observations
from releases already read for source association. Neither input observes an install.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, replace
from typing import Literal

from ..github.api import GitHubAcquisitionError, GitHubResponseError
from ..github.repository import GitHubRepositoryClient, RepositoryTextFile
from ..pypi.release import PublishedFileRequiresPython
from ..repository_path import repository_relative_parts
from ..target.artifact_environment import (
    TargetArtifactEnvironmentEvidence, interpret_target_artifact_environment,
)
from ..target.python_specifier import PythonLineSpecifierEvaluation, evaluate_python_line_specifier


PYTHON_LINE = re.compile(r"[1-9][0-9]{0,4}\.(?:0|[1-9][0-9]{0,4})")
WORKFLOW_TEXT_LIMIT = 128 * 1024


@dataclass(frozen=True)
class SelectedSamplePythonJob:
    workflow_path: str
    job: str

    def __post_init__(self):
        if (len(self.workflow_path) > 256 or repository_relative_parts(self.workflow_path) is None
                or not re.fullmatch(r"\.github/workflows/[^/]+\.ya?ml", self.workflow_path)
                or not self.workflow_path.isprintable()):
            raise ValueError("Select one .yml or .yaml file under .github/workflows.")
        if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_-]{0,99}", self.job):
            raise ValueError("Select one static workflow job ID.")


@dataclass(frozen=True)
class SampleFilePythonAssessment:
    file: PublishedFileRequiresPython
    state: Literal["overlaps", "excludes", "unknown", "yanked"]
    witness_patch: str | None = None


@dataclass(frozen=True)
class SampleReleasePythonAssessment:
    package: str
    version: str
    files: tuple[SampleFilePythonAssessment, ...]

    @property
    def state(self) -> Literal["overlaps", "excludes", "unknown"]:
        states = {item.state for item in self.files} - {"yanked"}
        if "overlaps" in states:
            return "overlaps"
        return "excludes" if states == {"excludes"} else "unknown"


@dataclass(frozen=True)
class SamplePythonScenario:
    selection: SelectedSamplePythonJob
    repository: str
    revision: str
    dependency_path: str | None = None
    workflow_text: str | None = None
    python_line: str | None = None
    python_location: str | None = None
    reason: str = "workflow_lookup_not_attempted"
    releases: tuple[SampleReleasePythonAssessment, ...] = ()


def assess_sample_file_python(python_line: str, file: PublishedFileRequiresPython) -> SampleFilePythonAssessment:
    if file.yanked is True:
        return SampleFilePythonAssessment(file, "yanked")
    if file.yanked is False and file.requires_python:
        result = evaluate_python_line_specifier(python_line, file.requires_python)
        if isinstance(result, PythonLineSpecifierEvaluation):
            if result.contains_stable_release:
                return SampleFilePythonAssessment(file, "overlaps", str(result.witness_version))
            return SampleFilePythonAssessment(file, "excludes")
    return SampleFilePythonAssessment(file, "unknown")


def collect_sample_python_scenario(scenario, identity, dependency_paths, sample_releases, observations, session):
    """Acquire one exact-head workflow after core source work and check retained release facts."""
    if len(dependency_paths) != 1:
        return replace(scenario, reason="ambiguous_dependency_source")
    path, = dependency_paths
    scenario = replace(scenario, dependency_path=path)
    try:
        workflow = GitHubRepositoryClient(session=session).get_exact_head_text_file(
            identity, scenario.selection.workflow_path)
    except GitHubAcquisitionError as error:
        return replace(scenario, reason=error.reason)
    except GitHubResponseError:
        return replace(scenario, reason="malformed_workflow_response")
    if not isinstance(workflow, RepositoryTextFile):
        return replace(scenario, reason=workflow.reason)
    if len(workflow.content.encode()) > WORKFLOW_TEXT_LIMIT:
        return replace(scenario, reason="workflow_retention_limit")
    scenario = replace(scenario, workflow_text=workflow.content)
    declared = interpret_target_artifact_environment(
        workflow, dependency_source_file=path, consuming_job_key=scenario.selection.job)
    if not isinstance(declared, TargetArtifactEnvironmentEvidence):
        return replace(scenario, reason=declared.state)
    if "strategy_context_not_interpreted" in declared.limitations:
        return replace(scenario, reason="unsupported_workflow_strategy")
    if declared.dependency_installation_declaration != "observed":
        return replace(scenario, reason="dependency_installation_declaration_unestablished")
    version = declared.python_version
    if version is None or not PYTHON_LINE.fullmatch(version.value):
        return replace(scenario, reason="unsupported_declared_python_line")
    releases = tuple(
        SampleReleasePythonAssessment(package, release, tuple(
            assess_sample_file_python(version.value, file) for file in observations.get((package, release), ())
        ))
        for package, release in sorted(sample_releases)
    )
    return replace(scenario, python_line=version.value, python_location=version.source,
                   reason="declared_python_line", releases=releases)
