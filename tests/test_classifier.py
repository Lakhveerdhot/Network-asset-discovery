from scanner.models import Host
from scanner.device_classifier import DeviceClassifier

host = Host(
    ip="192.168.31.46",
    mac="B4:8C:9D:D6:FF:77"
)

host.hostname = "LAPTOP-32CUAGJ2"

host.vendor = "AzureWave Technology Inc."

host.operating_system = "Microsoft Windows 11"

host.open_ports = [135, 139, 445]

host.services = {
    135: "MSRPC",
    139: "NETBIOS",
    445: "SMB"
}

classifier = DeviceClassifier()

host = classifier.classify(host)

print()

print("Device Type :", host.device_type)