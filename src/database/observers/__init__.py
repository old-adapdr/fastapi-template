"""
File contains database model observers
? Doc reference: https://orm.masoniteproject.com/models?q=obsrvers
"""
from .hello import HelloObserver


class Observers:
    """
    Container holding database observers
    """

    hello = HelloObserver
