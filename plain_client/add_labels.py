# Generated by ariadne-codegen
# Source: graphql/

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .fragments import LabelParts, MutationErrorParts


class AddLabels(BaseModel):
    add_labels: "AddLabelsAddLabels" = Field(alias="addLabels")


class AddLabelsAddLabels(BaseModel):
    labels: list["AddLabelsAddLabelsLabels"]
    error: Optional["AddLabelsAddLabelsError"]


class AddLabelsAddLabelsLabels(LabelParts):
    pass


class AddLabelsAddLabelsError(MutationErrorParts):
    pass


AddLabels.model_rebuild()
AddLabelsAddLabels.model_rebuild()
