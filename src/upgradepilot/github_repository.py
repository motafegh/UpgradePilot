"""Acquire repository text at the exact pull-request revision used by CI.

Purpose of this file
--------------------
``github_actions.py`` can prove that a workflow run and its jobs belong to the
pull request's exact ``head_sha``, but GitHub's run/job records do not contain the
complete workflow YAML commands. This module fills that evidence gap.

For a validated ``WorkflowRun``, it first asks GitHub for the run detail that names
the workflow path used by that execution. It then reads that path from the exact
``PullRequestIdentity.head_sha`` through GitHub's contents API.

How this file relates to the rest of UpgradePilot
-------------------------------------------------
Inputs:

* ``PullRequestIdentity`` from ``github_client.py`` supplies the repository and
  immutable head revision;
* ``WorkflowRun`` from ``github_actions.py`` supplies the run/workflow identifiers.

Output:

* ``RepositoryTextFile`` contains validated UTF-8 workflow text and provenance;
* ``UnavailableRepositoryFile`` records an explicit absence/inaccessibility state.

``workflow_commands.py`` consumes available text and extracts the deliberately
supported command forms. ``ci_authority.py`` consumes either union member and
chooses whether the workflow evidence is sufficient, insufficient, or unresolved.

Typical execution flow
----------------------
1. Verify that the supplied run and PR identity share the same head SHA.
2. Fetch run detail to recover the workflow path used by that exact execution.
3. Revalidate run ID, workflow ID, event, and head SHA.
4. Request the file with ``ref=<exact head SHA>``—not a branch name.
5. Validate response identity and encoding.
6. Convert base64 text → bytes → bounded UTF-8 text.
7. Return immutable evidence with path, revision, and blob SHA attached.

This module performs acquisition and decoding only. It does not decide what the
workflow commands mean.
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

# The contents API can return files of arbitrary size. UpgradePilot currently accepts
# at most one million decoded bytes so later text analysis remains explicitly bounded.
_MAX_TEXT_BYTES = 1_000_000


@dataclass(frozen=True, slots=True)
class RepositoryTextFile:
    """Validated UTF-8 repository file with exact-revision provenance.

    ``path`` identifies the repository location, ``revision`` records the commit SHA
    requested from GitHub, and ``blob_sha`` identifies GitHub's content object for
    that file version. Keeping all three beside ``content`` lets later interpretation
    explain precisely which text it examined.
    """

    path: str
    revision: str
    blob_sha: str
    content: str


@dataclass(frozen=True, slots=True)
class UnavailableRepositoryFile:
    """Typed evidence that an exact-revision file was absent or inaccessible.

    GitHub commonly uses HTTP 404 for both true absence and hidden/inaccessible
    resources. This record preserves that ambiguity instead of guessing. It is not
    equivalent to an empty file: the text was unavailable, so later authority logic
    must normally remain unresolved.
    """

    path: str
    revision: str
    reason: str
    detail: str


# The union forces callers to handle the two legitimate acquisition outcomes. A type
# checker can then prevent code from reading ``.content`` without first establishing
# that the result is ``RepositoryTextFile``.
type RepositoryFileEvidence = RepositoryTextFile | UnavailableRepositoryFile


class GitHubRepositoryClient(GitHubApiClient):
    """Read workflow definitions and generic text files at the frozen PR head.

    The base class supplies network/HTTP/JSON handling. This subclass adds repository
    path validation, run-detail reconciliation, exact-revision requests, base64
    decoding, byte bounds, UTF-8 validation, and provenance records.
    """

    def get_exact_head_workflow_file(
        self,
        identity: PullRequestIdentity,
        run: WorkflowRun,
    ) -> RepositoryFileEvidence:
        """Resolve the workflow path used by ``run`` and fetch its exact-head text.

        Goal:
            Obtain the actual workflow definition associated with the validated run,
            rather than whichever version currently exists on the default branch.

        Why two API requests are required:
            The run-detail endpoint tells us the path used by that execution. The
            contents endpoint then returns that path at the frozen PR head revision.
            A current workflow listing could reflect a later rename or edit.
        """

        # Reject a contradictory pair before network access. Evidence from two commits
        # must not be silently joined into one CI-authority assessment.
        if run.head_sha != identity.head_sha:
            raise GitHubResponseError(
                "Cannot acquire a workflow definition for a different head SHA."
            )

        # The exact run detail carries the workflow path tied to this execution.
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

        # ``run_id`` identifies the execution; ``workflow_id`` identifies its workflow
        # definition. Both must reconnect the detailed response to the supplied run.
        if run_id != run.run_id or workflow_id != run.workflow_id:
            raise GitHubResponseError(
                "GitHub workflow-run detail identity does not match the workflow run."
            )

        # Recheck the revision and event because HTTP success alone does not prove that
        # the returned detail belongs to this PR evidence chain.
        if head_sha != identity.head_sha or event != "pull_request":
            raise GitHubResponseError(
                "GitHub workflow-run detail does not match the frozen PR head and event."
            )

        # The current authority rule expects a normal Actions workflow definition.
        # A contradictory path elsewhere in the repository is rejected.
        if not workflow_path.startswith(".github/workflows/"):
            raise GitHubResponseError(
                "GitHub workflow path was outside .github/workflows/."
            )

        # Delegate generic path/request/decoding work after workflow-specific identity
        # has been established.
        return self.get_exact_head_text_file(identity, workflow_path)

    def get_exact_head_text_file(
        self,
        identity: PullRequestIdentity,
        path: str,
    ) -> RepositoryFileEvidence:
        """Fetch, validate, and decode one repository file at ``identity.head_sha``.

        Goal:
            Return trustworthy UTF-8 text whose requested path, returned path, commit
            revision, encoding, and bounded decoded content are all explicit.
        """

        normalized_path = _validate_repository_path(path)

        # URL quoting protects spaces and reserved characters inside path components.
        # ``safe="/"`` deliberately preserves slashes as repository hierarchy
        # separators instead of encoding the entire path as one component.
        encoded_path = quote(normalized_path, safe="/")
        url = self.api_url(
            f"/repos/{identity.repository}/contents/{encoded_path}"
        )

        try:
            data = self._get_json_object(
                url,
                resource="repository-file",
                # A commit SHA is immutable. A branch ref could move between the run
                # acquisition and this file request.
                params={"ref": identity.head_sha},
            )
        except GitHubAcquisitionError as exc:
            if exc.reason == "not_found_or_inaccessible":
                # This optional interpretation input may legitimately be unavailable.
                # Preserve GitHub's ambiguous 404 category as data for the evaluator.
                return UnavailableRepositoryFile(
                    path=normalized_path,
                    revision=identity.head_sha,
                    reason=exc.reason,
                    detail=str(exc),
                )

            # Bare ``raise`` rethrows the same exception and original traceback.
            # Timeouts, rate limits, and other acquisition failures are not converted
            # into ordinary file-unavailability evidence.
            raise

        try:
            # Direct indexing means these members are required. Missing keys become a
            # resource-specific ``GitHubResponseError`` in the handler below.
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

        # The contents endpoint can describe directories and other object shapes. Only
        # a regular file can become text evidence for this function.
        if response_type != "file":
            raise GitHubResponseError(
                "GitHub repository-file response did not describe a regular file."
            )

        # Reconcile GitHub's echoed path with the requested identity. A successful
        # response for another path must not be accepted silently.
        if response_path != normalized_path:
            raise GitHubResponseError(
                "GitHub repository-file path does not match the requested path."
            )
        if not isinstance(blob_sha, str) or not blob_sha:
            raise GitHubResponseError(
                "GitHub repository-file field 'sha' must be a non-empty string."
            )

        # This implementation supports one explicit transport encoding. Rejecting
        # unknown encodings is safer than guessing how to decode them.
        if encoding != "base64":
            raise GitHubResponseError(
                "GitHub repository-file content must use base64 encoding."
            )
        if not isinstance(encoded_content, str):
            raise GitHubResponseError(
                "GitHub repository-file field 'content' must be text."
            )

        # GitHub may wrap base64 with line breaks. ``split()`` without an argument
        # removes all whitespace groups, and joining restores one compact base64 token.
        compact_content = "".join(encoded_content.split())
        try:
            # ``validate=True`` rejects non-base64 characters instead of quietly
            # discarding them and decoding a partially malformed value.
            raw_content = base64.b64decode(compact_content, validate=True)
        except (binascii.Error, ValueError) as exc:
            raise GitHubResponseError(
                "GitHub repository-file content was not valid base64."
            ) from exc

        # The limit applies to real decoded file bytes, not the larger base64 text.
        if len(raw_content) > _MAX_TEXT_BYTES:
            raise GitHubResponseError(
                "The repository file exceeds the current bounded text-file limit "
                f"of {_MAX_TEXT_BYTES} bytes."
            )

        try:
            # The workflow reader consumes Python text, so bytes are decoded under one
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
    """Validate one normalized relative path for GitHub's repository API.

    This is not local filesystem resolution. The function preserves ordinary path
    spelling but rejects forms whose identity is ambiguous or unsafe for the API:
    empty paths, absolute paths, directory-like trailing slashes, repeated separators,
    and the special ``.`` or ``..`` components.
    """

    if not isinstance(path, str):
        raise ValueError("Repository path must be text.")
    normalized = path.strip()

    # Splitting exposes every component so one ``any`` expression can reject empty,
    # current-directory, and parent-directory segments.
    parts = normalized.split("/")
    if (
        not normalized
        or normalized.startswith("/")
        or normalized.endswith("/")
        or any(part in {"", ".", ".."} for part in parts)
    ):
        raise ValueError("Repository path must be a normalized relative file path.")
    return normalized
