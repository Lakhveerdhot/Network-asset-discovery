"""
Scheduler Repository
"""

from datetime import datetime


class SchedulerRepository:

    def __init__(self, db):

        self.db = db

        self.cursor = db.cursor

    # ---------------------------------------------

    def is_enabled(self):

        self.cursor.execute(

            """

            SELECT enabled

            FROM scheduler_settings

            WHERE id=1

            """

        )

        result = self.cursor.fetchone()

        return bool(result["enabled"])

    # ---------------------------------------------

    def enable(self):

        now = datetime.now().strftime(

            "%Y-%m-%d %H:%M:%S"

        )

        self.cursor.execute(

            """

            UPDATE scheduler_settings

            SET

                enabled=1,

                last_enabled=?,

                last_updated=?

            WHERE id=1

            """,

            (

                now,

                now

            )

        )

        self.db.connection.commit()

    # ---------------------------------------------

    def disable(self):

        self.cursor.execute(

            """

            UPDATE scheduler_settings

            SET

                enabled=0,

                last_updated=?

            WHERE id=1

            """,

            (

                datetime.now().strftime(

                    "%Y-%m-%d %H:%M:%S"

                ),

            )

        )

        self.db.connection.commit()

    # ---------------------------------------------

    def interval(self):

        self.cursor.execute(

            """

            SELECT interval_minutes

            FROM scheduler_settings

            WHERE id=1

            """

        )

        return self.cursor.fetchone()["interval_minutes"]

    # ---------------------------------------------

    def set_interval(

        self,

        minutes

    ):

        self.cursor.execute(

            """

            UPDATE scheduler_settings

            SET

                interval_minutes=?,

                last_updated=?

            WHERE id=1

            """,

            (

                minutes,

                datetime.now().strftime(

                    "%Y-%m-%d %H:%M:%S"

                )

            )

        )
        self.db.connection.commit()
    
    # ------------------------------------------------

    def last_enabled(self):

        self.cursor.execute(

            """
            SELECT last_enabled
            FROM scheduler_settings
            WHERE id=1
            """

        )

        result = self.cursor.fetchone()

        return result["last_enabled"]