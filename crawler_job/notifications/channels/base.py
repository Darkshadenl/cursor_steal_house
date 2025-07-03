from abc import ABC, abstractmethod
from typing import Optional

from crawler_job.models.house_models import House


class AbstractNotificationChannel(ABC):
    """Base abstract class for all notification channels.

    Each notification channel must implement the send_notification method.
    """

    @abstractmethod
    async def send_notification(self, house: Optional[House], **kwargs) -> bool:
        """Send a notification.

        Args:
            house: The house object to send a notification for. Can be None for general notifications.

        Returns:
            bool: True if the notification was sent successfully, False otherwise
        """
        pass
