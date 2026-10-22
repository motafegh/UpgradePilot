"""Offline retention and source/report representation checks for this exposed case.

Run from repository root with PYTHONPATH=src and the project Python. No producer,
model, HTTP request, native evaluation or independent usefulness grading runs here.
Wheel filename parsing checks consistency using the same packaging library as the
native owner; it is explicitly not an independent semantic oracle.
"""

from hashlib import sha256
import json
from pathlib import Path
import stat
import subprocess

import packaging
from packaging.utils import parse_wheel_filename

from upgradepilot.report import render_investigation_report
from upgradepilot.report_file import read_report


BASE = Path(__file__).parent
freeze = json.loads((BASE / "freeze.json").read_text())
preflight = json.loads((BASE / "preflight.json").read_text())
private = Path(freeze["private_output"])
preflight_private = Path(preflight["private_output"])
capture = json.loads((private / "capture.json").read_text())
index = json.loads((private / "sources/index.json").read_text())
invocation = json.loads((BASE / "invocation.json").read_text())
contract = json.loads((BASE / "contract.json").read_text())

for member in freeze["source_members"]:
    assert sha256(Path(member["path"]).read_bytes()).hexdigest() == member["sha256"], member["path"]
assert set(Path("src/upgradepilot").rglob("*.py")) == {
    Path(row["path"]) for row in freeze["source_members"] if row["path"].startswith("src/")
}
assert capture["contract_sha256"] == sha256((BASE / "contract.json").read_bytes()).hexdigest()
assert capture["source_index_sha256"] == sha256((private / "sources/index.json").read_bytes()).hexdigest()
assert capture["report_sha256"] == sha256((private / "report.json").read_bytes()).hexdigest()
assert invocation["freeze_sha256"] == sha256((BASE / "freeze.json").read_bytes()).hexdigest()
assert invocation["startup_inclusive_seconds"] < freeze["external_timeout_seconds"]
assert capture["outcome"] == "normal_report_captured" and invocation["exit_code"] == 0
for source, public in [("capture.json", "capture-receipt.json"), ("report.json", "report.json"),
                       ("report.txt", "report.txt"), ("sources/index.json", "source-index.json")]:
    assert (private / source).read_bytes() == (BASE / public).read_bytes()
assert (preflight_private / "index.json").read_bytes() == (BASE / "preflight-source-index.json").read_bytes()
assert preflight["source_index_sha256"] == sha256((preflight_private / "index.json").read_bytes()).hexdigest()

report = read_report(BASE / "report.json")
assert render_investigation_report(report) + "\n" == (BASE / "report.txt").read_text()
identity = {fact.name: fact.value for fact in report.identity}
for key in ("repository", "pull_number", "base_sha", "head_sha"):
    assert identity[key] == contract["expected_identity"][key]
rows = {row["number"]: row for row in index["requests"]}


def payload(number):
    return json.loads((private / "sources" / rows[number]["body"]).read_bytes())


for row in rows.values():
    data = (private / "sources" / row["body"]).read_bytes()
    assert len(data) == row["body_bytes"] and sha256(data).hexdigest() == row["body_sha256"]
assert sum(r["body_bytes"] for r in rows.values()) == capture["decoded_body_bytes"]
assert len(rows) <= contract["limits"]["max_requests"]
assert capture["decoded_body_bytes"] <= contract["limits"]["max_total_body_bytes"]
assert len(rows) + preflight["requests"] <= freeze["max_total_requests_including_preflight"]
for number in (1, 3):
    p = payload(number)
    assert str(p["number"]) == identity["pull_number"]
    assert p["base"]["sha"] == identity["base_sha"] and p["head"]["sha"] == identity["head_sha"]
changed = payload(2)
assert len(changed) == 1 and changed[0]["filename"] == "requirements.txt"
assert "-opencv-python==4.2.0.32" in changed[0]["patch"] and "+opencv-python==4.8.1.78" in changed[0]["patch"]
assert payload(4)["total_count"] == 0 and payload(4)["workflow_runs"] == []
for number, version in ((5, "4.8.1.78"), (6, "4.2.0.32")):
    p = payload(number)
    assert p["info"]["name"] == "opencv-python" and p["info"]["version"] == version


def tags(release):
    return {str(tag) for item in release["urls"] if item["packagetype"] == "bdist_wheel"
            for tag in parse_wheel_filename(item["filename"])[3]}


old_tags, new_tags = tags(payload(6)), tags(payload(5))
source = next(s for s in report.sources if s.kind == "artifact_capabilities")
removed = {f.value for f in source.identity if f.name.startswith("removed_tag_")}
added = {f.value for f in source.identity if f.name.startswith("added_tag_")}
assert removed == old_tags - new_tags and added == new_tags - old_tags
assessments = {a.assessment_id: a for a in report.assessments}
facts = {f.name: f.value for f in assessments["artifact-candidate"].facts}
assert facts["removed_count"] == str(len(removed)) and facts["added_count"] == str(len(added))
assert any(x["packagetype"] == "sdist" for x in payload(5)["urls"])
assert facts["source_distribution"] == "available"
assert assessments["artifact-environments"].state == "not established"
assert assessments["artifact-impact"].state == "unresolved" and report.action.state == "abstain"

retention = []
for label, directory in (("normal", private), ("preflight", preflight_private)):
    assert stat.S_IMODE(directory.stat().st_mode) == 0o700
    for path in sorted(directory.rglob("*")):
        if path.is_file():
            data = path.read_bytes()
            assert stat.S_IMODE(path.stat().st_mode) == 0o600
            retention.append({"capture": label, "path": str(path.relative_to(directory)),
                              "bytes": len(data), "sha256": sha256(data).hexdigest(), "mode": "0600"})

prior_base = Path("working-memory/evidence/2026-10-22-matched-report-source-capture")
prior_private = Path(json.loads((prior_base / "freeze.json").read_text())["private_output"])
prior_members = json.loads((prior_base / "verification.json").read_text())["private_members"]
assert {str(p.relative_to(prior_private)) for p in prior_private.rglob("*") if p.is_file()} == {r["path"] for r in prior_members}
for row in prior_members:
    assert sha256((prior_private / row["path"]).read_bytes()).hexdigest() == row["sha256"]
old = json.loads(Path("working-memory/evidence/2026-10-22-maintainer-utility-readiness/selection.json").read_text())
for row in old["reports"]:
    assert sha256(Path(row["path"]).read_bytes()).hexdigest() == row["historical_sha256"]
assert not subprocess.check_output(["git", "diff", "77f745c8", "--", "src", "tests", "tools", "experiments", "product-simulation"])

result = {"proof": "PASS for exposed byte/mode/source/report representation checks",
          "frozen_members_verified": len(freeze["source_members"]),
          "private_members": retention, "private_file_count": len(retention),
          "private_bytes": sum(x["bytes"] for x in retention),
          "prior_httpx_private_files_unchanged": len(prior_members),
          "original_report_hashes_unchanged": len(old["reports"]),
          "normal_requests": len(rows), "preflight_requests": preflight["requests"],
          "packaging_version_at_review": packaging.__version__,
          "removed_exact_tags": len(removed), "added_exact_tags": len(added),
          "independent_study_results": 0, "new_test_runs": 0,
          "recipe_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
          "non_claim": "Same-library representation check is not independent semantic or utility proof"}
with (BASE / "verification.json").open("x") as stream:
    json.dump(result, stream, indent=2)
    stream.write("\n")
print(json.dumps({k: v for k, v in result.items() if k != "private_members"}))
