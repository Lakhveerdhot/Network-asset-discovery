from scanner.models import Host
from scanner.os_fingerprinter import OSFingerprinter

host = Host(
    ip="192.168.31.46",
    mac="AA:BB:CC"
)

fingerprinter = OSFingerprinter()

host = fingerprinter.fingerprint(host)

print(host.operating_system)

print(host.os_confidence)