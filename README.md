# 🌐 Network Asset Discovery Platform

A **Python-based Network Asset Discovery and Security Monitoring Platform** that automatically discovers, identifies, classifies, and manages devices connected to an **authorized network**.

The platform combines **network discovery**, **asset inventory**, **port scanning**, **service detection**, **OS fingerprinting**, and a **Flask web dashboard** to provide a centralized view of network assets.

> ⚠️ This project is intended **only for authorized networks**. Always ensure you have permission before scanning any network.

---

# 🚀 Features

- 🔍 ARP-based Network Discovery
- 🌐 Multi-threaded TCP Port Scanning
- 🛰 Service Detection
- 🏷 Banner Grabbing
- 💻 Operating System Fingerprinting
- 🏭 Vendor Identification (IEEE OUI Lookup)
- 🏠 Hostname Discovery
- 🖥 Automatic Device Classification
- 📊 Device Profiling
- 🔄 Change Detection
- 🔒 Trust Management
- 🗄 Normalized SQLite Database
- 🌍 Flask Web Dashboard
- 📑 Report Generation
- ⏰ Automated Scheduler
- ⚙ Centralized Settings Management

---

# 🏗 Architecture

```text
                 User
                   │
                   ▼
          Flask Web Dashboard
                   │
                   ▼
             Scan Engine
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
 Network Discovery  Port Scan  Service Detection
        │
        ▼
 Banner Grabbing
        │
        ▼
 OS Fingerprinting
        │
        ▼
 Vendor Lookup
        │
        ▼
 Hostname Discovery
        │
        ▼
 Device Classification
        │
        ▼
 Change Detection
        │
        ▼
 Repository Layer
        │
        ▼
 SQLite Database
```

---

# 🛠 Tech Stack

### Programming Language

- Python

### Backend

- Flask

### Database

- SQLite

### Networking

- Scapy
- Python-Nmap
- Socket Programming

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Jinja2

---

# 📂 Project Structure

```text
network-asset-discovery/

├── config/
├── data/
├── database/
│   ├── repositories/
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

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/network-asset-discovery.git

cd network-asset-discovery
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

Verify that Nmap is installed

```bash
nmap --version
```

---

# ▶ Running the Project

### Run Network Scanner

```bash
python main.py
```

### Launch Dashboard

```bash
python -m web.app
```

Open

```
http://127.0.0.1:5000
```

### Start Scheduler

```bash
python run_scheduler.py
```

---

# 📸 Dashboard Modules

The web dashboard includes:

- 📊 Dashboard
- 💻 Assets
- 🔍 Device Details
- 📑 Reports
- ⏰ Scheduler
- ⚙ Settings

---

# 📸 Screenshots

> Replace these placeholders with actual screenshots.

| Module | Screenshot |
|---------|------------|
| Dashboard | *(Add Image)* |
| Assets | *(Add Image)* |
| Device Details | *(Add Image)* |
| Reports | *(Add Image)* |
| Scheduler | *(Add Image)* |
| Settings | *(Add Image)* |

---

# 🔄 Project Workflow

```text
Start Scan
     │
     ▼
Network Discovery
     │
     ▼
Port Scanning
     │
     ▼
Service Detection
     │
     ▼
Banner Grabbing
     │
     ▼
OS Fingerprinting
     │
     ▼
Vendor Lookup
     │
     ▼
Hostname Discovery
     │
     ▼
Device Classification
     │
     ▼
Change Detection
     │
     ▼
SQLite Database
     │
     ▼
Web Dashboard
```

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Lakhveer Singh**

B.Tech – Computer Science & Engineering

Cybersecurity Enthusiast

📧 Connect with me on LinkedIn and GitHub.

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub.