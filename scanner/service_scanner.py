"""
Service Scanner

Converts open ports into service names.
"""

from services.service_map import SERVICE_MAP


class ServiceScanner:

    def __init__(self):

        pass

    def get_service_name(self, port: int) -> str:
        """
        Return service name for a port.
        """

        return SERVICE_MAP.get(port, "UNKNOWN")

    def scan_host(self, host):

        services = {}

        for port in host.open_ports:

            services[port] = self.get_service_name(port)

        host.services = services

        return host