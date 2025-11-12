import os
from typing import Optional
from crawl4ai import CrawlResult, CrawlerRunConfig, SemaphoreDispatcher
from crawler_job.crawl4ai_wrappers.CustomAsyncWebCrawler import CustomAsyncWebCrawler
from crawler_job.flexibleCrawlers.base_scraper import BaseWebsiteScraper
from crawler_job.models.pydantic_models import WebsiteScrapeConfigJson
from crawler_job.notifications.notification_service import NotificationService
from crawler_job.services.logger_service import setup_logger
from crawler_job.helpers.decorators import (
    requires_crawler_initialized,
    requires_cookies_accepted,
    requires_filtering_config,
)
from crawler_job.services import config as global_config
from crawler_job.services.data_processing_service import DataProcessingService
from crawler_job.services.llm_extraction_service import LlmExtractionService

logger = setup_logger(__name__)


class NmgWonenScraper(BaseWebsiteScraper):
    """Nmg Wonen-specific scraper implementation."""

    def __init__(
        self,
        config: WebsiteScrapeConfigJson,
        session_id: str,
        crawler: CustomAsyncWebCrawler,
        standard_run_config: CrawlerRunConfig,
        standard_dispatcher: SemaphoreDispatcher,
        data_processing_service: DataProcessingService,
        llm_extraction_service: LlmExtractionService,
        notification_service: Optional[NotificationService] = None,
    ):
        super().__init__(
            config=config,
            session_id=session_id,
            crawler=crawler,
            standard_run_config=standard_run_config,
            standard_dispatcher=standard_dispatcher,
            data_processing_service=data_processing_service,
            llm_extraction_service=llm_extraction_service,
            notification_service=notification_service,
        )
        logger.debug("Nmg Wonen scraper initialized...")

    def get_run_config(self) -> CrawlerRunConfig:
        """Overrides the base run config for NMG Wonen specific actions."""
        config = super().get_run_config()
        config.exclude_all_images = False
        config.exclude_social_media_links = False
        return config

    @requires_crawler_initialized
    async def navigate_to_gallery_async(self, force_navigation: bool = False) -> None:
        logger.info("Navigating to gallery in override method...")
        if self.navigated_to_gallery and not force_navigation:
            return

        url = f"{self.website_info.base_url}{self.strategy_config.navigation_config.gallery}"
        config = self.get_run_config()
        result: CrawlResult = await self.crawler.arun_verify_target_url(url, config=config, filename_prefix="navigate_to_gallery", target_paths=["/huur"])  # type: ignore

        logger.info(f"Navigated to gallery successfully: {result.redirected_url}")
        self.navigated_to_gallery = True
        self.current_url = result.redirected_url

    @requires_filtering_config
    async def apply_filters_async(self) -> None:
        logger.info(f"Applying filters to {self.current_url}")
        search_city = self._get_search_city()
        logger.info(f"Applying filters with search city: {search_city}")

        js = f"""
        (async () => {{
            try {{
                const searchContainer = document.querySelector('.search-default');
                const addressInput = searchContainer.querySelector('.search-field--adres input');
                addressInput.value = '{search_city}';
                const searchButton = searchContainer.querySelector('.search-field--button button');
                searchButton.click();
                console.log('Filters applied');
            }} catch (error) {{
                console.error('Fout bij zoeken:', error);
            }}
        }})();
        """

        config = self.get_run_config()
        config.css_selector = self.filtering_config.filters_container_selector or ""
        config.js_code = js
        assert self.current_url is not None
        result: CrawlResult = await self.crawler.arun(
            url="https://nmgwonen.nl/huur/",
            config=config,  # type: ignore
        )
        if not result.success:
            raise Exception(f"Failed to apply filters: {result.error_message}")

        logger.info("Applied filters")
        self.current_url = result.url

    async def _accept_cookies(self, current_url: str) -> bool:
        if not self.cookies_config:
            logger.info("Accepting cookies not required.")
            return True
        if self.accepted_cookies:
            logger.info("Cookies already accepted.")
            return True

        logger.info(f"Accepting cookies for {self.website_config.website_name}...")

        js = f"""
            (async () => {{
                const declineButton = Array.from(document.querySelectorAll('button.btn.btn-default[type="button"]'))
                    .find(btn => btn.textContent && btn.textContent.trim() === "Weigeren");
                if (declineButton) {{
                    declineButton.click();
                    console.log("Decline button clicked");
                }}
                const cookieButton = document.querySelector('{self.cookies_config.accept_cookies_selector}');
                if (cookieButton) {{
                    cookieButton.click();
                    console.log("Cookie button clicked");
                }} else {{
                    console.log("Cookie button not found");
                }}
            }})();
            """

        cookie_config = self.get_run_config()
        cookie_config.js_code = js

        result: CrawlResult = await self.crawler.arun(
            url=current_url, config=cookie_config  # type: ignore
        )

        if result.success:
            logger.info(f"Cookies successfully handled. Current URL: {result.url}")
            self.accepted_cookies = True
        else:
            logger.error(f"Cookie handling failed: {result.error_message}")

        return self.accepted_cookies

    @requires_crawler_initialized
    @requires_cookies_accepted
    async def login_async(self) -> bool:
        try:
            login_url = self.strategy_config.navigation_config.login_page_url
            assert login_url is not None
            logger.info(
                f"Navigating to login page of {self.website_info.name} and logging in."
            )
            email = os.getenv(f"{self.website_info.name.upper()}_EMAIL")
            password = os.getenv(f"{self.website_info.name.upper()}_PASSWORD")

            js_code = [
                f"document.querySelector('{self.login_config.username_selector}').value = '{email}';",
                f"document.querySelector('{self.login_config.password_selector}').value = '{password}';",
                f"document.querySelector('{self.login_config.submit_selector}').click();",
            ]

            wait_for_condition = (
                f"js:() => window.location.pathname !== new URL('{login_url}').pathname"
            )

            run_config = self.get_login_run_config(js_code, wait_for_condition)

            login_result: CrawlResult = await self.crawler.arun_save_screenshot(login_url, config=run_config, filename_prefix="login")  # type: ignore

            if not login_result.success:
                if "Page.content: Unable to retrieve content" in (
                    login_result.error_message or ""
                ):
                    logger.info(
                        "Navigation in progress detected. Waiting for page to stabilize."
                    )

                    stabilize_js = """
                    (() => {
                        try {
                            const weigerButton = Array.from(document.querySelectorAll('button')).find(btn => btn.textContent && btn.textContent.includes('Weiger'));
                            if (weigerButton) { weigerButton.click(); }
                            return window.location.href === "https://nmgwonen.mijnklantdossier.nl/dossier/RelatieDossier.aspx";
                        } catch (e) { return false; }
                    })()
                    """
                    stabilize_config = self.get_run_config()
                    stabilize_config.js_only = True
                    stabilize_config.js_code = stabilize_js
                    stabilize_config.page_timeout = 15000

                    stabilize_result: CrawlResult = await self.crawler.arun(self.current_url or login_url, config=stabilize_config)  # type: ignore

                    if stabilize_result.success:
                        logger.info("Page stabilized successfully.")
                        self.current_url = stabilize_result.url
                        return True
                    else:
                        logger.warning(
                            f"Page stabilization failed: {stabilize_result.error_message}"
                        )
                        return True
                else:
                    raise Exception(
                        f"Login form submission failed: {login_result.error_message}"
                    )

            self.current_url = login_result.url
            return True

        except Exception as e:
            logger.error(f"Login failed: {str(e)}")
            return False
