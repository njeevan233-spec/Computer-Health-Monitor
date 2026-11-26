# Computer Health Monitor 🖥️

## 📌 Project Overview

Computer Health Monitor is a Python-based system monitoring tool designed to check computer health, analyze disk space, scan folder sizes, detect large files, and maintain execution history.

The project is developed in two weeks, with Week 1 focusing on basic system monitoring and Week 2 introducing Object-Oriented Programming (OOP), configurable checks, and history tracking.

## 🚀 Features

- Disk Space Monitoring
- Folder Size Analysis
- Large File Detection
- System Information Report
- Total Files and Subfolder Count
- Subfolder Size Analysis
- Object-Oriented Programming (OOP)
- JSON-Based Configuration
- Automated Health Reports
- Execution History Tracking

## 🛠️ Technologies Used

- Python 3
- JSON
- OS Module
- Standard Python Libraries

---

# 📅 Week 1 – Computer Health Monitor

## Features

- Displays computer system information.
- Checks total, used, and free disk space.
- Calculates folder size.
- Counts total files and subfolders.
- Analyzes individual subfolder sizes.

## 📊 Week 1 – Sample Output

```text
============================================================
                  COMPUTER HEALTH MONITOR
============================================================

Enter folder path to scan (Enter = current folder): [Folder Path]
============================================================
                    SYSTEM INFORMATION
============================================================

Report Date & Time : [Date and Time]
Computer Name      : [Computer Name]
Operating System   : Windows
OS Version         : [OS Version]
Python Version     : [Python Version]
Scanned Folder     : [Folder Path]

------------------------------------------------------------
                     DISK SPACE REPORT
------------------------------------------------------------

Total Disk Space : 474.37 GB
Used Disk Space  : 97.18 GB
Free Disk Space  : 377.19 GB
Disk Usage       : 20.49%
Free Space       : 79.51%

------------------------------------------------------------
                      FOLDER SUMMARY
------------------------------------------------------------

Total Folder Size : 16.67 KB
Total Files       : 7
Total Subfolders  : 2

------------------------------------------------------------
                 SUBFOLDER SIZE ANALYSIS
------------------------------------------------------------
```

---

# 📅 Week 2 – Object-Oriented Computer Health Monitor

## Features

- Implemented Object-Oriented Programming (OOP).
- Created a base class named `Check`.
- Used inheritance for individual health checks.
- Implemented `DiskSpaceCheck`, `FolderSizeCheck`, and `LargeFileCheck`.
- Used `config.json` for configurable monitoring limits.
- Stored execution history in `history.json`.
- Generated automated health status reports.

## 📊 Week 2 – Sample Output

```text
[FAIL] Disk Space: Free disk space: 79.23%

[OK] Folder Size: .: 112.25 MB (OK)

[WARN] Large Files: Files approaching limit:
.\python-manager-26.4.msix (96.22 MB)

============================================================

Run saved successfully to history.json
```

---

## 📂 Project Structure

```text
Computer-Health-Monitor/
│
├── monitor.py
├── config.json
├── history.json
├── health_log.txt
└── README.md
```

## ▶️ How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open the project folder in VS Code.
4. Open the terminal.
5. Execute the following command:

```bash
python monitor.py
```

## 🎯 Learning Outcomes

- Python programming and functions
- Object-Oriented Programming
- Classes and inheritance
- File handling
- JSON configuration
- System monitoring
- Error handling
- Logging and report generation

## 👨‍💻 Author

**Project:** Computer Health Monitor 🖥️

**Duration:** Week 1 and Week 2

**Technology:** Python

