from scanner.models import Host
from scanner.port_scanner import PortScanner

host = Host(
    ip="192.168.31.1",
    mac="AA:BB:CC:DD"
)

scanner = PortScanner()

updated_host = scanner.scan_host(
    host,
    [22,80,443]
)

print(updated_host.open_ports)