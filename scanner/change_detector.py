"""
Change Detection Engine
"""

from database.database_manager import DatabaseManager


class ChangeDetector:

    def __init__(self):

        self.database = DatabaseManager()

    def detect_changes(self, host):

        self.database.cursor.execute(

            """

            SELECT *

            FROM devices

            WHERE mac = ?

            """,

            (

                host.mac,

            )

        )

        previous = self.database.cursor.fetchone()

        changes = []

        if previous is None:

            changes.append(

                "[NEW DEVICE]"

            )

            return changes

        if previous["ip"] != host.ip:

            changes.append(

                f"IP Changed : {previous['ip']} -> {host.ip}"

            )

        if previous["hostname"] != host.hostname:

            changes.append(

                f"Hostname Changed : {previous['hostname']} -> {host.hostname}"

            )

        if previous["operating_system"] != host.operating_system:

            changes.append(

                f"OS Changed : {previous['operating_system']} -> {host.operating_system}"

            )

        if previous["device_type"] != host.device_type:

            changes.append(

                f"Device Type Changed : {previous['device_type']} -> {host.device_type}"

            )

        return changes