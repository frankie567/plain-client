# Generated by ariadne-codegen
# Source: graphql/

from typing import Optional

from .base_model import BaseModel
from .fragments import CustomerParts


class CustomerById(BaseModel):
    customer: Optional["CustomerByIdCustomer"]


class CustomerByIdCustomer(CustomerParts):
    pass


CustomerById.model_rebuild()
