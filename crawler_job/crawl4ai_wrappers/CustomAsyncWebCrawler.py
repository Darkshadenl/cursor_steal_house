from typing import Optional

from crawl4ai import AsyncWebCrawler, CrawlResult, CrawlerRunConfig
from crawl4ai.models import CrawlResultContainer
from crawl4ai.types import RunManyReturn

from crawler_job.exceptions.exceptions import NavigationFailedException
from crawler_job.helpers.utils import save_screenshot_from_crawl_result
from crawler_job.services.logger_service import setup_logger

logger = setup_logger(__name__)


class CustomAsyncWebCrawler(AsyncWebCrawler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def arun_save_screenshot(
        self,
        url: str,
        config: CrawlerRunConfig,
        filename_prefix: str = "arun_save_screenshot",
        **kwargs,
    ) -> CrawlResult:
        run_many_result = await super().arun(url, config, **kwargs)  # type: ignore
        result: CrawlResult = run_many_result._results[0]  # type: ignore
        save_screenshot_from_crawl_result(result, filename_prefix)
        return result

    async def arun_verify_target_url(
        self,
        url: str,
        config: CrawlerRunConfig,
        target_url: Optional[str] = None,
        target_paths: Optional[list[str]] = None,
        **kwargs,
    ) -> CrawlResult:
        """Verify if the navigation to the target URL was successful.
        Either uses target_url or target_paths to verify the navigation.
        If both are provided, target_paths is used.
        If neither are provided, the navigation is not verified.

        Args:
            url (str): The URL to navigate to.
            config (CrawlerRunConfig): The configuration for the crawl.
            target_url (Optional[str], optional): The target URL to verify. Defaults to None.
            target_paths (Optional[list[str]], optional): The paths to verify. Defaults to None.

        Raises:
            NavigationFailedException: If the navigation failed.

        Returns:
            RunManyReturn: The result of the crawl.
        """
        result = await self.arun_save_screenshot(
            url, config, "arun_verify_target_url", **kwargs
        )

        if result.success is False:
            raise NavigationFailedException(
                f"Navigation seems to have failed. Result.success: {result.success}",
                result,
            )

        if target_paths and len(target_paths) > 0:
            if not any(path in result.url for path in target_paths):
                raise NavigationFailedException(
                    f"Path check :: Navigation seems to have failed to reach {target_url}",
                    result,
                    target_paths=target_paths,
                )
        elif result.url != target_url or result.redirected_url != target_url:
            raise NavigationFailedException(
                f"Navigation seems to have failed to reach {target_url}", result
            )

        logger.info(
            f"Navigation seems to have reached {target_url}",
            extra={
                "result": result,
                "target_url": target_url,
                "target_paths": target_paths,
            },
        )
        return result
