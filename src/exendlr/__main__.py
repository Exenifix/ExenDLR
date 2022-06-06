import argparse
import sys

from .reader import Reader

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="exendlr",
        usage="exendlr <container-name> <stop-phrase>",
        description="Shows logs of the container until stop phrase is met",
    )
    parser.add_argument(
        "container_name",
        metavar="container_name",
        type=str,
        help="Name of the container show the logs of",
    )
    parser.add_argument(
        "stop_phrase",
        metavar="stop_phrase",
        type=str,
        help="Stop phrase after which the program should exit",
    )

    args = parser.parse_args()

    reader = Reader(args.container_name, args.stop_phrase)
    sys.exit(reader.start())
