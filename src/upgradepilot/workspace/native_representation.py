"""Bounded representation helpers for explicitly declared native codec layouts.

CI, impact and shared-input codecs supply fixed versioned fields and variant tables. This
module never discovers dataclass fields, resolves checkpoint-supplied imports, or evaluates
evidence. ``NativeValueCodec`` reconstructs only constructors admitted by those tables.
Nested layouts preserve native tuples, literal states, timestamps and version values.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime
from typing import cast

from packaging.version import InvalidVersion, Version


class NativeReconstructionError(ValueError):
    """Explicit unsupported/missing/invalid boundary; never a request to fetch or retry."""

    def __init__(self, reason: str, detail: str) -> None:
        self.reason = reason
        self.detail = detail
        super().__init__(f"{reason}: {detail}")


@dataclass(frozen=True, slots=True)
class RecordRef:
    """Reference to a fixed native variant layout, not a captured material-record ID."""

    variant: str


@dataclass(frozen=True, slots=True)
class SequenceOf:
    item: object


@dataclass(frozen=True, slots=True)
class Either:
    choices: tuple[object, ...]


@dataclass(frozen=True, slots=True)
class LiteralValues:
    values: tuple[object, ...]


@dataclass(frozen=True, slots=True)
class ObjectFields:
    fields: tuple[tuple[str, object], ...]


@dataclass(frozen=True, slots=True)
class RecordLayout:
    """A fixed variant's representation, including retained non-init constant fields."""

    variant: str
    constructor: type
    fields: tuple[tuple[str, object], ...]
    constant_fields: tuple[str, ...] = ()


def _invalid(detail: str) -> NativeReconstructionError:
    return NativeReconstructionError("invalid_native_material", detail)


def object_fields(value: object, names: tuple[str, ...]) -> dict[str, object]:
    if type(value) is not dict or set(value) != set(names):
        raise _invalid(f"Expected exactly the fields {names!r}.")
    return cast(dict[str, object], value)


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise _invalid(f"Duplicate JSON field {key!r}.")
        result[key] = value
    return result


def parse_json(payload: bytes) -> object:
    """Reject ambiguous objects/non-finite scalars and parser nesting failures."""

    def reject_constant(value: str) -> object:
        raise _invalid(f"Non-finite JSON scalar {value!r}.")

    if type(payload) is not bytes:
        raise _invalid("Encoded material must be immutable bytes.")
    try:
        return json.loads(
            payload, object_pairs_hook=_unique_object, parse_constant=reject_constant
        )
    except NativeReconstructionError:
        raise
    except (UnicodeError, ValueError, RecursionError) as error:
        raise _invalid("Unreadable or excessively nested JSON material.") from error


def json_bytes(value: object) -> bytes:
    try:
        return json.dumps(
            value,
            ensure_ascii=True,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except (TypeError, ValueError, RecursionError) as error:
        raise _invalid("Value has no supported JSON representation.") from error


class NativeValueCodec:
    """Encode/decode a selected root through a closed, owner-declared layout table.

    Record tags are fixed representation variants, never Python dispatch/import paths.
    Constructors validate representation only; parsers/evaluators are not codec callbacks.
    The depth guard bounds recursive static workflow values without accepting arbitrary
    object graphs. Unknown fields/variants and missing optional fields are refused.
    """

    def __init__(self, layouts: tuple[RecordLayout, ...]) -> None:
        self._layouts = {layout.variant: layout for layout in layouts}
        if len(self._layouts) != len(layouts):
            raise ValueError("Native layouts must have unique fixed variants.")

    def encode(self, value: object, shape: object) -> bytes:
        return json_bytes(self._transform(value, shape, encode=True, depth=0))

    def decode(self, payload: bytes, shape: object) -> object:
        return self._transform(parse_json(payload), shape, encode=False, depth=0)

    def _transform(
        self, value: object, shape: object, *, encode: bool, depth: int
    ) -> object:
        if depth > 64:
            raise _invalid("Native representation exceeds the supported nesting depth.")
        if shape in (str, int, bool, type(None)):
            if type(value) is not shape:
                raise _invalid(f"Expected scalar {shape.__name__}.")
            return value
        if isinstance(shape, LiteralValues):
            if not any(
                type(value) is type(item) and value == item for item in shape.values
            ):
                raise _invalid(f"Unsupported literal state {value!r}.")
            return value
        if isinstance(shape, Either):
            for choice in shape.choices:
                try:
                    return self._transform(
                        value, choice, encode=encode, depth=depth + 1
                    )
                except NativeReconstructionError:
                    continue
            raise _invalid("Value does not match an admitted native variant.")
        if isinstance(shape, SequenceOf):
            expected = tuple if encode else list
            if type(value) is not expected:
                raise _invalid(f"Expected ordered {expected.__name__}.")
            items = [
                self._transform(item, shape.item, encode=encode, depth=depth + 1)
                for item in value
            ]
            return items if encode else tuple(items)
        if isinstance(shape, ObjectFields):
            values = object_fields(value, tuple(name for name, _ in shape.fields))
            return {
                name: self._transform(
                    values[name], item, encode=encode, depth=depth + 1
                )
                for name, item in shape.fields
            }
        if shape is datetime:
            if encode:
                if type(value) is not datetime:
                    raise _invalid("Expected a native timestamp.")
                return {"iso": value.isoformat(), "fold": value.fold}
            values = object_fields(value, ("iso", "fold"))
            if type(values["iso"]) is not str or type(values["fold"]) is not int:
                raise _invalid("Invalid timestamp representation.")
            if values["fold"] not in (0, 1):
                raise _invalid("Invalid timestamp fold.")
            try:
                return datetime.fromisoformat(values["iso"]).replace(
                    fold=values["fold"]
                )
            except ValueError as error:
                raise _invalid("Invalid timestamp text.") from error
        if shape is Version:
            if encode:
                if type(value) is not Version:
                    raise _invalid("Expected a native parsed version.")
                return str(value)
            if type(value) is not str:
                raise _invalid("Invalid parsed-version representation.")
            try:
                return Version(value)
            except InvalidVersion as error:
                raise _invalid("Invalid retained version.") from error
        if isinstance(shape, RecordRef):
            layout = self._layouts[shape.variant]
            names = tuple(name for name, _ in layout.fields)
            if encode:
                if type(value) is not layout.constructor:
                    raise _invalid(f"Expected native variant {layout.variant}.")
                values = {name: getattr(value, name) for name in names}
            else:
                envelope = object_fields(value, ("variant", "fields"))
                if envelope["variant"] != layout.variant:
                    raise _invalid(f"Expected retained variant {layout.variant}.")
                values = object_fields(envelope["fields"], names)
            transformed = {
                name: self._transform(
                    values[name], item, encode=encode, depth=depth + 1
                )
                for name, item in layout.fields
            }
            if encode:
                return {"variant": layout.variant, "fields": transformed}
            try:
                result = layout.constructor(
                    **{
                        name: item
                        for name, item in transformed.items()
                        if name not in layout.constant_fields
                    }
                )
            except (TypeError, ValueError) as error:
                raise _invalid(
                    f"Invalid native representation for {layout.variant}."
                ) from error
            # Some existing representation constructors normalize locators. Recovery must
            # refuse altered/noncanonical retained fields rather than quietly repairing them.
            for name in transformed:
                if getattr(result, name) != transformed[name]:
                    raise _invalid(f"Constructor changed retained field {name!r}.")
            return result
        raise ValueError(f"Unsupported trusted codec layout {shape!r}.")
