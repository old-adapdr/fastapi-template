"""
File contains migration to create `hello` table.
"""

from masoniteorm.migrations import Migration


class CreateHelloTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("hello") as table:
            table.uuid("uuid").primary()
            table.text("name", length=32)

            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("hello")
