import logging
import os
from typing import Optional
from telegram import Bot
from telegram.error import TelegramError

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

        self.bot = Bot(token=self.telegram_bot_token)
        logger.info("Telegram notification channel initialized")

    async def send_notification(self, subject: str, message: str) -> bool:
        """Send a notification using Telegram.

        Args:
            subject: The notification title
            message: The notification body

        Returns:
            bool: True if the notification was sent successfully, False otherwise
        """
        try:
            # Combine subject and message
            full_message = f"*{subject}*\n\n{message}"

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
