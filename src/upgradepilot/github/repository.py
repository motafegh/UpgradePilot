"""Acquire bounded repository text at immutable GitHub revisions.

START HERE
----------
``GitHubRepositoryClient`` is the provider boundary for repository text used by dependency,
workflow, Target, and upstream consumers. A successful read returns ``RepositoryTextFile``;
an unavailable exact file returns ``UnavailableRepositoryFile``.

The durable successful-file contract is intentionally small:

``repository + immutable revision + repository-relative path + UTF-8 content``.

GitHub response details such as the returned path spelling are validated here when they are
needed to admit the response, then discarded. Downstream modules should validate their own
relationships and domain meaning rather than revalidating provider transport details.

Repository-relative path structure is owned by ``upgradepilot.repository_path`` and GitHub
repository/commit identity grammar by ``upgradepilot.github.identity``.
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
# Base64 uses four encoded characters for each three input bytes. Bounding the compact
# encoded form before decoding prevents a malicious/incorrect response from forcing an
# unbounded allocation merely because GitHub's separate reported-size field is no longer
# part of the admitted evidence contract.
_MAX_BASE64_TEXT_CHARS = 4 * ((_MAX_TEXT_BYTES + 2) // 3)


@dataclass(frozen=True, slots=True)
class RepositoryTextFile:
    """One structurally valid UTF-8 repository file at an immutable revision.

    This type enforces internal facts that every successful instance may rely on:
    canonical repository identity, normalized repository-relative path, canonical immutable
    Git revision, and bounded UTF-8-representable text. It does **not** prove that a manually
    constructed instance was actually fetched from GitHub; external acquisition truth remains
    the provider's responsibility.
    """

    repository: str
    path: str
    revision: str
    content: str

    def __post_init__(self) -> None:
        _validate_exact_file_locator(self.repository, self.path, self.revision)
        _validate_bounded_utf8_text(self.content)


@dataclass(frozen=True, slots=True)
class UnavailableRepositoryFile:
    """Typed evidence that one exact repository file was absent or inaccessible."""

    repository: str
    path: str
    revision: str
    reason: str
    detail: str

    def __post_init__(self) -> None:
        _validate_exact_file_locator(self.repository, self.path, self.revision)
        if not isinstance(self.reason, str) or not self.reason.strip():
            raise ValueError("Unavailable repository-file reason must be non-empty text.")
        if not isinstance(self.detail, str) or not self.detail.strip():
            raise ValueError("Unavailable repository-file detail must be non-empty text.")


type RepositoryFileEvidence = RepositoryTextFile | UnavailableRepositoryFile


class GitHubRepositoryClient(GitHubApiClient):
    """Read bounded UTF-8 repository text at immutable GitHub revisions."""

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
        """Acquire the same exact-file contract used by every repository-text reader."""

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
        """Acquire and admit one repository-relative UTF-8 file at ``revision``.

        Passing this boundary establishes that GitHub described a regular file at the
        requested path, supplied supported base64 text, and that the decoded bytes fit the
        product's text bound and decode as UTF-8. Response-only details used to establish
        those facts are intentionally not copied into ``RepositoryTextFile``.
        """

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


def _validate_exact_file_locator(repository: str, path: str, revision: str) -> None:
    """Enforce the canonical internal locator shared by available/unavailable evidence."""

    normalized_repository = validate_repository(repository)
    if normalized_repository != repository:
        raise ValueError("Repository identity must already be in canonical admitted form.")

    path_parts = repository_relative_parts(path)
    if path_parts is None or "/".join(path_parts) != path:
        raise ValueError(
            "Repository file path must be a normalized repository-relative POSIX path."
        )

    normalized_revision = validate_commit_sha(revision)
    if normalized_revision != revision:
        raise ValueError("Repository file revision must use canonical lowercase hex.")


def _validate_bounded_utf8_text(content: str) -> None:
    """Make the successful evidence type itself reject malformed/oversized text states."""

    if not isinstance(content, str):
        raise TypeError("Repository file content must be text.")
    try:
        raw_content = content.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError("Repository file content must be valid UTF-8 text.") from exc
    if len(raw_content) > _MAX_TEXT_BYTES:
        raise ValueError(
            "Repository file content exceeds the current bounded text-file limit of "
            f"{_MAX_TEXT_BYTES} bytes."
        )


def _decode_base64_repository_content(encoded_content: str) -> bytes:
    """Decode bounded GitHub base64 content without accepting malformed input."""

    compact_content = "".join(encoded_content.split())
    if len(compact_content) > _MAX_BASE64_TEXT_CHARS:
        raise GitHubResponseError(
            "The encoded repository file exceeds the current bounded text-file limit."
        )
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
