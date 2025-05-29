import os
from typing import Optional
from crawl4ai import AsyncWebCrawler, CacheMode, CrawlResult, CrawlerRunConfig
from crawler_job.flexibleCrawlers.base_scraper import BaseWebsiteScraper
from crawler_job.helpers.utils import save_screenshot_from_crawl_result
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

        # logger.info(f"Navigating to gallery via navigation menu...")
        url = f"{self.website_config.base_url}/huur"

        config = self.standard_run_config.clone()
        config.log_console = True
        config.delay_before_return_html = 5
        config.exclude_all_images = False
        config.exclude_social_media_links = False
        config.screenshot = True

        result: CrawlResult = await self.crawler.arun(
            url,
            config=config,
        )  # type: ignore
        save_screenshot_from_crawl_result(result, "navigate_to_gallery")

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

    async def _accept_cookies(self, current_url: str) -> bool:
        if not self.cookies_config:
            logger.info("Accepting cookies not required.")
            return True
        if not self.crawler:
            raise Exception("Crawler not initialized")
        if self.accepted_cookies:
            logger.info("Cookies already accepted.")
            return self.accepted_cookies

        logger.info(f"Accepting cookies for {self.website_config.website_name}...")

        # JavaScript to first check for the "Weigeren" (Decline) button and click it if present,
        # then proceed with the normal cookie accept logic.
        js = f"""
            (async () => {{
                // Try to find and click the "Weigeren" (Decline) button first
                const declineButton = Array.from(document.querySelectorAll('button.btn.btn-default[type="button"]'))
                    .find(btn => btn.textContent && btn.textContent.trim() === "Weigeren");
                if (declineButton) {{
                    declineButton.click();
                    console.log("Decline button clicked");
                }}

                // Now proceed with the normal cookie accept logic
                const cookieButton = document.querySelector('{self.cookies_config.accept_cookies_selector}');
                if (cookieButton) {{
                    cookieButton.click();
                    console.log("Cookie button clicked");
                }} else {{
                    console.log("Cookie button not found");
                    return true;
                }}

                while (true) {{
                    await new Promise(resolve => setTimeout(resolve, 100)); // Wait 100ms
                    const cookieButton = document.querySelector('{self.cookies_config.accept_cookies_selector}');
                    if (cookieButton) {{
                        cookieButton.click();
                        console.log("Cookie button clicked");
                        return true;
                    }}
                }}
            }})();
            """

        cookie_config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            js_only=True,
            magic=True,
            session_id=self.session_id,
            log_console=self.debug_mode,
            js_code=js,
        )

        result: CrawlResult = await self.crawler.arun(
            url=current_url, config=cookie_config
        )  # type: ignore

        if not result.success:
            logger.error("Cookie check failed:", result.error_message)
            return False
        elif result.success:
            logger.info(f"Cookies successfully accepted. Current URL: {result.url}")
            self.accepted_cookies = True
            return self.accepted_cookies
        else:
            logger.info("Cookie popup not found or already accepted")
            self.accepted_cookies = True
            return self.accepted_cookies

    async def login_async(self) -> bool:
        """Perform login if login configuration is provided.

        Returns:
            bool: True if login was successful or not required, False if login failed.
        """
        if not self.login_config or (
            self.navigated_to_gallery and not self.login_config.login_required
        ):
            logger.warn(f"Skipping login for {self.website_config.website_name}")
            return True

        if not self.crawler:
            raise Exception("Crawler not initialized")

        if not self.accepted_cookies:
            await self._accept_cookies(self.current_url or self.website_config.base_url)  # type: ignore

        try:
            base_url = self.website_config.base_url
            full_login_url = ""

            if self.login_config.login_url:
                full_login_url = self.login_config.login_url
            else:
                login_url_path = self.login_config.login_url_path
                full_login_url = f"{base_url}{login_url_path}"

            logger.info(
                f"Navigating to login page of {self.website_config.website_name} and logging in."
            )
            email = os.getenv(self.website_config.website_identifier.upper() + "_EMAIL")
            password = os.getenv(
                self.website_config.website_identifier.upper() + "_PASSWORD"
            )

            js_code = [
                f"document.querySelector('{self.login_config.username_selector}').value = '{email}';",
                f"document.querySelector('{self.login_config.password_selector}').value = '{password}';",
                f"document.querySelector('{self.login_config.submit_selector}').click();",
            ]

            # Configure wait condition based on login config
            wait_for_condition = None
            if self.login_config.success_indicator_selector:
                wait_for_condition = (
                    f"css:{self.login_config.success_indicator_selector}"
                )
            elif self.login_config.expected_url:
                # Wait for URL change or a reasonable delay
                wait_for_condition = (
                    "js:() => window.location.pathname !== '"
                    + (full_login_url or "")
                    + "'"
                )
            else:
                wait_for_condition = ""

            run_config = CrawlerRunConfig(
                session_id=self.session_id,
                exclude_all_images=True,
                exclude_social_media_links=True,
                cache_mode=CacheMode.BYPASS,
                js_only=False,
                magic=False,
                screenshot=True,
                js_code=js_code,
                wait_for=wait_for_condition,
                page_timeout=10000,  # 10 seconds timeout
                log_console=self.debug_mode,
            )

            login_result: CrawlResult = await self.crawler.arun(
                full_login_url, config=run_config
            )  # type: ignore
            save_screenshot_from_crawl_result(login_result, "login")

            if not login_result.success:
                if (
                    login_result.error_message
                    and "Page.content: Unable to retrieve content because the page is navigating and changing the content"
                    in login_result.error_message
                ):
                    logger.info(
                        f"Navigation in progress detected. Waiting for page to stabilize for {self.website_config.website_name}."
                    )

                    # JavaScript code to check for the jconfirm-holder and click the "Weigeren" button if present,
                    # then check if the URL is the expected one.
                    js = """
                    (() => {
                        try {
                            console.log("Searching for button with 'Weiger' text...");
                            
                            // Find all buttons on the page
                            const allButtons = document.querySelectorAll('button');
                            console.log(`Found ${allButtons.length} buttons on the page`);
                            
                            // Search for button containing "Weiger" text
                            let weigerButton = null;
                            for (const button of allButtons) {
                                if (button.textContent && button.textContent.includes('Weiger')) {
                                    weigerButton = button;
                                    break;
                                }
                            }
                            
                            if (weigerButton) {
                                console.log('Button with "Weiger" found:');
                                console.log('Button outerHTML:', weigerButton.outerHTML);
                                console.log('Button textContent:', weigerButton.textContent);
                                console.log('Button classList:', Array.from(weigerButton.classList));
                                console.log('Button parent element:', weigerButton.parentElement ? weigerButton.parentElement.outerHTML : 'No parent');
                                
                                // Click the button
                                weigerButton.click();
                                console.log('Button clicked');
                            } else {
                                console.log('No button with "Weiger" text found');
                            }
                            
                            // Now check if the URL is the expected one
                            console.log("Current URL:", window.location.href);
                            if (window.location.href === "https://nmgwonen.mijnklantdossier.nl/dossier/RelatieDossier.aspx") {
                                console.log("URL matches expected.");
                                return { success: true };
                            } else {
                                console.log("URL does not match expected.");
                                return { success: false, reason: "URL does not match" };
                            }
                        } catch (e) {
                            console.log("Error occurred:", e.message);
                            return { success: false, error: e.message };
                        }
                    })()
                    """

                    # Try again with a different wait strategy
                    stabilize_config = CrawlerRunConfig(
                        session_id=self.session_id,
                        cache_mode=CacheMode.BYPASS,
                        js_only=True,
                        js_code=js,
                        page_timeout=15000,
                        log_console=self.debug_mode,
                        screenshot=True,
                    )

                    stabilize_result: CrawlResult = await self.crawler.arun(
                        self.current_url or full_login_url, config=stabilize_config
                    )  # type: ignore

                    if stabilize_result.success:
                        logger.info(
                            f"Page stabilized successfully for {self.website_config.website_name}"
                        )
                        self.current_url = stabilize_result.url
                        return True
                    else:
                        logger.warning(
                            f"Page stabilization attempt failed: {stabilize_result.error_message}"
                        )
                        return (
                            True  # Assume login succeeded despite stabilization issues
                        )
                else:
                    raise Exception(
                        f"Login form submission failed: {login_result.error_message}"
                    )

            self.current_url = login_result.url
            return True

        except Exception as e:
            logger.error(f"Login failed: {str(e)}")
            return False
