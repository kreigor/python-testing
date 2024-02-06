import json
import logging
import sys
from pathlib import Path

import utils.args
from utils.logging import setup_logging

logger = logging.getLogger("Testing")


def main() -> None:
    parser = utils.args.init_argparse(VERSION)
    setup_logging(config_data["logger"])
    logger.info("Hello, World!")

    if not len(sys.argv) > 1:
        parser.print_help()
        sys.exit(1)
    else:
        args = parser.parse_args()

        if args.debug:
            logger.debug(f"Args: {args}",
                         extra={
                             "debug": f"{args.debug}",
                             "quiet": f"{args.quiet}",
                             "skip": f"{args.skip}"
                         })


# Load Config
full_file_path = Path(__file__).parent.joinpath("config.json")
with open(full_file_path, encoding="UTF-8") as settings:
    config_data = json.load(settings)

VERSION = "0.1.0"
SETTING_ONE = config_data["setting_one"]
SETTING_TWO = config_data["setting_two"]

if __name__ == "__main__":
    main()
