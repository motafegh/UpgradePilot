"""Deterministic tests for source-neutral JSON value contracts."""

from __future__ import annotations

import unittest

from upgradepilot.json_contract import (
    JsonContractViolation,
    expect_boolean,
    expect_integer,
    expect_list,
    expect_mapping,
    expect_nonempty_text,
    expect_nonnegative_integer,
    expect_optional_nonempty_text,
    expect_positive_integer,
)


class JsonContractTests(unittest.TestCase):
    def test_accepts_supported_json_value_shapes(self) -> None:
        mapping = {"name": "example"}
        array = [1, 2]

        self.assertIs(expect_mapping(mapping), mapping)
        self.assertIs(expect_list(array), array)
        self.assertEqual(expect_nonempty_text("value"), "value")
        self.assertEqual(expect_optional_nonempty_text("value"), "value")
        self.assertIsNone(expect_optional_nonempty_text(None))
        self.assertEqual(expect_integer(0), 0)
        self.assertEqual(expect_positive_integer(1), 1)
        self.assertEqual(expect_nonnegative_integer(0), 0)
        self.assertIs(expect_boolean(False), False)

    def test_rejects_wrong_container_and_text_shapes(self) -> None:
        for operation, value in (
            (expect_mapping, []),
            (expect_list, {}),
            (expect_nonempty_text, ""),
            (expect_nonempty_text, None),
            (expect_optional_nonempty_text, ""),
        ):
            with self.subTest(operation=operation.__name__, value=value):
                with self.assertRaises(JsonContractViolation):
                    operation(value)

    def test_integer_contract_rejects_boolean_and_wrong_ranges(self) -> None:
        for operation, value in (
            (expect_integer, True),
            (expect_integer, 1.0),
            (expect_positive_integer, 0),
            (expect_nonnegative_integer, -1),
        ):
            with self.subTest(operation=operation.__name__, value=value):
                with self.assertRaises(JsonContractViolation):
                    operation(value)

    def test_boolean_contract_requires_actual_boolean(self) -> None:
        for value in (0, 1, "false", None):
            with self.subTest(value=value):
                with self.assertRaises(JsonContractViolation):
                    expect_boolean(value)


if __name__ == "__main__":
    unittest.main()
