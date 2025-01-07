# Generated by ariadne-codegen
# Source: graphql/


from pydantic import Field

from .base_model import BaseModel
from .fragments import CompanyParts, PageInfoParts


class Companies(BaseModel):
    companies: "CompaniesCompanies"


class CompaniesCompanies(BaseModel):
    edges: list["CompaniesCompaniesEdges"]
    page_info: "CompaniesCompaniesPageInfo" = Field(alias="pageInfo")


class CompaniesCompaniesEdges(BaseModel):
    cursor: str
    node: "CompaniesCompaniesEdgesNode"


class CompaniesCompaniesEdgesNode(CompanyParts):
    pass


class CompaniesCompaniesPageInfo(PageInfoParts):
    pass


Companies.model_rebuild()
CompaniesCompanies.model_rebuild()
CompaniesCompaniesEdges.model_rebuild()
