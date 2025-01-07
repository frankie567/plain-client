# Generated by ariadne-codegen
# Source: graphql/

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .fragments import LabelTypeParts


class ArchiveLabelType(BaseModel):
    archive_label_type: "ArchiveLabelTypeArchiveLabelType" = Field(
        alias="archiveLabelType"
    )


class ArchiveLabelTypeArchiveLabelType(BaseModel):
    label_type: Optional["ArchiveLabelTypeArchiveLabelTypeLabelType"] = Field(
        alias="labelType"
    )
    error: Optional["ArchiveLabelTypeArchiveLabelTypeError"]


class ArchiveLabelTypeArchiveLabelTypeLabelType(LabelTypeParts):
    pass


class ArchiveLabelTypeArchiveLabelTypeError(BaseModel):
    message: str


ArchiveLabelType.model_rebuild()
ArchiveLabelTypeArchiveLabelType.model_rebuild()
