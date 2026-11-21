"""Protect the local LM Studio transport boundary."""

from __future__ import annotations

import unittest
from unittest.mock import patch

from requests import Response, Session

from test_support_drop_extractor import _positive_content, _response, _window
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

    def test_default_extractor_disables_redirects_and_reports_unresolved(self) -> None:
        response = Response()
        response.status_code = 307
        with patch.object(Session, "post", autospec=True, return_value=response) as post:
            result = LocalSupportDropExtractor().extract(_window(_positive_content()))

        post.assert_called_once()
        self.assertFalse(post.call_args.args[0].trust_env)
        self.assertIs(post.call_args.kwargs["allow_redirects"], False)
        self.assertEqual(result.state, "unresolved")
        self.assertIn("307", result.detail)

    def test_default_extractor_accepts_a_direct_local_response(self) -> None:
        response = _response({
            "candidates": [],
            "unresolved_if_no_candidates": False,
            "detail": "",
        })
        with patch.object(Session, "post", autospec=True, return_value=response):
            result = LocalSupportDropExtractor().extract(_window(_positive_content()))

        self.assertEqual(result.state, "no_relevant_claim")


if __name__ == "__main__":
    unittest.main()
