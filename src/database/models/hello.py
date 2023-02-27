"""
File contains hello model
"""
from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin, UUIDPrimaryKeyMixin


class Hello(Model, UUIDPrimaryKeyMixin, SoftDeletesMixin):
    """
    Database ORM Model for 'hello'
    """

    # __connection__ = 'NAME'
    __table__ = "hello"
    __primary_key__ = "uuid"

    __timezone__ = "Europe/Amsterdam"
    __timestamps__ = True

    __fillable__ = ["*"]
    # __guarded__ = ["COLUMN"]
