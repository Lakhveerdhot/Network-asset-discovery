"""
Validation helpers.
"""

from scanner.network import validate_network


def validate_target_network(network: str) -> None:
    """
    Raise an exception if the supplied network is invalid.
    """
    if not validate_network(network):
        raise ValueError(
            f"Invalid network: {network}"
        )