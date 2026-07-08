"""
Vendor Scanner

Looks up the vendor name using the device's MAC address.
"""

from services.oui_lookup import OUILookup
from scanner.models import Host


class VendorScanner:

    def __init__(self):

        self.lookup = OUILookup()

    def scan_host(self, host: Host) -> Host:

        host.vendor = self.lookup.lookup(
            host.mac
        )

        return host