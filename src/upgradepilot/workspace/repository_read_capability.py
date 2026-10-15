"""Bind the existing exact repository-file provider to the generic lifecycle host.

This adapter admits repository-relative paths at an exact target head, never a Python
declaration role. The existing provider owns acquisition and the domain caller owns all
interpretation. HTTP failure/inaccessibility is a problem, not proven file absence.
"""

from typing import cast

from ..github.api import GitHubAcquisitionError, GitHubResponseError
from ..github.pull_request import PullRequestIdentity
from ..github.repository import (
    GitHubRepositoryClient,
    RepositoryFileEvidence,
    RepositoryTextFile,
    UnavailableRepositoryFile,
)
from ..repository_path import repository_relative_parts
from .lifecycle_host import CapabilityResult, HostCapability
from .lifecycle_records import (
    CapabilityObservation,
    CapabilityRequest,
    LifecycleMethodIdentity,
)
from .native_inputs_codec import LAYOUTS
from .native_representation import Either, NativeValueCodec, RecordRef, json_bytes

REPOSITORY_READ_CAPABILITY = "read_exact_repository_file"
_REPRESENTATION = "repository-file/native-layout-1"
_CODEC = NativeValueCodec(LAYOUTS)
_SHAPE = Either(
    (RecordRef("repository_text_file"), RecordRef("unavailable_repository_file"))
)


def repository_read_capability(
    identity: PullRequestIdentity,
    client: GitHubRepositoryClient,
) -> HostCapability:
    provider = client.get_exact_head_text_file
    module = getattr(provider, "__module__", None)
    name = getattr(provider, "__qualname__", None)
    provider_method = (
        f"{module}.{name}" if type(module) is str and type(name) is str else None
    )
    method = LifecycleMethodIdentity(
        "github.repository",
        "workspace.repository_read_capability.repository_read_capability.execute",
        None,
        None,
        "exact-repository-read/1",
        json_bytes({"provider_method": provider_method}).decode("utf-8"),
        (
            "adapter_and_provider_versions_unavailable",
            "client_authentication_metadata_not_retained",
        )
        + (("provider_method_unavailable",) if provider_method is None else ()),
    )

    def accepts_scope(path: str) -> bool:
        parts = repository_relative_parts(path)
        return parts is not None and path == "/".join(parts)

    def execute(request: CapabilityRequest) -> CapabilityResult:
        try:
            source = client.get_exact_head_text_file(identity, request.scope)
        except (GitHubAcquisitionError, GitHubResponseError) as error:
            # A completed provider failure is retained separately from an exception with
            # unknown completion. No absence, retry, or semantic conclusion is inferred.
            source = UnavailableRepositoryFile(
                identity.repository,
                request.scope,
                identity.head_sha,
                error.reason
                if isinstance(error, GitHubAcquisitionError)
                else "invalid_provider_response",
                "Exact repository read returned a provider problem.",
            )
        if not isinstance(source, (RepositoryTextFile, UnavailableRepositoryFile)) or (
            source.repository,
            source.revision,
            source.path,
        ) != (identity.repository, identity.head_sha, request.scope):
            raise ValueError("Provider result is outside the admitted exact request.")
        outcome = (
            "problem"
            if isinstance(source, UnavailableRepositoryFile)
            else ("empty" if source.content == "" else "observed")
        )
        return CapabilityResult(
            outcome,
            "Exact scoped repository response; no global absence or semantic support claim.",
            source,
            _REPRESENTATION,
            _CODEC.encode(source, _SHAPE).decode("utf-8"),
        )

    return HostCapability(
        REPOSITORY_READ_CAPABILITY,
        method,
        frozenset({"repository_read"}),
        accepts_scope,
        execute,
    )


def restore_repository_observation(
    observation: CapabilityObservation,
) -> RepositoryFileEvidence:
    """Decode retained provider material offline; never acquire or interpret it."""
    if (
        observation.representation != _REPRESENTATION
        or observation.retained_content is None
    ):
        raise ValueError(
            "Unsupported or missing retained repository-file representation."
        )
    return cast(
        RepositoryFileEvidence,
        _CODEC.decode(observation.retained_content.encode("utf-8"), _SHAPE),
    )
