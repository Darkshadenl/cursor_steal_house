import base64
import os
from typing import Optional
from crawl4ai import CrawlResult
from crawler_job.services.logger_service import setup_logger

logger = setup_logger(__name__)


def save_screenshot_from_crawl_result(
    crawl_result: CrawlResult, filename_prefix: str, output_dir: Optional[str] = None
) -> Optional[str]:
    """
    Save a base64 screenshot from a CrawlResult to a PNG file.

    Args:
        crawl_result: The CrawlResult object containing the screenshot
        filename_prefix: Prefix for the filename (e.g., 'stabilize_screenshot')
        output_dir: Directory to save the screenshot (defaults to current working directory)

    Returns:
        str: Path to the saved screenshot file, or None if no screenshot was available
    """
    if not hasattr(crawl_result, "screenshot") or not crawl_result.screenshot:
        logger.warning("No screenshot available in CrawlResult")
        return None

    if output_dir is None:
        output_dir = f"{os.getcwd()}/debug_screenshots"

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    screenshot_path = os.path.join(output_dir, f"{filename_prefix}.png")

    try:
        with open(screenshot_path, "wb") as f:
            f.write(base64.b64decode(crawl_result.screenshot))

        logger.info(f"Screenshot saved to {screenshot_path}")
        return screenshot_path

    except Exception as e:
        logger.error(f"Failed to save screenshot: {str(e)}")
        return None
