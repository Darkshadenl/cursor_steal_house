import smtplib
import asyncio
import logging
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List

from .base import AbstractNotificationChannel

logger = logging.getLogger(__name__)


class EmailNotificationChannel(AbstractNotificationChannel):
    """Notification channel for sending emails."""

    def __init__(self, recipients_file_path: str):
        """Initialize the email notification channel.

        Args:
            recipients_file_path: Path to a text file containing recipient email addresses (one per line)
        """
        # Get settings from environment variables
        self.smtp_server = os.getenv("SMTP_SERVER")
        self.smtp_port = int(os.getenv("SMTP_PORT", "587"))
        self.email_user = os.getenv("EMAIL_USER")
        self.email_password = os.getenv("EMAIL_PASSWORD")

        # Read recipient emails from file
        self.recipient_emails = self._read_recipients_from_file(recipients_file_path)

        if not self.recipient_emails:
            raise ValueError(
                f"No recipient emails found in file: {recipients_file_path}"
            )

        # Validate required settings
        if not all([self.smtp_server, self.email_user, self.email_password]):
            raise ValueError(
                "Missing required email configuration in environment variables"
            )

        logger.info(
            f"Email notification channel initialized with {len(self.recipient_emails)} recipients"
        )

    def _read_recipients_from_file(self, file_path: str) -> List[str]:
        """Read recipient email addresses from a text file.

        Args:
            file_path: Path to the text file with email addresses (one per line)

        Returns:
            List of email addresses
        """
        if not os.path.exists(file_path):
            logger.error(f"Recipients file not found: {file_path}")
            return []

        try:
            with open(file_path, "r") as f:
                # Read lines, strip whitespace, and filter out empty lines
                emails = [line.strip() for line in f.readlines() if line.strip()]

            logger.info(f"Found {len(emails)} email recipients in {file_path}")
            return emails
        except Exception as e:
            logger.error(f"Error reading recipients file: {str(e)}")
            return []

    async def send_notification(self, subject: str, message: str) -> bool:
        """Send an email notification to all recipients.

        Args:
            subject: The email subject
            message: The email body

        Returns:
            bool: True if the email was sent successfully to all recipients, False otherwise
        """
        return await asyncio.to_thread(self._send_email_sync, subject, message)

    def _send_email_sync(self, subject: str, message: str) -> bool:
        """Synchronous method to send email (will be run in a thread).

        Args:
            subject: The email subject
            message: The email body

        Returns:
            bool: True if the email was sent successfully to all recipients, False otherwise
        """
        if not self.recipient_emails:
            logger.warning(
                "No recipient emails configured, skipping email notification"
            )
            return False

        success = True

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.email_user, self.email_password)

                # Send to each recipient
                for recipient in self.recipient_emails:
                    try:
                        # Create a multipart message
                        email_message = MIMEMultipart()
                        email_message["From"] = self.email_user
                        email_message["To"] = recipient
                        email_message["Subject"] = subject

                        email_message.attach(MIMEText(message, "html"))

                        server.send_message(email_message)
                        logger.info(f"Email notification sent to {recipient}")
                    except Exception as e:
                        logger.error(f"Failed to send email to {recipient}: {str(e)}")
                        success = False

            return success

        except Exception as e:
            logger.error(f"Failed to establish email connection: {str(e)}")
            return False
