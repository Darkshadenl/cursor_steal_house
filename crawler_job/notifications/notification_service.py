import os
import logging
from typing import List, Optional
from dotenv import load_dotenv

from crawler_job.models.house_models import House
from .channels.base import AbstractNotificationChannel
from .channels.email import EmailNotificationChannel
from .channels.pushover import PushoverNotificationChannel
from .channels.telegram import TelegramNotificationChannel

logger = logging.getLogger(__name__)


class NotificationService:
    """Service for managing notification channels and sending notifications."""

    def __init__(self):
        """Initialize the notification service with active channels based on environment variables."""
        self.active_channels: List[AbstractNotificationChannel] = []

        # Get notification configuration from environment variables
        notification_channels_active = os.getenv("NOTIFICATION_CHANNELS_ACTIVE", "")
        email_recipients_file = os.getenv("EMAIL_RECIPIENTS_FILE")

        # Parse the active channels string and initialize each channel
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

        if self.active_channels:
            logger.info(
                f"Successfully initialized {len(self.active_channels)} notification channels"
            )
        else:
            logger.warning(
                "No notification channels are active. Check your .env configuration."
            )

    def _initialize_channels(
        self, channel_names: List[str], email_recipients_file: Optional[str]
    ) -> None:
        """Initialize notification channels based on the provided names.

        Args:
            channel_names: List of channel names to initialize
            email_recipients_file: Path to file containing email recipients (one per line)
        """
        for channel_name in channel_names:
            try:
                if channel_name == "email":
                    if not email_recipients_file:
                        logger.warning(
                            "Email channel is enabled but EMAIL_RECIPIENTS_FILE is not set"
                        )
                        continue

                    self.active_channels.append(
                        EmailNotificationChannel(email_recipients_file)
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
        if not self.active_channels:
            logger.info("No active notification channels, skipping notification")
            return

        subject = f"New House Available: {house.address}, {house.city}"

        # Format the message with details about the house
        message = (
            f"A new property is available at {house.address}, {house.city}.\n\n"
            f"Status: {house.status}\n"
            f"Type: {house.house_type if hasattr(house, 'house_type') else 'Not specified'}\n"
            f"Price: {house.price if hasattr(house, 'price') else 'Not specified'}\n\n"
            f"View details: {house.detail_url}"
        )

        # Send the notification to each active channel
        for channel in self.active_channels:
            try:
                success = await channel.send_notification(subject, message)
                if success:
                    logger.info(
                        f"Notification for {house.address} sent successfully via {channel.__class__.__name__}"
                    )
                else:
                    logger.warning(
                        f"Failed to send notification for {house.address} via {channel.__class__.__name__}"
                    )
            except Exception as e:
                logger.error(
                    f"Error sending notification via {channel.__class__.__name__}: {str(e)}",
                    exc_info=True,
                )

    async def send_updated_house_notification(
        self, house: House, old_status: str
    ) -> None:
        """Send a notification about an updated house to all active channels.

        Args:
            house: The updated house to send a notification about
            old_status: The previous status of the house
        """
        if not self.active_channels:
            logger.info("No active notification channels, skipping notification")
            return

        subject = f"House Status Updated: {house.address}, {house.city}"

        # Format the message with details about the house
        message = (
            f"The status of a property at {house.address}, {house.city} has changed.\n\n"
            f"Previous status: {old_status}\n"
            f"New status: {house.status}\n"
            f"Type: {house.house_type if hasattr(house, 'house_type') else 'Not specified'}\n"
            f"Price: {house.price if hasattr(house, 'price') else 'Not specified'}\n\n"
            f"View details: {house.detail_url}"
        )

        # Send the notification to each active channel
        for channel in self.active_channels:
            try:
                success = await channel.send_notification(subject, message)
                if success:
                    logger.info(
                        f"Update notification for {house.address} sent successfully via {channel.__class__.__name__}"
                    )
                else:
                    logger.warning(
                        f"Failed to send update notification for {house.address} via {channel.__class__.__name__}"
                    )
            except Exception as e:
                logger.error(
                    f"Error sending update notification via {channel.__class__.__name__}: {str(e)}",
                    exc_info=True,
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

        # Send the notification to each active channel
        for channel in self.active_channels:
            channel_name = channel.__class__.__name__.replace("NotificationChannel", "")
            try:
                success = await channel.send_notification(subject, message)
                if success:
                    logger.info(
                        f"Test notification sent successfully via {channel_name}"
                    )
                    successful_channels.append(channel_name)
                else:
                    logger.warning(
                        f"Failed to send test notification via {channel_name}"
                    )
            except Exception as e:
                logger.error(
                    f"Error sending test notification via {channel_name}: {str(e)}",
                    exc_info=True,
                )

        return successful_channels
