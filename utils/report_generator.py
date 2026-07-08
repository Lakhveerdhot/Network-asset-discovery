"""
Text Report Generator
"""

from pathlib import Path
from datetime import datetime

from config.config import BASE_DIR

REPORT_DIR = BASE_DIR / "generated-reports"
REPORT_DIR.mkdir(exist_ok=True)

class ReportGenerator:

    def __init__(self):

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.report_path = REPORT_DIR / f"network_report_{timestamp}.txt"

    def generate(
    self,
    hosts,
    target_network,
    total_ports_tested,
    total_open_ports,
    known_vendors,
    duration,
    database_records,
    total_changes
    ):

        with open(
            self.report_path,
            "w",
            encoding="utf-8"
        ) as report:

            report.write("=" * 70 + "\n")
            report.write(
                "NETWORK ASSET DISCOVERY PLATFORM\n"
            )
            report.write(
                "Professional Network Asset Discovery Report\n"
            )
            report.write("=" * 70 + "\n\n")


            report.write(
                f"Generated On : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n"
            )

            report.write(
                f"Target Network : {target_network}\n\n"
            )

            for host in hosts:

                report.write("=" * 70 + "\n")

                report.write(f"{'IP Address':<18}: {host.ip}\n")

                report.write(f"{'MAC Address':<18}: {host.mac}\n")

                report.write("\n")

                report.write("=" * 25 + "\n")

                report.write("DEVICE PROFILE\n")

                report.write("=" * 25 + "\n")

                report.write(f"{'Vendor':<18}: {host.vendor}\n")

                report.write(f"{'Hostname':<18}: {host.hostname}\n")

                report.write(f"{'Source':<18}: {host.hostname_source}\n")

                report.write(f"{'Device Type':<18}: {host.device_type}\n")

                report.write(f"{'Status':<18}: {host.status}\n")

                report.write(f"{'Trust Status':<18}: {host.trust_status}\n")

                report.write(f"{'Operating System':<18}: {host.operating_system}\n")

                if host.os_confidence > 0:

                    report.write(
                        f"{'Confidence':<18}: {host.os_confidence}%\n"
                    )

                else:

                    report.write(
                        f"{'Confidence':<18}: N/A\n"
                    )

                report.write("\n")

                report.write(
                    f"{'PORT':<10}"
                    f"{'SERVICE':<20}"
                    f"{'BANNER'}\n"
                )

                report.write("-" * 70 + "\n")

                if host.open_ports:

                    for port in host.open_ports:

                        service = host.services.get(
                            port,
                            "UNKNOWN"
                        )

                        banner = host.banners.get(
                            port,
                            "N/A"
                        )

                        report.write(
                            f"{port:<10}"
                            f"{service:<20}"
                            f"{banner}\n"
                        )

                else:

                    report.write(
                        "No Open Ports Found\n"
                    )

                report.write("\n")

                if host.changes:
                    report.write("\n")
                    report.write("Changes\n")
                    report.write("-" * 40 + "\n")
                    for change in host.changes:
                        report.write(f"{change}\n")
                    report.write("\n")


            report.write("=" * 70 + "\n")
            report.write("Scan Summary\n")
            report.write("=" * 70 + "\n")

            report.write(
                f"Target Network : {target_network}\n"
            )

            report.write(
                f"Hosts Scanned  : {len(hosts)}\n"
            )

            report.write(
                f"Ports Tested   : {total_ports_tested}\n"
            )

            report.write(
                f"Open Ports     : {total_open_ports}\n"
            )

            report.write(
                f"Known Vendors  : {known_vendors}\n"
            )

            report.write(
                f"Database Records : {database_records}\n"
            )

            report.write(
                f"Changes Detected : {total_changes}\n"
            )

            report.write(
                f"Duration       : {duration:.2f} sec\n"
            )

            report.write(
                "Status         : Completed\n"
            )

            report.write("=" * 70 + "\n")

        return self.report_path