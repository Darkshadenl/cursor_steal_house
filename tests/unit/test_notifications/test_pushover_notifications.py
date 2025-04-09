import dotenv
import pytest
import os
from unittest.mock import patch, AsyncMock
import httpx
from crawler_job.notifications.channels.pushover import PushoverNotificationChannel


@pytest.fixture(scope="module")
def env_vars():
    """Fixture to load environment variables from .env file."""
    if not os.getenv("PUSHOVER_TOKEN") or not os.getenv("PUSHOVER_USER_KEY"):
        pytest.skip(
            "PUSHOVER_TOKEN and PUSHOVER_USER_KEY must be set in .env for integration tests"
        )
    yield


@pytest.fixture
def pushover_channel(env_vars):
    """Fixture to create a PushoverNotificationChannel instance using real env vars."""
    return PushoverNotificationChannel()


def test_init_with_valid_config(env_vars):
    """Test successful initialization reads from environment variables."""
    channel = PushoverNotificationChannel()
    assert channel.pushover_token == os.getenv("PUSHOVER_TOKEN")
    assert channel.pushover_user_key == os.getenv("PUSHOVER_USER_KEY")
    assert channel.api_url == "https://api.pushover.net/1/messages.json"


def test_init_missing_config():
    """Test initialization fails reliably when config is missing."""
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(ValueError) as exc_info:
            PushoverNotificationChannel()
        assert "Missing required Pushover configuration" in str(exc_info.value)


@pytest.mark.asyncio
async def test_send_real_notification_success(pushover_channel):
    """Test sending a REAL notification to Pushover.

    This test requires valid PUSHOVER_TOKEN and PUSHOVER_USER_KEY in the .env file.
    Manually verify the notification arrives on your device.
    """
    subject = "Pytest Real Notification Test"
    message = "This is a test message sent from the pytest integration test."

    print("\nAttempting to send a real Pushover notification...")
    print(f"  Token: {pushover_channel.pushover_token[:4]}...")
    print(f"  User Key: {pushover_channel.pushover_user_key[:4]}...")

    success = await pushover_channel.send_notification(subject, message)

    print(f"Notification send attempt returned: {success}")

    assert success is True

    print("--> Please manually check your Pushover device(s) for the notification. <--")
