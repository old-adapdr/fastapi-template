"""
Module contains database sub-modules
"""
from .models import Models
from .observers import Observers


class Database:
    """
    Container holding various database features.
    """

    Models = Models
    Observers = Observers
