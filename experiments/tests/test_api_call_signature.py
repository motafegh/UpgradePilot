"""Binding semantics and source/unknown boundaries, using locally authored controls.

The small trusted function bodies below are called only as Python binding oracles.
No retained project/library source is executed, installed or reflected over.
"""

import ast
from dataclasses import replace
from unittest import TestCase

from experiments.api_call_signature import (
    AnalysisLimit, SourceSpan, compare_arguments, extract_python_source,
)


def facts(text, *, complete=True):
    return extract_python_source("a" * 64, text, complete=complete)


def comparison(parameters, call, *, mode="as_written"):
    result = facts(f"def f({parameters}):\n pass\nf({call})\n")
    return compare_arguments(result.calls[-1], result.signatures[0], mode)


class ArgumentBindingTests(TestCase):
    def test_supported_binding_agrees_with_trusted_python_calls(self):
        controls = [
            ("a, b=None, *, c", "1, c=2", (1,), {"c": 2}),
            ("a, b=None, *, c", "1", (1,), {}),
            ("a, b=None, *, c", "1, 2, 3, c=2", (1, 2, 3), {"c": 2}),
            ("a, b=None, *, c", "1, a=2, c=3", (1,), {"a": 2, "c": 3}),
            ("a, b=None, *, c", "1, c=2, unknown=3", (1,), {"c": 2, "unknown": 3}),
            ("a, *items, **options", "1, 2, extra=4", (1, 2), {"extra": 4}),
            ("a, /, **options", "1, a=2", (1,), {"a": 2}),
            ("a, /, **options", "a=2", (), {"a": 2}),
            ("a, /", "a=1", (), {"a": 1}),
            ("*, c", "1", (1,), {}),
            ("*, c", "c=1", (), {"c": 1}),
            ("*items", "items=1", (), {"items": 1}),
            ("**options", "options=1", (), {"options": 1}),
            ("value=0, /, **options", "value=2", (), {"value": 2}),
            ("a, /, b=0, *, c=None", "1, c=2", (1,), {"c": 2}),
        ]
        for parameters, call, args, kwargs in controls:
            with self.subTest(parameters=parameters, call=call):
                namespace = {}
                # This source is a finite, locally authored test table, not input
                # supplied to the experiment or recovered from another project.
                exec(f"def control({parameters}):\n return None\n", namespace)
                try:
                    namespace["control"](*args, **kwargs)
                    expected = "bound"
                except TypeError:
                    expected = "rejected"
                result = comparison(parameters, call)
                self.assertEqual(result.outcome, expected)
                self.assertTrue(result.checks_complete)

    def test_optional_positional_only_name_can_enter_variadic_keywords(self):
        result = comparison("value=0, /, **options", "value=2")
        self.assertEqual(result.outcome, "bound")
        self.assertEqual(result.keyword_reception[0].outcome, "variadic_keyword")
        self.assertFalse(result.violations)

    def test_keyword_presence_is_not_deprecation_or_whole_compatibility(self):
        result = comparison("*, certificate=None", "certificate=None")
        self.assertEqual(result.outcome, "bound")
        self.assertIn("target_installed_versions_and_runtime_not_established", result.remaining_premises)

    def test_keyword_reception_survives_unknown_expansions_without_full_success(self):
        rejected = comparison("*, deadline=None", "*args, timeout=1, **options")
        self.assertEqual(rejected.outcome, "rejected")
        self.assertFalse(rejected.checks_complete)
        self.assertIn("unexpected_keyword", [v.reason for v in rejected.violations])
        unknown = comparison("*, timeout=None, **options", "timeout=1, **supplied")
        self.assertEqual(unknown.outcome, "undetermined")
        self.assertFalse(unknown.violations)
        self.assertIn("keyword_expansion_unresolved", unknown.unresolved_checks)

    def test_literal_unpacking_is_not_silently_evaluated(self):
        result = comparison("x", "*(1,), **{}")
        self.assertEqual(result.outcome, "undetermined")
        self.assertIn("positional_expansion_unresolved", result.unresolved_checks)

    def test_receiver_is_explicit_and_never_inferred_from_self_spelling(self):
        self.assertEqual(comparison("self, *, option=None", "option=1").outcome, "rejected")
        bound = comparison("receiver, *, option=None", "option=1", mode="one_receiver_assumed")
        self.assertEqual(bound.outcome, "bound")
        self.assertIn("one_bound_positional_receiver_assumed", bound.remaining_premises)
        self.assertEqual(comparison("self, *, option=None", "option=1", mode="unresolved").outcome, "undetermined")

    def test_incomplete_signature_cannot_prove_an_absent_parameter(self):
        parsed = facts("def f(): pass\nf(option=1)\n")
        result = compare_arguments(parsed.calls[0], replace(parsed.signatures[0], complete=False), "as_written")
        self.assertEqual(result.outcome, "undetermined")
        self.assertEqual(result.keyword_reception[0].outcome, "undetermined")
        self.assertFalse(result.violations)

    def test_missing_and_duplicate_binding_are_distinct_reasons(self):
        missing = comparison("x, *, y", "1")
        self.assertEqual([(v.reason, v.parameter) for v in missing.violations], [("missing_required_argument", "y")])
        duplicate = comparison("x", "1, x=2")
        self.assertIn("duplicate_argument", [v.reason for v in duplicate.violations])

    def test_package_and_parameter_names_are_not_special_rules(self):
        for module, keyword in [("bridge.transport", "application"), ("other.service", "retry")]:
            with self.subTest(module=module):
                parsed = facts(f"from {module} import send as S\ndef receive(*, different=None): pass\nS({keyword}=1)\n")
                result = compare_arguments(parsed.calls[0], parsed.signatures[0], "as_written")
                self.assertEqual(parsed.calls[0].binding.state, "established")
                self.assertEqual(result.violations[0].parameter, keyword)


class SourceExtractionTests(TestCase):
    def test_shared_binding_trace_disambiguates_same_line_calls(self):
        parsed = facts("from vendor import send\nsend(a=1); send(a=2)\n")
        self.assertEqual(len(parsed.calls), 2)
        self.assertNotEqual(parsed.calls[0].fact_id, parsed.calls[1].fact_id)
        self.assertNotEqual(parsed.calls[0].span, parsed.calls[1].span)
        self.assertTrue(all(c.binding.state == "established" for c in parsed.calls))
        self.assertEqual(parsed.calls[1].keywords, ("a",))

    def test_rebinding_and_dynamic_super_preserve_uncertainty(self):
        parsed = facts("from vendor import Client as C\nC()\nC=None\nC()\nclass K:\n def __init__(self):\n  super().__init__(option=1)\n")
        self.assertEqual(parsed.calls[0].binding.state, "established")
        self.assertNotEqual(parsed.calls[1].binding.state, "established")
        outer = next(c for c in parsed.calls if c.expression == "super().__init__")
        self.assertEqual(outer.binding.state, "unknown")
        self.assertEqual(outer.keywords, ("option",))

    def test_parameter_kinds_default_presence_and_header_are_source_facts(self):
        parsed = facts("async def f(a, /, b=None, *items, c, d=None, **options):\n return None\n")
        signature = parsed.signatures[0]
        self.assertEqual(signature.kind, "async_function")
        self.assertEqual([p.kind for p in signature.parameters], ["positional_only", "positional_or_keyword", "variadic_positional", "keyword_only", "keyword_only", "variadic_keyword"])
        self.assertEqual([p.has_default for p in signature.parameters], [False, True, False, False, True, False])
        self.assertEqual(signature.header_span.end_line, 2)

    def test_decorators_and_private_names_do_not_become_runtime_signatures(self):
        parsed = facts("@wrap\ndef f(*, option=None): pass\nf(option=1)\nclass C:\n def g(self, __hidden): pass\n")
        result = compare_arguments(parsed.calls[0], parsed.signatures[0], "as_written")
        self.assertIn("effective_decorator_signature_not_established", result.remaining_premises)
        self.assertIn("class_private_parameter_mangling_unsupported", parsed.signatures[1].limitations)

    def test_invalid_source_and_work_limits_never_return_an_empty_success(self):
        self.assertTrue(facts("def broken(").problems)
        with self.assertRaisesRegex(AnalysisLimit, "ast_node_limit"):
            extract_python_source("u", "f()", complete=True, max_nodes=1)
        with self.assertRaisesRegex(AnalysisLimit, "source_fact_limit"):
            extract_python_source("u", "f(); f()", complete=True, max_facts=1)

    def test_utf8_columns_and_arguments_match_real_ast_spans(self):
        text = "label='é'; f(1, *a, option=2, **b)\n"
        parsed = facts(text)
        node = next(n for n in ast.walk(ast.parse(text)) if isinstance(n, ast.Call))
        self.assertEqual(parsed.calls[0].span, SourceSpan.of(node))
        self.assertEqual(parsed.calls[0].positional, ("ordinary", "starred"))
        self.assertEqual(parsed.calls[0].keywords, ("option", None))
        self.assertEqual(len(parsed.calls[0].argument_spans), 4)
