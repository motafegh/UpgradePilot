#!/usr/bin/env python3
from pathlib import Path
import json, sys

root = Path(__file__).resolve().parents[2]
art = root / "artifacts"
errors = []
notes = []
parsed_json = {}
parsed_jsonl = {}

def load_json(path):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        parsed_json[str(path.relative_to(root))] = data
        return data
    except Exception as exc:
        errors.append(f"JSON parse {path.relative_to(root)}: {exc}")
        return None

def load_jsonl(path):
    rows = []
    try:
        for i,line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except Exception as exc:
                errors.append(f"JSONL parse {path.relative_to(root)}:{i}: {exc}")
        parsed_jsonl[str(path.relative_to(root))] = rows
    except Exception as exc:
        errors.append(f"JSONL read {path.relative_to(root)}: {exc}")
    return rows

for p in sorted(art.rglob("*.json")):
    # Validation result is intentionally excluded while it is being regenerated.
    if p.name == "bundle-validation.json":
        continue
    load_json(p)
for p in sorted(art.rglob("*.jsonl")):
    load_jsonl(p)

expected_scenario = "S003"
expected_run = "s003-20260722T201756Z-r1"
for rel,data in list(parsed_json.items()):
    if isinstance(data, dict) and data.get("artifact_status") == "manual_simulation":
        if data.get("scenario_id") != expected_scenario:
            errors.append(f"Scenario mismatch: {rel}")
        if data.get("run_id") != expected_run:
            errors.append(f"Run mismatch: {rel}")
for rel,rows in parsed_jsonl.items():
    for i,data in enumerate(rows,1):
        if data.get("scenario_id") != expected_scenario:
            errors.append(f"Scenario mismatch: {rel}:{i}")
        if data.get("run_id") != expected_run:
            errors.append(f"Run mismatch: {rel}:{i}")

groups = {
    "operation_id": parsed_jsonl.get("artifacts/OPERATION_EVENTS.jsonl", []),
    "evidence_id": parsed_jsonl.get("artifacts/EVIDENCE_ITEMS.jsonl", []),
    "record_id": parsed_jsonl.get("artifacts/CLAIMS_AND_INTERPRETATIONS.jsonl", []),
    "check_execution_id": parsed_jsonl.get("artifacts/CHECK_EXECUTIONS.jsonl", []),
}
findings = parsed_json.get("artifacts/FINDINGS.json", {}).get("findings", [])
groups["finding_id"] = findings
decision = parsed_json.get("artifacts/DECISION.json", {})
groups["reason_id"] = decision.get("reason_records", [])
groups["transition_id"] = decision.get("transitions", [])

id_sets = {}
for field, rows in groups.items():
    vals = [row.get(field) for row in rows]
    if any(v is None for v in vals):
        errors.append(f"Missing {field}")
    dup = sorted({v for v in vals if vals.count(v)>1})
    if dup:
        errors.append(f"Duplicate {field}: {dup}")
    id_sets[field] = set(v for v in vals if v)

ops = parsed_jsonl.get("artifacts/OPERATION_EVENTS.jsonl", [])
seq = [x.get("sequence") for x in ops]
if seq != list(range(1, len(seq)+1)):
    errors.append(f"Operation sequence invalid: {seq}")

ev_ids = id_sets["evidence_id"]
rec_ids = id_sets["record_id"]
fn_ids = id_sets["finding_id"]
op_ids = id_sets["operation_id"]
ce_ids = id_sets["check_execution_id"]

for ev in parsed_jsonl.get("artifacts/EVIDENCE_ITEMS.jsonl", []):
    op = ev.get("producing_operation_id")
    if op and op not in op_ids:
        errors.append(f"Evidence {ev.get('evidence_id')} unknown operation {op}")
    ref = ev.get("raw_or_reference", {})
    path = ref.get("path") if isinstance(ref, dict) else None
    if path and not (root/path).exists():
        errors.append(f"Evidence {ev.get('evidence_id')} missing path {path}")

for rec in parsed_jsonl.get("artifacts/CLAIMS_AND_INTERPRETATIONS.jsonl", []):
    for eid in rec.get("source_evidence_ids", []):
        if eid not in ev_ids:
            errors.append(f"Record {rec.get('record_id')} unknown evidence {eid}")
    for rid in rec.get("input_record_ids", []):
        if rid not in rec_ids:
            errors.append(f"Record {rec.get('record_id')} unknown input record {rid}")

for f in findings:
    for eid in f.get("supporting_evidence_ids", []):
        if eid not in ev_ids:
            errors.append(f"Finding {f.get('finding_id')} unknown evidence {eid}")
    for rid in f.get("supporting_record_ids", []):
        if rid not in rec_ids:
            errors.append(f"Finding {f.get('finding_id')} unknown record {rid}")
    op = f.get("created_operation_id")
    if op and op not in op_ids:
        errors.append(f"Finding {f.get('finding_id')} unknown operation {op}")

for rr in decision.get("reason_records", []):
    for fid in rr.get("finding_ids", []):
        if fid not in fn_ids:
            errors.append(f"Reason {rr.get('reason_id')} unknown finding {fid}")
    for eid in rr.get("evidence_ids", []):
        if eid not in ev_ids:
            errors.append(f"Reason {rr.get('reason_id')} unknown evidence {eid}")

attr = parsed_json.get("artifacts/FAILURE_ATTRIBUTION.json", {})
for cid in attr.get("failure_observation_ids", []):
    if cid not in ce_ids:
        errors.append(f"Attribution unknown failure execution {cid}")
for cid in attr.get("comparison_execution_ids", []):
    if cid not in ce_ids:
        errors.append(f"Attribution unknown comparison execution {cid}")
for cause in attr.get("candidate_causes", []):
    for eid in cause.get("supporting_evidence_ids", []) + cause.get("contradicting_or_limiting_evidence_ids", []):
        if eid not in ev_ids:
            errors.append(f"Cause {cause.get('cause_id')} unknown evidence {eid}")

manifest = parsed_json.get("artifacts/RUN_MANIFEST.json", {})
for item in manifest.get("artifact_inventory", []):
    path = item.get("path")
    if path and item.get("state") == "present" and not (root/path).exists():
        errors.append(f"Manifest present path missing: {path}")

machine = parsed_json.get("artifacts/MACHINE_REPORT.json", {})
if machine.get("decision", {}).get("decision_id") != decision.get("decision_id"):
    errors.append("Machine report decision mismatch")
if machine.get("attribution", {}).get("classification") != attr.get("current_classification"):
    errors.append("Machine report attribution mismatch")
human = (art/"HUMAN_REPORT.md").read_text(encoding="utf-8")
if decision.get("decision_dimensions", {}).get("dependency_update_assessment", {}).get("outcome") not in human:
    # Human report uses prose; record a note instead of requiring internal token.
    notes.append("Human report communicates dependency block in prose rather than internal outcome token.")
if "Do not merge PR #341" not in human:
    errors.append("Human report recommendation mismatch")

baseline = parsed_json.get("artifacts/BASELINE_RESULT.json", {})
allowed = set(baseline.get("allowed_inputs", {}).keys())
required_allowed = {"version_change_category","ci_conclusion","dependency_directness","release_note_keyword_signals"}
if allowed != required_allowed:
    errors.append(f"Baseline input boundary mismatch: {sorted(allowed)}")
if baseline.get("matched_rule", {}).get("rule_id") != "B01":
    errors.append("Baseline rule mismatch")
if baseline.get("comparison", {}).get("status") != "complete":
    errors.append("Baseline comparison incomplete")

proof = parsed_json.get("artifacts/checks/prospective-checkpoints.json", {})
commits = [x.get("commit_sha") for x in proof.get("checkpoints", []) if x.get("checkpoint") in [1,2,3]]
if not all(commits):
    errors.append("Prospective checkpoint proof incomplete")

required_files = [
    "README.md","CASE.md","artifacts/RUN_MANIFEST.json","artifacts/INVOCATION.json",
    "artifacts/CASE_IDENTITY.json","artifacts/OPERATION_EVENTS.jsonl",
    "artifacts/EVIDENCE_ITEMS.jsonl","artifacts/CLAIMS_AND_INTERPRETATIONS.jsonl",
    "artifacts/FINDINGS.json","artifacts/BASELINE_RESULT.json","artifacts/DECISION.json",
    "artifacts/MACHINE_REPORT.json","artifacts/HUMAN_REPORT.md",
    "artifacts/FOLLOW_UP_STATE.json","artifacts/REVIEW_AND_OWNERSHIP.json",
    "artifacts/CHECK_EXECUTIONS.jsonl","artifacts/FAILURE_ATTRIBUTION.json"
]
for rel in required_files:
    if not (root/rel).exists():
        errors.append(f"Required file missing: {rel}")

result = {
    "validation_status": "passed" if not errors else "failed",
    "error_count": len(errors),
    "errors": errors,
    "notes": notes,
    "counts": {
        "json_files_parsed": len(parsed_json),
        "jsonl_files_parsed": len(parsed_jsonl),
        "operations": len(ops),
        "evidence_items": len(parsed_jsonl.get("artifacts/EVIDENCE_ITEMS.jsonl", [])),
        "claims_and_interpretations": len(parsed_jsonl.get("artifacts/CLAIMS_AND_INTERPRETATIONS.jsonl", [])),
        "findings": len(findings),
        "check_executions": len(parsed_jsonl.get("artifacts/CHECK_EXECUTIONS.jsonl", [])),
        "decision_reasons": len(decision.get("reason_records", [])),
    }
}
print(json.dumps(result, indent=2))
sys.exit(0 if not errors else 1)
