"""Protect uv package-scope preservation across R3 selection and R4 reachability."""

from __future__ import annotations

import unittest

from upgradepilot.dependency.change import DependencyChangeSourceEvidence
from upgradepilot.dependency.environment import UvLockDependencyContext
from upgradepilot.dependency.environment_selection import observe_project_environment_selection
from upgradepilot.dependency.uv_reachability import evaluate_uv_selected_root_reachability
from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.github.workflow_definition import (
    RunStepDefinition,
    SourceSpan,
    StaticScalarValue,
)

_REPOSITORY = "example/project"
_HEAD_SHA = "a" * 40
_SPAN = SourceSpan(start_line=1, start_column=1, end_line=1, end_column=2)


def _scalar(text: str) -> StaticScalarValue:
    return StaticScalarValue(
        text=text,
        contains_expression="${{" in text,
        span=_SPAN,
    )


def _step(command: str) -> RunStepDefinition:
    return RunStepDefinition(
        source_index=0,
        command=_scalar(command),
        name=None,
        condition=None,
        continue_on_error=None,
        shell=None,
        working_directory=None,
        span=_SPAN,
    )


def _file(path: str, content: str) -> RepositoryTextFile:
    return RepositoryTextFile(
        repository=_REPOSITORY,
        path=path,
        revision=_HEAD_SHA,
        content=content,
    )


class UvPackageScopeTests(unittest.TestCase):
    def test_all_packages_scope_prevents_false_negative_across_real_workspace_shape(self) -> None:
        """One bound member cannot exhaust a command that selects all workspace members."""

        lock = _file(
            "uv.lock",
            '''version = 1
revision = 1

[[package]]
name = "demo"
source = { editable = "." }
[package.dev-dependencies]
docs = [{ name = "pytest" }]

[[package]]
name = "workspace-member"
source = { editable = "packages/member" }
[package.dev-dependencies]
docs = [{ name = "soupsieve" }]

[[package]]
name = "pytest"
version = "9.0"
source = { registry = "https://pypi.org/simple" }

[[package]]
name = "soupsieve"
version = "2.8.4"
source = { registry = "https://pypi.org/simple" }
''',
        )

        observation = observe_project_environment_selection(
            _step("uv sync --all-packages --group docs"),
            project_file_path="pyproject.toml",
        )
        self.assertEqual(observation.state, "observed")
        self.assertEqual(len(observation.declarations), 1)
        declaration = observation.declarations[0]
        self.assertEqual(declaration.package_scope, "all_workspace_packages")

        context = UvLockDependencyContext(
            repository=_REPOSITORY,
            revision=_HEAD_SHA,
            normalized_package="soupsieve",
            source_evidence=DependencyChangeSourceEvidence(
                path="uv.lock",
                file_format="uv_lock",
                extraction_method="exact_base_head_files",
            ),
        )
        result = evaluate_uv_selected_root_reachability(
            context,
            declaration,
            lock_file=lock,
        )

        self.assertEqual(result.state, "unresolved")
        self.assertEqual(result.reason, "uv_selected_root_workspace_scope_not_exhausted")
        self.assertNotEqual(result.state, "not_established")


if __name__ == "__main__":
    unittest.main()
