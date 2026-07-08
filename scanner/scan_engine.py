"""
Network Scan Engine
"""

import time
import ipaddress

from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed,
)

from config.config import (
    DEFAULT_NETWORK,
    PORT_SCAN_TIMEOUT,
    COMMON_PORT_SCAN_THREADS,
    BANNER_PORTS,
    ENABLE_OS_FINGERPRINTING,
)

from services.common_ports import COMMON_TCP_PORTS
from scanner.discovery import NetworkDiscovery
from scanner.port_scanner import PortScanner
from scanner.service_scanner import ServiceScanner
from scanner.banner_scanner import BannerScanner
from scanner.os_fingerprinter import OSFingerprinter
from scanner.vendor_scanner import VendorScanner
from scanner.hostname_scanner import HostnameScanner
from scanner.device_classifier import DeviceClassifier
from scanner.device_profile import DeviceProfileBuilder
from scanner.change_detector import ChangeDetector
from scanner.trust_manager import TrustManager
from database.database_manager import DatabaseManager
from utils.report_generator import ReportGenerator
from utils.validators import validate_target_network
from utils.logger import setup_logger
from database.repositories.device_repository import DeviceRepository
from database.repositories.port_repository import PortRepository
from database.repositories.banner_repository import BannerRepository
from database.repositories.change_repository import ChangeRepository
from database.repositories.scan_repository import ScanRepository
from utils.display import (
    print_banner,
    display_results,
)

logger = setup_logger()


class ScanEngine:

    def __init__(self):

        self.network_scanner = NetworkDiscovery(
            DEFAULT_NETWORK
        )

        self.port_scanner = PortScanner(
            timeout=PORT_SCAN_TIMEOUT
        )

        self.service_scanner = ServiceScanner()

        self.banner_scanner = BannerScanner()

        self.vendor_scanner = VendorScanner()

        self.hostname_scanner = HostnameScanner()

        self.device_classifier = DeviceClassifier()

        self.profile_builder = DeviceProfileBuilder()

        self.change_detector = ChangeDetector()

        self.database = DatabaseManager()
        
        self.trust_manager = TrustManager()

        self.report_generator = ReportGenerator()

        self.device_repo = DeviceRepository(self.database)

        self.port_repo = PortRepository(self.database)

        self.banner_repo = BannerRepository(self.database)

        self.change_repo = ChangeRepository(self.database)

        self.scan_repo = ScanRepository(self.database)

        self.os_scanner = None

        if ENABLE_OS_FINGERPRINTING:

            self.os_scanner = OSFingerprinter()


    def run(self):

        start = time.perf_counter()

        print_banner()

        validate_target_network(DEFAULT_NETWORK)

        hosts = self.network_scanner.scan()

        print("\nStarting Port Scan...\n")

        with ThreadPoolExecutor(
            max_workers=COMMON_PORT_SCAN_THREADS
        ) as executor:

            futures = {

                executor.submit(

                    self.port_scanner.scan_host,

                    host,

                    COMMON_TCP_PORTS

                ): host

                for host in hosts

            }

            updated_hosts = []

            total_hosts = len(futures)

            completed = 0

            for future in as_completed(futures):

                host = future.result()

                host = self.service_scanner.scan_host(host)

                for port in host.open_ports:

                    if port not in BANNER_PORTS:

                        continue

                    banner = self.banner_scanner.grab_banner(

                        host.ip,

                        port

                    )

                    host.banners[port] = banner

                if ENABLE_OS_FINGERPRINTING:

                    host = self.os_scanner.fingerprint(host)

                host = self.vendor_scanner.scan_host(host)

                host = self.hostname_scanner.scan_host(host)

                host = self.device_classifier.classify(host)

                host.profile = self.profile_builder.build_profile(host)

                host.changes = self.change_detector.detect_changes(host)

                host.trust_status = self.trust_manager.get_status(

                    host.mac

                )

                host.last_seen = time.strftime(

                    "%Y-%m-%d %H:%M:%S"

                )

                self.device_repo.save(host)
                self.port_repo.save(host)
                self.banner_repo.save(host)
                self.change_repo.save(host)

                completed += 1

                print(

                    f"[{completed}/{total_hosts}] "

                    f"{host.ip:<15} | "

                    f"{host.device_type:<15} | "

                    f"{host.vendor[:25]:<25} | "

                    f"{len(host.open_ports)} Open Ports"

                )

                updated_hosts.append(host)

        hosts = updated_hosts

        hosts.sort(

            key=lambda host: ipaddress.ip_address(host.ip)

        )

        total_ports_tested = (

            len(hosts)

            * len(COMMON_TCP_PORTS)

        )

        total_open_ports = sum(

            len(host.open_ports)

            for host in hosts

        )

        display_results(hosts)



        print()
        print("=" * 70)
        print("CHANGE DETECTION")
        print("=" * 70)
        changes_found = False

        for host in hosts:

            if host.changes:

                changes_found = True

                print()

                print(host.hostname)

                for change in host.changes:

                    print(f"  • {change}")

        if not changes_found:

            print()

            print("No Changes Detected.")

        print("=" * 70)

        end = time.perf_counter()

        known_vendors = sum(

            1

            for host in hosts

            if host.vendor != "Unknown"

        )

        total_changes = sum(

            len(host.changes)

            for host in hosts

        )

        self.scan_repo.save(
            total_hosts=len(hosts),
            total_open_ports=total_open_ports,
            duration=end-start
        )

        report_path = self.report_generator.generate(

            hosts=hosts,

            target_network=DEFAULT_NETWORK,

            total_ports_tested=total_ports_tested,

            total_open_ports=total_open_ports,

            known_vendors=known_vendors,

            duration=end-start,

            database_records=self.device_repo.total(),

            total_changes=total_changes

        )

        print()

        print(f"Report Saved : {report_path}")

        print()

        print("=" * 60)

        print("Scan Summary")

        print("=" * 60)

        print(f"Target Network : {DEFAULT_NETWORK}")

        print(f"Hosts Scanned  : {len(hosts)}")

        print(f"Ports Tested   : {total_ports_tested}")

        print(f"Open Ports     : {total_open_ports}")

        print(f"Known Vendors  : {known_vendors}")

        print(

            f"Database Records : "

            f"{self.device_repo.total()}"

        )

        print(

            f"Changes Detected : "

            f"{total_changes}"

        )

        print(

            f"Duration       : "

            f"{end-start:.2f} sec"

        )

        print("Status         : Completed")

        print("=" * 60)

        self.database.close()

        logger.info(

            "Discovery Complete"

        )

        return hosts