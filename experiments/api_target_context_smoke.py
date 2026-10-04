"""Ordinary public PR source/context trial; no model or compatibility verdict.

Run: PYTHONPATH=src .venv/bin/python -m experiments.api_target_context_smoke REPOSITORY PR
Known target paths, framework names and adapter versions are not runner arguments.
Providers share one 50-request budget per acquisition run. Anonymous by default;
token-env explicitly reads GITHUB_TOKEN, which is sent only to the GitHub API.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path

from upgradepilot.dependency.analysis import (
    DependencyChangeAnalysis,
    analyze_dependency_change,
)
from upgradepilot.github.api import GitHubAcquisitionError, GitHubResponseError
from upgradepilot.github.pull_request import (
    GitHubPullRequestClient,
    PullRequestIdentity,
)
from upgradepilot.github.repository import GitHubRepositoryClient
from upgradepilot.upstream.interval import DependencyReleaseInterval

from .api_adapter_exploration import AdapterExploration, AdapterSourceExplorer
from .api_change_source_acquisition import (
    AcquisitionProblem,
    DeclaredReleaseWindowAcquirer,
    TrialPublicSession,
)
from .api_target_context import (
    TargetContext,
    TargetContextAcquirer,
    file_sha256,
    source_id,
)


@dataclass(frozen=True)
class PublicPRContextTrial:
    identity: PullRequestIdentity
    analysis: DependencyChangeAnalysis
    target: TargetContext
    upstream: object
    adapters: AdapterExploration


def acquire_public_pr_context(
    repository: str,
    number: int,
    *,
    session=None,
    pull_requests=None,
    files=None,
    target=None,
    upstream=None,
    adapters=None,
) -> PublicPRContextTrial | AcquisitionProblem:
    session = session or TrialPublicSession()
    files = files or GitHubRepositoryClient(session=session)
    pull_requests = pull_requests or GitHubPullRequestClient(session=session)
    target = target or TargetContextAcquirer(session=session, files=files)
    upstream = upstream or DeclaredReleaseWindowAcquirer(session=session, files=files)
    adapters = adapters or AdapterSourceExplorer(session=session, files=files)
    try:
        identity = pull_requests.get_pull_request(repository, number)
        changes = pull_requests.get_changed_files(identity)
        analysis = analyze_dependency_change(identity, changes, files)
        if not isinstance(analysis, DependencyChangeAnalysis):
            return AcquisitionProblem(
                "dependency", analysis.reason, analysis.detail, analysis
            )
        context = target.acquire(identity.repository, identity.head_sha)
        if isinstance(context, AcquisitionProblem):
            return context
        dependency = analysis.dependency
        interval = DependencyReleaseInterval(
            dependency.package,
            dependency.normalized_package,
            dependency.old_version,
            dependency.proposed_version,
        )
        source = upstream.acquire(interval)
        explored = adapters.explore(context)
        return PublicPRContextTrial(identity, analysis, context, source, explored)
    except (GitHubAcquisitionError, GitHubResponseError) as exc:
        return AcquisitionProblem(
            "public_pr", getattr(exc, "reason", "malformed_response"), str(exc)
        )


def context_manifest(context: TargetContext) -> dict:
    return {
        "repository": context.inventory.repository,
        "revision": context.inventory.revision,
        "tree_sha": context.inventory.tree_sha,
        "inventory_truncated": context.inventory.truncated,
        "inventory_entries": len(context.inventory.entries),
        "files": [
            {
                "source_id": source_id(f),
                "sha256": file_sha256(f),
                "bytes": len(f.content.encode("utf-8")),
            }
            for f in context.files
        ],
        "imports": [asdict(f) for f in context.imports],
        "references": [asdict(r) for r in context.references],
        "declarations": [asdict(d) for d in context.declarations],
        "candidates": [asdict(c) for c in context.candidates],
        "excluded_paths": context.excluded_paths,
        "omitted_paths": context.omitted_paths,
        "gaps": [asdict(g) for g in context.gaps],
        "examined_bytes": context.examined_bytes,
        "limitations": context.limitations,
    }


def trial_manifest(
    result: PublicPRContextTrial | AcquisitionProblem, session: TrialPublicSession
) -> dict:
    manifest = {
        "timestamp": datetime.now(UTC).isoformat(),
        "auth": session.auth_mode,
        "github_requests": session.github_requests,
        "proof": "ordinary PR acquisition and static/exploration evidence; no model, resolved-version, runtime or compatibility acceptance",
        "code_sha256": {
            p: hashlib.sha256(Path(__file__).with_name(p).read_bytes()).hexdigest()
            for p in (
                "api_target_context.py",
                "api_adapter_exploration.py",
                "api_target_context_smoke.py",
                "api_change_source_acquisition.py",
            )
        },
    }
    if isinstance(result, AcquisitionProblem):
        return {
            **manifest,
            "state": "incomplete",
            "stage": result.stage,
            "reason": result.reason,
            "detail": result.detail,
        }
    upstream = result.upstream
    if isinstance(upstream, AcquisitionProblem):
        source = {
            "state": "incomplete",
            "stage": upstream.stage,
            "reason": upstream.reason,
            "detail": upstream.detail,
        }
    else:
        source = {
            "state": "available",
            "basis": upstream.association.basis,
            "repository": upstream.file.repository,
            "revision": upstream.file.revision,
            "path": upstream.file.path,
            "versions": upstream.ordered_versions,
            "sha256": upstream.full_text_sha256,
            "window_sha256": upstream.window_sha256,
        }
    return {
        **manifest,
        "state": "context_acquired",
        "identity": asdict(result.identity),
        "dependency": asdict(result.analysis.dependency),
        "target": context_manifest(result.target),
        "upstream": source,
        "adapter_exploration": {
            "samples": [
                {
                    "candidate": asdict(s.candidate),
                    "depth": s.depth,
                    "version": s.version,
                    "selection": s.selection,
                    "association_basis": s.association.basis,
                    "provenance_state": s.association.provenance_result.state,
                    "repository": s.file.repository,
                    "revision": s.file.revision,
                    "path": s.file.path,
                    "sha256": file_sha256(s.file),
                    "metadata": asdict(s.metadata),
                    "imports": [asdict(f) for f in s.imports],
                    "references": [asdict(r) for r in s.references],
                    "gaps": [asdict(g) for g in s.gaps],
                }
                for s in result.adapters.samples
            ],
            "problems": [
                {"stage": p.stage, "reason": p.reason, "detail": p.detail}
                for p in result.adapters.problems
            ],
            "omitted_candidates": [
                asdict(c) for c in result.adapters.omitted_candidates
            ],
            "limitations": result.adapters.limitations,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository")
    parser.add_argument("pull_number", type=int)
    parser.add_argument(
        "--github-auth", choices=("anonymous", "token-env"), default="anonymous"
    )
    args = parser.parse_args()
    token = os.environ.get("GITHUB_TOKEN") if args.github_auth == "token-env" else None
    if args.github_auth == "token-env" and not token:
        parser.error("token-env requires GITHUB_TOKEN")
    session = TrialPublicSession(token=token)
    result = acquire_public_pr_context(
        args.repository, args.pull_number, session=session
    )
    print(json.dumps(trial_manifest(result, session), indent=2))
    return 1 if isinstance(result, AcquisitionProblem) else 0


if __name__ == "__main__":
    raise SystemExit(main())
