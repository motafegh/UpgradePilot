#!/usr/bin/env python3
"""Offline integrity and identity verifier for the exposed FCI cohort.

This script performs no network access. Run it from the cohort root or pass the
cohort root as argv[1]. It verifies retained bytes, manifest hashes/Git blob
identities, and the frozen PR/run/job relationships encoded in retained JSON.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()  # noqa: S324 - Git object identity


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def provider_capture(case_dir: Path) -> dict:
    for name in ("provider-capture.json", "provider-meta.json"):
        candidate = case_dir / "raw" / name
        if candidate.exists():
            return load_json(candidate)
    raise AssertionError(f"{case_dir.name}: provider capture missing")


def jobs_capture(case_dir: Path, provider: dict) -> list[dict]:
    if isinstance(provider.get("jobs"), list):
        return provider["jobs"]
    path = case_dir / "raw" / "jobs-attempt-1.json"
    require(path.exists(), f"{case_dir.name}: run-attempt jobs capture missing")
    payload = load_json(path)
    require(isinstance(payload.get("jobs"), list), f"{case_dir.name}: jobs payload malformed")
    return payload["jobs"]


def classify_steps(job: dict) -> str:
    steps = job.get("steps")
    if steps is None:
        return "field_absent_or_unavailable"
    if steps == []:
        return "empty_array"
    require(isinstance(steps, list), f"job {job.get('id')}: steps must be list/null")
    return "non_empty_array"


def verify_case(case_dir: Path) -> dict:
    manifest = load_json(case_dir / "manifest.json")
    case_id = manifest["case_id"]
    identity = manifest["identity"]
    selected = manifest["selected_workflow"]

    artifacts_by_path: dict[str, dict] = {}
    for artifact in manifest["artifacts"]:
        rel = artifact["path"]
        require(rel not in artifacts_by_path, f"{case_id}: duplicate artifact path {rel}")
        artifacts_by_path[rel] = artifact
        path = case_dir / rel
        require(path.is_file(), f"{case_id}: missing retained artifact {rel}")
        data = path.read_bytes()
        require(len(data) == artifact["byte_size"], f"{case_id}:{rel}: byte-size mismatch")
        require(sha256(data) == artifact["sha256"], f"{case_id}:{rel}: SHA-256 mismatch")
        expected_git = artifact.get("git_blob_sha1")
        if expected_git is not None:
            require(git_blob_sha1(data) == expected_git, f"{case_id}:{rel}: Git blob identity mismatch")
        require(artifact.get("observation_time"), f"{case_id}:{rel}: observation time missing")
        require(artifact.get("retrieval_identity"), f"{case_id}:{rel}: retrieval identity missing")
        require(artifact.get("target_revision"), f"{case_id}:{rel}: target revision missing")

    authoritative = manifest["authoritative_dependency_transition_artifact"]
    require(authoritative in artifacts_by_path, f"{case_id}: authoritative transition artifact absent")
    require(
        artifacts_by_path[authoritative].get("role") == "authoritative_provider_exact_diff",
        f"{case_id}: authoritative transition artifact is not provider-exact",
    )

    provider = provider_capture(case_dir)
    pr = provider["pr"]
    require(pr["number"] == identity["pr_number"], f"{case_id}: PR number mismatch")
    require(pr["base_sha"] == identity["base_sha"], f"{case_id}: base SHA mismatch")
    require(pr["head_sha"] == identity["head_sha"], f"{case_id}: head SHA mismatch")

    run = provider["selected_run"]
    require(run["id"] == selected["run_id"], f"{case_id}: selected run ID mismatch")
    require(run["run_attempt"] == selected["run_attempt"], f"{case_id}: run-attempt mismatch")
    require(run["head_sha"] == identity["head_sha"], f"{case_id}: run head is not frozen PR head")
    require(run["path"] == selected["workflow_path"], f"{case_id}: workflow path mismatch")

    binding = run.get("pull_request_binding")
    if binding is not None:
        require(binding["number"] == identity["pr_number"], f"{case_id}: run PR binding mismatch")
        require(binding["base_sha"] == identity["base_sha"], f"{case_id}: run base binding mismatch")
        require(binding["head_sha"] == identity["head_sha"], f"{case_id}: run head binding mismatch")

    jobs = jobs_capture(case_dir, provider)
    require(jobs, f"{case_id}: no jobs retained")
    require(all(job["run_id"] == selected["run_id"] for job in jobs), f"{case_id}: cross-run job mixed in")
    states = [classify_steps(job) for job in jobs]
    require("empty_array" not in states, f"{case_id}: unexpected empty step array")

    if case_id == "FCI001":
        require(states == ["non_empty_array"], "FCI001: expected one non-empty step array")
        require(selected["static_correlation_eligibility"] == "eligible_for_current_owner", "FCI001: eligibility drift")
    elif case_id == "FCI002":
        require("non_empty_array" in states, "FCI002: executed jobs lost runtime steps")
        require("field_absent_or_unavailable" in states, "FCI002: skipped-job unavailable step state lost")
        require(selected["static_correlation_eligibility"] == "intentionally_unsupported_matrix", "FCI002: matrix boundary drift")
    elif case_id == "FCI003":
        require(all(state == "non_empty_array" for state in states), "FCI003: expected all job steps non-empty")
        require(
            selected["static_correlation_eligibility"] == "intentionally_unsupported_static_job_name_missing",
            "FCI003: static-name boundary drift",
        )
    else:
        raise AssertionError(f"unexpected case id {case_id}")

    return {
        "case_id": case_id,
        "artifact_count": len(artifacts_by_path),
        "job_count": len(jobs),
        "step_states": sorted(set(states)),
        "qualification": manifest["qualification"],
    }


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent
    cases_root = root / "cases"
    require(cases_root.is_dir(), f"cases directory missing under {root}")
    case_dirs = sorted(path for path in cases_root.iterdir() if path.is_dir() and path.name.startswith("FCI"))
    require([p.name[:6] for p in case_dirs] == ["FCI001", "FCI002", "FCI003"], "unexpected admitted case set")

    results = [verify_case(case_dir) for case_dir in case_dirs]
    print(json.dumps({"status": "pass", "network_required": False, "cases": results}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
