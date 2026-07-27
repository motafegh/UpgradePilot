"""Validate source-neutral JSON values at external trust boundaries.

This module owns only runtime value-shape rules that mean the same thing for every
structured source. It does not look up fields, name services, classify HTTP failures,
or decide evidence authority. Focused clients translate ``JsonContractViolation``
into their own public error or result contracts.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any


class JsonContractViolation(ValueError):
    """An untrusted JSON value did not satisfy the requested runtime contract."""


def expect_mapping(value: Any) -> Mapping[str, Any]:
    """Require a JSON object-like value."""

    if not isinstance(value, Mapping):
        raise JsonContractViolation("value must be an object")
    return value


def expect_list(value: Any) -> list[Any]:
    """Require a JSON array value."""

    if not isinstance(value, list):
        raise JsonContractViolation("value must be an array")
    return value


def expect_nonempty_text(value: Any) -> str:
    """Require a non-empty JSON string without changing its contents."""

    if not isinstance(value, str) or not value:
        raise JsonContractViolation("value must be non-empty text")
    return value


def expect_optional_nonempty_text(value: Any) -> str | None:
    """Require either JSON null or a non-empty string."""

    if value is None:
        return None
    return expect_nonempty_text(value)


def expect_integer(value: Any) -> int:
    """Require a JSON integer while rejecting booleans.

    Python treats ``bool`` as a subclass of ``int``. The explicit boolean rejection
    prevents JSON ``true`` and ``false`` from becoming numeric evidence.
    """

    if isinstance(value, bool) or not isinstance(value, int):
        raise JsonContractViolation("value must be an integer")
    return value


def expect_positive_integer(value: Any) -> int:
    """Require an integer greater than zero."""

    integer = expect_integer(value)
    if integer < 1:
        raise JsonContractViolation("value must be a positive integer")
    return integer


def expect_nonnegative_integer(value: Any) -> int:
    """Require an integer greater than or equal to zero."""

    integer = expect_integer(value)
    if integer < 0:
        raise JsonContractViolation("value must be a non-negative integer")
    return integer


def expect_boolean(value: Any) -> bool:
    """Require an actual JSON boolean."""

    if not isinstance(value, bool):
        raise JsonContractViolation("value must be a boolean")
    return value
