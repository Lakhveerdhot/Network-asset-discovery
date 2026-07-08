"""
Device Repository
"""

from database.database_manager import DatabaseManager


class DeviceRepository:

    def __init__(self, db):

        self.db = db

        self.connection = db.connection

        self.cursor = db.cursor

    # ---------------------------------------------

    def device_exists(self, mac):

        self.cursor.execute(

            """
            SELECT id

            FROM devices

            WHERE mac=?
            """,

            (mac,)

        )

        return self.cursor.fetchone() is not None

    # ---------------------------------------------

    def insert(self, host):

        self.cursor.execute(

            """
            INSERT INTO devices(

                ip,

                mac,

                vendor,

                hostname,

                hostname_source,

                device_type,

                operating_system,

                os_confidence,

                trust_status,

                status,

                first_seen,

                last_seen

            )

            VALUES(

                ?,?,?,?,?,?,?,?,?,?,?,?

            )
            """,

            (

                host.ip,

                host.mac,

                host.vendor,

                host.hostname,

                host.hostname_source,

                host.device_type,

                host.operating_system,

                host.os_confidence,

                host.trust_status,

                host.status,

                host.first_seen,

                host.last_seen

            )

        )

        self.connection.commit()

    # ---------------------------------------------

    def update(self, host):

        self.cursor.execute(

            """
            UPDATE devices

            SET

                previous_ip=?,

                previous_hostname=?,

                previous_os=?,

                previous_device_type=?,

                ip=?,

                vendor=?,

                hostname=?,

                hostname_source=?,

                device_type=?,

                operating_system=?,

                os_confidence=?,

                trust_status=?,

                status=?,

                last_seen=?

            WHERE mac=?

            """,

            (

                host.ip,

                host.hostname,

                host.operating_system,

                host.device_type,

                host.ip,

                host.vendor,

                host.hostname,

                host.hostname_source,

                host.device_type,

                host.operating_system,

                host.os_confidence,

                host.trust_status,

                host.status,

                host.last_seen,

                host.mac

            )

        )

        self.connection.commit()

    # ---------------------------------------------

    def save(self, host):

        if self.device_exists(host.mac):

            self.update(host)

        else:

            self.insert(host)

    # ---------------------------------------------

    def get_all(self):

        self.cursor.execute(

            """
            SELECT *

            FROM devices

            ORDER BY ip
            """

        )

        return self.cursor.fetchall()

    # ---------------------------------------------

    def get(self, mac):

        self.cursor.execute(

            """
            SELECT *

            FROM devices

            WHERE mac=?
            """,

            (mac,)

        )

        return self.cursor.fetchone()
    

    # -------------------------------------------------

    def trust(self, mac):

        self.cursor.execute(

            """
            UPDATE devices

            SET trust_status='Trusted'

            WHERE mac=?
            """,

            (mac,)

        )

        self.db.connection.commit()


    # -------------------------------------------------

    def untrust(self, mac):

        self.cursor.execute(

            """
            UPDATE devices

            SET trust_status='Untrusted'

            WHERE mac=?
            """,

            (mac,)

        )

        self.db.connection.commit()

    # -------------------------------------------------

    def delete(self, mac):

        self.cursor.execute(

            """
            DELETE FROM devices

            WHERE mac=?
            """,

            (mac,)

        )

        self.db.connection.commit()

    # ---------------------------------------------

    def total(self):

        self.cursor.execute(

            """
            SELECT COUNT(*)

            FROM devices
            """

        )

        return self.cursor.fetchone()[0]