from __future__ import annotations

import unittest
from unittest.mock import patch

from yaml.nodes import MappingNode, ScalarNode, SequenceNode

from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.github.workflow_definition import (
    JobProblem,
    ReusableWorkflowJobDefinition,
    RunStepDefinition,
    StaticMappingValue,
    StaticScalarValue,
    StaticSequenceValue,
    StepProblem,
    StepsJobDefinition,
    UsesStepDefinition,
    WorkflowDefinition,
    WorkflowDefinitionProblem,
    WorkflowYamlParseError,
    _compose_workflow_yaml,
    parse_workflow_definition,
)


def _mapping_value(node: MappingNode, key: str):
    for key_node, value_node in node.value:
        if isinstance(key_node, ScalarNode) and key_node.value == key:
            return value_node
    raise AssertionError(f"missing mapping key: {key}")


def _source(content: str, *, path: str = ".github/workflows/ci.yml") -> RepositoryTextFile:
    return RepositoryTextFile(
        path=path,
        revision="a" * 40,
        blob_sha="b" * 40,
        content=content.lstrip(),
    )


class WorkflowYamlDependencyBoundaryTests(unittest.TestCase):
    def test_base_loader_preserves_text_and_node_shapes(self) -> None:
        root = _compose_workflow_yaml(
            """
flag: true
runs-on: [self-hosted, linux]
runner:
  group: build-runners
""".lstrip()
        )

        self.assertIsInstance(root, MappingNode)
        assert isinstance(root, MappingNode)

        flag = _mapping_value(root, "flag")
        runs_on = _mapping_value(root, "runs-on")
        runner = _mapping_value(root, "runner")

        self.assertIsInstance(flag, ScalarNode)
        self.assertEqual(flag.value, "true")
        self.assertIsInstance(runs_on, SequenceNode)
        self.assertIsInstance(runner, MappingNode)

    def test_block_scalars_are_yaml_decoded_and_keep_source_marks(self) -> None:
        root = _compose_workflow_yaml(
            """
jobs:
  test:
    steps:
      - run: |
          echo one
          echo two
      - run: >
          echo three
          echo four
""".lstrip()
        )

        self.assertIsInstance(root, MappingNode)
        assert isinstance(root, MappingNode)
        jobs = _mapping_value(root, "jobs")
        assert isinstance(jobs, MappingNode)
        job = _mapping_value(jobs, "test")
        assert isinstance(job, MappingNode)
        steps = _mapping_value(job, "steps")
        assert isinstance(steps, SequenceNode)

        first = steps.value[0]
        second = steps.value[1]
        assert isinstance(first, MappingNode)
        assert isinstance(second, MappingNode)
        literal_run = _mapping_value(first, "run")
        folded_run = _mapping_value(second, "run")
        assert isinstance(literal_run, ScalarNode)
        assert isinstance(folded_run, ScalarNode)

        self.assertEqual(literal_run.value, "echo one\necho two\n")
        self.assertEqual(folded_run.value, "echo three echo four\n")
        self.assertEqual(literal_run.style, "|")
        self.assertEqual(folded_run.style, ">")
        self.assertGreaterEqual(literal_run.start_mark.line, 0)
        self.assertGreater(literal_run.end_mark.index, literal_run.start_mark.index)

    def test_duplicate_mapping_keys_remain_visible_before_conversion(self) -> None:
        root = _compose_workflow_yaml(
            """
jobs:
  test:
    runs-on: ubuntu-latest
  test:
    runs-on: windows-latest
""".lstrip()
        )

        self.assertIsInstance(root, MappingNode)
        assert isinstance(root, MappingNode)
        jobs = _mapping_value(root, "jobs")
        assert isinstance(jobs, MappingNode)

        job_keys = [
            key.value
            for key, _ in jobs.value
            if isinstance(key, ScalarNode)
        ]
        self.assertEqual(job_keys, ["test", "test"])

    def test_malformed_yaml_becomes_controlled_parse_error(self) -> None:
        with self.assertRaisesRegex(
            WorkflowYamlParseError,
            r"Workflow YAML could not be parsed at line \d+, column \d+\.",
        ):
            _compose_workflow_yaml("jobs:\n  test: [\n")

    def test_recursive_alias_is_rejected_by_graph_guard(self) -> None:
        with self.assertRaisesRegex(
            WorkflowYamlParseError,
            "recursive alias structure",
        ):
            _compose_workflow_yaml("root: &loop [*loop]\n")

    def test_depth_and_node_visit_limits_are_enforced(self) -> None:
        with patch(
            "upgradepilot.github.workflow_definition._MAX_NODE_DEPTH",
            2,
        ):
            with self.assertRaisesRegex(
                WorkflowYamlParseError,
                "nesting-depth limit",
            ):
                _compose_workflow_yaml("root: [[[value]]]\n")

        with patch(
            "upgradepilot.github.workflow_definition._MAX_NODE_VISITS",
            3,
        ):
            with self.assertRaisesRegex(
                WorkflowYamlParseError,
                "node traversal limit",
            ):
                _compose_workflow_yaml("root: [one, two, three]\n")


class WorkflowDefinitionIrTests(unittest.TestCase):
    def test_preserves_ordered_multi_job_structure_dynamic_values_and_steps(self) -> None:
        result = parse_workflow_definition(
            _source(
                """
defaults:
  run:
    shell: bash
    working-directory: repo
jobs:
  build:
    name: Build
    runs-on: ubuntu-latest
    if: github.event_name == 'pull_request'
    continue-on-error: false
    defaults:
      run:
        working-directory: package
    container: python:3.12
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Install
        run: |
          python -m pip install -r requirements.txt
        shell: bash
        working-directory: src
  test:
    needs: [build]
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
    steps:
      - run: python -m unittest
""",
            )
        )

        self.assertIsInstance(result, WorkflowDefinition)
        assert isinstance(result, WorkflowDefinition)
        self.assertEqual([job.key for job in result.jobs], ["build", "test"])

        build = result.jobs[0]
        test = result.jobs[1]
        self.assertIsInstance(build, StepsJobDefinition)
        self.assertIsInstance(test, StepsJobDefinition)
        assert isinstance(build, StepsJobDefinition)
        assert isinstance(test, StepsJobDefinition)

        self.assertEqual(build.source_index, 0)
        self.assertEqual(test.source_index, 1)
        assert build.name is not None
        assert build.runs_on is not None
        assert build.condition is not None
        assert build.continue_on_error is not None
        assert result.run_defaults is not None
        assert result.run_defaults.working_directory is not None
        assert build.run_defaults is not None
        assert build.run_defaults.working_directory is not None
        self.assertEqual(build.name.text, "Build")
        self.assertEqual(build.runs_on.text, "ubuntu-latest")
        self.assertEqual(build.condition.text, "github.event_name == 'pull_request'")
        self.assertEqual(build.continue_on_error.text, "false")
        self.assertEqual(result.run_defaults.working_directory.text, "repo")
        self.assertEqual(build.run_defaults.working_directory.text, "package")
        self.assertIsInstance(build.container, StaticScalarValue)

        self.assertIsInstance(test.needs, StaticSequenceValue)
        self.assertIsInstance(test.runs_on, StaticScalarValue)
        assert isinstance(test.runs_on, StaticScalarValue)
        self.assertTrue(test.runs_on.contains_expression)
        self.assertIsInstance(test.strategy, StaticMappingValue)

        self.assertEqual(len(build.steps), 2)
        self.assertIsInstance(build.steps[0], UsesStepDefinition)
        self.assertIsInstance(build.steps[1], RunStepDefinition)
        uses = build.steps[0]
        run = build.steps[1]
        assert isinstance(uses, UsesStepDefinition)
        assert isinstance(run, RunStepDefinition)
        self.assertEqual(uses.source_index, 0)
        self.assertEqual(uses.reference.text, "actions/checkout@v4")
        self.assertIsInstance(uses.with_inputs, StaticMappingValue)
        self.assertEqual(run.source_index, 1)
        self.assertEqual(run.command.text, "python -m pip install -r requirements.txt\n")
        assert run.shell is not None
        assert run.working_directory is not None
        self.assertEqual(run.shell.text, "bash")
        self.assertEqual(run.working_directory.text, "src")
        self.assertGreater(run.span.start_line, 0)

    def test_preserves_reusable_workflow_job_without_expanding_it(self) -> None:
        result = parse_workflow_definition(
            _source(
                """
jobs:
  delegate:
    needs: prep
    if: ${{ success() }}
    uses: org/repo/.github/workflows/reusable.yml@main
    with:
      python-version: "3.12"
""",
            )
        )

        self.assertIsInstance(result, WorkflowDefinition)
        assert isinstance(result, WorkflowDefinition)
        job = result.jobs[0]
        self.assertIsInstance(job, ReusableWorkflowJobDefinition)
        assert isinstance(job, ReusableWorkflowJobDefinition)
        self.assertEqual(job.key, "delegate")
        self.assertEqual(job.uses.text, "org/repo/.github/workflows/reusable.yml@main")
        assert job.condition is not None
        self.assertTrue(job.condition.contains_expression)
        self.assertIsInstance(job.with_inputs, StaticMappingValue)

    def test_duplicate_job_identity_is_workflow_level_problem(self) -> None:
        result = parse_workflow_definition(
            _source(
                """
jobs:
  test:
    steps:
      - run: echo one
  test:
    steps:
      - run: echo two
""",
            )
        )

        self.assertIsInstance(result, WorkflowDefinitionProblem)
        assert isinstance(result, WorkflowDefinitionProblem)
        self.assertEqual(result.reason, "duplicate_job_id")

    def test_local_job_problem_does_not_destroy_other_readable_jobs(self) -> None:
        result = parse_workflow_definition(
            _source(
                """
jobs:
  broken:
    uses: org/repo/.github/workflows/reusable.yml@main
    steps:
      - run: echo impossible
  healthy:
    runs-on: ubuntu-latest
    steps:
      - run: echo ok
""",
            )
        )

        self.assertIsInstance(result, WorkflowDefinition)
        assert isinstance(result, WorkflowDefinition)
        self.assertIsInstance(result.jobs[0], JobProblem)
        self.assertIsInstance(result.jobs[1], StepsJobDefinition)
        broken = result.jobs[0]
        assert isinstance(broken, JobProblem)
        self.assertEqual(broken.reason, "ambiguous_job_shape")

    def test_local_step_problem_preserves_sibling_step_order(self) -> None:
        result = parse_workflow_definition(
            _source(
                """
jobs:
  test:
    steps:
      - run: echo one
        uses: actions/checkout@v4
      - run: echo two
""",
            )
        )

        self.assertIsInstance(result, WorkflowDefinition)
        assert isinstance(result, WorkflowDefinition)
        job = result.jobs[0]
        assert isinstance(job, StepsJobDefinition)
        self.assertIsInstance(job.steps[0], StepProblem)
        self.assertIsInstance(job.steps[1], RunStepDefinition)
        problem = job.steps[0]
        assert isinstance(problem, StepProblem)
        self.assertEqual(problem.reason, "ambiguous_step_shape")

    def test_malformed_yaml_and_non_workflow_path_return_typed_problems(self) -> None:
        malformed = parse_workflow_definition(_source("jobs:\n  test: [\n"))
        wrong_path = parse_workflow_definition(_source("jobs: {}\n", path="ci.yml"))

        self.assertIsInstance(malformed, WorkflowDefinitionProblem)
        self.assertIsInstance(wrong_path, WorkflowDefinitionProblem)
        assert isinstance(malformed, WorkflowDefinitionProblem)
        assert isinstance(wrong_path, WorkflowDefinitionProblem)
        self.assertEqual(malformed.reason, "workflow_yaml_parse_error")
        self.assertEqual(wrong_path.reason, "unsupported_workflow_path")


if __name__ == "__main__":
    unittest.main()
