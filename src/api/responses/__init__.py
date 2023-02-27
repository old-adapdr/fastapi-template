"""Module contains and loads API Responses"""
from importlib import import_module
from pathlib import Path

APIResponses: dict = {}

for responses in Path("api/responses").iterdir():
    if "__" not in str(responses):
        name = responses.stem
        module = import_module(f"api.responses.{responses.stem}")
        response_class = getattr(module, name.capitalize())
        APIResponses.update({name: response_class})
