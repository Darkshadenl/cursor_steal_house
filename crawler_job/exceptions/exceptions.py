from typing import Optional
from crawl4ai import CrawlResult


class NavigationFailedException(Exception):
    """Navigation failed."""

    def __init__(
        self,
        message: str = "Navigation failed",
        result: Optional[CrawlResult] = None,
        **kwargs,
    ):
        self.result = result
        self.extra: dict = kwargs
        super().__init__(message)
