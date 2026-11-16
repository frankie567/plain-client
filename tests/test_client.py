import contextlib
import json
from collections.abc import AsyncGenerator, Callable, Coroutine

import httpx2
import pytest

from plain_client import Plain
from plain_client.input_types import (
    EmailAddressInput,
    SendChatInput,
    UpsertCustomerIdentifierInput,
    UpsertCustomerInput,
    UpsertCustomerOnCreateInput,
    UpsertCustomerOnUpdateInput,
)


@contextlib.asynccontextmanager
async def get_httpx2_client(
    handler: Callable[[httpx2.Request], Coroutine[None, None, httpx2.Response]],
) -> AsyncGenerator[httpx2.AsyncClient, None]:
    async with httpx2.AsyncClient(transport=httpx2.MockTransport(handler)) as client:
        yield client


@pytest.mark.asyncio
async def test_upsert_customer() -> None:
    async def handler(request: httpx2.Request) -> httpx2.Response:
        return httpx2.Response(
            200,
            json={
                "data": {
                    "upsertCustomer": {
                        "result": "CREATED",
                        "customer": None,
                        "error": None,
                    }
                }
            },
        )

    async with get_httpx2_client(handler) as httpx2_client:
        client = Plain(url="http://test.app", http_client=httpx2_client)
        result = await client.upsert_customer(
            UpsertCustomerInput(
                identifier=UpsertCustomerIdentifierInput(
                    externalId="CUSTOMER_ID", emailAddress="customer@example.com"
                ),
                onCreate=UpsertCustomerOnCreateInput(
                    externalId="CUSTOMER_ID",
                    email=EmailAddressInput(email="customer@example", isVerified=True),
                    fullName="John Doe",
                ),
                onUpdate=UpsertCustomerOnUpdateInput(
                    email=EmailAddressInput(email="customer@example", isVerified=True),
                ),
            )
        )
        assert result.result == "CREATED"


@pytest.mark.asyncio
async def test_send_chat() -> None:
    async def handler(request: httpx2.Request) -> httpx2.Response:
        payload = json.loads(request.content)
        assert payload["operationName"] == "sendChat"
        assert payload["variables"] == {
            "input": {"customerId": "CUSTOMER_ID", "text": "Hello"}
        }
        return httpx2.Response(
            200, json={"data": {"sendChat": {"chat": None, "error": None}}}
        )

    async with get_httpx2_client(handler) as httpx2_client:
        client = Plain(url="http://test.app", http_client=httpx2_client)
        result = await client.send_chat(
            SendChatInput(customerId="CUSTOMER_ID", text="Hello")
        )
        assert result.chat is None
        assert result.error is None
