"""
File contains response model/schema for the `Hello` table
"""
from typing import List
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Hello(BaseModel):
    """
    Model for a `Hello` object
    """

    __uuid__: UUID = Field(description="Unique IDentifier", default_factory=uuid4)

    name: str = Field(None, description="Who to say hello to")
    pronouns: str = Field('Champion', description="Pronoun to use when saying hello")

    __created_at__: str = Field(..., description="When the record was created")
    __updated_at__: str = Field(..., description="When the record was last updated")
    __deleted_at__: str = Field(..., description="When the record was deleted")

    class Config:
        orm_mode = True


class HelloList(BaseModel):
    """
    Model for a `Hello` object
    """

    data: List[Hello]

    class Config:
        orm_mode = False


class HelloSchema:
    """Container holding all Hello Schema"""
    Hello = Hello
    HelloList = List[Hello]
