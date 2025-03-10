# Generated by ariadne-codegen
# Source: graphql/

from typing import List

from pydantic import Field

from .base_model import BaseModel
from .fragments import CustomerParts, PageInfoParts


class Customers(BaseModel):
    customers: "CustomersCustomers"


class CustomersCustomers(BaseModel):
    edges: List["CustomersCustomersEdges"]
    page_info: "CustomersCustomersPageInfo" = Field(alias="pageInfo")
    total_count: int = Field(alias="totalCount")


class CustomersCustomersEdges(BaseModel):
    node: "CustomersCustomersEdgesNode"


class CustomersCustomersEdgesNode(CustomerParts):
    pass


class CustomersCustomersPageInfo(PageInfoParts):
    pass


Customers.model_rebuild()
CustomersCustomers.model_rebuild()
CustomersCustomersEdges.model_rebuild()
