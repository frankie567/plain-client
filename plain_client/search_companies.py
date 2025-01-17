# Generated by ariadne-codegen
# Source: graphql/

from typing import List

from pydantic import Field

from .base_model import BaseModel
from .fragments import CompanyParts, PageInfoParts


class SearchCompanies(BaseModel):
    search_companies: "SearchCompaniesSearchCompanies" = Field(alias="searchCompanies")


class SearchCompaniesSearchCompanies(BaseModel):
    edges: List["SearchCompaniesSearchCompaniesEdges"]
    page_info: "SearchCompaniesSearchCompaniesPageInfo" = Field(alias="pageInfo")


class SearchCompaniesSearchCompaniesEdges(BaseModel):
    cursor: str
    node: "SearchCompaniesSearchCompaniesEdgesNode"


class SearchCompaniesSearchCompaniesEdgesNode(BaseModel):
    company: "SearchCompaniesSearchCompaniesEdgesNodeCompany"


class SearchCompaniesSearchCompaniesEdgesNodeCompany(CompanyParts):
    pass


class SearchCompaniesSearchCompaniesPageInfo(PageInfoParts):
    pass


SearchCompanies.model_rebuild()
SearchCompaniesSearchCompanies.model_rebuild()
SearchCompaniesSearchCompaniesEdges.model_rebuild()
SearchCompaniesSearchCompaniesEdgesNode.model_rebuild()
