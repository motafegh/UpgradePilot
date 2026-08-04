"""Compatibility import for upstream interval evidence selection/composition.

New product code imports ``upgradepilot.upstream.interval_evidence``. This flat path
remains only while historical tests and tools migrate during source reconciliation.
"""

from .upstream.interval_evidence import *  # noqa: F401,F403
