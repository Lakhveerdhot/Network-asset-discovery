"""
Change Repository
"""

from datetime import datetime

from database.database_manager import DatabaseManager


class ChangeRepository:

    def __init__(self, db):

        self.db = db

        self.connection = db.connection

        self.cursor = db.cursor
    # -------------------------------------------------

    def save(self, host):

        for change in host.changes:

            self.cursor.execute(

                """
                INSERT INTO change_history(

                    mac,

                    change_text,

                    detected_at

                )

                VALUES(

                    ?,?,?

                )
                """,

                (

                    host.mac,

                    change,

                    datetime.now().strftime(

                        "%Y-%m-%d %H:%M:%S"

                    )

                )

            )

        self.connection.commit()

    # -------------------------------------------------

    def get(self, mac):

        self.cursor.execute(

            """
            SELECT *

            FROM change_history

            WHERE mac=?

            ORDER BY detected_at DESC
            """,

            (mac,)

        )

        return self.cursor.fetchall()
    

    # -------------------------------------------------

    def delete(self, mac):

        self.cursor.execute(

            """
            DELETE FROM change_history

            WHERE mac=?
            """,

            (mac,)

        )

        self.db.connection.commit()
    

    # -------------------------------------------------

    def get_by_mac(self, mac):

        self.cursor.execute(

            """
            SELECT *

            FROM change_history

            WHERE mac=?

            ORDER BY detected_at DESC
            """,

            (mac,)

        )

        return self.cursor.fetchall()