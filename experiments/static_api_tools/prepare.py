"""Reconstruct the dated static comparison packet from its two prior receipts."""

import argparse
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile

from upgradepilot.report_file import decode_report

ROOT = Path(__file__).resolve().parents[2]
AV_ARCHIVE = ROOT / "examples/av-tracer/av-tracer-pr-11.zip"
GLYPH_FREEZE = (
    ROOT / "working-memory/evidence/2026-10-28-caller-signature-second-real-case/freeze.json"
)
AV_ARCHIVE_DIGEST = "ffb9365e034833ce4ba3cd35be2080b099d331271b76214e241e6d3a8e115990"


def checked(data, expected):
    if hashlib.sha256(data).hexdigest() != expected:
        raise ValueError(f"Source digest differs from the frozen digest {expected}")
    return data


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def retain(packet, manifest, case, source_id, role, identity, content):
    path = Path(case, role, identity["path"])
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Invalid source path {path}")
    if not path.is_relative_to(Path(case, role)):
        raise ValueError(f"Source path escapes its declared role: {path}")
    data = checked(content.encode(), identity["sha256"])
    destination = packet / path
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("xb") as file:
        file.write(data)
    manifest.append(dict(identity, case=case, source_id=source_id, role=role, file=str(path)))


def prepare(packet, glyph_inputs):
    packet.mkdir(mode=0o700)
    manifest = []
    checked(AV_ARCHIVE.read_bytes(), AV_ARCHIVE_DIGEST)
    with ZipFile(AV_ARCHIVE) as archive:
        av = decode_report(archive.read("source-only/report.json"))
    for source in av.sources:
        if source.kind not in {"target_source", "dependency_source"}:
            continue
        if source.retention != "retained_text":
            continue
        identity = {fact.name: fact.value for fact in source.identity}
        roles = {
            "old_dependency": "httpx-old",
            "proposed_dependency": "httpx-new",
            "constraint_sample": identity.get("package"),
        }
        role = roles.get(identity["role"], "target")
        fields = ("path", "repository", "revision", "sha256", "coverage", "version")
        retain(
            packet, manifest, "av-tracer", source.source_id, role,
            {key: identity[key] for key in fields}, source.content,
        )

    freeze = json.loads(GLYPH_FREEZE.read_bytes())
    sources = json.loads(checked(
        (glyph_inputs / "sources.json").read_bytes(), freeze["source_profile_sha256"],
    ))
    selections = json.loads(checked(
        (glyph_inputs / "selections.json").read_bytes(), freeze["selections_sha256"],
    ))
    if selections["files"] != freeze["selected_files"] or selections["pairs"] != freeze["pairs"]:
        raise ValueError("glyphsLib selections differ from the published pre-run receipt")
    scopes = {scope["source_id"]: scope for scope in sources["scopes"]}
    selected = {(item["source_id"], item["path"]): item for item in selections["files"]}
    for file in sources["files"]:
        role = file["source_id"]
        item = selected.pop((role, file["path"]))
        scope = scopes[role]
        identity = {
            "path": file["path"], "repository": scope["repository"],
            "revision": scope["revision"], "sha256": item["content_sha256"],
            "coverage": item["coverage"],
        }
        retain(packet, manifest, "glyphslib", role, role, identity, file["content"])
    if selected:
        raise ValueError("Some frozen glyphsLib files are absent")

    control = b"class Other:\n    def TestClient(self, app):\n        return app\n\nother = Other()\nother.TestClient(object())\n"
    control_path = Path("controls/unrelated.py")
    (packet / control_path).parent.mkdir()
    (packet / control_path).write_bytes(control)
    write_json(packet / "manifest.json", {
        "files": manifest,
        "controls": [{"file": str(control_path), "sha256": hashlib.sha256(control).hexdigest()}],
    })
    write_json(packet / "glyph-pairs.json", selections["pairs"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path)
    parser.add_argument("glyph_inputs", type=Path)
    args = parser.parse_args()
    prepare(args.packet, args.glyph_inputs)
