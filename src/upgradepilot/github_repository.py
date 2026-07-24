"""Acquire exact-revision repository text files for CI interpretation.

GitHub Actions run records tell UpgradePilot which workflow executed, but they do
not contain the workflow commands themselves. This module closes that factual
acquisition gap by reading the workflow definition from the exact pull-request
head SHA already frozen in ``PullRequestIdentity``.

The module performs no CI interpretation. It only converts one GitHub contents
API response into either validated UTF-8 text or an explicit unavailable state.
"""

from __future__ import annotations

import base64
import binascii
from dataclasses import dataclass
from urllib.parse import quote

from .github_actions import WorkflowRun
from .github_api import (
    GitHubAcquisitionError,
    GitHubApiClient,
    GitHubResponseError,
    required_positive_int,
    required_str,
)
from .github_client import PullRequestIdentity

_MAX_TEXT_BYTES = 1_000_000


@dataclass(frozen=True, slots=True)
class RepositoryTextFile:
    """One UTF-8 repository file bound to an exact commit revision."""

    path: str
    revision: str
    blob_sha: str
    content: str


@dataclass(frozen=True, slots=True)
class UnavailableRepositoryFile:
    """An exact-revision file that GitHub reported as absent or inaccessible."""

    path: str
    revision: str
    reason: str
    detail: str


# Unavailability is evidence, not an exception, when GitHub returns its ambiguous
# 404 for one optional interpretation input. Other acquisition failures propagate.
type RepositoryFileEvidence = RepositoryTextFile | UnavailableRepositoryFile


class GitHubRepositoryClient(GitHubApiClient):
    """Acquire workflow definitions and repository files at the frozen PR head."""

    def get_exact_head_workflow_file(
        self,
        identity: PullRequestIdentity,
        run: WorkflowRun,
    ) -> RepositoryFileEvidence:
        """Resolve the run's workflow path and read it at the exact PR head."""

        if run.head_sha != identity.head_sha:
            raise GitHubResponseError(
                "Cannot acquire a workflow definition for a different head SHA."
            )

        # Run detail carries the path used by this execution. Current workflow
        # metadata could instead follow a later rename on the default branch.
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
        """Return one validated UTF-8 file at ``identity.head_sha``.

        GitHub's contents endpoint returns base64 text for ordinary files. The
        supplied path and returned path must agree, and the request is bound to
        the exact PR head through the ``ref`` query parameter.
        """

        normalized_path = _validate_repository_path(path)
        encoded_path = quote(normalized_path, safe="/")
        url = self.api_url(
            f"/repos/{identity.repository}/contents/{encoded_path}"
        )

        try:
            data = self._get_json_object(
                url,
                resource="repository-file",
                params={"ref": identity.head_sha},
            )
        except GitHubAcquisitionError as exc:
            if exc.reason == "not_found_or_inaccessible":
                return UnavailableRepositoryFile(
                    path=normalized_path,
                    revision=identity.head_sha,
                    reason=exc.reason,
                    detail=str(exc),
                )
            raise

        try:
            response_type = data["type"]
            response_path = data["path"]
            blob_sha = data["sha"]
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
        if response_path != normalized_path:
            raise GitHubResponseError(
                "GitHub repository-file path does not match the requested path."
            )
        if not isinstance(blob_sha, str) or not blob_sha:
            raise GitHubResponseError(
                "GitHub repository-file field 'sha' must be a non-empty string."
            )
        if encoding != "base64":
            raise GitHubResponseError(
                "GitHub repository-file content must use base64 encoding."
            )
        if not isinstance(encoded_content, str):
            raise GitHubResponseError(
                "GitHub repository-file field 'content' must be text."
            )

        # GitHub inserts line breaks into base64 content. Removing whitespace is
        # safe before strict decoding because base64 itself carries the bytes.
        compact_content = "".join(encoded_content.split())
        try:
            raw_content = base64.b64decode(compact_content, validate=True)
        except (binascii.Error, ValueError) as exc:
            raise GitHubResponseError(
                "GitHub repository-file content was not valid base64."
            ) from exc

        if len(raw_content) > _MAX_TEXT_BYTES:
            raise GitHubResponseError(
                "The repository file exceeds the current bounded text-file limit "
                f"of {_MAX_TEXT_BYTES} bytes."
            )

        try:
            text = raw_content.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise GitHubResponseError(
                "The repository file was not valid UTF-8 text."
            ) from exc

        return RepositoryTextFile(
            path=normalized_path,
            revision=identity.head_sha,
            blob_sha=blob_sha,
            content=text,
        )


def _validate_repository_path(path: str) -> str:
    """Return one safe relative repository path without rewriting its identity."""

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
