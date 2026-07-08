"""
Rule Loader

Loads all CSV rule files into memory.
"""

import csv
from pathlib import Path

from config.config import BASE_DIR


DATA_DIR = BASE_DIR / "data"


class RuleLoader:

    def __init__(self):

        self.hostname_rules = {}

        self.vendor_rules = {}

        self.os_rules = {}

        self.port_rules = {}

        self.service_rules = {}

        self.banner_rules = {}

        self.device_aliases = {}

        self.load_all_rules()

    # ---------------------------------------
    # Generic Keyword Loader
    # ---------------------------------------

    def load_keyword_rules(self, filename):

        rules = {}

        filepath = DATA_DIR / filename

        with open(
            filepath,
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                keyword = row["Keyword"].strip().upper()

                device_type = row["DeviceType"].strip()

                rules[keyword] = device_type

        return rules

    # ---------------------------------------
    # Port Loader
    # ---------------------------------------

    def load_port_rules(self):

        rules = {}

        filepath = DATA_DIR / "port_rules.csv"

        with open(
            filepath,
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                port = int(row["Port"])

                device = row["DeviceType"].strip()

                rules[port] = device

        return rules

    # ---------------------------------------
    # Device Alias Loader
    # ---------------------------------------

    def load_aliases(self):

        aliases = {}

        filepath = DATA_DIR / "device_aliases.csv"

        with open(
            filepath,
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                keyword = row["Keyword"].strip().upper()

                canonical = row["CanonicalName"].strip()

                aliases[keyword] = canonical

        return aliases

    # ---------------------------------------
    # Load Everything
    # ---------------------------------------

    def load_all_rules(self):

        self.hostname_rules = self.load_keyword_rules(
            "hostname_rules.csv"
        )

        self.vendor_rules = self.load_keyword_rules(
            "vendor_rules.csv"
        )

        self.os_rules = self.load_keyword_rules(
            "os_rules.csv"
        )

        self.service_rules = self.load_keyword_rules(
            "service_rules.csv"
        )

        self.banner_rules = self.load_keyword_rules(
            "banner_rules.csv"
        )

        self.port_rules = self.load_port_rules()

        self.device_aliases = self.load_aliases()