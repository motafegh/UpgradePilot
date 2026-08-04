"""Compatibility names for the retired upstream-source resolver generation.

Current architecture separates trusted upstream repository identity from GitHub release
acquisition, interval authority, and semantic claims. New product code imports
``upgradepilot.upstream.repository`` directly. The obsolete ``UpstreamReleaseEvidence``
and ``claim_state='unresolved_claim'`` contract no longer exists.
"""

from .upstream.repository import (
    UpstreamRepositoryEvidence,
    UpstreamRepositoryProblem,
    UpstreamRepositoryResolver,
    UpstreamRepositoryResult,
    normalize_project_url_label,
)

# Narrow migration aliases for callers that used the generic resolver/problem names.
UpstreamSourceResolver = UpstreamRepositoryResolver
UpstreamSourceProblem = UpstreamRepositoryProblem
UpstreamSourceResult = UpstreamRepositoryResult

__all__ = (
    "UpstreamRepositoryEvidence",
    "UpstreamRepositoryProblem",
    "UpstreamRepositoryResolver",
    "UpstreamRepositoryResult",
    "UpstreamSourceProblem",
    "UpstreamSourceResolver",
    "UpstreamSourceResult",
    "normalize_project_url_label",
)
