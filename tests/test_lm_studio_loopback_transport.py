"""Protect the local LM Studio loopback transport from ambient proxy inheritance."""

from __future__ import annotations

import unittest

from upgradepilot.upstream import support_drop_extractor
from upgradepilot.upstream.support_drop_extractor import (
    LocalSupportDropExtractor,
    build_lm_studio_session,
)


class LMStudioLoopbackTransportTests(unittest.TestCase):
    def test_loopback_session_does_not_trust_environment_proxy_settings(self) -> None:
        session = build_lm_studio_session()
        try:
            self.assertFalse(session.trust_env)
        finally:
            session.close()

    def test_default_extractor_uses_proxy_independent_transport(self) -> None:
        extractor = LocalSupportDropExtractor()
        self.assertIs(
            extractor._post,
            support_drop_extractor._post_without_ambient_proxy,
        )


if __name__ == "__main__":
    unittest.main()
