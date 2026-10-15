"""Qualify explicit frozen development cases against native product owners, without models.

Usage: PYTHONPATH=src .venv/bin/python3 tools/prepare_investigator_inputs.py
       --corpus <retained research corpus> --targets <explicit PR locator mapping>
       --output <new owner-only directory outside Git>

The legacy corpus is input data, never imported experiment code. This diagnostic bridges
its source/capture fields into product-owned source types, obtains exact missing public
native inputs through existing providers, and emits a NEW common freeze for both arms.
Current API evidence remains retrospective/acquisition-time evidence; historical illustrative
CI stays raw. Failures are retained and do not qualify a raw-only substitute as native proof.
"""

from __future__ import annotations

import argparse
import json
import sys
from contextlib import contextmanager
from dataclasses import asdict
from datetime import UTC, datetime
from hashlib import sha256
from pathlib import Path

from upgradepilot.ci.dependency_exercise import evaluate_dependency_ci_coverage
from upgradepilot.ci.dependency_state import evaluate_runtime_dependency_state
from upgradepilot.dependency.analysis import analyze_dependency_change
from upgradepilot.github.actions import GitHubActionsClient
from upgradepilot.github.auth_session import GitHubPublicSession
from upgradepilot.github.pull_request import GitHubPullRequestClient
from upgradepilot.github.repository import GitHubRepositoryClient, RepositoryTextFile
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.consumer_access import WorkspaceEvidenceAccess
from upgradepilot.workspace.lifecycle_host import InvestigationWorkspaceHost
from upgradepilot.workspace.lifecycle_records import DiscoveryObjective
from upgradepilot.workspace.native_projection import reconstruct_ci_projection
from upgradepilot.workspace.native_representation import parse_json
from upgradepilot.workspace.preparation import prepare_dependency_ci_workspace
from upgradepilot.workspace.source_access import (
    RetainedSourceCatalog,
    RetainedSourceFile,
    RetainedSourceScope,
    encode_source_catalog,
    read_source_catalog,
    read_source_delivery,
)


@contextmanager
def _measure_native_calls():
    """Count actual owner entries in this synchronous diagnostic, without replacing them."""
    owners = {
        function.__code__: function.__name__
        for function in (
            analyze_dependency_change,
            evaluate_dependency_ci_coverage,
            evaluate_runtime_dependency_state,
        )
    }
    counts = dict.fromkeys(owners.values(), 0)
    previous = sys.getprofile()

    def count(frame, event, arg):
        if event == "call" and frame.f_code in owners:
            counts[owners[frame.f_code]] += 1
        if previous is not None:
            previous(frame, event, arg)

    sys.setprofile(count)
    try:
        yield counts
    finally:
        sys.setprofile(previous)


def _read_legacy_corpus(path):
    """Convert bounded legacy source/acquisition inventory, not canonical native JSON.

    Its acquisition manifests are wider than native records. This conversion-only owner
    admits at most 64 MiB, depth 64 and one million structural punctuation tokens before
    allocation. Native codec/store limits remain unchanged; exported product input must
    independently pass those limits. Duplicate/non-finite JSON is refused.
    """
    payload = path.read_bytes()
    if len(payload) > 64 * 1024 * 1024:
        raise ValueError("Legacy corpus byte capacity exceeded.")
    depth = tokens = 0
    quoted = escaped = False
    for byte in payload:
        if quoted:
            if escaped:
                escaped = False
            elif byte == 92:
                escaped = True
            elif byte == 34:
                quoted = False
            continue
        if byte == 34:
            quoted = True
        elif byte in (123, 91):
            depth += 1
            if depth > 64:
                raise ValueError("Legacy corpus depth capacity exceeded.")
        elif byte in (125, 93):
            depth -= 1
        if byte in (123, 91, 125, 93, 44, 58):
            tokens += 1
            if tokens > 1_000_000:
                raise ValueError("Legacy corpus width capacity exceeded.")

    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError("Duplicate legacy corpus field.")
            result[key] = value
        return result

    def reject_constant(value):
        raise ValueError("Non-finite legacy corpus value.")

    return json.loads(
        payload.decode("utf-8"), object_pairs_hook=pairs, parse_constant=reject_constant
    )


class RecordedPublicSession(GitHubPublicSession):
    def __init__(self):
        super().__init__()
        self.receipts = []

    def request(self, method, url, **kwargs):
        if method.upper() != "GET":
            raise ValueError("Preparation only admits public reads.")
        started = datetime.now(UTC).isoformat()
        try:
            response = super().request(method, url, **kwargs)
        except Exception as error:
            self.receipts.append(
                {
                    "url": url,
                    "started": started,
                    "outcome": "problem",
                    "problem": type(error).__name__,
                }
            )
            raise
        self.receipts.append(
            {
                "url": response.url,
                "started": started,
                "completed": datetime.now(UTC).isoformat(),
                "status": response.status_code,
                "body": response.text,
                "authority": "Anonymous public API body at acquisition time; no original decision-time availability or historical completeness promise.",
            }
        )
        return response


class RecordedRepository(GitHubRepositoryClient):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.files = []

    def _get_exact_repository_text_file(self, repository, path, *, revision):
        result = super()._get_exact_repository_text_file(
            repository, path, revision=revision
        )
        if isinstance(result, RepositoryTextFile):
            self.files.append(result)
        return result


def _legacy_catalog(case, prepared, session, repository):
    # Preserve the old source identities before constructing a different, product-owned
    # profile. This establishes correspondence only; original capture strength stays explicit.
    descriptors = []
    for document in case["documents"]:
        descriptors.append(
            {
                "source_id": document["source_id"],
                "path": document["path"],
                "identity": document["identity"],
                "sha256": sha256(document["text"].encode()).hexdigest(),
                "lines": len(document["text"].splitlines()),
            }
        )
    original_id = sha256(
        json.dumps(
            {"sources": case["sources"], "documents": descriptors},
            sort_keys=True,
            ensure_ascii=False,
            allow_nan=False,
        ).encode()
    ).hexdigest()
    if original_id != case["corpus_sha256"]:
        raise ValueError("Original retained source identity does not match its freeze.")
    scopes = []
    for source in case["sources"]:
        members = [
            d for d in case["documents"] if d["source_id"] == source["source_id"]
        ]
        if any(
            d["identity"]["repository"] != source["repository"]
            or d["identity"]["revision"] != source["revision"]
            or d["identity"]["path"] != d["path"]
            for d in members
        ):
            raise ValueError("Retained document identity differs from declared source.")
        if len(members) != source["file_count"]:
            raise ValueError("Source inventory count differs from retained content.")
        scopes.append(
            RetainedSourceScope(
                source["source_id"],
                source["repository"],
                source["revision"],
                "captured_observation"
                if source["source_id"] == "ci-observations"
                else "repository_text",
                json.dumps(sorted({d["identity"]["basis"] for d in members})),
                json.dumps(source, sort_keys=True),
            )
        )
    files = [
        RetainedSourceFile(
            d["source_id"],
            d["path"],
            d["text"],
            json.dumps(d["identity"], sort_keys=True),
        )
        for d in case["documents"]
    ]
    # Exact source reads by the normal native owners remain raw-accessible to both arms.
    for index, file in enumerate(repository.files):
        identifier = f"prepared-file-{index}"
        scopes.append(
            RetainedSourceScope(
                identifier,
                file.repository,
                file.revision,
                "repository_text",
                "Native exact repository-file provider; acquisition time/mode is retained in preparation-observations.",
                "Only the exact supplied file; no runtime or package origin claim.",
            )
        )
        files.append(
            RetainedSourceFile(
                identifier,
                file.path,
                file.content,
                json.dumps(
                    {
                        "producer": "GitHubRepositoryClient",
                        "revision": file.revision,
                        "acquisition": "See bound preparation-observations receipts.",
                    }
                ),
            )
        )
    target = prepared.host.current.boundary.target
    scopes.append(
        RetainedSourceScope(
            "preparation-observations",
            target.repository,
            target.head_sha,
            "captured_observation",
            "Actual anonymous public API receipts from native preparation.",
            "Only these responses at recorded acquisition times; expired history/logs remain unknown.",
        )
    )
    for index, receipt in enumerate(session.receipts):
        files.append(
            RetainedSourceFile(
                "preparation-observations",
                f"request-{index}.json",
                json.dumps(receipt, indent=2),
                json.dumps(
                    {
                        "producer": "existing GitHub provider",
                        "acquisition_time": receipt["started"],
                        "url": receipt["url"],
                    }
                ),
            )
        )
    return RetainedSourceCatalog(tuple(scopes), tuple(files), target=target)


def run(corpus_path: Path, targets_path: Path, output: Path) -> dict:
    root = Path(__file__).resolve().parents[1]
    if output.resolve().is_relative_to(root):
        raise ValueError("Checkpoint/raw preparation output must stay outside Git.")
    if (
        corpus_path.stat().st_size > 64 * 1024 * 1024
        or targets_path.stat().st_size > 64 * 1024
    ):
        raise ValueError("Preparation input capacity exceeded.")
    corpus = _read_legacy_corpus(corpus_path)
    targets = parse_json(targets_path.read_bytes())
    if type(targets) is not list or not 1 <= len(targets) <= 20:
        raise ValueError("Require explicit bounded PR target mapping.")
    output.mkdir(mode=0o700, parents=False, exist_ok=False)
    manifest = {
        "format": "common-investigator-preparation/1",
        "created": datetime.now(UTC).isoformat(),
        "original_source_file_sha256": sha256(corpus_path.read_bytes()).hexdigest(),
        "product_source_sha256": {
            str(path.relative_to(root)): sha256(path.read_bytes()).hexdigest()
            for path in sorted((root / "src/upgradepilot").rglob("*.py"))
        },
        "scope": "Exposed development cases; new common preparation, no inference or semantic/usefulness acceptance.",
        "cases": [],
    }
    cases = {case["task"]["case_id"]: case for case in corpus["cases"]}
    for index, target in enumerate(targets):
        case = cases[target["case_id"]]
        task = case["task"]
        if (target["repository"], target["base"], target["head"]) != (
            task["repository"],
            task["base"],
            task["head"],
        ):
            raise ValueError("Target mapping differs from the original frozen case.")
        directory = output / f"case-{index + 1}"
        directory.mkdir(mode=0o700)
        session = RecordedPublicSession()
        repository = RecordedRepository(session=session)
        summary = {
            "case_id": target["case_id"],
            "repository": target["repository"],
            "pull_number": target["pull_number"],
            "base": target["base"],
            "head": target["head"],
        }
        try:
            store = CheckpointStore.create(directory / "checkpoint", schema_version=2)
            host = InvestigationWorkspaceHost(store=store)
            with _measure_native_calls() as counts:
                prepared = prepare_dependency_ci_workspace(
                    target["repository"],
                    target["pull_number"],
                    expected_base=target["base"],
                    expected_head=target["head"],
                    pull_client=GitHubPullRequestClient(session=session),
                    actions_client=GitHubActionsClient(session=session),
                    repository_client=repository,
                    host=host,
                )
            summary["native_owner_invocations"] = counts
            dependency = prepared.inputs.dependency
            if not prepared.ci or (
                dependency.normalized_package,
                dependency.old_version,
                dependency.proposed_version,
            ) != (task["dependency"].lower(), task["old"], task["proposed"]):
                raise ValueError(
                    "Native dependency transition does not qualify the selected comparison."
                )
            catalog = _legacy_catalog(case, prepared, session, repository)
            profile = encode_source_catalog(catalog)
            (directory / "common-sources.json").write_bytes(profile)
            if (
                read_source_catalog(
                    profile, expected_target=host.current.boundary.target
                ).identity
                != catalog.identity
            ):
                raise ValueError("Source profile cold correspondence failure.")
            access = WorkspaceEvidenceAccess(host, catalog)
            host.configure(authority=None, capabilities=(), methods=(access.method,))
            basis = next(
                r.record_id
                for r in host.current.boundary.records
                if r.family == "investigation_inputs"
            )
            purpose = host.add_purpose(
                DiscoveryObjective(
                    "Investigate this dependency update using the common frozen evidence.",
                    access.scope,
                    "Discover update-relevant evidence and uncertainty.",
                    "Only this qualified capture; no preselected candidate or sufficiency claim.",
                ),
                native_record_ids=(basis,),
            )
            # Source queries are generic qualification controls, not case-answer selectors.
            deliveries = [
                access.source_view(purpose, "list_sources", {}),
                access.source_view(
                    purpose, "search", {"query": dependency.normalized_package}
                ),
                access.native_view(
                    purpose,
                    ("investigation_inputs", "ci_coverage", "runtime_dependency_state"),
                ),
            ]
            first = next(file for file in catalog.files if file.content.splitlines())
            passage = access.source_view(
                purpose,
                "read",
                {"source_id": first.source_id, "path": first.path, "line_count": 1},
            )
            reference = read_source_delivery(
                host.lifecycle_value(passage).retained_content.encode()
            )["payload"]["reference"]
            deliveries.extend(
                (
                    passage,
                    access.source_view(purpose, "resolve", {"reference": reference}),
                )
            )
            proposal, citation = access.propose_source(
                purpose,
                passage,
                "passage",
                "Retained passage offered for interpretation.",
                reference,
            )
            evaluation = host.evaluate_proposal(proposal)
            projection = reconstruct_ci_projection(
                host.current.boundary, expected_target=host.current.boundary.target
            )
            summary.update(
                outcome="qualified_mechanical_preparation",
                catalog_id=catalog.identity,
                lineage_id=host.lineage_id,
                revision_id=host.current.revision_id,
                checkpoint_digest=host.current.digest(),
                target=asdict(host.current.boundary.target),
                source_files=len(catalog.files),
                source_profile_bytes=len(profile),
                changed_files=len(prepared.inputs.changed_files),
                workflow_runs=len(prepared.ci.inputs),
                native_coverage=projection.ci_coverage_result.state,
                native_runtime=asdict(projection.runtime_dependency_state_result),
                accounting=[asdict(receipt) for receipt in access.receipts],
                deliveries=deliveries,
                source_citation=citation,
                proposal_evaluation=host.lifecycle_value(evaluation).outcome,
                unavailable=[
                    "general API applicability",
                    "canonical adequacy",
                    "installed/artifact compatibility",
                    "strong release/interval authority without qualified family inputs",
                ],
                capture_limit="Current API evidence is acquisition-time and retrospective; historical bounded/manual CI is separate raw source. Original source inventories retain their exclusions.",
            )
        except (ValueError, RuntimeError, KeyError, TypeError) as error:
            summary.update(
                outcome="blocked", problem=type(error).__name__, detail=str(error)
            )
        finally:
            (directory / "public-acquisition.json").write_text(
                json.dumps(session.receipts, indent=2)
            )
            summary["public_backend_operations"] = len(session.receipts)
            session.close()
        manifest["cases"].append(summary)
        (output / "manifest.json").write_text(json.dumps(manifest, indent=2))
        print(
            json.dumps(
                {
                    key: summary[key]
                    for key in ("case_id", "outcome", "public_backend_operations")
                },
                sort_keys=True,
            ),
            flush=True,
        )
    manifest["outcome"] = (
        "qualified_mechanical_preparation"
        if all(
            c["outcome"] == "qualified_mechanical_preparation"
            for c in manifest["cases"]
        )
        else "blocked"
    )
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2))
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, required=True)
    parser.add_argument("--targets", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    raise SystemExit(
        0
        if run(args.corpus, args.targets, args.output)["outcome"]
        == "qualified_mechanical_preparation"
        else 1
    )
