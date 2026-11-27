"""One explicit workflow declaration and file-level predicates for existing samples.

The selected job supplies a static scenario. PyPI supplies exact-file observations
from releases already read for source association. Neither input observes an install.
"""

from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass, replace
from typing import Literal

from packaging.specifiers import SpecifierSet
from packaging.utils import InvalidSdistFilename, InvalidWheelFilename, parse_sdist_filename, parse_wheel_filename
from packaging.version import InvalidVersion, Version

from ..github.api import GitHubAcquisitionError, GitHubResponseError
from ..github.repository import GitHubRepositoryClient, RepositoryTextFile
from ..pypi.release import PublishedFileRequiresPython
from ..pypi.simple_index import PyPISimpleIndexClient, SimpleIndexBasis, SimpleIndexProblem
from ..repository_path import repository_relative_parts
from ..target.artifact_environment import (
    TargetArtifactEnvironmentEvidence, interpret_target_artifact_environment,
)
from ..target.python_specifier import PythonLineSpecifierEvaluation, evaluate_python_line_specifier


PYTHON_LINE = re.compile(r"[1-9][0-9]{0,4}\.(?:0|[1-9][0-9]{0,4})")
WORKFLOW_TEXT_LIMIT = 128 * 1024
RANKED_SAMPLE_BASIS = "stable_index_sample_for_declared_python_line"


@dataclass(frozen=True)
class SelectedSamplePythonJob:
    workflow_path: str
    job: str
    rank_adapters: bool = False

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
    rank_decisions: tuple[AdapterRankDecision, ...] = ()


@dataclass(frozen=True)
class AdapterRankDecision:
    package: str
    constraint: str
    state: Literal["pending", "confirmed", "unresolved"]
    reason: str
    index: SimpleIndexBasis | None = None
    checked_versions: int = 0
    unclassified_files: int = 0
    version: str | None = None
    file: SampleFilePythonAssessment | None = None
    exact_file: PublishedFileRequiresPython | None = None
    blocked_version: str | None = None


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


def acquire_sample_python_declaration(scenario, identity, dependency_paths, session):
    """Acquire and interpret the selected exact-head workflow without sampling releases."""
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
    return replace(scenario, python_line=version.value, python_location=version.source, reason="declared_python_line")


def annotate_sample_releases(scenario, sample_releases, observations):
    if scenario.python_line is None:
        return scenario
    releases = tuple(
        SampleReleasePythonAssessment(package, release, tuple(
            assess_sample_file_python(scenario.python_line, file) for file in observations.get((package, release), ())
        ))
        for package, release in sorted(sample_releases)
    )
    return replace(scenario, releases=releases)


def stable_sample_versions(raw_versions, constraint):
    """Use one stable version and visible constraint rule for both sampling modes."""
    specifier = SpecifierSet(constraint)
    for raw in raw_versions:
        try:
            version = Version(raw)
        except InvalidVersion:
            continue
        if not version.is_prerelease and not version.is_devrelease and specifier.contains(version):
            yield version, raw


class RankedAdapterSampler:
    """Hold one invocation's index reads and its index-to-release decisions."""

    def __init__(self, session, python_line, observations):
        self.client = PyPISimpleIndexClient(session=session)
        self.python_line = python_line
        self.observations = observations
        self.indices = {}
        self.decisions = {}

    def select(self, package, constraint):
        key = package, constraint
        if key in self.decisions:
            return self.decisions[key]
        if package not in self.indices:
            self.indices[package] = self.client.get_index(package)
        index = self.indices[package]
        if isinstance(index, SimpleIndexProblem):
            decision = AdapterRankDecision(package, constraint, "unresolved", index.reason)
        else:
            decision = self._rank(package, constraint, index)
        self.decisions[key] = decision
        return decision

    def _rank(self, package, constraint, index):
        specifier = SpecifierSet(constraint)
        versions = defaultdict(list)
        for parsed, raw in stable_sample_versions(index.versions, constraint):
            versions[parsed].append(raw)
        files = defaultdict(list)
        unclassified = 0
        for file in index.files:
            try:
                if file.filename.endswith(".whl"):
                    name, version, *_ = parse_wheel_filename(file.filename)
                else:
                    name, version = parse_sdist_filename(file.filename)
            except (InvalidSdistFilename, InvalidWheelFilename):
                unclassified += 1
                continue
            if name != package:
                return AdapterRankDecision(package, constraint, "unresolved", "index_file_package_mismatch", index.basis)
            if version in versions:
                files[version].append(file)
            elif not version.is_prerelease and not version.is_devrelease and specifier.contains(version):
                # A file naming a stable relevant release without a raw version
                # key still prevents a complete ordering at that position.
                versions[version] = []
        decision = AdapterRankDecision(package, constraint, "unresolved", "no_eligible_release",
                                       index.basis, unclassified_files=unclassified)
        for count, (version, names) in enumerate(sorted(versions.items(), reverse=True), start=1):
            decision = replace(decision, checked_versions=count)
            if len(names) == 1 and files[version]:
                rows = [assess_sample_file_python(self.python_line, file) for file in files[version]]
                eligible = [row for row in rows if row.state == "overlaps" and row.file.sha256]
                if eligible:
                    chosen = min(eligible, key=lambda row: row.file.filename)
                    return replace(decision, state="pending", reason="selected_from_index", version=names[0], file=chosen)
                if all(row.state == "yanked" or (row.state == "excludes" and row.file.sha256) for row in rows):
                    continue
            return replace(decision, reason="unclassified_candidate_version", blocked_version=str(version))
        return decision

    def record_exact_release(self, package, version, *, available):
        """Check exact file identity and predicates before provenance or source reads."""
        for key, decision in tuple(self.decisions.items()):
            if (decision.package, decision.version) != (package, version) or decision.state != "pending":
                continue
            self.decisions[key] = self._join(decision, available)
        return next((decision.reason for decision in self.decisions.values()
                     if (decision.package, decision.version) == (package, version)
                     and decision.state != "confirmed"), None)

    def _join(self, decision, available):
        if not available:
            return replace(decision, state="unresolved", reason="exact_release_unavailable")
        files = self.observations.get((decision.package, decision.version), ())
        selected = decision.file.file
        exact = next((file for file in files if file.filename == selected.filename), None)
        if exact is None:
            return replace(decision, state="unresolved", reason="exact_release_file_unestablished")
        if exact != selected:
            return replace(decision, state="unresolved", reason="exact_release_file_mismatch", exact_file=exact)
        return replace(decision, state="confirmed", reason="exact_release_file_matched", exact_file=exact)

    def finish_selection(self, package, constraint, reason):
        """Retain a refusal that occurred before the exact release could be checked."""
        key = package, constraint
        decision = self.decisions[key]
        if decision.state == "pending":
            self.decisions[key] = replace(decision, state="unresolved", reason=reason)
