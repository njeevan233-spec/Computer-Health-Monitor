
import os
import shutil


class Check:
    def __init__(self, name):
        self.name = name

    def run(self):
        raise NotImplementedError("Subclasses must implement run()")

    def result(self, status, detail):
        return {
            "name": self.name,
            "status": status,
            "detail": detail
        }


class DiskSpaceCheck(Check):
    def __init__(self, min_free_percent):
        super().__init__("Disk Space")
        self.min_free_percent = min_free_percent

    def run(self):
        total, used, free = shutil.disk_usage(os.path.abspath("."))
        free_percent = (free / total) * 100

        if free_percent < self.min_free_percent:
            status = "FAIL"
        elif free_percent < self.min_free_percent + 10:
            status = "WARN"
        else:
            status = "OK"

        detail = f"Free disk space: {free_percent:.2f}%"
        return self.result(status, detail)


class FolderSizeCheck(Check):
    def __init__(self, folders, max_folder_mb):
        super().__init__("Folder Size")
        self.folders = folders
        self.max_folder_mb = max_folder_mb

    def run(self):
        messages = []
        overall_status = "OK"

        for folder in self.folders:
            if not os.path.isdir(folder):
                messages.append(f"{folder}: folder not found")
                overall_status = "WARN"
                continue

            total_size = 0

            for root, dirs, files in os.walk(folder):
                dirs[:] = [
                    d for d in dirs
                    if d not in [".venv", ".git", "__pycache__"]
                ]

                for filename in files:
                    path = os.path.join(root, filename)
                    try:
                        total_size += os.path.getsize(path)
                    except OSError:
                        continue

            size_mb = total_size / (1024 * 1024)

            if size_mb > self.max_folder_mb:
                status = "FAIL"
            elif size_mb > self.max_folder_mb * 0.8:
                status = "WARN"
            else:
                status = "OK"

            if status == "FAIL":
                overall_status = "FAIL"
            elif status == "WARN" and overall_status == "OK":
                overall_status = "WARN"

            messages.append(f"{folder}: {size_mb:.2f} MB ({status})")

        return self.result(overall_status, "; ".join(messages))


class LargeFileCheck(Check):
    def __init__(self, folders, large_file_mb):
        super().__init__("Large Files")
        self.folders = folders
        self.large_file_mb = large_file_mb

    def run(self):
        large_files = []
        warning_files = []

        for folder in self.folders:
            if not os.path.isdir(folder):
                continue

            for root, dirs, files in os.walk(folder):
                dirs[:] = [
                    d for d in dirs
                    if d not in [".venv", ".git", "__pycache__"]
                ]

                for filename in files:
                    path = os.path.join(root, filename)

                    try:
                        size_mb = os.path.getsize(path) / (1024 * 1024)
                    except OSError:
                        continue

                    if size_mb >= self.large_file_mb:
                        large_files.append(
                            f"{path} ({size_mb:.2f} MB)"
                        )
                    elif size_mb >= self.large_file_mb * 0.8:
                        warning_files.append(
                            f"{path} ({size_mb:.2f} MB)"
                        )

        if large_files:
            status = "FAIL"
            detail = "Large files found: " + ", ".join(large_files[:5])
        elif warning_files:
            status = "WARN"
            detail = "Files approaching limit: " + ", ".join(warning_files[:5])
        else:
            status = "OK"
            detail = "No large files found."

        return self.result(status, detail)
