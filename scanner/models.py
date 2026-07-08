from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Host:

    ip: str

    mac: str

    status: str = "Alive"

    open_ports: list[int] = field(default_factory=list)

    services: dict[int, str] = field(default_factory=dict)

    banners: dict[int, str] = field(default_factory=dict)

    operating_system: str = "Unknown"

    os_confidence: int = 0

    vendor: str = "Unknown"

    hostname: str = "Unknown"

    hostname_source: str = "Unknown"

    device_type: str = "Unknown"

    trust_status: str = "Unknown"

    ports: list = field(default_factory=list)

    banner_history: list = field(default_factory=list)

    change_history: list = field(default_factory=list)

    first_seen: str = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    last_seen: str = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    profile: dict = field(default_factory=dict)

    changes: list = field(default_factory=list)