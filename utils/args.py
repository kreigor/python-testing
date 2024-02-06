import argparse


CONSOLE_ARGUMENTS = None


def init_argparse(version) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        epilog=f"APP NAME HERE version {version}",
        description="This is a description...",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"APP NAME HERE version {version}"
    )
    parser.add_argument(
        "-s",
        "--skip",
        action="store_true",
        dest="skip",
        help="Skip something. "
        "Use this if file already exists.",
    )

    subparsers = parser.add_subparsers(
        title="sup parser",
        help="Choose type {a or b}",
        dest="subcommand"
    )

    parser_a = subparsers.add_parser("a", help="Help for Sub Parser A")
    parser_a.add_argument(
        "--days_ago",
        dest="days_ago",
        default=1,
        type=int,
        help="Help Message for days_ago",
    )
    parser_a.add_argument(
        "--file_act",
        type=argparse.FileType("r"),
        help="Help Message for file_act",
    )
    parser_a.add_argument(
        "--file_pst",
        type=argparse.FileType("r"),
        help="Help Message for file_pst",
    )
    parser_a.add_argument("-a", action="store_true",
                          help="help for a, positional")
    parser_a.add_argument("-x", action="store_true",
                          help="help for x, positional")

    parser_b = subparsers.add_parser("b", help="Help for Sub Parser B")
    parser_b.add_argument("-b", type=str, help="help for b")
    parser_b.add_argument("-c", type=str, help="help for c")

    group_verbose = parser.add_mutually_exclusive_group()
    group_verbose.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        dest="quiet",
        help="Suppress Output"
    )
    group_verbose.add_argument(
        "-d",
        "--debug",
        action="store_true",
        dest="debug",
        help="Turn on debug output"
    )

    global CONSOLE_ARGUMENTS
    CONSOLE_ARGUMENTS = parser.parse_args()
    return parser
