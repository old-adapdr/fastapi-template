"""UpdateHelloTable Migration."""

from masoniteorm.migrations import Migration


class UpdateHelloTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("hello") as table:
            table.text("pronouns", length=32)

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table("hello") as table:
            table.drop_column("pronouns")
