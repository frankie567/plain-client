# Generated by ariadne-codegen
# Source: graphql/

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .fragments import MutationErrorParts


class ReplyToThread(BaseModel):
    reply_to_thread: "ReplyToThreadReplyToThread" = Field(alias="replyToThread")


class ReplyToThreadReplyToThread(BaseModel):
    error: Optional["ReplyToThreadReplyToThreadError"]


class ReplyToThreadReplyToThreadError(MutationErrorParts):
    pass


ReplyToThread.model_rebuild()
ReplyToThreadReplyToThread.model_rebuild()
