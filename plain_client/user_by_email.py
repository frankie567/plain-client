# Generated by ariadne-codegen
# Source: graphql/

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .fragments import UserParts


class UserByEmail(BaseModel):
    user_by_email: Optional["UserByEmailUserByEmail"] = Field(alias="userByEmail")


class UserByEmailUserByEmail(UserParts):
    pass


UserByEmail.model_rebuild()