"""Validate the localhost-only proxy isolation used by the Step 6C smoke runner."""

from __future__ import annotations

import unittest

from tools.run_step6c_support_drop_smoke import build_localhost_http_environment


class Step6CLocalHttpRunnerTests(unittest.TestCase):
    def test_proxy_variables_are_removed_from_child_environment(self) -> None:
        source = {
            "HTTP_PROXY": "http://127.0.0.1:8118",
            "HTTPS_PROXY": "http://127.0.0.1:8118",
            "ALL_PROXY": "socks5://127.0.0.1:9050",
            "http_proxy": "http://proxy.example",
            "https_proxy": "http://proxy.example",
            "all_proxy": "socks5://proxy.example",
            "PATH": "/usr/bin",
        }

        result = build_localhost_http_environment(source)

        for key in (
            "HTTP_PROXY",
            "HTTPS_PROXY",
            "ALL_PROXY",
            "http_proxy",
            "https_proxy",
            "all_proxy",
        ):
            self.assertNotIn(key, result)
        self.assertEqual(result["PATH"], "/usr/bin")

    def test_loopback_is_explicitly_excluded_from_proxying(self) -> None:
        result = build_localhost_http_environment({"NO_PROXY": "example.com"})

        self.assertEqual(result["NO_PROXY"], "127.0.0.1,localhost,::1")
        self.assertEqual(result["no_proxy"], "127.0.0.1,localhost,::1")


if __name__ == "__main__":
    unittest.main()
