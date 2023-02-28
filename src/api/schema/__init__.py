"""Module loads and contains APISchema"""
from importlib import import_module
from pathlib import Path

from config.auto_loader import AutoLoader

APISchema: dict = {}

for schema in Path(AutoLoader.schema_location).iterdir():
    if "__" in str(schema):
        continue
    name = schema.stem
    module_name = f"{AutoLoader.schema_location}/{name}".replace('/', '.')
    schema_container = getattr(
        import_module(module_name),
        f"{name.capitalize()}Schema"
    )

    APISchema.update({
        name: schema_container
    })
