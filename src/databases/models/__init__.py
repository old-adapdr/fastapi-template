"""Module contains and loads Database Models"""
from importlib import import_module
from pathlib import Path

from config.auto_loader import AutoLoader


class ModelsContainer(AutoLoader):
    def __init__(self) -> None:
        to_load: dict = {}
        # ? Locate other schema's
        for model in Path(self.models_location).iterdir():
            if "__" in str(model):
                continue
            name = model.stem
            module = f"{self.models_location}/{name}".replace('/', '.')
            to_load.update({
                name: getattr(
                    import_module(module),
                    f"{name.capitalize()}Model"
                )
            })

        # ? Set all APIModels properties
        for key, value in to_load.items():
            setattr(self, key, value)


APIModels = ModelsContainer()
