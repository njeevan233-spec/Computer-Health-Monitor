
import json
import os

CONFIG_FILE = "config.json"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        raise FileNotFoundError("config.json not found!")

    with open(CONFIG_FILE, "r") as file:
        config = json.load(file)

    required = [
        "min_free_percent",
        "max_folder_mb",
        "large_file_mb",
        "folders"
    ]

    for key in required:
        if key not in config:
            raise ValueError(f"Missing setting in config.json: {key}")

    return config
