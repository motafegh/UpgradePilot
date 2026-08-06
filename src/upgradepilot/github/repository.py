"""Acquire bounded repository text at immutable GitHub revisions.

One repository-text evidence type now serves workflows, target metadata, dependency
files, and upstream changelogs. Successful runtime acquisition populates the strong
exact-revision provenance fields: repository, requested/returned path, revision, blob,
reported/decoded byte counts, retrieval time, and UTF-8 content. Optional defaults
exist only so historical/manual fixtures can migrate without fabricating source facts.
"""

from __future__ import annotations

import base64
import binascii
from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime, timezone
from urllib.parse import quote

from requests import Session

from .actions import WorkflowRun
from .api import (
    DEFAULT_TIMEOUT,
    GitHubAcquisitionError,
    GitHubApiClient,
    GitHubResponseError,
    required_nonnegative_int,
    required_positive_int,
    required_str,
)
from .identity import validate_commit_sha, validate_repository
from .pull_request import PullRequestIdentity

_MAX_TEXT_BYTES = 1_000_000


@dataclass(frozen=True, slots=True)
class RepositoryTextFile:
    """UTF-8 repository file bound to one immutable revision.

    Runtime acquisition fills every provenance field. ``None`` is admitted only for
    older manually constructed evidence fixtures; downstream boundaries that require
    strict file identity must explicitly validate the strong fields before trusting
    them.
    """

    path: str
    revision: str
    blob_sha: str
    content: str
    repository: str | None = None
    returned_path: str | None = None
    reported_byte_count: int | None = None
    decoded_byte_count: int | None = None
    retrieved_at: datetime | None = None


# Historical name retained temporarily as an alias to the one active evidence type.
ExactRepositoryTextFile = RepositoryTextFile


@dataclass(frozen=True, slots=True)
class UnavailableRepositoryFile:
    """Typed evidence that an exact-revision file was absent or inaccessible."""

    path: str
    revision: str
    reason: str
    detail: str
    repository: str | None = None


type RepositoryFileEvidence = RepositoryTextFile | UnavailableRepositoryFile
type ExactRepositoryFileEvidence = RepositoryTextFile | UnavailableRepositoryFile


class GitHubRepositoryClient(GitHubApiClient):
    """Read strongly validated UTF-8 text at immutable repository revisions."""

    def __init__(
        self,
        *,
        token: str | None = None,
        session: Session | None = None,
        timeout: tuple[float, float] = DEFAULT_TIMEOUT,
        now: Callable[[], datetime] | None = None,
    ) -> None:
        super().__init__(token=token, session=session, timeout=timeout)
        self._now = now or (lambda: datetime.now(timezone.utc))

    def get_pull_request_base_file(
        self,
        identity: PullRequestIdentity,
        path: str,
    ) -> ExactRepositoryFileEvidence:
        return self._get_exact_pull_request_text_file(
            identity,
            path,
            revision=identity.base_sha,
        )

    def get_pull_request_head_file(
        self,
        identity: PullRequestIdentity,
        path: str,
    ) -> ExactRepositoryFileEvidence:
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
    ) -> ExactRepositoryFileEvidence:
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
        """Acquire the same strong exact-file contract used by every other reader."""

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
    ) -> ExactRepositoryFileEvidence:
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
    ) -> ExactRepositoryFileEvidence:
        normalized_path = _validate_repository_path(path)
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
            blob_sha = data["sha"]
            reported_byte_count = required_nonnegative_int(data, "size")
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
        if not isinstance(blob_sha, str) or not blob_sha:
            raise GitHubResponseError(
                "GitHub repository-file field 'sha' must be a non-empty string."
            )
        if reported_byte_count > _MAX_TEXT_BYTES:
            raise GitHubResponseError(
                "The repository-file reported size exceeds the current bounded "
                f"text-file limit of {_MAX_TEXT_BYTES} bytes."
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
        decoded_byte_count = len(raw_content)
        if decoded_byte_count != reported_byte_count:
            raise GitHubResponseError(
                "The decoded repository-file byte count does not match GitHub's "
                "reported size."
            )
        if decoded_byte_count > _MAX_TEXT_BYTES:
            raise GitHubResponseError(
                "The decoded repository file exceeds the current bounded text-file "
                f"limit of {_MAX_TEXT_BYTES} bytes."
            )

        return RepositoryTextFile(
            repository=repository,
            path=normalized_path,
            returned_path=returned_path,
            revision=revision,
            blob_sha=blob_sha,
            reported_byte_count=reported_byte_count,
            decoded_byte_count=decoded_byte_count,
            content=_decode_utf8_repository_content(raw_content),
            retrieved_at=self._now(),
        )


def _decode_base64_repository_content(encoded_content: str) -> bytes:
    compact_content = "".join(encoded_content.split())
    try:
        return base64.b64decode(compact_content, validate=True)
    except (binascii.Error, ValueError) as exc:
        raise GitHubResponseError(
            "GitHub repository-file content was not valid base64."
        ) from exc


def _decode_utf8_repository_content(raw_content: bytes) -> str:
    try:
        return raw_content.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise GitHubResponseError(
            "The repository file was not valid UTF-8 text."
        ) from exc


def _validate_repository_path(path: str) -> str:
    if not isinstance(path, str):
        raise ValueError("Repository path must be text.")
    normalized = path.strip()
    parts = normalized.split("/")
    if (
        not normalized
        or normalized.startswith("/")
        or normalized.endswith("/")
        or any(part in {"", ".", ".."} for part in parts)
    ):
        raise ValueError("Repository path must be a normalized relative file path.")
    return normalized


__all__ = (
    "ExactRepositoryFileEvidence",
    "ExactRepositoryTextFile",
    "GitHubRepositoryClient",
    "RepositoryFileEvidence",
    "RepositoryTextFile",
    "UnavailableRepositoryFile",
)
