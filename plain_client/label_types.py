# Generated by ariadne-codegen
# Source: graphql/

from typing import List

from pydantic import Field

from .base_model import BaseModel
from .fragments import LabelTypeParts, PageInfoParts


class LabelTypes(BaseModel):
    label_types: "LabelTypesLabelTypes" = Field(alias="labelTypes")


class LabelTypesLabelTypes(BaseModel):
    edges: List["LabelTypesLabelTypesEdges"]
    page_info: "LabelTypesLabelTypesPageInfo" = Field(alias="pageInfo")


class LabelTypesLabelTypesEdges(BaseModel):
    cursor: str
    node: "LabelTypesLabelTypesEdgesNode"


class LabelTypesLabelTypesEdgesNode(LabelTypeParts):
    pass


class LabelTypesLabelTypesPageInfo(PageInfoParts):
    pass


LabelTypes.model_rebuild()
LabelTypesLabelTypes.model_rebuild()
LabelTypesLabelTypesEdges.model_rebuild()
