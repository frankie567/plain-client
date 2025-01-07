# Generated by ariadne-codegen
# Source: graphql/

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .fragments import MutationErrorParts, ThreadParts


class CreateThread(BaseModel):
    create_thread: "CreateThreadCreateThread" = Field(alias="createThread")


class CreateThreadCreateThread(BaseModel):
    thread: Optional["CreateThreadCreateThreadThread"]
    error: Optional["CreateThreadCreateThreadError"]


class CreateThreadCreateThreadThread(ThreadParts):
    pass


class CreateThreadCreateThreadError(MutationErrorParts):
    pass


CreateThread.model_rebuild()
CreateThreadCreateThread.model_rebuild()