"""
Global configuration for the Network Asset Discovery Platform.
"""

from pathlib import Path

# -----------------------------
# Project Directories
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

LOG_DIR = BASE_DIR / "logs"

# -----------------------------
# Network Discovery Settings
# -----------------------------
DEFAULT_NETWORK = "192.168.31.0/24"

SCAN_TIMEOUT = 2

SCAN_RETRIES = 2

# -----------------------------
# Logging
# -----------------------------
LOG_LEVEL = "INFO"

LOG_FILE = LOG_DIR / "scanner.log"

# -----------------------------
# Port Scanner
# -----------------------------

PORT_SCAN_TIMEOUT = 0.5

MAX_PORT_THREADS = 100

COMMON_PORT_SCAN_THREADS = 20

# -----------------------------
# Banner Grabbing
# -----------------------------

BANNER_TIMEOUT = 2

BANNER_PORTS = {
    21,     # FTP
    22,     # SSH
    25,     # SMTP
    80,     # HTTP
    110,    # POP3
    143,    # IMAP
    443,    # HTTPS
    8080    # HTTP Alternate
}


# -----------------------------
# Operating System Fingerprinting
# -----------------------------

OS_DETECTION_ARGUMENTS = "-O"
ENABLE_OS_FINGERPRINTING = True

# -----------------------------
# IEEE OUI Database
# -----------------------------

OUI_DATABASE = BASE_DIR / "data" / "oui.csv"

# -----------------------------
# Scheduler
# -----------------------------
# =====================================================
# Scheduler Configuration
# =====================================================

ENABLE_SCHEDULER = True

SCAN_INTERVAL_MINUTES = 10

AUTO_START_SCHEDULER = False