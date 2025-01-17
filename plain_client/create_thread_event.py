# Generated by ariadne-codegen
# Source: graphql/

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .fragments import MutationErrorParts, ThreadEventParts


class CreateThreadEvent(BaseModel):
    create_thread_event: "CreateThreadEventCreateThreadEvent" = Field(
        alias="createThreadEvent"
    )


class CreateThreadEventCreateThreadEvent(BaseModel):
    thread_event: Optional["CreateThreadEventCreateThreadEventThreadEvent"] = Field(
        alias="threadEvent"
    )
    error: Optional["CreateThreadEventCreateThreadEventError"]


class CreateThreadEventCreateThreadEventThreadEvent(ThreadEventParts):
    pass


class CreateThreadEventCreateThreadEventError(MutationErrorParts):
    pass


CreateThreadEvent.model_rebuild()
CreateThreadEventCreateThreadEvent.model_rebuild()
