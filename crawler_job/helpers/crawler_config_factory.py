import os
from crawl4ai import (
    CrawlerRunConfig,
    RateLimiter,
    SemaphoreDispatcher,
    CrawlerMonitor,
    CacheMode,
)


class CrawlerConfigFactory:
    @staticmethod
    def create_standard_run_config(
        session_id: str, debug_mode: bool
    ) -> CrawlerRunConfig:
        return CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            session_id=session_id,
            log_console=debug_mode,
            js_only=False,
            magic=False,
            exclude_all_images=True,
            exclude_social_media_links=True,
            user_agent_mode="random",
        )

    @staticmethod
    def create_standard_dispatcher() -> SemaphoreDispatcher:
        enable_ui = os.getenv("CRAWLER_ENABLE_UI", "false").lower() == "true"
        return SemaphoreDispatcher(
            semaphore_count=1,
            max_session_permit=1,
            monitor=CrawlerMonitor(urls_total=10, enable_ui=enable_ui),
            rate_limiter=RateLimiter(
                base_delay=(3.0, 5.0),
                max_delay=30.0,
                max_retries=3,
                rate_limit_codes=[429, 503],
            ),
        )

    @staticmethod
    def create_login_run_config(
        standard_config: CrawlerRunConfig,
        full_login_url: str,
        js_code: list[str],
        wait_for_condition: str,
    ) -> CrawlerRunConfig:
        run_config = standard_config.clone()
        run_config.js_code = js_code
        run_config.wait_for = wait_for_condition
        run_config.page_timeout = 10000  # 10 seconds timeout
        return run_config
