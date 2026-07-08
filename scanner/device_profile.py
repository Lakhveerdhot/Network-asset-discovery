"""
Device Profile Builder

Builds a complete profile for every discovered device.
"""

from scanner.models import Host


class DeviceProfileBuilder:

    def __init__(self):

        pass

    def build_profile(self, host: Host) -> dict:

        profile = {

            "ip": host.ip,

            "mac": host.mac,

            "vendor": host.vendor,

            "hostname": host.hostname,

            "hostname_source": host.hostname_source,

            "device_type": host.device_type,

            "status": host.status,

            "operating_system": host.operating_system,

            "confidence": host.os_confidence,

            "open_ports": host.open_ports,

            "services": host.services,

            "banners": host.banners

        }

        return profile