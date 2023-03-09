"""Module loads and contains API Schema"""
from importlib import import_module
from pathlib import Path

from config.auto_loader import AutoLoader


class SchemaContainer(AutoLoader):
    def __init__(self) -> None:
        to_load: dict = {}
        # ? Locate other schema's
        for schema in Path(self.schema_location).iterdir():
            if "__" in str(schema):
                continue

            # ? Find required names & properties
            name = schema.stem
            module_name = f"{self.schema_location}/{name}".replace("/", ".")
            schema_container = getattr(import_module(module_name), f"{name.capitalize()}Schema")
            # ? Update API Schema
            to_load.update({name: schema_container})

        # ? Set all APISchema properties
        for key, value in to_load.items():
            setattr(self, key, value)


APISchema = SchemaContainer()
