import argparse
import asyncio
import os

from .vesteda_crawler import VestedaCrawler


def main():
    """
    Entry point for running the Vesteda crawler with command-line options.
    """
    parser = argparse.ArgumentParser(
        description="Run Vesteda crawler or test notifications"
    )
    parser.add_argument(
        "--notifications-on",
        action="store_true",
        help="Enable notifications after crawling",
    )
    parser.add_argument(
        "--test-notifications-only",
        action="store_true",
        help="Only run test notifications, no crawling",
    )
    args = parser.parse_args()

    if not args.notifications_on:
        os.environ["NOTIFICATION_CHANNELS_ACTIVE"] = ""

    VestedaCrawler(
        test_notifications_only=args.test_notifications_only,
        notifications_on=args.notifications_on,
    )


if __name__ == "__main__":
    main()
