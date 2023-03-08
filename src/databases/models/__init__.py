"""Module contains and loads Database Models"""
from importlib import import_module
from pathlib import Path

from config.auto_loader import AutoLoader

DBModels: dict = {}

for model in Path(AutoLoader.models_location).iterdir():
    if "__" in str(model):
        continue
    name = model.stem
    module = f"{AutoLoader.models_location}/{name}".replace('/', '.')
    DBModels.update({
        name: getattr(
            import_module(module),
            f"{name.capitalize()}Model"
        )
    })
