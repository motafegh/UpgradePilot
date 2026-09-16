"""Protect uv package-scope preservation across R3 selection and R4 reachability."""

from __future__ import annotations

import unittest

from upgradepilot.dependency.change import DependencyChangeSourceEvidence
from upgradepilot.dependency.environment import UvLockDependencyContext
from upgradepilot.dependency.environment_selection import observe_project_environment_selection
from upgradepilot.dependency.uv_reachability import evaluate_uv_selected_root_reachability
from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.github.workflow_command_analysis import (
    CommandSourceSpan,
    StaticCommandAnalysis,
    StaticCommandAtom,
    StaticCommandOccurrence,
)
from upgradepilot.github.workflow_command_shell import EffectiveShellContext
from upgradepilot.github.workflow_definition import (
    RunStepDefinition,
    SourceSpan,
    StaticScalarValue,
)

_REPOSITORY = "example/project"
_HEAD_SHA = "a" * 40
_SPAN = SourceSpan(start_line=1, start_column=1, end_line=1, end_column=2)
_SHELL_CONTEXT = EffectiveShellContext(
    state="resolved",
    source="step",
    syntax_family="bash",
    execution_profile="github_builtin_bash",
    raw_declaration="bash",
)


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


def _literal(value: str) -> StaticCommandAtom:
    return StaticCommandAtom(raw_source=value, literal_value=value, state="literal")


def _analysis() -> StaticCommandAnalysis:
    raw = "uv sync --all-packages --group docs"
    occurrence = StaticCommandOccurrence(
        source_order=0,
        source_span=CommandSourceSpan(
            start_byte=0,
            end_byte=len(raw.encode("utf-8")),
            start_line=0,
            start_column=0,
            end_line=0,
            end_column=len(raw.encode("utf-8")),
        ),
        raw_source=raw,
        executable=_literal("uv"),
        arguments=(
            _literal("sync"),
            _literal("--all-packages"),
            _literal("--group"),
            _literal("docs"),
        ),
        structural_context=("straightforward_top_level",),
    )
    return StaticCommandAnalysis(
        state="analyzable",
        shell_context=_SHELL_CONTEXT,
        command_occurrences=(occurrence,),
        problems=(),
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
            command_analysis=_analysis(),
        )
        self.assertEqual(observation.state, "observed")
        self.assertEqual(len(observation.declarations), 1)
        declaration = observation.declarations[0]
        self.assertEqual(declaration.package_scope, "all_workspace_packages")
        self.assertIsNotNone(declaration.command_location)

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
