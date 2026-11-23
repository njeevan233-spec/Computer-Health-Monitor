
import os
import shutil
import platform
from datetime import datetime
from collections import Counter


def human_size(num_bytes):
    size = float(num_bytes)

    for unit in ["Bytes", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} PB"


def disk_usage(path):
    total, used, free = shutil.disk_usage(path)
    return total, used, free


def folder_size(path):
    total_size = 0
    file_count = 0

    for root, dirs, files in os.walk(path):
        for name in files:
            file_path = os.path.join(root, name)

            try:
                if not os.path.islink(file_path):
                    total_size += os.path.getsize(file_path)
                    file_count += 1
            except (PermissionError, OSError):
                continue

    return total_size, file_count


def largest_files(path, n=10):
    file_list = []

    for root, dirs, files in os.walk(path):
        for name in files:
            file_path = os.path.join(root, name)

            try:
                if not os.path.islink(file_path):
                    size = os.path.getsize(file_path)
                    file_list.append((size, file_path))
            except (PermissionError, OSError):
                continue

    file_list.sort(key=lambda item: item[0], reverse=True)
    return file_list[:n]


def extension_count(path):
    extensions = Counter()

    for root, dirs, files in os.walk(path):
        for name in files:
            extension = os.path.splitext(name)[1].lower()

            if not extension:
                extension = "No extension"

            extensions[extension] += 1

    return extensions


def get_subfolder_sizes(path):
    results = []

    try:
        for item in os.scandir(path):
            if item.is_dir(follow_symlinks=False):
                size, count = folder_size(item.path)
                results.append((item.name, size, count))

    except (PermissionError, OSError):
        pass

    results.sort(key=lambda item: item[1], reverse=True)
    return results


def main():
    print("\n" + "=" * 65)
    print("                  COMPUTER HEALTH MONITOR")
    print("=" * 65)

    folder = input(
        "\nEnter folder path to scan (Enter = current folder): "
    ).strip()

    if not folder:
        folder = os.getcwd()

    folder = os.path.abspath(folder)

    if not os.path.isdir(folder):
        print("\nERROR: Folder does not exist!")
        print("Please check the path and try again.")
        return

    timestamp = datetime.now()

    # Disk information
    total, used, free = disk_usage(folder)
    used_percent = (used / total) * 100
    free_percent = (free / total) * 100

    # Folder information
    size, file_count = folder_size(folder)
    biggest = largest_files(folder, 10)
    extensions = extension_count(folder)
    subfolders = get_subfolder_sizes(folder)

    # Header
    print("\n" + "=" * 65)
    print("                    SYSTEM INFORMATION")
    print("=" * 65)

    print(f"Report Date & Time : {timestamp.strftime('%d-%m-%Y %H:%M:%S')}")
    print(f"Computer Name      : {platform.node()}")
    print(f"Operating System   : {platform.system()}")
    print(f"OS Version         : {platform.version()}")
    print(f"Python Version     : {platform.python_version()}")
    print(f"Scanned Folder     : {folder}")

    # Disk space
    print("\n" + "-" * 65)
    print("                    DISK SPACE REPORT")
    print("-" * 65)

    print(f"Total Disk Space   : {human_size(total)}")
    print(f"Used Disk Space    : {human_size(used)}")
    print(f"Free Disk Space    : {human_size(free)}")
    print(f"Disk Usage         : {used_percent:.2f}%")
    print(f"Free Space         : {free_percent:.2f}%")

    # Folder summary
    print("\n" + "-" * 65)
    print("                    FOLDER SUMMARY")
    print("-" * 65)

    print(f"Folder Location    : {folder}")
    print(f"Total Folder Size  : {human_size(size)}")
    print(f"Total Files        : {file_count}")
    print(f"Total Subfolders   : {len(subfolders)}")

    # Subfolder sizes
    print("\n" + "-" * 65)
    print("                  SUBFOLDER SIZE ANALYSIS")
    print("-" * 65)

    if subfolders:
        for name, folder_bytes, count in subfolders:
            print(f"\nFolder Name : {name}")
            print(f"Folder Size : {human_size(folder_bytes)}")
            print(f"File Count : {count}")
    else:
        print("No subfolders found.")

    # Largest files
    print("\n" + "-" * 65)
    print("                    TOP 10 LARGEST FILES")
    print("-" * 65)

    if biggest:
        for index, (file_bytes, file_path) in enumerate(biggest, start=1):
            print(f"\n{index}. File Name : {os.path.basename(file_path)}")
            print(f"   File Size : {human_size(file_bytes)}")
            print(f"   Location  : {file_path}")
    else:
        print("No files found.")

    # Extension statistics
    print("\n" + "-" * 65)
    print("                  FILE TYPE STATISTICS")
    print("-" * 65)

    if extensions:
        for ext, count in extensions.most_common():
            percentage = (count / file_count * 100) if file_count else 0

            print(
                f"{ext:<18} {count:>5} file(s) "
                f"| {percentage:.2f}% of files"
            )
    else:
        print("No file types found.")

    # Health
    print("\n" + "-" * 65)
    print("                    HEALTH STATUS")
    print("-" * 65)

    if used_percent >= 90:
        status = "CRITICAL"
        recommendation = "Disk space is almost full. Free up storage immediately."
    elif used_percent >= 80:
        status = "WARNING"
        recommendation = "Disk usage is high. Consider removing unnecessary files."
    elif used_percent >= 70:
        status = "NOTICE"
        recommendation = "Disk usage is increasing. Monitor your storage."
    else:
        status = "GOOD"
        recommendation = "Disk space is healthy."

    print(f"Disk Health         : {status}")
    print(f"Storage Used        : {used_percent:.2f}%")
    print(f"Storage Available    : {free_percent:.2f}%")
    print(f"Recommendation      : {recommendation}")

    # Additional recommendations
    print("\n" + "-" * 65)
    print("                    RECOMMENDATIONS")
    print("-" * 65)

    print("1. Regularly check your Downloads folder.")
    print("2. Remove duplicate and unnecessary files.")
    print("3. Keep important files backed up.")
    print("4. Monitor large videos, ZIP files and installers.")
    print("5. Maintain sufficient free disk space.")

    # Save log
    script_folder = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(script_folder, "health_log.txt")

    with open(log_file, "a", encoding="utf-8") as log:
        log.write(
            f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} | "
            f"Folder: {folder} | "
            f"Files: {file_count} | "
            f"Folder Size: {human_size(size)} | "
            f"Disk Used: {used_percent:.2f}% | "
            f"Free: {free_percent:.2f}% | "
            f"Status: {status}\n"
        )

    print("\n" + "=" * 65)
    print("                  REPORT COMPLETED")
    print("=" * 65)
    print(f"Log File Location : {log_file}")
    print("A new summary has been appended to the log file.")
    print("=" * 65)


if __name__ == "__main__":
    main()
