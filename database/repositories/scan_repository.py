"""
Scan Repository
"""
import time
from database.database_manager import DatabaseManager


class ScanRepository:

    def __init__(self, db):

        self.db = db

        self.connection = db.connection

        self.cursor = db.cursor

    # -------------------------------------------------

    def save(

        self,

        total_hosts,

        total_open_ports,

        duration

    ):

        scan_time = time.strftime(

            "%Y-%m-%d %H:%M:%S"

        )

        self.cursor.execute(

            """
            INSERT INTO scan_history(

                scan_time,

                total_hosts,

                open_ports,

                duration

            )

            VALUES(

                ?,?,?,?

            )
            """,

            (

                scan_time,

                total_hosts,

                total_open_ports,

                duration

            )

        )

        self.db.connection.commit()

    # -------------------------------------------------

    def get_all(self):

        self.cursor.execute(

            """
            SELECT *

            FROM scan_history

            ORDER BY id DESC
            """

        )

        return self.cursor.fetchall()
    

    # -------------------------------------------------

    def recent_scans(self, limit=10):

        self.cursor.execute(

            """
            SELECT *

            FROM scan_history

            ORDER BY id DESC

            LIMIT ?
            """,

            (limit,)

        )

        return self.cursor.fetchall()
    
    # -------------------------------------------------

    def latest_scan(self):

        self.cursor.execute(

            """
            SELECT *

            FROM scan_history

            ORDER BY id DESC

            LIMIT 1
            """

        )

        return self.cursor.fetchone()