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

    uid: UUID = Field(uuid4(), description="Unique IDentifier", alias="uid")
    name: str = Field(..., description="Who to say hello to")


class HelloSchema:
    """Container holding all Hello Schema"""
    Hello = Hello
    HelloList = List[Hello]
