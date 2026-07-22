import pytest
from fastapi.testclient import TestClient
from app.main import app


class TestRoutes:
    client = TestClient(app)

    def test_get_bearer_token(self):
        response = self.client.get("/")
        assert response.status_code == 200

    def test_get_bearer_token_favicon(self):
        response = self.client.get("/static/favicon.png")
        assert response.status_code == 200

    def test_get_bearer_token_json(self):
        response = self.client.get("/json")
        assert response.status_code == 200
        assert response.json() == {"token": "mocked-token"}

    def test_get_bearer_token_string(self):
        response = self.client.get("/text")
        assert response.status_code == 200
        assert response.text == "mocked-token"

    def test_get_health(self):
        response = self.client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "OK"}

# Bounded capture: fixtures omitted because they do not affect the TestClient constructor path.
