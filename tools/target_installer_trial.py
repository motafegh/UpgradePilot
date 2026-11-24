"""Capture and verify the controlled NumPy installer-evidence trial.

Capture uses only the standard library on either fixture interpreter. Verify runs
with the installed UpgradePilot package and consumes locally saved provider bytes.
"""

from __future__ import annotations

import argparse
import io
import json
import os
import platform
import re
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from hashlib import sha256
from importlib.metadata import version
from pathlib import Path


REPOSITORY = "motafegh/UpgradePilot"
FIXTURE = "tools/fixtures/installer-tags/requirements.txt"
FIXTURE_BASE = "ca774c64f0e8ca75fcb58414ed2ee30704bea1c9"
WORKFLOW = ".github/workflows/target-installer-evidence-trial.yml"
STEP = "Capture installer tags"
PIP_VERSION = "25.3"
INDEX = "https://pypi.org/simple"
BASE_REQUIREMENT = "numpy==2.2.6"
PROPOSED_REQUIREMENT = "numpy==2.3.0"
PYTHON_ROWS = {
    "3.10.22": ("established_applicable", False),
    "3.11.18": ("established_not_applicable", True),
}
RELEASE_DIGESTS = {
    "2.2.6": "c8f5ba0488e6785eb676ff66a43bbb810e511e0cfe8a018bb021c89c7f74f25c",
    "2.3.0": "01d309397a4ffff996f95f78a8d5957f9a26b6aa44863cf4a0b7a2bb560c6e75",
}
TAG_LIMIT = 4096
ARTIFACT_LIMIT = 512 * 1024
TAG_LINE = re.compile(r"  ([a-z0-9_]+-[a-z0-9_]+-[a-z0-9_]+)")
TAG_HEADER = re.compile(r"Compatible tags: ([0-9]{1,6})")
PIP_ARGS = ("-I", "-m", "pip", "--isolated", "debug", "--verbose")


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def git(*args):
    return subprocess.check_output(("git", *args), text=True, timeout=15).strip()


def fixture_patch(head):
    require(git("show", f"{FIXTURE_BASE}:{FIXTURE}") == BASE_REQUIREMENT, "Fixture base pin mismatch")
    require(git("show", f"{head}:{FIXTURE}") == PROPOSED_REQUIREMENT, "Fixture proposed pin mismatch")
    diff = git("diff", "--no-ext-diff", FIXTURE_BASE, head, "--", FIXTURE)
    return diff[diff.index("@@"):]


def read_tags(data):
    lines = data.decode("ascii").splitlines()
    require(bool(lines), "Empty tag block")
    header = TAG_HEADER.fullmatch(lines[0])
    require(header is not None, "Missing complete tag count")
    count = int(header[1])
    require(0 < count <= TAG_LIMIT and len(lines) == count + 1, "Incomplete or oversized tag block")
    matches = [TAG_LINE.fullmatch(line) for line in lines[1:]]
    require(all(matches), "Invalid tag row")
    tags = frozenset(match[1] for match in matches)
    require(len(tags) == count, "Duplicate tag row")
    return tags


def capture(destination):
    env = os.environ
    head = git("rev-parse", "HEAD")
    require(env["GITHUB_REPOSITORY"] == REPOSITORY and env["GITHUB_SHA"] == head, "Unexpected checkout")
    require(env["GITHUB_EVENT_NAME"] == "workflow_dispatch" and env["GITHUB_JOB"] == "capture", "Unexpected job")
    fixture_patch(head)
    interpreter = platform.python_version()
    require(interpreter == env["TRIAL_PYTHON"] and interpreter in PYTHON_ROWS, "Interpreter pin mismatch")
    require(platform.python_implementation() == "CPython" and version("pip") == PIP_VERSION, "Tool pin mismatch")
    require((env["RUNNER_OS"], env["RUNNER_ARCH"], env["ImageOS"]) == ("Linux", "X64", "ubuntu24"), "Unexpected runner")
    require(bool(env["ImageVersion"]), "Missing runner image version")
    debug = subprocess.check_output((sys.executable, *PIP_ARGS), timeout=30)
    header = re.search(rb"^Compatible tags: [0-9]+\r?$", debug, re.MULTILINE)
    require(header is not None, "pip did not emit a tag block")
    block = debug[header.start():]
    tags = read_tags(block)
    python_tag = "cp" + "".join(interpreter.split(".")[:2])
    require(f"{python_tag}-{python_tag}-manylinux_2_28_x86_64" in tags, "Trial needs a compatible glibc runner")
    manifest = {
        "version": 1,
        "repository": REPOSITORY,
        "checkout": head,
        "fixture_base": FIXTURE_BASE,
        "run": int(env["GITHUB_RUN_ID"]),
        "attempt": int(env["GITHUB_RUN_ATTEMPT"]),
        "job_key": env["GITHUB_JOB"],
        "python": interpreter,
        "pip": PIP_VERSION,
        "runner_image": env["ImageOS"],
        "runner_image_version": env["ImageVersion"],
        "observed_at": datetime.now(timezone.utc).isoformat(),
        "step": STEP,
        "command": ["python", *PIP_ARGS],
        "index_scope": INDEX,
        "tag_count": len(tags),
        "tag_bytes": len(block),
        "tag_sha256": sha256(block).hexdigest(),
    }
    manifest_bytes = (json.dumps(manifest, indent=2) + "\n").encode("utf-8")
    require(len(block) + len(manifest_bytes) <= ARTIFACT_LIMIT, "Expanded artifact exceeds limit")
    destination.mkdir()
    (destination / "manifest.json").write_bytes(manifest_bytes)
    (destination / "pip-tags.txt").write_bytes(block)


def unpack(blob):
    with zipfile.ZipFile(io.BytesIO(blob)) as archive:
        files = archive.infolist()
        require(sorted(file.filename for file in files) == ["manifest.json", "pip-tags.txt"], "Unexpected archive members")
        require(sum(file.file_size for file in files) <= ARTIFACT_LIMIT, "Expanded artifact exceeds limit")
        return json.loads(archive.read("manifest.json")), archive.read("pip-tags.txt")


def validate_artifact(blob, artifact, run, job, interpreter):
    require(blob is not None, "Missing artifact")
    require(len(blob) <= ARTIFACT_LIMIT, "Compressed artifact exceeds limit")
    parent = artifact["workflow_run"]
    require(
        parent["id"] == run["id"] and parent["head_sha"] == run["head_sha"]
        and parent["repository_id"] == run["repository"]["id"],
        "Artifact does not belong to the exact run",
    )
    require(artifact["digest"] == "sha256:" + sha256(blob).hexdigest(), "Artifact digest mismatch")
    manifest, block = unpack(blob)
    fields = {
        "version": 1, "repository": REPOSITORY, "checkout": run["head_sha"], "fixture_base": FIXTURE_BASE,
        "run": run["id"], "attempt": run["run_attempt"], "job_key": "capture", "python": interpreter,
        "step": STEP, "runner_image": "ubuntu24", "pip": PIP_VERSION,
        "command": ["python", *PIP_ARGS], "index_scope": INDEX,
    }
    require(all(manifest.get(name) == value for name, value in fields.items()), "Artifact revision, attempt or job row mismatch")
    require(manifest["runner_image_version"] and datetime.fromisoformat(manifest["observed_at"]).utcoffset() is not None,
            "Missing runner or observation identity")
    require(job["name"] == f"Installer tags ({interpreter})" and job["head_sha"] == run["head_sha"]
            and job["run_id"] == run["id"] and job["run_attempt"] == run["run_attempt"], "Job identity mismatch")
    steps = [step for step in job["steps"] if step["name"] == STEP]
    require(len(steps) == 1 and steps[0]["conclusion"] == "success", "Capture step not established")
    require(manifest["tag_sha256"] == sha256(block).hexdigest() and manifest["tag_bytes"] == len(block), "Tag block digest mismatch")
    tags = read_tags(block)
    require(manifest["tag_count"] == len(tags), "Manifest tag count mismatch")
    return manifest, tags, steps[0]["number"]


def load_candidate(directory, head):
    from unittest.mock import Mock

    from upgradepilot.dependency.analysis import DependencyChangeAnalysis, analyze_dependency_change
    from upgradepilot.github.pull_request import ChangedFile, PullRequestIdentity
    from upgradepilot.impact.artifact_serviceability import (
        ArtifactServiceabilityImpactCandidate,
        build_artifact_serviceability_impact_candidate,
    )
    from upgradepilot.pypi.release import PackageReleaseEvidence, PyPIReleaseClient

    fixture = PullRequestIdentity(REPOSITORY, 0, "Controlled installer trial", "open", False,
                                  "controlled-fixture", "fixture-base", FIXTURE_BASE, "fixture-head", head, 1)
    changed = ChangedFile(FIXTURE, "modified", 1, 1, 2, fixture_patch(head))
    repository_client = Mock()
    analysis = analyze_dependency_change(fixture, (changed,), repository_client)
    require(isinstance(analysis, DependencyChangeAnalysis) and not repository_client.mock_calls,
            "Fixture change not admitted from exact patch")

    def frozen_release(url, **_kwargs):
        for release_version, digest in RELEASE_DIGESTS.items():
            if url == f"https://pypi.org/pypi/numpy/{release_version}/json":
                path = directory / f"numpy-{release_version}.json"
                require(path.stat().st_size <= 1_000_000, "Release metadata exceeds limit")
                payload = path.read_bytes()
                require(sha256(payload).hexdigest() == digest, "Frozen release hash mismatch")
                return Mock(status_code=200, headers={}, iter_content=Mock(return_value=(payload,)))
        raise ValueError("Unfrozen release URL")

    client = PyPIReleaseClient(session=Mock(get=frozen_release))
    dependency = analysis.dependency
    old = client.get_release(dependency.package, dependency.old_version)
    proposed = client.get_release(dependency.package, dependency.proposed_version)
    require(isinstance(old, PackageReleaseEvidence) and isinstance(proposed, PackageReleaseEvidence), "Release inventory not established")
    candidate = build_artifact_serviceability_impact_candidate(fixture, dependency, old, proposed)
    require(isinstance(candidate, ArtifactServiceabilityImpactCandidate), "No publication candidate")
    return candidate


def controlled_blob(blob, *, manifest_changes=None, change_block=None):
    manifest, block = unpack(blob)
    if manifest_changes:
        manifest.update(manifest_changes)
    if change_block:
        block = change_block(block)
        manifest.update(tag_bytes=len(block), tag_sha256=sha256(block).hexdigest())
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("manifest.json", json.dumps(manifest))
        archive.writestr("pip-tags.txt", block)
    return buffer.getvalue()


def verify(directory, head):
    from packaging.tags import parse_tag

    from upgradepilot.impact.artifact_serviceability import (
        TargetWheelCompatibilityEvidence,
        evaluate_artifact_serviceability_impact,
    )

    run = json.loads((directory / "run.json").read_bytes())
    jobs = json.loads((directory / "jobs.json").read_bytes())
    artifacts = json.loads((directory / "artifacts.json").read_bytes())
    require(run["repository"]["full_name"] == REPOSITORY and run["head_sha"] == head
            and run["path"] == WORKFLOW and run["event"] == "workflow_dispatch"
            and run["run_attempt"] == 1 and run["conclusion"] == "success", "Unexpected workflow run")
    require(jobs["total_count"] == len(jobs["jobs"]) == 2, "Trial requires exactly two jobs")
    require(artifacts["total_count"] == len(artifacts["artifacts"]) == 2, "Trial requires exactly two artifacts")
    candidate = load_candidate(directory, head)
    baseline = evaluate_artifact_serviceability_impact(candidate).applicability.state
    require(baseline == "unresolved", "No-evidence baseline changed")
    rows = []
    raw_blobs = []
    for interpreter, (expected_state, proposed_match) in PYTHON_ROWS.items():
        job, = (job for job in jobs["jobs"] if job["name"] == f"Installer tags ({interpreter})")
        artifact, = (item for item in artifacts["artifacts"] if item["name"] == f"installer-tags-1-{interpreter}")
        archive = directory / f"{artifact['id']}.zip"
        require(archive.stat().st_size <= ARTIFACT_LIMIT, "Compressed artifact exceeds limit")
        blob = archive.read_bytes()
        raw_blobs.append((blob, artifact, job, interpreter))
        manifest, raw_tags, step = validate_artifact(blob, artifact, run, job, interpreter)
        tags = frozenset(tag for raw in raw_tags for tag in parse_tag(raw))
        source = (f"https://github.com/{REPOSITORY}/actions/runs/{run['id']}"
                  f"/job/{job['id']}#step:{step}:1")
        assessment = evaluate_artifact_serviceability_impact(
            candidate, TargetWheelCompatibilityEvidence(REPOSITORY, head, source, tags),
        )
        old_matches = [wheel.filename for wheel in candidate.old_wheels if tags & wheel.tags]
        proposed_matches = [wheel.filename for wheel in candidate.proposed_wheels if tags & wheel.tags]
        require(bool(old_matches) and bool(proposed_matches) == proposed_match, "Direct published-wheel intersection differed")
        require(assessment.applicability.state == expected_state, "Applicability evaluator disagreed")
        rows.append(dict(manifest=manifest, source=source, job_id=job["id"], step_number=step,
                         artifact_id=artifact["id"], archive_digest=artifact["digest"],
                         old_matches=old_matches, proposed_matches=proposed_matches, applicability=expected_state))

    blob, artifact, job, interpreter = raw_blobs[0]
    controls = (
        ("absent", None, "Missing artifact"),
        ("truncated", controlled_blob(blob, change_block=lambda block: b"\n".join(block.splitlines()[:-1])),
         "Incomplete or oversized tag block"),
        ("oversized", controlled_blob(blob, change_block=lambda block: block + b" " * ARTIFACT_LIMIT),
         "Expanded artifact exceeds limit"),
        ("wrong revision", controlled_blob(blob, manifest_changes={"checkout": FIXTURE_BASE}),
         "Artifact revision, attempt or job row mismatch"),
        ("wrong attempt", controlled_blob(blob, manifest_changes={"attempt": 2}),
         "Artifact revision, attempt or job row mismatch"),
        ("cross-job", raw_blobs[1][0], "Artifact revision, attempt or job row mismatch"),
    )
    for label, rejected, reason in controls:
        # Rebind each constructed control's byte digest so identity and completeness are tested directly.
        metadata = artifact if rejected is None else dict(artifact, digest="sha256:" + sha256(rejected).hexdigest())
        try:
            validate_artifact(rejected, metadata, run, job, interpreter)
        except ValueError as exc:
            require(str(exc) == reason, f"Unexpected {label} refusal: {exc}")
        else:
            raise ValueError(f"Accepted {label} control")

    return dict(controlled=True, repository=REPOSITORY, head=head, fixture_base=FIXTURE_BASE,
                run=run["id"], attempt=run["run_attempt"], baseline=baseline, rows=rows,
                refused_controls=[label for label, _, _ in controls])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("capture").add_argument("directory", type=Path)
    verifier = commands.add_parser("verify")
    verifier.add_argument("directory", type=Path)
    verifier.add_argument("head")
    arguments = parser.parse_args()
    if arguments.command == "capture":
        capture(arguments.directory)
    else:
        print(json.dumps(verify(arguments.directory, arguments.head), indent=2))


if __name__ == "__main__":
    main()
