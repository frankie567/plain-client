# Generated by ariadne-codegen
# Source: graphql/

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .fragments import MutationErrorParts, ThreadParts


class SnoozeThread(BaseModel):
    snooze_thread: "SnoozeThreadSnoozeThread" = Field(alias="snoozeThread")


class SnoozeThreadSnoozeThread(BaseModel):
    thread: Optional["SnoozeThreadSnoozeThreadThread"]
    error: Optional["SnoozeThreadSnoozeThreadError"]


class SnoozeThreadSnoozeThreadThread(ThreadParts):
    pass


class SnoozeThreadSnoozeThreadError(MutationErrorParts):
    pass


SnoozeThread.model_rebuild()
SnoozeThreadSnoozeThread.model_rebuild()