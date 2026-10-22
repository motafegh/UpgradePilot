"""Read-only reproduction of this exposed two-case review's mechanical observations.

Run from the repository root with PYTHONPATH=src and the project Python. Prints JSON;
never acquires sources, evaluates native owners, grades semantics or changes old records.
Literal spans locate already-reviewed examples; they are not a general change extractor.
"""

from hashlib import sha256
from itertools import product
import json
from pathlib import Path

from upgradepilot.report_file import read_report


CASES = {
    "httpx": "matched-report-source-capture",
    "opencv": "opencv-matched-report-source-capture",
}
LOCATORS = {
    "httpx": {
        "app_removal": "The deprecated <code>app</code> argument has now been removed.",
        "cert_deprecation": "The <code>cert</code> argument is now deprecated",
    },
    "opencv": {
        "python_support": "Dropped Python 3.6 support.",
        "truncation": "... (truncated)",
    },
}


def wheel_tags(release):
    """Expand only these retained wheel filenames' explicit last-three tag fields.

    This inventory arithmetic does not implement wheel compatibility or target inference.
    It avoids invoking the production owner or packaging's wheel parser as its own oracle.
    """
    tags = set()
    for row in release["urls"]:
        if row["packagetype"] == "bdist_wheel":
            assert row["filename"].endswith(".whl")
            fields = row["filename"][:-4].rsplit("-", 3)[-3:]
            assert len(fields) == 3
            tags.update("-".join(parts) for parts in product(*(f.split(".") for f in fields)))
    return tags


result = {"mode": "exposed_ai_assisted_development_review", "cases": {}}
for name, slug in CASES.items():
    public = Path("working-memory/evidence") / ("2026-10-22-" + slug)
    private = Path(json.loads((public / "freeze.json").read_text())["private_output"])
    capture = json.loads((public / "capture-receipt.json").read_text())
    for original, published in (("report.json", "report.json"), ("report.txt", "report.txt"),
                                ("sources/index.json", "source-index.json"),
                                ("capture.json", "capture-receipt.json")):
        assert (private / original).read_bytes() == (public / published).read_bytes()
    for path, digest in capture["product_source_sha256"].items():
        assert sha256(Path(path).read_bytes()).hexdigest() == digest, path
    index_bytes = (public / "source-index.json").read_bytes()
    assert sha256(index_bytes).hexdigest() == capture["source_index_sha256"]
    report_bytes = (public / "report.json").read_bytes()
    assert sha256(report_bytes).hexdigest() == capture["report_sha256"]
    read_report(public / "report.json")
    report = json.loads(report_bytes)["report"]
    requests = json.loads(index_bytes)["requests"]
    decoded = {}
    for row in requests:
        assert Path(row["body"]).name == row["body"]
        body = (private / "sources" / row["body"]).read_bytes()
        assert len(body) == row["body_bytes"] and sha256(body).hexdigest() == row["body_sha256"]
        if row["state"] == "body_complete":
            decoded[row["number"]] = json.loads(body)
    assert len(requests) == capture["requests"]
    assert sum(r["body_bytes"] for r in requests) == capture["decoded_body_bytes"]
    assert decoded[1]["body"] == decoded[3]["body"]
    pr_body = decoded[1]["body"]
    pr_sources = [s for s in report["sources"] if s["kind"] == "pull_request"]
    assert len(pr_sources) == 1 and pr_sources[0]["content"] is None
    identity = {f["name"]: f["value"] for f in report["identity"]}
    assert identity["base_sha"] == decoded[1]["base"]["sha"]
    assert identity["head_sha"] == decoded[1]["head"]["sha"]
    assert decoded[4] == {"total_count": 0, "workflow_runs": []}
    spans = {}
    for label, literal in LOCATORS[name].items():
        start = pr_body.index(literal)
        spans[label] = {"start_character": start, "end_character": start + len(literal),
                        "occurrences": pr_body.count(literal),
                        "text_sha256": sha256(literal.encode()).hexdigest()}
    old_tags, new_tags = wheel_tags(decoded[6]), wheel_tags(decoded[5])
    removed, added = sorted(old_tags - new_tags), sorted(new_tags - old_tags)
    if name == "opencv":
        facts = next(s for s in report["sources"] if s["kind"] == "artifact_capabilities")["identity"]
        assert removed == sorted(f["value"] for f in facts if f["name"].startswith("removed_tag_"))
        assert added == sorted(f["value"] for f in facts if f["name"].startswith("added_tag_"))
    else:
        assert not removed
    text = (public / "report.txt").read_text()
    result["cases"][name] = {
        "original_report_sha256": sha256(report_bytes).hexdigest(),
        "source_index_sha256": sha256(index_bytes).hexdigest(),
        "product_source_files_verified": len(capture["product_source_sha256"]),
        "http_observations_verified": len(requests),
        "complete_bodies": sum(r["state"] == "body_complete" for r in requests),
        "status_only_bodies": sum(r["state"] == "body_not_consumed" for r in requests),
        "decoded_bytes_verified": capture["decoded_body_bytes"],
        "pr_body_characters": len(pr_body), "pr_body_utf8_sha256": sha256(pr_body.encode()).hexdigest(),
        "spans_in_decoded_pr_body": spans, "pr_body_retained_in_report": False,
        "report_lines": len(text.splitlines()), "report_words": len(text.split()),
        "assessments": len(report["assessments"]), "findings": len(report["findings"]),
        "unknowns": len(report["unknowns"]), "sources": len(report["sources"]),
        "removed_exact_tags": removed, "added_exact_tags": added,
        "proposed_sdist": any(r["packagetype"] == "sdist" for r in decoded[5]["urls"]),
        "maintainer_action": report["action"]["state"],
    }
result["non_claims"] = ["independent utility", "semantic grading", "task-time savings",
                         "target compatibility", "fresh acquisition", "native replay"]
print(json.dumps(result, indent=2))
