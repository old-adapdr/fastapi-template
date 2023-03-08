"""Module loads and contains API Services"""
from importlib import import_module
from pathlib import Path

from config.auto_loader import AutoLoader

SERVICES = {}

for service in Path(AutoLoader.services_loaction).iterdir():
    if "__" in str(service):
        continue

    name = service.stem
    module = f"{AutoLoader.services_loaction}/{name}".replace("/", ".")
    SERVICES.update(
        {name: getattr(import_module(module), f"{name.capitalize()}Service")}
    )


class APIServices:
    """Class is ussed as an accessor for FastAPI Depends()"""

    @staticmethod
    def get(name: str):
        """Method returns a service container"""
        return SERVICES[name]
