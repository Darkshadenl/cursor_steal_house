"""
Shared pytest fixtures and configuration.
"""

import pytest

# Configure pytest-asyncio
pytest_plugins = ["pytest_asyncio"]

# Instead of trying to set asyncio_mode programmatically,
# add a pytest.ini file with the asyncio_mode configuration

# Add fixtures here that can be reused across multiple test files
# For example:
# @pytest.fixture
# def sample_gallery_house():
#     return GalleryHouse(
#         address="Test Address",
#         city="Test City",
#         status="For Rent",
#         detail_url="https://example.com/house/123"
#     )
