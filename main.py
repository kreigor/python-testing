import json
import logging
from pathlib import Path

from utils.logging import setup_logging

logger = logging.getLogger("Testing")


def main() -> None:
    setup_logging(config_data["logger"])
    print("Hello, World!")


# Load Config
full_file_path = Path(__file__).parent.joinpath("config.json")
with open(full_file_path, encoding="UTF-8") as settings:
    config_data = json.load(settings)

VERSION = "0.1.0"
SETTING_ONE = config_data["setting_one"]
SETTING_TWO = config_data["setting_two"]

if __name__ == "__main__":
    main()
