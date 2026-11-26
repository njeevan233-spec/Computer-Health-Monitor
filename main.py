
import json
import os
import argparse
from datetime import datetime

from config import load_config
from checks import (
    DiskSpaceCheck,
    FolderSizeCheck,
    LargeFileCheck
)

HISTORY_FILE = "history.json"

# Enable ANSI colours in Windows terminals
os.system("")


COLORS = {
    "OK": "\033[92m",
    "WARN": "\033[93m",
    "FAIL": "\033[91m",
    "RESET": "\033[0m"
}


def build_checks(config):
    return [
        DiskSpaceCheck(config["min_free_percent"]),
        FolderSizeCheck(
            config["folders"],
            config["max_folder_mb"]
        ),
        LargeFileCheck(
            config["folders"],
            config["large_file_mb"]
        )
    ]


def save_history(results):
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as file:
                history = json.load(file)
        except (json.JSONDecodeError, OSError):
            history = []
    else:
        history = []

    if not isinstance(history, list):
        history = []

    history.append({
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "results": results
    })

    # Keep only the latest 50 runs
    history = history[-50:]

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=2)


def display_results(results):
    print("\n========== PySentinel Health Report ==========\n")

    for result in results:
        status = result["status"]
        color = COLORS.get(status, COLORS["RESET"])

        print(
            f"{color}[{status}]{COLORS['RESET']} "
            f"{result['name']}: {result['detail']}"
        )

    print("\n==============================================\n")


def show_summary():
    if not os.path.exists(HISTORY_FILE):
        print("No history found. Run the monitoring tool first.")
        return

    with open(HISTORY_FILE, "r") as file:
        history = json.load(file)

    failure_counts = {}

    for run in history:
        for result in run.get("results", []):
            name = result.get("name", "Unknown")

            if name not in failure_counts:
                failure_counts[name] = 0

            if result.get("status") == "FAIL":
                failure_counts[name] += 1

    print("\n========== PySentinel Failure Summary ==========")
    print(f"Total recorded runs: {len(history)}\n")

    if not failure_counts:
        print("No check results found.")
    else:
        for name, count in failure_counts.items():
            print(f"{name}: {count} failure(s)")

    print("================================================\n")


def main():
    parser = argparse.ArgumentParser(
        description="PySentinel System Monitoring Tool"
    )

    parser.add_argument(
        "--summary",
        action="store_true",
        help="Show failure counts from previous runs"
    )

    args = parser.parse_args()

    if args.summary:
        show_summary()
        return

    try:
        config = load_config()
        checks = build_checks(config)

        results = []

        for check in checks:
            results.append(check.run())

        display_results(results)
        save_history(results)

        print("Run saved successfully to history.json")

    except (FileNotFoundError, ValueError, json.JSONDecodeError) as error:
        print(f"Configuration error: {error}")


if __name__ == "__main__":
    main()
