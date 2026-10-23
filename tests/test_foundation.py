import asyncio

import httpx
import pytest

from backend.app.main import app


def request(method, path, **kwargs):
    async def send():
        async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://local.test") as client:
            return await client.request(method, path, **kwargs)

    return asyncio.run(send())


@pytest.mark.parametrize("path,status", [("/health", "ok"), ("/ready", "ready")])
def test_foundation_probes(path, status):
    response = request("GET", path)
    assert response.status_code == 200
    assert response.json() == {"status": status, "stage": "foundation"}


def test_no_unapproved_execution_endpoint():
    assert request("POST", "/api/v1/projects/unknown/runs", json={}).status_code == 404
