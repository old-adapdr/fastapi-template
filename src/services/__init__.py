"""Module loads and contains API Services"""
from importlib import import_module
from pathlib import Path

APIServices: dict = {}

for schema in Path("services").iterdir():
    if "__" not in str(schema):
        name = schema.stem
        module = import_module(f"services.{schema.stem}")
        service_class = getattr(module, f"{name.capitalize()}Service")
        APIServices.update({name: service_class})
