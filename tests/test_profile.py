from scanner.models import Host
from scanner.device_profile import DeviceProfileBuilder

host = Host(
    ip="192.168.31.46",
    mac="B4:8C:9D:D6:FF:77"
)

host.vendor = "AzureWave Technology Inc."

host.operating_system = "Windows 11"

host.os_confidence = 97

host.open_ports = [135, 139, 445]

host.services = {
    135: "MSRPC",
    139: "NETBIOS",
    445: "SMB"
}

builder = DeviceProfileBuilder()

profile = builder.build_profile(host)

print(profile)