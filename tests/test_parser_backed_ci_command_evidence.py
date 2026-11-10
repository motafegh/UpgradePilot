from __future__ import annotations

import unittest
from textwrap import indent
from unittest.mock import patch

from upgradepilot.ci.workflow_commands import inspect_workflow_dependency_evidence
from upgradepilot.dependency.change import DependencyChangeSourceEvidence
from upgradepilot.dependency.environment import RequirementsFileDependencyContext
from upgradepilot.dependency.package_manager_operation import parse_package_manager_operation
from upgradepilot.github.repository import RepositoryTextFile


_HEAD_SHA = "a" * 40
_PATH = ".github/workflows/ci.yml"


def _source(content: str) -> RepositoryTextFile:
    return RepositoryTextFile(
        repository="example/project",
        path=_PATH,
        revision=_HEAD_SHA,
        content=content,
    )


def _requirements_context() -> RequirementsFileDependencyContext:
    evidence = DependencyChangeSourceEvidence(
        path="requirements-dev.txt",
        file_format="exact_requirement",
        extraction_method="changed_file_patch",
    )
    return RequirementsFileDependencyContext(
        repository="example/project",
        revision=_HEAD_SHA,
        normalized_package="pytest",
        source_evidence=evidence,
    )


class ParserBackedCICommandEvidenceTests(unittest.TestCase):
    def _inspect_httpx_step(self, command: str, *, skipped: bool = False):
        condition = "        if: false\n" if skipped else ""
        workflow = (
            "jobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n"
            "      - uses: actions/checkout@v4\n      - run: |\n"
            f"{indent(command, '          ')}\n{condition}"
        )
        return inspect_workflow_dependency_evidence(
            _source(workflow),
            source_contexts=(),
            package="httpx",
            normalized_package="httpx",
        )

    def test_static_pin_retains_source_identity_even_in_a_skipped_step(self) -> None:
        command = "python -m pip install -r other.txt 'HTTPX[http2]==0.28.1' anyio==4.0"
        result = self._inspect_httpx_step(command, skipped=True)
        self.assertEqual(result.problems, ())
        self.assertEqual(result.consumptions, ())
        self.assertEqual(result.invocations, ())
        (request,) = result.version_requests
        self.assertEqual((request.workflow_path, request.workflow_revision), (_PATH, _HEAD_SHA))
        self.assertEqual((request.job_key, request.step_source_index), ("test", 1))
        self.assertEqual(request.command_location.source_order, 0)
        self.assertEqual(request.command_location.source_span.end_byte, len(command))
        self.assertEqual(request.request.normalized_package, "httpx")
        self.assertEqual(request.request.version, "0.28.1")
        self.assertEqual(request.request.requirement_token, "HTTPX[http2]==0.28.1")

    def test_literal_request_after_file_operand_keeps_its_own_version(self) -> None:
        for option in ("-r httpx==0.27.0", "--requirement=httpx==0.27.0"):
            with self.subTest(option=option):
                result = self._inspect_httpx_step(
                    f"pip install {option} httpx==0.29.0 httpx==0.29.0"
                )
                (request,) = result.version_requests
                self.assertEqual(request.request.version, "0.29.0")

    def test_requests_require_unambiguous_positional_exact_pin(self) -> None:
        for command in (
            "pip install -r httpx==0.27.0",
            "pip install --requirement=httpx==0.27.0",
            "pip install --index-url httpx==0.27.0 httpx==0.28.1",
            "pip install httpx==0.27.0 -r",
            "pip install httpx==0.27.0 -r \"$REQ_FILE\"",
            "pip install httpx==0.27.0 \"$EXTRA_ARGS\"",
            "pip install 'httpx==0.27.*'",
            "pip install 'httpx>=0.27.0'",
            "pip install 'httpx==0.27.0; python_version < \"3.12\"'",
            "pip install 'httpx @ https://example.invalid/httpx.whl'",
            "pip install httpx==0.27.0 httpx==0.28.1",
            "pip install anyio==4.0",
            "pip install httpx==0.27.0 && pytest",
            "if true; then pip install httpx==0.27.0; fi",
        ):
            with self.subTest(command=command):
                self.assertEqual(self._inspect_httpx_step(command).version_requests, ())

    def test_file_consumption_and_inline_request_share_one_pip_operation(self) -> None:
        workflow = """jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install -r requirements-dev.txt pytest==8.3.4
"""
        with patch(
            "upgradepilot.dependency.package_manager_operation.parse_package_manager_operation",
            wraps=parse_package_manager_operation,
        ) as parse_operation:
            result = inspect_workflow_dependency_evidence(
                _source(workflow),
                source_contexts=(_requirements_context(),),
                package="pytest",
                normalized_package="pytest",
            )
        parse_operation.assert_called_once()
        (consumption,) = result.consumptions
        (request,) = result.version_requests
        self.assertEqual(consumption.state, "supported")
        self.assertEqual(request.request.version, "8.3.4")
        self.assertEqual(request.command_location, consumption.command_location)

    def test_one_analysis_supplies_direct_requirements_and_package_invocation_locations(
        self,
    ) -> None:
        workflow = """jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: |
          pip install -r requirements-dev.txt
          pytest tests
"""

        result = inspect_workflow_dependency_evidence(
            _source(workflow),
            source_contexts=(_requirements_context(),),
            package="pytest",
            normalized_package="pytest",
        )

        self.assertEqual(result.problems, ())
        self.assertEqual(len(result.consumptions), 1)
        self.assertEqual(len(result.invocations), 1)

        consumption = result.consumptions[0]
        invocation = result.invocations[0]

        self.assertEqual(consumption.state, "supported")
        self.assertIsNotNone(consumption.command_location)
        assert consumption.command_location is not None
        self.assertEqual(consumption.command_location.source_order, 0)
        self.assertEqual(
            consumption.whole_step_relation,
            "first_ordinary_top_level_command_in_sequential_script",
        )
        self.assertEqual(
            consumption.execution_profile,
            "github_default_non_windows",
        )

        self.assertEqual(invocation.state, "observed")
        self.assertIsNotNone(invocation.command_location)
        assert invocation.command_location is not None
        self.assertEqual(invocation.command_location.source_order, 1)
        self.assertIsNone(invocation.whole_step_relation)
        self.assertEqual(
            invocation.execution_profile,
            "github_default_non_windows",
        )
        self.assertEqual(invocation.workflow_path, _PATH)
        self.assertEqual(invocation.workflow_revision, _HEAD_SHA)

    def test_quoted_package_text_does_not_manufacture_invocation(self) -> None:
        workflow = """jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: |
          pip install -r requirements-dev.txt
          echo "pytest tests"
"""

        result = inspect_workflow_dependency_evidence(
            _source(workflow),
            source_contexts=(_requirements_context(),),
            package="pytest",
            normalized_package="pytest",
        )

        self.assertEqual(len(result.consumptions), 1)
        self.assertEqual(result.invocations, ())

    def test_other_repository_checkout_does_not_rebind_parsed_evidence(self) -> None:
        workflow = """jobs:
  external:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          repository: example/other
      - run: |
          pip install -r requirements-dev.txt
          pytest tests
"""

        result = inspect_workflow_dependency_evidence(
            _source(workflow),
            source_contexts=(_requirements_context(),),
            package="pytest",
            normalized_package="pytest",
        )

        self.assertEqual(result.consumptions, ())
        self.assertEqual(result.invocations, ())

    def test_missing_static_runner_context_preserves_requirements_uncertainty(self) -> None:
        workflow = """jobs:
  test:
    steps:
      - uses: actions/checkout@v4
      - run: pip install -r requirements-dev.txt
"""

        result = inspect_workflow_dependency_evidence(
            _source(workflow),
            source_contexts=(_requirements_context(),),
            package="pytest",
            normalized_package="pytest",
        )

        self.assertEqual(len(result.consumptions), 1)
        self.assertEqual(result.consumptions[0].state, "unresolved")
        self.assertEqual(
            result.consumptions[0].reason,
            "direct_install_command_analysis_unresolved",
        )
        self.assertIsNone(result.consumptions[0].command_location)


if __name__ == "__main__":
    unittest.main()
