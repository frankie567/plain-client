# Generated by ariadne-codegen
# Source: graphql/

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .fragments import CustomerGroupMembershipParts, PageInfoParts


class CustomerCustomerGroups(BaseModel):
    customer: Optional["CustomerCustomerGroupsCustomer"]


class CustomerCustomerGroupsCustomer(BaseModel):
    customer_group_memberships: (
        "CustomerCustomerGroupsCustomerCustomerGroupMemberships"
    ) = Field(alias="customerGroupMemberships")


class CustomerCustomerGroupsCustomerCustomerGroupMemberships(BaseModel):
    edges: List["CustomerCustomerGroupsCustomerCustomerGroupMembershipsEdges"]
    page_info: "CustomerCustomerGroupsCustomerCustomerGroupMembershipsPageInfo" = Field(
        alias="pageInfo"
    )


class CustomerCustomerGroupsCustomerCustomerGroupMembershipsEdges(BaseModel):
    node: "CustomerCustomerGroupsCustomerCustomerGroupMembershipsEdgesNode"


class CustomerCustomerGroupsCustomerCustomerGroupMembershipsEdgesNode(
    CustomerGroupMembershipParts
):
    pass


class CustomerCustomerGroupsCustomerCustomerGroupMembershipsPageInfo(PageInfoParts):
    pass


CustomerCustomerGroups.model_rebuild()
CustomerCustomerGroupsCustomer.model_rebuild()
CustomerCustomerGroupsCustomerCustomerGroupMemberships.model_rebuild()
CustomerCustomerGroupsCustomerCustomerGroupMembershipsEdges.model_rebuild()
