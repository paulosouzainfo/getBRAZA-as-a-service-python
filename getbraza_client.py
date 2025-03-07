import aiohttp
import json
from typing import Dict, Any

class GetBrazaClient:
    def __init__(self, application_id: str, api_key: str, account_number: str, base_url: str = "https://sandbox-api.getbraza.uk/v2/business"):
        self.application_id = application_id
        self.api_key = api_key
        self.account_number = account_number
        self.base_url = base_url

    async def _request(self, method: str, endpoint: str, data: Dict[str, Any] = None):
        headers = {
            "x-application-id": self.application_id,
            "x-api-key": self.api_key,
            "x-account-number": self.account_number,
            "Content-Type": "application/json"
        }
        async with aiohttp.ClientSession() as session:
            async with session.request(method, f"{self.base_url}{endpoint}", headers=headers, json=data) as response:
                response.raise_for_status()
                return await response.json()

    async def input_transaction(self, data: Dict[str, Any]):
        return await self._request("POST", "/v1/", data)

    async def retrieve_transactions(self):
        return await self._request("POST", "/v1/transactions")

    async def withdraw(self, data: Dict[str, Any]):
        return await self._request("POST", "/v1/withdraw", data)

    async def get_quote(self, pair: str, markup_type: str = None, markup_value: float = None):
        params = {"pair": pair}
        if markup_type:
            params["markup_type"] = markup_type
        if markup_value:
            params["markup_value"] = markup_value
        return await self._request("GET", "/v1/quote", params)

    async def internal_transfer(self, data: Dict[str, Any]):
        return await self._request("POST", "/v1/internal-transfer", data)

    async def auth(self):
        return await self._request("POST", "/v1/auth")

    async def get_balance(self):
        return await self._request("GET", "/v1/balance")
