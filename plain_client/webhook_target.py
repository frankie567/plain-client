# Generated by ariadne-codegen
# Source: graphql/

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .fragments import WebhookTargetParts


class WebhookTarget(BaseModel):
    webhook_target: Optional["WebhookTargetWebhookTarget"] = Field(
        alias="webhookTarget"
    )


class WebhookTargetWebhookTarget(WebhookTargetParts):
    pass


WebhookTarget.model_rebuild()