"""Planning-only record-shape witness, not a new producer/viewer implementation.

Run from the repository root with PYTHONPATH=src and the project Python. Outputs a
JSON receipt to stdout. Uses in-memory hypothetical records with explicit design IDs;
does not save a new product report, acquire/evaluate evidence or modify frozen inputs.
"""

from dataclasses import replace
from hashlib import sha256
import json
from pathlib import Path

from upgradepilot.report import ReportFact, render_investigation_report
from upgradepilot.report_file import SCHEMA_VERSION, decode_report, encode_report, read_report


CASE_SLUGS = {
    "httpx": "matched-report-source-capture",
    "opencv": "opencv-matched-report-source-capture",
}
result = {"mode": "planning_only_report_shape_witness", "schema_version": SCHEMA_VERSION,
          "cases": {}, "producer_or_viewer_implemented": False}
for name, slug in CASE_SLUGS.items():
    public = Path("working-memory/evidence") / ("2026-10-22-" + slug)
    private = Path(json.loads((public / "freeze.json").read_text())["private_output"])
    source_index = json.loads((public / "source-index.json").read_text())
    first = source_index["requests"][0]
    raw = (private / "sources" / first["body"]).read_bytes()
    assert sha256(raw).hexdigest() == first["body_sha256"]
    description = json.loads(raw)["body"]
    encoded = description.encode("utf-8")
    assert len(encoded) <= 262_144
    original_bytes = (public / "report.json").read_bytes()
    original = read_report(public / "report.json")
    source = next(s for s in original.sources if s.kind == "pull_request")
    assert source.retention == "reference_only" and source.content is None
    variants = []
    for state, text in (("retained", description), ("empty", ""),
                        ("null", None), ("not_recorded", None)):
        data = None if text is None else text.encode("utf-8")
        facts = (ReportFact("description_state", "Description state", state),)
        if data is not None:
            facts += (ReportFact("description_utf8_bytes", "Description bytes", str(len(data))),
                      ReportFact("description_content_sha256", "Description SHA-256",
                                 sha256(data).hexdigest()))
        proposed = replace(source, identity=source.identity + facts,
                           method="DESIGN ONLY: initial PR body observation",
                           retrieved_at=first["finished_at"] if state != "not_recorded" else None,
                           retention="retained_text" if text is not None else "reference_only",
                           content=text,
                           limitation="Design data only; copied PR context is not verified upstream evidence.")
        candidate = replace(original, report_id="design-shape-" + original.report_id,
                            generated_at="2026-10-23T00:00:00+00:00", generator_version="2",
                            sources=tuple(proposed if s.source_id == source.source_id else s
                                          for s in original.sources))
        reopened = decode_report(encode_report(candidate))
        assert reopened == candidate
        assert reopened.assessments == original.assessments
        assert reopened.findings == original.findings and reopened.unknowns == original.unknowns
        assert reopened.action == original.action
        assert reopened.generator_version == "2"
        if text:
            assert text not in render_investigation_report(reopened)
        variants.append(state)
    assert (public / "report.json").read_bytes() == original_bytes
    result["cases"][name] = {
        "original_report_sha256": sha256(original_bytes).hexdigest(),
        "original_pr_response_sha256": first["body_sha256"],
        "decoded_description_utf8_bytes": len(encoded),
        "decoded_description_sha256": sha256(encoded).hexdigest(),
        "compatible_report_source_shapes": variants,
        "original_domain_records_unchanged": True,
        "current_renderer_does_not_dump_body": True,
        "original_file_unchanged": True,
    }
result["non_claims"] = ["new provider/native codec", "implemented source viewer",
                         "automatic semantic interpretation", "independent utility",
                         "fresh normal investigation", "native recovery or replay"]
print(json.dumps(result, indent=2))
