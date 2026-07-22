# HTTPX 0.28.1 tagged changelog — bounded excerpt

## 0.28.1 (6th December, 2024)

- Fix SSL case where `verify=False` together with client side certificates.

## 0.28.0 (28th November, 2024)

- The deprecated `proxies` argument has now been removed.
- The deprecated `app` argument has now been removed.
- JSON request bodies use a compact representation.
- URL percent escape sets were reviewed.
- `certifi` and `httpcore` are imported only if required.
- `socks5h` is treated as a valid proxy scheme.
- The `Request()` method signature was cleaned up.
- `params={}` now strictly updates instead of merging an existing query string.

Source identity: `encode/httpx`, tag `0.28.1`, `CHANGELOG.md`.
