import logging
import os
import httpx

from .base import AbstractNotificationChannel

logger = logging.getLogger(__name__)


class PushoverNotificationChannel(AbstractNotificationChannel):
    """Notification channel for sending Pushover notifications."""

    def __init__(self):
        """Initialize the Pushover notification channel."""
        # Get settings from environment variables
        self.pushover_token = os.getenv("PUSHOVER_TOKEN")
        self.pushover_user_key = os.getenv("PUSHOVER_USER_KEY")
        self.api_url = "https://api.pushover.net/1/messages.json"

        if not all([self.pushover_token, self.pushover_user_key]):
            raise ValueError(
                "Missing required Pushover configuration in environment variables"
            )

        logger.info("Pushover notification channel initialized")

    async def send_notification(self, subject: str, message: str) -> bool:
        """Send a notification using Pushover.

        Args:
            subject: The notification title
            message: The notification body

        Returns:
            bool: True if the notification was sent successfully, False otherwise
        """
        try:
            payload = {
                "token": self.pushover_token,
                "user": self.pushover_user_key,
                "title": subject,
                "message": message,
                "priority": 0,
                "html": 1,  
            }

            async with httpx.AsyncClient() as client:
                response = await client.post(self.api_url, data=payload)
                response.raise_for_status()

            logger.info("Pushover notification sent successfully")
            return True

        except Exception as e:
            logger.error(f"Failed to send Pushover notification: {str(e)}")
            return False
