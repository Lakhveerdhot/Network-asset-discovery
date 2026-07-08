"""
System Settings Repository
"""

from datetime import datetime


class SettingsRepository:

    def __init__(self, db):

        self.db = db

        self.cursor = db.cursor

    # --------------------------------------------------

    def initialize(self):

        self.cursor.execute(

            """
            SELECT COUNT(*)

            FROM system_settings
            """

        )

        count = self.cursor.fetchone()[0]

        if count == 0:

            self.cursor.execute(

                """
                INSERT INTO system_settings(

                    id,

                    target_network,

                    scan_timeout,

                    port_scan_timeout,

                    common_threads,

                    banner_enabled,

                    os_fingerprinting_enabled,

                    vendor_lookup_enabled,

                    report_txt_enabled,

                    report_csv_enabled,

                    report_pdf_enabled,

                    last_updated

                )

                VALUES(

                    1,

                    '192.168.31.0/24',

                    2,

                    0.5,

                    20,

                    1,

                    1,

                    1,

                    1,

                    0,

                    0,

                    ?

                )

                """,

                (

                    datetime.now().strftime(

                        "%Y-%m-%d %H:%M:%S"

                    ),

                )

            )

            self.db.connection.commit()

    # --------------------------------------------------

    def get(self):

        self.cursor.execute(

            """
            SELECT *

            FROM system_settings

            WHERE id=1
            """

        )

        return self.cursor.fetchone()
    

    # --------------------------------------------------

    def update(

        self,

        target_network,

        scan_timeout,

        port_scan_timeout,

        common_threads,

        banner_enabled,

        os_enabled,

        vendor_enabled,

        report_txt,

        report_csv,

        report_pdf

    ):

        self.cursor.execute(

            """

            UPDATE system_settings

            SET

                target_network=?,

                scan_timeout=?,

                port_scan_timeout=?,

                common_threads=?,

                banner_enabled=?,

                os_fingerprinting_enabled=?,

                vendor_lookup_enabled=?,

                report_txt_enabled=?,

                report_csv_enabled=?,

                report_pdf_enabled=?,

                last_updated=?

            WHERE id=1

            """,

            (

                target_network,

                scan_timeout,

                port_scan_timeout,

                common_threads,

                banner_enabled,

                os_enabled,

                vendor_enabled,

                report_txt,

                report_csv,

                report_pdf,

                datetime.now().strftime(

                    "%Y-%m-%d %H:%M:%S"

                )

            )

        )

        self.db.connection.commit()