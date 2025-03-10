# Generated by ariadne-codegen
# Source: graphql/

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import UpsertResult
from .fragments import MutationErrorParts, ThreadFieldParts


class UpsertThreadField(BaseModel):
    upsert_thread_field: "UpsertThreadFieldUpsertThreadField" = Field(
        alias="upsertThreadField"
    )


class UpsertThreadFieldUpsertThreadField(BaseModel):
    result: Optional[UpsertResult]
    thread_field: Optional["UpsertThreadFieldUpsertThreadFieldThreadField"] = Field(
        alias="threadField"
    )
    error: Optional["UpsertThreadFieldUpsertThreadFieldError"]


class UpsertThreadFieldUpsertThreadFieldThreadField(ThreadFieldParts):
    pass


class UpsertThreadFieldUpsertThreadFieldError(MutationErrorParts):
    pass


UpsertThreadField.model_rebuild()
UpsertThreadFieldUpsertThreadField.model_rebuild()
