"""
Network utility functions.
"""

import ipaddress


def validate_network(network: str) -> bool:
    """
    Validate CIDR notation.
    """
    try:
        ipaddress.ip_network(network)
        return True
    except ValueError:
        return False


def get_network(network: str):
    """
    Return an IPv4Network object.
    """
    return ipaddress.ip_network(network, strict=False)


def get_hosts(network: str):
    """
    Return all usable host IP addresses.
    """
    net = get_network(network)
    return [str(ip) for ip in net.hosts()]