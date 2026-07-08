"""
Device Classification Engine
"""

from collections import Counter

from scanner.models import Host
from services.rule_loader import RuleLoader


class DeviceClassifier:

    def __init__(self):

        self.loader = RuleLoader()

    def classify(self, host: Host) -> Host:

        matches = []

        # -----------------------------------
        # Hostname Rules
        # -----------------------------------

        hostname = host.hostname.upper()

        for keyword, device in self.loader.hostname_rules.items():

            if keyword in hostname:

                matches.append(device)

        # -----------------------------------
        # Vendor Rules
        # -----------------------------------

        vendor = host.vendor.upper()

        for keyword, device in self.loader.vendor_rules.items():

            if keyword in vendor:

                matches.append(device)

        # -----------------------------------
        # Operating System Rules
        # -----------------------------------

        operating_system = host.operating_system.upper()

        for keyword, device in self.loader.os_rules.items():

            if keyword in operating_system:

                matches.append(device)

        # -----------------------------------
        # Port Rules
        # -----------------------------------

        for port in host.open_ports:

            if port in self.loader.port_rules:

                matches.append(
                    self.loader.port_rules[port]
                )

        # -----------------------------------
        # Service Rules
        # -----------------------------------

        for service in host.services.values():

            service = service.upper()

            for keyword, device in self.loader.service_rules.items():

                if keyword in service:

                    matches.append(device)

        # -----------------------------------
        # Banner Rules
        # -----------------------------------

        for banner in host.banners.values():

            banner = banner.upper()

            for keyword, device in self.loader.banner_rules.items():

                if keyword in banner:

                    matches.append(device)

        # -----------------------------------
        # Final Decision
        # -----------------------------------

        if matches:

            counter = Counter(matches)

            host.device_type = counter.most_common(1)[0][0]

        else:

            host.device_type = "Unknown"

        return host