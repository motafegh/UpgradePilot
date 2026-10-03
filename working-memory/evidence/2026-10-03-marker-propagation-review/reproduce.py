"""Read-only composition diagnostic; synthetic provider input, no live PR/model proof.

Run from the repository root with PYTHONPATH=src .venv/bin/python <this path>.
The provider supplies exact source files; production analysis creates the dependency
context and the production static collector derives consumption. No prebuilt positive
membership evidence is injected. Output records behavior, not an acceptance verdict.
"""

import json
import subprocess
from dataclasses import asdict, fields
from unittest.mock import Mock

from packaging.markers import Marker

from upgradepilot.ci.workflow_commands import (
    WorkflowProjectEnvironmentSource,
    inspect_workflow_dependency_evidence,
)
from upgradepilot.dependency.analysis import (
    DependencyChangeAnalysis,
    analyze_dependency_change,
)
from upgradepilot.github.pull_request import ChangedFile, PullRequestIdentity
from upgradepilot.github.repository import GitHubRepositoryClient, RepositoryTextFile


def reproduce(marker: str | None, selected_extra: str) -> dict:
    repository = "example/marker-audit"
    base_sha, head_sha = "a" * 40, "b" * 40
    identity = PullRequestIdentity(
        repository=repository,
        number=1,
        title="Marker propagation diagnostic",
        state="open",
        merged=False,
        author="diagnostic",
        base_ref="main",
        base_sha=base_sha,
        head_ref="update",
        head_sha=head_sha,
        changed_files=1,
    )
    changed = ChangedFile(
        filename="pyproject.toml",
        status="modified",
        additions=1,
        deletions=1,
        changes=2,
        patch=None,
    )
    suffix = f"; {marker}" if marker else ""

    def exact(version: str, revision: str) -> RepositoryTextFile:
        content = (
            '[project]\nname = "demo"\nversion = "0.1.0"\n'
            "[project.optional-dependencies]\n"
            f"speed = ['numpy=={version}{suffix}']\nother = ['pytest']\n"
        )
        return RepositoryTextFile(
            repository=repository,
            revision=revision,
            path="pyproject.toml",
            content=content,
        )

    base, head = exact("1.0", base_sha), exact("2.0", head_sha)
    provider = Mock(spec=GitHubRepositoryClient)
    provider.get_pull_request_base_file.return_value = base
    provider.get_pull_request_head_file.return_value = head
    analysis = analyze_dependency_change(identity, (changed,), provider)
    assert isinstance(analysis, DependencyChangeAnalysis), analysis
    provider.get_pull_request_base_file.assert_called_once_with(
        identity, "pyproject.toml"
    )
    provider.get_pull_request_head_file.assert_called_once_with(
        identity, "pyproject.toml"
    )
    workflow = RepositoryTextFile(
        repository=repository,
        revision=head_sha,
        path=".github/workflows/test.yml",
        content=f"""name: test
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: pip install -e ".[{selected_extra}]"
""",
    )
    static = inspect_workflow_dependency_evidence(
        workflow,
        source_contexts=analysis.source_contexts,
        package=analysis.dependency.package,
        normalized_package=analysis.dependency.normalized_package,
        project_environment_sources=(
            WorkflowProjectEnvironmentSource(
                context=analysis.source_contexts[0],
                project_file=head,
            ),
        ),
    )
    return {
        "marker": marker,
        "selected_extra": selected_extra,
        "marker_truth_for_declared_python_3_12": (
            Marker(marker).evaluate({"python_version": "3.12"}) if marker else True
        ),
        "base_project": base.content,
        "head_project": head.content,
        "workflow": workflow.content,
        "context_fields": [field.name for field in fields(analysis.source_contexts[0])],
        "consumptions": [asdict(item) for item in static.consumptions],
    }


if __name__ == "__main__":
    result = {
        "reviewed_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip(),
        "source_tree": subprocess.check_output(
            ["git", "rev-parse", "HEAD:src"], text=True
        ).strip(),
        "proof_class": "synthetic exact-source composition diagnostic; no live CLI/runtime proof",
        "cases": [
            reproduce(marker, extra)
            for marker, extra in (
                ('python_version < "3.12"', "speed"),
                ('python_version >= "3.12"', "speed"),
                (None, "speed"),
                ('python_version < "3.12"', "other"),
            )
        ],
    }
    print(json.dumps(result, indent=2))
