"""
Module contains database models
"""
from dataclasses import dataclass

from .hello import Hello


@dataclass
class Models:
    """
    Container class holding all DB models.
    """

    hello = Hello
