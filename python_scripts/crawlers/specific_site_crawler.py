from .base_crawler import BaseCrawler

class SpecificSiteCrawler(BaseCrawler):
    async def crawl_specific_data(self, url: str):
        result = await self.crawl_page(url)
        # Add specific parsing logic here
        return result 