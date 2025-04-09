from abc import ABC, abstractmethod
from typing import Optional


class AbstractNotificationChannel(ABC):
    """Base abstract class for all notification channels.

    Each notification channel must implement the send_notification method.
    """

    @abstractmethod
    async def send_notification(self, subject: str, message: str) -> bool:
        """Send a notification with the given subject and message.

        Args:
            subject: The subject or title of the notification
            message: The body of the notification

        Returns:
            bool: True if the notification was sent successfully, False otherwise
        """
        pass
