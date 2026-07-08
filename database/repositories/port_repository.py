"""
Port Repository
"""

from database.database_manager import DatabaseManager


class PortRepository:

    def __init__(self, db):

        self.db = db

        self.connection = db.connection

        self.cursor = db.cursor

    # ---------------------------------------------

    def clear(self, mac):

        self.cursor.execute(

            """
            DELETE FROM ports

            WHERE mac=?
            """,

            (mac,)

        )

        self.connection.commit()

    # ---------------------------------------------

    def save(self, host):

        self.clear(host.mac)

        for port in host.open_ports:

            self.cursor.execute(

                """
                INSERT INTO ports(

                    mac,

                    port,

                    service

                )

                VALUES(

                    ?,?,?

                )
                """,

                (

                    host.mac,

                    port,

                    host.services.get(

                        port,

                        "Unknown"

                    )

                )

            )

        self.connection.commit()


        # -------------------------------------------------

    def delete(self, mac):

        self.cursor.execute(

            """
            DELETE FROM ports

            WHERE mac=?
            """,

            (mac,)

        )

        self.db.connection.commit()

    # ---------------------------------------------

    def get(self, mac):

        self.cursor.execute(

            """
            SELECT *

            FROM ports

            WHERE mac=?

            ORDER BY port
            """,

            (mac,)

        )

        return self.cursor.fetchall()