"""
Operating System Fingerprinter
"""

import nmap


class OSFingerprinter:

    def __init__(self):

        self.scanner = nmap.PortScanner()

    def fingerprint(self, host):

        try:

            self.scanner.scan(
                host.ip,
                arguments="-O"
            )

            result = self.scanner[host.ip]

            if "osmatch" in result:
                matches = result["osmatch"]
                if matches:
                    best = matches[0]
                    accuracy = int(best["accuracy"])
                    # Ignore weak guesses
                    if accuracy >= 90:
                        host.operating_system = best["name"]
                        host.os_confidence = accuracy
                    else:
                        host.operating_system = "Unknown"
                        host.os_confidence = 0

            return host

        except Exception:

            host.operating_system = "Unknown"

            host.os_confidence = 0

            return host