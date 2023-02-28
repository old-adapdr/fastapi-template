"""
File contains 'users' model observer
"""

from masoniteorm.models import Model


class UsersObserver:
    def created(self, users: Model):
        """
        Handle the Users "created" event.

        Args:
            users (masoniteorm.models.Model): Users model.
        """
        pass

    def creating(self, users: Model):
        """
        Handle the Users "creating" event.

        Args:
            users (masoniteorm.models.Model): Users model.
        """
        pass

    def saving(self, users: Model):
        """
        Handle the Users "saving" event.

        Args:
            users (masoniteorm.models.Model): Users model.
        """
        pass

    def saved(self, users: Model):
        """
        Handle the Users "saved" event.

        Args:
            users (masoniteorm.models.Model): Users model.
        """
        pass

    def updating(self, users: Model):
        """
        Handle the Users "updating" event.

        Args:
            users (masoniteorm.models.Model): Users model.
        """
        pass

    def updated(self, users: Model):
        """
        Handle the Users "updated" event.

        Args:
            users (masoniteorm.models.Model): Users model.
        """
        pass

    def booted(self, users: Model):
        """
        Handle the Users "booted" event.

        Args:
            users (masoniteorm.models.Model): Users model.
        """
        pass

    def booting(self, users: Model):
        """
        Handle the Users "booting" event.

        Args:
            users (masoniteorm.models.Model): Users model.
        """
        pass

    def hydrating(self, users: Model):
        """
        Handle the Users "hydrating" event.

        Args:
            users (masoniteorm.models.Model): Users model.
        """
        pass

    def hydrated(self, users: Model):
        """
        Handle the Users "hydrated" event.

        Args:
            users (masoniteorm.models.Model): Users model.
        """
        pass

    def deleting(self, users: Model):
        """
        Handle the Users "deleting" event.

        Args:
            users (masoniteorm.models.Model): Users model.
        """
        pass

    def deleted(self, users: Model):
        """
        Handle the Users "deleted" event.

        Args:
            users (masoniteorm.models.Model): Users model.
        """
        pass
