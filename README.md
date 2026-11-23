# Computer Health Monitor 🖥️

A beginner-friendly Python project that checks computer disk space, folder sizes, and largest files. It generates a health report and saves a summary to a log file.

## Features

- Displays total, used, and free disk space.
- Calculates folder size.
- Finds the 5 largest files.
- Converts bytes into readable units (KB, MB, GB).
- Counts files by extension.
- Displays disk health status.
- Saves a timestamped summary to `health_log.txt`.
- Handles invalid folder paths.
- Uses only Python standard libraries.

## Technologies Used

- Python
- `os`
- `shutil`
- `datetime`

## How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/Computer-Health-Monitor.git
   ```

2. Navigate to the project folder:

   ```bash
   cd Computer-Health-Monitor
   ```

3. Run the program:

   ```bash
   python monitor.py
   ```

4. Enter the folder path you want to scan, or press Enter to scan the current directory.

## Sample Output

```text
COMPUTER HEALTH MONITOR

DISK SPACE
Total Disk Space: 475 GB
Used Disk Space: 320 GB
Free Disk Space: 155 GB

FOLDER INFORMATION
Folder Size: 2.5 GB

TOP 5 LARGEST FILES
1. video.mp4 - 850 MB
2. dataset.zip - 420 MB

HEALTH STATUS
GOOD: Disk space is healthy.

Report saved to health_log.txt
```

*The values shown above are examples.*

## Project Structure

```text
Computer-Health-Monitor/
├── monitor.py
├── README.md
└── health_log.txt
```

## Learning Objectives

- Working with Python standard libraries.
- File and folder handling.
- Functions and return values.
- Exception handling.
- Sorting data.
- Logging and file operations.

## Author

Created as a beginner Python project to practise core Python concepts.
