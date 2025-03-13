import os
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig
from dotenv import load_dotenv

class VestedaCrawler:
    def __init__(self):
        load_dotenv()
        self.base_url = "https://hurenbij.vesteda.com/login/"
        self.email = os.getenv("VESTEDA_EMAIL")
        self.password = os.getenv("VESTEDA_PASSWORD")
        
        # Set up browser config with persistent profile
        self.browser_config = BrowserConfig(
            user_data_dir="./browser_data/vesteda",  # Persistent profile directory
            headless=False  # Initially false for setup, can be changed to True later
        )
        
    async def login(self):
        async with AsyncWebCrawler(browser_config=self.browser_config) as crawler:
            # Navigate to login page
            await crawler.goto(self.base_url)
            
            # Fill in login form
            await crawler.fill('input[type="email"]', self.email)
            await crawler.fill('input[type="password"]', self.password)
            
            # Click login button
            await crawler.click('button[type="submit"]')
            
            # Wait for navigation to complete
            await crawler.wait_for_navigation()
            
            return await crawler.get_current_url()

    async def crawl_portal(self):
        # Implementation for crawling after login
        pass

if __name__ == "__main__":
    # Test the crawler
    crawler = VestedaCrawler()
    asyncio.run(crawler.login()) 