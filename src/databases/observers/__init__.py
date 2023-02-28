"""
File contains database model observers
? Doc reference: https://orm.masoniteproject.com/models?q=obsrvers
"""
from .users import UsersObserver


class Observers:
    """Container holding database observers"""

    users = UsersObserver
