"""Module loads and contains API Responses"""
from importlib import import_module
from pathlib import Path

from config.auto_loader import AutoLoader


class ResponsesContainer(AutoLoader):
    def __init__(self) -> None:
        to_load: dict = {}
        # ? Locate other responses's

        for responses in Path(self.responses_location).iterdir():
            if "__" in str(responses):
                continue
            name = responses.stem
            module = f"{self.responses_location}/{name}".replace("/", ".")
            to_load.update(
                {name: getattr(import_module(module), f"{name.capitalize()}Responses")}
            )

        # ? Set all APIResponses properties
        for key, value in to_load.items():
            setattr(self, key, value)


APIResponses = ResponsesContainer()
