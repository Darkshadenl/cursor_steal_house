import asyncio
import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from crawler_job.models.db_config_models import (
    WebsiteConfig,
    WebsiteInfo,
    LoginConfig,
    NavigationConfig,
    ExtractionConfig,
    FieldMapping,
)
from crawler_job.models.house_models import House
from crawler_job.crawlers.configurable_scraper import ConfigurableWebsiteScraper
from crawler_job.services.house_service import HouseService
from crawler_job.services.repositories.config_repository import WebsiteConfigRepository


@pytest.fixture
def mock_config():
    """Create a mock website configuration for testing"""
    return WebsiteConfig(
        website_info=WebsiteInfo(
            id=1,
            name="Test Website",
            base_url="https://example.com",
            is_active=True,
            description="Test website for unit tests",
        ),
        login_config=LoginConfig(
            id=1,
            website_id=1,
            login_url_path="/login",
            username_selector="input#email",
            password_selector="input#password",
            submit_selector="button[type='submit']",
            success_indicator_selector=".user-menu",
            needs_login=True,
            credential_source="env:TEST_EMAIL",
        ),
        navigation_config=NavigationConfig(
            id=1,
            website_id=1,
            gallery_url_path="/properties",
            steps=[{"action": "click", "selector": "a.search-button"}],
            next_page_selector=".pagination-next",
        ),
        gallery_extraction_config=ExtractionConfig(
            id=1,
            website_id=1,
            scope="gallery",
            extraction_method="css",
            base_selector=".property-card",
            field_mappings=[
                FieldMapping(
                    id=1,
                    extraction_config_id=1,
                    pydantic_field_name="address",
                    selector=".property-address",
                    selector_type="css",
                    extraction_type="text",
                    is_required=True,
                ),
                FieldMapping(
                    id=2,
                    extraction_config_id=1,
                    pydantic_field_name="city",
                    selector=".property-city",
                    selector_type="css",
                    extraction_type="text",
                    is_required=True,
                ),
                FieldMapping(
                    id=3,
                    extraction_config_id=1,
                    pydantic_field_name="status",
                    selector=".property-status",
                    selector_type="css",
                    extraction_type="text",
                    is_required=True,
                    default_value="For rent",
                ),
                FieldMapping(
                    id=4,
                    extraction_config_id=1,
                    pydantic_field_name="detail_url",
                    selector=".property-link",
                    selector_type="css",
                    extraction_type="attribute",
                    attribute_name="href",
                    is_required=True,
                ),
            ],
        ),
        detail_extraction_config=ExtractionConfig(
            id=2,
            website_id=1,
            scope="detail",
            extraction_method="llm",
            llm_provider="gemini",
            llm_instruction="Extract property details from this page.",
            field_mappings=[],
        ),
    )


@pytest.fixture
def mock_crawler():
    """Create a mock crawler for testing"""
    mock = AsyncMock()
    mock.arun.return_value = MagicMock(
        success=True, url="https://example.com/properties"
    )
    mock.aeval.side_effect = lambda js: (
        ["element1", "element2"]
        if "querySelectorAll" in js
        else {"textContent": "Test Value"}
    )
    return mock


@pytest.fixture
def mock_config_repo(mock_config):
    """Create a mock config repository for testing"""
    mock = AsyncMock(spec=WebsiteConfigRepository)
    mock.get_config_async.return_value = mock_config
    mock.get_website_id_by_name_async.return_value = 1
    return mock


@pytest.fixture
def mock_house_service():
    """Create a mock house service for testing"""
    mock = AsyncMock(spec=HouseService)
    mock.identify_new_houses_async.return_value = []
    mock.store_houses_atomic_async.return_value = {
        "new_count": 0,
        "existing_count": 2,
        "updated_count": 0,
    }
    return mock


@pytest.fixture
def mock_llm_service():
    """Create a mock LLM service for testing"""
    mock = AsyncMock()
    mock.extract.return_value = (
        '{"address": "123 Test St", "city": "Test City", "status": "For rent"}'
    )
    return mock


@pytest.fixture
def scraper(mock_crawler, mock_config_repo, mock_house_service, mock_llm_service):
    """Create a ConfigurableWebsiteScraper instance for testing"""
    return ConfigurableWebsiteScraper(
        crawler=mock_crawler,
        config_repository=mock_config_repo,
        house_service=mock_house_service,
        llm_service=mock_llm_service,
    )


class TestConfigurableWebsiteScraper:
    """Tests for the ConfigurableWebsiteScraper class"""

    @pytest.mark.asyncio
    async def test_load_config_async(self, scraper, mock_config_repo):
        """Test loading configuration"""
        await scraper.load_config_async(1)
        mock_config_repo.get_config_async.assert_called_once_with(1)
        assert scraper.config is not None
        assert scraper.session_id == "test website_session"

    @pytest.mark.asyncio
    @patch.dict(
        "os.environ",
        {"TEST_EMAIL": "test@example.com", "TEST_EMAIL_PASSWORD": "password"},
    )
    async def test_login_async(self, scraper, mock_crawler):
        """Test login functionality"""
        await scraper.load_config_async(1)
        result = await scraper.login_async()
        assert result is True
        mock_crawler.arun.assert_called_once()
        assert "login" in mock_crawler.arun.call_args[1]["url"]

    @pytest.mark.asyncio
    async def test_navigate_to_gallery_async(self, scraper, mock_crawler):
        """Test navigation to gallery page"""
        await scraper.load_config_async(1)
        result = await scraper.navigate_to_gallery_async()
        assert result == "https://example.com/properties"
        mock_crawler.arun.assert_called_once()
        assert "properties" in mock_crawler.arun.call_args[1]["url"]

    @pytest.mark.asyncio
    async def test_extract_gallery_async(self, scraper, mock_crawler):
        """Test gallery extraction"""
        await scraper.load_config_async(1)
        houses = await scraper.extract_gallery_async()
        assert len(houses) == 2  # Based on our mock returning 2 elements
        assert isinstance(houses[0], House)
        assert mock_crawler.aeval.call_count > 0

    @pytest.mark.asyncio
    async def test_extract_details_async_llm(
        self, scraper, mock_crawler, mock_llm_service
    ):
        """Test detail extraction using LLM"""
        await scraper.load_config_async(1)

        # Create a test house from gallery
        gallery_house = House(
            address="123 Test St",
            city="Test City",
            status="For rent",
            detail_url="https://example.com/property/123",
        )

        detailed_house = await scraper.extract_details_async(gallery_house)

        assert detailed_house is not None
        assert detailed_house.address == "123 Test St"
        assert detailed_house.city == "Test City"
        assert mock_llm_service.extract.call_count == 1

    @pytest.mark.asyncio
    async def test_run_async(self, scraper, mock_config_repo, mock_house_service):
        """Test running the complete scraping process"""
        result = await scraper.run_async(1)

        assert result["success"] is True
        assert result["website_id"] == 1
        assert result["website_name"] == "Test Website"
        assert "total_houses_count" in result
        assert "new_houses_count" in result
        assert "existing_houses_count" in result

        mock_config_repo.get_config_async.assert_called_once()
        mock_house_service.store_houses_atomic_async.assert_called_once()
