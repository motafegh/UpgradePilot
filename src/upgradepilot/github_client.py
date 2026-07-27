"""Acquire the pull-request identity and complete changed-file evidence.

Purpose of this file
--------------------
This module is the first GitHub-specific stage used by ``cli.py``. Given the two
user inputs—an ``owner/repository`` locator and a pull-request number—it produces:

* ``PullRequestIdentity``: the exact PR, base commit, head commit, and declared
  changed-file count;
* a tuple of ``ChangedFile`` records: every changed file GitHub associates with
  that PR.

How this file relates to the rest of UpgradePilot
-------------------------------------------------
``GitHubReadClient`` inherits the reusable HTTP/JSON operations from
``GitHubApiClient`` in ``github_api.py``. This file adds the meaning that the
shared transport layer deliberately does not know: PR fields, changed-file fields,
PR-number identity checks, and pagination completeness.

The resulting records then move in two directions:

* ``dependency_change.py`` inspects ``ChangedFile.patch`` values to decide whether
  the PR proves one supported pinned dependency update;
* ``github_actions.py`` and ``github_repository.py`` use the frozen
  ``PullRequestIdentity.head_sha`` to acquire CI evidence for the exact proposal
  revision rather than for a branch name that may later move.

Typical execution flow
----------------------
1. ``cli.py`` calls ``get_pull_request(repository, pull_number)``.
2. Local input validators reject unsupported locators before network access.
3. ``github_api.py`` performs the GET, HTTP classification, and top-level JSON check.
4. ``_parse_pull_request`` validates fields and builds ``PullRequestIdentity``.
5. ``cli.py`` passes that identity to ``get_changed_files``.
6. Every page and every item is validated, then the acquired count is reconciled
   with the PR metadata before an immutable tuple is returned.

This module acquires and validates evidence; it does not decide what the patch
means or whether the proposed upgrade is safe.
"""

# Postponed annotations allow type hints to refer to classes without forcing Python
# to resolve every annotation immediately when this module is imported.
from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from .github_api import (
    DEFAULT_TIMEOUT,
    # These error names remain importable from ``github_client`` for existing
    # callers/tests, although their implementation is owned by ``github_api.py``.
    GitHubAcquisitionError,
    GitHubApiClient,
    GitHubResponseError,
    required_bool,
    required_int,
    required_mapping,
    required_nonnegative_int,
    required_str,
)

# GitHub's changed-files endpoint supports at most 100 records per page. Requesting
# the maximum minimizes HTTP calls; it does not replace the count reconciliation in
# ``get_changed_files``.
_CHANGED_FILES_PER_PAGE = 100

# UpgradePilot requires complete changed-file evidence. This bound matches the
# current acquisition boundary: a larger PR is rejected instead of being analyzed
# from a silently partial file list.
_MAX_CHANGED_FILES = 3_000

# Supported user input is one plain ``owner/repository`` locator, not a URL. The
# compiled regex is reused by every validation call. ``fullmatch`` later requires
# the entire string—not merely a valid-looking substring—to follow this grammar.
_REPOSITORY_PATTERN = re.compile(
    r"^[A-Za-z0-9](?:[A-Za-z0-9_.-]{0,99})/[A-Za-z0-9_.-]{1,100}$"
)


class UpgradePilotInputError(ValueError):
    """The supplied PR locator is outside the supported local input grammar.

    This error is different from ``GitHubAcquisitionError``: it can be established
    without contacting GitHub. ``cli.py`` catches it and returns exit status 2,
    while network/HTTP acquisition failures use exit status 3.

    ``ValueError`` is suitable because the Python value exists, but its content or
    range is invalid for this operation.
    """


@dataclass(frozen=True, slots=True)
class PullRequestIdentity:
    """Trusted identity and revision boundary for one GitHub pull request.

    This record is created only after ``_parse_pull_request`` validates the GitHub
    response and confirms that its ``number`` equals the requested PR number.

    Why both branch names and SHAs are stored:

    * ``base_ref`` and ``head_ref`` are useful human-readable branch names;
    * ``base_sha`` and ``head_sha`` identify exact commits and cannot move.

    Later CI acquisition uses ``head_sha`` so workflow evidence belongs to the same
    proposal revision observed here. ``changed_files`` becomes the independent
    completeness target used by ``get_changed_files``.

    ``frozen=True`` prevents mutation after trust has been established. ``slots=True``
    gives the record a fixed field set and prevents accidental new attributes.
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
    """Validated metadata and optional patch text for one PR-changed file.

    ``dependency_change.py`` consumes these records. In particular, it compares the
    additions/deletions reported here with the visible diff lines in ``patch`` before
    trusting a dependency interpretation.

    ``patch`` is ``str | None`` because GitHub can omit patch text even when the rest
    of the file record is valid. ``None`` is therefore preserved as missing evidence;
    it must not be converted to an empty string, which would falsely mean that GitHub
    supplied an empty patch.
    """

    filename: str
    status: str
    additions: int
    deletions: int
    changes: int
    patch: str | None


class GitHubReadClient(GitHubApiClient):
    """Read PR identity and changed files using the shared GitHub API foundation.

    Inheritance supplies ``api_url``, ``_get_json_object``, ``_get_json_array``,
    authentication headers, timeouts, and common error classification. This subclass
    supplies PR-specific endpoints, pagination, field validation, and domain records.

    The class is read-only: every operation uses GET and never modifies the target
    repository or pull request.
    """

    def get_pull_request(
        self,
        repository: str,
        pull_number: int,
    ) -> PullRequestIdentity:
        """Acquire one PR and convert its response into an exact identity record.

        Goal:
            Establish the proposal identity that every later evidence lookup will
            use, especially the exact ``head_sha`` and declared changed-file count.

        Process:
            1. validate both user inputs locally;
            2. request ``/repos/{repository}/pulls/{pull_number}``;
            3. require an object-shaped JSON response through ``github_api.py``;
            4. parse and semantically bind the returned PR number to the request.
        """

        # Reassign the validated values so every later line in this function uses the
        # normalized/approved input rather than the original caller-provided strings.
        repository = validate_repository(repository)
        pull_number = validate_pull_number(pull_number)

        # ``api_url`` belongs to the base class. ``_get_json_object`` then performs
        # transport, HTTP-status, JSON-decoding, and top-level object validation.
        data = self._get_json_object(
            self.api_url(f"/repos/{repository}/pulls/{pull_number}"),
            resource="pull-request",
        )

        # Keep field parsing separate from HTTP acquisition. The parser can focus on
        # the trust conversion from untrusted JSON to ``PullRequestIdentity``.
        return self._parse_pull_request(repository, pull_number, data)

    def get_changed_files(
        self,
        identity: PullRequestIdentity,
    ) -> tuple[ChangedFile, ...]:
        """Acquire and validate the complete changed-file collection for one PR.

        Goal:
            Return every changed-file record associated with ``identity``—never a
            successful-looking partial first page.

        Why ``identity`` is passed instead of repository/number separately:
            The already-validated record keeps the repository, PR number, and expected
            count together. The caller cannot accidentally combine a locator from one
            PR with the count from another.

        Completeness rule:
            GitHub's PR response declared ``identity.changed_files``. Pagination may
            stop on an empty page or a short page, but the final proof is exact count
            equality: ``len(records) == identity.changed_files``.

        The function builds a mutable ``list`` because records arrive incrementally,
        then converts it to an immutable ``tuple`` only after completeness is proven.
        """

        # The product currently refuses evidence sets beyond this complete-acquisition
        # boundary. Continuing would risk interpreting a truncated collection.
        if identity.changed_files > _MAX_CHANGED_FILES:
            raise GitHubResponseError(
                "The pull request exceeds the current complete changed-file "
                f"acquisition limit of {_MAX_CHANGED_FILES} files."
            )

        # A declared count of zero is already complete evidence; no files endpoint
        # request is needed. ``()`` is the empty value of the promised tuple type.
        if identity.changed_files == 0:
            return ()

        url = self.api_url(
            f"/repos/{identity.repository}/pulls/{identity.number}/files"
        )
        records: list[ChangedFile] = []

        # GitHub REST page numbers are one-based, so acquisition starts at page 1.
        page = 1

        # Continue while the validated records are fewer than the metadata target.
        # This condition prevents an unnecessary extra page once equality is reached.
        while len(records) < identity.changed_files:
            # This endpoint returns a top-level JSON array, unlike the PR endpoint's
            # top-level object. Each item remains untrusted until checked below.
            items = self._get_json_array(
                url,
                resource="changed-file",
                params={"per_page": _CHANGED_FILES_PER_PAGE, "page": page},
            )

            # No more items can be learned from an empty page. Breaking does not call
            # the collection complete; the exact-count check after the loop decides.
            if not items:
                break

            for item_index, item in enumerate(items):
                # ``_get_json_array`` proved only that the outer container is a list.
                # Every element must independently be a dictionary-like JSON object.
                if not isinstance(item, Mapping):
                    # ``enumerate`` supplies the page-local zero-based index. Adding
                    # the previous record count and 1 produces a human-facing global
                    # position across all pages.
                    raise GitHubResponseError(
                        "GitHub changed-file response item "
                        f"{len(records) + item_index + 1} was not an object."
                    )
                records.append(self._parse_changed_file(item))

            # A short page is GitHub's ordinary signal that no later page should exist.
            # It is only a stopping signal; metadata equality remains the proof.
            if len(items) < _CHANGED_FILES_PER_PAGE:
                break
            page += 1

        # Reject both under-acquisition and any inconsistent over-acquisition. A later
        # interpreter must never receive a tuple whose completeness is uncertain.
        if len(records) != identity.changed_files:
            raise GitHubResponseError(
                "GitHub pull-request metadata and changed-file acquisition disagree: "
                f"expected {identity.changed_files} records but acquired {len(records)}."
            )

        # Freeze the now-complete collection before passing it to
        # ``extract_pinned_dependency_change`` in ``dependency_change.py``.
        return tuple(records)

    @staticmethod
    def _parse_pull_request(
        repository: str,
        pull_number: int,
        data: Mapping[str, Any],
    ) -> PullRequestIdentity:
        """Validate one PR JSON object and build ``PullRequestIdentity``.

        Goal:
            Cross the trust boundary from a structurally object-shaped response to a
            domain record whose required fields and requested identity are validated.

        ``@staticmethod`` is used because parsing requires only the explicit arguments;
        it does not read the client's session, token, headers, or timeout. That makes
        the function conceptually separate from network state and directly testable.
        """

        try:
            # ``base``, ``head``, and ``user`` are nested JSON objects. The shared
            # validator proves their object shape before inner keys are accessed.
            base = required_mapping(data, "base")
            head = required_mapping(data, "head")
            user = required_mapping(data, "user")
            number = required_int(data, "number")

            # A successful response is still contradictory evidence if it identifies
            # another PR. The requested number and returned number must be identical.
            if number != pull_number:
                raise GitHubResponseError(
                    "GitHub returned a different pull-request number than requested."
                )

            # Constructing the frozen dataclass is the final step of validation. The
            # raw dictionaries are not exposed to the rest of the application.
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
            # The ``required_*`` helpers intentionally use ``data[key]``. A missing
            # required key raises ``KeyError`` here, where the PR-specific parser can
            # translate it into a clearer response-evidence error.
            #
            # ``exc.args[0]`` is the missing key, and ``raise ... from exc`` preserves
            # the original KeyError as the underlying cause for debugging.
            raise GitHubResponseError(
                f"GitHub response is missing required field: {exc.args[0]}."
            ) from exc

    @staticmethod
    def _parse_changed_file(data: Mapping[str, Any]) -> ChangedFile:
        """Validate one changed-file JSON object and build ``ChangedFile``.

        Goal:
            Preserve the exact per-file metadata needed by ``dependency_change.py``
            while distinguishing required fields from optional patch evidence.

        This is also a ``@staticmethod`` because parsing depends only on the supplied
        JSON object and shared validators, not on client state.
        """

        try:
            # ``patch`` is the deliberate exception to required-key access. GitHub may
            # omit it, so ``get`` returns ``None`` for both an absent key and JSON null.
            # Downstream interpretation treats that state as unavailable evidence.
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
            # Missing required file metadata is different from a validly absent patch.
            # The former makes the GitHub response untrustworthy and stops acquisition.
            raise GitHubResponseError(
                "GitHub changed-file response is missing required field: "
                f"{exc.args[0]}."
            ) from exc


def validate_repository(repository: str) -> str:
    """Validate and return the supported ``owner/repository`` locator.

    Goal:
        Reject malformed or unsupported repository locators before any HTTP request.
        ``cli.py`` reports such failures as input errors rather than ambiguous GitHub
        acquisition failures.

    ``strip`` removes only accidental outer whitespace. The internal spelling and
    case are preserved because this function validates identity; it does not rewrite
    it. ``fullmatch`` requires every remaining character to follow the compiled
    owner/repository grammar.
    """

    normalized = repository.strip()
    if not _REPOSITORY_PATTERN.fullmatch(normalized):
        raise UpgradePilotInputError(
            "Repository must use the supported 'owner/repository' form."
        )
    return normalized


def validate_pull_number(pull_number: int) -> int:
    """Validate and return a positive integer pull-request number.

    Goal:
        Stop unsupported values locally before constructing a GitHub endpoint.

    Python's ``bool`` is a subclass of ``int``, so ``isinstance(True, int)`` is true.
    The explicit boolean check must therefore occur alongside the integer/range checks
    or ``True`` would incorrectly become PR number 1.
    """

    if (
        isinstance(pull_number, bool)
        or not isinstance(pull_number, int)
        or pull_number < 1
    ):
        raise UpgradePilotInputError("Pull-request number must be a positive integer.")
    return pull_number


# ``DEFAULT_TIMEOUT`` is implemented and consumed by the inherited transport in
# ``github_api.py``. This alias keeps the historical name available from this module
# for readers/tests without creating a second timeout configuration.
_DEFAULT_TIMEOUT = DEFAULT_TIMEOUT
