"""One-run audit evidence check; no producer, network or credential operation.

Run from repository root with PYTHONPATH=src:. .venv/bin/python <this file>.
Reads the indexed private captures; writes only this audit's public-safe summary.
"""
from contextlib import ExitStack
from hashlib import sha256
import json
from pathlib import Path
import stat
from unittest.mock import patch

from experiments import api_ordinary_call_signature_trial as owner
from experiments import api_call_signature_trial as curated

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EVIDENCE = ROOT / "working-memory/evidence"


def read(path):
    return json.loads(path.read_bytes())


def check_files(directory, hashes):
    for name, digest in hashes.items():
        path = directory / name
        assert sha256(path.read_bytes()).hexdigest() == digest, name
        assert stat.S_IMODE(path.stat().st_mode) == 0o600, name
    return len(hashes)


freeze = read(EVIDENCE / "2026-11-01-analysis-capacity-and-work-admission/qualified-method.json")
for name, digest in freeze["code_sha256"].items():
    assert sha256((ROOT / name).read_bytes()).hexdigest() == digest, name

rows = read(EVIDENCE / "2026-11-01-analysis-capacity-and-work-admission/retained-qualification-results.json")
checked = []
for row in rows:
    directory = Path(row["directory"])
    count = check_files(directory, row["output_sha256"])
    checked.append((row, directory, count))

digimon = EVIDENCE / "2026-11-01-untouched-partial-analysis-qualification/ordinary-digimon-scraper-pr-16"
contract = read(digimon / "contract.json")
verification = read(digimon / "verification.json")
fresh_root = Path(contract["private_retention"]["root"])
fresh_count = check_files(fresh_root, verification["artifact_hashes"])
curated_root = Path.home() / ".local/share/upgradepilot/caller-signature-evidence/retained-httpx-2026-10-28/attempt-01"
curated_index = read(EVIDENCE / "2026-10-28-caller-signature-build/inspection.json")
curated_hashes = {name: item["sha256"] for name, item in curated_index["private_saved_files"].items()}
curated_count = check_files(curated_root, curated_hashes)

summary = {"proof": "current offline hash, fixed-reader and recorded-work reconciliation",
           "source_hashes_matched": len(freeze["code_sha256"]), "retained_cases": []}
forbidden = ["ast.parse", "requests.sessions.Session.request", "socket.socket.connect",
             "experiments.api_ordinary_call_signature_trial.discover_source_candidates",
             "experiments.api_call_signature.compare_arguments",
             "experiments.api_ordinary_call_signature_trial._read_attempt_credential"]
with ExitStack() as stack:
    for name in forbidden:
        stack.enter_context(patch(name, side_effect=AssertionError("Forbidden during fixed audit open: " + name)))
    for row, directory, count in checked:
        body, catalog = owner.open_ordinary_comparison(directory)
        assert body["work"] == row["work"]
        original_input = read(directory / "input.json")
        assert [(f.source_id, f.path, f.content) for f in catalog.files] == [
            (f["source_id"], f["path"], f["content"]) for f in original_input["catalog"]["files"]]
        summary["retained_cases"].append({"case": row["case"], "matched_artifacts": count,
            "source_files": len(catalog.files), "work": body["work"],
            "unexamined_units": sum(r["state"] == "unexamined" for r in body["analysis_admission"]["units"]),
            "gaps_omitted": body["discovery"]["gaps_omitted"], "fixed_open": "passed"})
    opened = owner.open_fresh_ordinary_pr_attempt(fresh_root)
    assert opened["attempt"]["state"] == verification["state"]
    assert opened["comparison"]["work"] == verification["work"]
    summary["digimon"] = {"matched_artifacts": fresh_count, "state": opened["attempt"]["state"],
        "work": opened["comparison"]["work"], "source_packets": len(opened["source_material"]),
        "fixed_open": "passed"}
    body, catalog = curated.open_comparison(curated_root)
    outcomes = {p["selection"]["id"]: p["comparison"]["outcome"] for p in body["pairs"]}
    assert outcomes == {p["pair"]: p["outcome"] for p in curated_index["comparisons"]}
    summary["curated_httpx_rejection_control"] = {"matched_artifacts": curated_count,
        "outcomes": outcomes, "fixed_open": "passed"}

for row, directory, count in checked:
    check_files(directory, row["output_sha256"])
check_files(fresh_root, verification["artifact_hashes"])
check_files(curated_root, curated_hashes)
summary.update(forbidden_hooks=forbidden, retained_bytes_unchanged=True,
               new_acquisition_or_inference=False,
               limits="Does not rerun producers, grade semantic entailment or prove native product delivery.")
(HERE / "retained-checks.json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps(summary, indent=2))
