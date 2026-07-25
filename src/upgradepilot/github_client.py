"""Acquire and validate public pull-request and changed-file evidence.

This focused module owns GitHub pull-request identity and changed-file records.
Shared HTTP behavior lives in ``github_api``; GitHub Actions evidence lives in
``github_actions``. That separation follows the product flow without splitting
every individual API request into its own file.

The module first validates local locators, then converts successful but untrusted
GitHub JSON into immutable records. It deliberately stops before interpreting
what a changed patch means; that responsibility belongs to ``dependency_change``.
"""

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from .github_api import (
    DEFAULT_TIMEOUT,
    GitHubAcquisitionError,
    GitHubApiClient,
    GitHubResponseError,
    required_bool,
    required_int,
    required_mapping,
    required_nonnegative_int,
    required_str,
)

# GitHub permits up to 100 changed-file records per page. Using the maximum
# reduces requests without changing the completeness checks below.
_CHANGED_FILES_PER_PAGE = 100
# This is a deliberate product bound: beyond it, UpgradePilot abstains rather
# than risk partial evidence from GitHub's changed-file listing limit.
_MAX_CHANGED_FILES = 3_000
# Compile once at import time because the same locator grammar can be reused.
# The pattern accepts the bounded ``owner/repository`` subset supported here,
# rather than attempting to validate every possible GitHub URL or identifier.
_REPOSITORY_PATTERN = re.compile(
    r"^[A-Za-z0-9](?:[A-Za-z0-9_.-]{0,99})/[A-Za-z0-9_.-]{1,100}$"
)


class UpgradePilotInputError(ValueError):
    """The user-supplied repository or pull-request locator is unsupported.

    ``ValueError`` is appropriate because the failure is local and deterministic:
    no GitHub request is needed to know that the supplied value is outside the
    accepted input grammar.
    """


@dataclass(frozen=True, slots=True)
class PullRequestIdentity:
    """Exact proposal identity acquired from one public GitHub pull request.

    Base and head SHAs bind every later evidence lookup to the proposal revision
    observed here. Branch names are not sufficient because they can move.

    ``frozen=True`` prevents accidental mutation after validation, while
    ``slots=True`` keeps the record compact and prevents undeclared attributes.
    """

    repository: str
    number: int
    title: str
    state: str
    merged: bool
    author: str
    base_ref: str
    base_sha: str
    head_ref: str
    head_sha: str
    changed_files: int


@dataclass(frozen=True, slots=True)
class ChangedFile:
    """One validated changed-file record associated with a pull request.

    ``patch`` remains optional because GitHub can omit patch text from an
    otherwise valid file record. Interpretation must preserve that absence.

    An immutable record is returned so later extraction code receives stable
    evidence rather than the original mutable JSON mapping.
    """

    filename: str
    status: str
    additions: int
    deletions: int
    changes: int
    patch: str | None


class GitHubReadClient(GitHubApiClient):
    """Acquire public PR evidence without mutating the target repository.

    Inheriting from ``GitHubApiClient`` reuses one transport/error contract while
    leaving pull-request-specific identity checks in this focused client.
    """

    def get_pull_request(
        self,
        repository: str,
        pull_number: int,
    ) -> PullRequestIdentity:
        """Acquire and validate exact identity for one public pull request.

        Local validation runs before network access so malformed locators fail
        predictably and never become ambiguous GitHub HTTP errors.
        """

        repository = validate_repository(repository)
        pull_number = validate_pull_number(pull_number)
        data = self._get_json_object(
            self.api_url(f"/repos/{repository}/pulls/{pull_number}"),
            resource="pull-request",
        )
        # Parsing is separate from acquisition so deterministic tests can reason
        # about the trust conversion independently of HTTP mechanics.
        return self._parse_pull_request(repository, pull_number, data)

    def get_changed_files(
        self,
        identity: PullRequestIdentity,
    ) -> tuple[ChangedFile, ...]:
        """Acquire every changed file and reconcile the count with PR metadata.

        A successful first page is not complete evidence. Pagination continues
        until the acquired records equal the count already frozen in
        ``PullRequestIdentity``; disagreement is rejected before interpretation.

        A list is used while records are accumulated page by page. Only after
        completeness is proven is it converted to an immutable tuple.
        """

        if identity.changed_files > _MAX_CHANGED_FILES:
            raise GitHubResponseError(
                "The pull request exceeds the current complete changed-file "
                f"acquisition limit of {_MAX_CHANGED_FILES} files."
            )
        # Returning the empty tuple avoids an unnecessary API request while still
        # matching the immutable collection type used for non-empty results.
        if identity.changed_files == 0:
            return ()

        url = self.api_url(
            f"/repos/{identity.repository}/pulls/{identity.number}/files"
        )
        records: list[ChangedFile] = []
        # GitHub pagination is one-based, so the first request uses page 1.
        page = 1

        # The metadata count is the independent completion target. Looping against
        # it prevents a single valid page from being mistaken for the whole change.
        while len(records) < identity.changed_files:
            items = self._get_json_array(
                url,
                resource="changed-file",
                params={"per_page": _CHANGED_FILES_PER_PAGE, "page": page},
            )
            # An empty page cannot add evidence. The final equality check decides
            # whether this was a legitimate end or incomplete acquisition.
            if not items:
                break

            for item_index, item in enumerate(items):
                if not isinstance(item, Mapping):
                    # ``enumerate`` supplies a stable human-facing position; adding
                    # the existing record count makes it global across pages.
                    raise GitHubResponseError(
                        "GitHub changed-file response item "
                        f"{len(records) + item_index + 1} was not an object."
                    )
                records.append(self._parse_changed_file(item))

            # A short page is GitHub's normal end-of-pagination signal. It ends
            # requests, but the metadata reconciliation below remains the proof.
            if len(items) < _CHANGED_FILES_PER_PAGE:
                break
            page += 1

        if len(records) != identity.changed_files:
            raise GitHubResponseError(
                "GitHub pull-request metadata and changed-file acquisition disagree: "
                f"expected {identity.changed_files} records but acquired {len(records)}."
            )
        # Callers receive a fixed evidence collection that cannot be appended to
        # after the completeness invariant has been established.
        return tuple(records)

    @staticmethod
    def _parse_pull_request(
        repository: str,
        pull_number: int,
        data: Mapping[str, Any],
    ) -> PullRequestIdentity:
        """Convert untrusted PR JSON into an exact immutable identity.

        This method does not depend on client state, so ``@staticmethod`` makes
        that independence explicit and keeps the parser directly testable.
        """

        try:
            # Extract nested mappings once so every later field uses the shared
            # runtime validators from the transport boundary.
            base = required_mapping(data, "base")
            head = required_mapping(data, "head")
            user = required_mapping(data, "user")
            number = required_int(data, "number")
            # The URL requested one number; accepting another would bind all later
            # evidence to a different proposal despite an HTTP-success response.
            if number != pull_number:
                raise GitHubResponseError(
                    "GitHub returned a different pull-request number than requested."
                )
            return PullRequestIdentity(
                repository=repository,
                number=number,
                title=required_str(data, "title"),
                state=required_str(data, "state"),
                merged=required_bool(data, "merged"),
                author=required_str(user, "login"),
                base_ref=required_str(base, "ref"),
                base_sha=required_str(base, "sha"),
                head_ref=required_str(head, "ref"),
                head_sha=required_str(head, "sha"),
                changed_files=required_nonnegative_int(data, "changed_files"),
            )
        except KeyError as exc:
            # Indexing validators raise KeyError for absent required fields.
            # Chaining preserves that exact missing-key cause for diagnosis.
            raise GitHubResponseError(
                f"GitHub response is missing required field: {exc.args[0]}."
            ) from exc

    @staticmethod
    def _parse_changed_file(data: Mapping[str, Any]) -> ChangedFile:
        """Convert one untrusted changed-file object into a validated record.

        As above, ``@staticmethod`` is chosen because parsing depends only on the
        supplied JSON object, not on authentication, transport, or mutable state.
        """

        try:
            # ``get`` is intentional here: unlike the required fields below,
            # GitHub may validly omit ``patch``. Missing and JSON null therefore
            # both become ``None`` and remain explicit downstream.
            patch = data.get("patch")
            if patch is not None and not isinstance(patch, str):
                raise GitHubResponseError(
                    "GitHub field 'patch' must be text or absent."
                )
            return ChangedFile(
                filename=required_str(data, "filename"),
                status=required_str(data, "status"),
                additions=required_nonnegative_int(data, "additions"),
                deletions=required_nonnegative_int(data, "deletions"),
                changes=required_nonnegative_int(data, "changes"),
                patch=patch,
            )
        except KeyError as exc:
            raise GitHubResponseError(
                "GitHub changed-file response is missing required field: "
                f"{exc.args[0]}."
            ) from exc


def validate_repository(repository: str) -> str:
    """Return a normalized locator in the supported ``owner/repository`` form.

    Whitespace is removed only at the outer boundary; internal spelling is
    preserved because repository identity is not case-normalized or rewritten.
    ``fullmatch`` is used so every character must belong to the supported grammar.
    """

    normalized = repository.strip()
    if not _REPOSITORY_PATTERN.fullmatch(normalized):
        raise UpgradePilotInputError(
            "Repository must use the supported 'owner/repository' form."
        )
    return normalized


def validate_pull_number(pull_number: int) -> int:
    """Return a positive PR number while rejecting booleans as integers.

    The explicit boolean check is necessary because Python's ``bool`` subclasses
    ``int``; without it, ``True`` would be accepted as pull-request number 1.
    """

    if (
        isinstance(pull_number, bool)
        or not isinstance(pull_number, int)
        or pull_number < 1
    ):
        raise UpgradePilotInputError("Pull-request number must be a positive integer.")
    return pull_number


# Keep the timeout name available here for readers/tests that associate it with
# the public-PR client, while the actual transport setting is owned by github_api.
# This is a compatibility alias, not an independent timeout configuration.
_DEFAULT_TIMEOUT = DEFAULT_TIMEOUT
