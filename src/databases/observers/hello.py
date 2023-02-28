"""
File contains 'hello' model observer
"""

from masoniteorm.models import Model


class HelloObserver:
    def created(self, hello: Model):
        """
        Handle the Hello "created" event.

        Args:
            hello (masoniteorm.models.Model): Hello model.
        """
        pass

    def creating(self, hello: Model):
        """
        Handle the Hello "creating" event.

        Args:
            hello (masoniteorm.models.Model): Hello model.
        """
        pass

    def saving(self, hello: Model):
        """
        Handle the Hello "saving" event.

        Args:
            hello (masoniteorm.models.Model): Hello model.
        """
        pass

    def saved(self, hello: Model):
        """
        Handle the Hello "saved" event.

        Args:
            hello (masoniteorm.models.Model): Hello model.
        """
        pass

    def updating(self, hello: Model):
        """
        Handle the Hello "updating" event.

        Args:
            hello (masoniteorm.models.Model): Hello model.
        """
        pass

    def updated(self, hello: Model):
        """
        Handle the Hello "updated" event.

        Args:
            hello (masoniteorm.models.Model): Hello model.
        """
        pass

    def booted(self, hello: Model):
        """
        Handle the Hello "booted" event.

        Args:
            hello (masoniteorm.models.Model): Hello model.
        """
        pass

    def booting(self, hello: Model):
        """
        Handle the Hello "booting" event.

        Args:
            hello (masoniteorm.models.Model): Hello model.
        """
        pass

    def hydrating(self, hello: Model):
        """
        Handle the Hello "hydrating" event.

        Args:
            hello (masoniteorm.models.Model): Hello model.
        """
        pass

    def hydrated(self, hello: Model):
        """
        Handle the Hello "hydrated" event.

        Args:
            hello (masoniteorm.models.Model): Hello model.
        """
        pass

    def deleting(self, hello: Model):
        """
        Handle the Hello "deleting" event.

        Args:
            hello (masoniteorm.models.Model): Hello model.
        """
        pass

    def deleted(self, hello: Model):
        """
        Handle the Hello "deleted" event.

        Args:
            hello (masoniteorm.models.Model): Hello model.
        """
        pass
