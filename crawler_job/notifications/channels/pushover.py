import logging
import os
import httpx
from typing import Optional

from crawler_job.models.house_models import House
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

    async def send_notification(self, house: Optional[House], **kwargs) -> bool:
        """Send a notification using Pushover.

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
                "Pushover send_notification called without a house and not in test mode."
            )
            return False

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
