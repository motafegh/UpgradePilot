from __future__ import annotations

from dataclasses import asdict
from enum import Enum
from html import escape
import json
import os
from pathlib import Path
import tempfile
from typing import Any

from upgradepilot.domain.models import DecisionReport


def report_to_dict(report: DecisionReport) -> dict[str, Any]:
    return _json_value(asdict(report))


def render_markdown(report: DecisionReport) -> str:
    case = report.case
    lines = [
        "# UpgradePilot Decision Report — "
        f"{_markdown_text(case.repository_owner)}/"
        f"{_markdown_text(case.repository_name)}#{case.pull_request_number}",
        "",
        f"- **Dependency:** `{_inline_code(case.dependency_name)}` "
        f"`{_inline_code(case.old_version)}` → `{_inline_code(case.new_version)}`",
        f"- **Action:** `{report.action.value}`",
        f"- **Generated:** `{_inline_code(report.generated_at)}`",
        f"- **Policy:** `{_inline_code(report.policy_version)}`",
        "- **Base/head:** "
        f"`{_inline_code(case.base_revision)}` / `{_inline_code(case.head_revision)}`",
        "",
        "## Decision rationale",
        "",
        _markdown_text(report.reason),
        "",
        "## Evidence",
        "",
    ]

    if not report.evidence:
        lines.append("No evidence items were supplied.")
    for item in report.evidence:
        lines.extend(
            [
                f"### {_markdown_text(item.evidence_id)}",
                "",
                f"- **State:** `{item.state.value}`",
                f"- **Decision effect:** `{item.decision_effect.value}`",
                f"- **Material:** `{str(item.material).lower()}`",
                f"- **Claim:** {_markdown_text(item.claim)}",
                f"- **Interpretation:** {_markdown_text(item.interpretation)}",
            ]
        )
        if item.source is not None:
            lines.append(f"- **Source:** {_markdown_text(item.source.locator)}")
            lines.append(f"- **Retrieved:** `{_inline_code(item.source.retrieved_at)}`")
            if item.source.revision is not None:
                lines.append(f"- **Revision:** `{_inline_code(item.source.revision)}`")
        if item.suggested_check is not None:
            lines.append(f"- **Suggested check:** {_markdown_text(item.suggested_check)}")
        lines.append("")

    lines.extend(_section("Targeted checks", report.targeted_checks))
    lines.extend(_section("Uncertainties", report.uncertainties))
    lines.extend(_section("Limitations", report.limitations))
    lines.extend(["## Claim boundary", "", _markdown_text(report.claim_boundary), ""])
    return "\n".join(lines)


def write_reports(report: DecisionReport, output_dir: Path) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    stem = (
        f"{_safe(report.case.repository_owner)}-"
        f"{_safe(report.case.repository_name)}-"
        f"pr-{report.case.pull_request_number}"
    )
    json_path = output_dir / f"{stem}.report.json"
    markdown_path = output_dir / f"{stem}.report.md"

    json_text = json.dumps(report_to_dict(report), indent=2, sort_keys=True) + "\n"
    _atomic_write(json_path, json_text)
    _atomic_write(markdown_path, render_markdown(report))
    return json_path, markdown_path


def _json_value(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, dict):
        return {key: _json_value(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_value(item) for item in value]
    return value


def _section(title: str, values: tuple[str, ...]) -> list[str]:
    lines = [f"## {title}", ""]
    if values:
        lines.extend(f"- {_markdown_text(value)}" for value in values)
    else:
        lines.append("None recorded.")
    lines.append("")
    return lines


def _safe(value: str) -> str:
    normalized = "".join(character.lower() if character.isalnum() else "-" for character in value)
    return "-".join(part for part in normalized.split("-") if part) or "case"


def _inline_code(value: str) -> str:
    return _single_line(value).replace("`", "&#96;")


def _markdown_text(value: str) -> str:
    text = escape(_single_line(value))
    for character in ("\\", "`", "*", "_", "[", "]", "#", "|"):
        text = text.replace(character, f"\\{character}")
    return text


def _single_line(value: str) -> str:
    return " ".join(value.splitlines())


def _atomic_write(path: Path, content: str) -> None:
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            delete=False,
        ) as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
            temporary_path = Path(stream.name)
        os.replace(temporary_path, path)
    except Exception:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)
        raise
