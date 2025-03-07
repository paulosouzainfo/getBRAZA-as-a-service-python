import pytest
from getbraza.client import GetBrazaClient

@pytest.mark.asyncio
async def test_input_transaction():
    client = GetBrazaClient("app_id", "api_key", "account_number")
    response = await client.input_transaction({
        "url_callback": "https://example.com/callback",
        "amount": "100.00"
    })
    assert "message" in response
