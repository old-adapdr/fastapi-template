"""File contains the PreferencesService class."""
from typing import List

from api.schema.preferences import Preferences, PreferencesList
from databases.models import DBModels


class PreferencesService:
    """Service class for the PreferencesRouter."""

    def options(self):
        return ["HEAD", "OPTIONS", "GET", "POST", "PUT", "PATCH", "DELETE"]

    def create(self, data: Preferences):
        """Creates a `Preferences` Entity from data"""
        result = DBModels['preferences'].create(data.dict()).fresh()
        return Preferences.from_orm(result)

    def retrieve(self, uuid: str) -> Preferences:
        """Retrieves a `Preferences` Entity by uuid"""
        result = DBModels['preferences'].find(uuid)
        return Preferences.from_orm(result)

    def listed(
        self, limit: int = 10, page_nr: int = 1, **kwargs
    ) -> List[Preferences]:
        """Retrieves a `Preferences` Entity by uuid"""
        # ? Removes all empty kwarg pairs =)
        query = {key: value for key, value in kwargs.items() if value}
        result = DBModels['preferences'].where(query).simple_paginate(limit, page_nr)
        return PreferencesList(**result.serialize()).data

    def update(self, uuid: str, data: Preferences) -> Preferences:
        """Updates a `Preferences` Entity by uuid with data"""
        result = DBModels['preferences'].where({"uuid": uuid}).update(data.dict()).get()
        return Preferences.from_orm(result)

    def replace(self, uuid: str, data: Preferences) -> Preferences:
        """Replaces a `Preferences` Entity by uuid with data"""
        self.delete(uuid)
        return self.create(data)

    def delete(self, uuid: str) -> Preferences:
        """Delete a `Preferences` Entity by uuid"""
        result = DBModels['preferences'].delete(uuid)
        return Preferences.from_orm(result)
