"""Model-free dependency/CI preparation using the normal product's shared owners.

This is a trusted bootstrap entry point for an explicitly selected exact PR snapshot.
Provider failures propagate before affected facts are invented. Native preparation runs
once, publishes coherent partial progress and leaves upstream/semantic work unperformed.
It grants no Investigator execution authority or complete investigation/adequacy claim.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..dependency.change import DependencyVersionChange
from ..github.actions import GitHubActionsClient
from ..github.pull_request import GitHubPullRequestClient
from ..github.repository import GitHubRepositoryClient
from ..investigation_inputs import (
    AcquiredDependencyInputs,
    PreparedCIEvidence,
    acquire_dependency_inputs,
    prepare_ci_evidence,
)
from .lifecycle_host import InvestigationWorkspaceHost
from .native_capture import NativeInvestigationCapture
from .native_projection import reconstruct_ci_projection


@dataclass(frozen=True, slots=True)
class PreparedDependencyCIWorkspace:
    host: InvestigationWorkspaceHost
    inputs: AcquiredDependencyInputs
    ci: PreparedCIEvidence | None


def prepare_dependency_ci_workspace(
    repository: str,
    pull_number: int,
    *,
    expected_base: str,
    expected_head: str,
    pull_client: GitHubPullRequestClient | None = None,
    repository_client: GitHubRepositoryClient | None = None,
    actions_client: GitHubActionsClient | None = None,
    host: InvestigationWorkspaceHost | None = None,
) -> PreparedDependencyCIWorkspace:
    """Acquire/qualify an exact common input snapshot, without model or target execution.

    This bootstrap is native composition, not an Investigator request. Captures/receipts
    must retain acquisition time/strength separately; current API observations cannot be
    relabelled original decision-time inputs. Supplying a schema-2 host makes publication
    durable; omitting it uses the existing volatile contract.
    """
    pull_client = pull_client or GitHubPullRequestClient()
    repository_client = repository_client or GitHubRepositoryClient()
    actions_client = actions_client or GitHubActionsClient()
    host = host or InvestigationWorkspaceHost()
    inputs = acquire_dependency_inputs(
        repository,
        pull_number,
        pull_client,
        repository_client,
        expected_base=expected_base,
        expected_head=expected_head,
    )
    capture = NativeInvestigationCapture()
    capture.start(
        inputs.identity, inputs.changed_files, inputs.dependency, inputs.source_contexts
    )
    host.initialize(capture.partial_snapshot())
    ci = None
    if isinstance(inputs.dependency, DependencyVersionChange):
        ci = prepare_ci_evidence(inputs, actions_client, repository_client)
        capture.capture_ci(ci.inputs, ci.coverage, ci.runtime)
        host.publish_native_progress(capture.partial_snapshot())
    assert host.current is not None
    reconstruct_ci_projection(
        host.current.boundary, expected_target=host.current.boundary.target
    )
    return PreparedDependencyCIWorkspace(host, inputs, ci)
