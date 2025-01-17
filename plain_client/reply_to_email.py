# Generated by ariadne-codegen
# Source: graphql/

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .fragments import EmailParts, MutationErrorParts


class ReplyToEmail(BaseModel):
    reply_to_email: "ReplyToEmailReplyToEmail" = Field(alias="replyToEmail")


class ReplyToEmailReplyToEmail(BaseModel):
    email: Optional["ReplyToEmailReplyToEmailEmail"]
    error: Optional["ReplyToEmailReplyToEmailError"]


class ReplyToEmailReplyToEmailEmail(EmailParts):
    pass


class ReplyToEmailReplyToEmailError(MutationErrorParts):
    pass


ReplyToEmail.model_rebuild()
ReplyToEmailReplyToEmail.model_rebuild()
