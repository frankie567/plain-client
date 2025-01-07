# Generated by ariadne-codegen
# Source: graphql/

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .fragments import MutationErrorParts, ThreadParts


class UpdateThreadTenant(BaseModel):
    update_thread_tenant: "UpdateThreadTenantUpdateThreadTenant" = Field(
        alias="updateThreadTenant"
    )


class UpdateThreadTenantUpdateThreadTenant(BaseModel):
    thread: Optional["UpdateThreadTenantUpdateThreadTenantThread"]
    error: Optional["UpdateThreadTenantUpdateThreadTenantError"]


class UpdateThreadTenantUpdateThreadTenantThread(ThreadParts):
    pass


class UpdateThreadTenantUpdateThreadTenantError(MutationErrorParts):
    pass


UpdateThreadTenant.model_rebuild()
UpdateThreadTenantUpdateThreadTenant.model_rebuild()