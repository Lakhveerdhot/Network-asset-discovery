"""
Hostname Resolver

Supports:
- Reverse DNS
- NetBIOS
"""

import socket

from nmb.NetBIOS import NetBIOS


class HostnameResolver:

    def reverse_dns(self, ip: str):

        try:

            hostname, _, _ = socket.gethostbyaddr(ip)
            hostname = self.clean_hostname(hostname)
            return hostname, "Reverse DNS"
        
        except (
            socket.herror,
            socket.gaierror,
            TimeoutError,
            OSError
        ):

            return "Unknown", "Unknown"

    def netbios(self, ip: str):

        try:

            netbios = NetBIOS()

            names = netbios.queryIPForName(ip)

            netbios.close()

            if names:

                hostname = self.clean_hostname(names[0])
                return hostname, "NetBIOS"

        except Exception:

            pass

        return "Unknown", "Unknown"
    
    
    def clean_hostname(self, hostname: str) -> str:
        hostname = hostname.replace(".local.html", "")
        hostname = hostname.replace(".local", "")
        hostname = hostname.replace(".lan", "")
        hostname = hostname.replace(".home", "")
        hostname = hostname.strip()
        return hostname