"""Module loads and contains APISchema"""
from importlib import import_module
from pathlib import Path

APISchema: dict = {}

for schema in Path("api/schema").iterdir():
    if "__" not in str(schema):
        name = schema.stem
        module = import_module(f"api.schema.{schema.stem}")
        schema_class = getattr(module, f"{name.capitalize()}Schema")
        APISchema.update({name: schema_class})
