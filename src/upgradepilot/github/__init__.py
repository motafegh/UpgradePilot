"""GitHub-specific identity, acquisition, and exact-revision evidence boundaries."""

from .pull_request import ChangedFile, GitHubPullRequestClient, PullRequestIdentity

__all__ = ("ChangedFile", "GitHubPullRequestClient", "PullRequestIdentity")
