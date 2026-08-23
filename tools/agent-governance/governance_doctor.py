#!/usr/bin/env python3
"""Deterministic, low-noise diagnostics for UpgradePilot agent governance.

This tool checks objective repository structure, routing, schema, link, lifecycle,
and stable-ID facts only. It intentionally does not attempt to judge fuzzy
semantic questions or product behavior.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
AGENT_GOVERNANCE_ROOT = ROOT / "tools" / "agent-governance"
AUDITS_ROOT = ROOT / "audits"
SKILLS_ROOT = ROOT / ".agents" / "skills"

CASE_BANK_FILENAMES = (
    "cases.json",
    "audit_cases.json",
    "planning_cases.json",
    "build_cases.json",
    "learning_only_cases.json",
    "consistency_cases.json",
)
CASE_BANK_PATHS = tuple(AGENT_GOVERNANCE_ROOT / name for name in CASE_BANK_FILENAMES)

EXPECTED_OPERATION_SKILLS = (
    "upgradepilot-repository-audit",
    "upgradepilot-planning-design",
    "upgradepilot-build-implement",
    "upgradepilot-learning-by-doing",
    "upgradepilot-learning-only",
)

REQUIRED_GOVERNANCE_FILES = (
    ROOT / "AGENTS.md",
    ROOT / "PROJECT_CHARTER.md",
    ROOT / "OPERATING_GUIDE.md",
    ROOT / "SECURITY.md",
    ROOT / "ENVIRONMENT.md",
    ROOT / "MEMORY.md",
    ROOT / "docs" / "README.md",
    ROOT / "docs" / "specifications" / "README.md",
    ROOT / "docs" / "architecture" / "README.md",
    ROOT / "plans" / "README.md",
    ROOT / "audits" / "README.md",
    ROOT / "audits" / "LIFECYCLE.md",
    ROOT / "audits" / "active" / "README.md",
    ROOT / "audits" / "scheduled" / "README.md",
    ROOT / "audits" / "deferred" / "README.md",
    ROOT / "audits" / "absorbed" / "README.md",
    AGENT_GOVERNANCE_ROOT / "README.md",
)

ROOT_OWNER_PATHS = (
    ("`PROJECT_CHARTER.md`", ROOT / "PROJECT_CHARTER.md"),
    ("`plans/UPGRADEPILOT_90_DAY_PLAN.md`", ROOT / "plans" / "UPGRADEPILOT_90_DAY_PLAN.md"),
    ("`MEMORY.md`", ROOT / "MEMORY.md"),
    ("`ENVIRONMENT.md`", ROOT / "ENVIRONMENT.md"),
    ("`SECURITY.md`", ROOT / "SECURITY.md"),
    ("`OPERATING_GUIDE.md`", ROOT / "OPERATING_GUIDE.md"),
    ("`docs/README.md`", ROOT / "docs" / "README.md"),
    ("`plans/`", ROOT / "plans"),
    ("`docs/specifications/`", ROOT / "docs" / "specifications"),
    ("`docs/architecture/`", ROOT / "docs" / "architecture"),
    ("`src/upgradepilot/`", ROOT / "src" / "upgradepilot"),
    ("`tests/`", ROOT / "tests"),
    ("`experiments/`", ROOT / "experiments"),
    ("`tools/`", ROOT / "tools"),
    ("`.agents/skills/`", SKILLS_ROOT),
    ("`audits/`", AUDITS_ROOT),
    ("`examples/`", ROOT / "examples"),
    ("`product-simulation/`", ROOT / "product-simulation"),
    ("`working-memory/`", ROOT / "working-memory"),
    ("`learning/`", ROOT / "learning"),
    ("`proposals/`", ROOT / "proposals"),
    ("`archive/`", ROOT / "archive"),
    ("`chronicle/`", ROOT / "chronicle"),
)

ACTIVE_SPECIFICATION_FILES = (
    ROOT / "docs" / "specifications" / "UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md",
    ROOT / "docs" / "specifications" / "UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md",
    ROOT / "docs" / "specifications" / "UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md",
    ROOT / "docs" / "specifications" / "UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md",
)

AUDIT_LIFECYCLE_INDEXES = {
    "ACTIVE": AUDITS_ROOT / "active" / "README.md",
    "SCHEDULED": AUDITS_ROOT / "scheduled" / "README.md",
    "DEFERRED": AUDITS_ROOT / "deferred" / "README.md",
    "ABSORBED": AUDITS_ROOT / "absorbed" / "README.md",
}

STATIC_LINK_CHECK_FILES = (
    ROOT / "AGENTS.md",
    ROOT / "PROJECT_CHARTER.md",
    ROOT / "OPERATING_GUIDE.md",
    ROOT / "SECURITY.md",
    ROOT / "ENVIRONMENT.md",
    ROOT / "docs" / "README.md",
    ROOT / "docs" / "specifications" / "README.md",
    ROOT / "docs" / "architecture" / "README.md",
    ROOT / "plans" / "README.md",
    ROOT / "audits" / "README.md",
    ROOT / "audits" / "LIFECYCLE.md",
    *AUDIT_LIFECYCLE_INDEXES.values(),
    AGENT_GOVERNANCE_ROOT / "README.md",
    *ACTIVE_SPECIFICATION_FILES,
)

STATE_LEAK_CHECK_FILES = (
    ROOT / "plans" / "README.md",
    ROOT / "audits" / "README.md",
)

SIZE_REPORT_FILES = (
    ROOT / "AGENTS.md",
    ROOT / "OPERATING_GUIDE.md",
    ROOT / "SECURITY.md",
    ROOT / "ENVIRONMENT.md",
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
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
NORMATIVE_TABLE_ID_RE = re.compile(
    r"^\|\s*`([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*-\d{3})`\s*\|"
)
AUDIT_ID_RE = re.compile(r"AUDIT-\d{3}")
STATE_LEAK_RE = re.compile(r"(?im)^#+\s*Current classification\s*\(\d{4}-\d{2}-\d{2}\)")


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def check_required_files(errors: list[str]) -> None:
    for path in REQUIRED_GOVERNANCE_FILES:
        if not path.is_file():
            errors.append(f"missing required governance file: {relative(path)}")

    for path in CASE_BANK_PATHS:
        if not path.is_file():
            errors.append(f"missing governance case bank: {relative(path)}")

    for path in ACTIVE_SPECIFICATION_FILES:
        if not path.is_file():
            errors.append(f"missing registered active specification: {relative(path)}")


def check_root_responsibility_map(errors: list[str]) -> None:
    path = ROOT / "AGENTS.md"
    if not path.is_file():
        return

    text = path.read_text(encoding="utf-8")
    for marker, owner_path in ROOT_OWNER_PATHS:
        if marker not in text:
            errors.append(f"AGENTS.md responsibility map is missing owner marker {marker}")
        if not owner_path.exists():
            errors.append(
                f"AGENTS.md registered owner path does not exist: {relative(owner_path)}"
            )


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


def discovered_skill_paths() -> list[Path]:
    if not SKILLS_ROOT.is_dir():
        return []
    return sorted(path / "SKILL.md" for path in SKILLS_ROOT.iterdir() if path.is_dir())


def check_skills(errors: list[str]) -> None:
    if not SKILLS_ROOT.is_dir():
        errors.append("missing .agents/skills/ despite its registered responsibility")
        return

    skill_dirs = sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir())
    if not skill_dirs:
        errors.append(".agents/skills/ exists but contains no admitted skill")
        return

    seen_names: set[str] = set()
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

        name = metadata.get("name")
        if name:
            if name != skill_dir.name:
                errors.append(f"skill name '{name}' does not match directory '{skill_dir.name}'")
            if name in seen_names:
                errors.append(f"duplicate skill frontmatter name: {name}")
            seen_names.add(name)

    for name in EXPECTED_OPERATION_SKILLS:
        skill_path = SKILLS_ROOT / name / "SKILL.md"
        if not skill_path.is_file():
            errors.append(f"missing admitted operation Skill: {relative(skill_path)}")


def check_operation_skill_references(errors: list[str]) -> None:
    routing_surfaces = (ROOT / "AGENTS.md", ROOT / "OPERATING_GUIDE.md")
    texts = {
        path: path.read_text(encoding="utf-8")
        for path in routing_surfaces
        if path.is_file()
    }

    for name in EXPECTED_OPERATION_SKILLS:
        marker = f".agents/skills/{name}/SKILL.md"
        for path, text in texts.items():
            if marker not in text:
                errors.append(f"{relative(path)} is missing admitted operation Skill reference: {marker}")


def check_case_banks(errors: list[str]) -> None:
    seen_ids: dict[str, Path] = {}

    for path in CASE_BANK_PATHS:
        if not path.is_file():
            continue

        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{relative(path)} is invalid JSON: {exc}")
            continue

        if payload.get("schema_version") != 1:
            errors.append(f"{relative(path)} must declare schema_version 1")

        cases = payload.get("cases")
        if not isinstance(cases, list) or not cases:
            errors.append(f"{relative(path)} must contain a non-empty 'cases' list")
            continue

        bank_ids: set[str] = set()
        for index, case in enumerate(cases):
            label = f"{relative(path)} case[{index}]"
            if not isinstance(case, dict):
                errors.append(f"{label} must be an object")
                continue

            missing = sorted(REQUIRED_CASE_FIELDS - case.keys())
            if missing:
                errors.append(f"{label} missing fields: {', '.join(missing)}")

            case_id = case.get("id")
            if not isinstance(case_id, str) or not case_id.strip():
                errors.append(f"{label} has invalid id")
            else:
                if case_id in bank_ids:
                    errors.append(f"duplicate governance case id in {relative(path)}: {case_id}")
                bank_ids.add(case_id)

                prior = seen_ids.get(case_id)
                if prior is not None:
                    errors.append(
                        f"duplicate governance case id across banks: {case_id} "
                        f"({relative(prior)} and {relative(path)})"
                    )
                else:
                    seen_ids[case_id] = path

            criticality = case.get("criticality")
            if criticality not in ALLOWED_CRITICALITY:
                errors.append(f"{case_id or label} has invalid criticality: {criticality!r}")

            for field in ("owners_expected", "owners_not_expected", "must_do", "must_not_do"):
                value = case.get(field)
                if field in case and not isinstance(value, list):
                    errors.append(f"{case_id or label} field '{field}' must be a list")
                elif isinstance(value, list) and not all(isinstance(item, str) for item in value):
                    errors.append(f"{case_id or label} field '{field}' must contain strings only")

            for field in ("category", "prompt", "setup_context", "expected_action_mode", "notes"):
                value = case.get(field)
                if field in case and (not isinstance(value, str) or not value.strip()):
                    errors.append(f"{case_id or label} field '{field}' must be a non-empty string")

        critical_ids = payload.get("critical_case_ids", [])
        if not isinstance(critical_ids, list):
            errors.append(f"{relative(path)} critical_case_ids must be a list")
        else:
            for case_id in critical_ids:
                if case_id not in bank_ids:
                    errors.append(
                        f"{relative(path)} critical_case_ids references unknown id: {case_id}"
                    )


def normalize_link_target(raw_target: str) -> str | None:
    target = raw_target.strip()
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        return None

    # Markdown link titles are intentionally not supported here because the
    # checked governance surfaces use simple repository-relative links.
    target = target.split("#", 1)[0]
    return unquote(target)


def link_check_files() -> list[Path]:
    files = list(STATIC_LINK_CHECK_FILES)
    files.extend(path for path in discovered_skill_paths() if path.is_file())
    return sorted(set(files))


def check_internal_markdown_links(errors: list[str]) -> None:
    for source in link_check_files():
        if not source.is_file():
            continue
        text = source.read_text(encoding="utf-8")
        for _label, raw_target in MARKDOWN_LINK_RE.findall(text):
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
                errors.append(f"broken internal link in {relative(source)}: {raw_target}")


def check_normative_id_uniqueness(errors: list[str]) -> None:
    definitions: dict[str, tuple[Path, int]] = {}

    for path in ACTIVE_SPECIFICATION_FILES:
        if not path.is_file():
            continue
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            match = NORMATIVE_TABLE_ID_RE.match(line)
            if not match:
                continue
            normative_id = match.group(1)
            prior = definitions.get(normative_id)
            if prior is not None:
                prior_path, prior_line = prior
                errors.append(
                    f"duplicate active normative ID {normative_id}: "
                    f"{relative(prior_path)}:{prior_line} and {relative(path)}:{line_number}"
                )
            else:
                definitions[normative_id] = (path, line_number)


def check_audit_lifecycle(errors: list[str]) -> None:
    classifications: dict[str, tuple[str, Path]] = {}

    for state, index_path in AUDIT_LIFECYCLE_INDEXES.items():
        if not index_path.is_file():
            continue

        seen_in_index: set[str] = set()
        text = index_path.read_text(encoding="utf-8")
        for label, raw_target in MARKDOWN_LINK_RE.findall(text):
            audit_match = AUDIT_ID_RE.search(label)
            if audit_match is None:
                continue

            audit_id = audit_match.group(0)
            expected_prefix = f"{state} — {audit_id}"
            if not label.startswith(expected_prefix):
                errors.append(
                    f"audit lifecycle label in {relative(index_path)} should start with "
                    f"'{expected_prefix}': {label}"
                )

            if audit_id in seen_in_index:
                errors.append(f"duplicate {audit_id} in {relative(index_path)}")
            seen_in_index.add(audit_id)

            target = normalize_link_target(raw_target)
            if target is None:
                errors.append(
                    f"audit lifecycle entry {audit_id} in {relative(index_path)} must use a local canonical link"
                )
                continue

            resolved = (index_path.parent / target).resolve()
            if not resolved.exists():
                errors.append(
                    f"audit lifecycle entry {audit_id} points to missing file: {relative(index_path)} -> {raw_target}"
                )
                continue

            if resolved.parent != AUDITS_ROOT.resolve():
                errors.append(
                    f"audit lifecycle entry {audit_id} must point to a canonical audits/ root file: {raw_target}"
                )

            prior = classifications.get(audit_id)
            if prior is not None:
                prior_state, prior_path = prior
                errors.append(
                    f"audit {audit_id} is classified in multiple lifecycle indexes: "
                    f"{prior_state} ({relative(prior_path)}) and {state} ({relative(index_path)})"
                )
            else:
                classifications[audit_id] = (state, resolved)

    canonical_ids: dict[str, Path] = {}
    if AUDITS_ROOT.is_dir():
        for path in sorted(AUDITS_ROOT.glob("*AUDIT-*.md")):
            match = AUDIT_ID_RE.search(path.name)
            if match is None:
                continue
            audit_id = match.group(0)
            prior = canonical_ids.get(audit_id)
            if prior is not None:
                errors.append(
                    f"duplicate canonical audit ID {audit_id}: {relative(prior)} and {relative(path)}"
                )
            else:
                canonical_ids[audit_id] = path.resolve()

    for audit_id, canonical_path in canonical_ids.items():
        classification = classifications.get(audit_id)
        if classification is None:
            errors.append(f"canonical audit {audit_id} is missing from all lifecycle indexes")
            continue
        _state, indexed_path = classification
        if indexed_path != canonical_path:
            errors.append(
                f"audit lifecycle entry {audit_id} does not point to its canonical file: "
                f"expected {relative(canonical_path)}, got {relative(indexed_path)}"
            )

    for audit_id, (_state, indexed_path) in classifications.items():
        if audit_id not in canonical_ids:
            errors.append(
                f"audit lifecycle index references {audit_id} without a canonical audits/ root record: "
                f"{relative(indexed_path)}"
            )


def check_state_leaks(errors: list[str]) -> None:
    for path in STATE_LEAK_CHECK_FILES:
        if not path.is_file():
            continue
        if STATE_LEAK_RE.search(path.read_text(encoding="utf-8")):
            errors.append(
                f"generic durable governance file contains dated current-classification state: {relative(path)}"
            )


def report_sizes() -> None:
    print("Governance file observations:")
    observed = list(SIZE_REPORT_FILES)
    observed.extend(path for path in discovered_skill_paths() if path.is_file())
    for path in observed:
        if not path.is_file():
            continue
        raw = path.read_bytes()
        line_count = len(raw.decode("utf-8").splitlines())
        print(f"  {relative(path):<62} {line_count:>4} lines  {len(raw):>6} bytes")


def main() -> int:
    errors: list[str] = []

    check_required_files(errors)
    check_root_responsibility_map(errors)
    check_skills(errors)
    check_operation_skill_references(errors)
    check_case_banks(errors)
    check_internal_markdown_links(errors)
    check_normative_id_uniqueness(errors)
    check_audit_lifecycle(errors)
    check_state_leaks(errors)

    report_sizes()
    print(f"Validated governance case banks: {len(CASE_BANK_PATHS)}")
    print(f"Required operation Skills: {len(EXPECTED_OPERATION_SKILLS)}")
    print("Excluded subtree: product-simulation/ contents were not inspected by this tool.")

    if errors:
        print("\nGovernance doctor: FAIL")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("\nGovernance doctor: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
