from plain_client import Plain
from plain_client.custom_mutations import Mutation
from plain_client.custom_queries import Query
from plain_client.input_types import (
    EmailAddressInput,
    UpsertCustomerIdentifierInput,
    UpsertCustomerInput,
    UpsertCustomerOnCreateInput,
    UpsertCustomerOnUpdateInput,
)


async def test_client() -> None:
    client = Plain()
    mutation = Mutation.upsert_customer(
        UpsertCustomerInput(
            identifier=UpsertCustomerIdentifierInput(
                externalId="123", emailAddress="foo@bar.com"
            ),
            onCreate=UpsertCustomerOnCreateInput(
                externalId="123",
                email=EmailAddressInput(email="foo@bar.com", isVerified=True),
                fullName="Foo Bar",
            ),
            onUpdate=UpsertCustomerOnUpdateInput(
                email=EmailAddressInput(email="foo@bar.com", isVerified=True),
            ),
        )
    )

    result = await client.upsert_customer(
        UpsertCustomerInput(
            identifier=UpsertCustomerIdentifierInput(
                externalId="123", emailAddress="foo@bar.com"
            ),
            onCreate=UpsertCustomerOnCreateInput(
                externalId="123",
                email=EmailAddressInput(email="foo@bar.com", isVerified=True),
                fullName="Foo Bar",
            ),
            onUpdate=UpsertCustomerOnUpdateInput(
                email=EmailAddressInput(email="foo@bar.com", isVerified=True),
            ),
        )
    )
    result.upsert_customer.result

    query = Query.customer("aaa")
    response = await client.query(query, operation_name="Customer")

    response = await client.query(mutation, operation_name="UpsertCustomer")
    UpsertCustomerOutput
