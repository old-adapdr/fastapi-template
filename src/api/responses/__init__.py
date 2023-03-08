"""Module loads and contains API Responses"""
from importlib import import_module
from pathlib import Path

from config.auto_loader import AutoLoader

APIResponses: dict = {}

for responses in Path(AutoLoader.responses_location).iterdir():
    if "__" in str(responses):
        continue
    name = responses.stem
    module = f"{AutoLoader.responses_location}/{name}".replace("/", ".")
    APIResponses.update(
        {name: getattr(import_module(module), f"{name.capitalize()}Responses")}
    )
