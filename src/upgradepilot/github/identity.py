"""GitHub-specific locator and immutable object identity primitives."""

from __future__ import annotations

import re

from ..github_client import UpgradePilotInputError, validate_pull_number, validate_repository

_GIT_OBJECT_ID_PATTERN = re.compile(r"^(?:[0-9a-fA-F]{40}|[0-9a-fA-F]{64})\Z")


def validate_commit_sha(commit_sha: str) -> str:
    """Require one exact 40- or 64-hex immutable Git object identity."""

    if (
        not isinstance(commit_sha, str)
        or _GIT_OBJECT_ID_PATTERN.fullmatch(commit_sha) is None
    ):
        raise ValueError(
            "commit_sha must be a 40- or 64-character hexadecimal object ID."
        )
    return commit_sha


__all__ = (
    "UpgradePilotInputError",
    "validate_commit_sha",
    "validate_pull_number",
    "validate_repository",
)
