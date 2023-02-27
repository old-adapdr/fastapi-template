"""
Module contains standardized config loader and management.
This is implemented using Pydantic for type safety and docker secerts support.
"""
from pydantic import BaseSettings

from .api import APIConfig
# from .database import DatabaseConfig


class _Config(BaseSettings):
    """
    Top-level container for holding all configs
    """

    API = APIConfig()
    # Database = DatabaseConfig()


# ? Initialize the settings
Config = _Config()