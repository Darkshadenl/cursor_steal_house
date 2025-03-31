import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from typing import Optional

# Global variable to track if we've already accepted cookies
_cookies_accepted = False

async def accept_cookies(crawler: AsyncWebCrawler, current_url: str, session_id: str) -> bool:
    global _cookies_accepted
    
    if _cookies_accepted:
        print("Cookies already accepted, skipping check")
        return True
    
    cookie_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        js_only=True,
        session_id=session_id,
        js_code=
        """
            (async () => {
                Cookiebot.submitCustomConsent(false, true, false); Cookiebot.hide();
                const cookieButton = document.querySelector('a[href="javascript:Cookiebot.submitCustomConsent(false, true, false); Cookiebot.hide()"]');
                
                if (cookieButton) {
                    cookieButton.click();
                    console.log("Cookie button clicked");
                } else {
                    console.log("Cookie button not found");
                    return true;
                }
                
                while (true) {
                    await new Promise(resolve => setTimeout(resolve, 100)); // Wait 100ms
                    const cookieButton = document.querySelector('a[href="javascript:Cookiebot.submitCustomConsent(false, true, false); Cookiebot.hide()"]');
                    if (cookieButton) {
                        cookieButton.click();
                        console.log("Cookie button clicked");
                        return true;
                    }
                }
            })();
            """
    )
    
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