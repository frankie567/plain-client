# Generated by ariadne-codegen
# Source: graphql/

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .fragments import CustomerParts


class CustomerByExternalId(BaseModel):
    customer_by_external_id: Optional["CustomerByExternalIdCustomerByExternalId"] = (
        Field(alias="customerByExternalId")
    )


class CustomerByExternalIdCustomerByExternalId(CustomerParts):
    pass


CustomerByExternalId.model_rebuild()
