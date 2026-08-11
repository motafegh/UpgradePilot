#!/usr/bin/env python3
"""Deterministic, low-noise diagnostics for UpgradePilot agent governance.

This tool checks objective repository structure and schema facts only. It does not
attempt to judge fuzzy governance semantics or product behavior.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
CASES_PATH = ROOT / "tools" / "agent-governance" / "cases.json"

CORE_GOVERNANCE_FILES = (
    ROOT / "AGENTS.md",
    ROOT / "OPERATING_GUIDE.md",
    ROOT / "SECURITY.md",
    ROOT / "ENVIRONMENT.md",
    ROOT / "plans" / "README.md",
    ROOT / "audits" / "README.md",
    ROOT / "tools" / "agent-governance" / "README.md",
)

SIZE_REPORT_FILES = (
    ROOT / "AGENTS.md",
    ROOT / "OPERATING_GUIDE.md",
    ROOT / "SECURITY.md",
    ROOT / "ENVIRONMENT.md",
)

REQUIRED_ROOT_RESPONSIBILITY_MARKERS = (
    "`audits/`",
    "`examples/`",
    "`.agents/skills/`",
)

REQUIRED_CASE_FIELDS = {
    "id",
    "category",
    "prompt",
    "setup_context",
    "expected_action_mode",
    "owners_expected",
    "owners_not_expected",
    "must_do",
    "must_not_do",
    "criticality",
    "notes",
}

ALLOWED_CRITICALITY = {"critical", "high", "normal"}
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def check_required_files(errors: list[str]) -> None:
    for path in CORE_GOVERNANCE_FILES:
        if not path.is_file():
            errors.append(f"missing required governance file: {relative(path)}")

    if not CASES_PATH.is_file():
        errors.append(f"missing governance case bank: {relative(CASES_PATH)}")


def check_root_responsibility_map(errors: list[str]) -> None:
    path = ROOT / "AGENTS.md"
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    for marker in REQUIRED_ROOT_RESPONSIBILITY_MARKERS:
        if marker not in text:
            errors.append(f"AGENTS.md responsibility map is missing {marker}")


def parse_skill_frontmatter(path: Path) -> dict[str, str] | None:
    lines = path.read_text(encoding="utf-8").splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        return None
    try:
        end = next(index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        return None

    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"').strip("'")
    return metadata


def check_skills(errors: list[str]) -> None:
    skills_root = ROOT / ".agents" / "skills"
    if not skills_root.is_dir():
        errors.append("missing .agents/skills/ despite its registered responsibility")
        return

    skill_dirs = sorted(path for path in skills_root.iterdir() if path.is_dir())
    if not skill_dirs:
        errors.append(".agents/skills/ exists but contains no admitted skill")
        return

    for skill_dir in skill_dirs:
        skill_path = skill_dir / "SKILL.md"
        if not skill_path.is_file():
            errors.append(f"skill directory lacks SKILL.md: {relative(skill_dir)}")
            continue
        metadata = parse_skill_frontmatter(skill_path)
        if metadata is None:
            errors.append(f"skill frontmatter is missing or malformed: {relative(skill_path)}")
            continue
        for field in ("name", "description"):
            if not metadata.get(field):
                errors.append(f"skill frontmatter missing {field}: {relative(skill_path)}")
        if metadata.get("name") and metadata["name"] != skill_dir.name:
            errors.append(
                f"skill name '{metadata['name']}' does not match directory '{skill_dir.name}'"
            )


def check_cases(errors: list[str]) -> None:
    if not CASES_PATH.is_file():
        return

    try:
        payload = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"cases.json is invalid JSON: {exc}")
        return

    cases = payload.get("cases")
    if not isinstance(cases, list) or not cases:
        errors.append("cases.json must contain a non-empty 'cases' list")
        return

    seen_ids: set[str] = set()
    for index, case in enumerate(cases):
        label = f"case[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{label} must be an object")
            continue

        missing = sorted(REQUIRED_CASE_FIELDS - case.keys())
        if missing:
            errors.append(f"{label} missing fields: {', '.join(missing)}")

        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id.strip():
            errors.append(f"{label} has invalid id")
        elif case_id in seen_ids:
            errors.append(f"duplicate governance case id: {case_id}")
        else:
            seen_ids.add(case_id)

        criticality = case.get("criticality")
        if criticality not in ALLOWED_CRITICALITY:
            errors.append(f"{case_id or label} has invalid criticality: {criticality!r}")

        for field in ("owners_expected", "owners_not_expected", "must_do", "must_not_do"):
            if field in case and not isinstance(case[field], list):
                errors.append(f"{case_id or label} field '{field}' must be a list")

    critical_ids = payload.get("critical_case_ids", [])
    if not isinstance(critical_ids, list):
        errors.append("critical_case_ids must be a list")
    else:
        for case_id in critical_ids:
            if case_id not in seen_ids:
                errors.append(f"critical_case_ids references unknown id: {case_id}")


def normalize_link_target(raw_target: str) -> str | None:
    target = raw_target.strip()
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        return None

    # Markdown link titles are intentionally not supported here because the core
    # governance files use simple repository-relative links.
    target = target.split("#", 1)[0]
    return unquote(target)


def check_internal_markdown_links(errors: list[str]) -> None:
    for source in CORE_GOVERNANCE_FILES:
        if not source.is_file():
            continue
        text = source.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = normalize_link_target(raw_target)
            if target is None:
                continue
            resolved = (source.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(
                    f"repository-relative link escapes repository in {relative(source)}: {raw_target}"
                )
                continue
            if not resolved.exists():
                errors.append(
                    f"broken internal link in {relative(source)}: {raw_target}"
                )


def report_sizes() -> None:
    print("Governance file observations:")
    for path in SIZE_REPORT_FILES:
        if not path.is_file():
            continue
        raw = path.read_bytes()
        line_count = len(raw.decode("utf-8").splitlines())
        print(f"  {relative(path):<22} {line_count:>4} lines  {len(raw):>6} bytes")


def main() -> int:
    errors: list[str] = []

    check_required_files(errors)
    check_root_responsibility_map(errors)
    check_skills(errors)
    check_cases(errors)
    check_internal_markdown_links(errors)

    report_sizes()
    print("Excluded subtree: product-simulation/ was not inspected by this tool.")

    if errors:
        print("\nGovernance doctor: FAIL")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("\nGovernance doctor: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
