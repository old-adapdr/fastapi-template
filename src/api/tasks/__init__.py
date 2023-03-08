"""Module loads and contains API Tasks"""
from importlib import import_module
from pathlib import Path

from config.auto_loader import AutoLoader

TASKS = {}

for service in Path(AutoLoader.tasks_location).iterdir():
    if "__" in str(service):
        continue

    name = service.stem
    module = f"{AutoLoader.tasks_location}/{name}".replace("/", ".")
    TASKS.update({name: getattr(import_module(module), f"{name.capitalize()}Tasks")})


class APITasks:
    """Class is ussed as an accessor for FastAPI BackgroundTasks"""

    @staticmethod
    def get(name: str):
        """Method returns a tasks container"""
        return TASKS[name]
