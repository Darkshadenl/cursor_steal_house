import logging
import os
from typing import Optional
from telegram import Bot
from telegram.error import TelegramError

from crawler_job.models.house_models import House
from .base import AbstractNotificationChannel

logger = logging.getLogger(__name__)


class TelegramNotificationChannel(AbstractNotificationChannel):
    """Notification channel for sending Telegram messages."""

    def __init__(self):
        """Initialize the Telegram notification channel."""
        # Get settings from environment variables
        self.telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")

        # Validate required settings
        if not all([self.telegram_bot_token, self.telegram_chat_id]):
            raise ValueError(
                "Missing required Telegram configuration in environment variables"
            )

        assert self.telegram_bot_token is not None
        self.bot = Bot(token=self.telegram_bot_token)
        logger.info("Telegram notification channel initialized")

    async def send_notification(self, house: Optional[House], **kwargs) -> bool:
        """Send a notification using Telegram.

        Args:
            house: The house object to send a notification for. Can be None for test notifications.

        Returns:
            bool: True if the notification was sent successfully, False otherwise
        """
        is_test = kwargs.get("is_test", False)
        if is_test:
            subject = kwargs.get("subject", "Test Notification")
            message = kwargs.get("message", "This is a test.")
        elif house:
            old_status = kwargs.get("old_status")
            if old_status:
                subject = f"Updated House: {house.address}, {house.city}"
                message = (
                    f"The status of a property at {house.address}, {house.city} has changed.\n\n"
                    f"Previous status: {old_status}\n"
                    f"New status: {house.status}\n"
                    f"View details: {house.detail_url}"
                )
            else:
                subject = f"New House: {house.address}, {house.city}"
                message = (
                    f"A new property is available at {house.address}, {house.city}.\n\n"
                    f"Status: {house.status}\n"
                    f"Price: {house.rental_price}\n"
                    f"View details: {house.detail_url}"
                )
        else:
            logger.warning(
                "Telegram send_notification called without a house and not in test mode."
            )
            return False

        try:
            # Combine subject and message
            full_message = f"*{subject}*\n\n{message}"

            assert self.telegram_chat_id is not None
            # Send the message
            await self.bot.send_message(
                chat_id=self.telegram_chat_id, text=full_message, parse_mode="Markdown"
            )

            logger.info("Telegram notification sent successfully")
            return True

        except TelegramError as e:
            logger.error(f"Failed to send Telegram notification: {str(e)}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error sending Telegram notification: {str(e)}")
            return False
