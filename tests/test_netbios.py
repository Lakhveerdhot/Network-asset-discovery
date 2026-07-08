from scanner.models import Host
from scanner.hostname_scanner import HostnameScanner

host = Host(
    ip="192.168.31.46",
    mac="B4:8C:9D:D6:FF:77"
)

scanner = HostnameScanner()

host = scanner.scan_host(host)

print()

print("Hostname :", host.hostname)

print("Source   :", host.hostname_source)