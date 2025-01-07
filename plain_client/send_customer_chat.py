# Generated by ariadne-codegen
# Source: graphql/

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .fragments import ChatParts, MutationErrorParts


class SendCustomerChat(BaseModel):
    send_customer_chat: "SendCustomerChatSendCustomerChat" = Field(
        alias="sendCustomerChat"
    )


class SendCustomerChatSendCustomerChat(BaseModel):
    chat: Optional["SendCustomerChatSendCustomerChatChat"]
    error: Optional["SendCustomerChatSendCustomerChatError"]


class SendCustomerChatSendCustomerChatChat(ChatParts):
    pass


class SendCustomerChatSendCustomerChatError(MutationErrorParts):
    pass


SendCustomerChat.model_rebuild()
SendCustomerChatSendCustomerChat.model_rebuild()
