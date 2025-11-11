from typing import Optional

from crawl4ai import AsyncWebCrawler, CrawlResult, CrawlerRunConfig
from crawl4ai.types import RunManyReturn

from crawler_job.helpers.utils import save_screenshot_from_crawl_result


class CustomAsyncWebCrawler(AsyncWebCrawler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def arun_save_screenshot(
        self,
        url: str,
        config: CrawlerRunConfig,
        filename_prefix: str = "arun_save_screenshot",
        **kwargs,
    ) -> RunManyReturn:
        run_many_result: RunManyReturn = await super().arun(url, config, **kwargs)
        result: CrawlResult = run_many_result.results[0]
        save_screenshot_from_crawl_result(result, filename_prefix)
        return result
