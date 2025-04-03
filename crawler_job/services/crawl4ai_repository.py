import os
import time
import requests
import logging

from crawler_job.models.crawl4ai.models import CrawlRequest

# Set up logger
logger = logging.getLogger(__name__)

api_token = os.getenv("CRAWL4AI_API_TOKEN")
api_url = os.getenv("CRAWL4AI_API_URL")
crawl_api_url = f"{api_url}/crawl"
task_api_url = f"{api_url}/task"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_token}",
}


async def _poll_task_until_complete(task_id, headers, timeout=210):
    """
    Helper function to poll a task until it completes.

    Args:
        task_id: The ID of the task to poll
        headers: Headers to use for the request
        timeout: Timeout in seconds (default: 3.5 minutes)

    Returns:
        The task result on completion, or None on error/timeout
    """
    task_url = f"{task_api_url}/{task_id}"
    start_time = time.time()

    while True:
        # Check if we've exceeded the timeout
        if time.time() - start_time > timeout:
            logger.warning(f"Total polling timeout reached ({timeout} seconds)")
            return None

        task_status_response = requests.get(task_url, headers=headers, timeout=60)
        task_status_response.raise_for_status()
        task_status = task_status_response.json()

        if task_status["status"] == "completed":
            logger.info(f"Task completed: {task_id}")
            return task_status  # Return the actual results
        elif task_status["status"] in ("failed", "pending", "started", "processing"):
            logger.info(f"Task status: {task_status['status']}")
            time.sleep(2)  # Wait before polling again
        else:
            logger.error(f"Unexpected task status: {task_status['status']}")
            return None


async def crawl_single_via_api(crawlRequest: CrawlRequest) -> dict:
    """
    Crawls a single URL using the Crawl4AI Docker service's /crawl endpoint.
    Polls until the task is complete and returns the actual result.
    """
    request_data = crawlRequest.to_dict()
    response = requests.post(
        crawl_api_url, headers=headers, json=request_data, timeout=180
    )
    response.raise_for_status()
    task_response = response.json()

    # Extract task_id and poll for completion
    task_id = task_response.get("task_id")
    if not task_id:
        logger.warning("No task_id in response, returning immediate result")
        return task_response

    # Poll until complete
    result = await _poll_task_until_complete(task_id, headers)
    return result if result else task_response


async def crawl_multiple_via_api(urls):
    """
    Crawls multiple URLs using the Crawl4AI Docker service's /crawl endpoint.
    Submits a crawl task and then polls the /tasks/{task_id} endpoint
    until the task is complete.

    Args:
        urls: A list of URLs to crawl.
        api_token: Optional API token for authentication.

    Returns:
        A list of results (dictionaries), or None on error.
    """
    request_headers = {
        "Content-Type": "application/json",
    }

    request_data = {
        "urls": urls,
        "crawler_params": {
            "headless": True,
        },
        "cache_mode": "bypass",
        "extraction_config": {
            "type": "basic",
            "params": {},
        },
    }

    try:
        response = requests.post(
            crawl_api_url, headers=request_headers, json=request_data, timeout=180
        )
        response.raise_for_status()
        task_response = response.json()
        logger.info(f"Task response: {task_response}")
        task_id = task_response["task_id"]
        logger.info(f"Task ID: {task_id}")

        # Poll until complete
        result = await _poll_task_until_complete(task_id, request_headers)
        return result

    except requests.exceptions.RequestException as e:
        logger.error(f"Error making API call: {e}")
        logger.error(
            f"Response text: {getattr(e.response, 'text', 'No response text')}"
        )
        return None
