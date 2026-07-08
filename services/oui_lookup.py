"""
IEEE OUI Lookup
"""

import csv

from config.config import OUI_DATABASE


class OUILookup:

    def __init__(self):

        self.database = {}

        self.load_database()

    def load_database(self):

        with open(
            OUI_DATABASE,
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                oui = row["Assignment"].upper()

                vendor = row["Organization Name"]

                self.database[oui] = vendor

    def lookup(self, mac: str) -> str:

        if not mac:

            return "Unknown"

        oui = (
            mac.replace(":", "")
               .replace("-", "")
               .upper()[:6]
        )

        return self.database.get(
            oui,
            "Unknown"
        )