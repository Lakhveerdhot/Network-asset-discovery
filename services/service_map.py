"""
Service Mapping

Maps well-known TCP ports to their default service names.
"""

SERVICE_MAP = {

    # File Transfer
    20: "FTP-DATA",
    21: "FTP",

    # Remote Access
    22: "SSH",
    23: "TELNET",

    # Mail
    25: "SMTP",
    110: "POP3",
    143: "IMAP",
    993: "IMAPS",
    995: "POP3S",

    # DNS
    53: "DNS",

    # Web
    80: "HTTP",
    443: "HTTPS",
    8080: "HTTP-ALT",

    # Windows
    135: "MSRPC",
    139: "NETBIOS",
    445: "SMB",

    # Database
    1433: "MSSQL",
    1521: "ORACLE",
    3306: "MYSQL",
    5432: "POSTGRESQL",

    # Remote Desktop
    3389: "RDP",

    # Remote Desktop (Linux)
    5900: "VNC",

    # Cache
    6379: "REDIS"

}