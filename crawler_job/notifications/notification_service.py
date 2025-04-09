import os
import logging
from typing import List, Optional
from dotenv import load_dotenv

from crawler_job.models.house_models import GalleryHouse
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
        notification_recipient_email = os.getenv("NOTIFICATION_RECIPIENT_EMAIL")

        # Parse the active channels string and initialize each channel
        if notification_channels_active:
            active_channel_names = [
                name.strip().lower() for name in notification_channels_active.split(",")
            ]

            logger.info(
                f"Initializing notification channels: {', '.join(active_channel_names)}"
            )
            self._initialize_channels(
                active_channel_names, notification_recipient_email
            )
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
        self, channel_names: List[str], notification_recipient_email: Optional[str]
    ) -> None:
        """Initialize notification channels based on the provided names.

        Args:
            channel_names: List of channel names to initialize
            notification_recipient_email: Email address to send notifications to
        """
        for channel_name in channel_names:
            try:
                if channel_name == "email":
                    if not notification_recipient_email:
                        logger.warning(
                            "Email channel is enabled but NOTIFICATION_RECIPIENT_EMAIL is not set"
                        )
                        continue

                    self.active_channels.append(
                        EmailNotificationChannel(notification_recipient_email)
                    )
                    logger.info(
                        f"Email notification channel initialized for {notification_recipient_email}"
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

    async def send_new_house_notification(self, house: GalleryHouse) -> None:
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
