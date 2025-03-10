# Generated by ariadne-codegen
# Source: graphql/

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .fragments import MutationErrorParts


class RemoveCustomerFromTenants(BaseModel):
    remove_customer_from_tenants: "RemoveCustomerFromTenantsRemoveCustomerFromTenants" = Field(
        alias="removeCustomerFromTenants"
    )


class RemoveCustomerFromTenantsRemoveCustomerFromTenants(BaseModel):
    error: Optional["RemoveCustomerFromTenantsRemoveCustomerFromTenantsError"]


class RemoveCustomerFromTenantsRemoveCustomerFromTenantsError(MutationErrorParts):
    pass


RemoveCustomerFromTenants.model_rebuild()
RemoveCustomerFromTenantsRemoveCustomerFromTenants.model_rebuild()
