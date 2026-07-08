"""
Banner Scanner
"""

import socket


class BannerScanner:

    def __init__(self, timeout=2):
        self.timeout = timeout

    def grab_banner(self, ip: str, port: int) -> str:

        try:

            with socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            ) as sock:

                sock.settimeout(self.timeout)

                sock.connect((ip, port))

                if port in [80, 8080, 8000]:

                    sock.sendall(
                        b"HEAD / HTTP/1.0\r\n\r\n"
                    )

                elif port == 443:

                    return "HTTPS"

                else:

                    return "N/A"

                banner = sock.recv(4096).decode(
                    errors="ignore"
                )

                lines = []

                for line in banner.splitlines():

                    line = line.strip()

                    if not line:
                        continue

                    if (
                        line.startswith("HTTP/")
                        or line.lower().startswith("server:")
                    ):

                        lines.append(line)

                if not lines:

                    return "N/A"

                return " | ".join(lines)

        except Exception:

            return "N/A"