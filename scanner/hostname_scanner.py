"""
Hostname Scanner
"""

from scanner.models import Host
from services.hostname_resolver import HostnameResolver


class HostnameScanner:

    def __init__(self):

        self.resolver = HostnameResolver()

    def scan_host(self, host: Host) -> Host:

        hostname, source = self.resolver.reverse_dns(
            host.ip
        )

        if hostname == "Unknown":

            hostname, source = self.resolver.netbios(
                host.ip
            )

        host.hostname = hostname

        host.hostname_source = source

        return host