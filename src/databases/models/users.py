"""
File contains users model
"""
from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin, UUIDPrimaryKeyMixin


class UsersModel(Model, UUIDPrimaryKeyMixin, SoftDeletesMixin):
    """
    Database ORM Model for 'users'
    """

    # __connection__ = 'NAME'
    __table__ = "users"
    __primary_key__ = "uuid"

    __timezone__ = "Europe/Amsterdam"
    __timestamps__ = True

    # __fillable__ = ["*"]
    __guarded__ = ["created_at", "updated_at", "deleted_at"]
    __hidden__ = ["uuid", "created_at", "updated_at", "deleted_at"]
