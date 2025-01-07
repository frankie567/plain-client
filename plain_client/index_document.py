# Generated by ariadne-codegen
# Source: graphql/

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .fragments import IndexedDocumentParts, MutationErrorParts


class IndexDocument(BaseModel):
    create_indexed_document: "IndexDocumentCreateIndexedDocument" = Field(
        alias="createIndexedDocument"
    )


class IndexDocumentCreateIndexedDocument(BaseModel):
    indexed_document: Optional["IndexDocumentCreateIndexedDocumentIndexedDocument"] = (
        Field(alias="indexedDocument")
    )
    error: Optional["IndexDocumentCreateIndexedDocumentError"]


class IndexDocumentCreateIndexedDocumentIndexedDocument(IndexedDocumentParts):
    pass


class IndexDocumentCreateIndexedDocumentError(MutationErrorParts):
    pass


IndexDocument.model_rebuild()
IndexDocumentCreateIndexedDocument.model_rebuild()