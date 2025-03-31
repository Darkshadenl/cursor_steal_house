from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from typing import Optional

# Global variable to track if we've already accepted cookies
_cookies_accepted = False

async def accept_cookies(crawler: AsyncWebCrawler, url: Optional[str] = None) -> bool:
    """
    Check for cookie popup and accept analytics cookies if present
    Returns True if cookies were accepted or already handled, False on error
    """
    global _cookies_accepted
    
    # Skip if we've already accepted cookies
    if _cookies_accepted:
        print("Cookies already accepted, skipping check")
        return True
    
    # First check if the cookie is already set using JavaScript
    cookie_check_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        js_only=True,
        js_code=[
            """
            () => {
                // Check if Cookiebot cookie is already set
                const cookiebotCookie = document.cookie
                    .split('; ')
                    .find(row => row.startsWith('CookieConsent='));
                
                if (cookiebotCookie) {
                    console.log("Cookiebot cookie already set:", cookiebotCookie);
                    return true;
                }
                
                // Check if the cookie popup exists
                const cookieButton = document.querySelector('a[href*="Cookiebot.submitCustomConsent"]');
                
                if (cookieButton) {
                    console.log("Cookie popup found, accepting analytics cookies");
                    
                    // Click the "Alleen analytisch" button
                    cookieButton.click();
                    
                    return true; // Cookies accepted
                }
                
                return false; // No cookie popup found and no cookie set
            }
            """
        ]
    )
    
    try:
        # Run the cookie check on the current page or specified URL
        result = await crawler.arun(
            url=url or crawler.page.url,
            config=cookie_check_config
        )
        
        if not result.success:
            print("Cookie check failed:", result.error_message)
            return False
        
        # Verify cookies were accepted with a separate config
        verify_config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            js_only=True,
            js_code=[
                """
                () => {
                    // Check if Cookiebot cookie is set
                    const cookiebotCookie = document.cookie
                        .split('; ')
                        .find(row => row.startsWith('CookieConsent='));
                    
                    if (cookiebotCookie) {
                        return true;
                    }
                    
                    // Or check if cookie popup is gone
                    return !document.querySelector('a[href*="Cookiebot.submitCustomConsent"]');
                }
                """
            ]
        )
        
        verify_result = await crawler.arun(
            url=url or crawler.page.url,
            config=verify_config
        )
        
        if verify_result.success:
            print("Cookies successfully accepted or already set")
            _cookies_accepted = True
            return True
        else:
            print("Cookie popup not found or already accepted")
            _cookies_accepted = True  # Assume it's already accepted if not found
            return True
        
    except Exception as e:
        print(f"Error handling cookie popup: {str(e)}")
        return False 