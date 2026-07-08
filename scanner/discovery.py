"""
ARP-based network discovery.
"""

from typing import List

from scapy.all import ARP, Ether, srp

from scanner.models import Host
from config.config import SCAN_TIMEOUT
from utils.logger import setup_logger

logger = setup_logger()


class NetworkDiscovery:
    """
    Performs ARP discovery on a local network.
    """

    def __init__(self, network: str):
        self.network = network

    def scan(self) -> List[Host]:
        """
        Scan the supplied network using ARP.
        """

        logger.info(f"Starting ARP discovery on {self.network}")

        arp_request = ARP(pdst=self.network)

        broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")

        packet = broadcast / arp_request

        answered, unanswered = srp(
            packet,
            timeout=SCAN_TIMEOUT,
            verbose=False
        )

        hosts: List[Host] = []

        for _, response in answered:

            host = Host(
                ip=response.psrc,
                mac=response.hwsrc
            )

            hosts.append(host)

        logger.info(f"Discovered {len(hosts)} live hosts.")

        return hosts