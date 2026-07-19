from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from upgradepilot.domain.models import (
    AnalysisInput,
    CaseIdentity,
    DecisionEffect,
    EvidenceItem,
    EvidenceState,
    SourceReference,
)


class InputError(ValueError):
    """Raised when an input document violates the evidence contract."""


def load_analysis_input(path: Path) -> AnalysisInput:
    try:
        with path.open(encoding="utf-8") as stream:
            document = json.load(stream)
    except json.JSONDecodeError as exc:
        raise InputError(
            f"{path}: invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc
    except OSError as exc:
        raise InputError(f"{path}: cannot read input: {exc}") from exc

    try:
        return parse_analysis_input(document)
    except InputError:
        raise
    except (TypeError, ValueError) as exc:
        raise InputError(f"{path}: {exc}") from exc


def parse_analysis_input(document: Any) -> AnalysisInput:
    root = _mapping(document, "$")
    _keys(root, "$", required={"schema_version", "case", "evidence", "limitations"})

    case_data = _mapping(root["case"], "$.case")
    _keys(
        case_data,
        "$.case",
        required={
            "repository_owner",
            "repository_name",
            "pull_request_number",
            "pull_request_url",
            "base_revision",
            "head_revision",
            "dependency_name",
            "old_version",
            "new_version",
            "changed_files",
        },
    )
    try:
        case = CaseIdentity(
            repository_owner=_string(case_data["repository_owner"], "$.case.repository_owner"),
            repository_name=_string(case_data["repository_name"], "$.case.repository_name"),
            pull_request_number=_integer(
                case_data["pull_request_number"], "$.case.pull_request_number"
            ),
            pull_request_url=_string(case_data["pull_request_url"], "$.case.pull_request_url"),
            base_revision=_string(case_data["base_revision"], "$.case.base_revision"),
            head_revision=_string(case_data["head_revision"], "$.case.head_revision"),
            dependency_name=_string(case_data["dependency_name"], "$.case.dependency_name"),
            old_version=_string(case_data["old_version"], "$.case.old_version"),
            new_version=_string(case_data["new_version"], "$.case.new_version"),
            changed_files=_string_tuple(case_data["changed_files"], "$.case.changed_files"),
        )
    except ValueError as exc:
        raise InputError(f"$.case: {exc}") from exc

    evidence_data = _list(root["evidence"], "$.evidence")
    evidence = tuple(
        _parse_evidence(item, f"$.evidence[{index}]")
        for index, item in enumerate(evidence_data)
    )

    try:
        return AnalysisInput(
            schema_version=_string(root["schema_version"], "$.schema_version"),
            case=case,
            evidence=evidence,
            limitations=_string_tuple(root["limitations"], "$.limitations"),
        )
    except ValueError as exc:
        raise InputError(str(exc)) from exc


def _parse_evidence(value: Any, path: str) -> EvidenceItem:
    data = _mapping(value, path)
    _keys(
        data,
        path,
        required={
            "evidence_id",
            "claim",
            "state",
            "decision_effect",
            "material",
            "interpretation",
            "source",
            "suggested_check",
        },
    )
    source_value = data["source"]
    source = None if source_value is None else _parse_source(source_value, f"{path}.source")

    try:
        state = EvidenceState(_string(data["state"], f"{path}.state"))
    except ValueError as exc:
        raise InputError(f"{path}.state: unknown evidence state {data['state']!r}") from exc
    try:
        effect = DecisionEffect(
            _string(data["decision_effect"], f"{path}.decision_effect")
        )
    except ValueError as exc:
        raise InputError(
            f"{path}.decision_effect: unknown decision effect {data['decision_effect']!r}"
        ) from exc

    suggested_value = data["suggested_check"]
    suggested_check = (
        None
        if suggested_value is None
        else _string(suggested_value, f"{path}.suggested_check")
    )

    try:
        return EvidenceItem(
            evidence_id=_string(data["evidence_id"], f"{path}.evidence_id"),
            claim=_string(data["claim"], f"{path}.claim"),
            state=state,
            decision_effect=effect,
            material=_boolean(data["material"], f"{path}.material"),
            interpretation=_string(data["interpretation"], f"{path}.interpretation"),
            source=source,
            suggested_check=suggested_check,
        )
    except ValueError as exc:
        raise InputError(f"{path}: {exc}") from exc


def _parse_source(value: Any, path: str) -> SourceReference:
    data = _mapping(value, path)
    _keys(data, path, required={"locator", "retrieved_at", "revision"})
    revision_value = data["revision"]
    revision = None if revision_value is None else _string(revision_value, f"{path}.revision")
    try:
        return SourceReference(
            locator=_string(data["locator"], f"{path}.locator"),
            retrieved_at=_string(data["retrieved_at"], f"{path}.retrieved_at"),
            revision=revision,
        )
    except ValueError as exc:
        raise InputError(f"{path}: {exc}") from exc


def _keys(data: dict[str, Any], path: str, *, required: set[str]) -> None:
    actual = set(data)
    missing = sorted(required - actual)
    unknown = sorted(actual - required)
    if missing:
        raise InputError(f"{path}: missing keys: {', '.join(missing)}")
    if unknown:
        raise InputError(f"{path}: unknown keys: {', '.join(unknown)}")


def _mapping(value: Any, path: str) -> dict[str, Any]:
    if not isinstance(value, dict) or not all(isinstance(key, str) for key in value):
        raise InputError(f"{path}: expected an object")
    return value


def _list(value: Any, path: str) -> list[Any]:
    if not isinstance(value, list):
        raise InputError(f"{path}: expected an array")
    return value


def _string(value: Any, path: str) -> str:
    if not isinstance(value, str):
        raise InputError(f"{path}: expected a string")
    return value


def _integer(value: Any, path: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise InputError(f"{path}: expected an integer")
    return value


def _boolean(value: Any, path: str) -> bool:
    if not isinstance(value, bool):
        raise InputError(f"{path}: expected a boolean")
    return value


def _string_tuple(value: Any, path: str) -> tuple[str, ...]:
    values = _list(value, path)
    return tuple(_string(item, f"{path}[{index}]") for index, item in enumerate(values))
