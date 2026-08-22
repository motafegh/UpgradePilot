"""Acquire bounded repository text at immutable GitHub revisions.

START HERE
----------
``GitHubRepositoryClient`` is the provider boundary for repository files used by
UpgradePilot dependency, CI, Target, and upstream responsibilities.  The normal flow is:

``repository + immutable revision + repository path``
    -> GitHub Contents API
    -> validate the untrusted response as the exact requested regular file
    -> strict base64 decode + actual-byte bound + UTF-8 decode
    -> ``RepositoryTextFile`` or ``UnavailableRepositoryFile``
    -> domain-specific consumers

The durable successful contract intentionally contains only the source locator and text
that later product responsibilities need: repository, path, immutable revision, and
content. Provider response details such as the echoed path, reported size, blob identity,
and retrieval time are not propagated merely because GitHub returns them. A response fact
must support a current product/proof responsibility before it becomes durable evidence.

Repository-relative path *structure* is owned by ``upgradepilot.repository_path``.
GitHub-specific acquisition and response semantics stay here so external trust-boundary
validation cannot drift into dependency, CI, Target, or upstream consumers.
"""

from __future__ import annotations

import base64
import binascii
from dataclasses import dataclass
from urllib.parse import quote

from requests import Session

from ..repository_path import repository_relative_parts
from .actions import WorkflowRun
from .api import (
    DEFAULT_TIMEOUT,
    GitHubAcquisitionError,
    GitHubApiClient,
    GitHubResponseError,
    required_positive_int,
    required_str,
)
from .identity import validate_commit_sha, validate_repository
from .pull_request import PullRequestIdentity

_MAX_TEXT_BYTES = 1_000_000


@dataclass(frozen=True, slots=True)
class RepositoryTextFile:
    """One successfully admitted UTF-8 repository file at an immutable revision.

    The type carries only durable facts that current consumers need. Construction checks
    the internal locator/text shape so a consumer receiving this type does not need to
    revalidate provider-owned path/revision/text invariants. Actual acquisition authority
    still belongs to ``GitHubRepositoryClient``; manually constructing a structurally valid
    Python object does not prove that GitHub returned it.
    """

    repository: str
    path: str
    revision: str
    content: str

    def __post_init__(self) -> None:
        _validate_exact_repository_locator(
            repository=self.repository,
            path=self.path,
            revision=self.revision,
        )
        if not isinstance(self.content, str):
            raise TypeError("RepositoryTextFile content must be UTF-8 text.")


@dataclass(frozen=True, slots=True)
class UnavailableRepositoryFile:
    """Typed evidence that one exact-revision repository file was unavailable."""

    repository: str
    path: str
    revision: str
    reason: str
    detail: str

    def __post_init__(self) -> None:
        _validate_exact_repository_locator(
            repository=self.repository,
            path=self.path,
            revision=self.revision,
        )
        if not _is_nonempty_trimmed_text(self.reason):
            raise ValueError("UnavailableRepositoryFile reason must be non-empty text.")
        if not _is_nonempty_trimmed_text(self.detail):
            raise ValueError("UnavailableRepositoryFile detail must be non-empty text.")


type RepositoryFileEvidence = RepositoryTextFile | UnavailableRepositoryFile


class GitHubRepositoryClient(GitHubApiClient):
    """Read strongly admitted UTF-8 repository text at immutable revisions."""

    def __init__(
        self,
        *,
        token: str | None = None,
        session: Session | None = None,
        timeout: tuple[float, float] = DEFAULT_TIMEOUT,
    ) -> None:
        super().__init__(token=token, session=session, timeout=timeout)

    def get_pull_request_base_file(
        self,
        identity: PullRequestIdentity,
        path: str,
    ) -> RepositoryFileEvidence:
        """Acquire one file at the immutable pull-request base SHA."""

        return self._get_exact_pull_request_text_file(
            identity,
            path,
            revision=identity.base_sha,
        )

    def get_pull_request_head_file(
        self,
        identity: PullRequestIdentity,
        path: str,
    ) -> RepositoryFileEvidence:
        """Acquire one file at the immutable pull-request head SHA."""

        return self._get_exact_pull_request_text_file(
            identity,
            path,
            revision=identity.head_sha,
        )

    def get_exact_commit_text_file(
        self,
        repository: str,
        commit_sha: str,
        path: str,
    ) -> RepositoryFileEvidence:
        """Acquire one repository text file at an explicit immutable commit SHA."""

        repository = validate_repository(repository)
        commit_sha = validate_commit_sha(commit_sha)
        return self._get_exact_repository_text_file(
            repository,
            path,
            revision=commit_sha,
        )

    def get_exact_head_workflow_file(
        self,
        identity: PullRequestIdentity,
        run: WorkflowRun,
    ) -> RepositoryFileEvidence:
        """Resolve and acquire the workflow definition for one exact-head PR run."""

        if run.head_sha != identity.head_sha:
            raise GitHubResponseError(
                "Cannot acquire a workflow definition for a different head SHA."
            )

        metadata_url = self.api_url(
            f"/repos/{identity.repository}/actions/runs/{run.run_id}"
        )
        metadata = self._get_json_object(
            metadata_url,
            resource="workflow-run-detail",
        )
        try:
            run_id = required_positive_int(metadata, "id")
            workflow_id = required_positive_int(metadata, "workflow_id")
            head_sha = required_str(metadata, "head_sha")
            event = required_str(metadata, "event")
            workflow_path = required_str(metadata, "path")
        except KeyError as exc:
            raise GitHubResponseError(
                "GitHub workflow-run detail is missing required field: "
                f"{exc.args[0]}."
            ) from exc

        if run_id != run.run_id or workflow_id != run.workflow_id:
            raise GitHubResponseError(
                "GitHub workflow-run detail identity does not match the workflow run."
            )
        if head_sha != identity.head_sha or event != "pull_request":
            raise GitHubResponseError(
                "GitHub workflow-run detail does not match the frozen PR head and event."
            )
        if not workflow_path.startswith(".github/workflows/"):
            raise GitHubResponseError(
                "GitHub workflow path was outside .github/workflows/."
            )

        return self.get_exact_head_text_file(identity, workflow_path)

    def get_exact_head_text_file(
        self,
        identity: PullRequestIdentity,
        path: str,
    ) -> RepositoryFileEvidence:
        """Acquire the same exact-file contract used by every repository reader."""

        return self._get_exact_repository_text_file(
            identity.repository,
            path,
            revision=identity.head_sha,
        )

    def _get_exact_pull_request_text_file(
        self,
        identity: PullRequestIdentity,
        path: str,
        *,
        revision: str,
    ) -> RepositoryFileEvidence:
        if revision not in {identity.base_sha, identity.head_sha}:
            raise ValueError(
                "Exact pull-request file acquisition requires the PR base or head SHA."
            )
        return self._get_exact_repository_text_file(
            identity.repository,
            path,
            revision=revision,
        )

    def _get_exact_repository_text_file(
        self,
        repository: str,
        path: str,
        *,
        revision: str,
    ) -> RepositoryFileEvidence:
        """Acquire one exact path while retaining only durable admitted source facts.

        Passing this boundary permits downstream code to rely on repository/path/revision
        shape and UTF-8 content. The provider still checks GitHub's echoed path because a
        response for another file would be the wrong evidence; that echoed value is then
        discarded because equality has already established the durable ``path`` fact.
        """

        repository = validate_repository(repository)
        revision = validate_commit_sha(revision)

        path_parts = repository_relative_parts(path)
        if path_parts is None:
            raise ValueError(
                "Repository path must be a repository-relative POSIX file path."
            )
        normalized_path = "/".join(path_parts)

        encoded_path = quote(normalized_path, safe="/")
        url = self.api_url(f"/repos/{repository}/contents/{encoded_path}")

        try:
            data = self._get_json_object(
                url,
                resource="repository-file",
                params={"ref": revision},
            )
        except GitHubAcquisitionError as exc:
            if exc.reason == "not_found_or_inaccessible":
                return UnavailableRepositoryFile(
                    repository=repository,
                    path=normalized_path,
                    revision=revision,
                    reason=exc.reason,
                    detail=str(exc),
                )
            raise

        try:
            response_type = data["type"]
            returned_path = data["path"]
            encoding = data["encoding"]
            encoded_content = data["content"]
        except KeyError as exc:
            raise GitHubResponseError(
                "GitHub repository-file response is missing required field: "
                f"{exc.args[0]}."
            ) from exc

        if response_type != "file":
            raise GitHubResponseError(
                "GitHub repository-file response did not describe a regular file."
            )
        if returned_path != normalized_path:
            raise GitHubResponseError(
                "GitHub repository-file path does not match the requested path."
            )
        if encoding != "base64":
            raise GitHubResponseError(
                "GitHub repository-file content must use base64 encoding."
            )
        if not isinstance(encoded_content, str):
            raise GitHubResponseError(
                "GitHub repository-file field 'content' must be text."
            )

        raw_content = _decode_base64_repository_content(encoded_content)
        if len(raw_content) > _MAX_TEXT_BYTES:
            raise GitHubResponseError(
                "The decoded repository file exceeds the current bounded text-file "
                f"limit of {_MAX_TEXT_BYTES} bytes."
            )

        return RepositoryTextFile(
            repository=repository,
            path=normalized_path,
            revision=revision,
            content=_decode_utf8_repository_content(raw_content),
        )


def _validate_exact_repository_locator(
    *,
    repository: str,
    path: str,
    revision: str,
) -> None:
    """Enforce the normalized locator shape every exact-file evidence state promises."""

    normalized_repository = validate_repository(repository)
    if normalized_repository != repository:
        raise ValueError("Repository identity must already be normalized.")

    path_parts = repository_relative_parts(path)
    if path_parts is None or "/".join(path_parts) != path:
        raise ValueError("Repository path must already be a normalized POSIX file path.")

    normalized_revision = validate_commit_sha(revision)
    if normalized_revision != revision:
        raise ValueError("Repository revision must already be a normalized immutable SHA.")


def _is_nonempty_trimmed_text(value: object) -> bool:
    return isinstance(value, str) and bool(value) and value == value.strip()


def _decode_base64_repository_content(encoded_content: str) -> bytes:
    """Decode GitHub's base64 content field without accepting malformed input."""

    compact_content = "".join(encoded_content.split())
    try:
        return base64.b64decode(compact_content, validate=True)
    except (binascii.Error, ValueError) as exc:
        raise GitHubResponseError(
            "GitHub repository-file content was not valid base64."
        ) from exc


def _decode_utf8_repository_content(raw_content: bytes) -> str:
    """Decode repository bytes as the UTF-8 text contract owned by this client."""

    try:
        return raw_content.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise GitHubResponseError(
            "The repository file was not valid UTF-8 text."
        ) from exc


__all__ = (
    "GitHubRepositoryClient",
    "RepositoryFileEvidence",
    "RepositoryTextFile",
    "UnavailableRepositoryFile",
)
