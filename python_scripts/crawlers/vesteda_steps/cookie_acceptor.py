import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from typing import Optional

# Global variable to track if we've already accepted cookies
_cookies_accepted = False

async def accept_cookies(crawler: AsyncWebCrawler, current_url: str) -> bool:
    """
    Check for cookie popup and accept analytics cookies if present
    Returns True if cookies were accepted or already handled, False on error
    """
    global _cookies_accepted
    
    if _cookies_accepted:
        print("Cookies already accepted, skipping check")
        return True
    
    cookie_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        js_only=True,
        wait_for=
        """
            (() => {
                const cookieButton = document.querySelector('a[href="javascript:Cookiebot.submitCustomConsent(false, true, false); Cookiebot.hide()"]');
                if (cookieButton) {
                    console.log("Cookie button found");
                    return true;
                }
                console.log("Cookie button not found");
                return false;
            }
        """,
        js_code=
        """
            () => {
                const cookieButton = document.querySelector('a[href="javascript:Cookiebot.submitCustomConsent(false, true, false); Cookiebot.hide()"]');
                
                if (cookieButton) {
                    cookieButton.click();
                    return true;
                }
                console.log("Cookie button not found");
                return false;
            }
            """
    )
    
    try:
        # Run the cookie check on the current page
        result = await crawler.arun(
            url=current_url,
            config=cookie_config
        )
        
        if not result.success:
            print("Cookie check failed:", result.error_message)
            return False
        elif result.success:
            print(f"Cookies successfully accepted. Current URL: {result.url}")
            _cookies_accepted = True
            return True
        else:
            print("Cookie popup not found or already accepted")
            _cookies_accepted = True 
            return True
        
    except Exception as e:
        print(f"Error handling cookie popup: {str(e)}")
        raise Exception(f"Failed to accept cookies: {str(e)}") 