import contextlib
from collections.abc import AsyncGenerator, Coroutine
from typing import Callable

import httpx
import pytest

from plain_client import Plain
from plain_client.input_types import (
    EmailAddressInput,
    UpsertCustomerIdentifierInput,
    UpsertCustomerInput,
    UpsertCustomerOnCreateInput,
    UpsertCustomerOnUpdateInput,
)


@contextlib.asynccontextmanager
async def get_httpx_client(
    handler: Callable[[httpx.Request], Coroutine[None, None, httpx.Response]],
) -> AsyncGenerator[httpx.AsyncClient, None]:
    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
        yield client


@pytest.mark.asyncio
async def test_upsert_customer() -> None:
    async def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
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

    async with get_httpx_client(handler) as httpx_client:
        client = Plain(url="http://test.app", http_client=httpx_client)
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
