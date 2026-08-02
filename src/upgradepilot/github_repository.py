"""Acquire bounded repository text at immutable GitHub revisions.

Purpose of this file
--------------------
The module serves three exact-revision evidence paths:

* existing workflow and target-Python readers acquire validated text at the exact PR
  head revision used by the current CLI;
* dependency-file readers acquire complete text explicitly at the PR base or head and
  preserve stricter path, blob, reported-size, decoded-size, and UTF-8 evidence;
* Step 5C upstream acquisition reads one explicit repository path at an already resolved
  immutable commit SHA so tagged changelog evidence can be tied to the exact source tree
  named by a Git version tag.

``github_actions.py`` can prove that a workflow run and its jobs belong to the pull
request's exact ``head_sha``, but run/job records do not contain complete workflow YAML.
For a validated ``WorkflowRun``, this module resolves the workflow path from run detail
and reads that path from the exact head SHA through GitHub's contents API.

Structured dependency files require a different acquisition shape. A patch may be
incomplete or unsuitable for structural comparison, so explicit
``get_pull_request_base_file`` and ``get_pull_request_head_file`` methods read complete
text at immutable PR revisions and require GitHub's reported byte count to agree with
the decoded bytes before returning evidence.

Step 5C reuses that strict complete-file mechanism through
``get_exact_commit_text_file``. The caller must already know the immutable commit SHA;
this module does not resolve branches, tags, releases, or semantic changelog meaning.

How this file relates to the rest of UpgradePilot
-------------------------------------------------
Inputs:

* ``PullRequestIdentity`` supplies the repository and immutable base/head revisions;
* ``WorkflowRun`` supplies run/workflow identifiers for workflow-definition lookup;
* Step 5B ``GitHubTagCommitEvidence`` supplies the immutable commit later passed to the
  generic exact-commit reader.

Outputs:

* ``RepositoryTextFile`` preserves the existing exact-head text contract;
* ``ExactRepositoryTextFile`` preserves stricter exact-revision file evidence;
* ``UnavailableRepositoryFile`` records explicit absence/inaccessibility.

This module performs acquisition, identity reconciliation, decoding, and byte-bound
validation only. It does not parse dependency files, interpret workflow commands,
construct tagged-changelog authority, or decide compatibility, safety, or maintainer
action.
"""

from __future__ import annotations

import base64
import binascii
import re
from dataclasses import dataclass
from urllib.parse import quote

from .github_actions import WorkflowRun
from .github_api import (
    GitHubAcquisitionError,
    GitHubApiClient,
    GitHubResponseError,
    required_nonnegative_int,
    required_positive_int,
    required_str,
)
from .github_client import PullRequestIdentity, validate_repository

# The contents API can return files of arbitrary size. UpgradePilot accepts at most one
# million decoded bytes so later text analysis remains explicitly bounded. The strict
# exact-revision path validates GitHub's reported size before decoding and the actual
# decoded size again afterward.
_MAX_TEXT_BYTES = 1_000_000

# GitHub repositories currently expose SHA-1 commit IDs as 40 hexadecimal characters.
# Accept 64 hexadecimal characters as well so the API names the invariant we actually
# need—an immutable object identifier—without accepting movable refs such as ``main``.
_COMMIT_SHA = re.compile(r"^(?:[0-9a-fA-F]{40}|[0-9a-fA-F]{64})\Z")


@dataclass(frozen=True, slots=True)
class RepositoryTextFile:
    """Validated UTF-8 repository file with exact-revision provenance.

    This is the existing workflow/target contract. ``path`` identifies the repository
    location, ``revision`` records the commit SHA requested from GitHub, and
    ``blob_sha`` identifies GitHub's content object for that file version.
    """

    path: str
    revision: str
    blob_sha: str
    content: str


@dataclass(frozen=True, slots=True)
class ExactRepositoryTextFile:
    """Complete UTF-8 file bound to one exact revision and byte evidence.

    ``path`` is the normalized path requested by UpgradePilot. ``returned_path`` is the
    path echoed by GitHub and is retained even though acquisition requires both values
    to match. ``reported_byte_count`` comes from the contents response;
    ``decoded_byte_count`` comes from the actual Base64-decoded bytes. A successful
    record exists only when those counts agree and remain within the configured bound.

    The record proves file acquisition identity only. It does not say what the text
    means or whether the file establishes a dependency change or changelog claim.
    """

    repository: str
    path: str
    returned_path: str
    revision: str
    blob_sha: str
    reported_byte_count: int
    decoded_byte_count: int
    content: str


@dataclass(frozen=True, slots=True)
class UnavailableRepositoryFile:
    """Typed evidence that an exact-revision file was absent or inaccessible.

    GitHub commonly uses HTTP 404 for both true absence and hidden/inaccessible
    resources. This record preserves that ambiguity instead of guessing. It is not
    equivalent to an empty file: text was unavailable, so later interpretation must
    normally remain unresolved or produce an explicit file-unavailable problem.

    ``repository`` is optional to preserve the existing workflow/target construction
    contract. The strict exact-revision methods populate it.
    """

    path: str
    revision: str
    reason: str
    detail: str
    repository: str | None = None


# Existing workflow and target callers use the first union. Strict dependency/changelog
# acquisition uses the second union. Both force callers to narrow unavailable evidence
# before reading text fields.
type RepositoryFileEvidence = RepositoryTextFile | UnavailableRepositoryFile
type ExactRepositoryFileEvidence = ExactRepositoryTextFile | UnavailableRepositoryFile


class GitHubRepositoryClient(GitHubApiClient):
    """Read validated text at explicitly immutable repository revisions.

    The base class supplies network, HTTP, and top-level JSON handling. This subclass
    adds repository-path validation, workflow-run reconciliation, exact-revision
    requests, Base64 decoding, reported/decoded byte checks, UTF-8 validation, and
    immutable provenance records.
    """

    def get_pull_request_base_file(
        self,
        identity: PullRequestIdentity,
        path: str,
    ) -> ExactRepositoryFileEvidence:
        """Acquire one complete file at the pull request's immutable base SHA."""

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
        """Acquire one complete file at the pull request's immutable head SHA."""

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
        """Acquire one complete UTF-8 file at an explicit immutable commit SHA.

        Unlike the PR helpers, this operation is repository-generic and therefore
        validates that ``commit_sha`` is a hexadecimal object ID rather than a movable
        ref name. It does not prove that a tag resolves to this commit; Step 5B owns
        that fact and supplies the value consumed here.
        """

        repository = validate_repository(repository)
        commit_sha = _validate_commit_sha(commit_sha)
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
        """Resolve the workflow path used by ``run`` and fetch its exact-head text.

        The run-detail endpoint names the workflow path used by that execution. The
        contents endpoint then returns that path at the frozen PR head revision. A
        current workflow listing could reflect a later rename or edit.
        """

        # Reject a contradictory pair before network access. Evidence from two commits
        # must not be silently joined into one CI-authority assessment.
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
        """Preserve the existing exact-head workflow/target text contract."""

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

        raw_content = _decode_base64_repository_content(encoded_content)
        if len(raw_content) > _MAX_TEXT_BYTES:
            raise GitHubResponseError(
                "The repository file exceeds the current bounded text-file limit "
                f"of {_MAX_TEXT_BYTES} bytes."
            )

        text = _decode_utf8_repository_content(raw_content)
        return RepositoryTextFile(
            path=normalized_path,
            revision=identity.head_sha,
            blob_sha=blob_sha,
            content=text,
        )

    def _get_exact_pull_request_text_file(
        self,
        identity: PullRequestIdentity,
        path: str,
        *,
        revision: str,
    ) -> ExactRepositoryFileEvidence:
        """Acquire strict complete-file evidence at exactly the PR base or head SHA."""

        # This guard preserves the original PR-specific authority: these helpers cannot
        # be repurposed as arbitrary historical-file readers merely because the shared
        # exact-revision implementation now also serves Step 5C.
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
        """Acquire strict complete-file evidence at one already-approved revision."""

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

        # Reported size is checked before Base64 work. An oversized file therefore
        # cannot consume decoding memory merely because its encoded content is present.
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

        # Agreement is required before text interpretation. A response that reports one
        # size but decodes to another cannot become exact file evidence.
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

        text = _decode_utf8_repository_content(raw_content)
        return ExactRepositoryTextFile(
            repository=repository,
            path=normalized_path,
            returned_path=returned_path,
            revision=revision,
            blob_sha=blob_sha,
            reported_byte_count=reported_byte_count,
            decoded_byte_count=decoded_byte_count,
            content=text,
        )


def _decode_base64_repository_content(encoded_content: str) -> bytes:
    """Decode GitHub's line-wrapped Base64 text under one strict grammar."""

    compact_content = "".join(encoded_content.split())
    try:
        return base64.b64decode(compact_content, validate=True)
    except (binascii.Error, ValueError) as exc:
        raise GitHubResponseError(
            "GitHub repository-file content was not valid base64."
        ) from exc


def _decode_utf8_repository_content(raw_content: bytes) -> str:
    """Decode repository bytes as deterministic UTF-8 text."""

    try:
        return raw_content.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise GitHubResponseError(
            "The repository file was not valid UTF-8 text."
        ) from exc


def _validate_repository_path(path: str) -> str:
    """Validate one normalized relative path for GitHub's repository API.

    This is not local filesystem resolution. The function preserves ordinary path
    spelling but rejects forms whose identity is ambiguous or unsafe for the API:
    empty paths, absolute paths, directory-like trailing slashes, repeated separators,
    and the special ``.`` or ``..`` components.
    """

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


def _validate_commit_sha(commit_sha: str) -> str:
    """Require an immutable hexadecimal Git object identifier, never a movable ref."""

    if not isinstance(commit_sha, str) or _COMMIT_SHA.fullmatch(commit_sha) is None:
        raise ValueError("commit_sha must be a 40- or 64-character hexadecimal SHA.")
    return commit_sha.lower()
