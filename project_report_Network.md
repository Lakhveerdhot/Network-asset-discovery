# 🌐 Network Asset Discovery Platform

> A Professional Network Asset Discovery and Security Monitoring Platform built with **Python**, **Flask**, and **SQLite** for discovering, classifying, monitoring, and managing devices connected to an authorized network.

---

## 📖 Overview

The **Network Asset Discovery Platform (NADP)** is a comprehensive cybersecurity project designed to automatically discover, identify, classify, and monitor devices within an **authorized network**.

Unlike traditional network scanners that simply list active hosts, this platform builds a complete asset inventory by collecting detailed information about every discovered device, including:

- Device Identification
- Open Ports
- Running Services
- Service Banners
- Operating System
- Vendor Information
- Hostname
- Device Classification
- Trust Status
- Historical Changes

The platform also provides an interactive web dashboard for managing assets, viewing scan reports, scheduling automated scans, and monitoring network changes over time.

---

## 🎯 Objectives

The primary goals of this project are:

- Automatically discover all active devices in an authorized network.
- Build and maintain a centralized asset inventory.
- Identify running services and open ports.
- Perform OS fingerprinting and device classification.
- Track changes between scans.
- Monitor trusted and unknown devices.
- Provide a user-friendly dashboard for asset management.
- Generate professional scan reports.
- Support automated scheduled scanning.

---

# ✨ Key Features

## 🔍 Network Discovery

- ARP-based host discovery
- Detects live devices on authorized networks
- Fast subnet scanning
- Automatic device inventory generation

---

## 🌐 Port Scanning

- Multi-threaded TCP port scanning
- Detection of common network services
- Open port identification
- Service mapping

---

## 🛰 Service Detection

Automatically identifies services running on discovered ports, including:

- HTTP
- HTTPS
- DNS
- SMB
- NetBIOS
- FTP
- SSH
- SMTP
- POP3
- IMAP
- and many more.

---

## 🏷 Banner Grabbing

Collects service banners for supported ports to provide additional information about discovered services.

Examples:

- HTTP Server
- Web Server Version
- Router Firmware
- Service Headers

---

## 💻 Operating System Fingerprinting

Detects operating systems using Nmap OS fingerprinting.

Examples:

- Windows
- Linux
- OpenWrt
- Unknown Devices

---

## 🏭 Vendor Identification

Identifies device manufacturers using MAC Address OUI lookup.

Examples:

- Cisco
- Intel
- AzureWave
- Xiaomi
- TP-Link
- SERVERCOM
- and many more.

---

## 🖥 Device Classification

Automatically classifies devices such as:

- Router
- Laptop
- Desktop
- Mobile Phone
- Printer
- Server
- Unknown Device

---

## 🏠 Hostname Discovery

Supports hostname identification using:

- Reverse DNS
- NetBIOS
- mDNS
- LLMNR (where available)

---

## 🔒 Trust Management

Devices can be categorized as:

- Trusted
- Unknown
- Untrusted

Trust status can be managed directly from the web dashboard.

---

## 📊 Change Detection

Tracks changes between scans including:

- IP Address Changes
- Hostname Changes
- Operating System Changes
- Device Type Changes

All detected changes are stored for future reference.

---

## 🗄 Database Management

Uses a normalized SQLite database with separate repositories for:

- Devices
- Ports
- Banners
- Change History
- Scan History
- Scheduler Settings
- System Settings

Repository Pattern is used to keep database logic clean and maintainable.

---

## 🌍 Web Dashboard

The platform includes a modern Flask-based dashboard featuring:

- Dashboard Overview
- Asset Inventory
- Device Details
- Reports
- Scheduler
- Settings

---

## 📑 Reporting

Generates detailed scan reports containing:

- Device Information
- Open Ports
- Services
- Banners
- Operating Systems
- Vendors
- Change History
- Scan Summary

---

## ⏰ Scheduler

Built-in scheduler supports:

- Automatic Scanning
- Configurable Scan Interval
- Enable / Disable Scheduler
- Pause / Resume Functionality

---

## ⚙ Settings

The Settings module allows centralized management of:

- Target Network
- Scan Timeout
- Port Scan Timeout
- Worker Threads
- Banner Grabbing
- OS Fingerprinting
- Vendor Lookup
- Report Generation Options

---

# 🏗 System Architecture

```
                        +----------------------+
                        |    Web Dashboard     |
                        |      (Flask)         |
                        +----------+-----------+
                                   |
                                   |
                                   ▼
                    +-----------------------------+
                    |      Scan Engine            |
                    +-----------------------------+
                                   |
        -------------------------------------------------------------
        |             |             |              |                 |
        ▼             ▼             ▼              ▼                 ▼
 Network Discovery  Port Scan   Banner Grab   OS Detection   Vendor Lookup
        |             |             |              |                 |
        -------------------------------------------------------------
                                   |
                                   ▼
                      Device Classification
                                   |
                                   ▼
                        Device Profiling
                                   |
                                   ▼
                         Change Detection
                                   |
                                   ▼
                     Repository Layer (SQLite)
                                   |
        -------------------------------------------------------------
        |           |            |            |          |           |
        ▼           ▼            ▼            ▼          ▼           ▼
     Devices      Ports       Banners     Changes    Scans     Settings
```

---

# 📂 Project Structure

```text
network-asset-discovery/
│
├── config/
├── dashboard/
├── data/
├── database/
│   ├── repositories/
│   │   ├── banner_repository.py
│   │   ├── change_repository.py
│   │   ├── device_repository.py
│   │   ├── port_repository.py
│   │   ├── scan_repository.py
│   │   ├── scheduler_repository.py
│   │   └── settings_repository.py
│   │
│   ├── asset_inventory.db
│   └── database_manager.py
│
├── generated-reports/
├── logs/
├── models/
├── scanner/
├── scheduler/
├── services/
├── utils/
├── web/
│   ├── static/
│   └── templates/
│
├── main.py
├── run_scheduler.py
├── requirements.txt
└── README.md
```
---

# ⚙ Prerequisites

Before running the project, ensure that the following software is installed on your system.

## Software Requirements

- Python 3.10 or later
- Nmap
- Git
- Visual Studio Code (Recommended)

---

# 📦 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/network-asset-discovery.git

cd network-asset-discovery
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Verify Nmap Installation

Windows

```bash
nmap --version
```

Linux

```bash
sudo apt install nmap

nmap --version
```

---

# 📁 Project Configuration

Most project settings are available through the **Settings** page in the web dashboard.

Default values include:

| Setting | Default Value |
|----------|---------------|
| Target Network | 192.168.31.0/24 |
| Scan Timeout | 2 sec |
| Port Timeout | 0.5 sec |
| Worker Threads | 20 |
| Banner Grabbing | Enabled |
| OS Fingerprinting | Enabled |
| Vendor Lookup | Enabled |

---

# ▶ Running the Scanner

To perform a manual network scan:

```bash
python main.py
```

The scanner performs the following operations:

1. Discover live devices.
2. Scan common TCP ports.
3. Detect running services.
4. Grab service banners.
5. Perform OS fingerprinting.
6. Detect vendor information.
7. Discover hostnames.
8. Classify device types.
9. Detect network changes.
10. Save data into the database.
11. Generate a detailed scan report.

---

# 🌐 Running the Web Dashboard

Start the Flask web application.

```bash
python -m web.app
```

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

The dashboard provides access to:

- Dashboard
- Assets
- Device Details
- Reports
- Scheduler
- Settings

---

# ⏰ Running the Scheduler

To start automatic network monitoring:

```bash
python run_scheduler.py
```

The scheduler continuously monitors the database configuration and automatically performs scans based on the configured interval.

Features include:

- Enable Scheduler
- Disable Scheduler
- Pause Scheduler
- Resume Scheduler
- Configurable Scan Interval

---

# 📂 Generated Reports

Every completed scan automatically generates a report.

Reports are stored inside:

```text
generated-reports/
```

Each report contains:

- Scan Summary
- Device Inventory
- Open Ports
- Services
- Banner Information
- Operating System
- Vendor Information
- Change Detection Results

---

# 🗄 Database

The platform stores scan results inside a normalized SQLite database.

Database file:

```text
database/
└── asset_inventory.db
```

The database automatically stores:

- Device Inventory
- Port Information
- Banner Information
- Change History
- Scan History
- Scheduler Settings
- System Settings

---

# 📊 Dashboard Modules

## Dashboard

Provides an overview of:

- Total Devices
- Trusted Devices
- Unknown Devices
- Untrusted Devices
- Recent Scan History

---

## Assets

Displays the complete asset inventory with filtering and search capabilities.

Information includes:

- IP Address
- Hostname
- Vendor
- Device Type
- Operating System
- Trust Status

---

## Device Details

Each discovered device includes:

- IP Address
- MAC Address
- Hostname
- Vendor
- Device Type
- Operating System
- Trust Status
- Open Ports
- Port Banners
- Change History

---

## Reports

Manage generated scan reports.

Supported actions:

- View Report
- Download Report
- Delete Report

---

## Scheduler

Monitor and control automatic scans.

Capabilities:

- Enable Scheduler
- Disable Scheduler
- Configure Scan Interval
- View Last Scan
- View Next Scheduled Scan

---

## Settings

Configure scanner behavior directly from the dashboard.

Available settings include:

- Target Network
- Scan Timeout
- Port Timeout
- Thread Count
- Banner Grabbing
- OS Fingerprinting
- Vendor Lookup
- Report Preferences

---
---

# 🔄 Complete Scan Workflow

The following diagram illustrates the complete workflow of the Network Asset Discovery Platform.

```text
                     User Starts Scan
                             │
                             ▼
                Validate Target Network
                             │
                             ▼
                 ARP Host Discovery
                             │
                             ▼
             Detect Active Network Devices
                             │
                             ▼
              Multi-threaded Port Scanning
                             │
                             ▼
                Service Identification
                             │
                             ▼
                 Banner Grabbing
                             │
                             ▼
            Operating System Detection
                             │
                             ▼
               Vendor Identification
                             │
                             ▼
               Hostname Discovery
                             │
                             ▼
             Device Classification
                             │
                             ▼
              Device Profile Creation
                             │
                             ▼
                Change Detection
                             │
                             ▼
             Store Data in SQLite Database
                             │
                             ▼
              Generate Scan Report
                             │
                             ▼
           Update Web Dashboard
```

---

# 🗄 Database Design

The application uses a normalized SQLite database.

## Devices Table

Stores the primary inventory of discovered devices.

| Column |
|---------|
| id |
| ip |
| mac |
| vendor |
| hostname |
| hostname_source |
| device_type |
| operating_system |
| os_confidence |
| trust_status |
| status |
| first_seen |
| last_seen |
| previous_ip |
| previous_hostname |
| previous_os |
| previous_device_type |

---

## Ports Table

Stores open ports discovered during scans.

| Column |
|---------|
| id |
| mac |
| port |
| service |

---

## Banners Table

Stores service banners collected during banner grabbing.

| Column |
|---------|
| id |
| mac |
| port |
| banner |

---

## Change History Table

Stores detected changes between scans.

Examples include:

- IP Address Changed
- Hostname Changed
- Device Type Changed
- Operating System Changed

---

## Scan History Table

Stores historical scan information.

| Column |
|---------|
| id |
| scan_time |
| total_hosts |
| open_ports |
| duration |

---

## Scheduler Settings

Stores scheduler configuration.

Examples:

- Enabled
- Interval
- Last Enabled
- Last Updated

---

## System Settings

Stores configurable application settings.

Examples:

- Target Network
- Scan Timeout
- Port Timeout
- Worker Threads
- Banner Grabbing
- Vendor Lookup
- OS Fingerprinting
- Report Preferences

---

# 📚 Repository Pattern

The project follows the Repository Pattern to separate database operations from business logic.

```text
Database Manager
        │
        ▼
Repositories
        │
        ├── Device Repository
        ├── Port Repository
        ├── Banner Repository
        ├── Change Repository
        ├── Scan Repository
        ├── Scheduler Repository
        └── Settings Repository
```

Benefits include:

- Better maintainability
- Easier testing
- Cleaner project structure
- Separation of concerns
- Scalable architecture

---

# 🧩 Technologies Used

## Programming Language

- Python 3

---

## Backend

- Flask

---

## Database

- SQLite

---

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Jinja2 Templates

---

## Networking Libraries

- Scapy
- Python-Nmap
- Socket Programming

---

## Additional Libraries

- ReportLab
- Requests
- Colorama

---

# 📁 Reports

Each completed scan generates a detailed report containing:

- Network Summary
- Device Inventory
- Open Ports
- Service Detection
- Banner Information
- Operating System Details
- Vendor Information
- Change Detection Summary

Reports are automatically saved inside:

```text
generated-reports/
```

---

# 📸 Screenshots

> The following screenshots demonstrate different modules of the application.

## Dashboard

_Add dashboard screenshot here._

---

## Assets

_Add assets page screenshot here._

---

## Device Details

_Add device details screenshot here._

---

## Reports

_Add reports page screenshot here._

---

## Scheduler

_Add scheduler screenshot here._

---

## Settings

_Add settings screenshot here._

---

# ⚠ Legal Notice

This project is intended **only for authorized networks**.

The application must be used exclusively on networks for which you have explicit permission.

The author does **not** encourage or support unauthorized scanning, intrusion, or any activity that violates applicable laws or organizational policies.

Users are solely responsible for ensuring that the software is used in a lawful and ethical manner.

---

# 🛡 Security Considerations

This platform is designed as a **defensive cybersecurity tool**.

It is intended to assist with:

- Asset Inventory
- Network Visibility
- Device Identification
- Security Auditing
- Network Monitoring

It is **not** intended for offensive or unauthorized use.

---

# 🚀 Future Improvements

Potential future enhancements include:

- CSV and PDF report generation
- Interactive charts and analytics
- REST API
- Authentication and role-based access control
- Email notifications
- Multi-network support
- Docker deployment
- PostgreSQL/MySQL support

---

# 🤝 Contributing

Contributions, feature suggestions, and bug reports are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a Pull Request.

---

# 👨‍💻 Author

**Lakhveer Singh**

B.Tech – Computer Science & Engineering

Cybersecurity Enthusiast

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and supports future development.

---

# 📄 License

This project is released under the **MIT License**.

You are free to use, modify, and distribute this project in accordance with the terms of the license.