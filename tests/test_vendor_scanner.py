from scanner.models import Host
from scanner.vendor_scanner import VendorScanner

host = Host(
    ip="192.168.31.46",
    mac="B4:8C:9D:D6:FF:77"
)

scanner = VendorScanner()

host = scanner.scan_host(host)

print(host.vendor)