import smtplib
import asyncio
import logging
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional

from .base import AbstractNotificationChannel

logger = logging.getLogger(__name__)


class EmailNotificationChannel(AbstractNotificationChannel):
    """Notification channel for sending emails."""

    def __init__(self, recipient_email: str):
        """Initialize the email notification channel.

        Args:
            recipient_email: The email address to send notifications to
        """
        # Get settings from environment variables
        self.smtp_server = os.getenv("SMTP_SERVER")
        self.smtp_port = int(os.getenv("SMTP_PORT"))
        self.email_user = os.getenv("EMAIL_USER")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.recipient_email = recipient_email

        # Validate required settings
        if not all([self.smtp_server, self.email_user, self.email_password]):
            raise ValueError(
                "Missing required email configuration in environment variables"
            )

        logger.info(f"Email notification channel initialized for {recipient_email}")

    async def send_notification(self, subject: str, message: str) -> bool:
        """Send an email notification.

        Args:
            subject: The email subject
            message: The email body

        Returns:
            bool: True if the email was sent successfully, False otherwise
        """
        return await asyncio.to_thread(self._send_email_sync, subject, message)

    def _send_email_sync(self, subject: str, message: str) -> bool:
        """Synchronous method to send email (will be run in a thread).

        Args:
            subject: The email subject
            message: The email body

        Returns:
            bool: True if the email was sent successfully, False otherwise
        """
        try:
            # Create a multipart message
            email_message = MIMEMultipart()
            email_message["From"] = self.email_user
            email_message["To"] = self.recipient_email
            email_message["Subject"] = subject

            # Add the message body
            email_message.attach(MIMEText(message, "plain"))

            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.email_user, self.email_password)
                server.send_message(email_message)

            logger.info(f"Email notification sent to {self.recipient_email}")
            return True

        except Exception as e:
            logger.error(f"Failed to send email notification: {str(e)}")
            return False
