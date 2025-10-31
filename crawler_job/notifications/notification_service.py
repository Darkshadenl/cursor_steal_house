import os
from typing import List, Optional
import asyncio

from crawler_job.models.house_models import House
from crawler_job.services.llm_service import LLMProvider, LLMService
from crawler_job.services.logger_service import setup_logger
from .channels.base import AbstractNotificationChannel
from .channels.email import EmailNotificationChannel
from .channels.pushover import PushoverNotificationChannel
from .channels.telegram import TelegramNotificationChannel

logger = setup_logger(__name__)


class NotificationService:
    """Service for managing notification channels and sending notifications."""

    def __init__(self, notifications_on: bool):
        """Initialize the notification service with active channels based on environment variables."""
        self.active_channels: List[AbstractNotificationChannel] = []

        notification_channels_active = os.getenv("NOTIFICATION_CHANNELS_ACTIVE", "")
        email_recipients_file = os.getenv("EMAIL_RECIPIENTS_FILE")
        self.notifications_on = notifications_on

        if not notifications_on:
            logger.info("Notifications are disabled.")

        if notification_channels_active:
            active_channel_names = [
                name.strip().lower() for name in notification_channels_active.split(",")
            ]

            logger.info(
                f"Initializing notification channels: {', '.join(active_channel_names)}"
            )
            self._initialize_channels(active_channel_names, email_recipients_file)
        else:
            logger.info(
                "No notification channels configured in NOTIFICATION_CHANNELS_ACTIVE"
            )

        if self.active_channels and self.notifications_on:
            logger.info(
                f"Successfully initialized {len(self.active_channels)} notification channels"
            )
        else:
            logger.warning("No notification channels are active.")

    def _initialize_channels(
        self, channel_names: List[str], email_recipients_file: Optional[str]
    ) -> None:
        """Initialize notification channels based on the provided names.

        Args:
            channel_names: List of channel names to initialize
            email_recipients_file: Path to file containing email recipients (one per line)
        """
        llm_service = LLMService()

        for channel_name in channel_names:
            try:
                if channel_name == "email":
                    if not email_recipients_file:
                        logger.warning(
                            "Email channel is enabled but EMAIL_RECIPIENTS_FILE is not set"
                        )
                        continue

                    self.active_channels.append(
                        EmailNotificationChannel(email_recipients_file, llm_service)
                    )
                    logger.info(
                        f"Email notification channel initialized with recipients from {email_recipients_file}"
                    )

                elif channel_name == "pushover":
                    self.active_channels.append(PushoverNotificationChannel())
                    logger.info("Pushover notification channel initialized")

                elif channel_name == "telegram":
                    self.active_channels.append(TelegramNotificationChannel())
                    logger.info("Telegram notification channel initialized")

                else:
                    logger.warning(f"Unknown notification channel: {channel_name}")

            except ValueError as e:
                # This is expected when configuration is missing
                logger.warning(f"Could not initialize {channel_name} channel: {str(e)}")
            except Exception as e:
                # Unexpected error
                logger.error(
                    f"Failed to initialize {channel_name} channel: {str(e)}",
                    exc_info=True,
                )

    async def send_new_house_notification(self, house: House) -> None:
        """Send a notification about a new house to all active channels.

        Args:
            house: The new house to send a notification about
        """
        if not self.notifications_on:
            return

        if not self.active_channels:
            logger.info("No active notification channels, skipping notification")
            return

        # Run all channel notifications in parallel
        tasks = [channel.send_notification(house) for channel in self.active_channels]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        for channel, result in zip(self.active_channels, results):
            channel_name = channel.__class__.__name__
            if isinstance(result, Exception):
                logger.error(
                    f"Error sending notification via {channel_name}: {str(result)}",
                    exc_info=result,
                )
            elif result:
                logger.info(
                    f"Notification for {house.address} sent successfully via {channel_name}"
                )
            else:
                logger.warning(
                    f"Failed to send notification for {house.address} via {channel_name}"
                )

    async def send_updated_house_notification(
        self, house: House, old_status: str
    ) -> None:
        """Send a notification about an updated house to all active channels.

        Args:
            house: The updated house to send a notification about
            old_status: The previous status of the house
        """
        if not self.notifications_on:
            return

        if not self.active_channels:
            logger.info("No active notification channels, skipping notification")
            return

        # Run all channel update notifications in parallel
        tasks = [
            channel.send_notification(house, old_status=old_status)
            for channel in self.active_channels
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        for channel, result in zip(self.active_channels, results):
            channel_name = channel.__class__.__name__
            if isinstance(result, Exception):
                logger.error(
                    f"Error sending update notification via {channel_name}: {str(result)}",
                    exc_info=result,
                )
            elif result:
                logger.info(
                    f"Update notification for {house.address} sent successfully via {channel_name}"
                )
            else:
                logger.warning(
                    f"Failed to send update notification for {house.address} via {channel_name}"
                )

    async def send_test_notification(self) -> List[str]:
        """Send a test notification to all active channels.

        Returns:
            List of channel names that were successfully notified
        """
        if not self.active_channels:
            logger.info("No active notification channels, skipping test notification")
            return []

        subject = "StealHouse Notification Test"
        message = (
            "This is a test notification from StealHouse.\n\n"
            "If you're receiving this, your notification channel is properly configured."
        )

        successful_channels = []

        # Run all test notifications in parallel
        tasks = [
            channel.send_notification(
                house=None, subject=subject, message=message, is_test=True
            )
            for channel in self.active_channels
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        for channel, result in zip(self.active_channels, results):
            channel_name = channel.__class__.__name__.replace("NotificationChannel", "")
            if isinstance(result, Exception):
                logger.error(
                    f"Error sending test notification via {channel_name}: {str(result)}",
                    exc_info=result,
                )
            elif result:
                logger.info(f"Test notification sent successfully via {channel_name}")
                successful_channels.append(channel_name)
            else:
                logger.warning(f"Failed to send test notification via {channel_name}")

        return successful_channels
