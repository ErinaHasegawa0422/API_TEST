import httpx
from httpx._transports.asgi import ASGITransport
import pytest
from app.main import app

@pytest.mark.asyncio
async def test_get_hotpepper_data():
    transport = ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/hotpepper")
        assert response.status_code == 200
        data = response.json()
        assert "results" in data
        assert "shop" in data["results"]
