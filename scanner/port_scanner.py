"""
TCP Connect Port Scanner
"""

import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

from scanner.models import Host
from config.config import MAX_PORT_THREADS


class PortScanner:

    def __init__(self, timeout=0.5):
        self.timeout = timeout

    def scan_single_port(self, ip: str, port: int):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(self.timeout)

        result = sock.connect_ex((ip, port))

        sock.close()

        return port if result == 0 else None

    def scan_host(self, host: Host, ports: list[int]) -> Host:

        open_ports = []

        with ThreadPoolExecutor(
            max_workers=MAX_PORT_THREADS
        ) as executor:

            futures = {
                executor.submit(
                    self.scan_single_port,
                    host.ip,
                    port
                ): port
                for port in ports
            }

            for future in as_completed(futures):

                result = future.result()

                if result is not None:

                    open_ports.append(result)

        open_ports.sort()

        host.open_ports = open_ports

        return host