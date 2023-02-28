"""File contains the HelloService class."""
from typing import List
from databases.models import Models
from api.schema.hello import Hello, HelloList


class HelloService:
    """Service class for the HelloController."""

    def options(self):
        return ["HEAD", "OPTIONS", "GET", "POST", "PUT", "PATCH", "DELETE"]

    def create(self, data: Hello):
        """Creates a `Hello` Entity from data"""
        result = Models.Hello.create(data.dict()).fresh()
        return Hello.from_orm(result)

    def retrieve(self, uuid: str) -> Hello:
        """Retrieves a `Hello` Entity by uuid"""
        result = Models.Hello.find(uuid)
        return Hello.from_orm(result)

    def retrieve_multiple(self, limit: int = 10, page_nr: int = 1, **kwargs) -> List[Hello]:
        """Retrieves a `Hello` Entity by uuid"""
        # ? Removes all empty kwarg pairs =)
        query = {key: value for key, value in kwargs.items() if value}
        result = Models.Hello.where(query).simple_paginate(limit, page_nr)
        return HelloList(**result.serialize()).data

    def update(self, uuid: str, data: Hello) -> Hello:
        """Updates a `Hello` Entity by uuid with data"""
        result = Models.Hello.where({"uuid": uuid}).update(data.dict()).get()
        return Hello.from_orm(result)

    def replace(self, uuid: str, data: Hello) -> Hello:
        """Replaces a `Hello` Entity by uuid with data"""
        result = Models.Hello.where({"uuid": uuid}).update(data.dict()).get()
        return Hello.from_orm(result)

    def delete(self, uuid: str) -> Hello:
        """Delete a `Hello` Entity by uuid"""
        result = Models.Hello.delete(uuid)
        return Hello.from_orm(result)
