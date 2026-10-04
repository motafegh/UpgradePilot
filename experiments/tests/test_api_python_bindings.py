"""Independent source controls for ordered/scoped origins, traces and limitations."""

from unittest import TestCase

from experiments.api_target_context import extract_python_facts
from upgradepilot.github.repository import RepositoryTextFile

SOURCE = "owner/target@" + "a" * 40 + ":arbitrary.py"


def facts(text):
    imports, references, gaps = extract_python_facts(
        RepositoryTextFile("owner/target", "arbitrary.py", "a" * 40, text)
    )
    assert not gaps, gaps
    return imports, references


class BindingTests(TestCase):
    def test_before_after_unknown_rebinding_and_saved_alias_restoration(self):
        _, refs = facts(
            "from bridge.testing import Client as C\nsaved = C\nC(app)\nC = 42\nC(app)\nC = saved\nC(app)\n"
        )
        self.assertEqual(
            [r.lexical_import for r in refs],
            ["bridge.testing.Client", None, "bridge.testing.Client"],
        )
        self.assertEqual(
            [r.binding.state for r in refs], ["established", "unknown", "established"]
        )
        self.assertEqual(
            [
                (s.line, s.operation)
                for s in refs[-1].binding.trace
                if s.operation in {"alias_copy", "assignment_unknown"}
            ],
            [(2, "alias_copy"), (4, "assignment_unknown"), (6, "alias_copy")],
        )
        for ref in refs:
            self.assertTrue(all(s.source_id == SOURCE for s in ref.binding.trace))

    def test_alias_chains_reimports_and_renamed_equivalent_sources(self):
        for module, member, alias in [
            ("bridge.testing", "Client", "C"),
            ("different.tools", "Handler", "H"),
        ]:
            with self.subTest(module=module):
                _, refs = facts(
                    f"from {module} import {member} as {alias}\nA = {alias}\nB = A\nB()\n{alias}=None\nfrom {module} import {member} as {alias}\n{alias}()\n"
                )
                self.assertEqual(
                    [r.lexical_import for r in refs], [f"{module}.{member}"] * 2
                )
                self.assertEqual(
                    refs[0].binding.possible_imports, (f"{module}.{member}",)
                )

    def test_rebinding_to_a_different_known_origin_is_not_unknown(self):
        _, refs = facts(
            "from alpha import Client as C\nfrom beta import Other as O\nC()\nC=O\nC()\n"
        )
        self.assertEqual(
            [r.lexical_import for r in refs], ["alpha.Client", "beta.Other"]
        )

    def test_plain_dotted_import_and_annotated_alias(self):
        _, refs = facts(
            "import vendor.client\nvendor.client.Client()\nfrom vendor import Client as C\nS: object = C\nS()\n"
        )
        self.assertEqual(
            [r.lexical_import for r in refs], ["vendor.client.Client", "vendor.Client"]
        )

    def test_unrelated_function_parameter_preserves_module_binding(self):
        _, refs = facts("from vendor import Client as C\ndef f(C):\n return C()\nC()\n")
        self.assertIsNone(refs[0].lexical_import)
        self.assertEqual(refs[0].binding.state, "unknown")
        self.assertEqual(refs[1].lexical_import, "vendor.Client")
        self.assertNotEqual(refs[0].binding.scope, refs[1].binding.scope)

    def test_function_local_import_is_independent_and_can_be_restored(self):
        imports, refs = facts(
            "def f():\n from vendor import Client as C\n S=C\n C=None\n C=S\n return C()\n"
        )
        self.assertEqual(refs[0].lexical_import, "vendor.Client")
        self.assertFalse(imports[0].module_level)
        self.assertIn("function:f", refs[0].binding.scope)

    def test_function_wide_local_rule_prevents_using_an_earlier_global(self):
        _, refs = facts(
            "from vendor import Client as C\ndef f():\n C()\n C=None\n C()\n"
        )
        self.assertEqual([r.binding.state for r in refs], ["unbound", "unknown"])
        self.assertTrue(all(r.lexical_import is None for r in refs))
        self.assertIn("unbound_local_name", refs[0].binding.reasons)

    def test_local_import_later_in_function_is_also_a_local_write(self):
        _, refs = facts(
            "from alpha import Client as C\ndef f():\n C()\n from beta import Client as C\n C()\n"
        )
        self.assertEqual(refs[0].binding.state, "unbound")
        self.assertEqual(refs[1].lexical_import, "beta.Client")

    def test_delayed_global_read_never_uses_definition_time_as_proof(self):
        _, refs = facts(
            "from vendor import Client as C\ndef f():\n return C()\nf()\nC=None\n"
        )
        self.assertIsNone(refs[0].lexical_import)
        self.assertIn("delayed_global_read", refs[0].binding.reasons)

    def test_closure_and_nonlocal_do_not_become_local_import_proof(self):
        _, refs = facts(
            "def outer():\n from vendor import Client as C\n def inner():\n  nonlocal C\n  return C()\n C=None\n return inner()\n"
        )
        self.assertTrue(all(r.lexical_import is None for r in refs))
        inner = next(r for r in refs if r.line == 5)
        self.assertIn("closure_or_nonlocal_read", inner.binding.reasons)

    def test_global_write_in_another_function_stays_explicitly_uncertain(self):
        _, refs = facts(
            "from vendor import Client as C\ndef mutate():\n global C\n C=None\nmutate()\nC()\n"
        )
        self.assertIsNone(refs[-1].lexical_import)
        self.assertIn("cross_scope_global_mutation", refs[-1].binding.reasons)

    def test_class_namespace_and_method_scope_are_separate(self):
        _, refs = facts(
            "from vendor import Client as C\nclass Wrapper(C):\n C=None\n def method(self):\n  return C()\nC()\n"
        )
        self.assertEqual(refs[0].lexical_import, "vendor.Client")
        self.assertIsNone(refs[1].lexical_import)
        self.assertEqual(refs[2].lexical_import, "vendor.Client")

    def test_agreeing_branches_preserve_the_origin_without_choosing_a_path(self):
        _, refs = facts(
            "if flag:\n from vendor import Client as C\nelse:\n from vendor import Client as C\nC()\n"
        )
        self.assertEqual(refs[0].lexical_import, "vendor.Client")
        self.assertEqual(
            [s.line for s in refs[0].binding.trace if s.operation == "import"], [2, 4]
        )

    def test_differing_unknown_and_unbound_paths_preserve_alternatives(self):
        for other, origins, unknown, unbound in [
            (
                "from other import Client as C",
                ("other.Client", "vendor.Client"),
                False,
                False,
            ),
            ("C=None", ("vendor.Client",), True, False),
            ("del C", ("vendor.Client",), False, True),
        ]:
            with self.subTest(other=other):
                _, refs = facts(
                    "from vendor import Client as C\nif flag:\n pass\nelse:\n "
                    + other
                    + "\nC()\n"
                )
                value = refs[0].binding
                self.assertIsNone(refs[0].lexical_import)
                self.assertEqual(value.state, "conditional")
                self.assertEqual(value.possible_imports, origins)
                self.assertEqual(
                    (value.unknown_possible, value.unbound_possible), (unknown, unbound)
                )

    def test_conditional_import_missing_arm_is_not_promoted(self):
        _, refs = facts("if backend:\n import httpx\nhttpx.Client()\n")
        self.assertIsNone(refs[0].lexical_import)
        self.assertEqual(refs[0].binding.possible_imports, ("httpx.Client",))
        self.assertTrue(refs[0].binding.unbound_possible)

    def test_deletion_and_reimport_recover_without_claiming_unknown_is_unbound(self):
        _, refs = facts(
            "from vendor import Client as C\nC=None\nC()\ndel C\nC()\nfrom vendor import Client as C\nC()\n"
        )
        self.assertEqual(
            [r.binding.state for r in refs], ["unknown", "unbound", "established"]
        )
        self.assertEqual(refs[-1].lexical_import, "vendor.Client")
        self.assertIn("delete", [s.operation for s in refs[-1].binding.trace])

    def test_star_import_invalidation_and_explicit_reimport(self):
        _, refs = facts(
            "from vendor import Client as C\nC()\nfrom other import *\nC()\nfrom vendor import Client as C\nC()\n"
        )
        self.assertEqual(
            [r.lexical_import for r in refs], ["vendor.Client", None, "vendor.Client"]
        )
        self.assertIn("star_import_namespace_unknown", refs[1].binding.reasons)

    def test_unsupported_loop_try_with_match_invalidate_affected_names(self):
        for body in [
            "for x in items:\n C=None\n",
            "try:\n C=None\nexcept Exception:\n pass\n",
            "with context as C:\n pass\n",
            "match x:\n case C:\n  pass\n",
        ]:
            with self.subTest(body=body):
                _, refs = facts(
                    "from vendor import Client as C\nfrom other import Stable as S\n"
                    + body
                    + "C()\nS()\n"
                )
                self.assertIsNone(refs[-2].lexical_import)
                self.assertIn(
                    "unsupported_write_or_control_flow", refs[-2].binding.reasons
                )
                self.assertEqual(refs[-1].lexical_import, "other.Stable")

    def test_augmented_and_unpacking_assignment_do_not_keep_stale_origins(self):
        for body in ["C += 1", "C, x = values"]:
            with self.subTest(body=body):
                _, refs = facts("from vendor import Client as C\n" + body + "\nC()\n")
                self.assertIsNone(refs[0].lexical_import)

    def test_mutated_imported_receiver_invalidates_saved_aliases(self):
        _, refs = facts(
            "import vendor as V\nS=V\nV.Client()\nV.Client=None\nS.Client()\n"
        )
        self.assertEqual(refs[0].lexical_import, "vendor.Client")
        self.assertIsNone(refs[1].lexical_import)
        self.assertIn("attribute_or_subscript_write", refs[1].binding.reasons)

    def test_subscript_write_in_unsupported_loop_invalidates_receiver(self):
        _, refs = facts("import vendor as V\nfor x in items:\n V[x]=None\nV.Client()\n")
        self.assertIsNone(refs[-1].lexical_import)

    def test_dynamic_namespace_operation_prevents_later_positive(self):
        _, refs = facts('from vendor import Client as C\nexec("C=None")\nC()\n')
        self.assertIsNone(refs[-1].lexical_import)
        self.assertIn("dynamic_namespace_operation", refs[-1].binding.reasons)

    def test_lambda_comprehension_targets_do_not_shadow_module_names(self):
        _, refs = facts(
            "from vendor import Client as C\nf=lambda C: C()\nxs=[C() for C in items]\nC()\n"
        )
        self.assertTrue(all(r.lexical_import is None for r in refs[:-1]))
        self.assertEqual(refs[-1].lexical_import, "vendor.Client")

    def test_callee_snapshot_precedes_argument_assignment_effect(self):
        _, refs = facts("from vendor import Client as C\nC((C := None))\nC()\n")
        self.assertEqual(refs[0].lexical_import, "vendor.Client")
        self.assertIsNone(refs[1].lexical_import)

    def test_relative_import_never_becomes_absolute_external_origin(self):
        _, refs = facts("from .local import Client as C\nS=C\nS()\n")
        self.assertIsNone(refs[0].lexical_import)
        self.assertIn("relative_import_origin_unresolved", refs[0].binding.reasons)

    def test_trace_budget_is_visible_and_cannot_become_positive(self):
        text = (
            "from vendor import Client as C\n"
            + "".join(
                f"A{i}=" + ("C" if i == 0 else f"A{i - 1}") + "\n" for i in range(140)
            )
            + "A139()\n"
        )
        _, refs = facts(text)
        self.assertIsNone(refs[0].lexical_import)
        self.assertIn("binding_trace_budget_exhausted", refs[0].binding.reasons)
        self.assertLessEqual(len(refs[0].binding.trace), 128)

    def test_import_inventory_keeps_nested_scopes_even_in_unsupported_regions(self):
        imports, _ = facts(
            "try:\n def f():\n  from vendor import Client\n  Client()\nexcept Exception:\n pass\n"
        )
        self.assertFalse(imports[0].module_level)

    def test_dynamic_namespace_inside_unsupported_loop_invalidates_afterward(self):
        _, refs = facts(
            'from vendor import Client as C\nfor item in items:\n exec("C=None")\nC()\n'
        )
        self.assertIsNone(refs[-1].lexical_import)
        self.assertIn(
            "dynamic_namespace_in_unsupported_control_flow", refs[-1].binding.reasons
        )

    def test_alias_receiver_mutation_in_a_loop_invalidates_the_saved_alias(self):
        _, refs = facts(
            "import vendor as V\nS=V\nfor item in items:\n V.Client=None\nS.Client()\n"
        )
        self.assertIsNone(refs[-1].lexical_import)
        self.assertIn("attribute_or_subscript_write", refs[-1].binding.reasons)

    def test_class_global_write_does_not_leave_a_positive_module_binding(self):
        _, refs = facts(
            "from vendor import Client as C\nclass K:\n global C\n C=None\nC()\n"
        )
        self.assertIsNone(refs[-1].lexical_import)
        self.assertIn("cross_scope_global_mutation", refs[-1].binding.reasons)

    def test_alias_copy_of_dynamic_primitive_still_invalidates_the_namespace(self):
        _, refs = facts(
            'from vendor import Client as C\ne=exec\nf=e\nf("C=None")\nC()\n'
        )
        self.assertIsNone(refs[-1].lexical_import)
        self.assertIn("dynamic_namespace_operation", refs[-1].binding.reasons)

    def test_explicit_metaclass_namespace_does_not_establish_body_lookups(self):
        _, refs = facts(
            "from vendor import Client as C\nclass K(metaclass=factory):\n C()\n"
        )
        self.assertIsNone(refs[-1].lexical_import)
        self.assertIn("class_namespace_unmodeled", refs[-1].binding.reasons)

    def test_unknown_mutation_receiver_keeps_heap_alias_uncertainty_visible(self):
        _, refs = facts(
            'from vendor import Client as C\nd=globals()\nd["C"]=None\nC()\n'
        )
        self.assertIsNone(refs[-1].lexical_import)
        self.assertIn("unknown_mutation_receiver", refs[-1].binding.reasons)

    def test_dynamic_globals_exposed_by_a_function_stay_uncertain(self):
        _, refs = facts(
            'from vendor import Client as C\ndef mutate():\n g=globals\n g()["C"]=None\nmutate()\nC()\n'
        )
        self.assertIsNone(refs[-1].lexical_import)
        self.assertIn(
            "dynamic_global_namespace_in_nested_scope", refs[-1].binding.reasons
        )

    def test_origin_budget_cannot_silently_select_a_small_subset_as_established(self):
        text = (
            "from vendor0 import Client as C\n"
            + "".join(
                f"if flag{i}:\n from vendor{i} import Client as C\n"
                for i in range(1, 35)
            )
            + "C()\n"
        )
        _, refs = facts(text)
        self.assertIsNone(refs[0].lexical_import)
        self.assertIn("binding_origin_budget_exhausted", refs[0].binding.reasons)
        self.assertLessEqual(len(refs[0].binding.possible_imports), 32)

    def test_annotation_calls_are_retained_without_assuming_evaluation_timing(self):
        _, refs = facts(
            "from vendor import Type as T\nx: T()\ndef f(x: T()) -> T():\n pass\n"
        )
        self.assertEqual(len(refs), 3)
        self.assertTrue(all(r.lexical_import is None for r in refs))
        self.assertTrue(
            all("annotation_evaluation_unmodeled" in r.binding.reasons for r in refs)
        )

    def test_trace_coordinates_are_python_ast_utf8_byte_columns(self):
        text = "from vendor import Client as C\né = C; é()\n"
        _, refs = facts(text)
        self.assertEqual(refs[0].lexical_import, "vendor.Client")
        step = next(s for s in refs[0].binding.trace if s.operation == "reference")
        line = text.splitlines()[step.line - 1].encode("utf-8")
        self.assertEqual(line[step.column : step.end_column].decode("utf-8"), "é()")

    def test_dynamic_effect_in_implicit_scope_does_not_leave_a_stale_origin(self):
        _, refs = facts(
            'from vendor import Client as C\n[exec("C=None") for item in items]\nC()\n'
        )
        self.assertIsNone(refs[-1].lexical_import)
        self.assertIn("dynamic_namespace_in_implicit_scope", refs[-1].binding.reasons)

    def test_exposing_dynamic_namespace_through_a_comprehension_stays_limited(self):
        _, refs = facts(
            "from vendor import Client as C\n[globals().update(C=None) for item in items]\nC()\n"
        )
        self.assertIsNone(refs[-1].lexical_import)
        self.assertIn("dynamic_namespace_in_implicit_scope", refs[-1].binding.reasons)
