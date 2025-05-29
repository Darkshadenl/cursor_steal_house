from typing import Optional
from crawl4ai import AsyncWebCrawler, CrawlResult
from crawler_job.flexibleCrawlers.base_scraper import BaseWebsiteScraper
from crawler_job.models.db_config_models import WebsiteConfig
from crawler_job.notifications.notification_service import NotificationService
from crawler_job.services.logger_service import setup_logger

logger = setup_logger(__name__)


class NmgWonenScraper(BaseWebsiteScraper):
    """Nmg Wonen-specific scraper implementation."""

    def __init__(
        self,
        config: WebsiteConfig,
        session_id: str,
        crawler: AsyncWebCrawler,
        notification_service: Optional[NotificationService] = None,
        debug_mode: bool = False,
    ):
        super().__init__(config, session_id, crawler, notification_service, debug_mode)

        logger.info(f"Nmg Wonen scraper initialized...")

    async def navigate_to_gallery_async(self, force_navigation: bool = False) -> None:
        """Navigate to the listings/gallery page by interacting with the navigation menu."""
        if self.navigated_to_gallery and not force_navigation:
            return

        if not self.crawler:
            raise Exception("Crawler not initialized")

        logger.info(f"Navigating to gallery via navigation menu...")
        url = f"{self.website_config.base_url}"

        js = """
        (async () => {
            try {
                const nav = await window.stealhouse.waitForElement('.navigation', 10000);
                if (!nav) throw new Error('Navigation bar not found');
                const menuItem = document.querySelector('.menu-width > ul:nth-child(1) > li:nth-child(6)');
                if (!menuItem) throw new Error('Menu item not found');
                menuItem.click();
                return { success: true };
            } catch (error) {
                return { success: false, error: error.message };
            }
        })();
        """

        config = self.standard_run_config.clone()
        config.js_code = js
        config.log_console = True
        config.delay_before_return_html = 5
        config.exclude_all_images = False
        config.exclude_social_media_links = False

        result: CrawlResult = await self.crawler.arun(
            url,
            config=config,
        )  # type: ignore

        if (
            result
            and result.success
            and result.redirected_url
            and "/huur" in result.redirected_url
        ):
            logger.info(
                f"Navigated to gallery (huur) successfully: {result.redirected_url}"
            )
            self.navigated_to_gallery = True
            self.current_url = result.redirected_url
        else:
            self.current_url = getattr(result, "redirected_url", None)
            logger.error(
                f"Navigating to gallery failed: {getattr(result, 'error_message', 'Unknown error')}"
            )
            logger.error(f"Redirected URL: {getattr(result, 'redirected_url', None)}")

    async def apply_filters_async(self) -> None:
        """Apply filters if filtering configuration is provided."""
        if not self.filtering_config:
            logger.info("No filtering configuration provided.")
            return

        logger.info(f"Applying filters to {self.current_url}")

        search_input_field = "/html/body/div[2]/div[6]/div[2]/div/form/div[1]/div/div[1]/div[1]/div/input"
        submit_button = (
            "/html/body/div[2]/div[6]/div[2]/div/form/div[1]/div/div[1]/div[6]/button"
        )
        js = """
        (async () => {
    try {
        const searchContainer = document.querySelector('.search-default');

        const addressInput = searchContainer.querySelector('.search-field--adres input');
        addressInput.value = 'Tilburg';
        
        const searchButton = searchContainer.querySelector('.search-field--button button');
        searchButton.click();
        console.log('Filters applied');
    } catch (error) {
        console.error('Fout bij zoeken:', error);
    }
})();

        """

        config = self.standard_run_config.clone()
        config.log_console = True
        config.css_selector = self.filtering_config.filters_container_selector  # type: ignore
        config.js_code = js
        # config.wait_for = f"css:{self.filtering_config.filters_container_selector}"

        result: CrawlResult = await self.crawler.arun(
            url=self.current_url.replace("https://", ""),  # type: ignore
            config=config,
        )
        if not result.success:
            raise Exception(f"Failed to apply filters: {result.error_message}")

        logger.info("Applied filters")
        self.current_url = result.url
