"""GitHub-specific locator and immutable object identity primitives."""

from __future__ import annotations

import re

from ..github_client import UpgradePilotInputError, validate_pull_number, validate_repository

_COMMIT_SHA_PATTERN = re.compile(r"^[0-9a-f]{40}$")


def validate_commit_sha(commit_sha: str) -> str:
    """Require one lowercase immutable 40-hex Git commit identity."""

    if not isinstance(commit_sha, str) or _COMMIT_SHA_PATTERN.fullmatch(commit_sha) is None:
        raise UpgradePilotInputError(
            "Git commit identity must be exactly 40 lowercase hexadecimal characters."
        )
    return commit_sha


__all__ = (
    "UpgradePilotInputError",
    "validate_commit_sha",
    "validate_pull_number",
    "validate_repository",
)
