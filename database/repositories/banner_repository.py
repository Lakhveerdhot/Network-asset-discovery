"""
Banner Repository
"""

from database.database_manager import DatabaseManager


class BannerRepository:

    def __init__(self, db):

        self.db = db

        self.connection = db.connection

        self.cursor = db.cursor

    # -------------------------------------------------

    def clear(self, mac):

        self.cursor.execute(

            """
            DELETE FROM banners

            WHERE mac=?
            """,

            (mac,)

        )

        self.connection.commit()

    # -------------------------------------------------

    def save(self, host):

        self.clear(host.mac)

        for port, banner in host.banners.items():

            self.cursor.execute(

                """
                INSERT INTO banners(

                    mac,

                    port,

                    banner

                )

                VALUES(

                    ?,?,?

                )
                """,

                (

                    host.mac,

                    port,

                    banner

                )

            )

        self.connection.commit()

    # -------------------------------------------------

    def get(self, mac):

        self.cursor.execute(

            """
            SELECT *

            FROM banners

            WHERE mac=?

            ORDER BY port
            """,

            (mac,)

        )

        return self.cursor.fetchall()
    
    # -------------------------------------------------

    def delete(self, mac):

        self.cursor.execute(

            """
            DELETE FROM banners

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

            FROM banners

            WHERE mac=?

            ORDER BY port
            """,

            (mac,)

        )

        return self.cursor.fetchall()