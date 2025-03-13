from crawl4ai import Crawler
from typing import Dict, Any

class BaseCrawler:
    def __init__(self):
        self.crawler = Crawler()
        
    async def crawl_page(self, url: str) -> Dict[Any, Any]:
        """
        Basic crawl function that can be extended for specific websites
        """
        try:
            # Configure the crawler with respect to robots.txt
            self.crawler.respect_robots_txt = True
            
            # Crawl the page
            result = await self.crawler.crawl(url)
            return result
            
        except Exception as e:
            print(f"Error crawling {url}: {str(e)}")
            return {}

# Example usage
if __name__ == "__main__":
    import asyncio
    
    async def test_crawler():
        crawler = BaseCrawler()
        result = await crawler.crawl_page("https://example.com")
        print(result)
    
    asyncio.run(test_crawler())
