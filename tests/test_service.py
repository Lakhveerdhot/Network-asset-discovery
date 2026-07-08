from scanner.models import Host
from scanner.service_scanner import ServiceScanner

host = Host(
    ip="192.168.31.1",
    mac="AA:BB:CC"
)

host.open_ports = [
    53,
    80,
    443,
    8080
]

scanner = ServiceScanner()

host = scanner.scan_host(host)

print(host.services)