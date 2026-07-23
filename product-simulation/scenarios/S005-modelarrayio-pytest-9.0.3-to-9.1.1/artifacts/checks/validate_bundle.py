#!/usr/bin/env python3
"""Validate the illustrative S005 manual-simulation bundle."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXPECTED_SCENARIO = "S005"
EXPECTED_RUN = "s005-20260723T123700Z-r1"

REQUIRED = [
    "README.md", "CASE.md", "artifacts/RUN_MANIFEST.json",
    "artifacts/INVOCATION.json", "artifacts/CASE_IDENTITY.json",
    "artifacts/OPERATION_EVENTS.jsonl", "artifacts/EVIDENCE_ITEMS.jsonl",
    "artifacts/CLAIMS_AND_INTERPRETATIONS.jsonl", "artifacts/FINDINGS.json",
    "artifacts/BASELINE_RESULT.json", "artifacts/CHECK_EXECUTIONS.jsonl",
    "artifacts/DECISION.json", "artifacts/MACHINE_REPORT.json",
    "artifacts/HUMAN_REPORT.md", "artifacts/FOLLOW_UP_STATE.json",
    "artifacts/REVIEW_AND_OWNERSHIP.json",
    "artifacts/checks/prospective-checkpoints.json",
]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            errors.append(f"missing:{rel}")

    json_docs = {}
    jsonl_docs = {}
    for path in ROOT.rglob("*.json"):
        try:
            json_docs[path.relative_to(ROOT).as_posix()] = load_json(path)
        except Exception as exc:
            errors.append(f"invalid_json:{path.relative_to(ROOT)}:{exc}")
    for path in ROOT.rglob("*.jsonl"):
        try:
            jsonl_docs[path.relative_to(ROOT).as_posix()] = load_jsonl(path)
        except Exception as exc:
            errors.append(f"invalid_jsonl:{path.relative_to(ROOT)}:{exc}")

    for rel, doc in json_docs.items():
        if rel.endswith("fresh-clone-attempt.json"):
            continue
        if isinstance(doc, dict) and "scenario_id" in doc and doc["scenario_id"] != EXPECTED_SCENARIO:
            errors.append(f"scenario_mismatch:{rel}")
        if isinstance(doc, dict) and "run_id" in doc and doc["run_id"] != EXPECTED_RUN:
            errors.append(f"run_mismatch:{rel}")

    for rel, rows in jsonl_docs.items():
        for idx, row in enumerate(rows, 1):
            if row.get("scenario_id") != EXPECTED_SCENARIO or row.get("run_id") != EXPECTED_RUN:
                errors.append(f"jsonl_identity:{rel}:{idx}")

    ops = jsonl_docs.get("artifacts/OPERATION_EVENTS.jsonl", [])
    evidence = jsonl_docs.get("artifacts/EVIDENCE_ITEMS.jsonl", [])
    transformations = jsonl_docs.get("artifacts/CLAIMS_AND_INTERPRETATIONS.jsonl", [])
    executions = jsonl_docs.get("artifacts/CHECK_EXECUTIONS.jsonl", [])
    findings = json_docs.get("artifacts/FINDINGS.json", {}).get("findings", [])
    decision = json_docs.get("artifacts/DECISION.json", {})
    baseline = json_docs.get("artifacts/BASELINE_RESULT.json", {})
    report = json_docs.get("artifacts/MACHINE_REPORT.json", {})

    def unique(rows, key, label):
        vals = [row.get(key) for row in rows]
        if len(vals) != len(set(vals)) or None in vals:
            errors.append(f"non_unique_or_missing:{label}")

    unique(ops, "operation_id", "operations")
    unique(evidence, "evidence_id", "evidence")
    unique(transformations, "transformation_id", "transformations")
    unique(executions, "execution_id", "executions")
    unique(findings, "finding_id", "findings")

    evidence_ids = {x["evidence_id"] for x in evidence}
    transformation_ids = {x["transformation_id"] for x in transformations}
    finding_ids = {x["finding_id"] for x in findings}
    for tr in transformations:
        if not set(tr.get("evidence_refs", [])) <= evidence_ids:
            errors.append(f"bad_evidence_ref:{tr.get('transformation_id')}")
    for finding in findings:
        if not set(finding.get("transformation_refs", [])) <= transformation_ids:
            errors.append(f"bad_transformation_ref:{finding.get('finding_id')}")
    for reason in decision.get("reasons", []):
        if not set(reason.get("finding_refs", [])) <= finding_ids:
            errors.append(f"bad_finding_ref:{reason.get('reason_id')}")

    if baseline.get("outcome") != "run_targeted_checks":
        errors.append("baseline_action")
    if decision.get("action") != "merge_after_normal_review" or not decision.get("action_changed_from_baseline"):
        errors.append("decision_action_change")
    if "baseline_wrong_action" not in decision.get("comparison_classifications", []):
        errors.append("comparison_class")
    if report.get("full_decision", {}).get("action") != decision.get("action"):
        errors.append("report_decision_mismatch")

    result = {
        "validation_status": "passed" if not errors else "failed",
        "error_count": len(errors),
        "errors": errors,
        "counts": {
            "json_files": len(json_docs), "jsonl_files": len(jsonl_docs),
            "operations": len(ops), "evidence": len(evidence),
            "transformations": len(transformations), "executions": len(executions),
            "findings": len(findings), "decision_reasons": len(decision.get("reasons", [])),
        },
    }
    print(json.dumps(result, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
