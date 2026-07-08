"""
SQLite Database Manager
"""

import sqlite3
from pathlib import Path

from config.config import BASE_DIR
from database.repositories.settings_repository import SettingsRepository


DATABASE_DIR = BASE_DIR / "database"

DATABASE_DIR.mkdir(exist_ok=True)

DATABASE_FILE = DATABASE_DIR / "asset_inventory.db"


class DatabaseManager:

    def __init__(self):

        self.connection = sqlite3.connect(
            DATABASE_FILE,
            check_same_thread=False
        )
        self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

        self.create_table()

        self.initialize_scheduler()

        SettingsRepository(self).initialize()

        self.add_missing_columns()

        self.add_missing_scheduler_columns()

    # ------------------------------------------------

    def create_table(self):

    # ===================================================
    # DEVICES
    # ===================================================

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS devices(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                ip TEXT,

                mac TEXT UNIQUE,

                vendor TEXT,

                hostname TEXT,

                hostname_source TEXT,

                device_type TEXT,

                operating_system TEXT,

                os_confidence INTEGER,

                trust_status TEXT,

                status TEXT,

                first_seen TEXT,

                last_seen TEXT,

                previous_ip TEXT,

                previous_hostname TEXT,

                previous_os TEXT,

                previous_device_type TEXT

            )
            """
        )

        # ===================================================
        # PORTS
        # ===================================================

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS ports(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                mac TEXT,

                port INTEGER,

                service TEXT,

                FOREIGN KEY(mac)
                REFERENCES devices(mac)

            )
            """
        )

        # ===================================================
        # BANNERS
        # ===================================================

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS banners(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                mac TEXT,

                port INTEGER,

                banner TEXT,

                FOREIGN KEY(mac)
                REFERENCES devices(mac)

            )
            """
        )

        # ===================================================
        # CHANGE HISTORY
        # ===================================================

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS change_history(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                mac TEXT,

                change_text TEXT,

                detected_at TEXT,

                FOREIGN KEY(mac)
                REFERENCES devices(mac)

            )
            """
        )

        # ===================================================
        # SCAN HISTORY
        # ===================================================

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS scan_history(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                scan_time TEXT,

                total_hosts INTEGER,

                open_ports INTEGER,

                duration REAL

            )
            """
        )

        self.connection.commit()


        # ===================================================
        # SCHEDULER SETTINGS
        # ===================================================

        self.cursor.execute(

            """
            CREATE TABLE IF NOT EXISTS scheduler_settings(

                id INTEGER PRIMARY KEY,

                enabled INTEGER DEFAULT 1,

                interval_minutes INTEGER DEFAULT 10,

                last_enabled TEXT,

                last_updated TEXT

            )
            """

        )

        self.connection.commit()

        # ===================================================
        # SYSTEM SETTINGS
        # ===================================================

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS system_settings(

                id INTEGER PRIMARY KEY,

                target_network TEXT,

                scan_timeout INTEGER,

                port_scan_timeout REAL,

                common_threads INTEGER,

                banner_enabled INTEGER,

                os_fingerprinting_enabled INTEGER,

                vendor_lookup_enabled INTEGER,

                report_txt_enabled INTEGER,

                report_csv_enabled INTEGER,

                report_pdf_enabled INTEGER,

                last_updated TEXT

            )
            """
        )

    # ------------------------------------------------

    def add_missing_columns(self):

        self.cursor.execute(

            """
            PRAGMA table_info(devices)
            """
        )

        columns = [

            column["name"]

            for column in self.cursor.fetchall()

        ]

        new_columns = {
            "previous_ip": "TEXT",
            "previous_hostname": "TEXT",
            "previous_os": "TEXT",
            "previous_device_type": "TEXT",
            "trust_status": "TEXT DEFAULT 'Unknown'"
        }

        for column_name, column_type in new_columns.items():

            if column_name not in columns:

                self.cursor.execute(

                    f"""

                    ALTER TABLE devices

                    ADD COLUMN {column_name} {column_type}

                    """

                )

        self.connection.commit()


    # ------------------------------------------------

    def get_trust_status(self, mac):

        self.cursor.execute(

            """

            SELECT trust_status

            FROM devices

            WHERE mac=?

            """,

            (

                mac,

            )

        )

        result = self.cursor.fetchone()

        if result:

            return result["trust_status"]

        return "Unknown"

    # ------------------------------------------------

    def trust_device(self, mac):

        self.cursor.execute(

            """

            UPDATE devices

            SET trust_status='Trusted'

            WHERE mac=?

            """,

            (

                mac,

            )

        )

        self.connection.commit()

    # ------------------------------------------------

    def untrust_device(self, mac):

        self.cursor.execute(

            """

            UPDATE devices

            SET trust_status='Untrusted'

            WHERE mac=?

            """,

            (

                mac,

            )

        )

        self.connection.commit()


    # ------------------------------------------------

    def initialize_scheduler(self):

        self.cursor.execute(

            """

            SELECT COUNT(*)

            FROM scheduler_settings

            """

        )

        count = self.cursor.fetchone()[0]

        if count == 0:

            self.cursor.execute(

                """

                INSERT INTO scheduler_settings(

                    id,

                    enabled,

                    interval_minutes,

                    last_enabled,

                    last_updated

                )

                VALUES(

                    1,

                    1,

                    10,

                    datetime('now'),

                    datetime('now')

                )

                """

            )

            self.connection.commit()


    # ------------------------------------------------

    def add_missing_scheduler_columns(self):

        self.cursor.execute(

            """
            PRAGMA table_info(scheduler_settings)
            """

        )

        columns = [

            column["name"]

            for column in self.cursor.fetchall()

        ]

        new_columns = {

            "last_enabled": "TEXT"

        }

        for column_name, column_type in new_columns.items():

            if column_name not in columns:

                self.cursor.execute(

                    f"""

                    ALTER TABLE scheduler_settings

                    ADD COLUMN {column_name} {column_type}

                    """

                )

        self.connection.commit()

        self.cursor.execute(

            """

            UPDATE scheduler_settings

            SET last_enabled = datetime('now')

            WHERE last_enabled IS NULL

            """

        )

        self.connection.commit()
    # ------------------------------------------------

    def close(self):

        self.connection.close()

        
