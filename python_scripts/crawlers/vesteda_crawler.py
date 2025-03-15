import asyncio
import os
import time
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from dotenv import load_dotenv
from .vesteda_steps.login_step import execute_login_step
from .vesteda_steps.search_navigation_step import execute_search_navigation
from .vesteda_steps.property_extraction_step import execute_property_extraction
from .vesteda_steps.cookie_acceptor import accept_cookies

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

class VestedaCrawler():
    def __init__(self):
        # Create browser config first
        self.browser_config = BrowserConfig(
            user_data_dir="./browser_data/vesteda",  # Persistent profile directory
            headless=False,  # Initially false for setup
            verbose=True,     # For debugging
            use_managed_browser=True,  # For persistent sessions
        )
        load_dotenv()
        self.base_url = "https://hurenbij.vesteda.com"
        self.search_url = f"{self.base_url}/zoekopdracht/"
        self.email = os.getenv("VESTEDA_EMAIL")
        self.password = os.getenv("VESTEDA_PASSWORD")
        
    async def run_full_crawl(self):
        """Run the complete crawling process"""
        async with AsyncWebCrawler(config=self.browser_config) as crawler:
            pass
        
if __name__ == "__main__":
    crawler = VestedaCrawler()
    try:
        result = asyncio.run(crawler.run_full_crawl())
        print("Crawl result:", result) 
    except Exception as e:
        print(f"Error during crawl: {str(e)}")
        raise e 