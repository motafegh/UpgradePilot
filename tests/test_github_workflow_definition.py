from __future__ import annotations

import unittest
from unittest.mock import patch

from yaml.nodes import MappingNode, ScalarNode, SequenceNode

from upgradepilot.github.workflow_definition import (
    WorkflowYamlParseError,
    _compose_workflow_yaml,
)


def _mapping_value(node: MappingNode, key: str):
    for key_node, value_node in node.value:
        if isinstance(key_node, ScalarNode) and key_node.value == key:
            return value_node
    raise AssertionError(f"missing mapping key: {key}")


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


if __name__ == "__main__":
    unittest.main()
