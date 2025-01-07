# Generated by ariadne-codegen
# Source: graphql/

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .fragments import MutationErrorParts, ThreadParts


class ChangeThreadPriority(BaseModel):
    change_thread_priority: "ChangeThreadPriorityChangeThreadPriority" = Field(
        alias="changeThreadPriority"
    )


class ChangeThreadPriorityChangeThreadPriority(BaseModel):
    thread: Optional["ChangeThreadPriorityChangeThreadPriorityThread"]
    error: Optional["ChangeThreadPriorityChangeThreadPriorityError"]


class ChangeThreadPriorityChangeThreadPriorityThread(ThreadParts):
    pass


class ChangeThreadPriorityChangeThreadPriorityError(MutationErrorParts):
    pass


ChangeThreadPriority.model_rebuild()
ChangeThreadPriorityChangeThreadPriority.model_rebuild()