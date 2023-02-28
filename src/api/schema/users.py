"""
File contains response model/schema for the `Users` table
"""
from typing import List
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Users(BaseModel):
    """
    Model for a `Users` object
    """

    __uuid__: UUID = Field(description="Unique IDentifier", default_factory=uuid4)

    name: str = Field(None, description="Who to say users to")
    pronouns: str = Field('Champion', description="Pronoun to use when saying users")

    __created_at__: str = Field(..., description="When the record was created")
    __updated_at__: str = Field(..., description="When the record was last updated")
    __deleted_at__: str = Field(..., description="When the record was deleted")

    class Config:
        orm_mode = True


class UsersList(BaseModel):
    """
    Model for a `Users` object
    """

    data: List[Users]

    class Config:
        orm_mode = False


class UsersSchema:
    """Container holding all Users Schema"""
    Users = Users
    UsersList = List[Users]
