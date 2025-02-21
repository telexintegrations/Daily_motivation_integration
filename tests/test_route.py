import pytest
from httpx import AsyncClient, ASGITransport
from unittest.mock import AsyncMock, patch
from src import app 
from src.Daily_Bot.routes import get_motivation  


@pytest.mark.asyncio
async def test_get_integration_json():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/integration.json")
        assert response.status_code == 200
    data = response.json()
    assert data["data"]["descriptions"]["app_name"] == "Daily Motivation Bot"
    assert "app_url" in data["data"]["descriptions"]
    assert data["data"]["is_active"] is True


@pytest.mark.asyncio
@patch("src.Daily_Bot.routes.httpx.AsyncClient.post")
async def test_send_motivation(mock_post):
    payload = {
        "return_url": "http://example.com/return",
        "channel_id": "01950f92-160a-7aeb-a3b2-764c0cd03118",
        "settings": [
            {
                "label": "time interval",
                "type": "text",
                "required": True,
                "default": "0 21 * * *"
            }
    ]
    }

    mock_response = AsyncMock()
    mock_response.status_code = 202
    mock_response.json = AsyncMock(return_value={"status": "accepted"}) 
    mock_post.return_value = mock_response

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/tick", json=payload)
    response_json = await response.json()
    assert response.status_code == 202
    assert response_json == {"status": "accepted"}
