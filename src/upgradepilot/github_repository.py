"""Acquire exact-revision repository text files for CI interpretation.

GitHub Actions run records tell UpgradePilot which workflow executed, but they do
not contain the workflow commands themselves. This module closes that factual
acquisition gap by reading the workflow definition from the exact pull-request
head SHA already frozen in ``PullRequestIdentity``.

The module performs no CI interpretation. It only converts one GitHub contents
API response into either validated UTF-8 text or an explicit unavailable state.
This keeps repository acquisition separate from later questions about what the
workflow commands prove.
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

# The contents endpoint can return arbitrary repository files. This product bound
# limits which decoded text files UpgradePilot accepts for deterministic analysis.
_MAX_TEXT_BYTES = 1_000_000


@dataclass(frozen=True, slots=True)
class RepositoryTextFile:
    """One UTF-8 repository file bound to an exact commit revision.

    ``revision`` records which commit supplied the content, while ``blob_sha``
    identifies GitHub's content object for that file. The frozen record keeps this
    provenance attached to the text throughout later interpretation.
    """

    path: str
    revision: str
    blob_sha: str
    content: str


@dataclass(frozen=True, slots=True)
class UnavailableRepositoryFile:
    """An exact-revision file that GitHub reported as absent or inaccessible.

    This is a normal evidence state for an optional interpretation input. Keeping
    the path, revision, stable reason, and detail allows later logic to abstain
    transparently rather than treating missing evidence as empty content.
    """

    path: str
    revision: str
    reason: str
    detail: str


# Unavailability is evidence, not an exception, when GitHub returns its ambiguous
# 404 for one optional interpretation input. Other acquisition failures propagate.
# The union type requires callers to handle both validated text and explicit
# unavailability rather than assuming every request produced readable content.
type RepositoryFileEvidence = RepositoryTextFile | UnavailableRepositoryFile


class GitHubRepositoryClient(GitHubApiClient):
    """Acquire workflow definitions and repository files at the frozen PR head.

    The shared base class owns HTTP and top-level JSON validation. This client adds
    repository-path, exact-revision, content-encoding, and provenance checks.
    """

    def get_exact_head_workflow_file(
        self,
        identity: PullRequestIdentity,
        run: WorkflowRun,
    ) -> RepositoryFileEvidence:
        """Resolve the run's workflow path and read it at the exact PR head.

        The method deliberately performs two acquisitions: run detail establishes
        the path used by that execution, then the contents endpoint returns that
        path at the frozen head revision. This is stronger than reading whichever
        workflow file currently exists on the default branch.
        """

        # Reject inconsistent already-validated inputs before network access. A run
        # from another revision must never be joined to this PR's repository files.
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
            # These fields jointly reconnect the detailed response to the
            # previously validated run and frozen pull-request identity.
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

        # Both identifiers are checked: a workflow definition can have many runs,
        # and one run ID must not be paired with another workflow's metadata.
        if run_id != run.run_id or workflow_id != run.workflow_id:
            raise GitHubResponseError(
                "GitHub workflow-run detail identity does not match the workflow run."
            )
        # HTTP success is insufficient if the detail belongs to another commit or
        # was triggered by an event outside this pull-request evidence boundary.
        if head_sha != identity.head_sha or event != "pull_request":
            raise GitHubResponseError(
                "GitHub workflow-run detail does not match the frozen PR head and event."
            )
        # The current authority rule expects an ordinary repository workflow file,
        # not an arbitrary path returned by a contradictory response.
        if not workflow_path.startswith(".github/workflows/"):
            raise GitHubResponseError(
                "GitHub workflow path was outside .github/workflows/."
            )
        # Reuse the generic exact-head file reader after workflow-specific identity
        # and path checks have been completed.
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
        # URL-encode characters inside each path component while preserving ``/``
        # as the repository hierarchy separator expected by the contents endpoint.
        encoded_path = quote(normalized_path, safe="/")
        url = self.api_url(
            f"/repos/{identity.repository}/contents/{encoded_path}"
        )

        try:
            data = self._get_json_object(
                url,
                resource="repository-file",
                # A commit SHA is used instead of a branch so the acquired content
                # cannot move between the workflow run and this request.
                params={"ref": identity.head_sha},
            )
        except GitHubAcquisitionError as exc:
            if exc.reason == "not_found_or_inaccessible":
                # GitHub's 404 intentionally combines absence and inaccessibility.
                # For this optional evidence input, preserve that ambiguity as a
                # typed result instead of inventing a more specific explanation.
                return UnavailableRepositoryFile(
                    path=normalized_path,
                    revision=identity.head_sha,
                    reason=exc.reason,
                    detail=str(exc),
                )
            # A bare ``raise`` rethrows the same acquisition exception with its
            # original traceback; timeouts and other HTTP failures are not normal
            # file-unavailability evidence.
            raise

        try:
            # Direct indexing marks these response members as required. Their
            # individual value types and semantic identities are checked below.
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

        # The contents endpoint may also describe directories or other object
        # shapes; only an ordinary file is valid for text interpretation.
        if response_type != "file":
            raise GitHubResponseError(
                "GitHub repository-file response did not describe a regular file."
            )
        # Reconcile the echoed path so a successful response for another resource
        # cannot silently become evidence for the requested file.
        if response_path != normalized_path:
            raise GitHubResponseError(
                "GitHub repository-file path does not match the requested path."
            )
        if not isinstance(blob_sha, str) or not blob_sha:
            raise GitHubResponseError(
                "GitHub repository-file field 'sha' must be a non-empty string."
            )
        # This implementation has one explicit decoding contract. Other encodings
        # are rejected rather than guessed or silently passed through.
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
        # ``split`` without an argument removes all whitespace groups; joining the
        # pieces produces the compact alphabet expected by strict validation.
        compact_content = "".join(encoded_content.split())
        try:
            # ``validate=True`` rejects non-base64 characters instead of accepting
            # a partially malformed representation.
            raw_content = base64.b64decode(compact_content, validate=True)
        except (binascii.Error, ValueError) as exc:
            raise GitHubResponseError(
                "GitHub repository-file content was not valid base64."
            ) from exc

        # Measure decoded bytes rather than encoded characters because the bound
        # applies to the actual file accepted for downstream processing.
        if len(raw_content) > _MAX_TEXT_BYTES:
            raise GitHubResponseError(
                "The repository file exceeds the current bounded text-file limit "
                f"of {_MAX_TEXT_BYTES} bytes."
            )

        try:
            # Decode explicitly as UTF-8 so later parsers receive text under one
            # deterministic character-encoding contract.
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
    """Return one safe relative repository path without rewriting its identity.

    This validates an API repository path, not a local filesystem path. Outer
    whitespace is removed, but path components are otherwise preserved so the
    requested identity remains exact.
    """

    if not isinstance(path, str):
        raise ValueError("Repository path must be text.")
    normalized = path.strip()
    # Splitting once allows the same condition to reject repeated separators and
    # the special ``.``/``..`` components that would make identity ambiguous.
    parts = normalized.split("/")
    if (
        not normalized
        or normalized.startswith("/")
        or normalized.endswith("/")
        or any(part in {"", ".", ".."} for part in parts)
    ):
        raise ValueError("Repository path must be a normalized relative file path.")
    return normalized
