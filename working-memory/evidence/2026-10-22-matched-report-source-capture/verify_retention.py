"""Review-time byte/mode/source checks; no requests, producers or semantic evaluation.

Run from repository root with the project Python and PYTHONPATH=src. This reads the
private output named in the operational freeze and preserves a non-replacing receipt.
It checks retention/composition only; paired-review.json owns the source-aware review.
"""

from hashlib import sha256
import json
from pathlib import Path
import stat
import subprocess

from upgradepilot.report_file import read_report


BASE = Path(__file__).parent
freeze = json.loads((BASE / "freeze.json").read_text())
private = Path(freeze["private_output"])
index = json.loads((private / "sources/index.json").read_text())
capture = json.loads((private / "capture.json").read_text())
invocation = json.loads((BASE / "invocation.json").read_text())

for row in freeze["source_members"]:
    assert sha256(Path(row["path"]).read_bytes()).hexdigest() == row["sha256"], row["path"]
assert set(Path("src/upgradepilot").rglob("*.py")) == {
    Path(row["path"]) for row in freeze["source_members"] if row["path"].startswith("src/")
}
assert stat.S_IMODE(private.stat().st_mode) == 0o700
assert capture["source_index_sha256"] == sha256((private / "sources/index.json").read_bytes()).hexdigest()
assert capture["report_sha256"] == sha256((private / "report.json").read_bytes()).hexdigest()
assert capture["contract_sha256"] == sha256((BASE / "contract.json").read_bytes()).hexdigest()
assert invocation["freeze_sha256"] == sha256((BASE / "freeze.json").read_bytes()).hexdigest()
assert invocation["startup_inclusive_seconds"] < freeze["external_timeout_seconds"]
assert capture["outcome"] == "normal_report_captured" and invocation["exit_code"] == 0
for source, public in [("report.json", "report.json"), ("report.txt", "report.txt"),
                       ("sources/index.json", "source-index.json"),
                       ("capture.json", "capture-receipt.json")]:
    assert (private / source).read_bytes() == (BASE / public).read_bytes()
read_report(BASE / "report.json")

for row in index["requests"]:
    data = (private / "sources" / row["body"]).read_bytes()
    assert sha256(data).hexdigest() == row["body_sha256"] and len(data) == row["body_bytes"]
assert sum(row["body_bytes"] for row in index["requests"]) == capture["decoded_body_bytes"]
assert capture["requests"] <= json.loads((BASE / "contract.json").read_text())["limits"]["max_requests"]

old = json.loads(Path("working-memory/evidence/2026-10-22-maintainer-utility-readiness/selection.json").read_text())
for row in old["reports"]:
    assert sha256(Path(row["path"]).read_bytes()).hexdigest() == row["historical_sha256"]
assert not subprocess.check_output(["git", "diff", "242cf32d", "--", "src", "tests", "product-simulation"])

members = []
for path in sorted(private.rglob("*")):
    if path.is_file():
        data = path.read_bytes()
        assert stat.S_IMODE(path.stat().st_mode) == 0o600
        members.append({"path": str(path.relative_to(private)), "bytes": len(data),
                        "sha256": sha256(data).hexdigest(), "mode": "0600"})
result = {"proof": "PASS for byte retention, private modes and scoped composition",
          "private_members": members, "private_file_count": len(members),
          "private_bytes": sum(row["bytes"] for row in members),
          "frozen_members_verified": len(freeze["source_members"]),
          "original_reports_verified": len(old["reports"]),
          "product_tests_simulation_unchanged": True,
          "diagnostic_tests": 9, "inclusive_nearest_tests": 79,
          "live_attempts": 1, "live_normal_reports": 1,
          "independent_study_results": 0,
          "recipe_sha256": sha256(Path(__file__).read_bytes()).hexdigest()}
with (BASE / "verification.json").open("x") as stream:
    json.dump(result, stream, indent=2)
    stream.write("\n")
print(json.dumps({key: value for key, value in result.items() if key != "private_members"}))
