"""
Trust Manager
"""

from database.database_manager import DatabaseManager


class TrustManager:

    def __init__(self):

        self.database = DatabaseManager()

    # ----------------------------------------

    def get_status(self, mac):

        self.database.cursor.execute(

            """

            SELECT trust_status

            FROM devices

            WHERE mac = ?

            """,

            (

                mac,

            )

        )

        result = self.database.cursor.fetchone()

        if result:

            return result["trust_status"]

        return "Unknown"

    # ----------------------------------------

    def trust_device(self, mac):

        self.database.cursor.execute(

            """

            UPDATE devices

            SET trust_status='Trusted'

            WHERE mac=?

            """,

            (

                mac,

            )

        )

        self.database.connection.commit()

    # ----------------------------------------

    def untrust_device(self, mac):

        self.database.cursor.execute(

            """

            UPDATE devices

            SET trust_status='Untrusted'

            WHERE mac=?

            """,

            (

                mac,

            )

        )

        self.database.connection.commit()

    # ----------------------------------------

    def close(self):

        self.database.close()
        