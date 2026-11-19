"""Provider component proof; target scripts are parsed as inert text only."""

from __future__ import annotations

from dataclasses import FrozenInstanceError, replace
from hashlib import sha256
import json
from pathlib import Path
from textwrap import indent
import unittest
from unittest.mock import patch

from upgradepilot.github.repository import RepositoryTextFile
from upgradepilot.github.workflow_command_analysis import analyze_run_step_commands
from upgradepilot.github.workflow_definition import (
    RunStepDefinition, SourceSpan, StepsJobDefinition, WorkflowDefinition,
    WorkflowDefinitionProblem, _compose_workflow_yaml, parse_workflow_definition,
)
from upgradepilot.github.workflow_matrix import MatrixCoordinate, MatrixLiteral
from upgradepilot.github.workflow_specialization import (
    _SpecializationBudget, _specialize_scalar, prepare_workflow_job_instances,
)
from yaml.nodes import ScalarNode


def _source(text: str) -> RepositoryTextFile:
    return RepositoryTextFile("example/project", ".github/workflows/ci.yml", "a" * 40, text)


def _matrix(matrix: str, *, run: str = "echo ok", fields: str = ""):
    text = "jobs:\n  test:\n    runs-on: ubuntu-latest\n    strategy:\n      matrix:\n"
    text += indent(matrix.rstrip() + "\n", "        ")
    text += indent(fields, "    ")
    text += "    steps:\n      - run: |\n" + indent(run + "\n", "          ")
    return prepare_workflow_job_instances(_source(text))


def _values(instance):
    return {item.name: item.literal.value for item in instance.coordinates}


class LiteralMatrixExpansionTests(unittest.TestCase):
    def test_cartesian_axis_order_exclusion_and_include_original_row_semantics(self):
        result = _matrix("""fruit: [apple, pear]
animal: [cat, dog]
exclude:
  - fruit: pear
    animal: dog
include:
  - color: green
  - color: pink
    animal: cat
  - fruit: banana
  - fruit: banana
    animal: cat
""")
        job = result.jobs[0]
        self.assertEqual(job.state, "complete")
        self.assertEqual([_values(i) for i in job.instances], [
            {"fruit": "apple", "animal": "cat", "color": "pink"},
            {"fruit": "apple", "animal": "dog", "color": "green"},
            {"fruit": "pear", "animal": "cat", "color": "pink"},
            {"fruit": "banana"}, {"fruit": "banana", "animal": "cat"},
        ])
        self.assertEqual([i.original_axis_indices for i in job.instances],
                         [(0, 0), (0, 1), (1, 0), None, None])
        self.assertEqual(job.instances[0].include_indices, (0, 1))
        self.assertEqual(job.instances[4].include_indices, (3,))

    def test_partial_exclusion_and_include_reintroduction_preserve_provenance(self):
        result = _matrix("""os: [linux, windows]
py: ['3.12', '3.13']
exclude:
  - os: windows
include:
  - os: windows
    py: '3.12'
""")
        instances = result.jobs[0].instances
        self.assertEqual([i.original_axis_indices for i in instances], [(0, 0), (0, 1), None])
        self.assertEqual(_values(instances[-1]), {"os": "windows", "py": "3.12"})

    def test_repeated_coordinates_and_include_only_rows_remain_distinct(self):
        for matrix in ("py: ['3.12', '3.12']", "include: [{py: '3.12'}, {py: '3.12'}]"):
            with self.subTest(matrix=matrix):
                instances = _matrix(matrix).jobs[0].instances
                self.assertEqual(len(instances), 2)
                self.assertEqual(_values(instances[0]), _values(instances[1]))
                self.assertNotEqual(instances[0].identity, instances[1].identity)
                with self.assertRaises(FrozenInstanceError):
                    instances[0].identity.expansion_slot = 4

    def test_scalar_types_and_source_spelling_are_preserved(self):
        result = _matrix("""quoted: ['3.10']
flag: [TRUE]
empty: [null]
number: [+12]
legacy_word: [yes]
underscored: [1_000]
plain_version: [13.0.0]
digit_label: [123abc]
""")
        coordinates = {c.name: c.literal for c in result.jobs[0].instances[0].coordinates}
        self.assertEqual([(v.kind, v.value) for v in coordinates.values()], [
            ("string", "3.10"), ("boolean", True), ("null", None),
            ("integer", 12), ("string", "yes"), ("string", "1_000"),
            ("string", "13.0.0"), ("string", "123abc"),
        ])
        self.assertEqual(coordinates["quoted"].spelling, "'3.10'")
        self.assertEqual(coordinates["flag"].spelling, "TRUE")
        self.assertEqual(coordinates["number"].spelling, "+12")

    def test_alias_and_quoted_scalar_style_use_the_original_guarded_syntax(self):
        result = _matrix("py: [&python '3.10', *python]")
        instances = result.jobs[0].instances
        self.assertEqual([_values(i) for i in instances], [{"py": "3.10"}] * 2)
        self.assertEqual(instances[0].coordinates[0].literal.kind, "string")
        self.assertEqual(instances[0].coordinates[0].literal.span,
                         instances[1].coordinates[0].literal.span)

    def test_unqualified_types_expressions_comparisons_and_shapes_are_explicit(self):
        cases = {
            "value: [3.12]": "matrix_numeric_spelling_unsupported",
            "value: [01]": "matrix_numeric_spelling_unsupported",
            "value: [1e3]": "matrix_numeric_spelling_unsupported",
            "value: [9007199254740993]": "matrix_integer_precision_unsupported",
            "value: [" + "9" * 310 + "]": "matrix_integer_precision_unsupported",
            "value: [{nested: object}]": "matrix_non_scalar_value",
            "value: [!!str 'true']": "matrix_explicit_tag_unsupported",
            "value: ['${{ needs.prepare.outputs.version }}']": "matrix_dynamic_value",
            "value: [true, 'true']": "matrix_mixed_comparison_kinds",
            "value: [Linux, linux]": "matrix_case_only_value_collision",
            "value: [linux]\ninclude: [{value: LINUX}]": "matrix_case_only_value_collision",
            "value: [one]\nVALUE: [two]": "matrix_key_collision",
            "value: [one]\nvalue: [two]": "matrix_key_collision",
            "value: []": "matrix_axis_not_nonempty_sequence",
            "{}": "matrix_empty_declaration",
            "include: []": "matrix_empty_declaration",
            "include: [value]": "matrix_mapping_required",
            "value: [one]\ninclude: [{value: true}]": "matrix_mixed_comparison_kinds",
        }
        for matrix, reason in cases.items():
            with self.subTest(matrix=matrix):
                job = _matrix(matrix).jobs[0]
                self.assertEqual(job.state, "unresolved")
                self.assertEqual(job.instances, ())
                self.assertEqual(job.expansion.problem.reason, reason)

    def test_dynamic_matrix_and_unsupported_sibling_preserve_ordinary_jobs(self):
        result = prepare_workflow_job_instances(_source("""jobs:
  dynamic:
    strategy:
      matrix: ${{ fromJSON(needs.prepare.outputs.matrix) }}
    steps: [{run: echo dynamic}]
  ordinary:
    steps: [{run: echo ordinary}]
  delegate:
    uses: org/repo/.github/workflows/ci.yml@main
"""))
        self.assertEqual([job.state for job in result.jobs], ["unresolved", "complete", "unresolved"])
        self.assertEqual(result.jobs[1].instances[0].identity.kind, "ordinary")
        self.assertEqual(result.jobs[2].problem.reason, "reusable_workflow_specialization_unsupported")

    def test_job_limit_is_atomic_including_include_created_rows(self):
        for matrix in ("x: [one, two]\ny: [a, b]", "x: [one, two]\ninclude: [{x: three}]"):
            with self.subTest(matrix=matrix):
                with patch("upgradepilot.github.workflow_matrix.MAX_MATRIX_JOBS", 2):
                    job = _matrix(matrix).jobs[0]
                self.assertEqual(job.state, "incomplete")
                self.assertEqual(job.instances, ())
                self.assertEqual(job.expansion.rows, ())
                self.assertEqual(job.expansion.problem.reason, "matrix_expansion_limit")

    def test_excluding_every_row_is_a_complete_empty_expansion(self):
        job = _matrix("x: [one]\nexclude: [{x: one}]").jobs[0]
        self.assertEqual(job.state, "complete")
        self.assertEqual(job.instances, ())

    def test_documented_256_job_boundary_is_enforced_before_exclusion(self):
        axis = "x: [" + ", ".join(str(i) for i in range(256)) + "]"
        accepted = _matrix(axis).jobs[0]
        self.assertEqual((accepted.state, len(accepted.instances)), ("complete", 256))
        oversized = axis[:-1] + ", 256]\nexclude: [{x: 256}]"
        refused = _matrix(oversized).jobs[0]
        self.assertEqual((refused.state, refused.instances), ("incomplete", ()))


class WorkflowFieldSpecializationTests(unittest.TestCase):
    def test_direct_quoted_key_and_case_insensitive_lookups_have_utf8_ranges(self):
        run = "echo café '${{ matrix.PY }}' '${{ matrix['py'] }}'\n"
        instance = _matrix("py: ['3.12']", run=run).jobs[0].instances[0]
        field = instance.field(("steps", 0, "run"))
        self.assertEqual(field.generated_text, "echo café '3.12' '3.12'\n")
        self.assertEqual(len(field.replacements), 2)
        original = field.original_text.encode()
        generated = field.generated_text.encode()
        for replacement in field.replacements:
            self.assertTrue(original[replacement.original_start_byte:replacement.original_end_byte].startswith(b"${{"))
            self.assertEqual(generated[replacement.generated_start_byte:replacement.generated_end_byte], b"3.12")
        first = field.replacements[0]
        self.assertEqual(first.original_start_byte, len("echo café '".encode()))
        self.assertNotEqual(field.original_digest, field.generated_digest)

    def test_provider_substitution_does_not_shell_escape_inserted_values(self):
        instance = _matrix("value: ['first; echo second']", run="echo ${{ matrix.value }}").jobs[0].instances[0]
        field = instance.field(("steps", 0, "run"))
        self.assertEqual(field.generated_text, "echo first; echo second\n")
        # Component-only bridge. No target command is executed or runtime credited.
        definition = parse_workflow_definition(_source("jobs:\n  test:\n    runs-on: ubuntu-latest\n    steps: [{run: placeholder}]\n"))
        job = definition.jobs[0]
        step = job.steps[0]
        specialized_step = replace(step, command=replace(step.command, text=field.generated_text,
                                                        contains_expression=False))
        analysis = analyze_run_step_commands(definition, job, specialized_step)
        self.assertEqual([o.raw_source for o in analysis.command_occurrences], ["echo first", "echo second"])

    def test_quoted_property_key_handles_braces_escaped_quotes_and_unicode_values(self):
        instance = _matrix('"a}}b\'c": ["über😀"]',
                           run="echo ${{ matrix['a}}b''c'] }}").jobs[0].instances[0]
        field = instance.field(("steps", 0, "run"))
        self.assertEqual(field.generated_text, "echo über😀\n")
        replacement = field.replacements[0]
        self.assertEqual(field.generated_text.encode()[replacement.generated_start_byte:
                         replacement.generated_end_byte].decode(), "über😀")

    def test_exact_large_integer_retains_type_but_unqualified_text_conversion_is_unresolved(self):
        instance = _matrix("x: [1000000000000000000000]", run="echo ${{ matrix.x }}").jobs[0].instances[0]
        self.assertEqual(instance.coordinates[0].literal.kind, "integer")
        self.assertEqual(instance.field(("steps", 0, "run")).problem.reason,
                         "matrix_scalar_conversion_unsupported")

    def test_substitution_does_not_evaluate_inserted_expression_text_again(self):
        # Isolate the one-pass transformer boundary. Normal matrix declaration
        # admission separately refuses dynamic value expressions (tested above).
        span = SourceSpan(1, 1, 1, 2)
        coordinate = MatrixCoordinate("payload", MatrixLiteral("string", "${{ matrix.other }}", "literal", span), span)
        node = ScalarNode("tag:yaml.org,2002:str", "${{ matrix.payload }}",
                          start_mark=_compose_workflow_yaml("text").start_mark,
                          end_mark=_compose_workflow_yaml("text").end_mark)
        result = _specialize_scalar(node, ("run",), (coordinate,), True,
                                   _SpecializationBudget(), condition=False, boolean=False)
        self.assertEqual(result.generated_text, "${{ matrix.other }}")
        self.assertEqual(len(result.replacements), 1)

    def test_unsupported_expressions_missing_keys_and_incomplete_delimiters_refuse_whole_field(self):
        for expression, reason in (
            ("${{ matrix.absent }}", "matrix_property_missing"),
            ("${{ matrix.x || 'other' }}", "matrix_expression_unsupported"),
            ("${{ github.ref }}", "matrix_expression_unsupported"),
            ("${{ matrix.x", "matrix_expression_unterminated"),
        ):
            with self.subTest(expression=expression):
                field = _matrix("x: [one]", run="echo ${{ matrix.x }} " + expression).jobs[0].instances[0].fields[-1]
                self.assertEqual(field.state, "unresolved")
                self.assertEqual(field.problem.reason, reason)
                self.assertIsNone(field.generated_text)
                self.assertEqual(field.replacements, ())

    def test_field_context_rules_typed_booleans_and_condition_roles(self):
        result = prepare_workflow_job_instances(_source("""defaults:
  run:
    shell: ${{ matrix.shell }}
env:
  GLOBAL: ${{ matrix.x }}
jobs:
  test:
    strategy:
      fail-fast: true
      matrix:
        shell: [bash]
        enabled: [false]
        x: [12]
        empty: [null]
    if: ${{ matrix.enabled }}
    continue-on-error: ${{ matrix.enabled }}
    defaults:
      run:
        shell: ${{ matrix.shell }}
    steps:
      - name: Value ${{ matrix.x }}
        if: ${{ matrix.enabled }}
        run: echo ${{ matrix.empty }}-${{ matrix.enabled }}-${{ matrix.x }}
        shell: ${{ matrix.shell }}
        env:
          MODE: ${{ matrix.x }}
      - uses: ${{ matrix.shell }}
"""))
        instance = result.jobs[0].instances[0]
        self.assertEqual(instance.field(("if",)).problem.reason, "matrix_context_not_allowed")
        self.assertEqual(instance.field(("continue-on-error",)).value_kind, "boolean")
        self.assertIs(instance.field(("continue-on-error",)).value, False)
        condition = instance.field(("steps", 0, "if"))
        self.assertEqual((condition.role, condition.value), ("condition", False))
        self.assertEqual(instance.field(("steps", 0, "run")).generated_text, "echo -false-12")
        self.assertEqual(instance.field(("defaults", "run", "shell")).generated_text, "bash")
        self.assertEqual(instance.field(("steps", 0, "env", "MODE")).generated_text, "12")
        self.assertEqual(instance.field(("steps", 1, "uses")).problem.reason, "matrix_context_not_allowed")
        self.assertEqual(instance.field(("strategy", "fail-fast")).value, True)
        self.assertTrue(all(f.problem.reason == "matrix_context_not_allowed" for f in result.workflow_fields))

    def test_string_boolean_is_not_promoted_to_typed_error_handling(self):
        job = _matrix("enabled: ['false']", fields="continue-on-error: ${{ matrix.enabled }}\n").jobs[0]
        self.assertEqual(job.instances[0].field(("continue-on-error",)).problem.reason, "specialized_boolean_required")

    def test_duplicate_environment_keys_cannot_leave_a_positive_first_lookup(self):
        job = _matrix("x: [one]", fields="env:\n  MODE: first\n  MODE: second\n").jobs[0]
        self.assertEqual(job.instances[0].field(("env", "MODE")).state, "unresolved")

    def test_invalid_step_does_not_acquire_specialized_positive_fields(self):
        result = prepare_workflow_job_instances(_source("""jobs:
  test:
    steps:
      - run: echo one
        run: echo conflicting
      - run: echo healthy
"""))
        self.assertEqual(result.definition.jobs[0].steps[0].reason, "duplicate_material_key")
        fields = result.jobs[0].instances[0].fields
        self.assertEqual([f.path for f in fields], [("steps", 1, "run")])

    def test_generated_text_and_field_work_limits_are_explicit_and_atomic(self):
        for name, limit in (("_MAX_SPECIALIZED_BYTES", 10), ("_MAX_SPECIALIZED_FIELD_VISITS", 2)):
            with self.subTest(name=name):
                with patch("upgradepilot.github.workflow_specialization." + name, limit):
                    job = _matrix("x: [one, two]", run="echo ${{ matrix.x }}").jobs[0]
                self.assertEqual(job.state, "incomplete")
                self.assertEqual(job.instances, ())
                self.assertEqual(job.problem.reason, "workflow_specialization_limit")

    def test_workflow_field_limit_preserves_the_valid_original_definition(self):
        source = _source("env: {MODE: retained}\njobs: {test: {steps: [{run: echo ok}]}}\n")
        with patch("upgradepilot.github.workflow_specialization._MAX_SPECIALIZED_BYTES", 1):
            result = prepare_workflow_job_instances(source)
        self.assertEqual(result.definition, parse_workflow_definition(source))
        self.assertEqual(result.problem.reason, "workflow_specialization_limit")
        self.assertEqual(result.jobs, ())

    def test_ordinary_fields_and_base_definition_are_preserved_in_one_composition(self):
        source = _source("jobs:\n  test:\n    steps:\n      - run: echo café\n")
        with patch("upgradepilot.github.workflow_definition._compose_workflow_yaml", wraps=_compose_workflow_yaml) as compose:
            result = prepare_workflow_job_instances(source)
        self.assertEqual(compose.call_count, 1)
        self.assertEqual(result.definition, parse_workflow_definition(source))
        instance = result.jobs[0].instances[0]
        self.assertEqual(instance.identity.kind, "ordinary")
        field = instance.field(("steps", 0, "run"))
        self.assertEqual(field.original_text, field.generated_text)
        self.assertEqual(field.original_digest, field.generated_digest)
        self.assertEqual(field.replacements, ())

    def test_invalid_workflow_and_recursive_alias_keep_existing_parse_problem(self):
        for text in ("jobs: [", "root: &loop [*loop]", "env: []\njobs: {}\n"):
            result = prepare_workflow_job_instances(_source(text))
            self.assertIsInstance(result.definition, WorkflowDefinitionProblem)
            self.assertEqual(result.jobs, ())


class MapProxyWorkflowSpecializationTests(unittest.TestCase):
    def test_frozen_real_workflow_has_eight_separate_contexts_and_four_parseable_install_scripts(self):
        fixtures = Path(__file__).parent / "fixtures" / "github"
        receipt = json.loads((fixtures / "mapproxy-matrix-test.receipt.json").read_text())
        content = (fixtures / "mapproxy-matrix-test.yml").read_bytes()
        self.assertEqual(sha256(content).hexdigest(), receipt["fixture_sha256"])
        source = RepositoryTextFile(receipt["repository"], receipt["path"], receipt["revision"], content.decode())
        result = prepare_workflow_job_instances(source)
        self.assertEqual(result.definition.source.content.encode(), content)
        self.assertEqual([j.job_key for j in result.jobs], ["test", "coverage", "doc", "lint", "typechecking"])
        self.assertEqual([len(j.instances) for j in result.jobs], [4, 1, 1, 1, 1])
        self.assertEqual([j.state for j in result.jobs], ["complete"] * 5)
        variants = result.jobs[0].instances
        self.assertEqual([_values(i)["python-version"] for i in variants], ["3.12", "3.13", "3.14", "3.15"])
        scripts = [i.field(("steps", 3, "run")) for i in variants]
        self.assertEqual(len({f.generated_digest for f in scripts}), 1)
        self.assertEqual(len({i.identity for i in variants}), 4)
        self.assertEqual(len(scripts[0].original_text.encode()), 112)
        self.assertEqual(len(scripts[0].generated_text.encode()), 90)
        original_job = result.definition.jobs[0]
        self.assertIsInstance(original_job, StepsJobDefinition)
        original_step = original_job.steps[3]
        self.assertIsInstance(original_step, RunStepDefinition)
        for instance, field in zip(variants, scripts, strict=True):
            version = _values(instance)["python-version"]
            self.assertEqual(instance.field(("steps", 2, "name")).generated_text, f"Use python {version}")
            step = replace(original_step, command=replace(original_step.command,
                text=field.generated_text, contains_expression=False))
            analysis = analyze_run_step_commands(result.definition, original_job, step)
            self.assertEqual(analysis.state, "analyzable")
            self.assertEqual(len(analysis.command_occurrences), 4)
            requirement = analysis.command_occurrences[1]
            self.assertEqual(requirement.raw_source, "pip install -r requirements-tests.txt")
            self.assertIsNone(requirement.whole_step_relation)
            encoded = field.generated_text.encode()
            self.assertEqual(encoded[requirement.source_span.start_byte:requirement.source_span.end_byte].decode(), requirement.raw_source)
        self.assertEqual(result.definition, parse_workflow_definition(source))
        # Original MapProxy omits fail-fast. It is not synthesized as an observed
        # cancellation or runtime state by the static provider companion.
        self.assertFalse(any(f.path == ("strategy", "fail-fast") for f in variants[0].fields))


if __name__ == "__main__":
    unittest.main()
