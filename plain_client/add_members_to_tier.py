# Generated by ariadne-codegen
# Source: graphql/

from typing import Annotated, List, Literal, Optional, Union

from pydantic import Field

from .base_model import BaseModel
from .fragments import (
    CompanyTierMembershipParts,
    MutationErrorParts,
    TenantTierMembershipParts,
)


class AddMembersToTier(BaseModel):
    add_members_to_tier: "AddMembersToTierAddMembersToTier" = Field(
        alias="addMembersToTier"
    )


class AddMembersToTierAddMembersToTier(BaseModel):
    memberships: List[
        Annotated[
            Union[
                "AddMembersToTierAddMembersToTierMembershipsTenantTierMembership",
                "AddMembersToTierAddMembersToTierMembershipsCompanyTierMembership",
            ],
            Field(discriminator="typename__"),
        ]
    ]
    error: Optional["AddMembersToTierAddMembersToTierError"]


class AddMembersToTierAddMembersToTierMembershipsTenantTierMembership(
    TenantTierMembershipParts
):
    typename__: Literal["TenantTierMembership"] = Field(alias="__typename")


class AddMembersToTierAddMembersToTierMembershipsCompanyTierMembership(
    CompanyTierMembershipParts
):
    typename__: Literal["CompanyTierMembership"] = Field(alias="__typename")


class AddMembersToTierAddMembersToTierError(MutationErrorParts):
    pass


AddMembersToTier.model_rebuild()
AddMembersToTierAddMembersToTier.model_rebuild()
