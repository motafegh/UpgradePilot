"""Protect conditional optional requirements through normal acquisition/composition.

Providers supply exact synthetic files; product code extracts contexts, derives workflow
membership, and projects reports. These tests establish no live install/marker truth.
"""

from __future__ import annotations

import unittest
from unittest.mock import Mock

from upgradepilot.ci.workflow_commands import (
    WorkflowProjectEnvironmentSource,
    inspect_workflow_dependency_evidence,
)
from upgradepilot.dependency.analysis import (
    DependencyChangeAnalysis,
    analyze_dependency_change,
)
from upgradepilot.github.actions import WorkflowRun
from upgradepilot.github.pull_request import ChangedFile, PullRequestIdentity
from upgradepilot.github.repository import GitHubRepositoryClient, RepositoryTextFile
from upgradepilot.investigation import investigate_public_pull_request
from upgradepilot.pypi.release import PackageReleaseProblem
from upgradepilot.report import render_investigation_report
from upgradepilot.report_file import decode_report, encode_report
from upgradepilot.report_projection import project_investigation_report

_MARKER = 'python_version < "3.12"'
_IDENTITY = PullRequestIdentity(
    repository="example/conditional-dependency",
    number=1,
    title="Bump optional dependency",
    state="open",
    merged=False,
    author="dependency-bot",
    base_ref="main",
    base_sha="a" * 40,
    head_ref="update",
    head_sha="b" * 40,
    changed_files=1,
)
_CHANGED = ChangedFile(
    filename="pyproject.toml",
    status="modified",
    additions=1,
    deletions=1,
    changes=2,
    patch=None,
)


def _project(version: str, revision: str, marker: str | None, extras: str = ""):
    condition = f"; {marker}" if marker else ""
    return RepositoryTextFile(
        repository=_IDENTITY.repository,
        revision=revision,
        path="pyproject.toml",
        content=(
            '[project]\nname = "demo"\nversion = "0.1"\n'
            "[project.optional-dependencies]\n"
            f"speed = ['numpy{extras}=={version}{condition}']\nother = ['pytest']\n"
        ),
    )


def _provider(marker: str | None, extras: str = ""):
    provider = Mock(spec=GitHubRepositoryClient)
    provider.get_pull_request_base_file.return_value = _project(
        "1.0",
        _IDENTITY.base_sha,
        marker,
        extras,
    )
    head = _project("2.0", _IDENTITY.head_sha, marker, extras)
    provider.get_pull_request_head_file.return_value = head
    provider.get_exact_head_text_file.return_value = head
    return provider, head


def _workflow(extra: str = "speed", python: str = "3.12", *, all_extras: bool = False):
    command = "uv sync --all-extras" if all_extras else f'pip install -e ".[{extra}]"'
    return RepositoryTextFile(
        repository=_IDENTITY.repository,
        revision=_IDENTITY.head_sha,
        path=".github/workflows/test.yml",
        content=f"""name: test
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '{python}'
      - run: {command}
""",
    )


class ConditionalPyprojectConsumptionTests(unittest.TestCase):
    def test_normal_analysis_retains_marker_and_dependency_extras_separately(self):
        provider, _ = _provider(_MARKER, "[fast,gpu]")
        analysis = analyze_dependency_change(_IDENTITY, (_CHANGED,), provider)
        self.assertIsInstance(analysis, DependencyChangeAnalysis)
        context = analysis.source_contexts[0]
        self.assertEqual(context.extra, "speed")
        self.assertEqual(context.requirement_marker, _MARKER)
        self.assertEqual(context.requirement_extras, ("fast", "gpu"))
        self.assertEqual(context.revision, _IDENTITY.head_sha)

    def test_selected_marked_requirements_remain_unresolved_without_marker_environment(
        self,
    ):
        for marker, python, all_extras in (
            (_MARKER, "3.12", False),
            (_MARKER, "3.11", False),
            ('python_version >= "3.12"', "3.12", False),
            ('sys_platform == "win32" or python_version < "3.12"', "3.12", False),
            (_MARKER, "${{ matrix.python }}", False),
            (_MARKER, "3.12", True),
        ):
            with self.subTest(marker=marker, python=python):
                provider, head = _provider(marker)
                analysis = analyze_dependency_change(_IDENTITY, (_CHANGED,), provider)
                static = inspect_workflow_dependency_evidence(
                    _workflow(python=python, all_extras=all_extras),
                    source_contexts=analysis.source_contexts,
                    package="numpy",
                    normalized_package="numpy",
                    project_environment_sources=(
                        WorkflowProjectEnvironmentSource(
                            context=analysis.source_contexts[0],
                            project_file=head,
                        ),
                    ),
                )
                self.assertEqual(len(static.consumptions), 1)
                consumption = static.consumptions[0]
                self.assertEqual(consumption.state, "unresolved")
                self.assertEqual(
                    consumption.reason, "changed_requirement_marker_not_evaluated"
                )
                self.assertIn(marker, consumption.detail)
                self.assertEqual(consumption.unresolved_conditions, (marker,))

    def test_marker_does_not_override_unselected_extra(self):
        provider, head = _provider(_MARKER)
        analysis = analyze_dependency_change(_IDENTITY, (_CHANGED,), provider)
        static = inspect_workflow_dependency_evidence(
            _workflow(extra="other"),
            source_contexts=analysis.source_contexts,
            package="numpy",
            normalized_package="numpy",
            project_environment_sources=(
                WorkflowProjectEnvironmentSource(
                    context=analysis.source_contexts[0],
                    project_file=head,
                ),
            ),
        )
        self.assertEqual(static.consumptions[0].state, "not_established")

    def test_public_investigation_and_saved_report_preserve_condition_and_unconditional_control(
        self,
    ):
        for marker, expected in ((_MARKER, "unresolved"), (None, "supported")):
            with self.subTest(marker=marker):
                repository, _ = _provider(marker)
                repository.get_exact_head_workflow_file.return_value = _workflow()
                pull = Mock()
                pull.get_pull_request.return_value = _IDENTITY
                pull.get_changed_files.return_value = (_CHANGED,)
                actions = Mock()
                actions.get_exact_head_workflow_runs.return_value = (
                    WorkflowRun(
                        run_id=1,
                        workflow_id=1,
                        name="test",
                        event="pull_request",
                        head_sha=_IDENTITY.head_sha,
                        status="completed",
                        conclusion="success",
                        run_attempt=1,
                    ),
                )
                actions.get_workflow_jobs.return_value = ()
                package = Mock()
                package.get_release.return_value = PackageReleaseProblem(
                    state="version_not_found",
                    requested_package="numpy",
                    normalized_package="numpy",
                    requested_version="2.0",
                    source_url="https://pypi.org/pypi/numpy/2.0/json",
                    detail="Unrelated upstream capability unavailable in this controlled proof.",
                )
                investigation = investigate_public_pull_request(
                    _IDENTITY.repository,
                    _IDENTITY.number,
                    pull_client=pull,
                    actions_client=actions,
                    repository_client=repository,
                    package_client=package,
                    release_index_client=Mock(),
                    upstream_repository_resolver=Mock(),
                    tag_client=Mock(),
                    changelog_client=Mock(),
                    support_drop_evaluator=Mock(),
                )
                consumption = investigation.ci_coverage_result.workflows[
                    0
                ].consumptions[0]
                self.assertEqual(consumption.state, expected)
                report = project_investigation_report(investigation)
                opened = decode_report(encode_report(report))
                self.assertEqual(opened, report)
                if marker:
                    self.assertIn(marker, render_investigation_report(opened))
                    self.assertIn(
                        b"changed_requirement_marker_not_evaluated",
                        encode_report(opened),
                    )
                repository.get_pull_request_base_file.assert_called_once_with(
                    _IDENTITY,
                    "pyproject.toml",
                )
                repository.get_pull_request_head_file.assert_called_once_with(
                    _IDENTITY,
                    "pyproject.toml",
                )


if __name__ == "__main__":
    unittest.main()
