import smtplib
import asyncio
import logging
import os
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict, Any, Optional

from crawler_job.models.house_models import House
from crawler_job.services.llm_service import LLMService
from .base import AbstractNotificationChannel

logger = logging.getLogger(__name__)


class EmailNotificationChannel(AbstractNotificationChannel):
    """Notification channel for sending emails."""

    def __init__(self, recipients_file_path: str, llm_service: LLMService):
        """Initialize the email notification channel.

        Args:
            recipients_file_path: Path to a JSON file containing recipient email addresses and metrics.
            llm_service: An instance of the LLMService for generating analyses.
        """
        self.llm_service = llm_service
        self.smtp_server = os.getenv("SMTP_SERVER")
        self.smtp_port = int(os.getenv("SMTP_PORT", "587"))
        self.email_user = os.getenv("EMAIL_USER")
        self.email_password = os.getenv("EMAIL_PASSWORD")

        if not all([self.smtp_server, self.email_user, self.email_password]):
            raise ValueError(
                "Missing required email configuration in environment variables: SMTP_SERVER, EMAIL_USER, EMAIL_PASSWORD"
            )

        self.recipients: List[Dict[str, Any]] = self._read_recipients_from_file(
            recipients_file_path
        )

        if not self.recipients:
            raise ValueError(f"No recipients found in file: {recipients_file_path}")

        logger.info(
            f"Email notification channel initialized with {len(self.recipients)} recipients"
        )

    def _read_recipients_from_file(self, file_path: str) -> List[Dict[str, Any]]:
        """Read recipient data from a JSON file.

        Args:
            file_path: Path to the JSON file with recipient data.

        Returns:
            List of recipient dictionaries.
        """
        if not os.path.exists(file_path):
            logger.error(f"Recipients file not found: {file_path}")
            return []

        try:
            with open(file_path, "r") as f:
                recipients = json.load(f)
            logger.info(f"Found {len(recipients)} recipients in {file_path}")
            logger.debug(f"Recipients: {recipients}")
            return recipients
        except (json.JSONDecodeError, Exception) as e:
            logger.error(f"Error reading or parsing recipients file: {str(e)}")
            return []

    async def send_notification(self, house: Optional[House], **kwargs) -> bool:
        """
        Sends a personalized email notification to each recipient.
        Handles both new house notifications and test notifications.
        Uses parallel processing for better performance.
        """
        is_test = kwargs.get("is_test", False)

        if is_test:
            subject = kwargs.get("subject", "Test Notification")
            message = kwargs.get("message", "This is a test.")

            # Create tasks for all test emails in parallel
            tasks = []
            for recipient_data in self.recipients:
                email = recipient_data.get("email")
                if email:
                    task = asyncio.to_thread(
                        self._send_email_sync, subject, message, email
                    )
                    tasks.append(task)

            if not tasks:
                return True

            # Execute all test emails in parallel
            results = await asyncio.gather(*tasks, return_exceptions=True)
            return all(
                result is True
                for result in results
                if not isinstance(result, Exception)
            )

        if not house:
            logger.warning(
                "send_notification called without a house and not in test mode."
            )
            return False

        subject = f"New House Available: {house.address}, {house.city}"

        # Create tasks for all recipients in parallel
        tasks = []
        for recipient_data in self.recipients:
            email = recipient_data.get("email")
            metrics = recipient_data.get("metrics")

            if not email:
                logger.warning(
                    f"Skipping recipient with missing email: {recipient_data}"
                )
                continue

            # Create a task for this recipient (analysis + email sending)
            tasks.append(self._process_recipient_async(house, subject, email, metrics))

        if not tasks:
            logger.warning("No valid recipients found for email notifications")
            return True

        # Execute all recipient processing in parallel
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Count successes and log any exceptions
        successful_count = 0
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                logger.error(
                    f"Failed to process recipient: {str(result)}", exc_info=result
                )
            elif result is True:
                successful_count += 1

        logger.info(
            f"Email notifications: {successful_count}/{len(results)} sent successfully"
        )
        return successful_count == len(results)

    async def _process_recipient_async(
        self, house: House, subject: str, email: str, metrics: Optional[str]
    ) -> bool:
        """
        Process a single recipient: generate analysis and send email.

        Args:
            house: The house object
            subject: Email subject
            email: Recipient email address
            metrics: Personal metrics for this recipient

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Generate personalized analysis
            analysis = await self.llm_service.analyse_house(
                house, personal_metrics=metrics
            )

            # Send email
            success = await asyncio.to_thread(
                self._send_email_sync, subject, analysis, email
            )

            if os.getenv("NOTIFY_ME_OF_ALL_EMAILS") == "true":
                await asyncio.to_thread(
                    self._send_email_sync, subject, analysis, "q.m.b@hotmail.com"
                )

            if success:
                logger.info(f"Email notification sent successfully to {email}")
            else:
                logger.warning(f"Failed to send email to {email}")

            return success

        except Exception as e:
            logger.error(
                f"Failed to generate analysis or send email to {email}: {str(e)}",
                exc_info=True,
            )
            return False

    def _send_email_sync(self, subject: str, message: str, recipient: str) -> bool:
        """Synchronous method to send a single email.

        Args:
            subject: The email subject.
            message: The email body.
            recipient: The email address of the recipient.

        Returns:
            bool: True if the email was sent successfully, False otherwise.
        """
        # The __init__ check ensures these are not None
        assert self.smtp_server is not None
        assert self.email_user is not None
        assert self.email_password is not None

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.email_user, self.email_password)

                email_message = MIMEMultipart()
                email_message["From"] = self.email_user
                email_message["To"] = recipient
                email_message["Subject"] = subject
                email_message.attach(MIMEText(message, "html"))

                server.send_message(email_message)
                logger.info(f"Email notification sent to {recipient}")
                return True
        except Exception as e:
            logger.error(f"Failed to send email to {recipient}: {str(e)}")
            return False
