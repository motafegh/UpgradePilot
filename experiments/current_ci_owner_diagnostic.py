"""Disposable FCI retained/fresh diagnostic; never a product replay interface.

CLI: prepare FREEZE; offline FREEZE OUTPUT PRIVATE; live FREEZE OUTPUT PRIVATE.
The two stage directories are exclusive: a failed official stage cannot be overwritten.
Frozen jobs are refused by the real parser before any explicitly conditional DTO projection.
Fresh observations use unmodified product clients and a byte-recording anonymous transport.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
from datetime import datetime, timezone
from types import SimpleNamespace
from urllib.parse import urlsplit

from requests.adapters import HTTPAdapter

from upgradepilot.ci.runtime_execution import assess_correlated_step_execution
from upgradepilot.ci.workflow_runtime_correlation import correlate_workflow_runtime
from upgradepilot.github.actions import GitHubActionsClient, WorkflowJob
from upgradepilot.github.api import GitHubAcquisitionError, GitHubResponseError
from upgradepilot.github.auth_session import GitHubPublicSession
from upgradepilot.github.pull_request import GitHubPullRequestClient
from upgradepilot.github.repository import GitHubRepositoryClient, RepositoryTextFile

ROOT = Path(__file__).resolve().parents[1]
COHORT = ROOT / "product-simulation/fresh-current-ci-diagnostic-2026-10-20"
CASES = ("FCI001-openai-agents-mcp", "FCI002-mdformat-footnote-tox", "FCI003-pasarguard-fastapi")
PLAN = ROOT / "plans/CURRENT_CI_RETAINED_INPUT_ADMISSION_AND_OWNER_DIAGNOSTIC_PLAN.md"
MIB = 1024 * 1024
SAFE_HEADERS = {"date", "content-type", "etag", "x-github-request-id", "x-ratelimit-limit",
                "x-ratelimit-remaining", "x-ratelimit-reset", "x-ratelimit-used", "retry-after"}
PREMISE = "derived scope premise, not a provider job-head observation"


def utc():
    return datetime.now(timezone.utc).isoformat()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load(path):
    return json.loads(path.read_text())


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def fingerprints():
    paths = [PLAN, Path(__file__), ROOT / "experiments/tests/test_current_ci_owner_diagnostic.py",
             COHORT / "verify_bundle.py"]
    paths.extend((ROOT / "src/upgradepilot").rglob("*.py"))
    for name in CASES:
        case = COHORT / "cases" / name
        paths.append(case / "manifest.json")
        paths.extend(case / row["path"] for row in load(case / "manifest.json")["artifacts"])
    return {str(path.relative_to(ROOT)): digest(path.read_bytes()) for path in sorted(set(paths))}


def check_freeze(freeze):
    if load(freeze)["files"] != fingerprints():
        raise ValueError("Frozen input/executable/contract identity changed; no stage dispatched")


def case_inputs(name):
    directory = COHORT / "cases" / name
    manifest = load(directory / "manifest.json")
    provider_path = directory / "raw/provider-capture.json"
    if not provider_path.exists():
        provider_path = directory / "raw/provider-meta.json"
    provider = load(provider_path)
    jobs_path = provider_path if "jobs" in provider else directory / "raw/jobs-attempt-1.json"
    jobs = provider["jobs"] if "jobs" in provider else load(jobs_path)["jobs"]
    return directory, manifest, provider_path, provider, jobs_path, jobs


def joined_run(provider):
    """Join only the missing workflow ID; refuse ambiguous or conflicting retained identity."""
    selected = dict(provider["selected_run"])
    candidates = [row for row in provider["exact_head_runs"] if row["id"] == selected["id"]]
    if len(candidates) != 1:
        raise ValueError("Selected run has no unique retained run-list join")
    for field in ("workflow_id", "name", "status", "conclusion"):
        if field in selected and selected[field] != candidates[0][field]:
            raise ValueError(f"Conflicting selected/run-list field: {field}")
    selected["workflow_id"] = candidates[0]["workflow_id"]
    return selected, provider["exact_head_runs"].index(candidates[0])


def owner_result(source, run, jobs):
    result = correlate_workflow_runtime(source, run, jobs)
    steps = []
    for job in result.jobs:
        for match in job.steps:
            assessment = assess_correlated_step_execution(match)
            steps.append({"job_key": job.static_job.key, "job_id": job.runtime_job.job_id,
                          "static_step_index": match.static_step.source_index,
                          "runtime_step_number": match.runtime_step.number,
                          "runtime_name": match.runtime_step.name,
                          "runtime_status": match.runtime_step.status,
                          "runtime_conclusion": match.runtime_step.conclusion,
                          "state": assessment.state, "basis": assessment.basis,
                          "reason": assessment.reason})
    return {"state": result.state, "reason": result.reason, "detail": result.detail,
            "matched_jobs": len(result.jobs), "step_execution": steps}


def step_shape(job):
    if "steps" not in job:
        return "absent"
    if job["steps"] is None:
        return "null"
    return "empty_array" if job["steps"] == [] else "non_empty_array"


def retained_case(name):
    directory, manifest, provider_path, provider, jobs_path, raw_jobs = case_inputs(name)
    data, index = joined_run(provider)
    # Minimal parser context, not a fabricated full PR or public replay claim.
    context = SimpleNamespace(head_sha=manifest["identity"]["head_sha"])
    run = GitHubActionsClient._parse_workflow_run(context, data)
    ledger, projected = [], []
    for index_job, raw in enumerate(raw_jobs):
        pointer = f"/jobs/{index_job}"
        row = {"job_id": raw.get("id"), "source": str(jobs_path.relative_to(ROOT)),
               "source_sha256": digest(jobs_path.read_bytes()), "pointer": pointer,
               "observed": {key: raw[key] for key in ("id", "run_id", "name", "head_sha", "status", "conclusion") if key in raw},
               "missing": [key for key in ("id", "run_id", "name", "head_sha", "status", "conclusion") if key not in raw],
               "steps_shape": step_shape(raw), "steps_count": len(raw["steps"]) if isinstance(raw.get("steps"), list) else None}
        try:
            parsed = GitHubActionsClient._parse_workflow_job(context, run, raw)
            row["strict"] = {"state": "admitted"}
        except GitHubResponseError as exc:
            parsed = None
            row["strict"] = {"state": "refused", "detail": str(exc)}
        # Only head_sha may be projected; all other fields/step validation stay owner-owned.
        if parsed is None and row["missing"] == ["head_sha"]:
            steps = raw.get("steps")
            parsed = WorkflowJob(job_id=raw["id"], run_id=raw["run_id"], name=raw["name"],
                                 head_sha=run.head_sha, status=raw["status"], conclusion=raw["conclusion"],
                                 steps=None if steps is None else tuple(GitHubActionsClient._parse_workflow_step(step) for step in steps))
            # Validate all available job fields and relationships using the real parser.
            # This temporary validation copy is never published as provider JSON or replay.
            checked = GitHubActionsClient._parse_workflow_job(context, run, {**raw, "head_sha": run.head_sha})
            if parsed != checked:
                raise ValueError("Conditional DTO disagrees with available-field parser validation")
            row["conditional_head_scope"] = {"value": run.head_sha, "label": PREMISE,
                                              "source": "selected_run.head_sha", "provider_observation": False}
        if parsed is None:
            raise ValueError("Conditional mapping requires more than the authorized head premise")
        projected.append(parsed)
        ledger.append(row)
    source_path = directory / manifest["authoritative_workflow_source_artifact"]
    source = RepositoryTextFile(repository=manifest["identity"]["repository"],
                                path=manifest["selected_workflow"]["workflow_path"],
                                revision=run.head_sha, content=source_path.read_text())
    return {"case_id": manifest["case_id"], "state": "completed", "track": "retained",
            "strict_admission": "admitted" if all(row["strict"]["state"] == "admitted" for row in ledger) else "input_unavailable",
            "run_parser": "admitted_with_minimal_saved_head_context",
            "run_workflow_id_join": {"source": str(provider_path.relative_to(ROOT)),
                                     "selected_pointer": "/selected_run", "join_pointer": f"/exact_head_runs/{index}/workflow_id"},
            "transport_limit": "Reduced structured capture; no complete pagination/attempt-response envelope",
            "jobs": ledger, "conditional_label": PREMISE,
            "conditional_owner": owner_result(source, run, projected)}


class DiagnosticLimit(RuntimeError):
    """An experiment limit, never a product evidence classification."""


class RecordingAdapter(HTTPAdapter):
    """Retain decoded entity bytes before the product consumes each HTTP response.

    Adapter.send is the actual-send seam, including redirects. No retries are installed.
    Bodies stay private; receipts contain only selected transport metadata and hashes.
    """

    def __init__(self, private, public, repository, request_left=12, body_left=8 * MIB):
        super().__init__(max_retries=0)
        self.private, self.public, self.repository = private, public, repository
        self.request_cap = min(12, request_left)
        self.body_left = body_left
        self.count = 0
        self.body_bytes = 0
        self.receipts = []

    def send(self, request, **kwargs):
        parsed = urlsplit(request.url)
        if (request.method != "GET" or parsed.scheme != "https" or parsed.netloc != "api.github.com"
                or not parsed.path.startswith(f"/repos/{self.repository}/")
                or any(header in request.headers for header in ("Authorization", "Cookie"))):
            raise DiagnosticLimit("Transport escaped anonymous selected-repository GET scope")
        if self.count >= self.request_cap:
            raise DiagnosticLimit("Attempted GET ceiling exhausted")
        self.count += 1
        receipt = {"sequence": self.count, "url": request.url, "method": request.method,
                   "utc_start": utc(), "monotonic_start": time.monotonic(), "state": "send_started"}
        self.receipts.append(receipt)
        self.persist()
        response = None
        try:
            response = super().send(request, **kwargs)
            receipt.update(status=response.status_code,
                           headers={key.lower(): value for key, value in response.headers.items() if key.lower() in SAFE_HEADERS})
            chunks, size = [], 0
            for chunk in response.iter_content(chunk_size=65536):
                size += len(chunk)
                if size > 2 * MIB or self.body_bytes + size > self.body_left:
                    receipt.update(state="body_limit", decoded_bytes_seen=size,
                                   retained_body=False)
                    raise DiagnosticLimit("Decoded body retention ceiling exceeded; body omitted")
                chunks.append(chunk)
            body = b"".join(chunks)
            self.private.mkdir(parents=True, exist_ok=True, mode=0o700)
            body_path = self.private / f"response-{self.count:02d}.body"
            with body_path.open("xb") as output:
                os.chmod(body_path, 0o600)
                output.write(body)
            self.body_bytes += len(body)
            receipt.update(state="response_retained", decoded_bytes=len(body), sha256=digest(body),
                           private_body=body_path.name, retained_body=True)
            response._content = body
            response._content_consumed = True
            return response
        except Exception as exc:
            receipt.update(error_class=type(exc).__name__)
            if receipt["state"] == "send_started":
                receipt["state"] = "transport_failure"
            raise
        finally:
            if response is not None:
                response.close()
            receipt.update(utc_receipt=utc(), elapsed_seconds=time.monotonic() - receipt["monotonic_start"])
            self.persist()

    def persist(self):
        write(self.public / "receipts.json", self.receipts)


def fresh_case(name, session, preserve=None):
    """Use normal selected-CI acquisition; preserve partial progress before each next read."""
    directory, manifest, _, _, _, _ = case_inputs(name)
    identity, selected = manifest["identity"], manifest["selected_workflow"]
    pr_client = GitHubPullRequestClient(session=session)
    actions = GitHubActionsClient(session=session)
    repository = GitHubRepositoryClient(session=session)
    row = {"case_id": manifest["case_id"], "track": "separately_fresh", "state": "acquiring"}
    def checkpoint():
        if preserve is not None:
            preserve(row)
    pr = pr_client.get_pull_request(identity["repository"], identity["pr_number"])
    row["initial_pr"] = {key: getattr(pr, key) for key in ("base_sha", "head_sha", "changed_files", "state")}
    checkpoint()
    if (pr.base_sha, pr.head_sha) != (identity["base_sha"], identity["head_sha"]):
        return {**row, "state": "target_drift"}
    runs = actions.get_exact_head_workflow_runs(pr)
    matching = [run for run in runs if run.run_id == selected["run_id"]]
    row["exact_head_run_ids"] = [run.run_id for run in runs]
    if len(matching) != 1:
        return {**row, "state": "selected_run_unavailable"}
    run = matching[0]
    row["selected_run"] = vars_dto(run)
    checkpoint()
    if run.run_attempt != selected["run_attempt"]:
        return {**row, "state": "attempt_drift"}
    jobs = actions.get_workflow_jobs(pr, run)
    row["jobs"] = [vars_dto(job) for job in jobs]
    checkpoint()
    source = repository.get_exact_head_workflow_file(pr, run)
    if not isinstance(source, RepositoryTextFile):
        return {**row, "state": "source_unavailable", "source": vars_dto(source)}
    expected_source = directory / manifest["authoritative_workflow_source_artifact"]
    row["workflow"] = {"path": source.path, "revision": source.revision,
                       "sha256": digest(source.content.encode()), "frozen_sha256": digest(expected_source.read_bytes())}
    checkpoint()
    final = pr_client.get_pull_request(identity["repository"], identity["pr_number"])
    row["final_pr"] = {key: getattr(final, key) for key in ("base_sha", "head_sha", "changed_files", "state")}
    if (pr.base_sha, pr.head_sha, pr.changed_files) != (final.base_sha, final.head_sha, final.changed_files):
        return {**row, "state": "target_drift_after_acquisition"}
    if source.path != selected["workflow_path"] or row["workflow"]["sha256"] != row["workflow"]["frozen_sha256"]:
        return {**row, "state": "source_binding_discrepancy"}
    row.update(state="completed", owner=owner_result(source, run, jobs),
               job_heads="observed_and_validated_by_normal_product_client",
               claim_limit="Selected CI acquisition/correlation only; no dependency state, semantic usefulness or action authority")
    return row


def vars_dto(value):
    from dataclasses import asdict
    return asdict(value)


def block_offline(event, args):
    if event.startswith("socket.") or event in ("subprocess.Popen", "os.system", "os.posix_spawn"):
        raise DiagnosticLimit("Offline worker attempted network/process access")


def alarm_expired(signum, frame):
    raise DiagnosticLimit("Monotonic-enforced worker deadline alarm")


def run_worker(stage, freeze, output, private, name, request_left, body_left):
    start = time.monotonic()
    row = {"case_id": name[:6], "state": "worker_started", "utc_start": utc()}
    write(output / "result.json", row)
    signal.signal(signal.SIGALRM, alarm_expired)
    signal.setitimer(signal.ITIMER_REAL, 30 if stage == "offline" else 90)
    adapter = None
    try:
        check_freeze(freeze)
        if stage == "offline":
            sys.addaudithook(block_offline)
            row.update(retained_case(name))
        else:
            session = GitHubPublicSession()
            adapter = RecordingAdapter(private, output, case_inputs(name)[1]["identity"]["repository"], request_left, body_left)
            # Mount on all schemes so redirects cannot escape the guard.
            session.mount("https://", adapter)
            session.mount("http://", adapter)
            def preserve(partial):
                row.update(partial)
                write(output / "result.json", row)
            row.update(fresh_case(name, session, preserve))
    except GitHubAcquisitionError as exc:
        row.update(state="acquisition_unavailable", reason=exc.reason, status_code=exc.status_code)
    except GitHubResponseError as exc:
        row.update(state="product_response_refusal", detail=str(exc))
    except Exception as exc:
        row.update(state="diagnostic_failure", error_class=type(exc).__name__, detail=str(exc))
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        row.update(elapsed_seconds=time.monotonic() - start, utc_end=utc())
        if adapter:
            row.update(attempted_gets=adapter.count, retained_body_bytes=adapter.body_bytes)
        write(output / "result.json", row)


def dispatch(command, result_path, timeout):
    """External watchdog preserves partial worker records and never retries."""
    try:
        result = subprocess.run(command, cwd=ROOT, timeout=timeout, capture_output=True, text=True)
        if result.returncode:
            row = load(result_path) if result_path.exists() else {}
            row.update(state="worker_process_failure", returncode=result.returncode,
                       stderr=result.stderr[:2000])
            write(result_path, row)
    except subprocess.TimeoutExpired:
        row = load(result_path) if result_path.exists() else {}
        row.update(state="watchdog_cancelled", timeout_seconds=timeout,
                   cancellation="subprocess.run killed and waited for worker")
        write(result_path, row)


def evidence_bytes(paths):
    return sum(path.stat().st_size for root in paths if root.exists() for path in root.rglob("*") if path.is_file())


def run_stage(stage, freeze, output, private, entered):
    check_freeze(freeze)
    if private.resolve().is_relative_to(ROOT):
        raise ValueError("Raw response bodies must remain outside the Git workspace")
    if output.exists() or private.exists():
        raise ValueError("Exclusive stage output/private directory already exists; no rerun")
    output.mkdir(parents=True)
    private.mkdir(parents=True, mode=0o700)
    rows, sends, bodies = [], 0, 0
    quota_blocked = False
    case_total = 0.0
    for name in CASES:
        remaining = (180 if stage == "offline" else 300) - (time.monotonic() - entered) - 3
        aggregate_left = (90 if stage == "offline" else 270) - case_total
        row_path = output / name[:6] / "result.json"
        if remaining <= 0 or aggregate_left <= 0 or quota_blocked:
            row = {"case_id": name[:6], "state": "unattempted", "reason": "quota_or_deadline"}
            write(row_path, row)
        else:
            started = time.monotonic()
            command = [sys.executable, str(Path(__file__)), "worker", str(freeze), str(row_path.parent),
                       str(private / name[:6]), "--stage", stage, "--case", name,
                       "--request-left", str(36 - sends), "--body-left", str(8 * MIB - bodies)]
            dispatch(command, row_path, min(30 if stage == "offline" else 90, remaining, aggregate_left))
            case_total += time.monotonic() - started
            row = load(row_path)
            # Receipts survive parent watchdog cancellation before the worker's final write.
            receipts_path = row_path.parent / "receipts.json"
            receipts = load(receipts_path) if receipts_path.exists() else []
            sends += len(receipts)
            bodies += sum(receipt.get("decoded_bytes", 0) for receipt in receipts)
            quota_blocked = any(receipt.get("status") in (403, 429) for receipt in receipts)
        rows.append({"case_id": name[:6], "state": row["state"], "result_sha256": digest(row_path.read_bytes())})
        write(output / "progress.json", {"stage": stage, "rows": rows, "attempted_gets": sends,
                                         "retained_body_bytes": bodies, "elapsed_seconds": time.monotonic() - entered})
    if evidence_bytes([freeze.parent, private.parent]) > 15 * MIB:
        raise DiagnosticLimit("Total public/private evidence exceeds contract; preserve and stop")
    check_freeze(freeze)
    write(output / "summary.json", {"stage": stage, "utc_end": utc(), "rows": rows,
                                   "requested_cases": 3, "attempted_gets": sends,
                                   "retained_body_bytes": bodies, "case_wall_seconds": case_total,
                                   "whole_elapsed_seconds": time.monotonic() - entered,
                                   "unchanged_frozen_inputs": True})


def main():
    entered = time.monotonic()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("prepare", "offline", "live", "worker"))
    parser.add_argument("freeze", type=Path)
    parser.add_argument("output", type=Path, nargs="?")
    parser.add_argument("private", type=Path, nargs="?")
    parser.add_argument("--stage", choices=("offline", "live"))
    parser.add_argument("--case", choices=CASES)
    parser.add_argument("--request-left", type=int, default=12)
    parser.add_argument("--body-left", type=int, default=8 * MIB)
    args = parser.parse_args()
    if args.command == "prepare":
        if args.freeze.exists():
            raise ValueError("Freeze already exists")
        write(args.freeze, {"utc_frozen": utc(), "files": fingerprints(), "cases": CASES,
                            "contract": str(PLAN.relative_to(ROOT)), "official_batches": "one retained then one separately fresh",
                            "recovery": "No original job-head observation location identified in manifests/construction records; no home/session scan or synthetic recovery",
                            "reviewer_overlap": "Same source-aware implementer/reviewer; exposed development cases, no independent evaluation"})
    elif args.command == "worker":
        run_worker(args.stage, args.freeze, args.output, args.private, args.case, args.request_left, args.body_left)
    else:
        if args.command == "live" and not (args.output.parent / "offline/summary.json").exists():
            raise ValueError("Retained stage must be preserved before fresh stage")
        run_stage(args.command, args.freeze, args.output, args.private, entered)


if __name__ == "__main__":
    main()
