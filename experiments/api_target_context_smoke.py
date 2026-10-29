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

from upgradepilot.dependency.analysis import DependencyChangeAnalysis
from upgradepilot.dependency.change import DependencyVersionChange
from upgradepilot.github.api import GitHubAcquisitionError, GitHubResponseError
from upgradepilot.github.pull_request import (
    GitHubPullRequestClient,
    PullRequestIdentity,
)
from upgradepilot.github.repository import GitHubRepositoryClient
from upgradepilot.investigation_inputs import AcquiredDependencyInputs, acquire_dependency_inputs
from upgradepilot.upstream.interval import DependencyReleaseInterval

from .api_adapter_exploration import (
    AdapterExploration, AdapterSourceExplorer, ExaminedPythonModule, PythonModuleSourceRequest,
    PythonSourceAcquisitionRun,
    PythonSourceAcquisitionWork,
)
from .api_change_source_acquisition import (
    AcquisitionProblem,
    DeclaredReleaseWindowAcquirer,
    TrialPublicSession,
)
from .api_python_bindings import python_facts_manifest
from .api_release_window_manifest import release_window_manifest
from .api_target_context import (
    TargetContext,
    TargetContextAcquirer,
    file_sha256,
    source_id,
)


@dataclass(frozen=True)
class PublicPRContextTrial:
    """One native acquisition horizon plus experimental source observations.

    The read-only identity/analysis properties preserve existing consumers; they
    project the shared inputs without another provider read or domain evaluation.
    The legacy manifest remains a fact/hash view, not complete offline recovery.
    """

    inputs: AcquiredDependencyInputs
    target: TargetContext
    upstream: object
    adapters: AdapterExploration
    changed_sources: tuple[ChangedPackageModuleAttempt, ...] = ()
    source_work: PythonSourceAcquisitionWork | None = None
    unexamined_changed_modules: tuple[str, ...] = ()

    @property
    def identity(self) -> PullRequestIdentity:
        return self.inputs.identity

    @property
    def analysis(self) -> DependencyChangeAnalysis:
        return DependencyChangeAnalysis(self.inputs.dependency, self.inputs.source_contexts)


@dataclass(frozen=True)
class ChangedPackageModuleAttempt:
    request: PythonModuleSourceRequest
    outcome: ExaminedPythonModule | AcquisitionProblem


def _origin_for_module(module, import_fact, references):
    """Keep a matching existing binding trace when available; infer no new binding."""
    for reference in references:
        if reference.source_id == import_fact.source_id and reference.binding is not None:
            if any(origin == module or origin.startswith(module + ".")
                   for origin in reference.binding.possible_imports):
                return reference
    return import_fact


def examine_changed_package_modules(inputs, context, exploration, source_run):
    """Inspect observed changed-package modules at native old/proposed versions.

    Target candidates already carry the declaration/module association; adapter
    imports require the acquired release's declaration, as in normal exploration.
    This is module examination only: no export, callable or execution edge is inferred.
    """
    package = inputs.dependency.normalized_package
    origins = [
        (candidate.imported_module, _origin_for_module(candidate.imported_module, origin, context.references))
        for candidate in context.candidates
        if candidate.declaration.package == package
        for origin in context.imports
        if origin.source_id == candidate.import_source_id and origin.line == candidate.import_line
        and origin.module == candidate.imported_module
    ]
    for candidate in exploration.deferred_candidates:
        for sample in exploration.samples:
            origins.extend(
                (origin.module, _origin_for_module(origin.module, origin, sample.references))
                for origin in sample.imports
                if origin.source_id == candidate.import_source_id
                and origin.line == candidate.import_line and origin.module == candidate.imported_module
            )
    # One observed basis per distinct module is sufficient for source examination,
    # not call-site/path coverage. All original imports remain in their input owner.
    by_module = dict()
    for module, origin in origins:
        by_module.setdefault(module, origin)
    attempts, omitted = [], []
    for module, origin in by_module.items():
        if len(attempts) + 2 > source_run.max_module_files:
            omitted.append(module)
            continue
        for version, basis in (
            (inputs.dependency.old_version, "native_old_version"),
            (inputs.dependency.proposed_version, "native_proposed_version"),
        ):
            request = PythonModuleSourceRequest(package, version, module, basis, origin)
            attempts.append(ChangedPackageModuleAttempt(request, source_run.examine(request)))
    return tuple(attempts), tuple(omitted)


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
    expected_base: str | None = None,
    expected_head: str | None = None,
    max_target_python_files: int = 200,
    source_run: PythonSourceAcquisitionRun | None = None,
) -> PublicPRContextTrial | AcquisitionProblem:
    session = session or TrialPublicSession()
    files = files or GitHubRepositoryClient(session=session)
    pull_requests = pull_requests or GitHubPullRequestClient(session=session)
    target = target or TargetContextAcquirer(session=session, files=files)
    upstream = upstream or DeclaredReleaseWindowAcquirer(session=session, files=files)
    adapters = adapters or AdapterSourceExplorer(session=session, files=files)
    source_run = source_run if source_run is not None else adapters.source_run()
    try:
        acquired = acquire_dependency_inputs(
            repository, number, pull_requests, files,
            expected_base=expected_base, expected_head=expected_head,
        )
        identity = acquired.identity
        dependency = acquired.dependency
        if not isinstance(dependency, DependencyVersionChange):
            return AcquisitionProblem(
                "dependency", dependency.reason, dependency.detail, dependency
            )
        context = target.acquire(
            identity.repository, identity.head_sha, max_python_files=max_target_python_files,
        )
        if isinstance(context, AcquisitionProblem):
            return context
        interval = DependencyReleaseInterval(
            dependency.package,
            dependency.normalized_package,
            dependency.old_version,
            dependency.proposed_version,
        )
        source = upstream.acquire(interval)
        explored = adapters.explore(
            context, source_run=source_run, stop_at_package=dependency.normalized_package,
        )
        changed_sources, omitted = examine_changed_package_modules(acquired, context, explored, source_run)
        return PublicPRContextTrial(
            acquired, context, source, explored, changed_sources,
            source_run.work, omitted,
        )
    except (GitHubAcquisitionError, GitHubResponseError) as exc:
        return AcquisitionProblem(
            "public_pr", getattr(exc, "reason", "malformed_response"), str(exc), exc,
        )


def context_manifest(context: TargetContext) -> dict:
    return {
        **python_facts_manifest(context.imports, context.references),
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
                "api_release_window_manifest.py",
                "api_python_bindings.py",
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
    return {
        **manifest,
        "state": "context_acquired",
        "identity": asdict(result.identity),
        "dependency": asdict(result.analysis.dependency),
        "target": context_manifest(result.target),
        "changed_package_sources": {
            "proof": "observed-module examination at native versions; no callable or runtime correspondence",
            "work": asdict(result.source_work) if result.source_work is not None else None,
            "unexamined_modules": result.unexamined_changed_modules,
            "attempts": [module_attempt_manifest(attempt) for attempt in result.changed_sources],
            "retention": "source identities/hashes and facts only; complete text recovery not supplied by this manifest",
        },
        "upstream": release_window_manifest(result.upstream),
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
                    **python_facts_manifest(s.imports, s.references),
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
            "deferred_to_native_versions": [asdict(c) for c in result.adapters.deferred_candidates],
            "limitations": result.adapters.limitations,
        },
    }


def module_attempt_manifest(attempt: ChangedPackageModuleAttempt) -> dict:
    question = {"request": asdict(attempt.request)}
    source = attempt.outcome
    if isinstance(source, AcquisitionProblem):
        # Budget refusal may follow partial acquisition; only the separate omitted
        # module list represents questions not issued by this composition.
        return {**question, "state": "refused" if source.stage == "python_source_budget" else "unavailable", "stage": source.stage,
                "reason": source.reason, "detail": source.detail}
    return {
        **question, "state": "module_examined",
        "repository": source.file.repository, "revision": source.file.revision,
        "path": source.file.path, "sha256": file_sha256(source.file),
        "bytes": len(source.file.content.encode("utf-8")),
        "association_basis": source.association.basis,
        "provenance_state": source.association.provenance_result.state,
        "tag_commits": {tag.requested_tag: tag.resolved_commit_sha for tag in source.tags},
        "metadata": asdict(source.metadata),
        **python_facts_manifest(source.imports, source.references),
        "gaps": [asdict(gap) for gap in source.gaps],
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
    # Keep the complete machine-consumed packet within its replay byte budget;
    # human-facing product report formatting is a separate responsibility.
    print(json.dumps(trial_manifest(result, session), separators=(",", ":")))
    return 1 if isinstance(result, AcquisitionProblem) else 0


if __name__ == "__main__":
    raise SystemExit(main())
