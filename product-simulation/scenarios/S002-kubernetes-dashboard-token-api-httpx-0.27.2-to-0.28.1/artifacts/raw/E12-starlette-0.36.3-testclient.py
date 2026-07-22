# Bounded source excerpt: Kludex/starlette tag 0.36.3

class TestClient(httpx.Client):
    def __init__(self, app, base_url="http://testserver", ...):
        ...
        transport = _TestClientTransport(self.app, ...)
        ...
        super().__init__(
            app=self.app,
            base_url=base_url,
            headers=headers,
            transport=transport,
            follow_redirects=follow_redirects,
            cookies=cookies,
        )
