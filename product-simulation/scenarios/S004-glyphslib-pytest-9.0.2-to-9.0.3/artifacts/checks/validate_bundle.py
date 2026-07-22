from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

SCENARIO_ID = "S004"
RUN_ID = "s004-20260722T224500Z-r1"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{line_number} is not an object")
        records.append(value)
    return records


def main() -> int:
    scenario_root = Path(__file__).resolve().parents[2]
    artifacts = scenario_root / "artifacts"
    errors: list[str] = []

    required = [
        scenario_root / "README.md",
        scenario_root / "CASE.md",
        artifacts / "RUN_MANIFEST.json",
        artifacts / "INVOCATION.json",
        artifacts / "CASE_IDENTITY.json",
        artifacts / "OPERATION_EVENTS.jsonl",
        artifacts / "EVIDENCE_ITEMS.jsonl",
        artifacts / "CLAIMS_AND_INTERPRETATIONS.jsonl",
        artifacts / "FINDINGS.json",
        artifacts / "BASELINE_RESULT.json",
        artifacts / "STOPPING_EVALUATION.json",
        artifacts / "DECISION.json",
        artifacts / "MACHINE_REPORT.json",
        artifacts / "HUMAN_REPORT.md",
        artifacts / "FOLLOW_UP_STATE.json",
        artifacts / "REVIEW_AND_OWNERSHIP.json",
        artifacts / "checks/prospective-checkpoints.json",
    ]
    for path in required:
        if not path.exists():
            errors.append(f"missing required path: {path.relative_to(scenario_root)}")

    json_paths = [
        path
        for path in artifacts.rglob("*.json")
        if path.name != "bundle-validation.json"
    ]
    parsed_json: dict[str, Any] = {}
    for path in json_paths:
        try:
            value = load_json(path)
            parsed_json[str(path.relative_to(scenario_root))] = value
        except Exception as exc:  # noqa: BLE001 - validator must report malformed artifacts
            errors.append(f"invalid JSON {path.relative_to(scenario_root)}: {exc}")

    jsonl_paths = list(artifacts.rglob("*.jsonl"))
    parsed_jsonl: dict[str, list[dict[str, Any]]] = {}
    for path in jsonl_paths:
        try:
            records = load_jsonl(path)
            parsed_jsonl[str(path.relative_to(scenario_root))] = records
        except Exception as exc:  # noqa: BLE001
            errors.append(f"invalid JSONL {path.relative_to(scenario_root)}: {exc}")

    def check_identity(value: Any, location: str) -> None:
        if isinstance(value, dict) and "scenario_id" in value:
            if value.get("scenario_id") != SCENARIO_ID:
                errors.append(f"scenario mismatch in {location}")
            if value.get("run_id") != RUN_ID:
                errors.append(f"run mismatch in {location}")

    for location, value in parsed_json.items():
        check_identity(value, location)
    for location, records in parsed_jsonl.items():
        for index, record in enumerate(records):
            check_identity(record, f"{location}[{index}]")

    operations = parsed_jsonl.get("artifacts/OPERATION_EVENTS.jsonl", [])
    evidence = parsed_jsonl.get("artifacts/EVIDENCE_ITEMS.jsonl", [])
    transformations = parsed_jsonl.get("artifacts/CLAIMS_AND_INTERPRETATIONS.jsonl", [])
    findings_doc = parsed_json.get("artifacts/FINDINGS.json", {})
    findings = findings_doc.get("findings", []) if isinstance(findings_doc, dict) else []

    def unique(records: list[dict[str, Any]], field: str, label: str) -> set[str]:
        values = [record.get(field) for record in records]
        if any(not isinstance(value, str) or not value for value in values):
            errors.append(f"missing or invalid {field} in {label}")
        clean = {value for value in values if isinstance(value, str) and value}
        if len(clean) != len(values):
            errors.append(f"duplicate {field} in {label}")
        return clean

    operation_ids = unique(operations, "operation_id", "operations")
    evidence_ids = unique(evidence, "evidence_id", "evidence")
    transformation_ids = unique(transformations, "transformation_id", "transformations")
    finding_ids = unique(findings, "finding_id", "findings")

    timestamps = [record.get("occurred_at", "") for record in operations]
    if timestamps != sorted(timestamps):
        errors.append("operation timestamps are not ordered")

    for record in transformations:
        for evidence_id in record.get("evidence_ids", []):
            if evidence_id not in evidence_ids:
                errors.append(f"unknown evidence reference {evidence_id} in transformation")

    for finding in findings:
        for evidence_id in finding.get("evidence_ids", []):
            if evidence_id not in evidence_ids:
                errors.append(f"unknown evidence reference {evidence_id} in finding")
        for transformation_id in finding.get("transformation_ids", []):
            if transformation_id not in transformation_ids:
                errors.append(f"unknown transformation reference {transformation_id} in finding")

    decision = parsed_json.get("artifacts/DECISION.json", {})
    for reason in decision.get("reason_records", []):
        for evidence_id in reason.get("evidence_ids", []):
            if evidence_id not in evidence_ids:
                errors.append(f"unknown evidence reference {evidence_id} in decision")
        for finding_id in reason.get("finding_ids", []):
            if finding_id not in finding_ids:
                errors.append(f"unknown finding reference {finding_id} in decision")

    manifest = parsed_json.get("artifacts/RUN_MANIFEST.json", {})
    for relative in manifest.get("present_artifacts", []):
        if not (scenario_root / relative).exists():
            errors.append(f"manifest path missing: {relative}")

    baseline = parsed_json.get("artifacts/BASELINE_RESULT.json", {})
    machine = parsed_json.get("artifacts/MACHINE_REPORT.json", {})
    follow_up = parsed_json.get("artifacts/FOLLOW_UP_STATE.json", {})
    stopping = parsed_json.get("artifacts/STOPPING_EVALUATION.json", {})
    review = parsed_json.get("artifacts/REVIEW_AND_OWNERSHIP.json", {})

    if decision.get("broad_outcome") != "merge_after_normal_review":
        errors.append("unexpected decision outcome")
    if baseline.get("outcome") != decision.get("broad_outcome"):
        errors.append("baseline/full outcome mismatch")
    expected_classes = {"baseline_sufficient", "full_investigation_added_no_material_value"}
    if set(baseline.get("comparison_classification", [])) != expected_classes:
        errors.append("baseline comparison classification mismatch")
    if machine.get("decision", {}).get("outcome") != decision.get("broad_outcome"):
        errors.append("machine report decision mismatch")
    if follow_up.get("current_decision_id") != decision.get("decision_id"):
        errors.append("follow-up decision reference mismatch")
    if stopping.get("current_state") != "stopped_baseline_sufficient":
        errors.append("stopping state is not final")
    if stopping.get("conditional_stages_activated") != []:
        errors.append("conditional stages unexpectedly activated")
    if review.get("execution_status") != "complete_at_justified_stop":
        errors.append("review execution status is not complete")
    if not operation_ids:
        errors.append("no operation records")

    result = {
        "validation_status": "passed" if not errors else "failed",
        "error_count": len(errors),
        "errors": errors,
        "counts": {
            "json_files_parsed": len(json_paths),
            "jsonl_files_parsed": len(jsonl_paths),
            "operations": len(operations),
            "evidence_items": len(evidence),
            "claims_and_interpretations": len(transformations),
            "findings": len(findings),
            "decision_reasons": len(decision.get("reason_records", [])),
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
