# Generated by ariadne-codegen
# Source: graphql/

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .fragments import MutationErrorParts, TenantParts


class UpsertTenant(BaseModel):
    upsert_tenant: "UpsertTenantUpsertTenant" = Field(alias="upsertTenant")


class UpsertTenantUpsertTenant(BaseModel):
    tenant: Optional["UpsertTenantUpsertTenantTenant"]
    error: Optional["UpsertTenantUpsertTenantError"]


class UpsertTenantUpsertTenantTenant(TenantParts):
    pass


class UpsertTenantUpsertTenantError(MutationErrorParts):
    pass


UpsertTenant.model_rebuild()
UpsertTenantUpsertTenant.model_rebuild()
