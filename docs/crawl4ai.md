# This is documentation for Crawl4ai, meant to help the user with solving crawl4ai related problems in their codebase!



# Table of Contents

- [Home - Crawl4AI Documentation (v0.5.x)](#home-crawl4ai-documentation-v0-5-x-)
- [File Downloading - Crawl4AI Documentation (v0.5.x)](#file-downloading-crawl4ai-documentation-v0-5-x-)
- [Crawl Dispatcher - Crawl4AI Documentation (v0.5.x)](#crawl-dispatcher-crawl4ai-documentation-v0-5-x-)
- [Identity Based Crawling - Crawl4AI Documentation (v0.5.x)](#identity-based-crawling-crawl4ai-documentation-v0-5-x-)
- [Proxy & Security - Crawl4AI Documentation (v0.5.x)](#proxy-security-crawl4ai-documentation-v0-5-x-)
- [Release Summary for Version 0.4.0 (December 1, 2024) - Crawl4AI Documentation (v0.5.x)](#release-summary-for-version-0-4-0-december-1-2024-crawl4ai-documentation-v0-5-x-)
- [Lazy Loading - Crawl4AI Documentation (v0.5.x)](#lazy-loading-crawl4ai-documentation-v0-5-x-)
- [SSL Certificate - Crawl4AI Documentation (v0.5.x)](#ssl-certificate-crawl4ai-documentation-v0-5-x-)
- [arun_many() - Crawl4AI Documentation (v0.5.x)](#arun-many-crawl4ai-documentation-v0-5-x-)
- [Strategies - Crawl4AI Documentation (v0.5.x)](#strategies-crawl4ai-documentation-v0-5-x-)
- [Dockerize hooks - Crawl4AI Documentation (v0.5.x)](#dockerize-hooks-crawl4ai-documentation-v0-5-x-)
- [CrawlResult - Crawl4AI Documentation (v0.5.x)](#crawlresult-crawl4ai-documentation-v0-5-x-)
- [Hooks & Auth - Crawl4AI Documentation (v0.5.x)](#hooks-auth-crawl4ai-documentation-v0-5-x-)
- [Session Management - Crawl4AI Documentation (v0.5.x)](#session-management-crawl4ai-documentation-v0-5-x-)
- [Overview - Crawl4AI Documentation (v0.5.x)](#overview-crawl4ai-documentation-v0-5-x-)
- [Multi-URL Crawling - Crawl4AI Documentation (v0.5.x)](#multi-url-crawling-crawl4ai-documentation-v0-5-x-)
- [Release Summary for Version 0.4.1 (December 8, 2024): Major Efficiency Boosts with New Features! - Crawl4AI Documentation (v0.5.x)](#release-summary-for-version-0-4-1-december-8-2024-major-efficiency-boosts-with-new-features-crawl4ai-documentation-v0-5-x-)
- [arun() - Crawl4AI Documentation (v0.5.x)](#arun-crawl4ai-documentation-v0-5-x-)
- [Blog Home - Crawl4AI Documentation (v0.5.x)](#blog-home-crawl4ai-documentation-v0-5-x-)
- [Installation 💻 - Crawl4AI Documentation (v0.5.x)](#installation-crawl4ai-documentation-v0-5-x-)
- [Browser, Crawler & LLM Config - Crawl4AI Documentation (v0.5.x)](#browser-crawler-llm-config-crawl4ai-documentation-v0-5-x-)
- [AsyncWebCrawler - Crawl4AI Documentation (v0.5.x)](#asyncwebcrawler-crawl4ai-documentation-v0-5-x-)
- [0.4.2 - Crawl4AI Documentation (v0.5.x)](#0-4-2-crawl4ai-documentation-v0-5-x-)
- [Crawl4AI 0.4.3: Major Performance Boost & LLM Integration - Crawl4AI Documentation (v0.5.x)](#crawl4ai-0-4-3-major-performance-boost-llm-integration-crawl4ai-documentation-v0-5-x-)
- [Browser, Crawler & LLM Config - Crawl4AI Documentation (v0.5.x)](#browser-crawler-llm-config-crawl4ai-documentation-v0-5-x-)
- [Crawl4AI v0.5.0 Release Notes - Crawl4AI Documentation (v0.5.x)](#crawl4ai-v0-5-0-release-notes-crawl4ai-documentation-v0-5-x-)
- [Cache Modes - Crawl4AI Documentation (v0.5.x)](#cache-modes-crawl4ai-documentation-v0-5-x-)
- [Command Line Interface - Crawl4AI Documentation (v0.5.x)](#command-line-interface-crawl4ai-documentation-v0-5-x-)
- [Crawler Result - Crawl4AI Documentation (v0.5.x)](#crawler-result-crawl4ai-documentation-v0-5-x-)
- [Deep Crawling - Crawl4AI Documentation (v0.5.x)](#deep-crawling-crawl4ai-documentation-v0-5-x-)
- [Content Selection - Crawl4AI Documentation (v0.5.x)](#content-selection-crawl4ai-documentation-v0-5-x-)
- [Docker Deployment - Crawl4AI Documentation (v0.5.x)](#docker-deployment-crawl4ai-documentation-v0-5-x-)
- [Installation - Crawl4AI Documentation (v0.5.x)](#installation-crawl4ai-documentation-v0-5-x-)
- [Fit Markdown - Crawl4AI Documentation (v0.5.x)](#fit-markdown-crawl4ai-documentation-v0-5-x-)
- [Link & Media - Crawl4AI Documentation (v0.5.x)](#link-media-crawl4ai-documentation-v0-5-x-)
- [Local Files & Raw HTML - Crawl4AI Documentation (v0.5.x)](#local-files-raw-html-crawl4ai-documentation-v0-5-x-)
- [Markdown Generation - Crawl4AI Documentation (v0.5.x)](#markdown-generation-crawl4ai-documentation-v0-5-x-)
- [Chunking - Crawl4AI Documentation (v0.5.x)](#chunking-crawl4ai-documentation-v0-5-x-)
- [Simple Crawling - Crawl4AI Documentation (v0.5.x)](#simple-crawling-crawl4ai-documentation-v0-5-x-)
- [LLM Strategies - Crawl4AI Documentation (v0.5.x)](#llm-strategies-crawl4ai-documentation-v0-5-x-)
- [404 Not Found](#404-not-found)
- [Clustering Strategies - Crawl4AI Documentation (v0.5.x)](#clustering-strategies-crawl4ai-documentation-v0-5-x-)
- [Page Interaction - Crawl4AI Documentation (v0.5.x)](#page-interaction-crawl4ai-documentation-v0-5-x-)
- [Quick Start - Crawl4AI Documentation (v0.5.x)](#quick-start-crawl4ai-documentation-v0-5-x-)
- [LLM-Free Strategies - Crawl4AI Documentation (v0.5.x)](#llm-free-strategies-crawl4ai-documentation-v0-5-x-)

---

# Home - Crawl4AI Documentation (v0.5.x)

🚀🤖 Crawl4AI: Open-Source LLM-Friendly Web Crawler & Scraper
=============================================================

[![unclecode%2Fcrawl4ai | Trendshift](https://trendshift.io/api/badge/repositories/11716)](https://trendshift.io/repositories/11716)

 [![GitHub Stars](https://img.shields.io/github/stars/unclecode/crawl4ai?style=social)](https://github.com/unclecode/crawl4ai/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/unclecode/crawl4ai?style=social)](https://github.com/unclecode/crawl4ai/network/members)
[![PyPI version](https://badge.fury.io/py/crawl4ai.svg)](https://badge.fury.io/py/crawl4ai)

 [![Python Version](https://img.shields.io/pypi/pyversions/crawl4ai)](https://pypi.org/project/crawl4ai/)
[![Downloads](https://static.pepy.tech/badge/crawl4ai/month)](https://pepy.tech/project/crawl4ai)
[![License](https://img.shields.io/github/license/unclecode/crawl4ai)](https://github.com/unclecode/crawl4ai/blob/main/LICENSE)

Crawl4AI is the #1 trending GitHub repository, actively maintained by a vibrant community. It delivers blazing-fast, AI-ready web crawling tailored for large language models, AI agents, and data pipelines. Fully open source, flexible, and built for real-time performance, **Crawl4AI** empowers developers with unmatched speed, precision, and deployment ease.

> **Note**: If you're looking for the old documentation, you can access it [here](https://old.docs.crawl4ai.com)
> .

Quick Start
-----------

Here's a quick example to show you how easy it is to use Crawl4AI with its asynchronous capabilities:

`[](#__codelineno-0-1) import asyncio [](#__codelineno-0-2) from crawl4ai import AsyncWebCrawler [](#__codelineno-0-3) [](#__codelineno-0-4) async def main(): [](#__codelineno-0-5)     # Create an instance of AsyncWebCrawler [](#__codelineno-0-6)     async with AsyncWebCrawler() as crawler: [](#__codelineno-0-7)         # Run the crawler on a URL [](#__codelineno-0-8)         result = await crawler.arun(url="https://crawl4ai.com") [](#__codelineno-0-9) [](#__codelineno-0-10)         # Print the extracted content [](#__codelineno-0-11)         print(result.markdown) [](#__codelineno-0-12) [](#__codelineno-0-13) # Run the async main function [](#__codelineno-0-14) asyncio.run(main())`

* * *

What Does Crawl4AI Do?
----------------------

Crawl4AI is a feature-rich crawler and scraper that aims to:

1. **Generate Clean Markdown**: Perfect for RAG pipelines or direct ingestion into LLMs.  
2. **Structured Extraction**: Parse repeated patterns with CSS, XPath, or LLM-based extraction.  
3. **Advanced Browser Control**: Hooks, proxies, stealth modes, session re-use—fine-grained control.  
4. **High Performance**: Parallel crawling, chunk-based extraction, real-time use cases.  
5. **Open Source**: No forced API keys, no paywalls—everyone can access their data.

**Core Philosophies**: - **Democratize Data**: Free to use, transparent, and highly configurable.  
\- **LLM Friendly**: Minimally processed, well-structured text, images, and metadata, so AI models can easily consume it.

* * *

Documentation Structure
-----------------------

To help you get started, we’ve organized our docs into clear sections:

*   **Setup & Installation**  
    Basic instructions to install Crawl4AI via pip or Docker.
*   **Quick Start**  
    A hands-on introduction showing how to do your first crawl, generate Markdown, and do a simple extraction.
*   **Core**  
    Deeper guides on single-page crawling, advanced browser/crawler parameters, content filtering, and caching.
*   **Advanced**  
    Explore link & media handling, lazy loading, hooking & authentication, proxies, session management, and more.
*   **Extraction**  
    Detailed references for no-LLM (CSS, XPath) vs. LLM-based strategies, chunking, and clustering approaches.
*   **API Reference**  
    Find the technical specifics of each class and method, including `AsyncWebCrawler`, `arun()`, and `CrawlResult`.

Throughout these sections, you’ll find code samples you can **copy-paste** into your environment. If something is missing or unclear, raise an issue or PR.

* * *

How You Can Support
-------------------

*   **Star & Fork**: If you find Crawl4AI helpful, star the repo on GitHub or fork it to add your own features.
*   **File Issues**: Encounter a bug or missing feature? Let us know by filing an issue, so we can improve.
*   **Pull Requests**: Whether it’s a small fix, a big feature, or better docs—contributions are always welcome.
*   **Join Discord**: Come chat about web scraping, crawling tips, or AI workflows with the community.
*   **Spread the Word**: Mention Crawl4AI in your blog posts, talks, or on social media.

**Our mission**: to empower everyone—students, researchers, entrepreneurs, data scientists—to access, parse, and shape the world’s data with speed, cost-efficiency, and creative freedom.

* * *

Quick Links
-----------

*   **[GitHub Repo](https://github.com/unclecode/crawl4ai)
    **
*   **[Installation Guide](core/installation/)
    **
*   **[Quick Start](core/quickstart/)
    **
*   **[API Reference](api/async-webcrawler/)
    **
*   **[Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
    **

Thank you for joining me on this journey. Let’s keep building an **open, democratic** approach to data extraction and AI together.

Happy Crawling!  
— _Unclecode, Founder & Maintainer of Crawl4AI_

* * *

---

# File Downloading - Crawl4AI Documentation (v0.5.x)

Download Handling in Crawl4AI
=============================

This guide explains how to use Crawl4AI to handle file downloads during crawling. You'll learn how to trigger downloads, specify download locations, and access downloaded files.

Enabling Downloads
------------------

To enable downloads, set the `accept_downloads` parameter in the `BrowserConfig` object and pass it to the crawler.

`[](#__codelineno-0-1) from crawl4ai.async_configs import BrowserConfig, AsyncWebCrawler [](#__codelineno-0-2) [](#__codelineno-0-3) async def main(): [](#__codelineno-0-4)     config = BrowserConfig(accept_downloads=True)  # Enable downloads globally [](#__codelineno-0-5)     async with AsyncWebCrawler(config=config) as crawler: [](#__codelineno-0-6)         # ... your crawling logic ... [](#__codelineno-0-7) [](#__codelineno-0-8) asyncio.run(main())`

Specifying Download Location
----------------------------

Specify the download directory using the `downloads_path` attribute in the `BrowserConfig` object. If not provided, Crawl4AI defaults to creating a "downloads" directory inside the `.crawl4ai` folder in your home directory.

`[](#__codelineno-1-1) from crawl4ai.async_configs import BrowserConfig [](#__codelineno-1-2) import os [](#__codelineno-1-3) [](#__codelineno-1-4) downloads_path = os.path.join(os.getcwd(), "my_downloads")  # Custom download path [](#__codelineno-1-5) os.makedirs(downloads_path, exist_ok=True) [](#__codelineno-1-6) [](#__codelineno-1-7) config = BrowserConfig(accept_downloads=True, downloads_path=downloads_path) [](#__codelineno-1-8) [](#__codelineno-1-9) async def main(): [](#__codelineno-1-10)     async with AsyncWebCrawler(config=config) as crawler: [](#__codelineno-1-11)         result = await crawler.arun(url="https://example.com") [](#__codelineno-1-12)         # ...`

Triggering Downloads
--------------------

Downloads are typically triggered by user interactions on a web page, such as clicking a download button. Use `js_code` in `CrawlerRunConfig` to simulate these actions and `wait_for` to allow sufficient time for downloads to start.

`[](#__codelineno-2-1) from crawl4ai.async_configs import CrawlerRunConfig [](#__codelineno-2-2) [](#__codelineno-2-3) config = CrawlerRunConfig( [](#__codelineno-2-4)     js_code=""" [](#__codelineno-2-5)         const downloadLink = document.querySelector('a[href$=".exe"]'); [](#__codelineno-2-6)         if (downloadLink) { [](#__codelineno-2-7)             downloadLink.click(); [](#__codelineno-2-8)         } [](#__codelineno-2-9)     """, [](#__codelineno-2-10)     wait_for=5  # Wait 5 seconds for the download to start [](#__codelineno-2-11) ) [](#__codelineno-2-12) [](#__codelineno-2-13) result = await crawler.arun(url="https://www.python.org/downloads/", config=config)`

Accessing Downloaded Files
--------------------------

The `downloaded_files` attribute of the `CrawlResult` object contains paths to downloaded files.

`[](#__codelineno-3-1) if result.downloaded_files: [](#__codelineno-3-2)     print("Downloaded files:") [](#__codelineno-3-3)     for file_path in result.downloaded_files: [](#__codelineno-3-4)         print(f"- {file_path}") [](#__codelineno-3-5)         file_size = os.path.getsize(file_path) [](#__codelineno-3-6)         print(f"- File size: {file_size} bytes") [](#__codelineno-3-7) else: [](#__codelineno-3-8)     print("No files downloaded.")`

Example: Downloading Multiple Files
-----------------------------------

`[](#__codelineno-4-1) from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig [](#__codelineno-4-2) import os [](#__codelineno-4-3) from pathlib import Path [](#__codelineno-4-4) [](#__codelineno-4-5) async def download_multiple_files(url: str, download_path: str): [](#__codelineno-4-6)     config = BrowserConfig(accept_downloads=True, downloads_path=download_path) [](#__codelineno-4-7)     async with AsyncWebCrawler(config=config) as crawler: [](#__codelineno-4-8)         run_config = CrawlerRunConfig( [](#__codelineno-4-9)             js_code=""" [](#__codelineno-4-10)                 const downloadLinks = document.querySelectorAll('a[download]'); [](#__codelineno-4-11)                 for (const link of downloadLinks) { [](#__codelineno-4-12)                     link.click(); [](#__codelineno-4-13)                     // Delay between clicks [](#__codelineno-4-14)                     await new Promise(r => setTimeout(r, 2000));   [](#__codelineno-4-15)                 } [](#__codelineno-4-16)             """, [](#__codelineno-4-17)             wait_for=10  # Wait for all downloads to start [](#__codelineno-4-18)         ) [](#__codelineno-4-19)         result = await crawler.arun(url=url, config=run_config) [](#__codelineno-4-20) [](#__codelineno-4-21)         if result.downloaded_files: [](#__codelineno-4-22)             print("Downloaded files:") [](#__codelineno-4-23)             for file in result.downloaded_files: [](#__codelineno-4-24)                 print(f"- {file}") [](#__codelineno-4-25)         else: [](#__codelineno-4-26)             print("No files downloaded.") [](#__codelineno-4-27) [](#__codelineno-4-28) # Usage [](#__codelineno-4-29) download_path = os.path.join(Path.home(), ".crawl4ai", "downloads") [](#__codelineno-4-30) os.makedirs(download_path, exist_ok=True) [](#__codelineno-4-31) [](#__codelineno-4-32) asyncio.run(download_multiple_files("https://www.python.org/downloads/windows/", download_path))`

Important Considerations
------------------------

*   **Browser Context:** Downloads are managed within the browser context. Ensure `js_code` correctly targets the download triggers on the webpage.
*   **Timing:** Use `wait_for` in `CrawlerRunConfig` to manage download timing.
*   **Error Handling:** Handle errors to manage failed downloads or incorrect paths gracefully.
*   **Security:** Scan downloaded files for potential security threats before use.

This revised guide ensures consistency with the `Crawl4AI` codebase by using `BrowserConfig` and `CrawlerRunConfig` for all download-related configurations. Let me know if further adjustments are needed!

* * *

---

# Crawl Dispatcher - Crawl4AI Documentation (v0.5.x)

Crawl Dispatcher
================

We’re excited to announce a **Crawl Dispatcher** module that can handle **thousands** of crawling tasks simultaneously. By efficiently managing system resources (memory, CPU, network), this dispatcher ensures high-performance data extraction at scale. It also provides **real-time monitoring** of each crawler’s status, memory usage, and overall progress.

Stay tuned—this feature is **coming soon** in an upcoming release of Crawl4AI! For the latest news, keep an eye on our changelogs and follow [@unclecode](https://twitter.com/unclecode)
 on X.

Below is a **sample** of how the dispatcher’s performance monitor might look in action:

![Crawl Dispatcher Performance Monitor](../../assets/images/dispatcher.png)

We can’t wait to bring you this streamlined, **scalable** approach to multi-URL crawling—**watch this space** for updates!

* * *

---

# Identity Based Crawling - Crawl4AI Documentation (v0.5.x)

Preserve Your Identity with Crawl4AI
====================================

Crawl4AI empowers you to navigate and interact with the web using your **authentic digital identity**, ensuring you’re recognized as a human and not mistaken for a bot. This tutorial covers:

1. **Managed Browsers** – The recommended approach for persistent profiles and identity-based crawling.  
2. **Magic Mode** – A simplified fallback solution for quick automation without persistent identity.

* * *

1\. Managed Browsers: Your Digital Identity Solution
----------------------------------------------------

**Managed Browsers** let developers create and use **persistent browser profiles**. These profiles store local storage, cookies, and other session data, letting you browse as your **real self**—complete with logins, preferences, and cookies.

### Key Benefits

*   **Authentic Browsing Experience**: Retain session data and browser fingerprints as though you’re a normal user.
*   **Effortless Configuration**: Once you log in or solve CAPTCHAs in your chosen data directory, you can re-run crawls without repeating those steps.
*   **Empowered Data Access**: If you can see the data in your own browser, you can automate its retrieval with your genuine identity.

* * *

Below is a **partial update** to your **Managed Browsers** tutorial, specifically the section about **creating a user-data directory** using **Playwright’s Chromium** binary rather than a system-wide Chrome/Edge. We’ll show how to **locate** that binary and launch it with a `--user-data-dir` argument to set up your profile. You can then point `BrowserConfig.user_data_dir` to that folder for subsequent crawls.

* * *

### Creating a User Data Directory (Command-Line Approach via Playwright)

If you installed Crawl4AI (which installs Playwright under the hood), you already have a Playwright-managed Chromium on your system. Follow these steps to launch that **Chromium** from your command line, specifying a **custom** data directory:

1. **Find** the Playwright Chromium binary: - On most systems, installed browsers go under a `~/.cache/ms-playwright/` folder or similar path.  
\- To see an overview of installed browsers, run:

`[](#__codelineno-0-1) python -m playwright install --dry-run`

or

`[](#__codelineno-1-1) playwright install --dry-run`

(depending on your environment). This shows where Playwright keeps Chromium.

*   For instance, you might see a path like:
    
    `[](#__codelineno-2-1) ~/.cache/ms-playwright/chromium-1234/chrome-linux/chrome`
    
    on Linux, or a corresponding folder on macOS/Windows.

2. **Launch** the Playwright Chromium binary with a **custom** user-data directory:

`[](#__codelineno-3-1) # Linux example [](#__codelineno-3-2) ~/.cache/ms-playwright/chromium-1234/chrome-linux/chrome \ [](#__codelineno-3-3)     --user-data-dir=/home/<you>/my_chrome_profile`

`[](#__codelineno-4-1) # macOS example (Playwright’s internal binary) [](#__codelineno-4-2) ~/Library/Caches/ms-playwright/chromium-1234/chrome-mac/Chromium.app/Contents/MacOS/Chromium \ [](#__codelineno-4-3)     --user-data-dir=/Users/<you>/my_chrome_profile`

`[](#__codelineno-5-1) # Windows example (PowerShell/cmd) [](#__codelineno-5-2) "C:\Users\<you>\AppData\Local\ms-playwright\chromium-1234\chrome-win\chrome.exe" ^ [](#__codelineno-5-3)     --user-data-dir="C:\Users\<you>\my_chrome_profile"`

**Replace** the path with the actual subfolder indicated in your `ms-playwright` cache structure.  
\- This **opens** a fresh Chromium with your new or existing data folder.  
\- **Log into** any sites or configure your browser the way you want.  
\- **Close** when done—your profile data is saved in that folder.

3. **Use** that folder in **`BrowserConfig.user_data_dir`**:

`[](#__codelineno-6-1) from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig [](#__codelineno-6-2) [](#__codelineno-6-3) browser_config = BrowserConfig( [](#__codelineno-6-4)     headless=True, [](#__codelineno-6-5)     use_managed_browser=True, [](#__codelineno-6-6)     user_data_dir="/home/<you>/my_chrome_profile", [](#__codelineno-6-7)     browser_type="chromium" [](#__codelineno-6-8) )`

\- Next time you run your code, it reuses that folder—**preserving** your session data, cookies, local storage, etc.

* * *

3\. Using Managed Browsers in Crawl4AI
--------------------------------------

Once you have a data directory with your session data, pass it to **`BrowserConfig`**:

`[](#__codelineno-7-1) import asyncio [](#__codelineno-7-2) from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig [](#__codelineno-7-3) [](#__codelineno-7-4) async def main(): [](#__codelineno-7-5)     # 1) Reference your persistent data directory [](#__codelineno-7-6)     browser_config = BrowserConfig( [](#__codelineno-7-7)         headless=True,             # 'True' for automated runs [](#__codelineno-7-8)         verbose=True, [](#__codelineno-7-9)         use_managed_browser=True,  # Enables persistent browser strategy [](#__codelineno-7-10)         browser_type="chromium", [](#__codelineno-7-11)         user_data_dir="/path/to/my-chrome-profile" [](#__codelineno-7-12)     ) [](#__codelineno-7-13) [](#__codelineno-7-14)     # 2) Standard crawl config [](#__codelineno-7-15)     crawl_config = CrawlerRunConfig( [](#__codelineno-7-16)         wait_for="css:.logged-in-content" [](#__codelineno-7-17)     ) [](#__codelineno-7-18) [](#__codelineno-7-19)     async with AsyncWebCrawler(config=browser_config) as crawler: [](#__codelineno-7-20)         result = await crawler.arun(url="https://example.com/private", config=crawl_config) [](#__codelineno-7-21)         if result.success: [](#__codelineno-7-22)             print("Successfully accessed private data with your identity!") [](#__codelineno-7-23)         else: [](#__codelineno-7-24)             print("Error:", result.error_message) [](#__codelineno-7-25) [](#__codelineno-7-26) if __name__ == "__main__": [](#__codelineno-7-27)     asyncio.run(main())`

### Workflow

1. **Login** externally (via CLI or your normal Chrome with `--user-data-dir=...`).  
2. **Close** that browser.  
3. **Use** the same folder in `user_data_dir=` in Crawl4AI.  
4. **Crawl** – The site sees your identity as if you’re the same user who just logged in.

* * *

4\. Magic Mode: Simplified Automation
-------------------------------------

If you **don’t** need a persistent profile or identity-based approach, **Magic Mode** offers a quick way to simulate human-like browsing without storing long-term data.

`[](#__codelineno-8-1) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig [](#__codelineno-8-2) [](#__codelineno-8-3) async with AsyncWebCrawler() as crawler: [](#__codelineno-8-4)     result = await crawler.arun( [](#__codelineno-8-5)         url="https://example.com", [](#__codelineno-8-6)         config=CrawlerRunConfig( [](#__codelineno-8-7)             magic=True,  # Simplifies a lot of interaction [](#__codelineno-8-8)             remove_overlay_elements=True, [](#__codelineno-8-9)             page_timeout=60000 [](#__codelineno-8-10)         ) [](#__codelineno-8-11)     )`

**Magic Mode**:

*   Simulates a user-like experience
*   Randomizes user agent & navigator
*   Randomizes interactions & timings
*   Masks automation signals
*   Attempts pop-up handling

**But** it’s no substitute for **true** user-based sessions if you want a fully legitimate identity-based solution.

* * *

5\. Comparing Managed Browsers vs. Magic Mode
---------------------------------------------

| Feature                 | **Managed Browsers**                                       | **Magic Mode**                                      |
| ----------------------- | ---------------------------------------------------------- | --------------------------------------------------- |
| **Session Persistence** | Full localStorage/cookies retained in user\_data\_dir      | No persistent data (fresh each run)                 |
| **Genuine Identity**    | Real user profile with full rights & preferences           | Emulated user-like patterns, but no actual identity |
| **Complex Sites**       | Best for login-gated sites or heavy config                 | Simple tasks, minimal login or config needed        |
| **Setup**               | External creation of user\_data\_dir, then use in Crawl4AI | Single-line approach (`magic=True`)                 |
| **Reliability**         | Extremely consistent (same data across runs)               | Good for smaller tasks, can be less stable          |

* * *

6\. Using the BrowserProfiler Class
-----------------------------------

Crawl4AI provides a dedicated `BrowserProfiler` class for managing browser profiles, making it easy to create, list, and delete profiles for identity-based browsing.

### Creating and Managing Profiles with BrowserProfiler

The `BrowserProfiler` class offers a comprehensive API for browser profile management:

`[](#__codelineno-9-1) import asyncio [](#__codelineno-9-2) from crawl4ai import BrowserProfiler [](#__codelineno-9-3) [](#__codelineno-9-4) async def manage_profiles(): [](#__codelineno-9-5)     # Create a profiler instance [](#__codelineno-9-6)     profiler = BrowserProfiler() [](#__codelineno-9-7) [](#__codelineno-9-8)     # Create a profile interactively - opens a browser window [](#__codelineno-9-9)     profile_path = await profiler.create_profile( [](#__codelineno-9-10)         profile_name="my-login-profile"  # Optional: name your profile [](#__codelineno-9-11)     ) [](#__codelineno-9-12) [](#__codelineno-9-13)     print(f"Profile saved at: {profile_path}") [](#__codelineno-9-14) [](#__codelineno-9-15)     # List all available profiles [](#__codelineno-9-16)     profiles = profiler.list_profiles() [](#__codelineno-9-17) [](#__codelineno-9-18)     for profile in profiles: [](#__codelineno-9-19)         print(f"Profile: {profile['name']}") [](#__codelineno-9-20)         print(f"  Path: {profile['path']}") [](#__codelineno-9-21)         print(f"  Created: {profile['created']}") [](#__codelineno-9-22)         print(f"  Browser type: {profile['type']}") [](#__codelineno-9-23) [](#__codelineno-9-24)     # Get a specific profile path by name [](#__codelineno-9-25)     specific_profile = profiler.get_profile_path("my-login-profile") [](#__codelineno-9-26) [](#__codelineno-9-27)     # Delete a profile when no longer needed [](#__codelineno-9-28)     success = profiler.delete_profile("old-profile-name") [](#__codelineno-9-29) [](#__codelineno-9-30) asyncio.run(manage_profiles())`

**How profile creation works:** 1. A browser window opens for you to interact with 2. You log in to websites, set preferences, etc. 3. When you're done, press 'q' in the terminal to close the browser 4. The profile is saved in the Crawl4AI profiles directory 5. You can use the returned path with `BrowserConfig.user_data_dir`

### Interactive Profile Management

The `BrowserProfiler` also offers an interactive management console that guides you through profile creation, listing, and deletion:

`[](#__codelineno-10-1) import asyncio [](#__codelineno-10-2) from crawl4ai import BrowserProfiler, AsyncWebCrawler, BrowserConfig [](#__codelineno-10-3) [](#__codelineno-10-4) # Define a function to use a profile for crawling [](#__codelineno-10-5) async def crawl_with_profile(profile_path, url): [](#__codelineno-10-6)     browser_config = BrowserConfig( [](#__codelineno-10-7)         headless=True, [](#__codelineno-10-8)         use_managed_browser=True, [](#__codelineno-10-9)         user_data_dir=profile_path [](#__codelineno-10-10)     ) [](#__codelineno-10-11) [](#__codelineno-10-12)     async with AsyncWebCrawler(config=browser_config) as crawler: [](#__codelineno-10-13)         result = await crawler.arun(url) [](#__codelineno-10-14)         return result [](#__codelineno-10-15) [](#__codelineno-10-16) async def main(): [](#__codelineno-10-17)     # Create a profiler instance [](#__codelineno-10-18)     profiler = BrowserProfiler() [](#__codelineno-10-19) [](#__codelineno-10-20)     # Launch the interactive profile manager [](#__codelineno-10-21)     # Passing the crawl function as a callback adds a "crawl with profile" option [](#__codelineno-10-22)     await profiler.interactive_manager(crawl_callback=crawl_with_profile) [](#__codelineno-10-23) [](#__codelineno-10-24) asyncio.run(main())`

### Legacy Methods

For backward compatibility, the previous methods on `ManagedBrowser` are still available, but they delegate to the new `BrowserProfiler` class:

`[](#__codelineno-11-1) from crawl4ai.browser_manager import ManagedBrowser [](#__codelineno-11-2) [](#__codelineno-11-3) # These methods still work but use BrowserProfiler internally [](#__codelineno-11-4) profiles = ManagedBrowser.list_profiles()`

### Complete Example

See the full example in `docs/examples/identity_based_browsing.py` for a complete demonstration of creating and using profiles for authenticated browsing using the new `BrowserProfiler` class.

* * *

7\. Summary
-----------

*   **Create** your user-data directory either:
*   By launching Chrome/Chromium externally with `--user-data-dir=/some/path`
*   Or by using the built-in `BrowserProfiler.create_profile()` method
*   Or through the interactive interface with `profiler.interactive_manager()`
*   **Log in** or configure sites as needed, then close the browser
*   **Reference** that folder in `BrowserConfig(user_data_dir="...")` + `use_managed_browser=True`
*   **List and reuse** profiles with `BrowserProfiler.list_profiles()`
*   **Manage** your profiles with the dedicated `BrowserProfiler` class
*   Enjoy **persistent** sessions that reflect your real identity
*   If you only need quick, ephemeral automation, **Magic Mode** might suffice

**Recommended**: Always prefer a **Managed Browser** for robust, identity-based crawling and simpler interactions with complex sites. Use **Magic Mode** for quick tasks or prototypes where persistent data is unnecessary.

With these approaches, you preserve your **authentic** browsing environment, ensuring the site sees you exactly as a normal user—no repeated logins or wasted time.

* * *

---

# Proxy & Security - Crawl4AI Documentation (v0.5.x)

Proxy
=====

Basic Proxy Setup
-----------------

Simple proxy configuration with `BrowserConfig`:

`[](#__codelineno-0-1) from crawl4ai.async_configs import BrowserConfig [](#__codelineno-0-2) [](#__codelineno-0-3) # Using proxy URL [](#__codelineno-0-4) browser_config = BrowserConfig(proxy="http://proxy.example.com:8080") [](#__codelineno-0-5) async with AsyncWebCrawler(config=browser_config) as crawler: [](#__codelineno-0-6)     result = await crawler.arun(url="https://example.com") [](#__codelineno-0-7) [](#__codelineno-0-8) # Using SOCKS proxy [](#__codelineno-0-9) browser_config = BrowserConfig(proxy="socks5://proxy.example.com:1080") [](#__codelineno-0-10) async with AsyncWebCrawler(config=browser_config) as crawler: [](#__codelineno-0-11)     result = await crawler.arun(url="https://example.com")`

Authenticated Proxy
-------------------

Use an authenticated proxy with `BrowserConfig`:

`[](#__codelineno-1-1) from crawl4ai.async_configs import BrowserConfig [](#__codelineno-1-2) [](#__codelineno-1-3) proxy_config = { [](#__codelineno-1-4)     "server": "http://proxy.example.com:8080", [](#__codelineno-1-5)     "username": "user", [](#__codelineno-1-6)     "password": "pass" [](#__codelineno-1-7) } [](#__codelineno-1-8) [](#__codelineno-1-9) browser_config = BrowserConfig(proxy_config=proxy_config) [](#__codelineno-1-10) async with AsyncWebCrawler(config=browser_config) as crawler: [](#__codelineno-1-11)     result = await crawler.arun(url="https://example.com")`

Here's the corrected documentation:

Rotating Proxies
----------------

Example using a proxy rotation service dynamically:

`[](#__codelineno-2-1) from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig [](#__codelineno-2-2) [](#__codelineno-2-3) async def get_next_proxy(): [](#__codelineno-2-4)     # Your proxy rotation logic here [](#__codelineno-2-5)     return {"server": "http://next.proxy.com:8080"} [](#__codelineno-2-6) [](#__codelineno-2-7) async def main(): [](#__codelineno-2-8)     browser_config = BrowserConfig() [](#__codelineno-2-9)     run_config = CrawlerRunConfig() [](#__codelineno-2-10) [](#__codelineno-2-11)     async with AsyncWebCrawler(config=browser_config) as crawler: [](#__codelineno-2-12)         # For each URL, create a new run config with different proxy [](#__codelineno-2-13)         for url in urls: [](#__codelineno-2-14)             proxy = await get_next_proxy() [](#__codelineno-2-15)             # Clone the config and update proxy - this creates a new browser context [](#__codelineno-2-16)             current_config = run_config.clone(proxy_config=proxy) [](#__codelineno-2-17)             result = await crawler.arun(url=url, config=current_config) [](#__codelineno-2-18) [](#__codelineno-2-19) if __name__ == "__main__": [](#__codelineno-2-20)     import asyncio [](#__codelineno-2-21)     asyncio.run(main())`

* * *

---

# Release Summary for Version 0.4.0 (December 1, 2024) - Crawl4AI Documentation (v0.5.x)

Release Summary for Version 0.4.0 (December 1, 2024)
====================================================

Overview
--------

The 0.4.0 release introduces significant improvements to content filtering, multi-threaded environment handling, user-agent generation, and test coverage. Key highlights include the introduction of the PruningContentFilter, designed to automatically identify and extract the most valuable parts of an HTML document, as well as enhancements to the BM25ContentFilter to extend its versatility and effectiveness.

Major Features and Enhancements
-------------------------------

### 1\. PruningContentFilter

*   Introduced a new unsupervised content filtering strategy that scores and prunes less relevant nodes in an HTML document based on metrics like text and link density.
*   Focuses on retaining the most valuable parts of the content, making it highly effective for extracting relevant information from complex web pages.
*   Fully documented with updated README and expanded user guides.

### 2\. User-Agent Generator

*   Added a user-agent generator utility that resolves compatibility issues and supports customizable user-agent strings.
*   By default, the generator randomizes user agents for each request, adding diversity, but users can customize it for tailored scenarios.

### 3\. Enhanced Thread Safety

*   Improved handling of multi-threaded environments by adding better thread locks for parallel processing, ensuring consistency and stability when running multiple threads.

### 4\. Extended Content Filtering Strategies

*   Users now have access to both the PruningContentFilter for unsupervised extraction and the BM25ContentFilter for supervised filtering based on user queries.
*   Enhanced BM25ContentFilter with improved capabilities to process page titles, meta tags, and descriptions, allowing for more effective classification and clustering of text chunks.

### 5\. Documentation Updates

*   Updated examples and tutorials to promote the use of the PruningContentFilter alongside the BM25ContentFilter, providing clear instructions for selecting the appropriate filter for each use case.

### 6\. Unit Test Enhancements

*   Added unit tests for PruningContentFilter to ensure accuracy and reliability.
*   Enhanced BM25ContentFilter tests to cover additional edge cases and performance metrics, particularly for malformed HTML inputs.

Revised Change Logs for Version 0.4.0
-------------------------------------

### PruningContentFilter (Dec 01, 2024)

*   Introduced the PruningContentFilter to optimize content extraction by pruning less relevant HTML nodes.
*   **Affected Files:**
    *   **crawl4ai/content\_filter\_strategy.py**: Added a scoring-based pruning algorithm.
    *   **README.md**: Updated to include PruningContentFilter usage.
    *   **docs/md\_v2/basic/content\_filtering.md**: Expanded user documentation, detailing the use and benefits of PruningContentFilter.

### Unit Tests for PruningContentFilter (Dec 01, 2024)

*   Added comprehensive unit tests for PruningContentFilter to ensure correctness and efficiency.
*   **Affected Files:**
    *   **tests/async/test\_content\_filter\_prune.py**: Created tests covering different pruning scenarios to ensure stability and correctness.

### Enhanced BM25ContentFilter Tests (Dec 01, 2024)

*   Expanded tests to cover additional extraction scenarios and performance metrics, improving robustness.
*   **Affected Files:**
    *   **tests/async/test\_content\_filter\_bm25.py**: Added tests for edge cases, including malformed HTML inputs.

### Documentation and Example Updates (Dec 01, 2024)

*   Revised examples to illustrate the use of PruningContentFilter alongside existing content filtering methods.
*   **Affected Files:**
    *   **docs/examples/quickstart\_async.py**: Enhanced example clarity and usability for new users.

Experimental Features
---------------------

*   The PruningContentFilter is still under experimental development, and we continue to gather feedback for further refinements.

Conclusion
----------

This release significantly enhances the content extraction capabilities of Crawl4ai with the introduction of the PruningContentFilter, improved supervised filtering with BM25ContentFilter, and robust multi-threaded handling. Additionally, the user-agent generator provides much-needed versatility, resolving compatibility issues faced by many users.

Users are encouraged to experiment with the new content filtering methods to determine which best suits their needs.

* * *

---

# Lazy Loading - Crawl4AI Documentation (v0.5.x)

Handling Lazy-Loaded Images
---------------------------

Many websites now load images **lazily** as you scroll. If you need to ensure they appear in your final crawl (and in `result.media`), consider:

1. **`wait_for_images=True`** – Wait for images to fully load.  
2. **`scan_full_page`** – Force the crawler to scroll the entire page, triggering lazy loads.  
3. **`scroll_delay`** – Add small delays between scroll steps.

**Note**: If the site requires multiple “Load More” triggers or complex interactions, see the [Page Interaction docs](../../core/page-interaction/)
.

### Example: Ensuring Lazy Images Appear

`[](#__codelineno-0-1) import asyncio [](#__codelineno-0-2) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, BrowserConfig [](#__codelineno-0-3) from crawl4ai.async_configs import CacheMode [](#__codelineno-0-4) [](#__codelineno-0-5) async def main(): [](#__codelineno-0-6)     config = CrawlerRunConfig( [](#__codelineno-0-7)         # Force the crawler to wait until images are fully loaded [](#__codelineno-0-8)         wait_for_images=True, [](#__codelineno-0-9) [](#__codelineno-0-10)         # Option 1: If you want to automatically scroll the page to load images [](#__codelineno-0-11)         scan_full_page=True,  # Tells the crawler to try scrolling the entire page [](#__codelineno-0-12)         scroll_delay=0.5,     # Delay (seconds) between scroll steps [](#__codelineno-0-13) [](#__codelineno-0-14)         # Option 2: If the site uses a 'Load More' or JS triggers for images, [](#__codelineno-0-15)         # you can also specify js_code or wait_for logic here. [](#__codelineno-0-16) [](#__codelineno-0-17)         cache_mode=CacheMode.BYPASS, [](#__codelineno-0-18)         verbose=True [](#__codelineno-0-19)     ) [](#__codelineno-0-20) [](#__codelineno-0-21)     async with AsyncWebCrawler(config=BrowserConfig(headless=True)) as crawler: [](#__codelineno-0-22)         result = await crawler.arun("https://www.example.com/gallery", config=config) [](#__codelineno-0-23) [](#__codelineno-0-24)         if result.success: [](#__codelineno-0-25)             images = result.media.get("images", []) [](#__codelineno-0-26)             print("Images found:", len(images)) [](#__codelineno-0-27)             for i, img in enumerate(images[:5]): [](#__codelineno-0-28)                 print(f"[Image {i}] URL: {img['src']}, Score: {img.get('score','N/A')}") [](#__codelineno-0-29)         else: [](#__codelineno-0-30)             print("Error:", result.error_message) [](#__codelineno-0-31) [](#__codelineno-0-32) if __name__ == "__main__": [](#__codelineno-0-33)     asyncio.run(main())`

**Explanation**:

*   **`wait_for_images=True`**  
    The crawler tries to ensure images have finished loading before finalizing the HTML.
*   **`scan_full_page=True`**  
    Tells the crawler to attempt scrolling from top to bottom. Each scroll step helps trigger lazy loading.
*   **`scroll_delay=0.5`**  
    Pause half a second between each scroll step. Helps the site load images before continuing.

**When to Use**:

*   **Lazy-Loading**: If images appear only when the user scrolls into view, `scan_full_page` + `scroll_delay` helps the crawler see them.
*   **Heavier Pages**: If a page is extremely long, be mindful that scanning the entire page can be slow. Adjust `scroll_delay` or the max scroll steps as needed.

* * *

Combining with Other Link & Media Filters
-----------------------------------------

You can still combine **lazy-load** logic with the usual **exclude\_external\_images**, **exclude\_domains**, or link filtration:

`[](#__codelineno-1-1) config = CrawlerRunConfig( [](#__codelineno-1-2)     wait_for_images=True, [](#__codelineno-1-3)     scan_full_page=True, [](#__codelineno-1-4)     scroll_delay=0.5, [](#__codelineno-1-5) [](#__codelineno-1-6)     # Filter out external images if you only want local ones [](#__codelineno-1-7)     exclude_external_images=True, [](#__codelineno-1-8) [](#__codelineno-1-9)     # Exclude certain domains for links [](#__codelineno-1-10)     exclude_domains=["spammycdn.com"], [](#__codelineno-1-11) )`

This approach ensures you see **all** images from the main domain while ignoring external ones, and the crawler physically scrolls the entire page so that lazy-loading triggers.

* * *

Tips & Troubleshooting
----------------------

1. **Long Pages**  
\- Setting `scan_full_page=True` on extremely long or infinite-scroll pages can be resource-intensive.  
\- Consider using [hooks](../../core/page-interaction/)
 or specialized logic to load specific sections or “Load More” triggers repeatedly.

2. **Mixed Image Behavior**  
\- Some sites load images in batches as you scroll. If you’re missing images, increase your `scroll_delay` or call multiple partial scrolls in a loop with JS code or hooks.

3. **Combining with Dynamic Wait**  
\- If the site has a placeholder that only changes to a real image after a certain event, you might do `wait_for="css:img.loaded"` or a custom JS `wait_for`.

4. **Caching**  
\- If `cache_mode` is enabled, repeated crawls might skip some network fetches. If you suspect caching is missing new images, set `cache_mode=CacheMode.BYPASS` for fresh fetches.

* * *

With **lazy-loading** support, **wait\_for\_images**, and **scan\_full\_page** settings, you can capture the entire gallery or feed of images you expect—even if the site only loads them as the user scrolls. Combine these with the standard media filtering and domain exclusion for a complete link & media handling strategy.

* * *

---

# SSL Certificate - Crawl4AI Documentation (v0.5.x)

`SSLCertificate` Reference
==========================

The **`SSLCertificate`** class encapsulates an SSL certificate’s data and allows exporting it in various formats (PEM, DER, JSON, or text). It’s used within **Crawl4AI** whenever you set **`fetch_ssl_certificate=True`** in your **`CrawlerRunConfig`**.

1\. Overview
------------

**Location**: `crawl4ai/ssl_certificate.py`

`[](#__codelineno-0-1) class SSLCertificate: [](#__codelineno-0-2)     """ [](#__codelineno-0-3)     Represents an SSL certificate with methods to export in various formats. [](#__codelineno-0-4) [](#__codelineno-0-5)     Main Methods: [](#__codelineno-0-6)     - from_url(url, timeout=10) [](#__codelineno-0-7)     - from_file(file_path) [](#__codelineno-0-8)     - from_binary(binary_data) [](#__codelineno-0-9)     - to_json(filepath=None) [](#__codelineno-0-10)     - to_pem(filepath=None) [](#__codelineno-0-11)     - to_der(filepath=None) [](#__codelineno-0-12)     ... [](#__codelineno-0-13) [](#__codelineno-0-14)     Common Properties: [](#__codelineno-0-15)     - issuer [](#__codelineno-0-16)     - subject [](#__codelineno-0-17)     - valid_from [](#__codelineno-0-18)     - valid_until [](#__codelineno-0-19)     - fingerprint [](#__codelineno-0-20)     """`

### Typical Use Case

1.  You **enable** certificate fetching in your crawl by:
    
    `[](#__codelineno-1-1) CrawlerRunConfig(fetch_ssl_certificate=True, ...)`
    
2.  After `arun()`, if `result.ssl_certificate` is present, it’s an instance of **`SSLCertificate`**.
3.  You can **read** basic properties (issuer, subject, validity) or **export** them in multiple formats.

* * *

2\. Construction & Fetching
---------------------------

### 2.1 **`from_url(url, timeout=10)`**

Manually load an SSL certificate from a given URL (port 443). Typically used internally, but you can call it directly if you want:

`[](#__codelineno-2-1) cert = SSLCertificate.from_url("https://example.com") [](#__codelineno-2-2) if cert: [](#__codelineno-2-3)     print("Fingerprint:", cert.fingerprint)`

### 2.2 **`from_file(file_path)`**

Load from a file containing certificate data in ASN.1 or DER. Rarely needed unless you have local cert files:

`[](#__codelineno-3-1) cert = SSLCertificate.from_file("/path/to/cert.der")`

### 2.3 **`from_binary(binary_data)`**

Initialize from raw binary. E.g., if you captured it from a socket or another source:

`[](#__codelineno-4-1) cert = SSLCertificate.from_binary(raw_bytes)`

* * *

3\. Common Properties
---------------------

After obtaining a **`SSLCertificate`** instance (e.g. `result.ssl_certificate` from a crawl), you can read:

1. **`issuer`** _(dict)_  
\- E.g. `{"CN": "My Root CA", "O": "..."}` 2. **`subject`** _(dict)_  
\- E.g. `{"CN": "example.com", "O": "ExampleOrg"}` 3. **`valid_from`** _(str)_  
\- NotBefore date/time. Often in ASN.1/UTC format. 4. **`valid_until`** _(str)_  
\- NotAfter date/time. 5. **`fingerprint`** _(str)_  
\- The SHA-256 digest (lowercase hex).  
\- E.g. `"d14d2e..."`

* * *

4\. Export Methods
------------------

Once you have a **`SSLCertificate`** object, you can **export** or **inspect** it:

### 4.1 **`to_json(filepath=None)` → `Optional[str]`**

*   Returns a JSON string containing the parsed certificate fields.
*   If `filepath` is provided, saves it to disk instead, returning `None`.

**Usage**:

`[](#__codelineno-5-1) json_data = cert.to_json()  # returns JSON string [](#__codelineno-5-2) cert.to_json("certificate.json")  # writes file, returns None`

### 4.2 **`to_pem(filepath=None)` → `Optional[str]`**

*   Returns a PEM-encoded string (common for web servers).
*   If `filepath` is provided, saves it to disk instead.

`[](#__codelineno-6-1) pem_str = cert.to_pem()              # in-memory PEM string [](#__codelineno-6-2) cert.to_pem("/path/to/cert.pem")     # saved to file`

### 4.3 **`to_der(filepath=None)` → `Optional[bytes]`**

*   Returns the original DER (binary ASN.1) bytes.
*   If `filepath` is specified, writes the bytes there instead.

`[](#__codelineno-7-1) der_bytes = cert.to_der() [](#__codelineno-7-2) cert.to_der("certificate.der")`

### 4.4 (Optional) **`export_as_text()`**

*   If you see a method like `export_as_text()`, it typically returns an OpenSSL-style textual representation.
*   Not always needed, but can help for debugging or manual inspection.

* * *

5\. Example Usage in Crawl4AI
-----------------------------

Below is a minimal sample showing how the crawler obtains an SSL cert from a site, then reads or exports it. The code snippet:

`[](#__codelineno-8-1) import asyncio [](#__codelineno-8-2) import os [](#__codelineno-8-3) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode [](#__codelineno-8-4) [](#__codelineno-8-5) async def main(): [](#__codelineno-8-6)     tmp_dir = "tmp" [](#__codelineno-8-7)     os.makedirs(tmp_dir, exist_ok=True) [](#__codelineno-8-8) [](#__codelineno-8-9)     config = CrawlerRunConfig( [](#__codelineno-8-10)         fetch_ssl_certificate=True, [](#__codelineno-8-11)         cache_mode=CacheMode.BYPASS [](#__codelineno-8-12)     ) [](#__codelineno-8-13) [](#__codelineno-8-14)     async with AsyncWebCrawler() as crawler: [](#__codelineno-8-15)         result = await crawler.arun("https://example.com", config=config) [](#__codelineno-8-16)         if result.success and result.ssl_certificate: [](#__codelineno-8-17)             cert = result.ssl_certificate [](#__codelineno-8-18)             # 1. Basic Info [](#__codelineno-8-19)             print("Issuer CN:", cert.issuer.get("CN", "")) [](#__codelineno-8-20)             print("Valid until:", cert.valid_until) [](#__codelineno-8-21)             print("Fingerprint:", cert.fingerprint) [](#__codelineno-8-22) [](#__codelineno-8-23)             # 2. Export [](#__codelineno-8-24)             cert.to_json(os.path.join(tmp_dir, "certificate.json")) [](#__codelineno-8-25)             cert.to_pem(os.path.join(tmp_dir, "certificate.pem")) [](#__codelineno-8-26)             cert.to_der(os.path.join(tmp_dir, "certificate.der")) [](#__codelineno-8-27) [](#__codelineno-8-28) if __name__ == "__main__": [](#__codelineno-8-29)     asyncio.run(main())`

* * *

6\. Notes & Best Practices
--------------------------

1. **Timeout**: `SSLCertificate.from_url` internally uses a default **10s** socket connect and wraps SSL.  
2. **Binary Form**: The certificate is loaded in ASN.1 (DER) form, then re-parsed by `OpenSSL.crypto`.  
3. **Validation**: This does **not** validate the certificate chain or trust store. It only fetches and parses.  
4. **Integration**: Within Crawl4AI, you typically just set `fetch_ssl_certificate=True` in `CrawlerRunConfig`; the final result’s `ssl_certificate` is automatically built.  
5. **Export**: If you need to store or analyze a cert, the `to_json` and `to_pem` are quite universal.

* * *

### Summary

*   **`SSLCertificate`** is a convenience class for capturing and exporting the **TLS certificate** from your crawled site(s).
*   Common usage is in the **`CrawlResult.ssl_certificate`** field, accessible after setting `fetch_ssl_certificate=True`.
*   Offers quick access to essential certificate details (`issuer`, `subject`, `fingerprint`) and is easy to export (PEM, DER, JSON) for further analysis or server usage.

Use it whenever you need **insight** into a site’s certificate or require some form of cryptographic or compliance check.

* * *

---

# arun_many() - Crawl4AI Documentation (v0.5.x)

`arun_many(...)` Reference
==========================

> **Note**: This function is very similar to [`arun()`](../arun/)
>  but focused on **concurrent** or **batch** crawling. If you’re unfamiliar with `arun()` usage, please read that doc first, then review this for differences.

Function Signature
------------------

``[](#__codelineno-0-1) async def arun_many( [](#__codelineno-0-2)     urls: Union[List[str], List[Any]], [](#__codelineno-0-3)     config: Optional[CrawlerRunConfig] = None, [](#__codelineno-0-4)     dispatcher: Optional[BaseDispatcher] = None, [](#__codelineno-0-5)     ... [](#__codelineno-0-6) ) -> Union[List[CrawlResult], AsyncGenerator[CrawlResult, None]]: [](#__codelineno-0-7)     """ [](#__codelineno-0-8)     Crawl multiple URLs concurrently or in batches. [](#__codelineno-0-9) [](#__codelineno-0-10)     :param urls: A list of URLs (or tasks) to crawl. [](#__codelineno-0-11)     :param config: (Optional) A default `CrawlerRunConfig` applying to each crawl. [](#__codelineno-0-12)     :param dispatcher: (Optional) A concurrency controller (e.g. MemoryAdaptiveDispatcher). [](#__codelineno-0-13)     ... [](#__codelineno-0-14)     :return: Either a list of `CrawlResult` objects, or an async generator if streaming is enabled. [](#__codelineno-0-15)     """``

Differences from `arun()`
-------------------------

1. **Multiple URLs**:

*   Instead of crawling a single URL, you pass a list of them (strings or tasks). 
*   The function returns either a **list** of `CrawlResult` or an **async generator** if streaming is enabled.

2. **Concurrency & Dispatchers**:

*   **`dispatcher`** param allows advanced concurrency control. 
*   If omitted, a default dispatcher (like `MemoryAdaptiveDispatcher`) is used internally. 
*   Dispatchers handle concurrency, rate limiting, and memory-based adaptive throttling (see [Multi-URL Crawling](../../advanced/multi-url-crawling/)
    ).

3. **Streaming Support**:

*   Enable streaming by setting `stream=True` in your `CrawlerRunConfig`.
*   When streaming, use `async for` to process results as they become available.
*   Ideal for processing large numbers of URLs without waiting for all to complete.

4. **Parallel** Execution\*\*:

*   `arun_many()` can run multiple requests concurrently under the hood. 
*   Each `CrawlResult` might also include a **`dispatch_result`** with concurrency details (like memory usage, start/end times).

### Basic Example (Batch Mode)

`[](#__codelineno-1-1) # Minimal usage: The default dispatcher will be used [](#__codelineno-1-2) results = await crawler.arun_many( [](#__codelineno-1-3)     urls=["https://site1.com", "https://site2.com"], [](#__codelineno-1-4)     config=CrawlerRunConfig(stream=False)  # Default behavior [](#__codelineno-1-5) ) [](#__codelineno-1-6) [](#__codelineno-1-7) for res in results: [](#__codelineno-1-8)     if res.success: [](#__codelineno-1-9)         print(res.url, "crawled OK!") [](#__codelineno-1-10)     else: [](#__codelineno-1-11)         print("Failed:", res.url, "-", res.error_message)`

### Streaming Example

`[](#__codelineno-2-1) config = CrawlerRunConfig( [](#__codelineno-2-2)     stream=True,  # Enable streaming mode [](#__codelineno-2-3)     cache_mode=CacheMode.BYPASS [](#__codelineno-2-4) ) [](#__codelineno-2-5) [](#__codelineno-2-6) # Process results as they complete [](#__codelineno-2-7) async for result in await crawler.arun_many( [](#__codelineno-2-8)     urls=["https://site1.com", "https://site2.com", "https://site3.com"], [](#__codelineno-2-9)     config=config [](#__codelineno-2-10) ): [](#__codelineno-2-11)     if result.success: [](#__codelineno-2-12)         print(f"Just completed: {result.url}") [](#__codelineno-2-13)         # Process each result immediately [](#__codelineno-2-14)         process_result(result)`

### With a Custom Dispatcher

`[](#__codelineno-3-1) dispatcher = MemoryAdaptiveDispatcher( [](#__codelineno-3-2)     memory_threshold_percent=70.0, [](#__codelineno-3-3)     max_session_permit=10 [](#__codelineno-3-4) ) [](#__codelineno-3-5) results = await crawler.arun_many( [](#__codelineno-3-6)     urls=["https://site1.com", "https://site2.com", "https://site3.com"], [](#__codelineno-3-7)     config=my_run_config, [](#__codelineno-3-8)     dispatcher=dispatcher [](#__codelineno-3-9) )`

**Key Points**: - Each URL is processed by the same or separate sessions, depending on the dispatcher’s strategy. - `dispatch_result` in each `CrawlResult` (if using concurrency) can hold memory and timing info.  - If you need to handle authentication or session IDs, pass them in each individual task or within your run config.

### Return Value

Either a **list** of [`CrawlResult`](../crawl-result/)
 objects, or an **async generator** if streaming is enabled. You can iterate to check `result.success` or read each item’s `extracted_content`, `markdown`, or `dispatch_result`.

* * *

Dispatcher Reference
--------------------

*   **`MemoryAdaptiveDispatcher`**: Dynamically manages concurrency based on system memory usage. 
*   **`SemaphoreDispatcher`**: Fixed concurrency limit, simpler but less adaptive. 

For advanced usage or custom settings, see [Multi-URL Crawling with Dispatchers](../../advanced/multi-url-crawling/)
.

* * *

Common Pitfalls
---------------

1. **Large Lists**: If you pass thousands of URLs, be mindful of memory or rate-limits. A dispatcher can help. 

2. **Session Reuse**: If you need specialized logins or persistent contexts, ensure your dispatcher or tasks handle sessions accordingly. 

3. **Error Handling**: Each `CrawlResult` might fail for different reasons—always check `result.success` or the `error_message` before proceeding.

* * *

Conclusion
----------

Use `arun_many()` when you want to **crawl multiple URLs** simultaneously or in controlled parallel tasks. If you need advanced concurrency features (like memory-based adaptive throttling or complex rate-limiting), provide a **dispatcher**. Each result is a standard `CrawlResult`, possibly augmented with concurrency stats (`dispatch_result`) for deeper inspection. For more details on concurrency logic and dispatchers, see the [Advanced Multi-URL Crawling](../../advanced/multi-url-crawling/)
 docs.

* * *

---

# Strategies - Crawl4AI Documentation (v0.5.x)

Extraction & Chunking Strategies API
====================================

This documentation covers the API reference for extraction and chunking strategies in Crawl4AI.

Extraction Strategies
---------------------

All extraction strategies inherit from the base `ExtractionStrategy` class and implement two key methods: - `extract(url: str, html: str) -> List[Dict[str, Any]]` - `run(url: str, sections: List[str]) -> List[Dict[str, Any]]`

### LLMExtractionStrategy

Used for extracting structured data using Language Models.

`[](#__codelineno-0-1) LLMExtractionStrategy( [](#__codelineno-0-2)     # Required Parameters [](#__codelineno-0-3)     provider: str = DEFAULT_PROVIDER,     # LLM provider (e.g., "ollama/llama2") [](#__codelineno-0-4)     api_token: Optional[str] = None,      # API token [](#__codelineno-0-5) [](#__codelineno-0-6)     # Extraction Configuration [](#__codelineno-0-7)     instruction: str = None,              # Custom extraction instruction [](#__codelineno-0-8)     schema: Dict = None,                  # Pydantic model schema for structured data [](#__codelineno-0-9)     extraction_type: str = "block",       # "block" or "schema" [](#__codelineno-0-10) [](#__codelineno-0-11)     # Chunking Parameters [](#__codelineno-0-12)     chunk_token_threshold: int = 4000,    # Maximum tokens per chunk [](#__codelineno-0-13)     overlap_rate: float = 0.1,           # Overlap between chunks [](#__codelineno-0-14)     word_token_rate: float = 0.75,       # Word to token conversion rate [](#__codelineno-0-15)     apply_chunking: bool = True,         # Enable/disable chunking [](#__codelineno-0-16) [](#__codelineno-0-17)     # API Configuration [](#__codelineno-0-18)     base_url: str = None,                # Base URL for API [](#__codelineno-0-19)     extra_args: Dict = {},               # Additional provider arguments [](#__codelineno-0-20)     verbose: bool = False                # Enable verbose logging [](#__codelineno-0-21) )`

### CosineStrategy

Used for content similarity-based extraction and clustering.

`[](#__codelineno-1-1) CosineStrategy( [](#__codelineno-1-2)     # Content Filtering [](#__codelineno-1-3)     semantic_filter: str = None,        # Topic/keyword filter [](#__codelineno-1-4)     word_count_threshold: int = 10,     # Minimum words per cluster [](#__codelineno-1-5)     sim_threshold: float = 0.3,         # Similarity threshold [](#__codelineno-1-6) [](#__codelineno-1-7)     # Clustering Parameters [](#__codelineno-1-8)     max_dist: float = 0.2,             # Maximum cluster distance [](#__codelineno-1-9)     linkage_method: str = 'ward',       # Clustering method [](#__codelineno-1-10)     top_k: int = 3,                    # Top clusters to return [](#__codelineno-1-11) [](#__codelineno-1-12)     # Model Configuration [](#__codelineno-1-13)     model_name: str = 'sentence-transformers/all-MiniLM-L6-v2',  # Embedding model [](#__codelineno-1-14) [](#__codelineno-1-15)     verbose: bool = False              # Enable verbose logging [](#__codelineno-1-16) )`

### JsonCssExtractionStrategy

Used for CSS selector-based structured data extraction.

`[](#__codelineno-2-1) JsonCssExtractionStrategy( [](#__codelineno-2-2)     schema: Dict[str, Any],    # Extraction schema [](#__codelineno-2-3)     verbose: bool = False      # Enable verbose logging [](#__codelineno-2-4) ) [](#__codelineno-2-5) [](#__codelineno-2-6) # Schema Structure [](#__codelineno-2-7) schema = { [](#__codelineno-2-8)     "name": str,              # Schema name [](#__codelineno-2-9)     "baseSelector": str,      # Base CSS selector [](#__codelineno-2-10)     "fields": [               # List of fields to extract [](#__codelineno-2-11)         { [](#__codelineno-2-12)             "name": str,      # Field name [](#__codelineno-2-13)             "selector": str,  # CSS selector [](#__codelineno-2-14)             "type": str,     # Field type: "text", "attribute", "html", "regex" [](#__codelineno-2-15)             "attribute": str, # For type="attribute" [](#__codelineno-2-16)             "pattern": str,  # For type="regex" [](#__codelineno-2-17)             "transform": str, # Optional: "lowercase", "uppercase", "strip" [](#__codelineno-2-18)             "default": Any    # Default value if extraction fails [](#__codelineno-2-19)         } [](#__codelineno-2-20)     ] [](#__codelineno-2-21) }`

Chunking Strategies
-------------------

All chunking strategies inherit from `ChunkingStrategy` and implement the `chunk(text: str) -> list` method.

### RegexChunking

Splits text based on regex patterns.

`[](#__codelineno-3-1) RegexChunking( [](#__codelineno-3-2)     patterns: List[str] = None  # Regex patterns for splitting [](#__codelineno-3-3)                                # Default: [r'\n\n'] [](#__codelineno-3-4) )`

### SlidingWindowChunking

Creates overlapping chunks with a sliding window approach.

`[](#__codelineno-4-1) SlidingWindowChunking( [](#__codelineno-4-2)     window_size: int = 100,    # Window size in words [](#__codelineno-4-3)     step: int = 50             # Step size between windows [](#__codelineno-4-4) )`

### OverlappingWindowChunking

Creates chunks with specified overlap.

`[](#__codelineno-5-1) OverlappingWindowChunking( [](#__codelineno-5-2)     window_size: int = 1000,   # Chunk size in words [](#__codelineno-5-3)     overlap: int = 100         # Overlap size in words [](#__codelineno-5-4) )`

Usage Examples
--------------

### LLM Extraction

`[](#__codelineno-6-1) from pydantic import BaseModel [](#__codelineno-6-2) from crawl4ai.extraction_strategy import LLMExtractionStrategy [](#__codelineno-6-3) from crawl4ai import LLMConfig [](#__codelineno-6-4) [](#__codelineno-6-5) # Define schema [](#__codelineno-6-6) class Article(BaseModel): [](#__codelineno-6-7)     title: str [](#__codelineno-6-8)     content: str [](#__codelineno-6-9)     author: str [](#__codelineno-6-10) [](#__codelineno-6-11) # Create strategy [](#__codelineno-6-12) strategy = LLMExtractionStrategy( [](#__codelineno-6-13)     llm_config = LLMConfig(provider="ollama/llama2"), [](#__codelineno-6-14)     schema=Article.schema(), [](#__codelineno-6-15)     instruction="Extract article details" [](#__codelineno-6-16) ) [](#__codelineno-6-17) [](#__codelineno-6-18) # Use with crawler [](#__codelineno-6-19) result = await crawler.arun( [](#__codelineno-6-20)     url="https://example.com/article", [](#__codelineno-6-21)     extraction_strategy=strategy [](#__codelineno-6-22) ) [](#__codelineno-6-23) [](#__codelineno-6-24) # Access extracted data [](#__codelineno-6-25) data = json.loads(result.extracted_content)`

### CSS Extraction

`[](#__codelineno-7-1) from crawl4ai.extraction_strategy import JsonCssExtractionStrategy [](#__codelineno-7-2) [](#__codelineno-7-3) # Define schema [](#__codelineno-7-4) schema = { [](#__codelineno-7-5)     "name": "Product List", [](#__codelineno-7-6)     "baseSelector": ".product-card", [](#__codelineno-7-7)     "fields": [ [](#__codelineno-7-8)         { [](#__codelineno-7-9)             "name": "title", [](#__codelineno-7-10)             "selector": "h2.title", [](#__codelineno-7-11)             "type": "text" [](#__codelineno-7-12)         }, [](#__codelineno-7-13)         { [](#__codelineno-7-14)             "name": "price", [](#__codelineno-7-15)             "selector": ".price", [](#__codelineno-7-16)             "type": "text", [](#__codelineno-7-17)             "transform": "strip" [](#__codelineno-7-18)         }, [](#__codelineno-7-19)         { [](#__codelineno-7-20)             "name": "image", [](#__codelineno-7-21)             "selector": "img", [](#__codelineno-7-22)             "type": "attribute", [](#__codelineno-7-23)             "attribute": "src" [](#__codelineno-7-24)         } [](#__codelineno-7-25)     ] [](#__codelineno-7-26) } [](#__codelineno-7-27) [](#__codelineno-7-28) # Create and use strategy [](#__codelineno-7-29) strategy = JsonCssExtractionStrategy(schema) [](#__codelineno-7-30) result = await crawler.arun( [](#__codelineno-7-31)     url="https://example.com/products", [](#__codelineno-7-32)     extraction_strategy=strategy [](#__codelineno-7-33) )`

### Content Chunking

`[](#__codelineno-8-1) from crawl4ai.chunking_strategy import OverlappingWindowChunking [](#__codelineno-8-2) from crawl4ai import LLMConfig [](#__codelineno-8-3) [](#__codelineno-8-4) # Create chunking strategy [](#__codelineno-8-5) chunker = OverlappingWindowChunking( [](#__codelineno-8-6)     window_size=500,  # 500 words per chunk [](#__codelineno-8-7)     overlap=50        # 50 words overlap [](#__codelineno-8-8) ) [](#__codelineno-8-9) [](#__codelineno-8-10) # Use with extraction strategy [](#__codelineno-8-11) strategy = LLMExtractionStrategy( [](#__codelineno-8-12)     llm_config = LLMConfig(provider="ollama/llama2"), [](#__codelineno-8-13)     chunking_strategy=chunker [](#__codelineno-8-14) ) [](#__codelineno-8-15) [](#__codelineno-8-16) result = await crawler.arun( [](#__codelineno-8-17)     url="https://example.com/long-article", [](#__codelineno-8-18)     extraction_strategy=strategy [](#__codelineno-8-19) )`

Best Practices
--------------

1. **Choose the Right Strategy** - Use `LLMExtractionStrategy` for complex, unstructured content - Use `JsonCssExtractionStrategy` for well-structured HTML - Use `CosineStrategy` for content similarity and clustering

2. **Optimize Chunking**

`[](#__codelineno-9-1) # For long documents [](#__codelineno-9-2) strategy = LLMExtractionStrategy( [](#__codelineno-9-3)     chunk_token_threshold=2000,  # Smaller chunks [](#__codelineno-9-4)     overlap_rate=0.1           # 10% overlap [](#__codelineno-9-5) )`

3. **Handle Errors**

`[](#__codelineno-10-1) try: [](#__codelineno-10-2)     result = await crawler.arun( [](#__codelineno-10-3)         url="https://example.com", [](#__codelineno-10-4)         extraction_strategy=strategy [](#__codelineno-10-5)     ) [](#__codelineno-10-6)     if result.success: [](#__codelineno-10-7)         content = json.loads(result.extracted_content) [](#__codelineno-10-8) except Exception as e: [](#__codelineno-10-9)     print(f"Extraction failed: {e}")`

4. **Monitor Performance**

`[](#__codelineno-11-1) strategy = CosineStrategy( [](#__codelineno-11-2)     verbose=True,  # Enable logging [](#__codelineno-11-3)     word_count_threshold=20,  # Filter short content [](#__codelineno-11-4)     top_k=5  # Limit results [](#__codelineno-11-5) )`

* * *

---

# Dockerize hooks - Crawl4AI Documentation (v0.5.x)

Introducing Event Streams and Interactive Hooks in Crawl4AI
-----------------------------------------------------------

![event-driven-crawl](https://res.cloudinary.com/kidocode/image/upload/t_400x400/v1734344008/15bb8bbb-83ac-43ac-962d-3feb3e0c3bbf_2_tjmr4n.webp)

In the near future, I’m planning to enhance Crawl4AI’s capabilities by introducing an event stream mechanism that will give clients deeper, real-time insights into the crawling process. Today, hooks are a powerful feature at the code level—they let developers define custom logic at key points in the crawl. However, when using Crawl4AI as a service (e.g., through a Dockerized API), there isn’t an easy way to interact with these hooks at runtime.

**What’s Changing?**

I’m working on a solution that will allow the crawler to emit a continuous stream of events, updating clients on the current crawling stage, encountered pages, and any decision points. This event stream could be exposed over a standardized protocol like Server-Sent Events (SSE) or WebSockets, enabling clients to “subscribe” and listen as the crawler works.

**Interactivity Through Process IDs**

A key part of this new design is the concept of a unique process ID for each crawl session. Imagine you’re listening to an event stream that informs you: - The crawler just hit a certain page  
\- It triggered a hook and is now pausing for instructions

With the event stream in place, you can send a follow-up request back to the server—referencing the unique process ID—to provide extra data, instructions, or parameters. This might include selecting which links to follow next, adjusting extraction strategies, or providing authentication tokens for a protected API. Once the crawler receives these instructions, it resumes execution with the updated context.

`[](#__codelineno-0-1) sequenceDiagram [](#__codelineno-0-2)     participant Client [](#__codelineno-0-3)     participant Server [](#__codelineno-0-4)     participant Crawler [](#__codelineno-0-5) [](#__codelineno-0-6)     Client->>Server: Start crawl request [](#__codelineno-0-7)     Server->>Crawler: Initiate crawl with Process ID [](#__codelineno-0-8)     Crawler-->>Server: Event: Page hit [](#__codelineno-0-9)     Server-->>Client: Stream: Page hit event [](#__codelineno-0-10)     Client->>Server: Instruction for Process ID [](#__codelineno-0-11)     Server->>Crawler: Update crawl with new instructions [](#__codelineno-0-12)     Crawler-->>Server: Event: Crawl completed [](#__codelineno-0-13)     Server-->>Client: Stream: Crawl completed`

**Benefits for Developers and Users**

1. **Fine-Grained Control**: Instead of predefining all logic upfront, you can dynamically guide the crawler in response to actual data and conditions encountered mid-crawl. 2. **Real-Time Insights**: Monitor progress, errors, or network bottlenecks as they happen, without waiting for the entire crawl to finish. 3. **Enhanced Collaboration**: Different team members or automated systems can watch the same crawl events and provide input, making the crawling process more adaptive and intelligent.

**Next Steps**

I’m currently exploring the best APIs, technologies, and patterns to make this vision a reality. My goal is to deliver a seamless developer experience—one that integrates with existing Crawl4AI workflows while offering new flexibility and power.

Stay tuned for more updates as I continue building this feature out. In the meantime, I’d love to hear any feedback or suggestions you might have to help shape this interactive, event-driven future of web crawling with Crawl4AI.

* * *

---

# CrawlResult - Crawl4AI Documentation (v0.5.x)

`CrawlResult` Reference
=======================

The **`CrawlResult`** class encapsulates everything returned after a single crawl operation. It provides the **raw or processed content**, details on links and media, plus optional metadata (like screenshots, PDFs, or extracted JSON).

**Location**: `crawl4ai/crawler/models.py` (for reference)

`[](#__codelineno-0-1) class CrawlResult(BaseModel): [](#__codelineno-0-2)     url: str [](#__codelineno-0-3)     html: str [](#__codelineno-0-4)     success: bool [](#__codelineno-0-5)     cleaned_html: Optional[str] = None [](#__codelineno-0-6)     media: Dict[str, List[Dict]] = {} [](#__codelineno-0-7)     links: Dict[str, List[Dict]] = {} [](#__codelineno-0-8)     downloaded_files: Optional[List[str]] = None [](#__codelineno-0-9)     screenshot: Optional[str] = None [](#__codelineno-0-10)     pdf : Optional[bytes] = None [](#__codelineno-0-11)     markdown: Optional[Union[str, MarkdownGenerationResult]] = None [](#__codelineno-0-12)     extracted_content: Optional[str] = None [](#__codelineno-0-13)     metadata: Optional[dict] = None [](#__codelineno-0-14)     error_message: Optional[str] = None [](#__codelineno-0-15)     session_id: Optional[str] = None [](#__codelineno-0-16)     response_headers: Optional[dict] = None [](#__codelineno-0-17)     status_code: Optional[int] = None [](#__codelineno-0-18)     ssl_certificate: Optional[SSLCertificate] = None [](#__codelineno-0-19)     dispatch_result: Optional[DispatchResult] = None [](#__codelineno-0-20)     ...`

Below is a **field-by-field** explanation and possible usage patterns.

* * *

1\. Basic Crawl Info
--------------------

### 1.1 **`url`** _(str)_

**What**: The final crawled URL (after any redirects).  
**Usage**:

`[](#__codelineno-1-1) print(result.url)  # e.g., "https://example.com/"`

### 1.2 **`success`** _(bool)_

**What**: `True` if the crawl pipeline ended without major errors; `False` otherwise.  
**Usage**:

`[](#__codelineno-2-1) if not result.success: [](#__codelineno-2-2)     print(f"Crawl failed: {result.error_message}")`

### 1.3 **`status_code`** _(Optional\[int\])_

**What**: The page’s HTTP status code (e.g., 200, 404).  
**Usage**:

`[](#__codelineno-3-1) if result.status_code == 404: [](#__codelineno-3-2)     print("Page not found!")`

### 1.4 **`error_message`** _(Optional\[str\])_

**What**: If `success=False`, a textual description of the failure.  
**Usage**:

`[](#__codelineno-4-1) if not result.success: [](#__codelineno-4-2)     print("Error:", result.error_message)`

### 1.5 **`session_id`** _(Optional\[str\])_

**What**: The ID used for reusing a browser context across multiple calls.  
**Usage**:

`[](#__codelineno-5-1) # If you used session_id="login_session" in CrawlerRunConfig, see it here: [](#__codelineno-5-2) print("Session:", result.session_id)`

### 1.6 **`response_headers`** _(Optional\[dict\])_

**What**: Final HTTP response headers.  
**Usage**:

`[](#__codelineno-6-1) if result.response_headers: [](#__codelineno-6-2)     print("Server:", result.response_headers.get("Server", "Unknown"))`

### 1.7 **`ssl_certificate`** _(Optional\[SSLCertificate\])_

**What**: If `fetch_ssl_certificate=True` in your CrawlerRunConfig, **`result.ssl_certificate`** contains a [**`SSLCertificate`**](../../advanced/ssl-certificate/)
 object describing the site’s certificate. You can export the cert in multiple formats (PEM/DER/JSON) or access its properties like `issuer`, `subject`, `valid_from`, `valid_until`, etc. **Usage**:

`[](#__codelineno-7-1) if result.ssl_certificate: [](#__codelineno-7-2)     print("Issuer:", result.ssl_certificate.issuer)`

* * *

2\. Raw / Cleaned Content
-------------------------

### 2.1 **`html`** _(str)_

**What**: The **original** unmodified HTML from the final page load.  
**Usage**:

`[](#__codelineno-8-1) # Possibly large [](#__codelineno-8-2) print(len(result.html))`

### 2.2 **`cleaned_html`** _(Optional\[str\])_

**What**: A sanitized HTML version—scripts, styles, or excluded tags are removed based on your `CrawlerRunConfig`.  
**Usage**:

`[](#__codelineno-9-1) print(result.cleaned_html[:500])  # Show a snippet`

### 2.3 **`fit_html`** _(Optional\[str\])_

**What**: If a **content filter** or heuristic (e.g., Pruning/BM25) modifies the HTML, the “fit” or post-filter version.  
**When**: This is **only** present if your `markdown_generator` or `content_filter` produces it.  
**Usage**:

`[](#__codelineno-10-1) if result.markdown.fit_html: [](#__codelineno-10-2)     print("High-value HTML content:", result.markdown.fit_html[:300])`

* * *

3\. Markdown Fields
-------------------

### 3.1 The Markdown Generation Approach

Crawl4AI can convert HTML→Markdown, optionally including:

*   **Raw** markdown
*   **Links as citations** (with a references section)
*   **Fit** markdown if a **content filter** is used (like Pruning or BM25)

**`MarkdownGenerationResult`** includes: - **`raw_markdown`** _(str)_: The full HTML→Markdown conversion.  
\- **`markdown_with_citations`** _(str)_: Same markdown, but with link references as academic-style citations.  
\- **`references_markdown`** _(str)_: The reference list or footnotes at the end.  
\- **`fit_markdown`** _(Optional\[str\])_: If content filtering (Pruning/BM25) was applied, the filtered “fit” text.  
\- **`fit_html`** _(Optional\[str\])_: The HTML that led to `fit_markdown`.

**Usage**:

`[](#__codelineno-11-1) if result.markdown: [](#__codelineno-11-2)     md_res = result.markdown [](#__codelineno-11-3)     print("Raw MD:", md_res.raw_markdown[:300]) [](#__codelineno-11-4)     print("Citations MD:", md_res.markdown_with_citations[:300]) [](#__codelineno-11-5)     print("References:", md_res.references_markdown) [](#__codelineno-11-6)     if md_res.fit_markdown: [](#__codelineno-11-7)         print("Pruned text:", md_res.fit_markdown[:300])`

### 3.2 **`markdown`** _(Optional\[Union\[str, MarkdownGenerationResult\]\])_

**What**: Holds the `MarkdownGenerationResult`.  
**Usage**:

`[](#__codelineno-12-1) print(result.markdown.raw_markdown[:200]) [](#__codelineno-12-2) print(result.markdown.fit_markdown) [](#__codelineno-12-3) print(result.markdown.fit_html)`

**Important**: “Fit” content (in `fit_markdown`/`fit_html`) exists in result.markdown, only if you used a **filter** (like **PruningContentFilter** or **BM25ContentFilter**) within a `MarkdownGenerationStrategy`.

* * *

4\. Media & Links
-----------------

### 4.1 **`media`** _(Dict\[str, List\[Dict\]\])_

**What**: Contains info about discovered images, videos, or audio. Typically keys: `"images"`, `"videos"`, `"audios"`.  
**Common Fields** in each item:

*   `src` _(str)_: Media URL
*   `alt` or `title` _(str)_: Descriptive text
*   `score` _(float)_: Relevance score if the crawler’s heuristic found it “important”
*   `desc` or `description` _(Optional\[str\])_: Additional context extracted from surrounding text

**Usage**:

`[](#__codelineno-13-1) images = result.media.get("images", []) [](#__codelineno-13-2) for img in images: [](#__codelineno-13-3)     if img.get("score", 0) > 5: [](#__codelineno-13-4)         print("High-value image:", img["src"])`

### 4.2 **`links`** _(Dict\[str, List\[Dict\]\])_

**What**: Holds internal and external link data. Usually two keys: `"internal"` and `"external"`.  
**Common Fields**:

*   `href` _(str)_: The link target
*   `text` _(str)_: Link text
*   `title` _(str)_: Title attribute
*   `context` _(str)_: Surrounding text snippet
*   `domain` _(str)_: If external, the domain

**Usage**:

`[](#__codelineno-14-1) for link in result.links["internal"]: [](#__codelineno-14-2)     print(f"Internal link to {link['href']} with text {link['text']}")`

* * *

5\. Additional Fields
---------------------

### 5.1 **`extracted_content`** _(Optional\[str\])_

**What**: If you used **`extraction_strategy`** (CSS, LLM, etc.), the structured output (JSON).  
**Usage**:

`[](#__codelineno-15-1) if result.extracted_content: [](#__codelineno-15-2)     data = json.loads(result.extracted_content) [](#__codelineno-15-3)     print(data)`

### 5.2 **`downloaded_files`** _(Optional\[List\[str\]\])_

**What**: If `accept_downloads=True` in your `BrowserConfig` + `downloads_path`, lists local file paths for downloaded items.  
**Usage**:

`[](#__codelineno-16-1) if result.downloaded_files: [](#__codelineno-16-2)     for file_path in result.downloaded_files: [](#__codelineno-16-3)         print("Downloaded:", file_path)`

### 5.3 **`screenshot`** _(Optional\[str\])_

**What**: Base64-encoded screenshot if `screenshot=True` in `CrawlerRunConfig`.  
**Usage**:

`[](#__codelineno-17-1) import base64 [](#__codelineno-17-2) if result.screenshot: [](#__codelineno-17-3)     with open("page.png", "wb") as f: [](#__codelineno-17-4)         f.write(base64.b64decode(result.screenshot))`

### 5.4 **`pdf`** _(Optional\[bytes\])_

**What**: Raw PDF bytes if `pdf=True` in `CrawlerRunConfig`.  
**Usage**:

`[](#__codelineno-18-1) if result.pdf: [](#__codelineno-18-2)     with open("page.pdf", "wb") as f: [](#__codelineno-18-3)         f.write(result.pdf)`

### 5.5 **`metadata`** _(Optional\[dict\])_

**What**: Page-level metadata if discovered (title, description, OG data, etc.).  
**Usage**:

`[](#__codelineno-19-1) if result.metadata: [](#__codelineno-19-2)     print("Title:", result.metadata.get("title")) [](#__codelineno-19-3)     print("Author:", result.metadata.get("author"))`

* * *

6\. `dispatch_result` (optional)
--------------------------------

A `DispatchResult` object providing additional concurrency and resource usage information when crawling URLs in parallel (e.g., via `arun_many()` with custom dispatchers). It contains:

*   **`task_id`**: A unique identifier for the parallel task.
*   **`memory_usage`** (float): The memory (in MB) used at the time of completion.
*   **`peak_memory`** (float): The peak memory usage (in MB) recorded during the task’s execution.
*   **`start_time`** / **`end_time`** (datetime): Time range for this crawling task.
*   **`error_message`** (str): Any dispatcher- or concurrency-related error encountered.

`[](#__codelineno-20-1) # Example usage: [](#__codelineno-20-2) for result in results: [](#__codelineno-20-3)     if result.success and result.dispatch_result: [](#__codelineno-20-4)         dr = result.dispatch_result [](#__codelineno-20-5)         print(f"URL: {result.url}, Task ID: {dr.task_id}") [](#__codelineno-20-6)         print(f"Memory: {dr.memory_usage:.1f} MB (Peak: {dr.peak_memory:.1f} MB)") [](#__codelineno-20-7)         print(f"Duration: {dr.end_time - dr.start_time}")`

> **Note**: This field is typically populated when using `arun_many(...)` alongside a **dispatcher** (e.g., `MemoryAdaptiveDispatcher` or `SemaphoreDispatcher`). If no concurrency or dispatcher is used, `dispatch_result` may remain `None`.

* * *

7\. Example: Accessing Everything
---------------------------------

`[](#__codelineno-21-1) async def handle_result(result: CrawlResult): [](#__codelineno-21-2)     if not result.success: [](#__codelineno-21-3)         print("Crawl error:", result.error_message) [](#__codelineno-21-4)         return [](#__codelineno-21-5) [](#__codelineno-21-6)     # Basic info [](#__codelineno-21-7)     print("Crawled URL:", result.url) [](#__codelineno-21-8)     print("Status code:", result.status_code) [](#__codelineno-21-9) [](#__codelineno-21-10)     # HTML [](#__codelineno-21-11)     print("Original HTML size:", len(result.html)) [](#__codelineno-21-12)     print("Cleaned HTML size:", len(result.cleaned_html or "")) [](#__codelineno-21-13) [](#__codelineno-21-14)     # Markdown output [](#__codelineno-21-15)     if result.markdown: [](#__codelineno-21-16)         print("Raw Markdown:", result.markdown.raw_markdown[:300]) [](#__codelineno-21-17)         print("Citations Markdown:", result.markdown.markdown_with_citations[:300]) [](#__codelineno-21-18)         if result.markdown.fit_markdown: [](#__codelineno-21-19)             print("Fit Markdown:", result.markdown.fit_markdown[:200]) [](#__codelineno-21-20) [](#__codelineno-21-21)     # Media & Links [](#__codelineno-21-22)     if "images" in result.media: [](#__codelineno-21-23)         print("Image count:", len(result.media["images"])) [](#__codelineno-21-24)     if "internal" in result.links: [](#__codelineno-21-25)         print("Internal link count:", len(result.links["internal"])) [](#__codelineno-21-26) [](#__codelineno-21-27)     # Extraction strategy result [](#__codelineno-21-28)     if result.extracted_content: [](#__codelineno-21-29)         print("Structured data:", result.extracted_content) [](#__codelineno-21-30) [](#__codelineno-21-31)     # Screenshot/PDF [](#__codelineno-21-32)     if result.screenshot: [](#__codelineno-21-33)         print("Screenshot length:", len(result.screenshot)) [](#__codelineno-21-34)     if result.pdf: [](#__codelineno-21-35)         print("PDF bytes length:", len(result.pdf))`

* * *

8\. Key Points & Future
-----------------------

1. **Deprecated legacy properties of CrawlResult**  
\- `markdown_v2` - Deprecated in v0.5. Just use `markdown`. It holds the `MarkdownGenerationResult` now! - `fit_markdown` and `fit_html` - Deprecated in v0.5. They can now be accessed via `MarkdownGenerationResult` in `result.markdown`. eg: `result.markdown.fit_markdown` and `result.markdown.fit_html`

2. **Fit Content**  
\- **`fit_markdown`** and **`fit_html`** appear in MarkdownGenerationResult, only if you used a content filter (like **PruningContentFilter** or **BM25ContentFilter**) inside your **MarkdownGenerationStrategy** or set them directly.  
\- If no filter is used, they remain `None`.

3. **References & Citations**  
\- If you enable link citations in your `DefaultMarkdownGenerator` (`options={"citations": True}`), you’ll see `markdown_with_citations` plus a **`references_markdown`** block. This helps large language models or academic-like referencing.

4. **Links & Media**  
\- `links["internal"]` and `links["external"]` group discovered anchors by domain.  
\- `media["images"]` / `["videos"]` / `["audios"]` store extracted media elements with optional scoring or context.

5. **Error Cases**  
\- If `success=False`, check `error_message` (e.g., timeouts, invalid URLs).  
\- `status_code` might be `None` if we failed before an HTTP response.

Use **`CrawlResult`** to glean all final outputs and feed them into your data pipelines, AI models, or archives. With the synergy of a properly configured **BrowserConfig** and **CrawlerRunConfig**, the crawler can produce robust, structured results here in **`CrawlResult`**.

* * *

---

# Hooks & Auth - Crawl4AI Documentation (v0.5.x)

Hooks & Auth in AsyncWebCrawler
===============================

Crawl4AI’s **hooks** let you customize the crawler at specific points in the pipeline:

1. **`on_browser_created`** – After browser creation.  
2. **`on_page_context_created`** – After a new context & page are created.  
3. **`before_goto`** – Just before navigating to a page.  
4. **`after_goto`** – Right after navigation completes.  
5. **`on_user_agent_updated`** – Whenever the user agent changes.  
6. **`on_execution_started`** – Once custom JavaScript execution begins.  
7. **`before_retrieve_html`** – Just before the crawler retrieves final HTML.  
8. **`before_return_html`** – Right before returning the HTML content.

**Important**: Avoid heavy tasks in `on_browser_created` since you don’t yet have a page context. If you need to _log in_, do so in **`on_page_context_created`**.

> note "Important Hook Usage Warning" **Avoid Misusing Hooks**: Do not manipulate page objects in the wrong hook or at the wrong time, as it can crash the pipeline or produce incorrect results. A common mistake is attempting to handle authentication prematurely—such as creating or closing pages in `on_browser_created`.
> 
> **Use the Right Hook for Auth**: If you need to log in or set tokens, use `on_page_context_created`. This ensures you have a valid page/context to work with, without disrupting the main crawling flow.
> 
> **Identity-Based Crawling**: For robust auth, consider identity-based crawling (or passing a session ID) to preserve state. Run your initial login steps in a separate, well-defined process, then feed that session to your main crawl—rather than shoehorning complex authentication into early hooks. Check out [Identity-Based Crawling](../identity-based-crawling/)
>  for more details.
> 
> **Be Cautious**: Overwriting or removing elements in the wrong hook can compromise the final crawl. Keep hooks focused on smaller tasks (like route filters, custom headers), and let your main logic (crawling, data extraction) proceed normally.

Below is an example demonstration.

* * *

Example: Using Hooks in AsyncWebCrawler
---------------------------------------

`[](#__codelineno-0-1) import asyncio [](#__codelineno-0-2) import json [](#__codelineno-0-3) from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode [](#__codelineno-0-4) from playwright.async_api import Page, BrowserContext [](#__codelineno-0-5) [](#__codelineno-0-6) async def main(): [](#__codelineno-0-7)     print("🔗 Hooks Example: Demonstrating recommended usage") [](#__codelineno-0-8) [](#__codelineno-0-9)     # 1) Configure the browser [](#__codelineno-0-10)     browser_config = BrowserConfig( [](#__codelineno-0-11)         headless=True, [](#__codelineno-0-12)         verbose=True [](#__codelineno-0-13)     ) [](#__codelineno-0-14) [](#__codelineno-0-15)     # 2) Configure the crawler run [](#__codelineno-0-16)     crawler_run_config = CrawlerRunConfig( [](#__codelineno-0-17)         js_code="window.scrollTo(0, document.body.scrollHeight);", [](#__codelineno-0-18)         wait_for="body", [](#__codelineno-0-19)         cache_mode=CacheMode.BYPASS [](#__codelineno-0-20)     ) [](#__codelineno-0-21) [](#__codelineno-0-22)     # 3) Create the crawler instance [](#__codelineno-0-23)     crawler = AsyncWebCrawler(config=browser_config) [](#__codelineno-0-24) [](#__codelineno-0-25)     # [](#__codelineno-0-26)     # Define Hook Functions [](#__codelineno-0-27)     # [](#__codelineno-0-28) [](#__codelineno-0-29)     async def on_browser_created(browser, **kwargs): [](#__codelineno-0-30)         # Called once the browser instance is created (but no pages or contexts yet) [](#__codelineno-0-31)         print("[HOOK] on_browser_created - Browser created successfully!") [](#__codelineno-0-32)         # Typically, do minimal setup here if needed [](#__codelineno-0-33)         return browser [](#__codelineno-0-34) [](#__codelineno-0-35)     async def on_page_context_created(page: Page, context: BrowserContext, **kwargs): [](#__codelineno-0-36)         # Called right after a new page + context are created (ideal for auth or route config). [](#__codelineno-0-37)         print("[HOOK] on_page_context_created - Setting up page & context.") [](#__codelineno-0-38) [](#__codelineno-0-39)         # Example 1: Route filtering (e.g., block images) [](#__codelineno-0-40)         async def route_filter(route): [](#__codelineno-0-41)             if route.request.resource_type == "image": [](#__codelineno-0-42)                 print(f"[HOOK] Blocking image request: {route.request.url}") [](#__codelineno-0-43)                 await route.abort() [](#__codelineno-0-44)             else: [](#__codelineno-0-45)                 await route.continue_() [](#__codelineno-0-46) [](#__codelineno-0-47)         await context.route("**", route_filter) [](#__codelineno-0-48) [](#__codelineno-0-49)         # Example 2: (Optional) Simulate a login scenario [](#__codelineno-0-50)         # (We do NOT create or close pages here, just do quick steps if needed) [](#__codelineno-0-51)         # e.g., await page.goto("https://example.com/login") [](#__codelineno-0-52)         # e.g., await page.fill("input[name='username']", "testuser") [](#__codelineno-0-53)         # e.g., await page.fill("input[name='password']", "password123") [](#__codelineno-0-54)         # e.g., await page.click("button[type='submit']") [](#__codelineno-0-55)         # e.g., await page.wait_for_selector("#welcome") [](#__codelineno-0-56)         # e.g., await context.add_cookies([...]) [](#__codelineno-0-57)         # Then continue [](#__codelineno-0-58) [](#__codelineno-0-59)         # Example 3: Adjust the viewport [](#__codelineno-0-60)         await page.set_viewport_size({"width": 1080, "height": 600}) [](#__codelineno-0-61)         return page [](#__codelineno-0-62) [](#__codelineno-0-63)     async def before_goto( [](#__codelineno-0-64)         page: Page, context: BrowserContext, url: str, **kwargs [](#__codelineno-0-65)     ): [](#__codelineno-0-66)         # Called before navigating to each URL. [](#__codelineno-0-67)         print(f"[HOOK] before_goto - About to navigate: {url}") [](#__codelineno-0-68)         # e.g., inject custom headers [](#__codelineno-0-69)         await page.set_extra_http_headers({ [](#__codelineno-0-70)             "Custom-Header": "my-value" [](#__codelineno-0-71)         }) [](#__codelineno-0-72)         return page [](#__codelineno-0-73) [](#__codelineno-0-74)     async def after_goto( [](#__codelineno-0-75)         page: Page, context: BrowserContext,  [](#__codelineno-0-76)         url: str, response, **kwargs [](#__codelineno-0-77)     ): [](#__codelineno-0-78)         # Called after navigation completes. [](#__codelineno-0-79)         print(f"[HOOK] after_goto - Successfully loaded: {url}") [](#__codelineno-0-80)         # e.g., wait for a certain element if we want to verify [](#__codelineno-0-81)         try: [](#__codelineno-0-82)             await page.wait_for_selector('.content', timeout=1000) [](#__codelineno-0-83)             print("[HOOK] Found .content element!") [](#__codelineno-0-84)         except: [](#__codelineno-0-85)             print("[HOOK] .content not found, continuing anyway.") [](#__codelineno-0-86)         return page [](#__codelineno-0-87) [](#__codelineno-0-88)     async def on_user_agent_updated( [](#__codelineno-0-89)         page: Page, context: BrowserContext,  [](#__codelineno-0-90)         user_agent: str, **kwargs [](#__codelineno-0-91)     ): [](#__codelineno-0-92)         # Called whenever the user agent updates. [](#__codelineno-0-93)         print(f"[HOOK] on_user_agent_updated - New user agent: {user_agent}") [](#__codelineno-0-94)         return page [](#__codelineno-0-95) [](#__codelineno-0-96)     async def on_execution_started(page: Page, context: BrowserContext, **kwargs): [](#__codelineno-0-97)         # Called after custom JavaScript execution begins. [](#__codelineno-0-98)         print("[HOOK] on_execution_started - JS code is running!") [](#__codelineno-0-99)         return page [](#__codelineno-0-100) [](#__codelineno-0-101)     async def before_retrieve_html(page: Page, context: BrowserContext, **kwargs): [](#__codelineno-0-102)         # Called before final HTML retrieval. [](#__codelineno-0-103)         print("[HOOK] before_retrieve_html - We can do final actions") [](#__codelineno-0-104)         # Example: Scroll again [](#__codelineno-0-105)         await page.evaluate("window.scrollTo(0, document.body.scrollHeight);") [](#__codelineno-0-106)         return page [](#__codelineno-0-107) [](#__codelineno-0-108)     async def before_return_html( [](#__codelineno-0-109)         page: Page, context: BrowserContext, html: str, **kwargs [](#__codelineno-0-110)     ): [](#__codelineno-0-111)         # Called just before returning the HTML in the result. [](#__codelineno-0-112)         print(f"[HOOK] before_return_html - HTML length: {len(html)}") [](#__codelineno-0-113)         return page [](#__codelineno-0-114) [](#__codelineno-0-115)     # [](#__codelineno-0-116)     # Attach Hooks [](#__codelineno-0-117)     # [](#__codelineno-0-118) [](#__codelineno-0-119)     crawler.crawler_strategy.set_hook("on_browser_created", on_browser_created) [](#__codelineno-0-120)     crawler.crawler_strategy.set_hook( [](#__codelineno-0-121)         "on_page_context_created", on_page_context_created [](#__codelineno-0-122)     ) [](#__codelineno-0-123)     crawler.crawler_strategy.set_hook("before_goto", before_goto) [](#__codelineno-0-124)     crawler.crawler_strategy.set_hook("after_goto", after_goto) [](#__codelineno-0-125)     crawler.crawler_strategy.set_hook( [](#__codelineno-0-126)         "on_user_agent_updated", on_user_agent_updated [](#__codelineno-0-127)     ) [](#__codelineno-0-128)     crawler.crawler_strategy.set_hook( [](#__codelineno-0-129)         "on_execution_started", on_execution_started [](#__codelineno-0-130)     ) [](#__codelineno-0-131)     crawler.crawler_strategy.set_hook( [](#__codelineno-0-132)         "before_retrieve_html", before_retrieve_html [](#__codelineno-0-133)     ) [](#__codelineno-0-134)     crawler.crawler_strategy.set_hook( [](#__codelineno-0-135)         "before_return_html", before_return_html [](#__codelineno-0-136)     ) [](#__codelineno-0-137) [](#__codelineno-0-138)     await crawler.start() [](#__codelineno-0-139) [](#__codelineno-0-140)     # 4) Run the crawler on an example page [](#__codelineno-0-141)     url = "https://example.com" [](#__codelineno-0-142)     result = await crawler.arun(url, config=crawler_run_config) [](#__codelineno-0-143) [](#__codelineno-0-144)     if result.success: [](#__codelineno-0-145)         print("\nCrawled URL:", result.url) [](#__codelineno-0-146)         print("HTML length:", len(result.html)) [](#__codelineno-0-147)     else: [](#__codelineno-0-148)         print("Error:", result.error_message) [](#__codelineno-0-149) [](#__codelineno-0-150)     await crawler.close() [](#__codelineno-0-151) [](#__codelineno-0-152) if __name__ == "__main__": [](#__codelineno-0-153)     asyncio.run(main())`

* * *

Hook Lifecycle Summary
----------------------

1. **`on_browser_created`**:  
\- Browser is up, but **no** pages or contexts yet.  
\- Light setup only—don’t try to open or close pages here (that belongs in `on_page_context_created`).

2. **`on_page_context_created`**:  
\- Perfect for advanced **auth** or route blocking.  
\- You have a **page** + **context** ready but haven’t navigated to the target URL yet.

3. **`before_goto`**:  
\- Right before navigation. Typically used for setting **custom headers** or logging the target URL.

4. **`after_goto`**:  
\- After page navigation is done. Good place for verifying content or waiting on essential elements.

5. **`on_user_agent_updated`**:  
\- Whenever the user agent changes (for stealth or different UA modes).

6. **`on_execution_started`**:  
\- If you set `js_code` or run custom scripts, this runs once your JS is about to start.

7. **`before_retrieve_html`**:  
\- Just before the final HTML snapshot is taken. Often you do a final scroll or lazy-load triggers here.

8. **`before_return_html`**:  
\- The last hook before returning HTML to the `CrawlResult`. Good for logging HTML length or minor modifications.

* * *

When to Handle Authentication
-----------------------------

**Recommended**: Use **`on_page_context_created`** if you need to:

*   Navigate to a login page or fill forms
*   Set cookies or localStorage tokens
*   Block resource routes to avoid ads

This ensures the newly created context is under your control **before** `arun()` navigates to the main URL.

* * *

Additional Considerations
-------------------------

*   **Session Management**: If you want multiple `arun()` calls to reuse a single session, pass `session_id=` in your `CrawlerRunConfig`. Hooks remain the same.
*   **Performance**: Hooks can slow down crawling if they do heavy tasks. Keep them concise.
*   **Error Handling**: If a hook fails, the overall crawl might fail. Catch exceptions or handle them gracefully.
*   **Concurrency**: If you run `arun_many()`, each URL triggers these hooks in parallel. Ensure your hooks are thread/async-safe.

* * *

Conclusion
----------

Hooks provide **fine-grained** control over:

*   **Browser** creation (light tasks only)
*   **Page** and **context** creation (auth, route blocking)
*   **Navigation** phases
*   **Final HTML** retrieval

Follow the recommended usage: - **Login** or advanced tasks in `on_page_context_created`  
\- **Custom headers** or logs in `before_goto` / `after_goto`  
\- **Scrolling** or final checks in `before_retrieve_html` / `before_return_html`

* * *

---

# Session Management - Crawl4AI Documentation (v0.5.x)

Session Management
==================

Session management in Crawl4AI is a powerful feature that allows you to maintain state across multiple requests, making it particularly suitable for handling complex multi-step crawling tasks. It enables you to reuse the same browser tab (or page object) across sequential actions and crawls, which is beneficial for:

*   **Performing JavaScript actions before and after crawling.**
*   **Executing multiple sequential crawls faster** without needing to reopen tabs or allocate memory repeatedly.

**Note:** This feature is designed for sequential workflows and is not suitable for parallel operations.

* * *

#### Basic Session Usage

Use `BrowserConfig` and `CrawlerRunConfig` to maintain state with a `session_id`:

`[](#__codelineno-0-1) from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig [](#__codelineno-0-2) [](#__codelineno-0-3) async with AsyncWebCrawler() as crawler: [](#__codelineno-0-4)     session_id = "my_session" [](#__codelineno-0-5) [](#__codelineno-0-6)     # Define configurations [](#__codelineno-0-7)     config1 = CrawlerRunConfig( [](#__codelineno-0-8)         url="https://example.com/page1", session_id=session_id [](#__codelineno-0-9)     ) [](#__codelineno-0-10)     config2 = CrawlerRunConfig( [](#__codelineno-0-11)         url="https://example.com/page2", session_id=session_id [](#__codelineno-0-12)     ) [](#__codelineno-0-13) [](#__codelineno-0-14)     # First request [](#__codelineno-0-15)     result1 = await crawler.arun(config=config1) [](#__codelineno-0-16) [](#__codelineno-0-17)     # Subsequent request using the same session [](#__codelineno-0-18)     result2 = await crawler.arun(config=config2) [](#__codelineno-0-19) [](#__codelineno-0-20)     # Clean up when done [](#__codelineno-0-21)     await crawler.crawler_strategy.kill_session(session_id)`

* * *

#### Dynamic Content with Sessions

Here's an example of crawling GitHub commits across multiple pages while preserving session state:

`[](#__codelineno-1-1) from crawl4ai.async_configs import CrawlerRunConfig [](#__codelineno-1-2) from crawl4ai.extraction_strategy import JsonCssExtractionStrategy [](#__codelineno-1-3) from crawl4ai.cache_context import CacheMode [](#__codelineno-1-4) [](#__codelineno-1-5) async def crawl_dynamic_content(): [](#__codelineno-1-6)     async with AsyncWebCrawler() as crawler: [](#__codelineno-1-7)         session_id = "github_commits_session" [](#__codelineno-1-8)         url = "https://github.com/microsoft/TypeScript/commits/main" [](#__codelineno-1-9)         all_commits = [] [](#__codelineno-1-10) [](#__codelineno-1-11)         # Define extraction schema [](#__codelineno-1-12)         schema = { [](#__codelineno-1-13)             "name": "Commit Extractor", [](#__codelineno-1-14)             "baseSelector": "li.Box-sc-g0xbh4-0", [](#__codelineno-1-15)             "fields": [{ [](#__codelineno-1-16)                 "name": "title", "selector": "h4.markdown-title", "type": "text" [](#__codelineno-1-17)             }], [](#__codelineno-1-18)         } [](#__codelineno-1-19)         extraction_strategy = JsonCssExtractionStrategy(schema) [](#__codelineno-1-20) [](#__codelineno-1-21)         # JavaScript and wait configurations [](#__codelineno-1-22)         js_next_page = """document.querySelector('a[data-testid="pagination-next-button"]').click();""" [](#__codelineno-1-23)         wait_for = """() => document.querySelectorAll('li.Box-sc-g0xbh4-0').length > 0""" [](#__codelineno-1-24) [](#__codelineno-1-25)         # Crawl multiple pages [](#__codelineno-1-26)         for page in range(3): [](#__codelineno-1-27)             config = CrawlerRunConfig( [](#__codelineno-1-28)                 url=url, [](#__codelineno-1-29)                 session_id=session_id, [](#__codelineno-1-30)                 extraction_strategy=extraction_strategy, [](#__codelineno-1-31)                 js_code=js_next_page if page > 0 else None, [](#__codelineno-1-32)                 wait_for=wait_for if page > 0 else None, [](#__codelineno-1-33)                 js_only=page > 0, [](#__codelineno-1-34)                 cache_mode=CacheMode.BYPASS [](#__codelineno-1-35)             ) [](#__codelineno-1-36) [](#__codelineno-1-37)             result = await crawler.arun(config=config) [](#__codelineno-1-38)             if result.success: [](#__codelineno-1-39)                 commits = json.loads(result.extracted_content) [](#__codelineno-1-40)                 all_commits.extend(commits) [](#__codelineno-1-41)                 print(f"Page {page + 1}: Found {len(commits)} commits") [](#__codelineno-1-42) [](#__codelineno-1-43)         # Clean up session [](#__codelineno-1-44)         await crawler.crawler_strategy.kill_session(session_id) [](#__codelineno-1-45)         return all_commits`

* * *

Example 1: Basic Session-Based Crawling
---------------------------------------

A simple example using session-based crawling:

`[](#__codelineno-2-1) import asyncio [](#__codelineno-2-2) from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig [](#__codelineno-2-3) from crawl4ai.cache_context import CacheMode [](#__codelineno-2-4) [](#__codelineno-2-5) async def basic_session_crawl(): [](#__codelineno-2-6)     async with AsyncWebCrawler() as crawler: [](#__codelineno-2-7)         session_id = "dynamic_content_session" [](#__codelineno-2-8)         url = "https://example.com/dynamic-content" [](#__codelineno-2-9) [](#__codelineno-2-10)         for page in range(3): [](#__codelineno-2-11)             config = CrawlerRunConfig( [](#__codelineno-2-12)                 url=url, [](#__codelineno-2-13)                 session_id=session_id, [](#__codelineno-2-14)                 js_code="document.querySelector('.load-more-button').click();" if page > 0 else None, [](#__codelineno-2-15)                 css_selector=".content-item", [](#__codelineno-2-16)                 cache_mode=CacheMode.BYPASS [](#__codelineno-2-17)             ) [](#__codelineno-2-18) [](#__codelineno-2-19)             result = await crawler.arun(config=config) [](#__codelineno-2-20)             print(f"Page {page + 1}: Found {result.extracted_content.count('.content-item')} items") [](#__codelineno-2-21) [](#__codelineno-2-22)         await crawler.crawler_strategy.kill_session(session_id) [](#__codelineno-2-23) [](#__codelineno-2-24) asyncio.run(basic_session_crawl())`

This example shows: 1. Reusing the same `session_id` across multiple requests. 2. Executing JavaScript to load more content dynamically. 3. Properly closing the session to free resources.

* * *

Advanced Technique 1: Custom Execution Hooks
--------------------------------------------

> Warning: You might feel confused by the end of the next few examples 😅, so make sure you are comfortable with the order of the parts before you start this.

Use custom hooks to handle complex scenarios, such as waiting for content to load dynamically:

`[](#__codelineno-3-1) async def advanced_session_crawl_with_hooks(): [](#__codelineno-3-2)     first_commit = "" [](#__codelineno-3-3) [](#__codelineno-3-4)     async def on_execution_started(page): [](#__codelineno-3-5)         nonlocal first_commit [](#__codelineno-3-6)         try: [](#__codelineno-3-7)             while True: [](#__codelineno-3-8)                 await page.wait_for_selector("li.commit-item h4") [](#__codelineno-3-9)                 commit = await page.query_selector("li.commit-item h4") [](#__codelineno-3-10)                 commit = await commit.evaluate("(element) => element.textContent").strip() [](#__codelineno-3-11)                 if commit and commit != first_commit: [](#__codelineno-3-12)                     first_commit = commit [](#__codelineno-3-13)                     break [](#__codelineno-3-14)                 await asyncio.sleep(0.5) [](#__codelineno-3-15)         except Exception as e: [](#__codelineno-3-16)             print(f"Warning: New content didn't appear: {e}") [](#__codelineno-3-17) [](#__codelineno-3-18)     async with AsyncWebCrawler() as crawler: [](#__codelineno-3-19)         session_id = "commit_session" [](#__codelineno-3-20)         url = "https://github.com/example/repo/commits/main" [](#__codelineno-3-21)         crawler.crawler_strategy.set_hook("on_execution_started", on_execution_started) [](#__codelineno-3-22) [](#__codelineno-3-23)         js_next_page = """document.querySelector('a.pagination-next').click();""" [](#__codelineno-3-24) [](#__codelineno-3-25)         for page in range(3): [](#__codelineno-3-26)             config = CrawlerRunConfig( [](#__codelineno-3-27)                 url=url, [](#__codelineno-3-28)                 session_id=session_id, [](#__codelineno-3-29)                 js_code=js_next_page if page > 0 else None, [](#__codelineno-3-30)                 css_selector="li.commit-item", [](#__codelineno-3-31)                 js_only=page > 0, [](#__codelineno-3-32)                 cache_mode=CacheMode.BYPASS [](#__codelineno-3-33)             ) [](#__codelineno-3-34) [](#__codelineno-3-35)             result = await crawler.arun(config=config) [](#__codelineno-3-36)             print(f"Page {page + 1}: Found {len(result.extracted_content)} commits") [](#__codelineno-3-37) [](#__codelineno-3-38)         await crawler.crawler_strategy.kill_session(session_id) [](#__codelineno-3-39) [](#__codelineno-3-40) asyncio.run(advanced_session_crawl_with_hooks())`

This technique ensures new content loads before the next action.

* * *

Advanced Technique 2: Integrated JavaScript Execution and Waiting
-----------------------------------------------------------------

Combine JavaScript execution and waiting logic for concise handling of dynamic content:

`[](#__codelineno-4-1) async def integrated_js_and_wait_crawl(): [](#__codelineno-4-2)     async with AsyncWebCrawler() as crawler: [](#__codelineno-4-3)         session_id = "integrated_session" [](#__codelineno-4-4)         url = "https://github.com/example/repo/commits/main" [](#__codelineno-4-5) [](#__codelineno-4-6)         js_next_page_and_wait = """ [](#__codelineno-4-7)         (async () => { [](#__codelineno-4-8)             const getCurrentCommit = () => document.querySelector('li.commit-item h4').textContent.trim(); [](#__codelineno-4-9)             const initialCommit = getCurrentCommit(); [](#__codelineno-4-10)             document.querySelector('a.pagination-next').click(); [](#__codelineno-4-11)             while (getCurrentCommit() === initialCommit) { [](#__codelineno-4-12)                 await new Promise(resolve => setTimeout(resolve, 100)); [](#__codelineno-4-13)             } [](#__codelineno-4-14)         })(); [](#__codelineno-4-15)         """ [](#__codelineno-4-16) [](#__codelineno-4-17)         for page in range(3): [](#__codelineno-4-18)             config = CrawlerRunConfig( [](#__codelineno-4-19)                 url=url, [](#__codelineno-4-20)                 session_id=session_id, [](#__codelineno-4-21)                 js_code=js_next_page_and_wait if page > 0 else None, [](#__codelineno-4-22)                 css_selector="li.commit-item", [](#__codelineno-4-23)                 js_only=page > 0, [](#__codelineno-4-24)                 cache_mode=CacheMode.BYPASS [](#__codelineno-4-25)             ) [](#__codelineno-4-26) [](#__codelineno-4-27)             result = await crawler.arun(config=config) [](#__codelineno-4-28)             print(f"Page {page + 1}: Found {len(result.extracted_content)} commits") [](#__codelineno-4-29) [](#__codelineno-4-30)         await crawler.crawler_strategy.kill_session(session_id) [](#__codelineno-4-31) [](#__codelineno-4-32) asyncio.run(integrated_js_and_wait_crawl())`

* * *

#### Common Use Cases for Sessions

1. **Authentication Flows**: Login and interact with secured pages.

2. **Pagination Handling**: Navigate through multiple pages.

3. **Form Submissions**: Fill forms, submit, and process results.

4. **Multi-step Processes**: Complete workflows that span multiple actions.

5. **Dynamic Content Navigation**: Handle JavaScript-rendered or event-triggered content.

* * *

---

# Overview - Crawl4AI Documentation (v0.5.x)

Overview of Some Important Advanced Features
============================================

(Proxy, PDF, Screenshot, SSL, Headers, & Storage State)

Crawl4AI offers multiple power-user features that go beyond simple crawling. This tutorial covers:

1. **Proxy Usage**  
2. **Capturing PDFs & Screenshots**  
3. **Handling SSL Certificates**  
4. **Custom Headers**  
5. **Session Persistence & Local Storage**  
6. **Robots.txt Compliance**

> **Prerequisites**  
> \- You have a basic grasp of [AsyncWebCrawler Basics](../../core/simple-crawling/)
>   
> \- You know how to run or configure your Python environment with Playwright installed

* * *

1\. Proxy Usage
---------------

If you need to route your crawl traffic through a proxy—whether for IP rotation, geo-testing, or privacy—Crawl4AI supports it via `BrowserConfig.proxy_config`.

`[](#__codelineno-0-1) import asyncio [](#__codelineno-0-2) from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig [](#__codelineno-0-3) [](#__codelineno-0-4) async def main(): [](#__codelineno-0-5)     browser_cfg = BrowserConfig( [](#__codelineno-0-6)         proxy_config={ [](#__codelineno-0-7)             "server": "http://proxy.example.com:8080", [](#__codelineno-0-8)             "username": "myuser", [](#__codelineno-0-9)             "password": "mypass", [](#__codelineno-0-10)         }, [](#__codelineno-0-11)         headless=True [](#__codelineno-0-12)     ) [](#__codelineno-0-13)     crawler_cfg = CrawlerRunConfig( [](#__codelineno-0-14)         verbose=True [](#__codelineno-0-15)     ) [](#__codelineno-0-16) [](#__codelineno-0-17)     async with AsyncWebCrawler(config=browser_cfg) as crawler: [](#__codelineno-0-18)         result = await crawler.arun( [](#__codelineno-0-19)             url="https://www.whatismyip.com/", [](#__codelineno-0-20)             config=crawler_cfg [](#__codelineno-0-21)         ) [](#__codelineno-0-22)         if result.success: [](#__codelineno-0-23)             print("[OK] Page fetched via proxy.") [](#__codelineno-0-24)             print("Page HTML snippet:", result.html[:200]) [](#__codelineno-0-25)         else: [](#__codelineno-0-26)             print("[ERROR]", result.error_message) [](#__codelineno-0-27) [](#__codelineno-0-28) if __name__ == "__main__": [](#__codelineno-0-29)     asyncio.run(main())`

**Key Points**  
\- **`proxy_config`** expects a dict with `server` and optional auth credentials.  
\- Many commercial proxies provide an HTTP/HTTPS “gateway” server that you specify in `server`.  
\- If your proxy doesn’t need auth, omit `username`/`password`.

* * *

2\. Capturing PDFs & Screenshots
--------------------------------

Sometimes you need a visual record of a page or a PDF “printout.” Crawl4AI can do both in one pass:

`[](#__codelineno-1-1) import os, asyncio [](#__codelineno-1-2) from base64 import b64decode [](#__codelineno-1-3) from crawl4ai import AsyncWebCrawler, CacheMode [](#__codelineno-1-4) [](#__codelineno-1-5) async def main(): [](#__codelineno-1-6)     async with AsyncWebCrawler() as crawler: [](#__codelineno-1-7)         result = await crawler.arun( [](#__codelineno-1-8)             url="https://en.wikipedia.org/wiki/List_of_common_misconceptions", [](#__codelineno-1-9)             cache_mode=CacheMode.BYPASS, [](#__codelineno-1-10)             pdf=True, [](#__codelineno-1-11)             screenshot=True [](#__codelineno-1-12)         ) [](#__codelineno-1-13) [](#__codelineno-1-14)         if result.success: [](#__codelineno-1-15)             # Save screenshot [](#__codelineno-1-16)             if result.screenshot: [](#__codelineno-1-17)                 with open("wikipedia_screenshot.png", "wb") as f: [](#__codelineno-1-18)                     f.write(b64decode(result.screenshot)) [](#__codelineno-1-19) [](#__codelineno-1-20)             # Save PDF [](#__codelineno-1-21)             if result.pdf: [](#__codelineno-1-22)                 with open("wikipedia_page.pdf", "wb") as f: [](#__codelineno-1-23)                     f.write(result.pdf) [](#__codelineno-1-24) [](#__codelineno-1-25)             print("[OK] PDF & screenshot captured.") [](#__codelineno-1-26)         else: [](#__codelineno-1-27)             print("[ERROR]", result.error_message) [](#__codelineno-1-28) [](#__codelineno-1-29) if __name__ == "__main__": [](#__codelineno-1-30)     asyncio.run(main())`

**Why PDF + Screenshot?**  
\- Large or complex pages can be slow or error-prone with “traditional” full-page screenshots.  
\- Exporting a PDF is more reliable for very long pages. Crawl4AI automatically converts the first PDF page into an image if you request both.

**Relevant Parameters**  
\- **`pdf=True`**: Exports the current page as a PDF (base64-encoded in `result.pdf`).  
\- **`screenshot=True`**: Creates a screenshot (base64-encoded in `result.screenshot`).  
\- **`scan_full_page`** or advanced hooking can further refine how the crawler captures content.

* * *

3\. Handling SSL Certificates
-----------------------------

If you need to verify or export a site’s SSL certificate—for compliance, debugging, or data analysis—Crawl4AI can fetch it during the crawl:

`[](#__codelineno-2-1) import asyncio, os [](#__codelineno-2-2) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode [](#__codelineno-2-3) [](#__codelineno-2-4) async def main(): [](#__codelineno-2-5)     tmp_dir = os.path.join(os.getcwd(), "tmp") [](#__codelineno-2-6)     os.makedirs(tmp_dir, exist_ok=True) [](#__codelineno-2-7) [](#__codelineno-2-8)     config = CrawlerRunConfig( [](#__codelineno-2-9)         fetch_ssl_certificate=True, [](#__codelineno-2-10)         cache_mode=CacheMode.BYPASS [](#__codelineno-2-11)     ) [](#__codelineno-2-12) [](#__codelineno-2-13)     async with AsyncWebCrawler() as crawler: [](#__codelineno-2-14)         result = await crawler.arun(url="https://example.com", config=config) [](#__codelineno-2-15) [](#__codelineno-2-16)         if result.success and result.ssl_certificate: [](#__codelineno-2-17)             cert = result.ssl_certificate [](#__codelineno-2-18)             print("\nCertificate Information:") [](#__codelineno-2-19)             print(f"Issuer (CN): {cert.issuer.get('CN', '')}") [](#__codelineno-2-20)             print(f"Valid until: {cert.valid_until}") [](#__codelineno-2-21)             print(f"Fingerprint: {cert.fingerprint}") [](#__codelineno-2-22) [](#__codelineno-2-23)             # Export in multiple formats: [](#__codelineno-2-24)             cert.to_json(os.path.join(tmp_dir, "certificate.json")) [](#__codelineno-2-25)             cert.to_pem(os.path.join(tmp_dir, "certificate.pem")) [](#__codelineno-2-26)             cert.to_der(os.path.join(tmp_dir, "certificate.der")) [](#__codelineno-2-27) [](#__codelineno-2-28)             print("\nCertificate exported to JSON/PEM/DER in 'tmp' folder.") [](#__codelineno-2-29)         else: [](#__codelineno-2-30)             print("[ERROR] No certificate or crawl failed.") [](#__codelineno-2-31) [](#__codelineno-2-32) if __name__ == "__main__": [](#__codelineno-2-33)     asyncio.run(main())`

**Key Points**  
\- **`fetch_ssl_certificate=True`** triggers certificate retrieval.  
\- `result.ssl_certificate` includes methods (`to_json`, `to_pem`, `to_der`) for saving in various formats (handy for server config, Java keystores, etc.).

* * *

4\. Custom Headers
------------------

Sometimes you need to set custom headers (e.g., language preferences, authentication tokens, or specialized user-agent strings). You can do this in multiple ways:

``[](#__codelineno-3-1) import asyncio [](#__codelineno-3-2) from crawl4ai import AsyncWebCrawler [](#__codelineno-3-3) [](#__codelineno-3-4) async def main(): [](#__codelineno-3-5)     # Option 1: Set headers at the crawler strategy level [](#__codelineno-3-6)     crawler1 = AsyncWebCrawler( [](#__codelineno-3-7)         # The underlying strategy can accept headers in its constructor [](#__codelineno-3-8)         crawler_strategy=None  # We'll override below for clarity [](#__codelineno-3-9)     ) [](#__codelineno-3-10)     crawler1.crawler_strategy.update_user_agent("MyCustomUA/1.0") [](#__codelineno-3-11)     crawler1.crawler_strategy.set_custom_headers({ [](#__codelineno-3-12)         "Accept-Language": "fr-FR,fr;q=0.9" [](#__codelineno-3-13)     }) [](#__codelineno-3-14)     result1 = await crawler1.arun("https://www.example.com") [](#__codelineno-3-15)     print("Example 1 result success:", result1.success) [](#__codelineno-3-16) [](#__codelineno-3-17)     # Option 2: Pass headers directly to `arun()` [](#__codelineno-3-18)     crawler2 = AsyncWebCrawler() [](#__codelineno-3-19)     result2 = await crawler2.arun( [](#__codelineno-3-20)         url="https://www.example.com", [](#__codelineno-3-21)         headers={"Accept-Language": "es-ES,es;q=0.9"} [](#__codelineno-3-22)     ) [](#__codelineno-3-23)     print("Example 2 result success:", result2.success) [](#__codelineno-3-24) [](#__codelineno-3-25) if __name__ == "__main__": [](#__codelineno-3-26)     asyncio.run(main())``

**Notes**  
\- Some sites may react differently to certain headers (e.g., `Accept-Language`).  
\- If you need advanced user-agent randomization or client hints, see [Identity-Based Crawling (Anti-Bot)](../identity-based-crawling/)
 or use `UserAgentGenerator`.

* * *

5\. Session Persistence & Local Storage
---------------------------------------

Crawl4AI can preserve cookies and localStorage so you can continue where you left off—ideal for logging into sites or skipping repeated auth flows.

### 5.1 `storage_state`

`[](#__codelineno-4-1) import asyncio [](#__codelineno-4-2) from crawl4ai import AsyncWebCrawler [](#__codelineno-4-3) [](#__codelineno-4-4) async def main(): [](#__codelineno-4-5)     storage_dict = { [](#__codelineno-4-6)         "cookies": [ [](#__codelineno-4-7)             { [](#__codelineno-4-8)                 "name": "session", [](#__codelineno-4-9)                 "value": "abcd1234", [](#__codelineno-4-10)                 "domain": "example.com", [](#__codelineno-4-11)                 "path": "/", [](#__codelineno-4-12)                 "expires": 1699999999.0, [](#__codelineno-4-13)                 "httpOnly": False, [](#__codelineno-4-14)                 "secure": False, [](#__codelineno-4-15)                 "sameSite": "None" [](#__codelineno-4-16)             } [](#__codelineno-4-17)         ], [](#__codelineno-4-18)         "origins": [ [](#__codelineno-4-19)             { [](#__codelineno-4-20)                 "origin": "https://example.com", [](#__codelineno-4-21)                 "localStorage": [ [](#__codelineno-4-22)                     {"name": "token", "value": "my_auth_token"} [](#__codelineno-4-23)                 ] [](#__codelineno-4-24)             } [](#__codelineno-4-25)         ] [](#__codelineno-4-26)     } [](#__codelineno-4-27) [](#__codelineno-4-28)     # Provide the storage state as a dictionary to start "already logged in" [](#__codelineno-4-29)     async with AsyncWebCrawler( [](#__codelineno-4-30)         headless=True, [](#__codelineno-4-31)         storage_state=storage_dict [](#__codelineno-4-32)     ) as crawler: [](#__codelineno-4-33)         result = await crawler.arun("https://example.com/protected") [](#__codelineno-4-34)         if result.success: [](#__codelineno-4-35)             print("Protected page content length:", len(result.html)) [](#__codelineno-4-36)         else: [](#__codelineno-4-37)             print("Failed to crawl protected page") [](#__codelineno-4-38) [](#__codelineno-4-39) if __name__ == "__main__": [](#__codelineno-4-40)     asyncio.run(main())`

### 5.2 Exporting & Reusing State

You can sign in once, export the browser context, and reuse it later—without re-entering credentials.

*   **`await context.storage_state(path="my_storage.json")`**: Exports cookies, localStorage, etc. to a file.
*   Provide `storage_state="my_storage.json"` on subsequent runs to skip the login step.

**See**: [Detailed session management tutorial](../session-management/)
 or [Explanations → Browser Context & Managed Browser](../identity-based-crawling/)
 for more advanced scenarios (like multi-step logins, or capturing after interactive pages).

* * *

6\. Robots.txt Compliance
-------------------------

Crawl4AI supports respecting robots.txt rules with efficient caching:

`[](#__codelineno-5-1) import asyncio [](#__codelineno-5-2) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig [](#__codelineno-5-3) [](#__codelineno-5-4) async def main(): [](#__codelineno-5-5)     # Enable robots.txt checking in config [](#__codelineno-5-6)     config = CrawlerRunConfig( [](#__codelineno-5-7)         check_robots_txt=True  # Will check and respect robots.txt rules [](#__codelineno-5-8)     ) [](#__codelineno-5-9) [](#__codelineno-5-10)     async with AsyncWebCrawler() as crawler: [](#__codelineno-5-11)         result = await crawler.arun( [](#__codelineno-5-12)             "https://example.com", [](#__codelineno-5-13)             config=config [](#__codelineno-5-14)         ) [](#__codelineno-5-15) [](#__codelineno-5-16)         if not result.success and result.status_code == 403: [](#__codelineno-5-17)             print("Access denied by robots.txt") [](#__codelineno-5-18) [](#__codelineno-5-19) if __name__ == "__main__": [](#__codelineno-5-20)     asyncio.run(main())`

**Key Points** - Robots.txt files are cached locally for efficiency - Cache is stored in `~/.crawl4ai/robots/robots_cache.db` - Cache has a default TTL of 7 days - If robots.txt can't be fetched, crawling is allowed - Returns 403 status code if URL is disallowed

* * *

Putting It All Together
-----------------------

Here’s a snippet that combines multiple “advanced” features (proxy, PDF, screenshot, SSL, custom headers, and session reuse) into one run. Normally, you’d tailor each setting to your project’s needs.

`[](#__codelineno-6-1) import os, asyncio [](#__codelineno-6-2) from base64 import b64decode [](#__codelineno-6-3) from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode [](#__codelineno-6-4) [](#__codelineno-6-5) async def main(): [](#__codelineno-6-6)     # 1. Browser config with proxy + headless [](#__codelineno-6-7)     browser_cfg = BrowserConfig( [](#__codelineno-6-8)         proxy_config={ [](#__codelineno-6-9)             "server": "http://proxy.example.com:8080", [](#__codelineno-6-10)             "username": "myuser", [](#__codelineno-6-11)             "password": "mypass", [](#__codelineno-6-12)         }, [](#__codelineno-6-13)         headless=True, [](#__codelineno-6-14)     ) [](#__codelineno-6-15) [](#__codelineno-6-16)     # 2. Crawler config with PDF, screenshot, SSL, custom headers, and ignoring caches [](#__codelineno-6-17)     crawler_cfg = CrawlerRunConfig( [](#__codelineno-6-18)         pdf=True, [](#__codelineno-6-19)         screenshot=True, [](#__codelineno-6-20)         fetch_ssl_certificate=True, [](#__codelineno-6-21)         cache_mode=CacheMode.BYPASS, [](#__codelineno-6-22)         headers={"Accept-Language": "en-US,en;q=0.8"}, [](#__codelineno-6-23)         storage_state="my_storage.json",  # Reuse session from a previous sign-in [](#__codelineno-6-24)         verbose=True, [](#__codelineno-6-25)     ) [](#__codelineno-6-26) [](#__codelineno-6-27)     # 3. Crawl [](#__codelineno-6-28)     async with AsyncWebCrawler(config=browser_cfg) as crawler: [](#__codelineno-6-29)         result = await crawler.arun( [](#__codelineno-6-30)             url = "https://secure.example.com/protected",  [](#__codelineno-6-31)             config=crawler_cfg [](#__codelineno-6-32)         ) [](#__codelineno-6-33) [](#__codelineno-6-34)         if result.success: [](#__codelineno-6-35)             print("[OK] Crawled the secure page. Links found:", len(result.links.get("internal", []))) [](#__codelineno-6-36) [](#__codelineno-6-37)             # Save PDF & screenshot [](#__codelineno-6-38)             if result.pdf: [](#__codelineno-6-39)                 with open("result.pdf", "wb") as f: [](#__codelineno-6-40)                     f.write(b64decode(result.pdf)) [](#__codelineno-6-41)             if result.screenshot: [](#__codelineno-6-42)                 with open("result.png", "wb") as f: [](#__codelineno-6-43)                     f.write(b64decode(result.screenshot)) [](#__codelineno-6-44) [](#__codelineno-6-45)             # Check SSL cert [](#__codelineno-6-46)             if result.ssl_certificate: [](#__codelineno-6-47)                 print("SSL Issuer CN:", result.ssl_certificate.issuer.get("CN", "")) [](#__codelineno-6-48)         else: [](#__codelineno-6-49)             print("[ERROR]", result.error_message) [](#__codelineno-6-50) [](#__codelineno-6-51) if __name__ == "__main__": [](#__codelineno-6-52)     asyncio.run(main())`

* * *

Conclusion & Next Steps
-----------------------

You’ve now explored several **advanced** features:

*   **Proxy Usage**
*   **PDF & Screenshot** capturing for large or critical pages
*   **SSL Certificate** retrieval & exporting
*   **Custom Headers** for language or specialized requests
*   **Session Persistence** via storage state
*   **Robots.txt Compliance**

With these power tools, you can build robust scraping workflows that mimic real user behavior, handle secure sites, capture detailed snapshots, and manage sessions across multiple runs—streamlining your entire data collection pipeline.

**Last Updated**: 2025-01-01

* * *

---

# Multi-URL Crawling - Crawl4AI Documentation (v0.5.x)

Advanced Multi-URL Crawling with Dispatchers
============================================

> **Heads Up**: Crawl4AI supports advanced dispatchers for **parallel** or **throttled** crawling, providing dynamic rate limiting and memory usage checks. The built-in `arun_many()` function uses these dispatchers to handle concurrency efficiently.

1\. Introduction
----------------

When crawling many URLs:

*   **Basic**: Use `arun()` in a loop (simple but less efficient)
*   **Better**: Use `arun_many()`, which efficiently handles multiple URLs with proper concurrency control
*   **Best**: Customize dispatcher behavior for your specific needs (memory management, rate limits, etc.)

**Why Dispatchers?**

*   **Adaptive**: Memory-based dispatchers can pause or slow down based on system resources
*   **Rate-limiting**: Built-in rate limiting with exponential backoff for 429/503 responses
*   **Real-time Monitoring**: Live dashboard of ongoing tasks, memory usage, and performance
*   **Flexibility**: Choose between memory-adaptive or semaphore-based concurrency

* * *

2\. Core Components
-------------------

### 2.1 Rate Limiter

`[](#__codelineno-0-1) class RateLimiter: [](#__codelineno-0-2)     def __init__( [](#__codelineno-0-3)         # Random delay range between requests [](#__codelineno-0-4)         base_delay: Tuple[float, float] = (1.0, 3.0),   [](#__codelineno-0-5) [](#__codelineno-0-6)         # Maximum backoff delay [](#__codelineno-0-7)         max_delay: float = 60.0,                         [](#__codelineno-0-8) [](#__codelineno-0-9)         # Retries before giving up [](#__codelineno-0-10)         max_retries: int = 3,                           [](#__codelineno-0-11) [](#__codelineno-0-12)         # Status codes triggering backoff [](#__codelineno-0-13)         rate_limit_codes: List[int] = [429, 503]         [](#__codelineno-0-14)     )`

Here’s the revised and simplified explanation of the **RateLimiter**, focusing on constructor parameters and adhering to your markdown style and mkDocs guidelines.

#### RateLimiter Constructor Parameters

The **RateLimiter** is a utility that helps manage the pace of requests to avoid overloading servers or getting blocked due to rate limits. It operates internally to delay requests and handle retries but can be configured using its constructor parameters.

**Parameters of the `RateLimiter` constructor:**

1. **`base_delay`** (`Tuple[float, float]`, default: `(1.0, 3.0)`)  
  The range for a random delay (in seconds) between consecutive requests to the same domain.

*   A random delay is chosen between `base_delay[0]` and `base_delay[1]` for each request.
*   This prevents sending requests at a predictable frequency, reducing the chances of triggering rate limits.

**Example:**  
If `base_delay = (2.0, 5.0)`, delays could be randomly chosen as `2.3s`, `4.1s`, etc.

* * *

2. **`max_delay`** (`float`, default: `60.0`)  
  The maximum allowable delay when rate-limiting errors occur.

*   When servers return rate-limit responses (e.g., 429 or 503), the delay increases exponentially with jitter.
*   The `max_delay` ensures the delay doesn’t grow unreasonably high, capping it at this value.

**Example:**  
For a `max_delay = 30.0`, even if backoff calculations suggest a delay of `45s`, it will cap at `30s`.

* * *

3. **`max_retries`** (`int`, default: `3`)  
  The maximum number of retries for a request if rate-limiting errors occur.

*   After encountering a rate-limit response, the `RateLimiter` retries the request up to this number of times.
*   If all retries fail, the request is marked as failed, and the process continues.

**Example:**  
If `max_retries = 3`, the system retries a failed request three times before giving up.

* * *

4. **`rate_limit_codes`** (`List[int]`, default: `[429, 503]`)  
  A list of HTTP status codes that trigger the rate-limiting logic.

*   These status codes indicate the server is overwhelmed or actively limiting requests.
*   You can customize this list to include other codes based on specific server behavior.

**Example:**  
If `rate_limit_codes = [429, 503, 504]`, the crawler will back off on these three error codes.

* * *

**How to Use the `RateLimiter`:**

Here’s an example of initializing and using a `RateLimiter` in your project:

`[](#__codelineno-1-1) from crawl4ai import RateLimiter [](#__codelineno-1-2) [](#__codelineno-1-3) # Create a RateLimiter with custom settings [](#__codelineno-1-4) rate_limiter = RateLimiter( [](#__codelineno-1-5)     base_delay=(2.0, 4.0),  # Random delay between 2-4 seconds [](#__codelineno-1-6)     max_delay=30.0,         # Cap delay at 30 seconds [](#__codelineno-1-7)     max_retries=5,          # Retry up to 5 times on rate-limiting errors [](#__codelineno-1-8)     rate_limit_codes=[429, 503]  # Handle these HTTP status codes [](#__codelineno-1-9) ) [](#__codelineno-1-10) [](#__codelineno-1-11) # RateLimiter will handle delays and retries internally [](#__codelineno-1-12) # No additional setup is required for its operation`

The `RateLimiter` integrates seamlessly with dispatchers like `MemoryAdaptiveDispatcher` and `SemaphoreDispatcher`, ensuring requests are paced correctly without user intervention. Its internal mechanisms manage delays and retries to avoid overwhelming servers while maximizing efficiency.

### 2.2 Crawler Monitor

The CrawlerMonitor provides real-time visibility into crawling operations:

`[](#__codelineno-2-1) from crawl4ai import CrawlerMonitor, DisplayMode [](#__codelineno-2-2) monitor = CrawlerMonitor( [](#__codelineno-2-3)     # Maximum rows in live display [](#__codelineno-2-4)     max_visible_rows=15,           [](#__codelineno-2-5) [](#__codelineno-2-6)     # DETAILED or AGGREGATED view [](#__codelineno-2-7)     display_mode=DisplayMode.DETAILED   [](#__codelineno-2-8) )`

**Display Modes**:

1.  **DETAILED**: Shows individual task status, memory usage, and timing
2.  **AGGREGATED**: Displays summary statistics and overall progress

* * *

3\. Available Dispatchers
-------------------------

### 3.1 MemoryAdaptiveDispatcher (Default)

Automatically manages concurrency based on system memory usage:

`[](#__codelineno-3-1) from crawl4ai.async_dispatcher import MemoryAdaptiveDispatcher [](#__codelineno-3-2) [](#__codelineno-3-3) dispatcher = MemoryAdaptiveDispatcher( [](#__codelineno-3-4)     memory_threshold_percent=90.0,  # Pause if memory exceeds this [](#__codelineno-3-5)     check_interval=1.0,             # How often to check memory [](#__codelineno-3-6)     max_session_permit=10,          # Maximum concurrent tasks [](#__codelineno-3-7)     rate_limiter=RateLimiter(       # Optional rate limiting [](#__codelineno-3-8)         base_delay=(1.0, 2.0), [](#__codelineno-3-9)         max_delay=30.0, [](#__codelineno-3-10)         max_retries=2 [](#__codelineno-3-11)     ), [](#__codelineno-3-12)     monitor=CrawlerMonitor(         # Optional monitoring [](#__codelineno-3-13)         max_visible_rows=15, [](#__codelineno-3-14)         display_mode=DisplayMode.DETAILED [](#__codelineno-3-15)     ) [](#__codelineno-3-16) )`

**Constructor Parameters:**

1. **`memory_threshold_percent`** (`float`, default: `90.0`)  
  Specifies the memory usage threshold (as a percentage). If system memory usage exceeds this value, the dispatcher pauses crawling to prevent system overload.

2. **`check_interval`** (`float`, default: `1.0`)  
  The interval (in seconds) at which the dispatcher checks system memory usage.

3. **`max_session_permit`** (`int`, default: `10`)  
  The maximum number of concurrent crawling tasks allowed. This ensures resource limits are respected while maintaining concurrency.

4. **`memory_wait_timeout`** (`float`, default: `300.0`)  
  Optional timeout (in seconds). If memory usage exceeds `memory_threshold_percent` for longer than this duration, a `MemoryError` is raised.

5. **`rate_limiter`** (`RateLimiter`, default: `None`)  
  Optional rate-limiting logic to avoid server-side blocking (e.g., for handling 429 or 503 errors). See **RateLimiter** for details.

6. **`monitor`** (`CrawlerMonitor`, default: `None`)  
  Optional monitoring for real-time task tracking and performance insights. See **CrawlerMonitor** for details.

* * *

### 3.2 SemaphoreDispatcher

Provides simple concurrency control with a fixed limit:

`[](#__codelineno-4-1) from crawl4ai.async_dispatcher import SemaphoreDispatcher [](#__codelineno-4-2) [](#__codelineno-4-3) dispatcher = SemaphoreDispatcher( [](#__codelineno-4-4)     max_session_permit=20,         # Maximum concurrent tasks [](#__codelineno-4-5)     rate_limiter=RateLimiter(      # Optional rate limiting [](#__codelineno-4-6)         base_delay=(0.5, 1.0), [](#__codelineno-4-7)         max_delay=10.0 [](#__codelineno-4-8)     ), [](#__codelineno-4-9)     monitor=CrawlerMonitor(        # Optional monitoring [](#__codelineno-4-10)         max_visible_rows=15, [](#__codelineno-4-11)         display_mode=DisplayMode.DETAILED [](#__codelineno-4-12)     ) [](#__codelineno-4-13) )`

**Constructor Parameters:**

1. **`max_session_permit`** (`int`, default: `20`)  
  The maximum number of concurrent crawling tasks allowed, irrespective of semaphore slots.

2. **`rate_limiter`** (`RateLimiter`, default: `None`)  
  Optional rate-limiting logic to avoid overwhelming servers. See **RateLimiter** for details.

3. **`monitor`** (`CrawlerMonitor`, default: `None`)  
  Optional monitoring for tracking task progress and resource usage. See **CrawlerMonitor** for details.

* * *

4\. Usage Examples
------------------

### 4.1 Batch Processing (Default)

`[](#__codelineno-5-1) async def crawl_batch(): [](#__codelineno-5-2)     browser_config = BrowserConfig(headless=True, verbose=False) [](#__codelineno-5-3)     run_config = CrawlerRunConfig( [](#__codelineno-5-4)         cache_mode=CacheMode.BYPASS, [](#__codelineno-5-5)         stream=False  # Default: get all results at once [](#__codelineno-5-6)     ) [](#__codelineno-5-7) [](#__codelineno-5-8)     dispatcher = MemoryAdaptiveDispatcher( [](#__codelineno-5-9)         memory_threshold_percent=70.0, [](#__codelineno-5-10)         check_interval=1.0, [](#__codelineno-5-11)         max_session_permit=10, [](#__codelineno-5-12)         monitor=CrawlerMonitor( [](#__codelineno-5-13)             display_mode=DisplayMode.DETAILED [](#__codelineno-5-14)         ) [](#__codelineno-5-15)     ) [](#__codelineno-5-16) [](#__codelineno-5-17)     async with AsyncWebCrawler(config=browser_config) as crawler: [](#__codelineno-5-18)         # Get all results at once [](#__codelineno-5-19)         results = await crawler.arun_many( [](#__codelineno-5-20)             urls=urls, [](#__codelineno-5-21)             config=run_config, [](#__codelineno-5-22)             dispatcher=dispatcher [](#__codelineno-5-23)         ) [](#__codelineno-5-24) [](#__codelineno-5-25)         # Process all results after completion [](#__codelineno-5-26)         for result in results: [](#__codelineno-5-27)             if result.success: [](#__codelineno-5-28)                 await process_result(result) [](#__codelineno-5-29)             else: [](#__codelineno-5-30)                 print(f"Failed to crawl {result.url}: {result.error_message}")`

**Review:**  
\- **Purpose:** Executes a batch crawl with all URLs processed together after crawling is complete.  
\- **Dispatcher:** Uses `MemoryAdaptiveDispatcher` to manage concurrency and system memory.  
\- **Stream:** Disabled (`stream=False`), so all results are collected at once for post-processing.  
\- **Best Use Case:** When you need to analyze results in bulk rather than individually during the crawl.

* * *

### 4.2 Streaming Mode

`[](#__codelineno-6-1) async def crawl_streaming(): [](#__codelineno-6-2)     browser_config = BrowserConfig(headless=True, verbose=False) [](#__codelineno-6-3)     run_config = CrawlerRunConfig( [](#__codelineno-6-4)         cache_mode=CacheMode.BYPASS, [](#__codelineno-6-5)         stream=True  # Enable streaming mode [](#__codelineno-6-6)     ) [](#__codelineno-6-7) [](#__codelineno-6-8)     dispatcher = MemoryAdaptiveDispatcher( [](#__codelineno-6-9)         memory_threshold_percent=70.0, [](#__codelineno-6-10)         check_interval=1.0, [](#__codelineno-6-11)         max_session_permit=10, [](#__codelineno-6-12)         monitor=CrawlerMonitor( [](#__codelineno-6-13)             display_mode=DisplayMode.DETAILED [](#__codelineno-6-14)         ) [](#__codelineno-6-15)     ) [](#__codelineno-6-16) [](#__codelineno-6-17)     async with AsyncWebCrawler(config=browser_config) as crawler: [](#__codelineno-6-18)         # Process results as they become available [](#__codelineno-6-19)         async for result in await crawler.arun_many( [](#__codelineno-6-20)             urls=urls, [](#__codelineno-6-21)             config=run_config, [](#__codelineno-6-22)             dispatcher=dispatcher [](#__codelineno-6-23)         ): [](#__codelineno-6-24)             if result.success: [](#__codelineno-6-25)                 # Process each result immediately [](#__codelineno-6-26)                 await process_result(result) [](#__codelineno-6-27)             else: [](#__codelineno-6-28)                 print(f"Failed to crawl {result.url}: {result.error_message}")`

**Review:**  
\- **Purpose:** Enables streaming to process results as soon as they’re available.  
\- **Dispatcher:** Uses `MemoryAdaptiveDispatcher` for concurrency and memory management.  
\- **Stream:** Enabled (`stream=True`), allowing real-time processing during crawling.  
\- **Best Use Case:** When you need to act on results immediately, such as for real-time analytics or progressive data storage.

* * *

### 4.3 Semaphore-based Crawling

`[](#__codelineno-7-1) async def crawl_with_semaphore(urls): [](#__codelineno-7-2)     browser_config = BrowserConfig(headless=True, verbose=False) [](#__codelineno-7-3)     run_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS) [](#__codelineno-7-4) [](#__codelineno-7-5)     dispatcher = SemaphoreDispatcher( [](#__codelineno-7-6)         semaphore_count=5, [](#__codelineno-7-7)         rate_limiter=RateLimiter( [](#__codelineno-7-8)             base_delay=(0.5, 1.0), [](#__codelineno-7-9)             max_delay=10.0 [](#__codelineno-7-10)         ), [](#__codelineno-7-11)         monitor=CrawlerMonitor( [](#__codelineno-7-12)             max_visible_rows=15, [](#__codelineno-7-13)             display_mode=DisplayMode.DETAILED [](#__codelineno-7-14)         ) [](#__codelineno-7-15)     ) [](#__codelineno-7-16) [](#__codelineno-7-17)     async with AsyncWebCrawler(config=browser_config) as crawler: [](#__codelineno-7-18)         results = await crawler.arun_many( [](#__codelineno-7-19)             urls,  [](#__codelineno-7-20)             config=run_config, [](#__codelineno-7-21)             dispatcher=dispatcher [](#__codelineno-7-22)         ) [](#__codelineno-7-23)         return results`

**Review:**  
\- **Purpose:** Uses `SemaphoreDispatcher` to limit concurrency with a fixed number of slots.  
\- **Dispatcher:** Configured with a semaphore to control parallel crawling tasks.  
\- **Rate Limiter:** Prevents servers from being overwhelmed by pacing requests.  
\- **Best Use Case:** When you want precise control over the number of concurrent requests, independent of system memory.

* * *

### 4.4 Robots.txt Consideration

`[](#__codelineno-8-1) import asyncio [](#__codelineno-8-2) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode [](#__codelineno-8-3) [](#__codelineno-8-4) async def main(): [](#__codelineno-8-5)     urls = [ [](#__codelineno-8-6)         "https://example1.com", [](#__codelineno-8-7)         "https://example2.com", [](#__codelineno-8-8)         "https://example3.com" [](#__codelineno-8-9)     ] [](#__codelineno-8-10) [](#__codelineno-8-11)     config = CrawlerRunConfig( [](#__codelineno-8-12)         cache_mode=CacheMode.ENABLED, [](#__codelineno-8-13)         check_robots_txt=True,  # Will respect robots.txt for each URL [](#__codelineno-8-14)         semaphore_count=3      # Max concurrent requests [](#__codelineno-8-15)     ) [](#__codelineno-8-16) [](#__codelineno-8-17)     async with AsyncWebCrawler() as crawler: [](#__codelineno-8-18)         async for result in crawler.arun_many(urls, config=config): [](#__codelineno-8-19)             if result.success: [](#__codelineno-8-20)                 print(f"Successfully crawled {result.url}") [](#__codelineno-8-21)             elif result.status_code == 403 and "robots.txt" in result.error_message: [](#__codelineno-8-22)                 print(f"Skipped {result.url} - blocked by robots.txt") [](#__codelineno-8-23)             else: [](#__codelineno-8-24)                 print(f"Failed to crawl {result.url}: {result.error_message}") [](#__codelineno-8-25) [](#__codelineno-8-26) if __name__ == "__main__": [](#__codelineno-8-27)     asyncio.run(main())`

**Review:**  
\- **Purpose:** Ensures compliance with `robots.txt` rules for ethical and legal web crawling.  
\- **Configuration:** Set `check_robots_txt=True` to validate each URL against `robots.txt` before crawling.  
\- **Dispatcher:** Handles requests with concurrency limits (`semaphore_count=3`).  
\- **Best Use Case:** When crawling websites that strictly enforce robots.txt policies or for responsible crawling practices.

* * *

5\. Dispatch Results
--------------------

Each crawl result includes dispatch information:

`[](#__codelineno-9-1) @dataclass [](#__codelineno-9-2) class DispatchResult: [](#__codelineno-9-3)     task_id: str [](#__codelineno-9-4)     memory_usage: float [](#__codelineno-9-5)     peak_memory: float [](#__codelineno-9-6)     start_time: datetime [](#__codelineno-9-7)     end_time: datetime [](#__codelineno-9-8)     error_message: str = ""`

Access via `result.dispatch_result`:

`[](#__codelineno-10-1) for result in results: [](#__codelineno-10-2)     if result.success: [](#__codelineno-10-3)         dr = result.dispatch_result [](#__codelineno-10-4)         print(f"URL: {result.url}") [](#__codelineno-10-5)         print(f"Memory: {dr.memory_usage:.1f}MB") [](#__codelineno-10-6)         print(f"Duration: {dr.end_time - dr.start_time}")`

6\. Summary
-----------

1. **Two Dispatcher Types**:

*   MemoryAdaptiveDispatcher (default): Dynamic concurrency based on memory
*   SemaphoreDispatcher: Fixed concurrency limit

2. **Optional Components**:

*   RateLimiter: Smart request pacing and backoff
*   CrawlerMonitor: Real-time progress visualization

3. **Key Benefits**:

*   Automatic memory management
*   Built-in rate limiting
*   Live progress monitoring
*   Flexible concurrency control

Choose the dispatcher that best fits your needs:

*   **MemoryAdaptiveDispatcher**: For large crawls or limited resources
*   **SemaphoreDispatcher**: For simple, fixed-concurrency scenarios

* * *

---

# Release Summary for Version 0.4.1 (December 8, 2024): Major Efficiency Boosts with New Features! - Crawl4AI Documentation (v0.5.x)

Release Summary for Version 0.4.1 (December 8, 2024): Major Efficiency Boosts with New Features!
================================================================================================

_This post was generated with the help of ChatGPT, take everything with a grain of salt. 🧂_

Hi everyone,

I just finished putting together version 0.4.1 of Crawl4AI, and there are a few changes in here that I think you’ll find really helpful. I’ll explain what’s new, why it matters, and exactly how you can use these features (with the code to back it up). Let’s get into it.

* * *

### Handling Lazy Loading Better (Images Included)

One thing that always bugged me with crawlers is how often they miss lazy-loaded content, especially images. In this version, I made sure Crawl4AI **waits for all images to load** before moving forward. This is useful because many modern websites only load images when they’re in the viewport or after some JavaScript executes.

Here’s how to enable it:

`[](#__codelineno-0-1) await crawler.crawl( [](#__codelineno-0-2)     url="https://example.com", [](#__codelineno-0-3)     wait_for_images=True  # Add this argument to ensure images are fully loaded [](#__codelineno-0-4) )`

What this does is: 1. Waits for the page to reach a "network idle" state. 2. Ensures all images on the page have been completely loaded.

This single change handles the majority of lazy-loading cases you’re likely to encounter.

* * *

### Text-Only Mode (Fast, Lightweight Crawling)

Sometimes, you don’t need to download images or process JavaScript at all. For example, if you’re crawling to extract text data, you can enable **text-only mode** to speed things up. By disabling images, JavaScript, and other heavy resources, this mode makes crawling **3-4 times faster** in most cases.

Here’s how to turn it on:

`[](#__codelineno-1-1) crawler = AsyncPlaywrightCrawlerStrategy( [](#__codelineno-1-2)     text_mode=True  # Set this to True to enable text-only crawling [](#__codelineno-1-3) )`

When `text_mode=True`, the crawler automatically: - Disables GPU processing. - Blocks image and JavaScript resources. - Reduces the viewport size to 800x600 (you can override this with `viewport_width` and `viewport_height`).

If you need to crawl thousands of pages where you only care about text, this mode will save you a ton of time and resources.

* * *

### Adjusting the Viewport Dynamically

Another useful addition is the ability to **dynamically adjust the viewport size** to match the content on the page. This is particularly helpful when you’re working with responsive layouts or want to ensure all parts of the page load properly.

Here’s how it works: 1. The crawler calculates the page’s width and height after it loads. 2. It adjusts the viewport to fit the content dimensions. 3. (Optional) It uses Chrome DevTools Protocol (CDP) to simulate zooming out so everything fits in the viewport.

To enable this, use:

`[](#__codelineno-2-1) await crawler.crawl( [](#__codelineno-2-2)     url="https://example.com", [](#__codelineno-2-3)     adjust_viewport_to_content=True  # Dynamically adjusts the viewport [](#__codelineno-2-4) )`

This approach makes sure the entire page gets loaded into the viewport, especially for layouts that load content based on visibility.

* * *

### Simulating Full-Page Scrolling

Some websites load data dynamically as you scroll down the page. To handle these cases, I added support for **full-page scanning**. It simulates scrolling to the bottom of the page, checking for new content, and capturing it all.

Here’s an example:

`[](#__codelineno-3-1) await crawler.crawl( [](#__codelineno-3-2)     url="https://example.com", [](#__codelineno-3-3)     scan_full_page=True,   # Enables scrolling [](#__codelineno-3-4)     scroll_delay=0.2       # Waits 200ms between scrolls (optional) [](#__codelineno-3-5) )`

What happens here: 1. The crawler scrolls down in increments, waiting for content to load after each scroll. 2. It stops when no new content appears (i.e., dynamic elements stop loading). 3. It scrolls back to the top before finishing (if necessary).

If you’ve ever had to deal with infinite scroll pages, this is going to save you a lot of headaches.

* * *

### Reusing Browser Sessions (Save Time on Setup)

By default, every time you crawl a page, a new browser context (or tab) is created. That’s fine for small crawls, but if you’re working on a large dataset, it’s more efficient to reuse the same session.

I added a method called `create_session` for this:

`[](#__codelineno-4-1) session_id = await crawler.create_session() [](#__codelineno-4-2) [](#__codelineno-4-3) # Use the same session for multiple crawls [](#__codelineno-4-4) await crawler.crawl( [](#__codelineno-4-5)     url="https://example.com/page1", [](#__codelineno-4-6)     session_id=session_id  # Reuse the session [](#__codelineno-4-7) ) [](#__codelineno-4-8) await crawler.crawl( [](#__codelineno-4-9)     url="https://example.com/page2", [](#__codelineno-4-10)     session_id=session_id [](#__codelineno-4-11) )`

This avoids creating a new tab for every page, speeding up the crawl and reducing memory usage.

* * *

### Other Updates

Here are a few smaller updates I’ve made: - **Light Mode**: Use `light_mode=True` to disable background processes, extensions, and other unnecessary features, making the browser more efficient. - **Logging**: Improved logs to make debugging easier. - **Defaults**: Added sensible defaults for things like `delay_before_return_html` (now set to 0.1 seconds).

* * *

### How to Get the Update

You can install or upgrade to version `0.4.1` like this:

`[](#__codelineno-5-1) pip install crawl4ai --upgrade`

As always, I’d love to hear your thoughts. If there’s something you think could be improved or if you have suggestions for future versions, let me know!

Enjoy the new features, and happy crawling! 🕷️

* * *

* * *

---

# arun() - Crawl4AI Documentation (v0.5.x)

`arun()` Parameter Guide (New Approach)
=======================================

In Crawl4AI’s **latest** configuration model, nearly all parameters that once went directly to `arun()` are now part of **`CrawlerRunConfig`**. When calling `arun()`, you provide:

`[](#__codelineno-0-1) await crawler.arun( [](#__codelineno-0-2)     url="https://example.com",   [](#__codelineno-0-3)     config=my_run_config [](#__codelineno-0-4) )`

Below is an organized look at the parameters that can go inside `CrawlerRunConfig`, divided by their functional areas. For **Browser** settings (e.g., `headless`, `browser_type`), see [BrowserConfig](../parameters/)
.

* * *

1. Core Usage
-------------

`[](#__codelineno-1-1) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode [](#__codelineno-1-2) [](#__codelineno-1-3) async def main(): [](#__codelineno-1-4)     run_config = CrawlerRunConfig( [](#__codelineno-1-5)         verbose=True,            # Detailed logging [](#__codelineno-1-6)         cache_mode=CacheMode.ENABLED,  # Use normal read/write cache [](#__codelineno-1-7)         check_robots_txt=True,   # Respect robots.txt rules [](#__codelineno-1-8)         # ... other parameters [](#__codelineno-1-9)     ) [](#__codelineno-1-10) [](#__codelineno-1-11)     async with AsyncWebCrawler() as crawler: [](#__codelineno-1-12)         result = await crawler.arun( [](#__codelineno-1-13)             url="https://example.com", [](#__codelineno-1-14)             config=run_config [](#__codelineno-1-15)         ) [](#__codelineno-1-16) [](#__codelineno-1-17)         # Check if blocked by robots.txt [](#__codelineno-1-18)         if not result.success and result.status_code == 403: [](#__codelineno-1-19)             print(f"Error: {result.error_message}")`

**Key Fields**: - `verbose=True` logs each crawl step.  - `cache_mode` decides how to read/write the local crawl cache.

* * *

2. Cache Control
----------------

**`cache_mode`** (default: `CacheMode.ENABLED`)  
Use a built-in enum from `CacheMode`:

*   `ENABLED`: Normal caching—reads if available, writes if missing.
*   `DISABLED`: No caching—always refetch pages.
*   `READ_ONLY`: Reads from cache only; no new writes.
*   `WRITE_ONLY`: Writes to cache but doesn’t read existing data.
*   `BYPASS`: Skips reading cache for this crawl (though it might still write if set up that way).

`[](#__codelineno-2-1) run_config = CrawlerRunConfig( [](#__codelineno-2-2)     cache_mode=CacheMode.BYPASS [](#__codelineno-2-3) )`

**Additional flags**:

*   `bypass_cache=True` acts like `CacheMode.BYPASS`.
*   `disable_cache=True` acts like `CacheMode.DISABLED`.
*   `no_cache_read=True` acts like `CacheMode.WRITE_ONLY`.
*   `no_cache_write=True` acts like `CacheMode.READ_ONLY`.

* * *

3. Content Processing & Selection
---------------------------------

### 3.1 Text Processing

`[](#__codelineno-3-1) run_config = CrawlerRunConfig( [](#__codelineno-3-2)     word_count_threshold=10,   # Ignore text blocks <10 words [](#__codelineno-3-3)     only_text=False,           # If True, tries to remove non-text elements [](#__codelineno-3-4)     keep_data_attributes=False # Keep or discard data-* attributes [](#__codelineno-3-5) )`

### 3.2 Content Selection

`[](#__codelineno-4-1) run_config = CrawlerRunConfig( [](#__codelineno-4-2)     css_selector=".main-content",  # Focus on .main-content region only [](#__codelineno-4-3)     excluded_tags=["form", "nav"], # Remove entire tag blocks [](#__codelineno-4-4)     remove_forms=True,             # Specifically strip <form> elements [](#__codelineno-4-5)     remove_overlay_elements=True,  # Attempt to remove modals/popups [](#__codelineno-4-6) )`

### 3.3 Link Handling

`[](#__codelineno-5-1) run_config = CrawlerRunConfig( [](#__codelineno-5-2)     exclude_external_links=True,         # Remove external links from final content [](#__codelineno-5-3)     exclude_social_media_links=True,     # Remove links to known social sites [](#__codelineno-5-4)     exclude_domains=["ads.example.com"], # Exclude links to these domains [](#__codelineno-5-5)     exclude_social_media_domains=["facebook.com","twitter.com"], # Extend the default list [](#__codelineno-5-6) )`

### 3.4 Media Filtering

`[](#__codelineno-6-1) run_config = CrawlerRunConfig( [](#__codelineno-6-2)     exclude_external_images=True  # Strip images from other domains [](#__codelineno-6-3) )`

* * *

4. Page Navigation & Timing
---------------------------

### 4.1 Basic Browser Flow

`[](#__codelineno-7-1) run_config = CrawlerRunConfig( [](#__codelineno-7-2)     wait_for="css:.dynamic-content", # Wait for .dynamic-content [](#__codelineno-7-3)     delay_before_return_html=2.0,    # Wait 2s before capturing final HTML [](#__codelineno-7-4)     page_timeout=60000,             # Navigation & script timeout (ms) [](#__codelineno-7-5) )`

**Key Fields**:

*   `wait_for`:
*   `"css:selector"` or
*   `"js:() => boolean"`  
    e.g. `js:() => document.querySelectorAll('.item').length > 10`.
    
*   `mean_delay` & `max_range`: define random delays for `arun_many()` calls. 
    
*   `semaphore_count`: concurrency limit when crawling multiple URLs.

### 4.2 JavaScript Execution

`[](#__codelineno-8-1) run_config = CrawlerRunConfig( [](#__codelineno-8-2)     js_code=[ [](#__codelineno-8-3)         "window.scrollTo(0, document.body.scrollHeight);", [](#__codelineno-8-4)         "document.querySelector('.load-more')?.click();" [](#__codelineno-8-5)     ], [](#__codelineno-8-6)     js_only=False [](#__codelineno-8-7) )`

*   `js_code` can be a single string or a list of strings. 
*   `js_only=True` means “I’m continuing in the same session with new JS steps, no new full navigation.”

### 4.3 Anti-Bot

`[](#__codelineno-9-1) run_config = CrawlerRunConfig( [](#__codelineno-9-2)     magic=True, [](#__codelineno-9-3)     simulate_user=True, [](#__codelineno-9-4)     override_navigator=True [](#__codelineno-9-5) )`

\- `magic=True` tries multiple stealth features.  - `simulate_user=True` mimics mouse movements or random delays.  - `override_navigator=True` fakes some navigator properties (like user agent checks).

* * *

5. Session Management
---------------------

**`session_id`**:

`[](#__codelineno-10-1) run_config = CrawlerRunConfig( [](#__codelineno-10-2)     session_id="my_session123" [](#__codelineno-10-3) )`

If re-used in subsequent `arun()` calls, the same tab/page context is continued (helpful for multi-step tasks or stateful browsing).

* * *

6. Screenshot, PDF & Media Options
----------------------------------

`[](#__codelineno-11-1) run_config = CrawlerRunConfig( [](#__codelineno-11-2)     screenshot=True,             # Grab a screenshot as base64 [](#__codelineno-11-3)     screenshot_wait_for=1.0,     # Wait 1s before capturing [](#__codelineno-11-4)     pdf=True,                    # Also produce a PDF [](#__codelineno-11-5)     image_description_min_word_threshold=5,  # If analyzing alt text [](#__codelineno-11-6)     image_score_threshold=3,                # Filter out low-score images [](#__codelineno-11-7) )`

**Where they appear**: - `result.screenshot` → Base64 screenshot string. - `result.pdf` → Byte array with PDF data.

* * *

7. Extraction Strategy
----------------------

**For advanced data extraction** (CSS/LLM-based), set `extraction_strategy`:

`[](#__codelineno-12-1) run_config = CrawlerRunConfig( [](#__codelineno-12-2)     extraction_strategy=my_css_or_llm_strategy [](#__codelineno-12-3) )`

The extracted data will appear in `result.extracted_content`.

* * *

8. Comprehensive Example
------------------------

Below is a snippet combining many parameters:

`[](#__codelineno-13-1) import asyncio [](#__codelineno-13-2) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode [](#__codelineno-13-3) from crawl4ai.extraction_strategy import JsonCssExtractionStrategy [](#__codelineno-13-4) [](#__codelineno-13-5) async def main(): [](#__codelineno-13-6)     # Example schema [](#__codelineno-13-7)     schema = { [](#__codelineno-13-8)         "name": "Articles", [](#__codelineno-13-9)         "baseSelector": "article.post", [](#__codelineno-13-10)         "fields": [ [](#__codelineno-13-11)             {"name": "title", "selector": "h2", "type": "text"}, [](#__codelineno-13-12)             {"name": "link",  "selector": "a",  "type": "attribute", "attribute": "href"} [](#__codelineno-13-13)         ] [](#__codelineno-13-14)     } [](#__codelineno-13-15) [](#__codelineno-13-16)     run_config = CrawlerRunConfig( [](#__codelineno-13-17)         # Core [](#__codelineno-13-18)         verbose=True, [](#__codelineno-13-19)         cache_mode=CacheMode.ENABLED, [](#__codelineno-13-20)         check_robots_txt=True,   # Respect robots.txt rules [](#__codelineno-13-21) [](#__codelineno-13-22)         # Content [](#__codelineno-13-23)         word_count_threshold=10, [](#__codelineno-13-24)         css_selector="main.content", [](#__codelineno-13-25)         excluded_tags=["nav", "footer"], [](#__codelineno-13-26)         exclude_external_links=True, [](#__codelineno-13-27) [](#__codelineno-13-28)         # Page & JS [](#__codelineno-13-29)         js_code="document.querySelector('.show-more')?.click();", [](#__codelineno-13-30)         wait_for="css:.loaded-block", [](#__codelineno-13-31)         page_timeout=30000, [](#__codelineno-13-32) [](#__codelineno-13-33)         # Extraction [](#__codelineno-13-34)         extraction_strategy=JsonCssExtractionStrategy(schema), [](#__codelineno-13-35) [](#__codelineno-13-36)         # Session [](#__codelineno-13-37)         session_id="persistent_session", [](#__codelineno-13-38) [](#__codelineno-13-39)         # Media [](#__codelineno-13-40)         screenshot=True, [](#__codelineno-13-41)         pdf=True, [](#__codelineno-13-42) [](#__codelineno-13-43)         # Anti-bot [](#__codelineno-13-44)         simulate_user=True, [](#__codelineno-13-45)         magic=True, [](#__codelineno-13-46)     ) [](#__codelineno-13-47) [](#__codelineno-13-48)     async with AsyncWebCrawler() as crawler: [](#__codelineno-13-49)         result = await crawler.arun("https://example.com/posts", config=run_config) [](#__codelineno-13-50)         if result.success: [](#__codelineno-13-51)             print("HTML length:", len(result.cleaned_html)) [](#__codelineno-13-52)             print("Extraction JSON:", result.extracted_content) [](#__codelineno-13-53)             if result.screenshot: [](#__codelineno-13-54)                 print("Screenshot length:", len(result.screenshot)) [](#__codelineno-13-55)             if result.pdf: [](#__codelineno-13-56)                 print("PDF bytes length:", len(result.pdf)) [](#__codelineno-13-57)         else: [](#__codelineno-13-58)             print("Error:", result.error_message) [](#__codelineno-13-59) [](#__codelineno-13-60) if __name__ == "__main__": [](#__codelineno-13-61)     asyncio.run(main())`

**What we covered**:

1. **Crawling** the main content region, ignoring external links.  2. Running **JavaScript** to click “.show-more”.  3. **Waiting** for “.loaded-block” to appear.  4. Generating a **screenshot** & **PDF** of the final page.  5. Extracting repeated “article.post” elements with a **CSS-based** extraction strategy.

* * *

9. Best Practices
-----------------

1. **Use `BrowserConfig` for global browser** settings (headless, user agent).  2. **Use `CrawlerRunConfig`** to handle the **specific** crawl needs: content filtering, caching, JS, screenshot, extraction, etc.  3. Keep your **parameters consistent** in run configs—especially if you’re part of a large codebase with multiple crawls.  4. **Limit** large concurrency (`semaphore_count`) if the site or your system can’t handle it.  5. For dynamic pages, set `js_code` or `scan_full_page` so you load all content.

* * *

10. Conclusion
--------------

All parameters that used to be direct arguments to `arun()` now belong in **`CrawlerRunConfig`**. This approach:

*   Makes code **clearer** and **more maintainable**. 
*   Minimizes confusion about which arguments affect global vs. per-crawl behavior. 
*   Allows you to create **reusable** config objects for different pages or tasks.

For a **full** reference, check out the [CrawlerRunConfig Docs](../parameters/)
. 

Happy crawling with your **structured, flexible** config approach!

* * *

---

# Blog Home - Crawl4AI Documentation (v0.5.x)

Crawl4AI Blog
=============

Welcome to the Crawl4AI blog! Here you'll find detailed release notes, technical insights, and updates about the project. Whether you're looking for the latest improvements or want to dive deep into web crawling techniques, this is the place.

Latest Release
--------------

### [Crawl4AI v0.5.0: Deep Crawling, Scalability, and a New CLI!](releases/0.5.0/)

My dear friends and crawlers, there you go, this is the release of Crawl4AI v0.5.0! This release brings a wealth of new features, performance improvements, and a more streamlined developer experience. Here's a breakdown of what's new:

**Major New Features:**

*   **Deep Crawling:** Explore entire websites with configurable strategies (BFS, DFS, Best-First). Define custom filters and URL scoring for targeted crawls.
*   **Memory-Adaptive Dispatcher:** Handle large-scale crawls with ease! Our new dispatcher dynamically adjusts concurrency based on available memory and includes built-in rate limiting.
*   **Multiple Crawler Strategies:** Choose between the full-featured Playwright browser-based crawler or a new, _much_ faster HTTP-only crawler for simpler tasks.
*   **Docker Deployment:** Deploy Crawl4AI as a scalable, self-contained service with built-in API endpoints and optional JWT authentication.
*   **Command-Line Interface (CLI):** Interact with Crawl4AI directly from your terminal. Crawl, configure, and extract data with simple commands.
*   **LLM Configuration (`LLMConfig`):** A new, unified way to configure LLM providers (OpenAI, Anthropic, Ollama, etc.) for extraction, filtering, and schema generation. Simplifies API key management and switching between models.

**Minor Updates & Improvements:**

*   **LXML Scraping Mode:** Faster HTML parsing with `LXMLWebScrapingStrategy`.
*   **Proxy Rotation:** Added `ProxyRotationStrategy` with a `RoundRobinProxyStrategy` implementation.
*   **PDF Processing:** Extract text, images, and metadata from PDF files.
*   **URL Redirection Tracking:** Automatically follows and records redirects.
*   **Robots.txt Compliance:** Optionally respect website crawling rules.
*   **LLM-Powered Schema Generation:** Automatically create extraction schemas using an LLM.
*   **`LLMContentFilter`:** Generate high-quality, focused markdown using an LLM.
*   **Improved Error Handling & Stability:** Numerous bug fixes and performance enhancements.
*   **Enhanced Documentation:** Updated guides and examples.

**Breaking Changes & Migration:**

This release includes several breaking changes to improve the library's structure and consistency. Here's what you need to know:

*   **`arun_many()` Behavior:** Now uses the `MemoryAdaptiveDispatcher` by default. The return type depends on the `stream` parameter in `CrawlerRunConfig`. Adjust code that relied on unbounded concurrency.
*   **`max_depth` Location:** Moved to `CrawlerRunConfig` and now controls _crawl depth_.
*   **Deep Crawling Imports:** Import `DeepCrawlStrategy` and related classes from `crawl4ai.deep_crawling`.
*   **`BrowserContext` API:** Updated; the old `get_context` method is deprecated.
*   **Optional Model Fields:** Many data model fields are now optional. Handle potential `None` values.
*   **`ScrapingMode` Enum:** Replaced with strategy pattern (`WebScrapingStrategy`, `LXMLWebScrapingStrategy`).
*   **`content_filter` Parameter:** Removed from `CrawlerRunConfig`. Use extraction strategies or markdown generators with filters.
*   **Removed Functionality:** The synchronous `WebCrawler`, the old CLI, and docs management tools have been removed.
*   **Docker:** Significant changes to deployment. See the [Docker documentation](../deploy/docker/README.md)
    .
*   **`ssl_certificate.json`:** This file has been removed.
*   **Config**: FastFilterChain has been replaced with FilterChain
*   **Deep-Crawl**: DeepCrawlStrategy.arun now returns Union\[CrawlResultT, List\[CrawlResultT\], AsyncGenerator\[CrawlResultT, None\]\]
*   **Proxy**: Removed synchronous WebCrawler support and related rate limiting configurations
*   **LLM Parameters:** Use the new `LLMConfig` object instead of passing `provider`, `api_token`, `base_url`, and `api_base` directly to `LLMExtractionStrategy` and `LLMContentFilter`.

**In short:** Update imports, adjust `arun_many()` usage, check for optional fields, and review the Docker deployment guide.

License Change
--------------

Crawl4AI v0.5.0 updates the license to Apache 2.0 _with a required attribution clause_. This means you are free to use, modify, and distribute Crawl4AI (even commercially), but you _must_ clearly attribute the project in any public use or distribution. See the updated `LICENSE` file for the full legal text and specific requirements.

**Get Started:**

*   **Installation:** `pip install "crawl4ai[all]"` (or use the Docker image)
*   **Documentation:** [https://docs.crawl4ai.com](https://docs.crawl4ai.com)
    
*   **GitHub:** [https://github.com/unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)
    

I'm very excited to see what you build with Crawl4AI v0.5.0!

* * *

### [0.4.2 - Configurable Crawlers, Session Management, and Smarter Screenshots](releases/0.4.2/)

_December 12, 2024_

The 0.4.2 update brings massive improvements to configuration, making crawlers and browsers easier to manage with dedicated objects. You can now import/export local storage for seamless session management. Plus, long-page screenshots are faster and cleaner, and full-page PDF exports are now possible. Check out all the new features to make your crawling experience even smoother.

[Read full release notes →](releases/0.4.2/)

* * *

### [0.4.1 - Smarter Crawling with Lazy-Load Handling, Text-Only Mode, and More](releases/0.4.1/)

_December 8, 2024_

This release brings major improvements to handling lazy-loaded images, a blazing-fast Text-Only Mode, full-page scanning for infinite scrolls, dynamic viewport adjustments, and session reuse for efficient crawling. If you're looking to improve speed, reliability, or handle dynamic content with ease, this update has you covered.

[Read full release notes →](releases/0.4.1/)

* * *

### [0.4.0 - Major Content Filtering Update](releases/0.4.0/)

_December 1, 2024_

Introduced significant improvements to content filtering, multi-threaded environment handling, and user-agent generation. This release features the new PruningContentFilter, enhanced thread safety, and improved test coverage.

[Read full release notes →](releases/0.4.0/)

Project History
---------------

Curious about how Crawl4AI has evolved? Check out our [complete changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
 for a detailed history of all versions and updates.

Stay Updated
------------

*   Star us on [GitHub](https://github.com/unclecode/crawl4ai)
    
*   Follow [@unclecode](https://twitter.com/unclecode)
     on Twitter
*   Join our community discussions on GitHub

* * *

---

# Installation 💻 - Crawl4AI Documentation (v0.5.x)

Installation 💻
===============

Crawl4AI offers flexible installation options to suit various use cases. You can install it as a Python package, use it with Docker, or run it as a local server.

Option 1: Python Package Installation (Recommended)
---------------------------------------------------

Crawl4AI is now available on PyPI, making installation easier than ever. Choose the option that best fits your needs:

### Basic Installation

For basic web crawling and scraping tasks:

`[](#__codelineno-0-1) pip install crawl4ai [](#__codelineno-0-2) playwright install # Install Playwright dependencies`

### Installation with PyTorch

For advanced text clustering (includes CosineSimilarity cluster strategy):

`[](#__codelineno-1-1) pip install crawl4ai[torch]`

### Installation with Transformers

For text summarization and Hugging Face models:

`[](#__codelineno-2-1) pip install crawl4ai[transformer]`

### Full Installation

For all features:

`[](#__codelineno-3-1) pip install crawl4ai[all]`

### Development Installation

For contributors who plan to modify the source code:

`[](#__codelineno-4-1) git clone https://github.com/unclecode/crawl4ai.git [](#__codelineno-4-2) cd crawl4ai [](#__codelineno-4-3) pip install -e ".[all]" [](#__codelineno-4-4) playwright install # Install Playwright dependencies`

💡 After installation with "torch", "transformer", or "all" options, it's recommended to run the following CLI command to load the required models:

`[](#__codelineno-5-1) crawl4ai-download-models`

This is optional but will boost the performance and speed of the crawler. You only need to do this once after installation.

Playwright Installation Note for Ubuntu
---------------------------------------

If you encounter issues with Playwright installation on Ubuntu, you may need to install additional dependencies:

`[](#__codelineno-6-1) sudo apt-get install -y \ [](#__codelineno-6-2)     libwoff1 \ [](#__codelineno-6-3)     libopus0 \ [](#__codelineno-6-4)     libwebp7 \ [](#__codelineno-6-5)     libwebpdemux2 \ [](#__codelineno-6-6)     libenchant-2-2 \ [](#__codelineno-6-7)     libgudev-1.0-0 \ [](#__codelineno-6-8)     libsecret-1-0 \ [](#__codelineno-6-9)     libhyphen0 \ [](#__codelineno-6-10)     libgdk-pixbuf2.0-0 \ [](#__codelineno-6-11)     libegl1 \ [](#__codelineno-6-12)     libnotify4 \ [](#__codelineno-6-13)     libxslt1.1 \ [](#__codelineno-6-14)     libevent-2.1-7 \ [](#__codelineno-6-15)     libgles2 \ [](#__codelineno-6-16)     libxcomposite1 \ [](#__codelineno-6-17)     libatk1.0-0 \ [](#__codelineno-6-18)     libatk-bridge2.0-0 \ [](#__codelineno-6-19)     libepoxy0 \ [](#__codelineno-6-20)     libgtk-3-0 \ [](#__codelineno-6-21)     libharfbuzz-icu0 \ [](#__codelineno-6-22)     libgstreamer-gl1.0-0 \ [](#__codelineno-6-23)     libgstreamer-plugins-bad1.0-0 \ [](#__codelineno-6-24)     gstreamer1.0-plugins-good \ [](#__codelineno-6-25)     gstreamer1.0-plugins-bad \ [](#__codelineno-6-26)     libxt6 \ [](#__codelineno-6-27)     libxaw7 \ [](#__codelineno-6-28)     xvfb \ [](#__codelineno-6-29)     fonts-noto-color-emoji \ [](#__codelineno-6-30)     libfontconfig \ [](#__codelineno-6-31)     libfreetype6 \ [](#__codelineno-6-32)     xfonts-cyrillic \ [](#__codelineno-6-33)     xfonts-scalable \ [](#__codelineno-6-34)     fonts-liberation \ [](#__codelineno-6-35)     fonts-ipafont-gothic \ [](#__codelineno-6-36)     fonts-wqy-zenhei \ [](#__codelineno-6-37)     fonts-tlwg-loma-otf \ [](#__codelineno-6-38)     fonts-freefont-ttf`

Option 2: Using Docker (Coming Soon)
------------------------------------

Docker support for Crawl4AI is currently in progress and will be available soon. This will allow you to run Crawl4AI in a containerized environment, ensuring consistency across different systems.

Option 3: Local Server Installation
-----------------------------------

For those who prefer to run Crawl4AI as a local server, instructions will be provided once the Docker implementation is complete.

Verifying Your Installation
---------------------------

After installation, you can verify that Crawl4AI is working correctly by running a simple Python script:

`[](#__codelineno-7-1) import asyncio [](#__codelineno-7-2) from crawl4ai import AsyncWebCrawler [](#__codelineno-7-3) [](#__codelineno-7-4) async def main(): [](#__codelineno-7-5)     async with AsyncWebCrawler(verbose=True) as crawler: [](#__codelineno-7-6)         result = await crawler.arun(url="https://www.example.com") [](#__codelineno-7-7)         print(result.markdown[:500])  # Print first 500 characters [](#__codelineno-7-8) [](#__codelineno-7-9) if __name__ == "__main__": [](#__codelineno-7-10)     asyncio.run(main())`

This script should successfully crawl the example website and print the first 500 characters of the extracted content.

Getting Help
------------

If you encounter any issues during installation or usage, please check the [documentation](https://docs.crawl4ai.com/)
 or raise an issue on the [GitHub repository](https://github.com/unclecode/crawl4ai/issues)
.

Happy crawling! 🕷️🤖

* * *

---

# Browser, Crawler & LLM Config - Crawl4AI Documentation (v0.5.x)

1. **BrowserConfig** – Controlling the Browser
==============================================

`BrowserConfig` focuses on **how** the browser is launched and behaves. This includes headless mode, proxies, user agents, and other environment tweaks.

`[](#__codelineno-0-1) from crawl4ai import AsyncWebCrawler, BrowserConfig [](#__codelineno-0-2) [](#__codelineno-0-3) browser_cfg = BrowserConfig( [](#__codelineno-0-4)     browser_type="chromium", [](#__codelineno-0-5)     headless=True, [](#__codelineno-0-6)     viewport_width=1280, [](#__codelineno-0-7)     viewport_height=720, [](#__codelineno-0-8)     proxy="http://user:pass@proxy:8080", [](#__codelineno-0-9)     user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/116.0.0.0 Safari/537.36", [](#__codelineno-0-10) )`

1.1 Parameter Highlights
------------------------

| **Parameter**                | **Type / Default**                                                   | **What It Does**                                                                                                             |
| ---------------------------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **`browser_type`**           | `"chromium"`, `"firefox"`, `"webkit"`  <br>_(default: `"chromium"`)_ | Which browser engine to use. `"chromium"` is typical for many sites, `"firefox"` or `"webkit"` for specialized tests.        |
| **`headless`**               | `bool` (default: `True`)                                             | Headless means no visible UI. `False` is handy for debugging.                                                                |
| **`viewport_width`**         | `int` (default: `1080`)                                              | Initial page width (in px). Useful for testing responsive layouts.                                                           |
| **`viewport_height`**        | `int` (default: `600`)                                               | Initial page height (in px).                                                                                                 |
| **`proxy`**                  | `str` (default: `None`)                                              | Single-proxy URL if you want all traffic to go through it, e.g. `"http://user:pass@proxy:8080"`.                             |
| **`proxy_config`**           | `dict` (default: `None`)                                             | For advanced or multi-proxy needs, specify details like `{"server": "...", "username": "...", ...}`.                         |
| **`use_persistent_context`** | `bool` (default: `False`)                                            | If `True`, uses a **persistent** browser context (keep cookies, sessions across runs). Also sets `use_managed_browser=True`. |
| **`user_data_dir`**          | `str or None` (default: `None`)                                      | Directory to store user data (profiles, cookies). Must be set if you want permanent sessions.                                |
| **`ignore_https_errors`**    | `bool` (default: `True`)                                             | If `True`, continues despite invalid certificates (common in dev/staging).                                                   |
| **`java_script_enabled`**    | `bool` (default: `True`)                                             | Disable if you want no JS overhead, or if only static content is needed.                                                     |
| **`cookies`**                | `list` (default: `[]`)                                               | Pre-set cookies, each a dict like `{"name": "session", "value": "...", "url": "..."}`.                                       |
| **`headers`**                | `dict` (default: `{}`)                                               | Extra HTTP headers for every request, e.g. `{"Accept-Language": "en-US"}`.                                                   |
| **`user_agent`**             | `str` (default: Chrome-based UA)                                     | Your custom or random user agent. `user_agent_mode="random"` can shuffle it.                                                 |
| **`light_mode`**             | `bool` (default: `False`)                                            | Disables some background features for performance gains.                                                                     |
| **`text_mode`**              | `bool` (default: `False`)                                            | If `True`, tries to disable images/other heavy content for speed.                                                            |
| **`use_managed_browser`**    | `bool` (default: `False`)                                            | For advanced “managed” interactions (debugging, CDP usage). Typically set automatically if persistent context is on.         |
| **`extra_args`**             | `list` (default: `[]`)                                               | Additional flags for the underlying browser process, e.g. `["--disable-extensions"]`.                                        |

**Tips**: - Set `headless=False` to visually **debug** how pages load or how interactions proceed.  
\- If you need **authentication** storage or repeated sessions, consider `use_persistent_context=True` and specify `user_data_dir`.  
\- For large pages, you might need a bigger `viewport_width` and `viewport_height` to handle dynamic content.

* * *

2. **CrawlerRunConfig** – Controlling Each Crawl
================================================

While `BrowserConfig` sets up the **environment**, `CrawlerRunConfig` details **how** each **crawl operation** should behave: caching, content filtering, link or domain blocking, timeouts, JavaScript code, etc.

`[](#__codelineno-1-1) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig [](#__codelineno-1-2) [](#__codelineno-1-3) run_cfg = CrawlerRunConfig( [](#__codelineno-1-4)     wait_for="css:.main-content", [](#__codelineno-1-5)     word_count_threshold=15, [](#__codelineno-1-6)     excluded_tags=["nav", "footer"], [](#__codelineno-1-7)     exclude_external_links=True, [](#__codelineno-1-8)     stream=True,  # Enable streaming for arun_many() [](#__codelineno-1-9) )`

2.1 Parameter Highlights
------------------------

We group them by category.

### A) **Content Processing**

| **Parameter**              | **Type / Default**                   | **What It Does**                                                                                                                                                                                         |
| -------------------------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`word_count_threshold`** | `int` (default: ~200)                | Skips text blocks below X words. Helps ignore trivial sections.                                                                                                                                          |
| **`extraction_strategy`**  | `ExtractionStrategy` (default: None) | If set, extracts structured data (CSS-based, LLM-based, etc.).                                                                                                                                           |
| **`markdown_generator`**   | `MarkdownGenerationStrategy` (None)  | If you want specialized markdown output (citations, filtering, chunking, etc.).                                                                                                                          |
| **`css_selector`**         | `str` (None)                         | Retains only the part of the page matching this selector. Affects the entire extraction process.                                                                                                         |
| **`target_elements`**      | `List[str]` (None)                   | List of CSS selectors for elements to focus on for markdown generation and data extraction, while still processing the entire page for links, media, etc. Provides more flexibility than `css_selector`. |
| **`excluded_tags`**        | `list` (None)                        | Removes entire tags (e.g. `["script", "style"]`).                                                                                                                                                        |
| **`excluded_selector`**    | `str` (None)                         | Like `css_selector` but to exclude. E.g. `"#ads, .tracker"`.                                                                                                                                             |
| **`only_text`**            | `bool` (False)                       | If `True`, tries to extract text-only content.                                                                                                                                                           |
| **`prettiify`**            | `bool` (False)                       | If `True`, beautifies final HTML (slower, purely cosmetic).                                                                                                                                              |
| **`keep_data_attributes`** | `bool` (False)                       | If `True`, preserve `data-*` attributes in cleaned HTML.                                                                                                                                                 |
| **`remove_forms`**         | `bool` (False)                       | If `True`, remove all `<form>` elements.                                                                                                                                                                 |

* * *

### B) **Caching & Session**

| **Parameter**        | **Type / Default**  | **What It Does**                                                                                                     |
| -------------------- | ------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **`cache_mode`**     | `CacheMode or None` | Controls how caching is handled (`ENABLED`, `BYPASS`, `DISABLED`, etc.). If `None`, typically defaults to `ENABLED`. |
| **`session_id`**     | `str or None`       | Assign a unique ID to reuse a single browser session across multiple `arun()` calls.                                 |
| **`bypass_cache`**   | `bool` (False)      | If `True`, acts like `CacheMode.BYPASS`.                                                                             |
| **`disable_cache`**  | `bool` (False)      | If `True`, acts like `CacheMode.DISABLED`.                                                                           |
| **`no_cache_read`**  | `bool` (False)      | If `True`, acts like `CacheMode.WRITE_ONLY` (writes cache but never reads).                                          |
| **`no_cache_write`** | `bool` (False)      | If `True`, acts like `CacheMode.READ_ONLY` (reads cache but never writes).                                           |

Use these for controlling whether you read or write from a local content cache. Handy for large batch crawls or repeated site visits.

* * *

### C) **Page Navigation & Timing**

| **Parameter**                        | **Type / Default**       | **What It Does**                                                                                                       |
| ------------------------------------ | ------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| **`wait_until`**                     | `str` (domcontentloaded) | Condition for navigation to “complete”. Often `"networkidle"` or `"domcontentloaded"`.                                 |
| **`page_timeout`**                   | `int` (60000 ms)         | Timeout for page navigation or JS steps. Increase for slow sites.                                                      |
| **`wait_for`**                       | `str or None`            | Wait for a CSS (`"css:selector"`) or JS (`"js:() => bool"`) condition before content extraction.                       |
| **`wait_for_images`**                | `bool` (False)           | Wait for images to load before finishing. Slows down if you only want text.                                            |
| **`delay_before_return_html`**       | `float` (0.1)            | Additional pause (seconds) before final HTML is captured. Good for last-second updates.                                |
| **`check_robots_txt`**               | `bool` (False)           | Whether to check and respect robots.txt rules before crawling. If True, caches robots.txt for efficiency.              |
| **`mean_delay`** and **`max_range`** | `float` (0.1, 0.3)       | If you call `arun_many()`, these define random delay intervals between crawls, helping avoid detection or rate limits. |
| **`semaphore_count`**                | `int` (5)                | Max concurrency for `arun_many()`. Increase if you have resources for parallel crawls.                                 |

* * *

### D) **Page Interaction**

| **Parameter**                    | **Type / Default**        | **What It Does**                                                                             |
| -------------------------------- | ------------------------- | -------------------------------------------------------------------------------------------- |
| **`js_code`**                    | `str or list[str]` (None) | JavaScript to run after load. E.g. `"document.querySelector('button')?.click();"`.           |
| **`js_only`**                    | `bool` (False)            | If `True`, indicates we’re reusing an existing session and only applying JS. No full reload. |
| **`ignore_body_visibility`**     | `bool` (True)             | Skip checking if `<body>` is visible. Usually best to keep `True`.                           |
| **`scan_full_page`**             | `bool` (False)            | If `True`, auto-scroll the page to load dynamic content (infinite scroll).                   |
| **`scroll_delay`**               | `float` (0.2)             | Delay between scroll steps if `scan_full_page=True`.                                         |
| **`process_iframes`**            | `bool` (False)            | Inlines iframe content for single-page extraction.                                           |
| **`remove_overlay_elements`**    | `bool` (False)            | Removes potential modals/popups blocking the main content.                                   |
| **`simulate_user`**              | `bool` (False)            | Simulate user interactions (mouse movements) to avoid bot detection.                         |
| **`override_navigator`**         | `bool` (False)            | Override `navigator` properties in JS for stealth.                                           |
| **`magic`**                      | `bool` (False)            | Automatic handling of popups/consent banners. Experimental.                                  |
| **`adjust_viewport_to_content`** | `bool` (False)            | Resizes viewport to match page content height.                                               |

If your page is a single-page app with repeated JS updates, set `js_only=True` in subsequent calls, plus a `session_id` for reusing the same tab.

* * *

### E) **Media Handling**

| **Parameter**                              | **Type / Default** | **What It Does**                                                                             |
| ------------------------------------------ | ------------------ | -------------------------------------------------------------------------------------------- |
| **`screenshot`**                           | `bool` (False)     | Capture a screenshot (base64) in `result.screenshot`.                                        |
| **`screenshot_wait_for`**                  | `float or None`    | Extra wait time before the screenshot.                                                       |
| **`screenshot_height_threshold`**          | `int` (~20000)     | If the page is taller than this, alternate screenshot strategies are used.                   |
| **`pdf`**                                  | `bool` (False)     | If `True`, returns a PDF in `result.pdf`.                                                    |
| **`image_description_min_word_threshold`** | `int` (~50)        | Minimum words for an image’s alt text or description to be considered valid.                 |
| **`image_score_threshold`**                | `int` (~3)         | Filter out low-scoring images. The crawler scores images by relevance (size, context, etc.). |
| **`exclude_external_images`**              | `bool` (False)     | Exclude images from other domains.                                                           |

* * *

### F) **Link/Domain Handling**

| **Parameter**                      | **Type / Default**             | **What It Does**                                                                        |
| ---------------------------------- | ------------------------------ | --------------------------------------------------------------------------------------- |
| **`exclude_social_media_domains`** | `list` (e.g. Facebook/Twitter) | A default list can be extended. Any link to these domains is removed from final output. |
| **`exclude_external_links`**       | `bool` (False)                 | Removes all links pointing outside the current domain.                                  |
| **`exclude_social_media_links`**   | `bool` (False)                 | Strips links specifically to social sites (like Facebook or Twitter).                   |
| **`exclude_domains`**              | `list` (\[\])                  | Provide a custom list of domains to exclude (like `["ads.com", "trackers.io"]`).        |

Use these for link-level content filtering (often to keep crawls “internal” or to remove spammy domains).

* * *

### G) **Debug & Logging**

| **Parameter**     | **Type / Default** | **What It Does**                                                           |
| ----------------- | ------------------ | -------------------------------------------------------------------------- |
| **`verbose`**     | `bool` (True)      | Prints logs detailing each step of crawling, interactions, or errors.      |
| **`log_console`** | `bool` (False)     | Logs the page’s JavaScript console output if you want deeper JS debugging. |

* * *

2.2 Helper Methods
------------------

Both `BrowserConfig` and `CrawlerRunConfig` provide a `clone()` method to create modified copies:

`[](#__codelineno-2-1) # Create a base configuration [](#__codelineno-2-2) base_config = CrawlerRunConfig( [](#__codelineno-2-3)     cache_mode=CacheMode.ENABLED, [](#__codelineno-2-4)     word_count_threshold=200 [](#__codelineno-2-5) ) [](#__codelineno-2-6) [](#__codelineno-2-7) # Create variations using clone() [](#__codelineno-2-8) stream_config = base_config.clone(stream=True) [](#__codelineno-2-9) no_cache_config = base_config.clone( [](#__codelineno-2-10)     cache_mode=CacheMode.BYPASS, [](#__codelineno-2-11)     stream=True [](#__codelineno-2-12) )`

The `clone()` method is particularly useful when you need slightly different configurations for different use cases, without modifying the original config.

2.3 Example Usage
-----------------

``[](#__codelineno-3-1) import asyncio [](#__codelineno-3-2) from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode [](#__codelineno-3-3) [](#__codelineno-3-4) async def main(): [](#__codelineno-3-5)     # Configure the browser [](#__codelineno-3-6)     browser_cfg = BrowserConfig( [](#__codelineno-3-7)         headless=False, [](#__codelineno-3-8)         viewport_width=1280, [](#__codelineno-3-9)         viewport_height=720, [](#__codelineno-3-10)         proxy="http://user:pass@myproxy:8080", [](#__codelineno-3-11)         text_mode=True [](#__codelineno-3-12)     ) [](#__codelineno-3-13) [](#__codelineno-3-14)     # Configure the run [](#__codelineno-3-15)     run_cfg = CrawlerRunConfig( [](#__codelineno-3-16)         cache_mode=CacheMode.BYPASS, [](#__codelineno-3-17)         session_id="my_session", [](#__codelineno-3-18)         css_selector="main.article", [](#__codelineno-3-19)         excluded_tags=["script", "style"], [](#__codelineno-3-20)         exclude_external_links=True, [](#__codelineno-3-21)         wait_for="css:.article-loaded", [](#__codelineno-3-22)         screenshot=True, [](#__codelineno-3-23)         stream=True [](#__codelineno-3-24)     ) [](#__codelineno-3-25) [](#__codelineno-3-26)     async with AsyncWebCrawler(config=browser_cfg) as crawler: [](#__codelineno-3-27)         result = await crawler.arun( [](#__codelineno-3-28)             url="https://example.com/news", [](#__codelineno-3-29)             config=run_cfg [](#__codelineno-3-30)         ) [](#__codelineno-3-31)         if result.success: [](#__codelineno-3-32)             print("Final cleaned_html length:", len(result.cleaned_html)) [](#__codelineno-3-33)             if result.screenshot: [](#__codelineno-3-34)                 print("Screenshot captured (base64, length):", len(result.screenshot)) [](#__codelineno-3-35)         else: [](#__codelineno-3-36)             print("Crawl failed:", result.error_message) [](#__codelineno-3-37) [](#__codelineno-3-38) if __name__ == "__main__": [](#__codelineno-3-39)     asyncio.run(main()) [](#__codelineno-3-40) [](#__codelineno-3-41) ## 2.4 Compliance & Ethics [](#__codelineno-3-42) [](#__codelineno-3-43) | **Parameter**          | **Type / Default**      | **What It Does**                                                                                                    | [](#__codelineno-3-44) |-----------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------| [](#__codelineno-3-45) | **`check_robots_txt`**| `bool` (False)          | When True, checks and respects robots.txt rules before crawling. Uses efficient caching with SQLite backend.          | [](#__codelineno-3-46) | **`user_agent`**      | `str` (None)            | User agent string to identify your crawler. Used for robots.txt checking when enabled.                                | [](#__codelineno-3-47) [](#__codelineno-3-48) ```python [](#__codelineno-3-49) run_config = CrawlerRunConfig( [](#__codelineno-3-50)     check_robots_txt=True,  # Enable robots.txt compliance [](#__codelineno-3-51)     user_agent="MyBot/1.0"  # Identify your crawler [](#__codelineno-3-52) )``

3\. **LLMConfig** - Setting up LLM providers
============================================

LLMConfig is useful to pass LLM provider config to strategies and functions that rely on LLMs to do extraction, filtering, schema generation etc. Currently it can be used in the following -

1.  LLMExtractionStrategy
2.  LLMContentFilter
3.  JsonCssExtractionStrategy.generate\_schema
4.  JsonXPathExtractionStrategy.generate\_schema

3.1 Parameters
--------------

| **Parameter**   | **Type / Default**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | **What It Does**                        |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| **`provider`**  | `"ollama/llama3","groq/llama3-70b-8192","groq/llama3-8b-8192", "openai/gpt-4o-mini" ,"openai/gpt-4o","openai/o1-mini","openai/o1-preview","openai/o3-mini","openai/o3-mini-high","anthropic/claude-3-haiku-20240307","anthropic/claude-3-opus-20240229","anthropic/claude-3-sonnet-20240229","anthropic/claude-3-5-sonnet-20240620","gemini/gemini-pro","gemini/gemini-1.5-pro","gemini/gemini-2.0-flash","gemini/gemini-2.0-flash-exp","gemini/gemini-2.0-flash-lite-preview-02-05","deepseek/deepseek-chat"`  <br>_(default: `"openai/gpt-4o-mini"`)_ | Which LLM provoder to use.              |
| **`api_token`** | 1.Optional. When not provided explicitly, api\_token will be read from environment variables based on provider. For example: If a gemini model is passed as provider then,`"GEMINI_API_KEY"` will be read from environment variables  <br>2\. API token of LLM provider  <br>eg: `api_token = "gsk_1ClHGGJ7Lpn4WGybR7vNWGdyb3FY7zXEw3SCiy0BAVM9lL8CQv"`  <br>3\. Environment variable - use with prefix "env:"  <br>eg:`api_token = "env: GROQ_API_KEY"`                                                                                                | API token to use for the given provider |
| **`base_url`**  | Optional. Custom API endpoint                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | If your provider has a custom endpoint  |

3.2 Example Usage
-----------------

`[](#__codelineno-4-1) llm_config = LLMConfig(provider="openai/gpt-4o-mini", api_token=os.getenv("OPENAI_API_KEY"))`

4\. Putting It All Together
---------------------------

*   **Use** `BrowserConfig` for **global** browser settings: engine, headless, proxy, user agent.
*   **Use** `CrawlerRunConfig` for each crawl’s **context**: how to filter content, handle caching, wait for dynamic elements, or run JS.
*   **Pass** both configs to `AsyncWebCrawler` (the `BrowserConfig`) and then to `arun()` (the `CrawlerRunConfig`).
*   **Use** `LLMConfig` for LLM provider configurations that can be used across all extraction, filtering, schema generation tasks. Can be used in - `LLMExtractionStrategy`, `LLMContentFilter`, `JsonCssExtractionStrategy.generate_schema` & `JsonXPathExtractionStrategy.generate_schema`

`[](#__codelineno-5-1) # Create a modified copy with the clone() method [](#__codelineno-5-2) stream_cfg = run_cfg.clone( [](#__codelineno-5-3)     stream=True, [](#__codelineno-5-4)     cache_mode=CacheMode.BYPASS [](#__codelineno-5-5) )`

* * *

---

# AsyncWebCrawler - Crawl4AI Documentation (v0.5.x)

AsyncWebCrawler
===============

The **`AsyncWebCrawler`** is the core class for asynchronous web crawling in Crawl4AI. You typically create it **once**, optionally customize it with a **`BrowserConfig`** (e.g., headless, user agent), then **run** multiple **`arun()`** calls with different **`CrawlerRunConfig`** objects.

**Recommended usage**:

1. **Create** a `BrowserConfig` for global browser settings. 

2. **Instantiate** `AsyncWebCrawler(config=browser_config)`. 

3. **Use** the crawler in an async context manager (`async with`) or manage start/close manually. 

4. **Call** `arun(url, config=crawler_run_config)` for each page you want.

* * *

1. Constructor Overview
-----------------------

`[](#__codelineno-0-1) class AsyncWebCrawler: [](#__codelineno-0-2)     def __init__( [](#__codelineno-0-3)         self, [](#__codelineno-0-4)         crawler_strategy: Optional[AsyncCrawlerStrategy] = None, [](#__codelineno-0-5)         config: Optional[BrowserConfig] = None, [](#__codelineno-0-6)         always_bypass_cache: bool = False,           # deprecated [](#__codelineno-0-7)         always_by_pass_cache: Optional[bool] = None, # also deprecated [](#__codelineno-0-8)         base_directory: str = ..., [](#__codelineno-0-9)         thread_safe: bool = False, [](#__codelineno-0-10)         **kwargs, [](#__codelineno-0-11)     ): [](#__codelineno-0-12)         """ [](#__codelineno-0-13)         Create an AsyncWebCrawler instance. [](#__codelineno-0-14) [](#__codelineno-0-15)         Args: [](#__codelineno-0-16)             crawler_strategy:  [](#__codelineno-0-17)                 (Advanced) Provide a custom crawler strategy if needed. [](#__codelineno-0-18)             config:  [](#__codelineno-0-19)                 A BrowserConfig object specifying how the browser is set up. [](#__codelineno-0-20)             always_bypass_cache:  [](#__codelineno-0-21)                 (Deprecated) Use CrawlerRunConfig.cache_mode instead. [](#__codelineno-0-22)             base_directory:      [](#__codelineno-0-23)                 Folder for storing caches/logs (if relevant). [](#__codelineno-0-24)             thread_safe:  [](#__codelineno-0-25)                 If True, attempts some concurrency safeguards. Usually False. [](#__codelineno-0-26)             **kwargs:  [](#__codelineno-0-27)                 Additional legacy or debugging parameters. [](#__codelineno-0-28)         """ [](#__codelineno-0-29)     ) [](#__codelineno-0-30) [](#__codelineno-0-31) ### Typical Initialization [](#__codelineno-0-32) [](#__codelineno-0-33) ```python [](#__codelineno-0-34) from crawl4ai import AsyncWebCrawler, BrowserConfig [](#__codelineno-0-35) [](#__codelineno-0-36) browser_cfg = BrowserConfig( [](#__codelineno-0-37)     browser_type="chromium", [](#__codelineno-0-38)     headless=True, [](#__codelineno-0-39)     verbose=True [](#__codelineno-0-40) ) [](#__codelineno-0-41) [](#__codelineno-0-42) crawler = AsyncWebCrawler(config=browser_cfg)`

**Notes**:

*   **Legacy** parameters like `always_bypass_cache` remain for backward compatibility, but prefer to set **caching** in `CrawlerRunConfig`.

* * *

2. Lifecycle: Start/Close or Context Manager
--------------------------------------------

### 2.1 Context Manager (Recommended)

`[](#__codelineno-1-1) async with AsyncWebCrawler(config=browser_cfg) as crawler: [](#__codelineno-1-2)     result = await crawler.arun("https://example.com") [](#__codelineno-1-3)     # The crawler automatically starts/closes resources`

When the `async with` block ends, the crawler cleans up (closes the browser, etc.).

### 2.2 Manual Start & Close

`[](#__codelineno-2-1) crawler = AsyncWebCrawler(config=browser_cfg) [](#__codelineno-2-2) await crawler.start() [](#__codelineno-2-3) [](#__codelineno-2-4) result1 = await crawler.arun("https://example.com") [](#__codelineno-2-5) result2 = await crawler.arun("https://another.com") [](#__codelineno-2-6) [](#__codelineno-2-7) await crawler.close()`

Use this style if you have a **long-running** application or need full control of the crawler’s lifecycle.

* * *

3. Primary Method: `arun()`
---------------------------

`[](#__codelineno-3-1) async def arun( [](#__codelineno-3-2)     self, [](#__codelineno-3-3)     url: str, [](#__codelineno-3-4)     config: Optional[CrawlerRunConfig] = None, [](#__codelineno-3-5)     # Legacy parameters for backward compatibility... [](#__codelineno-3-6) ) -> CrawlResult: [](#__codelineno-3-7)     ...`

### 3.1 New Approach

You pass a `CrawlerRunConfig` object that sets up everything about a crawl—content filtering, caching, session reuse, JS code, screenshots, etc.

`[](#__codelineno-4-1) import asyncio [](#__codelineno-4-2) from crawl4ai import CrawlerRunConfig, CacheMode [](#__codelineno-4-3) [](#__codelineno-4-4) run_cfg = CrawlerRunConfig( [](#__codelineno-4-5)     cache_mode=CacheMode.BYPASS, [](#__codelineno-4-6)     css_selector="main.article", [](#__codelineno-4-7)     word_count_threshold=10, [](#__codelineno-4-8)     screenshot=True [](#__codelineno-4-9) ) [](#__codelineno-4-10) [](#__codelineno-4-11) async with AsyncWebCrawler(config=browser_cfg) as crawler: [](#__codelineno-4-12)     result = await crawler.arun("https://example.com/news", config=run_cfg) [](#__codelineno-4-13)     print("Crawled HTML length:", len(result.cleaned_html)) [](#__codelineno-4-14)     if result.screenshot: [](#__codelineno-4-15)         print("Screenshot base64 length:", len(result.screenshot))`

### 3.2 Legacy Parameters Still Accepted

For **backward** compatibility, `arun()` can still accept direct arguments like `css_selector=...`, `word_count_threshold=...`, etc., but we strongly advise migrating them into a **`CrawlerRunConfig`**.

* * *

4. Batch Processing: `arun_many()`
----------------------------------

`[](#__codelineno-5-1) async def arun_many( [](#__codelineno-5-2)     self, [](#__codelineno-5-3)     urls: List[str], [](#__codelineno-5-4)     config: Optional[CrawlerRunConfig] = None, [](#__codelineno-5-5)     # Legacy parameters maintained for backwards compatibility... [](#__codelineno-5-6) ) -> List[CrawlResult]: [](#__codelineno-5-7)     """ [](#__codelineno-5-8)     Process multiple URLs with intelligent rate limiting and resource monitoring. [](#__codelineno-5-9)     """`

### 4.1 Resource-Aware Crawling

The `arun_many()` method now uses an intelligent dispatcher that:

*   Monitors system memory usage
*   Implements adaptive rate limiting
*   Provides detailed progress monitoring
*   Manages concurrent crawls efficiently

### 4.2 Example Usage

Check page [Multi-url Crawling](../../advanced/multi-url-crawling/)
 for a detailed example of how to use `arun_many()`.

``[](#__codelineno-6-1) ### 4.3 Key Features [](#__codelineno-6-2) [](#__codelineno-6-3) 1. **Rate Limiting** [](#__codelineno-6-4) [](#__codelineno-6-5)    - Automatic delay between requests [](#__codelineno-6-6)    - Exponential backoff on rate limit detection [](#__codelineno-6-7)    - Domain-specific rate limiting [](#__codelineno-6-8)    - Configurable retry strategy [](#__codelineno-6-9) [](#__codelineno-6-10) 2. **Resource Monitoring** [](#__codelineno-6-11) [](#__codelineno-6-12)    - Memory usage tracking [](#__codelineno-6-13)    - Adaptive concurrency based on system load [](#__codelineno-6-14)    - Automatic pausing when resources are constrained [](#__codelineno-6-15) [](#__codelineno-6-16) 3. **Progress Monitoring** [](#__codelineno-6-17) [](#__codelineno-6-18)    - Detailed or aggregated progress display [](#__codelineno-6-19)    - Real-time status updates [](#__codelineno-6-20)    - Memory usage statistics [](#__codelineno-6-21) [](#__codelineno-6-22) 4. **Error Handling** [](#__codelineno-6-23) [](#__codelineno-6-24)    - Graceful handling of rate limits [](#__codelineno-6-25)    - Automatic retries with backoff [](#__codelineno-6-26)    - Detailed error reporting [](#__codelineno-6-27) [](#__codelineno-6-28) --- [](#__codelineno-6-29) [](#__codelineno-6-30) ## 5. `CrawlResult` Output [](#__codelineno-6-31) [](#__codelineno-6-32) Each `arun()` returns a **`CrawlResult`** containing: [](#__codelineno-6-33) [](#__codelineno-6-34) - `url`: Final URL (if redirected). [](#__codelineno-6-35) - `html`: Original HTML. [](#__codelineno-6-36) - `cleaned_html`: Sanitized HTML. [](#__codelineno-6-37) - `markdown_v2`: Deprecated. Instead just use regular `markdown` [](#__codelineno-6-38) - `extracted_content`: If an extraction strategy was used (JSON for CSS/LLM strategies). [](#__codelineno-6-39) - `screenshot`, `pdf`: If screenshots/PDF requested. [](#__codelineno-6-40) - `media`, `links`: Information about discovered images/links. [](#__codelineno-6-41) - `success`, `error_message`: Status info. [](#__codelineno-6-42) [](#__codelineno-6-43) For details, see [CrawlResult doc](./crawl-result.md). [](#__codelineno-6-44) [](#__codelineno-6-45) --- [](#__codelineno-6-46) [](#__codelineno-6-47) ## 6. Quick Example [](#__codelineno-6-48) [](#__codelineno-6-49) Below is an example hooking it all together: [](#__codelineno-6-50) [](#__codelineno-6-51) ```python [](#__codelineno-6-52) import asyncio [](#__codelineno-6-53) from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode [](#__codelineno-6-54) from crawl4ai.extraction_strategy import JsonCssExtractionStrategy [](#__codelineno-6-55) import json [](#__codelineno-6-56) [](#__codelineno-6-57) async def main(): [](#__codelineno-6-58)     # 1. Browser config [](#__codelineno-6-59)     browser_cfg = BrowserConfig( [](#__codelineno-6-60)         browser_type="firefox", [](#__codelineno-6-61)         headless=False, [](#__codelineno-6-62)         verbose=True [](#__codelineno-6-63)     ) [](#__codelineno-6-64) [](#__codelineno-6-65)     # 2. Run config [](#__codelineno-6-66)     schema = { [](#__codelineno-6-67)         "name": "Articles", [](#__codelineno-6-68)         "baseSelector": "article.post", [](#__codelineno-6-69)         "fields": [ [](#__codelineno-6-70)             { [](#__codelineno-6-71)                 "name": "title",  [](#__codelineno-6-72)                 "selector": "h2",  [](#__codelineno-6-73)                 "type": "text" [](#__codelineno-6-74)             }, [](#__codelineno-6-75)             { [](#__codelineno-6-76)                 "name": "url",  [](#__codelineno-6-77)                 "selector": "a",  [](#__codelineno-6-78)                 "type": "attribute",  [](#__codelineno-6-79)                 "attribute": "href" [](#__codelineno-6-80)             } [](#__codelineno-6-81)         ] [](#__codelineno-6-82)     } [](#__codelineno-6-83) [](#__codelineno-6-84)     run_cfg = CrawlerRunConfig( [](#__codelineno-6-85)         cache_mode=CacheMode.BYPASS, [](#__codelineno-6-86)         extraction_strategy=JsonCssExtractionStrategy(schema), [](#__codelineno-6-87)         word_count_threshold=15, [](#__codelineno-6-88)         remove_overlay_elements=True, [](#__codelineno-6-89)         wait_for="css:.post"  # Wait for posts to appear [](#__codelineno-6-90)     ) [](#__codelineno-6-91) [](#__codelineno-6-92)     async with AsyncWebCrawler(config=browser_cfg) as crawler: [](#__codelineno-6-93)         result = await crawler.arun( [](#__codelineno-6-94)             url="https://example.com/blog", [](#__codelineno-6-95)             config=run_cfg [](#__codelineno-6-96)         ) [](#__codelineno-6-97) [](#__codelineno-6-98)         if result.success: [](#__codelineno-6-99)             print("Cleaned HTML length:", len(result.cleaned_html)) [](#__codelineno-6-100)             if result.extracted_content: [](#__codelineno-6-101)                 articles = json.loads(result.extracted_content) [](#__codelineno-6-102)                 print("Extracted articles:", articles[:2]) [](#__codelineno-6-103)         else: [](#__codelineno-6-104)             print("Error:", result.error_message) [](#__codelineno-6-105) [](#__codelineno-6-106) asyncio.run(main())``

**Explanation**:

*   We define a **`BrowserConfig`** with Firefox, no headless, and `verbose=True`. 
*   We define a **`CrawlerRunConfig`** that **bypasses cache**, uses a **CSS** extraction schema, has a `word_count_threshold=15`, etc. 
*   We pass them to `AsyncWebCrawler(config=...)` and `arun(url=..., config=...)`.

* * *

7. Best Practices & Migration Notes
-----------------------------------

1. **Use** `BrowserConfig` for **global** settings about the browser’s environment.  2. **Use** `CrawlerRunConfig` for **per-crawl** logic (caching, content filtering, extraction strategies, wait conditions).  3. **Avoid** legacy parameters like `css_selector` or `word_count_threshold` directly in `arun()`. Instead:

`[](#__codelineno-7-1) run_cfg = CrawlerRunConfig(css_selector=".main-content", word_count_threshold=20) [](#__codelineno-7-2) result = await crawler.arun(url="...", config=run_cfg)`

4. **Context Manager** usage is simplest unless you want a persistent crawler across many calls.

* * *

8. Summary
----------

**AsyncWebCrawler** is your entry point to asynchronous crawling:

*   **Constructor** accepts **`BrowserConfig`** (or defaults). 
*   **`arun(url, config=CrawlerRunConfig)`** is the main method for single-page crawls. 
*   **`arun_many(urls, config=CrawlerRunConfig)`** handles concurrency across multiple URLs. 
*   For advanced lifecycle control, use `start()` and `close()` explicitly. 

**Migration**:

*   If you used `AsyncWebCrawler(browser_type="chromium", css_selector="...")`, move browser settings to `BrowserConfig(...)` and content/crawl logic to `CrawlerRunConfig(...)`.

This modular approach ensures your code is **clean**, **scalable**, and **easy to maintain**. For any advanced or rarely used parameters, see the [BrowserConfig docs](../parameters/)
.

* * *

---

# 0.4.2 - Crawl4AI Documentation (v0.5.x)

🚀 Crawl4AI 0.4.2 Update: Smarter Crawling Just Got Easier (Dec 12, 2024)
-------------------------------------------------------------------------

### Hey Developers,

I’m excited to share Crawl4AI 0.4.2—a major upgrade that makes crawling smarter, faster, and a whole lot more intuitive. I’ve packed in a bunch of new features to simplify your workflows and improve your experience. Let’s cut to the chase!

* * *

### 🔧 **Configurable Browser and Crawler Behavior**

You’ve asked for better control over how browsers and crawlers are configured, and now you’ve got it. With the new `BrowserConfig` and `CrawlerRunConfig` objects, you can set up your browser and crawling behavior exactly how you want. No more cluttering `arun` with a dozen arguments—just pass in your configs and go.

**Example:**

`[](#__codelineno-0-1) from crawl4ai import BrowserConfig, CrawlerRunConfig, AsyncWebCrawler [](#__codelineno-0-2) [](#__codelineno-0-3) browser_config = BrowserConfig(headless=True, viewport_width=1920, viewport_height=1080) [](#__codelineno-0-4) crawler_config = CrawlerRunConfig(cache_mode="BYPASS") [](#__codelineno-0-5) [](#__codelineno-0-6) async with AsyncWebCrawler(config=browser_config) as crawler: [](#__codelineno-0-7)     result = await crawler.arun(url="https://example.com", config=crawler_config) [](#__codelineno-0-8)     print(result.markdown[:500])`

This setup is a game-changer for scalability, keeping your code clean and flexible as we add more parameters in the future.

Remember: If you like to use the old way, you can still pass arguments directly to `arun` as before, no worries!

* * *

### 🔐 **Streamlined Session Management**

Here’s the big one: You can now pass local storage and cookies directly. Whether it’s setting values programmatically or importing a saved JSON state, managing sessions has never been easier. This is a must-have for authenticated crawls—just export your storage state once and reuse it effortlessly across runs.

**Example:** 1. Open a browser, log in manually, and export the storage state. 2. Import the JSON file for seamless authenticated crawling:

`[](#__codelineno-1-1) result = await crawler.arun( [](#__codelineno-1-2)     url="https://example.com/protected", [](#__codelineno-1-3)     storage_state="my_storage_state.json" [](#__codelineno-1-4) )`

* * *

### 🔢 **Handling Large Pages: Supercharged Screenshots and PDF Conversion**

Two big upgrades here:

*   **Blazing-fast long-page screenshots**: Turn extremely long web pages into clean, high-quality screenshots—without breaking a sweat. It’s optimized to handle large content without lag.
    
*   **Full-page PDF exports**: Now, you can also convert any page into a PDF with all the details intact. Perfect for archiving or sharing complex layouts.
    

* * *

### 🔧 **Other Cool Stuff**

*   **Anti-bot enhancements**: Magic mode now handles overlays, user simulation, and anti-detection features like a pro.
*   **JavaScript execution**: Execute custom JS snippets to handle dynamic content. No more wrestling with endless page interactions.

* * *

### 📊 **Performance Boosts and Dev-friendly Updates**

*   Faster rendering and viewport adjustments for better performance.
*   Improved cookie and local storage handling for seamless authentication.
*   Better debugging with detailed logs and actionable error messages.

* * *

### 🔠 **Use Cases You’ll Love**

1. **Authenticated Crawls**: Login once, export your storage state, and reuse it across multiple requests without the headache. 2. **Long-page Screenshots**: Perfect for blogs, e-commerce pages, or any endless-scroll website. 3. **PDF Export**: Create professional-looking page PDFs in seconds.

* * *

### Let’s Get Crawling

Crawl4AI 0.4.2 is ready for you to download and try. I’m always looking for ways to improve, so don’t hold back—share your thoughts and feedback.

Happy Crawling! 🚀

* * *

---

# Crawl4AI 0.4.3: Major Performance Boost & LLM Integration - Crawl4AI Documentation (v0.5.x)

Crawl4AI 0.4.3: Major Performance Boost & LLM Integration
=========================================================

We're excited to announce Crawl4AI 0.4.3, focusing on three key areas: Speed & Efficiency, LLM Integration, and Core Platform Improvements. This release significantly improves crawling performance while adding powerful new LLM-powered features.

⚡ Speed & Efficiency Improvements
---------------------------------

### 1\. Memory-Adaptive Dispatcher System

The new dispatcher system provides intelligent resource management and real-time monitoring:

`[](#__codelineno-0-1) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, DisplayMode [](#__codelineno-0-2) from crawl4ai.async_dispatcher import MemoryAdaptiveDispatcher, CrawlerMonitor [](#__codelineno-0-3) [](#__codelineno-0-4) async def main(): [](#__codelineno-0-5)     urls = ["https://example1.com", "https://example2.com"] * 50 [](#__codelineno-0-6) [](#__codelineno-0-7)     # Configure memory-aware dispatch [](#__codelineno-0-8)     dispatcher = MemoryAdaptiveDispatcher( [](#__codelineno-0-9)         memory_threshold_percent=80.0,  # Auto-throttle at 80% memory [](#__codelineno-0-10)         check_interval=0.5,             # Check every 0.5 seconds [](#__codelineno-0-11)         max_session_permit=20,          # Max concurrent sessions [](#__codelineno-0-12)         monitor=CrawlerMonitor(         # Real-time monitoring [](#__codelineno-0-13)             display_mode=DisplayMode.DETAILED [](#__codelineno-0-14)         ) [](#__codelineno-0-15)     ) [](#__codelineno-0-16) [](#__codelineno-0-17)     async with AsyncWebCrawler() as crawler: [](#__codelineno-0-18)         results = await dispatcher.run_urls( [](#__codelineno-0-19)             urls=urls, [](#__codelineno-0-20)             crawler=crawler, [](#__codelineno-0-21)             config=CrawlerRunConfig() [](#__codelineno-0-22)         )`

### 2\. Streaming Support

Process crawled URLs in real-time instead of waiting for all results:

`[](#__codelineno-1-1) config = CrawlerRunConfig(stream=True) [](#__codelineno-1-2) [](#__codelineno-1-3) async with AsyncWebCrawler() as crawler: [](#__codelineno-1-4)     async for result in await crawler.arun_many(urls, config=config): [](#__codelineno-1-5)         print(f"Got result for {result.url}") [](#__codelineno-1-6)         # Process each result immediately`

### 3\. LXML-Based Scraping

New LXML scraping strategy offering up to 20x faster parsing:

`[](#__codelineno-2-1) config = CrawlerRunConfig( [](#__codelineno-2-2)     scraping_strategy=LXMLWebScrapingStrategy(), [](#__codelineno-2-3)     cache_mode=CacheMode.ENABLED [](#__codelineno-2-4) )`

🤖 LLM Integration
------------------

### 1\. LLM-Powered Markdown Generation

Smart content filtering and organization using LLMs:

`[](#__codelineno-3-1) config = CrawlerRunConfig( [](#__codelineno-3-2)     markdown_generator=DefaultMarkdownGenerator( [](#__codelineno-3-3)         content_filter=LLMContentFilter( [](#__codelineno-3-4)             provider="openai/gpt-4o", [](#__codelineno-3-5)             instruction="Extract technical documentation and code examples" [](#__codelineno-3-6)         ) [](#__codelineno-3-7)     ) [](#__codelineno-3-8) )`

### 2\. Automatic Schema Generation

Generate extraction schemas instantly using LLMs instead of manual CSS/XPath writing:

`[](#__codelineno-4-1) schema = JsonCssExtractionStrategy.generate_schema( [](#__codelineno-4-2)     html_content, [](#__codelineno-4-3)     schema_type="CSS", [](#__codelineno-4-4)     query="Extract product name, price, and description" [](#__codelineno-4-5) )`

🔧 Core Improvements
--------------------

### 1\. Proxy Support & Rotation

Integrated proxy support with automatic rotation and verification:

`[](#__codelineno-5-1) config = CrawlerRunConfig( [](#__codelineno-5-2)     proxy_config={ [](#__codelineno-5-3)         "server": "http://proxy:8080", [](#__codelineno-5-4)         "username": "user", [](#__codelineno-5-5)         "password": "pass" [](#__codelineno-5-6)     } [](#__codelineno-5-7) )`

### 2\. Robots.txt Compliance

Built-in robots.txt support with SQLite caching:

`[](#__codelineno-6-1) config = CrawlerRunConfig(check_robots_txt=True) [](#__codelineno-6-2) result = await crawler.arun(url, config=config) [](#__codelineno-6-3) if result.status_code == 403: [](#__codelineno-6-4)     print("Access blocked by robots.txt")`

### 3\. URL Redirection Tracking

Track final URLs after redirects:

`[](#__codelineno-7-1) result = await crawler.arun(url) [](#__codelineno-7-2) print(f"Initial URL: {url}") [](#__codelineno-7-3) print(f"Final URL: {result.redirected_url}")`

Performance Impact
------------------

*   Memory usage reduced by up to 40% with adaptive dispatcher
*   Parsing speed increased up to 20x with LXML strategy
*   Streaming reduces memory footprint for large crawls by ~60%

Getting Started
---------------

`[](#__codelineno-8-1) pip install -U crawl4ai`

For complete examples, check our [demo repository](https://github.com/unclecode/crawl4ai/examples)
.

Stay Connected
--------------

*   Star us on [GitHub](https://github.com/unclecode/crawl4ai)
    
*   Follow [@unclecode](https://twitter.com/unclecode)
    
*   Join our [Discord](https://discord.gg/crawl4ai)
    

Happy crawling! 🕷️

* * *

---

# Browser, Crawler & LLM Config - Crawl4AI Documentation (v0.5.x)

Browser, Crawler & LLM Configuration (Quick Overview)
=====================================================

Crawl4AI’s flexibility stems from two key classes:

1. **`BrowserConfig`** – Dictates **how** the browser is launched and behaves (e.g., headless or visible, proxy, user agent).  
2. **`CrawlerRunConfig`** – Dictates **how** each **crawl** operates (e.g., caching, extraction, timeouts, JavaScript code to run, etc.).  
3\. **`LLMConfig`** - Dictates **how** LLM providers are configured. (model, api token, base url, temperature etc.)

In most examples, you create **one** `BrowserConfig` for the entire crawler session, then pass a **fresh** or re-used `CrawlerRunConfig` whenever you call `arun()`. This tutorial shows the most commonly used parameters. If you need advanced or rarely used fields, see the [Configuration Parameters](../../api/parameters/)
.

* * *

1\. BrowserConfig Essentials
----------------------------

`[](#__codelineno-0-1) class BrowserConfig: [](#__codelineno-0-2)     def __init__( [](#__codelineno-0-3)         browser_type="chromium", [](#__codelineno-0-4)         headless=True, [](#__codelineno-0-5)         proxy_config=None, [](#__codelineno-0-6)         viewport_width=1080, [](#__codelineno-0-7)         viewport_height=600, [](#__codelineno-0-8)         verbose=True, [](#__codelineno-0-9)         use_persistent_context=False, [](#__codelineno-0-10)         user_data_dir=None, [](#__codelineno-0-11)         cookies=None, [](#__codelineno-0-12)         headers=None, [](#__codelineno-0-13)         user_agent=None, [](#__codelineno-0-14)         text_mode=False, [](#__codelineno-0-15)         light_mode=False, [](#__codelineno-0-16)         extra_args=None, [](#__codelineno-0-17)         # ... other advanced parameters omitted here [](#__codelineno-0-18)     ): [](#__codelineno-0-19)         ...`

### Key Fields to Note

1. **`browser_type`**  
\- Options: `"chromium"`, `"firefox"`, or `"webkit"`.  
\- Defaults to `"chromium"`.  
\- If you need a different engine, specify it here.

2. **`headless`**  
\- `True`: Runs the browser in headless mode (invisible browser).  
\- `False`: Runs the browser in visible mode, which helps with debugging.

3. **`proxy_config`**  
\- A dictionary with fields like:  

`[](#__codelineno-1-1) { [](#__codelineno-1-2)     "server": "http://proxy.example.com:8080",  [](#__codelineno-1-3)     "username": "...",  [](#__codelineno-1-4)     "password": "..." [](#__codelineno-1-5) }`

\- Leave as `None` if a proxy is not required.

4. **`viewport_width` & `viewport_height`**:  
\- The initial window size.  
\- Some sites behave differently with smaller or bigger viewports.

5. **`verbose`**:  
\- If `True`, prints extra logs.  
\- Handy for debugging.

6. **`use_persistent_context`**:  
\- If `True`, uses a **persistent** browser profile, storing cookies/local storage across runs.  
\- Typically also set `user_data_dir` to point to a folder.

7. **`cookies`** & **`headers`**:  
\- If you want to start with specific cookies or add universal HTTP headers, set them here.  
\- E.g. `cookies=[{"name": "session", "value": "abc123", "domain": "example.com"}]`.

8. **`user_agent`**:  
\- Custom User-Agent string. If `None`, a default is used.  
\- You can also set `user_agent_mode="random"` for randomization (if you want to fight bot detection).

9. **`text_mode`** & **`light_mode`**:  
\- `text_mode=True` disables images, possibly speeding up text-only crawls.  
\- `light_mode=True` turns off certain background features for performance.

10. **`extra_args`**:  
\- Additional flags for the underlying browser.  
\- E.g. `["--disable-extensions"]`.

### Helper Methods

Both configuration classes provide a `clone()` method to create modified copies:

`[](#__codelineno-2-1) # Create a base browser config [](#__codelineno-2-2) base_browser = BrowserConfig( [](#__codelineno-2-3)     browser_type="chromium", [](#__codelineno-2-4)     headless=True, [](#__codelineno-2-5)     text_mode=True [](#__codelineno-2-6) ) [](#__codelineno-2-7) [](#__codelineno-2-8) # Create a visible browser config for debugging [](#__codelineno-2-9) debug_browser = base_browser.clone( [](#__codelineno-2-10)     headless=False, [](#__codelineno-2-11)     verbose=True [](#__codelineno-2-12) )`

**Minimal Example**:

`[](#__codelineno-3-1) from crawl4ai import AsyncWebCrawler, BrowserConfig [](#__codelineno-3-2) [](#__codelineno-3-3) browser_conf = BrowserConfig( [](#__codelineno-3-4)     browser_type="firefox", [](#__codelineno-3-5)     headless=False, [](#__codelineno-3-6)     text_mode=True [](#__codelineno-3-7) ) [](#__codelineno-3-8) [](#__codelineno-3-9) async with AsyncWebCrawler(config=browser_conf) as crawler: [](#__codelineno-3-10)     result = await crawler.arun("https://example.com") [](#__codelineno-3-11)     print(result.markdown[:300])`

* * *

2\. CrawlerRunConfig Essentials
-------------------------------

`[](#__codelineno-4-1) class CrawlerRunConfig: [](#__codelineno-4-2)     def __init__( [](#__codelineno-4-3)         word_count_threshold=200, [](#__codelineno-4-4)         extraction_strategy=None, [](#__codelineno-4-5)         markdown_generator=None, [](#__codelineno-4-6)         cache_mode=None, [](#__codelineno-4-7)         js_code=None, [](#__codelineno-4-8)         wait_for=None, [](#__codelineno-4-9)         screenshot=False, [](#__codelineno-4-10)         pdf=False, [](#__codelineno-4-11)         enable_rate_limiting=False, [](#__codelineno-4-12)         rate_limit_config=None, [](#__codelineno-4-13)         memory_threshold_percent=70.0, [](#__codelineno-4-14)         check_interval=1.0, [](#__codelineno-4-15)         max_session_permit=20, [](#__codelineno-4-16)         display_mode=None, [](#__codelineno-4-17)         verbose=True, [](#__codelineno-4-18)         stream=False,  # Enable streaming for arun_many() [](#__codelineno-4-19)         # ... other advanced parameters omitted [](#__codelineno-4-20)     ): [](#__codelineno-4-21)         ...`

### Key Fields to Note

1. **`word_count_threshold`**:  
\- The minimum word count before a block is considered.  
\- If your site has lots of short paragraphs or items, you can lower it.

2. **`extraction_strategy`**:  
\- Where you plug in JSON-based extraction (CSS, LLM, etc.).  
\- If `None`, no structured extraction is done (only raw/cleaned HTML + markdown).

3. **`markdown_generator`**:  
\- E.g., `DefaultMarkdownGenerator(...)`, controlling how HTML→Markdown conversion is done.  
\- If `None`, a default approach is used.

4. **`cache_mode`**:  
\- Controls caching behavior (`ENABLED`, `BYPASS`, `DISABLED`, etc.).  
\- If `None`, defaults to some level of caching or you can specify `CacheMode.ENABLED`.

5. **`js_code`**:  
\- A string or list of JS strings to execute.  
\- Great for “Load More” buttons or user interactions.

6. **`wait_for`**:  
\- A CSS or JS expression to wait for before extracting content.  
\- Common usage: `wait_for="css:.main-loaded"` or `wait_for="js:() => window.loaded === true"`.

7. **`screenshot`** & **`pdf`**:  
\- If `True`, captures a screenshot or PDF after the page is fully loaded.  
\- The results go to `result.screenshot` (base64) or `result.pdf` (bytes).

8. **`verbose`**:  
\- Logs additional runtime details.  
\- Overlaps with the browser’s verbosity if also set to `True` in `BrowserConfig`.

9. **`enable_rate_limiting`**:  
\- If `True`, enables rate limiting for batch processing.  
\- Requires `rate_limit_config` to be set.

10. **`memory_threshold_percent`**:  
\- The memory threshold (as a percentage) to monitor.  
\- If exceeded, the crawler will pause or slow down.

11. **`check_interval`**:  
\- The interval (in seconds) to check system resources.  
\- Affects how often memory and CPU usage are monitored.

12. **`max_session_permit`**:  
\- The maximum number of concurrent crawl sessions.  
\- Helps prevent overwhelming the system.

13. **`display_mode`**:  
\- The display mode for progress information (`DETAILED`, `BRIEF`, etc.).  
\- Affects how much information is printed during the crawl.

### Helper Methods

The `clone()` method is particularly useful for creating variations of your crawler configuration:

`[](#__codelineno-5-1) # Create a base configuration [](#__codelineno-5-2) base_config = CrawlerRunConfig( [](#__codelineno-5-3)     cache_mode=CacheMode.ENABLED, [](#__codelineno-5-4)     word_count_threshold=200, [](#__codelineno-5-5)     wait_until="networkidle" [](#__codelineno-5-6) ) [](#__codelineno-5-7) [](#__codelineno-5-8) # Create variations for different use cases [](#__codelineno-5-9) stream_config = base_config.clone( [](#__codelineno-5-10)     stream=True,  # Enable streaming mode [](#__codelineno-5-11)     cache_mode=CacheMode.BYPASS [](#__codelineno-5-12) ) [](#__codelineno-5-13) [](#__codelineno-5-14) debug_config = base_config.clone( [](#__codelineno-5-15)     page_timeout=120000,  # Longer timeout for debugging [](#__codelineno-5-16)     verbose=True [](#__codelineno-5-17) )`

The `clone()` method: - Creates a new instance with all the same settings - Updates only the specified parameters - Leaves the original configuration unchanged - Perfect for creating variations without repeating all parameters

* * *

3\. LLMConfig Essentials
------------------------

### Key fields to note

1. **`provider`**:  
\- Which LLM provoder to use. - Possible values are `"ollama/llama3","groq/llama3-70b-8192","groq/llama3-8b-8192", "openai/gpt-4o-mini" ,"openai/gpt-4o","openai/o1-mini","openai/o1-preview","openai/o3-mini","openai/o3-mini-high","anthropic/claude-3-haiku-20240307","anthropic/claude-3-opus-20240229","anthropic/claude-3-sonnet-20240229","anthropic/claude-3-5-sonnet-20240620","gemini/gemini-pro","gemini/gemini-1.5-pro","gemini/gemini-2.0-flash","gemini/gemini-2.0-flash-exp","gemini/gemini-2.0-flash-lite-preview-02-05","deepseek/deepseek-chat"`  
_(default: `"openai/gpt-4o-mini"`)_

2. **`api_token`**:  
\- Optional. When not provided explicitly, api\_token will be read from environment variables based on provider. For example: If a gemini model is passed as provider then,`"GEMINI_API_KEY"` will be read from environment variables  
\- API token of LLM provider  
eg: `api_token = "gsk_1ClHGGJ7Lpn4WGybR7vNWGdyb3FY7zXEw3SCiy0BAVM9lL8CQv"` - Environment variable - use with prefix "env:"  
eg:`api_token = "env: GROQ_API_KEY"`

3. **`base_url`**:  
\- If your provider has a custom endpoint

`[](#__codelineno-6-1) llm_config = LLMConfig(provider="openai/gpt-4o-mini", api_token=os.getenv("OPENAI_API_KEY"))`

4\. Putting It All Together
---------------------------

In a typical scenario, you define **one** `BrowserConfig` for your crawler session, then create **one or more** `CrawlerRunConfig` & `LLMConfig` depending on each call’s needs:

`[](#__codelineno-7-1) import asyncio [](#__codelineno-7-2) from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode, LLMConfig [](#__codelineno-7-3) from crawl4ai.extraction_strategy import JsonCssExtractionStrategy [](#__codelineno-7-4) [](#__codelineno-7-5) async def main(): [](#__codelineno-7-6)     # 1) Browser config: headless, bigger viewport, no proxy [](#__codelineno-7-7)     browser_conf = BrowserConfig( [](#__codelineno-7-8)         headless=True, [](#__codelineno-7-9)         viewport_width=1280, [](#__codelineno-7-10)         viewport_height=720 [](#__codelineno-7-11)     ) [](#__codelineno-7-12) [](#__codelineno-7-13)     # 2) Example extraction strategy [](#__codelineno-7-14)     schema = { [](#__codelineno-7-15)         "name": "Articles", [](#__codelineno-7-16)         "baseSelector": "div.article", [](#__codelineno-7-17)         "fields": [ [](#__codelineno-7-18)             {"name": "title", "selector": "h2", "type": "text"}, [](#__codelineno-7-19)             {"name": "link", "selector": "a", "type": "attribute", "attribute": "href"} [](#__codelineno-7-20)         ] [](#__codelineno-7-21)     } [](#__codelineno-7-22)     extraction = JsonCssExtractionStrategy(schema) [](#__codelineno-7-23) [](#__codelineno-7-24)     # 3) Example LLM content filtering [](#__codelineno-7-25) [](#__codelineno-7-26)     gemini_config = LLMConfig( [](#__codelineno-7-27)         provider="gemini/gemini-1.5-pro"  [](#__codelineno-7-28)         api_token = "env:GEMINI_API_TOKEN" [](#__codelineno-7-29)     ) [](#__codelineno-7-30) [](#__codelineno-7-31)     # Initialize LLM filter with specific instruction [](#__codelineno-7-32)     filter = LLMContentFilter( [](#__codelineno-7-33)         llm_config=gemini_config,  # or your preferred provider [](#__codelineno-7-34)         instruction=""" [](#__codelineno-7-35)         Focus on extracting the core educational content. [](#__codelineno-7-36)         Include: [](#__codelineno-7-37)         - Key concepts and explanations [](#__codelineno-7-38)         - Important code examples [](#__codelineno-7-39)         - Essential technical details [](#__codelineno-7-40)         Exclude: [](#__codelineno-7-41)         - Navigation elements [](#__codelineno-7-42)         - Sidebars [](#__codelineno-7-43)         - Footer content [](#__codelineno-7-44)         Format the output as clean markdown with proper code blocks and headers. [](#__codelineno-7-45)         """, [](#__codelineno-7-46)         chunk_token_threshold=500,  # Adjust based on your needs [](#__codelineno-7-47)         verbose=True [](#__codelineno-7-48)     ) [](#__codelineno-7-49) [](#__codelineno-7-50)     md_generator = DefaultMarkdownGenerator( [](#__codelineno-7-51)     content_filter=filter, [](#__codelineno-7-52)     options={"ignore_links": True} [](#__codelineno-7-53) [](#__codelineno-7-54)     # 4) Crawler run config: skip cache, use extraction [](#__codelineno-7-55)     run_conf = CrawlerRunConfig( [](#__codelineno-7-56)         markdown_generator=md_generator, [](#__codelineno-7-57)         extraction_strategy=extraction, [](#__codelineno-7-58)         cache_mode=CacheMode.BYPASS, [](#__codelineno-7-59)     ) [](#__codelineno-7-60) [](#__codelineno-7-61)     async with AsyncWebCrawler(config=browser_conf) as crawler: [](#__codelineno-7-62)         # 4) Execute the crawl [](#__codelineno-7-63)         result = await crawler.arun(url="https://example.com/news", config=run_conf) [](#__codelineno-7-64) [](#__codelineno-7-65)         if result.success: [](#__codelineno-7-66)             print("Extracted content:", result.extracted_content) [](#__codelineno-7-67)         else: [](#__codelineno-7-68)             print("Error:", result.error_message) [](#__codelineno-7-69) [](#__codelineno-7-70) if __name__ == "__main__": [](#__codelineno-7-71)     asyncio.run(main())`

* * *

5\. Next Steps
--------------

For a **detailed list** of available parameters (including advanced ones), see:

*   [BrowserConfig, CrawlerRunConfig & LLMConfig Reference](../../api/parameters/)
    

You can explore topics like:

*   **Custom Hooks & Auth** (Inject JavaScript or handle login forms).
*   **Session Management** (Re-use pages, preserve state across multiple calls).
*   **Magic Mode** or **Identity-based Crawling** (Fight bot detection by simulating user behavior).
*   **Advanced Caching** (Fine-tune read/write cache modes).

* * *

6\. Conclusion
--------------

**BrowserConfig**, **CrawlerRunConfig** and **LLMConfig** give you straightforward ways to define:

*   **Which** browser to launch, how it should run, and any proxy or user agent needs.
*   **How** each crawl should behave—caching, timeouts, JavaScript code, extraction strategies, etc.
*   **Which** LLM provider to use, api token, temperature and base url for custom endpoints

Use them together for **clear, maintainable** code, and when you need more specialized behavior, check out the advanced parameters in the [reference docs](../../api/parameters/)
. Happy crawling!

* * *

---

# Crawl4AI v0.5.0 Release Notes - Crawl4AI Documentation (v0.5.x)

Crawl4AI v0.5.0 Release Notes
=============================

**Release Theme: Power, Flexibility, and Scalability**

Crawl4AI v0.5.0 is a major release focused on significantly enhancing the library's power, flexibility, and scalability. Key improvements include a new **deep crawling** system, a **memory-adaptive dispatcher** for handling large-scale crawls, **multiple crawling strategies** (including a fast HTTP-only crawler), **Docker** deployment options, and a powerful **command-line interface (CLI)**. This release also includes numerous bug fixes, performance optimizations, and documentation updates.

**Important Note:** This release contains several **breaking changes**. Please review the "Breaking Changes" section carefully and update your code accordingly.

Key Features
------------

### 1\. Deep Crawling

Crawl4AI now supports deep crawling, allowing you to explore websites beyond the initial URLs. This is controlled by the `deep_crawl_strategy` parameter in `CrawlerRunConfig`. Several strategies are available:

*   **`BFSDeepCrawlStrategy` (Breadth-First Search):** Explores the website level by level. (Default)
*   **`DFSDeepCrawlStrategy` (Depth-First Search):** Explores each branch as deeply as possible before backtracking.
*   **`BestFirstCrawlingStrategy`:** Uses a scoring function to prioritize which URLs to crawl next.

`[](#__codelineno-0-1) import time [](#__codelineno-0-2) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, BFSDeepCrawlStrategy [](#__codelineno-0-3) from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy [](#__codelineno-0-4) from crawl4ai.deep_crawling import DomainFilter, ContentTypeFilter, FilterChain, URLPatternFilter, KeywordRelevanceScorer, BestFirstCrawlingStrategy [](#__codelineno-0-5) import asyncio [](#__codelineno-0-6) [](#__codelineno-0-7) # Create a filter chain to filter urls based on patterns, domains and content type [](#__codelineno-0-8) filter_chain = FilterChain( [](#__codelineno-0-9)     [ [](#__codelineno-0-10)         DomainFilter( [](#__codelineno-0-11)             allowed_domains=["docs.crawl4ai.com"], [](#__codelineno-0-12)             blocked_domains=["old.docs.crawl4ai.com"], [](#__codelineno-0-13)         ), [](#__codelineno-0-14)         URLPatternFilter(patterns=["*core*", "*advanced*"],), [](#__codelineno-0-15)         ContentTypeFilter(allowed_types=["text/html"]), [](#__codelineno-0-16)     ] [](#__codelineno-0-17) ) [](#__codelineno-0-18) [](#__codelineno-0-19) # Create a keyword scorer that prioritises the pages with certain keywords first [](#__codelineno-0-20) keyword_scorer = KeywordRelevanceScorer( [](#__codelineno-0-21)     keywords=["crawl", "example", "async", "configuration"], weight=0.7 [](#__codelineno-0-22) ) [](#__codelineno-0-23) [](#__codelineno-0-24) # Set up the configuration [](#__codelineno-0-25) deep_crawl_config = CrawlerRunConfig( [](#__codelineno-0-26)     deep_crawl_strategy=BestFirstCrawlingStrategy( [](#__codelineno-0-27)         max_depth=2, [](#__codelineno-0-28)         include_external=False, [](#__codelineno-0-29)         filter_chain=filter_chain, [](#__codelineno-0-30)         url_scorer=keyword_scorer, [](#__codelineno-0-31)     ), [](#__codelineno-0-32)     scraping_strategy=LXMLWebScrapingStrategy(), [](#__codelineno-0-33)     stream=True, [](#__codelineno-0-34)     verbose=True, [](#__codelineno-0-35) ) [](#__codelineno-0-36) [](#__codelineno-0-37) async def main(): [](#__codelineno-0-38)     async with AsyncWebCrawler() as crawler: [](#__codelineno-0-39)         start_time = time.perf_counter() [](#__codelineno-0-40)         results = [] [](#__codelineno-0-41)         async for result in await crawler.arun(url="https://docs.crawl4ai.com", config=deep_crawl_config): [](#__codelineno-0-42)             print(f"Crawled: {result.url} (Depth: {result.metadata['depth']}), score: {result.metadata['score']:.2f}") [](#__codelineno-0-43)             results.append(result) [](#__codelineno-0-44)         duration = time.perf_counter() - start_time [](#__codelineno-0-45)         print(f"\n✅ Crawled {len(results)} high-value pages in {duration:.2f} seconds") [](#__codelineno-0-46) [](#__codelineno-0-47) asyncio.run(main())`

**Breaking Change:** The `max_depth` parameter is now part of `CrawlerRunConfig` and controls the _depth_ of the crawl, not the number of concurrent crawls. The `arun()` and `arun_many()` methods are now decorated to handle deep crawling strategies. Imports for deep crawling strategies have changed. See the [Deep Crawling documentation](../../../core/deep-crawling/)
 for more details.

### 2\. Memory-Adaptive Dispatcher

The new `MemoryAdaptiveDispatcher` dynamically adjusts concurrency based on available system memory and includes built-in rate limiting. This prevents out-of-memory errors and avoids overwhelming target websites.

`[](#__codelineno-1-1) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, MemoryAdaptiveDispatcher [](#__codelineno-1-2) import asyncio [](#__codelineno-1-3) [](#__codelineno-1-4) # Configure the dispatcher (optional, defaults are used if not provided) [](#__codelineno-1-5) dispatcher = MemoryAdaptiveDispatcher( [](#__codelineno-1-6)     memory_threshold_percent=80.0,  # Pause if memory usage exceeds 80% [](#__codelineno-1-7)     check_interval=0.5,  # Check memory every 0.5 seconds [](#__codelineno-1-8) ) [](#__codelineno-1-9) [](#__codelineno-1-10) async def batch_mode(): [](#__codelineno-1-11)     async with AsyncWebCrawler() as crawler: [](#__codelineno-1-12)         results = await crawler.arun_many( [](#__codelineno-1-13)             urls=["https://docs.crawl4ai.com", "https://github.com/unclecode/crawl4ai"], [](#__codelineno-1-14)             config=CrawlerRunConfig(stream=False),  # Batch mode [](#__codelineno-1-15)             dispatcher=dispatcher, [](#__codelineno-1-16)         ) [](#__codelineno-1-17)         for result in results: [](#__codelineno-1-18)             print(f"Crawled: {result.url} with status code: {result.status_code}") [](#__codelineno-1-19) [](#__codelineno-1-20) async def stream_mode(): [](#__codelineno-1-21)     async with AsyncWebCrawler() as crawler: [](#__codelineno-1-22)         # OR, for streaming: [](#__codelineno-1-23)         async for result in await crawler.arun_many( [](#__codelineno-1-24)             urls=["https://docs.crawl4ai.com", "https://github.com/unclecode/crawl4ai"], [](#__codelineno-1-25)             config=CrawlerRunConfig(stream=True), [](#__codelineno-1-26)             dispatcher=dispatcher, [](#__codelineno-1-27)         ): [](#__codelineno-1-28)             print(f"Crawled: {result.url} with status code: {result.status_code}") [](#__codelineno-1-29) [](#__codelineno-1-30) print("Dispatcher in batch mode:") [](#__codelineno-1-31) asyncio.run(batch_mode()) [](#__codelineno-1-32) print("-" * 50) [](#__codelineno-1-33) print("Dispatcher in stream mode:") [](#__codelineno-1-34) asyncio.run(stream_mode())`

**Breaking Change:** `AsyncWebCrawler.arun_many()` now uses `MemoryAdaptiveDispatcher` by default. Existing code that relied on unbounded concurrency may require adjustments.

### 3\. Multiple Crawling Strategies (Playwright and HTTP)

Crawl4AI now offers two crawling strategies:

*   **`AsyncPlaywrightCrawlerStrategy` (Default):** Uses Playwright for browser-based crawling, supporting JavaScript rendering and complex interactions.
*   **`AsyncHTTPCrawlerStrategy`:** A lightweight, fast, and memory-efficient HTTP-only crawler. Ideal for simple scraping tasks where browser rendering is unnecessary.

`[](#__codelineno-2-1) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, HTTPCrawlerConfig [](#__codelineno-2-2) from crawl4ai.async_crawler_strategy import AsyncHTTPCrawlerStrategy [](#__codelineno-2-3) import asyncio [](#__codelineno-2-4) [](#__codelineno-2-5) # Use the HTTP crawler strategy [](#__codelineno-2-6) http_crawler_config = HTTPCrawlerConfig( [](#__codelineno-2-7)         method="GET", [](#__codelineno-2-8)         headers={"User-Agent": "MyCustomBot/1.0"}, [](#__codelineno-2-9)         follow_redirects=True, [](#__codelineno-2-10)         verify_ssl=True [](#__codelineno-2-11) ) [](#__codelineno-2-12) [](#__codelineno-2-13) async def main(): [](#__codelineno-2-14)     async with AsyncWebCrawler(crawler_strategy=AsyncHTTPCrawlerStrategy(browser_config =http_crawler_config)) as crawler: [](#__codelineno-2-15)         result = await crawler.arun("https://example.com") [](#__codelineno-2-16)         print(f"Status code: {result.status_code}") [](#__codelineno-2-17)         print(f"Content length: {len(result.html)}") [](#__codelineno-2-18) [](#__codelineno-2-19) asyncio.run(main())`

### 4\. Docker Deployment

Crawl4AI can now be easily deployed as a Docker container, providing a consistent and isolated environment. The Docker image includes a FastAPI server with both streaming and non-streaming endpoints.

`[](#__codelineno-3-1) # Build the image (from the project root) [](#__codelineno-3-2) docker build -t crawl4ai . [](#__codelineno-3-3) [](#__codelineno-3-4) # Run the container [](#__codelineno-3-5) docker run -d -p 8000:8000 --name crawl4ai crawl4ai`

**API Endpoints:**

*   `/crawl` (POST): Non-streaming crawl.
*   `/crawl/stream` (POST): Streaming crawl (NDJSON).
*   `/health` (GET): Health check.
*   `/schema` (GET): Returns configuration schemas.
*   `/md/{url}` (GET): Returns markdown content of the URL.
*   `/llm/{url}` (GET): Returns LLM extracted content.
*   `/token` (POST): Get JWT token

**Breaking Changes:**

*   Docker deployment now requires a `.llm.env` file for API keys.
*   Docker deployment now requires Redis and a new `config.yml` structure.
*   Server startup now uses `supervisord` instead of direct process management.
*   Docker server now requires authentication by default (JWT tokens).

See the [Docker deployment documentation](../../../core/docker-deployment/)
 for detailed instructions.

### 5\. Command-Line Interface (CLI)

A new CLI (`crwl`) provides convenient access to Crawl4AI's functionality from the terminal.

`[](#__codelineno-4-1) # Basic crawl [](#__codelineno-4-2) crwl https://example.com [](#__codelineno-4-3) [](#__codelineno-4-4) # Get markdown output [](#__codelineno-4-5) crwl https://example.com -o markdown [](#__codelineno-4-6) [](#__codelineno-4-7) # Use a configuration file [](#__codelineno-4-8) crwl https://example.com -B browser.yml -C crawler.yml [](#__codelineno-4-9) [](#__codelineno-4-10) # Use LLM-based extraction [](#__codelineno-4-11) crwl https://example.com -e extract.yml -s schema.json [](#__codelineno-4-12) [](#__codelineno-4-13) # Ask a question about the crawled content [](#__codelineno-4-14) crwl https://example.com -q "What is the main topic?" [](#__codelineno-4-15) [](#__codelineno-4-16) # See usage examples [](#__codelineno-4-17) crwl --example`

See the [CLI documentation](../docs/md_v2/core/cli.md)
 for more details.

### 6\. LXML Scraping Mode

Added `LXMLWebScrapingStrategy` for faster HTML parsing using the `lxml` library. This can significantly improve scraping performance, especially for large or complex pages. Set `scraping_strategy=LXMLWebScrapingStrategy()` in your `CrawlerRunConfig`.

**Breaking Change:** The `ScrapingMode` enum has been replaced with a strategy pattern. Use `WebScrapingStrategy` (default) or `LXMLWebScrapingStrategy`.

### 7\. Proxy Rotation

Added `ProxyRotationStrategy` abstract base class with `RoundRobinProxyStrategy` concrete implementation.

`[](#__codelineno-5-1) import re [](#__codelineno-5-2) from crawl4ai import ( [](#__codelineno-5-3)     AsyncWebCrawler, [](#__codelineno-5-4)     BrowserConfig, [](#__codelineno-5-5)     CrawlerRunConfig, [](#__codelineno-5-6)     CacheMode, [](#__codelineno-5-7)     RoundRobinProxyStrategy, [](#__codelineno-5-8) ) [](#__codelineno-5-9) import asyncio [](#__codelineno-5-10) from crawl4ai.proxy_strategy import ProxyConfig [](#__codelineno-5-11) async def main(): [](#__codelineno-5-12)     # Load proxies and create rotation strategy [](#__codelineno-5-13)     proxies = ProxyConfig.from_env() [](#__codelineno-5-14)     #eg: export PROXIES="ip1:port1:username1:password1,ip2:port2:username2:password2" [](#__codelineno-5-15)     if not proxies: [](#__codelineno-5-16)         print("No proxies found in environment. Set PROXIES env variable!") [](#__codelineno-5-17)         return [](#__codelineno-5-18) [](#__codelineno-5-19)     proxy_strategy = RoundRobinProxyStrategy(proxies) [](#__codelineno-5-20) [](#__codelineno-5-21)     # Create configs [](#__codelineno-5-22)     browser_config = BrowserConfig(headless=True, verbose=False) [](#__codelineno-5-23)     run_config = CrawlerRunConfig( [](#__codelineno-5-24)         cache_mode=CacheMode.BYPASS, [](#__codelineno-5-25)         proxy_rotation_strategy=proxy_strategy [](#__codelineno-5-26)     ) [](#__codelineno-5-27) [](#__codelineno-5-28)     async with AsyncWebCrawler(config=browser_config) as crawler: [](#__codelineno-5-29)         urls = ["https://httpbin.org/ip"] * (len(proxies) * 2)  # Test each proxy twice [](#__codelineno-5-30) [](#__codelineno-5-31)         print("\n📈 Initializing crawler with proxy rotation...") [](#__codelineno-5-32)         async with AsyncWebCrawler(config=browser_config) as crawler: [](#__codelineno-5-33)             print("\n🚀 Starting batch crawl with proxy rotation...") [](#__codelineno-5-34)             results = await crawler.arun_many( [](#__codelineno-5-35)                 urls=urls, [](#__codelineno-5-36)                 config=run_config [](#__codelineno-5-37)             ) [](#__codelineno-5-38)             for result in results: [](#__codelineno-5-39)                 if result.success: [](#__codelineno-5-40)                     ip_match = re.search(r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}', result.html) [](#__codelineno-5-41)                     current_proxy = run_config.proxy_config if run_config.proxy_config else None [](#__codelineno-5-42) [](#__codelineno-5-43)                     if current_proxy and ip_match: [](#__codelineno-5-44)                         print(f"URL {result.url}") [](#__codelineno-5-45)                         print(f"Proxy {current_proxy.server} -> Response IP: {ip_match.group(0)}") [](#__codelineno-5-46)                         verified = ip_match.group(0) == current_proxy.ip [](#__codelineno-5-47)                         if verified: [](#__codelineno-5-48)                             print(f"✅ Proxy working! IP matches: {current_proxy.ip}") [](#__codelineno-5-49)                         else: [](#__codelineno-5-50)                             print("❌ Proxy failed or IP mismatch!") [](#__codelineno-5-51)                     print("---") [](#__codelineno-5-52) [](#__codelineno-5-53) asyncio.run(main())`

Other Changes and Improvements
------------------------------

*   **Added: `LLMContentFilter` for intelligent markdown generation.** This new filter uses an LLM to create more focused and relevant markdown output.

`[](#__codelineno-6-1) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, DefaultMarkdownGenerator [](#__codelineno-6-2) from crawl4ai.content_filter_strategy import LLMContentFilter [](#__codelineno-6-3) from crawl4ai import LLMConfig [](#__codelineno-6-4) import asyncio [](#__codelineno-6-5) [](#__codelineno-6-6) llm_config = LLMConfig(provider="gemini/gemini-1.5-pro", api_token="env:GEMINI_API_KEY") [](#__codelineno-6-7) [](#__codelineno-6-8) markdown_generator = DefaultMarkdownGenerator( [](#__codelineno-6-9)     content_filter=LLMContentFilter(llm_config=llm_config, instruction="Extract key concepts and summaries") [](#__codelineno-6-10) ) [](#__codelineno-6-11) [](#__codelineno-6-12) config = CrawlerRunConfig(markdown_generator=markdown_generator) [](#__codelineno-6-13) async def main(): [](#__codelineno-6-14)     async with AsyncWebCrawler() as crawler: [](#__codelineno-6-15)         result = await crawler.arun("https://docs.crawl4ai.com", config=config) [](#__codelineno-6-16)         print(result.markdown.fit_markdown) [](#__codelineno-6-17) [](#__codelineno-6-18) asyncio.run(main())`

*   **Added: URL redirection tracking.** The crawler now automatically follows HTTP redirects (301, 302, 307, 308) and records the final URL in the `redirected_url` field of the `CrawlResult` object. No code changes are required to enable this; it's automatic.
    
*   **Added: LLM-powered schema generation utility.** A new `generate_schema` method has been added to `JsonCssExtractionStrategy` and `JsonXPathExtractionStrategy`. This greatly simplifies creating extraction schemas.
    

`[](#__codelineno-7-1) from crawl4ai.extraction_strategy import JsonCssExtractionStrategy [](#__codelineno-7-2) from crawl4ai import LLMConfig [](#__codelineno-7-3) [](#__codelineno-7-4) llm_config = LLMConfig(provider="gemini/gemini-1.5-pro", api_token="env:GEMINI_API_KEY") [](#__codelineno-7-5) [](#__codelineno-7-6) schema = JsonCssExtractionStrategy.generate_schema( [](#__codelineno-7-7)     html="<div class='product'><h2>Product Name</h2><span class='price'>$99</span></div>", [](#__codelineno-7-8)     llm_config = llm_config, [](#__codelineno-7-9)     query="Extract product name and price" [](#__codelineno-7-10) ) [](#__codelineno-7-11) print(schema)`

Expected Output (may vary slightly due to LLM)

`[](#__codelineno-8-1) { [](#__codelineno-8-2)   "name": "ProductExtractor", [](#__codelineno-8-3)   "baseSelector": "div.product", [](#__codelineno-8-4)   "fields": [ [](#__codelineno-8-5)       {"name": "name", "selector": "h2", "type": "text"}, [](#__codelineno-8-6)       {"name": "price", "selector": ".price", "type": "text"} [](#__codelineno-8-7)     ] [](#__codelineno-8-8)  }`

*   **Added: robots.txt compliance support.** The crawler can now respect `robots.txt` rules. Enable this by setting `check_robots_txt=True` in `CrawlerRunConfig`.

`[](#__codelineno-9-1) config = CrawlerRunConfig(check_robots_txt=True)`

*   **Added: PDF processing capabilities.** Crawl4AI can now extract text, images, and metadata from PDF files (both local and remote). This uses a new `PDFCrawlerStrategy` and `PDFContentScrapingStrategy`.

`[](#__codelineno-10-1) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig [](#__codelineno-10-2) from crawl4ai.processors.pdf import PDFCrawlerStrategy, PDFContentScrapingStrategy [](#__codelineno-10-3) import asyncio [](#__codelineno-10-4) [](#__codelineno-10-5) async def main(): [](#__codelineno-10-6)     async with AsyncWebCrawler(crawler_strategy=PDFCrawlerStrategy()) as crawler: [](#__codelineno-10-7)         result = await crawler.arun( [](#__codelineno-10-8)             "https://arxiv.org/pdf/2310.06825.pdf", [](#__codelineno-10-9)             config=CrawlerRunConfig( [](#__codelineno-10-10)                 scraping_strategy=PDFContentScrapingStrategy() [](#__codelineno-10-11)             ) [](#__codelineno-10-12)         ) [](#__codelineno-10-13)         print(result.markdown)  # Access extracted text [](#__codelineno-10-14)         print(result.metadata)  # Access PDF metadata (title, author, etc.) [](#__codelineno-10-15) [](#__codelineno-10-16) asyncio.run(main())`

*   **Added: Support for frozenset serialization.** Improves configuration serialization, especially for sets of allowed/blocked domains. No code changes required.
    
*   **Added: New `LLMConfig` parameter.** This new parameter can be passed for extraction, filtering, and schema generation tasks. It simplifies passing provider strings, API tokens, and base URLs across all sections where LLM configuration is necessary. It also enables reuse and allows for quick experimentation between different LLM configurations.
    

`[](#__codelineno-11-1) from crawl4ai import LLMConfig [](#__codelineno-11-2) from crawl4ai.extraction_strategy import LLMExtractionStrategy [](#__codelineno-11-3) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig [](#__codelineno-11-4) [](#__codelineno-11-5) # Example of using LLMConfig with LLMExtractionStrategy [](#__codelineno-11-6) llm_config = LLMConfig(provider="openai/gpt-4o", api_token="YOUR_API_KEY") [](#__codelineno-11-7) strategy = LLMExtractionStrategy(llm_config=llm_config, schema=...) [](#__codelineno-11-8) [](#__codelineno-11-9) # Example usage within a crawler [](#__codelineno-11-10) async with AsyncWebCrawler() as crawler: [](#__codelineno-11-11)     result = await crawler.arun( [](#__codelineno-11-12)         url="https://example.com", [](#__codelineno-11-13)         config=CrawlerRunConfig(extraction_strategy=strategy) [](#__codelineno-11-14)     )`

**Breaking Change:** Removed old parameters like `provider`, `api_token`, `base_url`, and `api_base` from `LLMExtractionStrategy` and `LLMContentFilter`. Users should migrate to using the `LLMConfig` object.

*   **Changed: Improved browser context management and added shared data support. (Breaking Change:** `BrowserContext` API updated). Browser contexts are now managed more efficiently, reducing resource usage. A new `shared_data` dictionary is available in the `BrowserContext` to allow passing data between different stages of the crawling process. **Breaking Change:** The `BrowserContext` API has changed, and the old `get_context` method is deprecated.
    
*   **Changed:** Renamed `final_url` to `redirected_url` in `CrawledURL`. This improves consistency and clarity. Update any code referencing the old field name.
    
*   **Changed:** Improved type hints and removed unused files. This is an internal improvement and should not require code changes.
    
*   **Changed:** Reorganized deep crawling functionality into dedicated module. (**Breaking Change:** Import paths for `DeepCrawlStrategy` and related classes have changed). This improves code organization. Update imports to use the new `crawl4ai.deep_crawling` module.
    
*   **Changed:** Improved HTML handling and cleanup codebase. (**Breaking Change:** Removed `ssl_certificate.json` file). This removes an unused file. If you were relying on this file for custom certificate validation, you'll need to implement an alternative approach.
    
*   **Changed:** Enhanced serialization and config handling. (**Breaking Change:** `FastFilterChain` has been replaced with `FilterChain`). This change simplifies config and improves the serialization.
    
*   **Added:** Modified the license to Apache 2.0 _with a required attribution clause_. See the `LICENSE` file for details. All users must now clearly attribute the Crawl4AI project when using, distributing, or creating derivative works.
    
*   **Fixed:** Prevent memory leaks by ensuring proper closure of Playwright pages. No code changes required.
    
*   **Fixed:** Make model fields optional with default values (**Breaking Change:** Code relying on all fields being present may need adjustment). Fields in data models (like `CrawledURL`) are now optional, with default values (usually `None`). Update code to handle potential `None` values.
    
*   **Fixed:** Adjust memory threshold and fix dispatcher initialization. This is an internal bug fix; no code changes are required.
    
*   **Fixed:** Ensure proper exit after running doctor command. No code changes are required.
    
*   **Fixed:** JsonCss selector and crawler improvements.
*   **Fixed:** Not working long page screenshot (#403)
*   **Documentation:** Updated documentation URLs to the new domain.
*   **Documentation:** Added SERP API project example.
*   **Documentation:** Added clarifying comments for CSS selector behavior.
*   **Documentation:** Add Code of Conduct for the project (#410)

Breaking Changes Summary
------------------------

*   **Dispatcher:** The `MemoryAdaptiveDispatcher` is now the default for `arun_many()`, changing concurrency behavior. The return type of `arun_many` depends on the `stream` parameter.
*   **Deep Crawling:** `max_depth` is now part of `CrawlerRunConfig` and controls crawl depth. Import paths for deep crawling strategies have changed.
*   **Browser Context:** The `BrowserContext` API has been updated.
*   **Models:** Many fields in data models are now optional, with default values.
*   **Scraping Mode:** `ScrapingMode` enum replaced by strategy pattern (`WebScrapingStrategy`, `LXMLWebScrapingStrategy`).
*   **Content Filter:** Removed `content_filter` parameter from `CrawlerRunConfig`. Use extraction strategies or markdown generators with filters instead.
*   **Removed:** Synchronous `WebCrawler`, CLI, and docs management functionality.
*   **Docker:** Significant changes to Docker deployment, including new requirements and configuration.
*   **File Removed**: Removed ssl\_certificate.json file which might affect existing certificate validations
*   **Renamed**: final\_url to redirected\_url for consistency
*   **Config**: FastFilterChain has been replaced with FilterChain
*   **Deep-Crawl**: DeepCrawlStrategy.arun now returns Union\[CrawlResultT, List\[CrawlResultT\], AsyncGenerator\[CrawlResultT, None\]\]
*   **Proxy**: Removed synchronous WebCrawler support and related rate limiting configurations

Migration Guide
---------------

1.  **Update Imports:** Adjust imports for `DeepCrawlStrategy`, `BreadthFirstSearchStrategy`, and related classes due to the new `deep_crawling` module structure.
2.  **`CrawlerRunConfig`:** Move `max_depth` to `CrawlerRunConfig`. If using `content_filter`, migrate to an extraction strategy or a markdown generator with a filter.
3.  **`arun_many()`:** Adapt code to the new `MemoryAdaptiveDispatcher` behavior and the return type.
4.  **`BrowserContext`:** Update code using the `BrowserContext` API.
5.  **Models:** Handle potential `None` values for optional fields in data models.
6.  **Scraping:** Replace `ScrapingMode` enum with `WebScrapingStrategy` or `LXMLWebScrapingStrategy`.
7.  **Docker:** Review the updated Docker documentation and adjust your deployment accordingly.
8.  **CLI:** Migrate to the new `crwl` command and update any scripts using the old CLI.
9.  **Proxy:**: Removed synchronous WebCrawler support and related rate limiting configurations.
10.  **Config:**: Replace FastFilterChain to FilterChain

* * *

---

# Cache Modes - Crawl4AI Documentation (v0.5.x)

Crawl4AI Cache System and Migration Guide
=========================================

Overview
--------

Starting from version 0.5.0, Crawl4AI introduces a new caching system that replaces the old boolean flags with a more intuitive `CacheMode` enum. This change simplifies cache control and makes the behavior more predictable.

Old vs New Approach
-------------------

### Old Way (Deprecated)

The old system used multiple boolean flags: - `bypass_cache`: Skip cache entirely - `disable_cache`: Disable all caching - `no_cache_read`: Don't read from cache - `no_cache_write`: Don't write to cache

### New Way (Recommended)

The new system uses a single `CacheMode` enum: - `CacheMode.ENABLED`: Normal caching (read/write) - `CacheMode.DISABLED`: No caching at all - `CacheMode.READ_ONLY`: Only read from cache - `CacheMode.WRITE_ONLY`: Only write to cache - `CacheMode.BYPASS`: Skip cache for this operation

Migration Example
-----------------

### Old Code (Deprecated)

`[](#__codelineno-0-1) import asyncio [](#__codelineno-0-2) from crawl4ai import AsyncWebCrawler [](#__codelineno-0-3) [](#__codelineno-0-4) async def use_proxy(): [](#__codelineno-0-5)     async with AsyncWebCrawler(verbose=True) as crawler: [](#__codelineno-0-6)         result = await crawler.arun( [](#__codelineno-0-7)             url="https://www.nbcnews.com/business", [](#__codelineno-0-8)             bypass_cache=True  # Old way [](#__codelineno-0-9)         ) [](#__codelineno-0-10)         print(len(result.markdown)) [](#__codelineno-0-11) [](#__codelineno-0-12) async def main(): [](#__codelineno-0-13)     await use_proxy() [](#__codelineno-0-14) [](#__codelineno-0-15) if __name__ == "__main__": [](#__codelineno-0-16)     asyncio.run(main())`

### New Code (Recommended)

`[](#__codelineno-1-1) import asyncio [](#__codelineno-1-2) from crawl4ai import AsyncWebCrawler, CacheMode [](#__codelineno-1-3) from crawl4ai.async_configs import CrawlerRunConfig [](#__codelineno-1-4) [](#__codelineno-1-5) async def use_proxy(): [](#__codelineno-1-6)     # Use CacheMode in CrawlerRunConfig [](#__codelineno-1-7)     config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)   [](#__codelineno-1-8)     async with AsyncWebCrawler(verbose=True) as crawler: [](#__codelineno-1-9)         result = await crawler.arun( [](#__codelineno-1-10)             url="https://www.nbcnews.com/business", [](#__codelineno-1-11)             config=config  # Pass the configuration object [](#__codelineno-1-12)         ) [](#__codelineno-1-13)         print(len(result.markdown)) [](#__codelineno-1-14) [](#__codelineno-1-15) async def main(): [](#__codelineno-1-16)     await use_proxy() [](#__codelineno-1-17) [](#__codelineno-1-18) if __name__ == "__main__": [](#__codelineno-1-19)     asyncio.run(main())`

Common Migration Patterns
-------------------------

| Old Flag              | New Mode                          |
| --------------------- | --------------------------------- |
| `bypass_cache=True`   | `cache_mode=CacheMode.BYPASS`     |
| `disable_cache=True`  | `cache_mode=CacheMode.DISABLED`   |
| `no_cache_read=True`  | `cache_mode=CacheMode.WRITE_ONLY` |
| `no_cache_write=True` | `cache_mode=CacheMode.READ_ONLY`  |

* * *

---

# Command Line Interface - Crawl4AI Documentation (v0.5.x)

Crawl4AI CLI Guide
==================

Table of Contents
-----------------

*   [Installation](#installation)
    
*   [Basic Usage](#basic-usage)
    
*   [Configuration](#configuration)
    
*   [Browser Configuration](#browser-configuration)
    
*   [Crawler Configuration](#crawler-configuration)
    
*   [Extraction Configuration](#extraction-configuration)
    
*   [Content Filtering](#content-filtering)
    
*   [Advanced Features](#advanced-features)
    
*   [LLM Q&A](#llm-qa)
    
*   [Structured Data Extraction](#structured-data-extraction)
    
*   [Content Filtering](#content-filtering-1)
    
*   [Output Formats](#output-formats)
    
*   [Examples](#examples)
    
*   [Configuration Reference](#configuration-reference)
    
*   [Best Practices & Tips](#best-practices--tips)
    

Basic Usage
-----------

The Crawl4AI CLI (`crwl`) provides a simple interface to the Crawl4AI library:

`[](#__codelineno-0-1) # Basic crawling [](#__codelineno-0-2) crwl https://example.com [](#__codelineno-0-3) [](#__codelineno-0-4) # Get markdown output [](#__codelineno-0-5) crwl https://example.com -o markdown [](#__codelineno-0-6) [](#__codelineno-0-7) # Verbose JSON output with cache bypass [](#__codelineno-0-8) crwl https://example.com -o json -v --bypass-cache [](#__codelineno-0-9) [](#__codelineno-0-10) # See usage examples [](#__codelineno-0-11) crwl --example`

Quick Example of Advanced Usage
-------------------------------

If you clone the repository and run the following command, you will receive the content of the page in JSON format according to a JSON-CSS schema:

`[](#__codelineno-1-1) crwl "https://www.infoq.com/ai-ml-data-eng/" -e docs/examples/cli/extract_css.yml -s docs/examples/cli/css_schema.json -o json;`

Configuration
-------------

### Browser Configuration

Browser settings can be configured via YAML file or command line parameters:

`[](#__codelineno-2-1) # browser.yml [](#__codelineno-2-2) headless: true [](#__codelineno-2-3) viewport_width: 1280 [](#__codelineno-2-4) user_agent_mode: "random" [](#__codelineno-2-5) verbose: true [](#__codelineno-2-6) ignore_https_errors: true`

`[](#__codelineno-3-1) # Using config file [](#__codelineno-3-2) crwl https://example.com -B browser.yml [](#__codelineno-3-3) [](#__codelineno-3-4) # Using direct parameters [](#__codelineno-3-5) crwl https://example.com -b "headless=true,viewport_width=1280,user_agent_mode=random"`

### Crawler Configuration

Control crawling behavior:

`[](#__codelineno-4-1) # crawler.yml [](#__codelineno-4-2) cache_mode: "bypass" [](#__codelineno-4-3) wait_until: "networkidle" [](#__codelineno-4-4) page_timeout: 30000 [](#__codelineno-4-5) delay_before_return_html: 0.5 [](#__codelineno-4-6) word_count_threshold: 100 [](#__codelineno-4-7) scan_full_page: true [](#__codelineno-4-8) scroll_delay: 0.3 [](#__codelineno-4-9) process_iframes: false [](#__codelineno-4-10) remove_overlay_elements: true [](#__codelineno-4-11) magic: true [](#__codelineno-4-12) verbose: true`

`[](#__codelineno-5-1) # Using config file [](#__codelineno-5-2) crwl https://example.com -C crawler.yml [](#__codelineno-5-3) [](#__codelineno-5-4) # Using direct parameters [](#__codelineno-5-5) crwl https://example.com -c "css_selector=#main,delay_before_return_html=2,scan_full_page=true"`

### Extraction Configuration

Two types of extraction are supported:

1.  CSS/XPath-based extraction:
    
    `[](#__codelineno-6-1) # extract_css.yml [](#__codelineno-6-2) type: "json-css" [](#__codelineno-6-3) params: [](#__codelineno-6-4)   verbose: true`
    

`[](#__codelineno-7-1) // css_schema.json [](#__codelineno-7-2) { [](#__codelineno-7-3)   "name": "ArticleExtractor", [](#__codelineno-7-4)   "baseSelector": ".article", [](#__codelineno-7-5)   "fields": [ [](#__codelineno-7-6)     { [](#__codelineno-7-7)       "name": "title", [](#__codelineno-7-8)       "selector": "h1.title", [](#__codelineno-7-9)       "type": "text" [](#__codelineno-7-10)     }, [](#__codelineno-7-11)     { [](#__codelineno-7-12)       "name": "link", [](#__codelineno-7-13)       "selector": "a.read-more", [](#__codelineno-7-14)       "type": "attribute", [](#__codelineno-7-15)       "attribute": "href" [](#__codelineno-7-16)     } [](#__codelineno-7-17)   ] [](#__codelineno-7-18) }`

1.  LLM-based extraction:
    
    `[](#__codelineno-8-1) # extract_llm.yml [](#__codelineno-8-2) type: "llm" [](#__codelineno-8-3) provider: "openai/gpt-4" [](#__codelineno-8-4) instruction: "Extract all articles with their titles and links" [](#__codelineno-8-5) api_token: "your-token" [](#__codelineno-8-6) params: [](#__codelineno-8-7)   temperature: 0.3 [](#__codelineno-8-8)   max_tokens: 1000`
    

`[](#__codelineno-9-1) // llm_schema.json [](#__codelineno-9-2) { [](#__codelineno-9-3)   "title": "Article", [](#__codelineno-9-4)   "type": "object", [](#__codelineno-9-5)   "properties": { [](#__codelineno-9-6)     "title": { [](#__codelineno-9-7)       "type": "string", [](#__codelineno-9-8)       "description": "The title of the article" [](#__codelineno-9-9)     }, [](#__codelineno-9-10)     "link": { [](#__codelineno-9-11)       "type": "string", [](#__codelineno-9-12)       "description": "URL to the full article" [](#__codelineno-9-13)     } [](#__codelineno-9-14)   } [](#__codelineno-9-15) }`

Advanced Features
-----------------

### LLM Q&A

Ask questions about crawled content:

`[](#__codelineno-10-1) # Simple question [](#__codelineno-10-2) crwl https://example.com -q "What is the main topic discussed?" [](#__codelineno-10-3) [](#__codelineno-10-4) # View content then ask questions [](#__codelineno-10-5) crwl https://example.com -o markdown  # See content first [](#__codelineno-10-6) crwl https://example.com -q "Summarize the key points" [](#__codelineno-10-7) crwl https://example.com -q "What are the conclusions?" [](#__codelineno-10-8) [](#__codelineno-10-9) # Combined with advanced crawling [](#__codelineno-10-10) crwl https://example.com \ [](#__codelineno-10-11)     -B browser.yml \ [](#__codelineno-10-12)     -c "css_selector=article,scan_full_page=true" \ [](#__codelineno-10-13)     -q "What are the pros and cons mentioned?"`

First-time setup: - Prompts for LLM provider and API token - Saves configuration in `~/.crawl4ai/global.yml` - Supports various providers (openai/gpt-4, anthropic/claude-3-sonnet, etc.) - For case of `ollama` you do not need to provide API token. - See [LiteLLM Providers](https://docs.litellm.ai/docs/providers)
 for full list

### Structured Data Extraction

Extract structured data using CSS selectors:

`[](#__codelineno-11-1) crwl https://example.com \ [](#__codelineno-11-2)     -e extract_css.yml \ [](#__codelineno-11-3)     -s css_schema.json \ [](#__codelineno-11-4)     -o json`

Or using LLM-based extraction:

`[](#__codelineno-12-1) crwl https://example.com \ [](#__codelineno-12-2)     -e extract_llm.yml \ [](#__codelineno-12-3)     -s llm_schema.json \ [](#__codelineno-12-4)     -o json`

### Content Filtering

Filter content for relevance:

`[](#__codelineno-13-1) # filter_bm25.yml [](#__codelineno-13-2) type: "bm25" [](#__codelineno-13-3) query: "target content" [](#__codelineno-13-4) threshold: 1.0 [](#__codelineno-13-5) [](#__codelineno-13-6) # filter_pruning.yml [](#__codelineno-13-7) type: "pruning" [](#__codelineno-13-8) query: "focus topic" [](#__codelineno-13-9) threshold: 0.48`

`[](#__codelineno-14-1) crwl https://example.com -f filter_bm25.yml -o markdown-fit`

Output Formats
--------------

*   `all` - Full crawl result including metadata
*   `json` - Extracted structured data (when using extraction)
*   `markdown` / `md` - Raw markdown output
*   `markdown-fit` / `md-fit` - Filtered markdown for better readability

Complete Examples
-----------------

1.  Basic Extraction:
    
    `[](#__codelineno-15-1) crwl https://example.com \ [](#__codelineno-15-2)     -B browser.yml \ [](#__codelineno-15-3)     -C crawler.yml \ [](#__codelineno-15-4)     -o json`
    
2.  Structured Data Extraction:
    
    `[](#__codelineno-16-1) crwl https://example.com \ [](#__codelineno-16-2)     -e extract_css.yml \ [](#__codelineno-16-3)     -s css_schema.json \ [](#__codelineno-16-4)     -o json \ [](#__codelineno-16-5)     -v`
    
3.  LLM Extraction with Filtering:
    
    `[](#__codelineno-17-1) crwl https://example.com \ [](#__codelineno-17-2)     -B browser.yml \ [](#__codelineno-17-3)     -e extract_llm.yml \ [](#__codelineno-17-4)     -s llm_schema.json \ [](#__codelineno-17-5)     -f filter_bm25.yml \ [](#__codelineno-17-6)     -o json`
    
4.  Interactive Q&A:
    
    `[](#__codelineno-18-1) # First crawl and view [](#__codelineno-18-2) crwl https://example.com -o markdown [](#__codelineno-18-3) [](#__codelineno-18-4) # Then ask questions [](#__codelineno-18-5) crwl https://example.com -q "What are the main points?" [](#__codelineno-18-6) crwl https://example.com -q "Summarize the conclusions"`
    

Best Practices & Tips
---------------------

1.  **Configuration Management**:
2.  Keep common configurations in YAML files
3.  Use CLI parameters for quick overrides
4.  Store sensitive data (API tokens) in `~/.crawl4ai/global.yml`
    
5.  **Performance Optimization**:
    
6.  Use `--bypass-cache` for fresh content
7.  Enable `scan_full_page` for infinite scroll pages
8.  Adjust `delay_before_return_html` for dynamic content
    
9.  **Content Extraction**:
    
10.  Use CSS extraction for structured content
11.  Use LLM extraction for unstructured content
12.  Combine with filters for focused results
    
13.  **Q&A Workflow**:
    
14.  View content first with `-o markdown`
15.  Ask specific questions
16.  Use broader context with appropriate selectors

Recap
-----

The Crawl4AI CLI provides: - Flexible configuration via files and parameters - Multiple extraction strategies (CSS, XPath, LLM) - Content filtering and optimization - Interactive Q&A capabilities - Various output formats

* * *

---

# Crawler Result - Crawl4AI Documentation (v0.5.x)

Crawl Result and Output
=======================

When you call `arun()` on a page, Crawl4AI returns a **`CrawlResult`** object containing everything you might need—raw HTML, a cleaned version, optional screenshots or PDFs, structured extraction results, and more. This document explains those fields and how they map to different output types.

* * *

1\. The `CrawlResult` Model
---------------------------

Below is the core schema. Each field captures a different aspect of the crawl’s result:

`[](#__codelineno-0-1) class MarkdownGenerationResult(BaseModel): [](#__codelineno-0-2)     raw_markdown: str [](#__codelineno-0-3)     markdown_with_citations: str [](#__codelineno-0-4)     references_markdown: str [](#__codelineno-0-5)     fit_markdown: Optional[str] = None [](#__codelineno-0-6)     fit_html: Optional[str] = None [](#__codelineno-0-7) [](#__codelineno-0-8) class CrawlResult(BaseModel): [](#__codelineno-0-9)     url: str [](#__codelineno-0-10)     html: str [](#__codelineno-0-11)     success: bool [](#__codelineno-0-12)     cleaned_html: Optional[str] = None [](#__codelineno-0-13)     media: Dict[str, List[Dict]] = {} [](#__codelineno-0-14)     links: Dict[str, List[Dict]] = {} [](#__codelineno-0-15)     downloaded_files: Optional[List[str]] = None [](#__codelineno-0-16)     screenshot: Optional[str] = None [](#__codelineno-0-17)     pdf : Optional[bytes] = None [](#__codelineno-0-18)     markdown: Optional[Union[str, MarkdownGenerationResult]] = None [](#__codelineno-0-19)     extracted_content: Optional[str] = None [](#__codelineno-0-20)     metadata: Optional[dict] = None [](#__codelineno-0-21)     error_message: Optional[str] = None [](#__codelineno-0-22)     session_id: Optional[str] = None [](#__codelineno-0-23)     response_headers: Optional[dict] = None [](#__codelineno-0-24)     status_code: Optional[int] = None [](#__codelineno-0-25)     ssl_certificate: Optional[SSLCertificate] = None [](#__codelineno-0-26)     class Config: [](#__codelineno-0-27)         arbitrary_types_allowed = True`

### Table: Key Fields in `CrawlResult`

| Field (Name & Type)                                        | Description                                                                                                                                                                                |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **url (`str`)**                                            | The final or actual URL crawled (in case of redirects).                                                                                                                                    |
| **html (`str`)**                                           | Original, unmodified page HTML. Good for debugging or custom processing.                                                                                                                   |
| **success (`bool`)**                                       | `True` if the crawl completed without major errors, else `False`.                                                                                                                          |
| **cleaned\_html (`Optional[str]`)**                        | Sanitized HTML with scripts/styles removed; can exclude tags if configured via `excluded_tags` etc.                                                                                        |
| **media (`Dict[str, List[Dict]]`)**                        | Extracted media info (images, audio, etc.), each with attributes like `src`, `alt`, `score`, etc.                                                                                          |
| **links (`Dict[str, List[Dict]]`)**                        | Extracted link data, split by `internal` and `external`. Each link usually has `href`, `text`, etc.                                                                                        |
| **downloaded\_files (`Optional[List[str]]`)**              | If `accept_downloads=True` in `BrowserConfig`, this lists the filepaths of saved downloads.                                                                                                |
| **screenshot (`Optional[str]`)**                           | Screenshot of the page (base64-encoded) if `screenshot=True`.                                                                                                                              |
| **pdf (`Optional[bytes]`)**                                | PDF of the page if `pdf=True`.                                                                                                                                                             |
| **markdown (`Optional[str or MarkdownGenerationResult]`)** | It holds a `MarkdownGenerationResult`. Over time, this will be consolidated into `markdown`. The generator can provide raw markdown, citations, references, and optionally `fit_markdown`. |
| **extracted\_content (`Optional[str]`)**                   | The output of a structured extraction (CSS/LLM-based) stored as JSON string or other text.                                                                                                 |
| **metadata (`Optional[dict]`)**                            | Additional info about the crawl or extracted data.                                                                                                                                         |
| **error\_message (`Optional[str]`)**                       | If `success=False`, contains a short description of what went wrong.                                                                                                                       |
| **session\_id (`Optional[str]`)**                          | The ID of the session used for multi-page or persistent crawling.                                                                                                                          |
| **response\_headers (`Optional[dict]`)**                   | HTTP response headers, if captured.                                                                                                                                                        |
| **status\_code (`Optional[int]`)**                         | HTTP status code (e.g., 200 for OK).                                                                                                                                                       |
| **ssl\_certificate (`Optional[SSLCertificate]`)**          | SSL certificate info if `fetch_ssl_certificate=True`.                                                                                                                                      |

* * *

2\. HTML Variants
-----------------

### `html`: Raw HTML

Crawl4AI preserves the exact HTML as `result.html`. Useful for:

*   Debugging page issues or checking the original content.
*   Performing your own specialized parse if needed.

### `cleaned_html`: Sanitized

If you specify any cleanup or exclusion parameters in `CrawlerRunConfig` (like `excluded_tags`, `remove_forms`, etc.), you’ll see the result here:

`[](#__codelineno-1-1) config = CrawlerRunConfig( [](#__codelineno-1-2)     excluded_tags=["form", "header", "footer"], [](#__codelineno-1-3)     keep_data_attributes=False [](#__codelineno-1-4) ) [](#__codelineno-1-5) result = await crawler.arun("https://example.com", config=config) [](#__codelineno-1-6) print(result.cleaned_html)  # Freed of forms, header, footer, data-* attributes`

* * *

3\. Markdown Generation
-----------------------

### 3.1 `markdown`

*   **`markdown`**: The current location for detailed markdown output, returning a **`MarkdownGenerationResult`** object.
*   **`markdown_v2`**: Deprecated since v0.5.

**`MarkdownGenerationResult`** Fields:

| Field                         | Description                                                          |
| ----------------------------- | -------------------------------------------------------------------- |
| **raw\_markdown**             | The basic HTML→Markdown conversion.                                  |
| **markdown\_with\_citations** | Markdown including inline citations that reference links at the end. |
| **references\_markdown**      | The references/citations themselves (if `citations=True`).           |
| **fit\_markdown**             | The filtered/“fit” markdown if a content filter was used.            |
| **fit\_html**                 | The filtered HTML that generated `fit_markdown`.                     |

### 3.2 Basic Example with a Markdown Generator

`[](#__codelineno-2-1) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig [](#__codelineno-2-2) from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator [](#__codelineno-2-3) [](#__codelineno-2-4) config = CrawlerRunConfig( [](#__codelineno-2-5)     markdown_generator=DefaultMarkdownGenerator( [](#__codelineno-2-6)         options={"citations": True, "body_width": 80}  # e.g. pass html2text style options [](#__codelineno-2-7)     ) [](#__codelineno-2-8) ) [](#__codelineno-2-9) result = await crawler.arun(url="https://example.com", config=config) [](#__codelineno-2-10) [](#__codelineno-2-11) md_res = result.markdown  # or eventually 'result.markdown' [](#__codelineno-2-12) print(md_res.raw_markdown[:500]) [](#__codelineno-2-13) print(md_res.markdown_with_citations) [](#__codelineno-2-14) print(md_res.references_markdown)`

**Note**: If you use a filter like `PruningContentFilter`, you’ll get `fit_markdown` and `fit_html` as well.

* * *

4\. Structured Extraction: `extracted_content`
----------------------------------------------

If you run a JSON-based extraction strategy (CSS, XPath, LLM, etc.), the structured data is **not** stored in `markdown`—it’s placed in **`result.extracted_content`** as a JSON string (or sometimes plain text).

### Example: CSS Extraction with `raw://` HTML

`[](#__codelineno-3-1) import asyncio [](#__codelineno-3-2) import json [](#__codelineno-3-3) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode [](#__codelineno-3-4) from crawl4ai.extraction_strategy import JsonCssExtractionStrategy [](#__codelineno-3-5) [](#__codelineno-3-6) async def main(): [](#__codelineno-3-7)     schema = { [](#__codelineno-3-8)         "name": "Example Items", [](#__codelineno-3-9)         "baseSelector": "div.item", [](#__codelineno-3-10)         "fields": [ [](#__codelineno-3-11)             {"name": "title", "selector": "h2", "type": "text"}, [](#__codelineno-3-12)             {"name": "link", "selector": "a", "type": "attribute", "attribute": "href"} [](#__codelineno-3-13)         ] [](#__codelineno-3-14)     } [](#__codelineno-3-15)     raw_html = "<div class='item'><h2>Item 1</h2><a href='https://example.com/item1'>Link 1</a></div>" [](#__codelineno-3-16) [](#__codelineno-3-17)     async with AsyncWebCrawler() as crawler: [](#__codelineno-3-18)         result = await crawler.arun( [](#__codelineno-3-19)             url="raw://" + raw_html, [](#__codelineno-3-20)             config=CrawlerRunConfig( [](#__codelineno-3-21)                 cache_mode=CacheMode.BYPASS, [](#__codelineno-3-22)                 extraction_strategy=JsonCssExtractionStrategy(schema) [](#__codelineno-3-23)             ) [](#__codelineno-3-24)         ) [](#__codelineno-3-25)         data = json.loads(result.extracted_content) [](#__codelineno-3-26)         print(data) [](#__codelineno-3-27) [](#__codelineno-3-28) if __name__ == "__main__": [](#__codelineno-3-29)     asyncio.run(main())`

Here: - `url="raw://..."` passes the HTML content directly, no network requests.  
\- The **CSS** extraction strategy populates `result.extracted_content` with the JSON array `[{"title": "...", "link": "..."}]`.

* * *

5\. More Fields: Links, Media, and More
---------------------------------------

### 5.1 `links`

A dictionary, typically with `"internal"` and `"external"` lists. Each entry might have `href`, `text`, `title`, etc. This is automatically captured if you haven’t disabled link extraction.

`[](#__codelineno-4-1) print(result.links["internal"][:3])  # Show first 3 internal links`

### 5.2 `media`

Similarly, a dictionary with `"images"`, `"audio"`, `"video"`, etc. Each item could include `src`, `alt`, `score`, and more, if your crawler is set to gather them.

`[](#__codelineno-5-1) images = result.media.get("images", []) [](#__codelineno-5-2) for img in images: [](#__codelineno-5-3)     print("Image URL:", img["src"], "Alt:", img.get("alt"))`

### 5.3 `screenshot` and `pdf`

If you set `screenshot=True` or `pdf=True` in **`CrawlerRunConfig`**, then:

*   `result.screenshot` contains a base64-encoded PNG string.
*   `result.pdf` contains raw PDF bytes (you can write them to a file).

`[](#__codelineno-6-1) with open("page.pdf", "wb") as f: [](#__codelineno-6-2)     f.write(result.pdf)`

### 5.4 `ssl_certificate`

If `fetch_ssl_certificate=True`, `result.ssl_certificate` holds details about the site’s SSL cert, such as issuer, validity dates, etc.

* * *

6\. Accessing These Fields
--------------------------

After you run:

`[](#__codelineno-7-1) result = await crawler.arun(url="https://example.com", config=some_config)`

Check any field:

`[](#__codelineno-8-1) if result.success: [](#__codelineno-8-2)     print(result.status_code, result.response_headers) [](#__codelineno-8-3)     print("Links found:", len(result.links.get("internal", []))) [](#__codelineno-8-4)     if result.markdown: [](#__codelineno-8-5)         print("Markdown snippet:", result.markdown.raw_markdown[:200]) [](#__codelineno-8-6)     if result.extracted_content: [](#__codelineno-8-7)         print("Structured JSON:", result.extracted_content) [](#__codelineno-8-8) else: [](#__codelineno-8-9)     print("Error:", result.error_message)`

**Deprecation**: Since v0.5 `result.markdown_v2`, `result.fit_html`,`result.fit_markdown` are deprecated. Use `result.markdown` instead! It holds `MarkdownGenerationResult`, which includes `fit_html` and `fit_markdown` as it's properties.

* * *

7\. Next Steps
--------------

*   **Markdown Generation**: Dive deeper into how to configure `DefaultMarkdownGenerator` and various filters.
*   **Content Filtering**: Learn how to use `BM25ContentFilter` and `PruningContentFilter`.
*   **Session & Hooks**: If you want to manipulate the page or preserve state across multiple `arun()` calls, see the hooking or session docs.
*   **LLM Extraction**: For complex or unstructured content requiring AI-driven parsing, check the LLM-based strategies doc.

**Enjoy** exploring all that `CrawlResult` offers—whether you need raw HTML, sanitized output, markdown, or fully structured data, Crawl4AI has you covered!

* * *

---

# Deep Crawling - Crawl4AI Documentation (v0.5.x)

Deep Crawling
=============

One of Crawl4AI's most powerful features is its ability to perform **configurable deep crawling** that can explore websites beyond a single page. With fine-tuned control over crawl depth, domain boundaries, and content filtering, Crawl4AI gives you the tools to extract precisely the content you need.

In this tutorial, you'll learn:

1.  How to set up a **Basic Deep Crawler** with BFS strategy
2.  Understanding the difference between **streamed and non-streamed** output
3.  Implementing **filters and scorers** to target specific content
4.  Creating **advanced filtering chains** for sophisticated crawls
5.  Using **BestFirstCrawling** for intelligent exploration prioritization

> **Prerequisites**  
> \- You’ve completed or read [AsyncWebCrawler Basics](../simple-crawling/)
>  to understand how to run a simple crawl.  
> \- You know how to configure `CrawlerRunConfig`.

* * *

1\. Quick Example
-----------------

Here's a minimal code snippet that implements a basic deep crawl using the **BFSDeepCrawlStrategy**:

`[](#__codelineno-0-1) import asyncio [](#__codelineno-0-2) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig [](#__codelineno-0-3) from crawl4ai.deep_crawling import BFSDeepCrawlStrategy [](#__codelineno-0-4) from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy [](#__codelineno-0-5) [](#__codelineno-0-6) async def main(): [](#__codelineno-0-7)     # Configure a 2-level deep crawl [](#__codelineno-0-8)     config = CrawlerRunConfig( [](#__codelineno-0-9)         deep_crawl_strategy=BFSDeepCrawlStrategy( [](#__codelineno-0-10)             max_depth=2,  [](#__codelineno-0-11)             include_external=False [](#__codelineno-0-12)         ), [](#__codelineno-0-13)         scraping_strategy=LXMLWebScrapingStrategy(), [](#__codelineno-0-14)         verbose=True [](#__codelineno-0-15)     ) [](#__codelineno-0-16) [](#__codelineno-0-17)     async with AsyncWebCrawler() as crawler: [](#__codelineno-0-18)         results = await crawler.arun("https://example.com", config=config) [](#__codelineno-0-19) [](#__codelineno-0-20)         print(f"Crawled {len(results)} pages in total") [](#__codelineno-0-21) [](#__codelineno-0-22)         # Access individual results [](#__codelineno-0-23)         for result in results[:3]:  # Show first 3 results [](#__codelineno-0-24)             print(f"URL: {result.url}") [](#__codelineno-0-25)             print(f"Depth: {result.metadata.get('depth', 0)}") [](#__codelineno-0-26) [](#__codelineno-0-27) if __name__ == "__main__": [](#__codelineno-0-28)     asyncio.run(main())`

**What's happening?**  
\- `BFSDeepCrawlStrategy(max_depth=2, include_external=False)` instructs Crawl4AI to: - Crawl the starting page (depth 0) plus 2 more levels - Stay within the same domain (don't follow external links) - Each result contains metadata like the crawl depth - Results are returned as a list after all crawling is complete

* * *

2\. Understanding Deep Crawling Strategy Options
------------------------------------------------

### 2.1 BFSDeepCrawlStrategy (Breadth-First Search)

The **BFSDeepCrawlStrategy** uses a breadth-first approach, exploring all links at one depth before moving deeper:

`[](#__codelineno-1-1) from crawl4ai.deep_crawling import BFSDeepCrawlStrategy [](#__codelineno-1-2) [](#__codelineno-1-3) # Basic configuration [](#__codelineno-1-4) strategy = BFSDeepCrawlStrategy( [](#__codelineno-1-5)     max_depth=2,               # Crawl initial page + 2 levels deep [](#__codelineno-1-6)     include_external=False,    # Stay within the same domain [](#__codelineno-1-7)     max_pages=50,              # Maximum number of pages to crawl (optional) [](#__codelineno-1-8)     score_threshold=0.3,       # Minimum score for URLs to be crawled (optional) [](#__codelineno-1-9) )`

**Key parameters:** - **`max_depth`**: Number of levels to crawl beyond the starting page - **`include_external`**: Whether to follow links to other domains - **`max_pages`**: Maximum number of pages to crawl (default: infinite) - **`score_threshold`**: Minimum score for URLs to be crawled (default: -inf) - **`filter_chain`**: FilterChain instance for URL filtering - **`url_scorer`**: Scorer instance for evaluating URLs

### 2.2 DFSDeepCrawlStrategy (Depth-First Search)

The **DFSDeepCrawlStrategy** uses a depth-first approach, explores as far down a branch as possible before backtracking.

`[](#__codelineno-2-1) from crawl4ai.deep_crawling import DFSDeepCrawlStrategy [](#__codelineno-2-2) [](#__codelineno-2-3) # Basic configuration [](#__codelineno-2-4) strategy = DFSDeepCrawlStrategy( [](#__codelineno-2-5)     max_depth=2,               # Crawl initial page + 2 levels deep [](#__codelineno-2-6)     include_external=False,    # Stay within the same domain [](#__codelineno-2-7)     max_pages=30,              # Maximum number of pages to crawl (optional) [](#__codelineno-2-8)     score_threshold=0.5,       # Minimum score for URLs to be crawled (optional) [](#__codelineno-2-9) )`

**Key parameters:** - **`max_depth`**: Number of levels to crawl beyond the starting page - **`include_external`**: Whether to follow links to other domains - **`max_pages`**: Maximum number of pages to crawl (default: infinite) - **`score_threshold`**: Minimum score for URLs to be crawled (default: -inf) - **`filter_chain`**: FilterChain instance for URL filtering - **`url_scorer`**: Scorer instance for evaluating URLs

### 2.3 BestFirstCrawlingStrategy (⭐️ - Recommended Deep crawl strategy)

For more intelligent crawling, use **BestFirstCrawlingStrategy** with scorers to prioritize the most relevant pages:

`[](#__codelineno-3-1) from crawl4ai.deep_crawling import BestFirstCrawlingStrategy [](#__codelineno-3-2) from crawl4ai.deep_crawling.scorers import KeywordRelevanceScorer [](#__codelineno-3-3) [](#__codelineno-3-4) # Create a scorer [](#__codelineno-3-5) scorer = KeywordRelevanceScorer( [](#__codelineno-3-6)     keywords=["crawl", "example", "async", "configuration"], [](#__codelineno-3-7)     weight=0.7 [](#__codelineno-3-8) ) [](#__codelineno-3-9) [](#__codelineno-3-10) # Configure the strategy [](#__codelineno-3-11) strategy = BestFirstCrawlingStrategy( [](#__codelineno-3-12)     max_depth=2, [](#__codelineno-3-13)     include_external=False, [](#__codelineno-3-14)     url_scorer=scorer, [](#__codelineno-3-15)     max_pages=25,              # Maximum number of pages to crawl (optional) [](#__codelineno-3-16) )`

This crawling approach: - Evaluates each discovered URL based on scorer criteria - Visits higher-scoring pages first - Helps focus crawl resources on the most relevant content - Can limit total pages crawled with `max_pages` - Does not need `score_threshold` as it naturally prioritizes by score

* * *

3\. Streaming vs. Non-Streaming Results
---------------------------------------

Crawl4AI can return results in two modes:

### 3.1 Non-Streaming Mode (Default)

`[](#__codelineno-4-1) config = CrawlerRunConfig( [](#__codelineno-4-2)     deep_crawl_strategy=BFSDeepCrawlStrategy(max_depth=1), [](#__codelineno-4-3)     stream=False  # Default behavior [](#__codelineno-4-4) ) [](#__codelineno-4-5) [](#__codelineno-4-6) async with AsyncWebCrawler() as crawler: [](#__codelineno-4-7)     # Wait for ALL results to be collected before returning [](#__codelineno-4-8)     results = await crawler.arun("https://example.com", config=config) [](#__codelineno-4-9) [](#__codelineno-4-10)     for result in results: [](#__codelineno-4-11)         process_result(result)`

**When to use non-streaming mode:** - You need the complete dataset before processing - You're performing batch operations on all results together - Crawl time isn't a critical factor

### 3.2 Streaming Mode

`[](#__codelineno-5-1) config = CrawlerRunConfig( [](#__codelineno-5-2)     deep_crawl_strategy=BFSDeepCrawlStrategy(max_depth=1), [](#__codelineno-5-3)     stream=True  # Enable streaming [](#__codelineno-5-4) ) [](#__codelineno-5-5) [](#__codelineno-5-6) async with AsyncWebCrawler() as crawler: [](#__codelineno-5-7)     # Returns an async iterator [](#__codelineno-5-8)     async for result in await crawler.arun("https://example.com", config=config): [](#__codelineno-5-9)         # Process each result as it becomes available [](#__codelineno-5-10)         process_result(result)`

**Benefits of streaming mode:** - Process results immediately as they're discovered - Start working with early results while crawling continues - Better for real-time applications or progressive display - Reduces memory pressure when handling many pages

* * *

4\. Filtering Content with Filter Chains
----------------------------------------

Filters help you narrow down which pages to crawl. Combine multiple filters using **FilterChain** for powerful targeting.

### 4.1 Basic URL Pattern Filter

`[](#__codelineno-6-1) from crawl4ai.deep_crawling.filters import FilterChain, URLPatternFilter [](#__codelineno-6-2) [](#__codelineno-6-3) # Only follow URLs containing "blog" or "docs" [](#__codelineno-6-4) url_filter = URLPatternFilter(patterns=["*blog*", "*docs*"]) [](#__codelineno-6-5) [](#__codelineno-6-6) config = CrawlerRunConfig( [](#__codelineno-6-7)     deep_crawl_strategy=BFSDeepCrawlStrategy( [](#__codelineno-6-8)         max_depth=1, [](#__codelineno-6-9)         filter_chain=FilterChain([url_filter]) [](#__codelineno-6-10)     ) [](#__codelineno-6-11) )`

### 4.2 Combining Multiple Filters

`[](#__codelineno-7-1) from crawl4ai.deep_crawling.filters import ( [](#__codelineno-7-2)     FilterChain, [](#__codelineno-7-3)     URLPatternFilter, [](#__codelineno-7-4)     DomainFilter, [](#__codelineno-7-5)     ContentTypeFilter [](#__codelineno-7-6) ) [](#__codelineno-7-7) [](#__codelineno-7-8) # Create a chain of filters [](#__codelineno-7-9) filter_chain = FilterChain([ [](#__codelineno-7-10)     # Only follow URLs with specific patterns [](#__codelineno-7-11)     URLPatternFilter(patterns=["*guide*", "*tutorial*"]), [](#__codelineno-7-12) [](#__codelineno-7-13)     # Only crawl specific domains [](#__codelineno-7-14)     DomainFilter( [](#__codelineno-7-15)         allowed_domains=["docs.example.com"], [](#__codelineno-7-16)         blocked_domains=["old.docs.example.com"] [](#__codelineno-7-17)     ), [](#__codelineno-7-18) [](#__codelineno-7-19)     # Only include specific content types [](#__codelineno-7-20)     ContentTypeFilter(allowed_types=["text/html"]) [](#__codelineno-7-21) ]) [](#__codelineno-7-22) [](#__codelineno-7-23) config = CrawlerRunConfig( [](#__codelineno-7-24)     deep_crawl_strategy=BFSDeepCrawlStrategy( [](#__codelineno-7-25)         max_depth=2, [](#__codelineno-7-26)         filter_chain=filter_chain [](#__codelineno-7-27)     ) [](#__codelineno-7-28) )`

### 4.3 Available Filter Types

Crawl4AI includes several specialized filters:

*   **`URLPatternFilter`**: Matches URL patterns using wildcard syntax
*   **`DomainFilter`**: Controls which domains to include or exclude
*   **`ContentTypeFilter`**: Filters based on HTTP Content-Type
*   **`ContentRelevanceFilter`**: Uses similarity to a text query
*   **`SEOFilter`**: Evaluates SEO elements (meta tags, headers, etc.)

* * *

5\. Using Scorers for Prioritized Crawling
------------------------------------------

Scorers assign priority values to discovered URLs, helping the crawler focus on the most relevant content first.

### 5.1 KeywordRelevanceScorer

`[](#__codelineno-8-1) from crawl4ai.deep_crawling.scorers import KeywordRelevanceScorer [](#__codelineno-8-2) from crawl4ai.deep_crawling import BestFirstCrawlingStrategy [](#__codelineno-8-3) [](#__codelineno-8-4) # Create a keyword relevance scorer [](#__codelineno-8-5) keyword_scorer = KeywordRelevanceScorer( [](#__codelineno-8-6)     keywords=["crawl", "example", "async", "configuration"], [](#__codelineno-8-7)     weight=0.7  # Importance of this scorer (0.0 to 1.0) [](#__codelineno-8-8) ) [](#__codelineno-8-9) [](#__codelineno-8-10) config = CrawlerRunConfig( [](#__codelineno-8-11)     deep_crawl_strategy=BestFirstCrawlingStrategy( [](#__codelineno-8-12)         max_depth=2, [](#__codelineno-8-13)         url_scorer=keyword_scorer [](#__codelineno-8-14)     ), [](#__codelineno-8-15)     stream=True  # Recommended with BestFirstCrawling [](#__codelineno-8-16) ) [](#__codelineno-8-17) [](#__codelineno-8-18) # Results will come in order of relevance score [](#__codelineno-8-19) async with AsyncWebCrawler() as crawler: [](#__codelineno-8-20)     async for result in await crawler.arun("https://example.com", config=config): [](#__codelineno-8-21)         score = result.metadata.get("score", 0) [](#__codelineno-8-22)         print(f"Score: {score:.2f} | {result.url}")`

**How scorers work:** - Evaluate each discovered URL before crawling - Calculate relevance based on various signals - Help the crawler make intelligent choices about traversal order

* * *

6\. Advanced Filtering Techniques
---------------------------------

### 6.1 SEO Filter for Quality Assessment

The **SEOFilter** helps you identify pages with strong SEO characteristics:

`[](#__codelineno-9-1) from crawl4ai.deep_crawling.filters import FilterChain, SEOFilter [](#__codelineno-9-2) [](#__codelineno-9-3) # Create an SEO filter that looks for specific keywords in page metadata [](#__codelineno-9-4) seo_filter = SEOFilter( [](#__codelineno-9-5)     threshold=0.5,  # Minimum score (0.0 to 1.0) [](#__codelineno-9-6)     keywords=["tutorial", "guide", "documentation"] [](#__codelineno-9-7) ) [](#__codelineno-9-8) [](#__codelineno-9-9) config = CrawlerRunConfig( [](#__codelineno-9-10)     deep_crawl_strategy=BFSDeepCrawlStrategy( [](#__codelineno-9-11)         max_depth=1, [](#__codelineno-9-12)         filter_chain=FilterChain([seo_filter]) [](#__codelineno-9-13)     ) [](#__codelineno-9-14) )`

### 6.2 Content Relevance Filter

The **ContentRelevanceFilter** analyzes the actual content of pages:

`[](#__codelineno-10-1) from crawl4ai.deep_crawling.filters import FilterChain, ContentRelevanceFilter [](#__codelineno-10-2) [](#__codelineno-10-3) # Create a content relevance filter [](#__codelineno-10-4) relevance_filter = ContentRelevanceFilter( [](#__codelineno-10-5)     query="Web crawling and data extraction with Python", [](#__codelineno-10-6)     threshold=0.7  # Minimum similarity score (0.0 to 1.0) [](#__codelineno-10-7) ) [](#__codelineno-10-8) [](#__codelineno-10-9) config = CrawlerRunConfig( [](#__codelineno-10-10)     deep_crawl_strategy=BFSDeepCrawlStrategy( [](#__codelineno-10-11)         max_depth=1, [](#__codelineno-10-12)         filter_chain=FilterChain([relevance_filter]) [](#__codelineno-10-13)     ) [](#__codelineno-10-14) )`

This filter: - Measures semantic similarity between query and page content - It's a BM25-based relevance filter using head section content

* * *

7\. Building a Complete Advanced Crawler
----------------------------------------

This example combines multiple techniques for a sophisticated crawl:

`[](#__codelineno-11-1) import asyncio [](#__codelineno-11-2) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig [](#__codelineno-11-3) from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy [](#__codelineno-11-4) from crawl4ai.deep_crawling import BestFirstCrawlingStrategy [](#__codelineno-11-5) from crawl4ai.deep_crawling.filters import ( [](#__codelineno-11-6)     FilterChain, [](#__codelineno-11-7)     DomainFilter, [](#__codelineno-11-8)     URLPatternFilter, [](#__codelineno-11-9)     ContentTypeFilter [](#__codelineno-11-10) ) [](#__codelineno-11-11) from crawl4ai.deep_crawling.scorers import KeywordRelevanceScorer [](#__codelineno-11-12) [](#__codelineno-11-13) async def run_advanced_crawler(): [](#__codelineno-11-14)     # Create a sophisticated filter chain [](#__codelineno-11-15)     filter_chain = FilterChain([ [](#__codelineno-11-16)         # Domain boundaries [](#__codelineno-11-17)         DomainFilter( [](#__codelineno-11-18)             allowed_domains=["docs.example.com"], [](#__codelineno-11-19)             blocked_domains=["old.docs.example.com"] [](#__codelineno-11-20)         ), [](#__codelineno-11-21) [](#__codelineno-11-22)         # URL patterns to include [](#__codelineno-11-23)         URLPatternFilter(patterns=["*guide*", "*tutorial*", "*blog*"]), [](#__codelineno-11-24) [](#__codelineno-11-25)         # Content type filtering [](#__codelineno-11-26)         ContentTypeFilter(allowed_types=["text/html"]) [](#__codelineno-11-27)     ]) [](#__codelineno-11-28) [](#__codelineno-11-29)     # Create a relevance scorer [](#__codelineno-11-30)     keyword_scorer = KeywordRelevanceScorer( [](#__codelineno-11-31)         keywords=["crawl", "example", "async", "configuration"], [](#__codelineno-11-32)         weight=0.7 [](#__codelineno-11-33)     ) [](#__codelineno-11-34) [](#__codelineno-11-35)     # Set up the configuration [](#__codelineno-11-36)     config = CrawlerRunConfig( [](#__codelineno-11-37)         deep_crawl_strategy=BestFirstCrawlingStrategy( [](#__codelineno-11-38)             max_depth=2, [](#__codelineno-11-39)             include_external=False, [](#__codelineno-11-40)             filter_chain=filter_chain, [](#__codelineno-11-41)             url_scorer=keyword_scorer [](#__codelineno-11-42)         ), [](#__codelineno-11-43)         scraping_strategy=LXMLWebScrapingStrategy(), [](#__codelineno-11-44)         stream=True, [](#__codelineno-11-45)         verbose=True [](#__codelineno-11-46)     ) [](#__codelineno-11-47) [](#__codelineno-11-48)     # Execute the crawl [](#__codelineno-11-49)     results = [] [](#__codelineno-11-50)     async with AsyncWebCrawler() as crawler: [](#__codelineno-11-51)         async for result in await crawler.arun("https://docs.example.com", config=config): [](#__codelineno-11-52)             results.append(result) [](#__codelineno-11-53)             score = result.metadata.get("score", 0) [](#__codelineno-11-54)             depth = result.metadata.get("depth", 0) [](#__codelineno-11-55)             print(f"Depth: {depth} | Score: {score:.2f} | {result.url}") [](#__codelineno-11-56) [](#__codelineno-11-57)     # Analyze the results [](#__codelineno-11-58)     print(f"Crawled {len(results)} high-value pages") [](#__codelineno-11-59)     print(f"Average score: {sum(r.metadata.get('score', 0) for r in results) / len(results):.2f}") [](#__codelineno-11-60) [](#__codelineno-11-61)     # Group by depth [](#__codelineno-11-62)     depth_counts = {} [](#__codelineno-11-63)     for result in results: [](#__codelineno-11-64)         depth = result.metadata.get("depth", 0) [](#__codelineno-11-65)         depth_counts[depth] = depth_counts.get(depth, 0) + 1 [](#__codelineno-11-66) [](#__codelineno-11-67)     print("Pages crawled by depth:") [](#__codelineno-11-68)     for depth, count in sorted(depth_counts.items()): [](#__codelineno-11-69)         print(f"  Depth {depth}: {count} pages") [](#__codelineno-11-70) [](#__codelineno-11-71) if __name__ == "__main__": [](#__codelineno-11-72)     asyncio.run(run_advanced_crawler())`

* * *

8\. Limiting and Controlling Crawl Size
---------------------------------------

### 8.1 Using max\_pages

You can limit the total number of pages crawled with the `max_pages` parameter:

`[](#__codelineno-12-1) # Limit to exactly 20 pages regardless of depth [](#__codelineno-12-2) strategy = BFSDeepCrawlStrategy( [](#__codelineno-12-3)     max_depth=3, [](#__codelineno-12-4)     max_pages=20 [](#__codelineno-12-5) )`

This feature is useful for: - Controlling API costs - Setting predictable execution times - Focusing on the most important content - Testing crawl configurations before full execution

### 8.2 Using score\_threshold

For BFS and DFS strategies, you can set a minimum score threshold to only crawl high-quality pages:

`[](#__codelineno-13-1) # Only follow links with scores above 0.4 [](#__codelineno-13-2) strategy = DFSDeepCrawlStrategy( [](#__codelineno-13-3)     max_depth=2, [](#__codelineno-13-4)     url_scorer=KeywordRelevanceScorer(keywords=["api", "guide", "reference"]), [](#__codelineno-13-5)     score_threshold=0.4  # Skip URLs with scores below this value [](#__codelineno-13-6) )`

Note that for BestFirstCrawlingStrategy, score\_threshold is not needed since pages are already processed in order of highest score first.

9\. Common Pitfalls & Tips
--------------------------

1.**Set realistic limits.** Be cautious with `max_depth` values > 3, which can exponentially increase crawl size. Use `max_pages` to set hard limits.

2.**Don't neglect the scoring component.** BestFirstCrawling works best with well-tuned scorers. Experiment with keyword weights for optimal prioritization.

3.**Be a good web citizen.** Respect robots.txt. (disabled by default)

4.**Handle page errors gracefully.** Not all pages will be accessible. Check `result.status` when processing results.

5.**Balance breadth vs. depth.** Choose your strategy wisely - BFS for comprehensive coverage, DFS for deep exploration, BestFirst for focused relevance-based crawling.

* * *

10\. Summary & Next Steps
-------------------------

In this **Deep Crawling with Crawl4AI** tutorial, you learned to:

*   Configure **BFSDeepCrawlStrategy**, **DFSDeepCrawlStrategy**, and **BestFirstCrawlingStrategy**
*   Process results in streaming or non-streaming mode
*   Apply filters to target specific content
*   Use scorers to prioritize the most relevant pages
*   Limit crawls with `max_pages` and `score_threshold` parameters
*   Build a complete advanced crawler with combined techniques

With these tools, you can efficiently extract structured data from websites at scale, focusing precisely on the content you need for your specific use case.

* * *

---

# Content Selection - Crawl4AI Documentation (v0.5.x)

Content Selection
=================

Crawl4AI provides multiple ways to **select**, **filter**, and **refine** the content from your crawls. Whether you need to target a specific CSS region, exclude entire tags, filter out external links, or remove certain domains and images, **`CrawlerRunConfig`** offers a wide range of parameters.

Below, we show how to configure these parameters and combine them for precise control.

* * *

1\. CSS-Based Selection
-----------------------

There are two ways to select content from a page: using `css_selector` or the more flexible `target_elements`.

### 1.1 Using `css_selector`

A straightforward way to **limit** your crawl results to a certain region of the page is **`css_selector`** in **`CrawlerRunConfig`**:

`[](#__codelineno-0-1) import asyncio [](#__codelineno-0-2) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig [](#__codelineno-0-3) [](#__codelineno-0-4) async def main(): [](#__codelineno-0-5)     config = CrawlerRunConfig( [](#__codelineno-0-6)         # e.g., first 30 items from Hacker News [](#__codelineno-0-7)         css_selector=".athing:nth-child(-n+30)"   [](#__codelineno-0-8)     ) [](#__codelineno-0-9)     async with AsyncWebCrawler() as crawler: [](#__codelineno-0-10)         result = await crawler.arun( [](#__codelineno-0-11)             url="https://news.ycombinator.com/newest",  [](#__codelineno-0-12)             config=config [](#__codelineno-0-13)         ) [](#__codelineno-0-14)         print("Partial HTML length:", len(result.cleaned_html)) [](#__codelineno-0-15) [](#__codelineno-0-16) if __name__ == "__main__": [](#__codelineno-0-17)     asyncio.run(main())`

**Result**: Only elements matching that selector remain in `result.cleaned_html`.

### 1.2 Using `target_elements`

The `target_elements` parameter provides more flexibility by allowing you to target **multiple elements** for content extraction while preserving the entire page context for other features:

`[](#__codelineno-1-1) import asyncio [](#__codelineno-1-2) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig [](#__codelineno-1-3) [](#__codelineno-1-4) async def main(): [](#__codelineno-1-5)     config = CrawlerRunConfig( [](#__codelineno-1-6)         # Target article body and sidebar, but not other content [](#__codelineno-1-7)         target_elements=["article.main-content", "aside.sidebar"] [](#__codelineno-1-8)     ) [](#__codelineno-1-9)     async with AsyncWebCrawler() as crawler: [](#__codelineno-1-10)         result = await crawler.arun( [](#__codelineno-1-11)             url="https://example.com/blog-post",  [](#__codelineno-1-12)             config=config [](#__codelineno-1-13)         ) [](#__codelineno-1-14)         print("Markdown focused on target elements") [](#__codelineno-1-15)         print("Links from entire page still available:", len(result.links.get("internal", []))) [](#__codelineno-1-16) [](#__codelineno-1-17) if __name__ == "__main__": [](#__codelineno-1-18)     asyncio.run(main())`

**Key difference**: With `target_elements`, the markdown generation and structural data extraction focus on those elements, but other page elements (like links, images, and tables) are still extracted from the entire page. This gives you fine-grained control over what appears in your markdown content while preserving full page context for link analysis and media collection.

* * *

2\. Content Filtering & Exclusions
----------------------------------

### 2.1 Basic Overview

`[](#__codelineno-2-1) config = CrawlerRunConfig( [](#__codelineno-2-2)     # Content thresholds [](#__codelineno-2-3)     word_count_threshold=10,        # Minimum words per block [](#__codelineno-2-4) [](#__codelineno-2-5)     # Tag exclusions [](#__codelineno-2-6)     excluded_tags=['form', 'header', 'footer', 'nav'], [](#__codelineno-2-7) [](#__codelineno-2-8)     # Link filtering [](#__codelineno-2-9)     exclude_external_links=True,     [](#__codelineno-2-10)     exclude_social_media_links=True, [](#__codelineno-2-11)     # Block entire domains [](#__codelineno-2-12)     exclude_domains=["adtrackers.com", "spammynews.org"],     [](#__codelineno-2-13)     exclude_social_media_domains=["facebook.com", "twitter.com"], [](#__codelineno-2-14) [](#__codelineno-2-15)     # Media filtering [](#__codelineno-2-16)     exclude_external_images=True [](#__codelineno-2-17) )`

**Explanation**:

*   **`word_count_threshold`**: Ignores text blocks under X words. Helps skip trivial blocks like short nav or disclaimers.
*   **`excluded_tags`**: Removes entire tags (`<form>`, `<header>`, `<footer>`, etc.).
*   **Link Filtering**:
*   `exclude_external_links`: Strips out external links and may remove them from `result.links`.
*   `exclude_social_media_links`: Removes links pointing to known social media domains.
*   `exclude_domains`: A custom list of domains to block if discovered in links.
*   `exclude_social_media_domains`: A curated list (override or add to it) for social media sites.
*   **Media Filtering**:
*   `exclude_external_images`: Discards images not hosted on the same domain as the main page (or its subdomains).

By default in case you set `exclude_social_media_links=True`, the following social media domains are excluded:

`[](#__codelineno-3-1) [ [](#__codelineno-3-2)     'facebook.com', [](#__codelineno-3-3)     'twitter.com', [](#__codelineno-3-4)     'x.com', [](#__codelineno-3-5)     'linkedin.com', [](#__codelineno-3-6)     'instagram.com', [](#__codelineno-3-7)     'pinterest.com', [](#__codelineno-3-8)     'tiktok.com', [](#__codelineno-3-9)     'snapchat.com', [](#__codelineno-3-10)     'reddit.com', [](#__codelineno-3-11) ]`

### 2.2 Example Usage

`[](#__codelineno-4-1) import asyncio [](#__codelineno-4-2) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode [](#__codelineno-4-3) [](#__codelineno-4-4) async def main(): [](#__codelineno-4-5)     config = CrawlerRunConfig( [](#__codelineno-4-6)         css_selector="main.content",  [](#__codelineno-4-7)         word_count_threshold=10, [](#__codelineno-4-8)         excluded_tags=["nav", "footer"], [](#__codelineno-4-9)         exclude_external_links=True, [](#__codelineno-4-10)         exclude_social_media_links=True, [](#__codelineno-4-11)         exclude_domains=["ads.com", "spammytrackers.net"], [](#__codelineno-4-12)         exclude_external_images=True, [](#__codelineno-4-13)         cache_mode=CacheMode.BYPASS [](#__codelineno-4-14)     ) [](#__codelineno-4-15) [](#__codelineno-4-16)     async with AsyncWebCrawler() as crawler: [](#__codelineno-4-17)         result = await crawler.arun(url="https://news.ycombinator.com", config=config) [](#__codelineno-4-18)         print("Cleaned HTML length:", len(result.cleaned_html)) [](#__codelineno-4-19) [](#__codelineno-4-20) if __name__ == "__main__": [](#__codelineno-4-21)     asyncio.run(main())`

**Note**: If these parameters remove too much, reduce or disable them accordingly.

* * *

3\. Handling Iframes
--------------------

Some sites embed content in `<iframe>` tags. If you want that inline:

`[](#__codelineno-5-1) config = CrawlerRunConfig( [](#__codelineno-5-2)     # Merge iframe content into the final output [](#__codelineno-5-3)     process_iframes=True,     [](#__codelineno-5-4)     remove_overlay_elements=True [](#__codelineno-5-5) )`

**Usage**:

`[](#__codelineno-6-1) import asyncio [](#__codelineno-6-2) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig [](#__codelineno-6-3) [](#__codelineno-6-4) async def main(): [](#__codelineno-6-5)     config = CrawlerRunConfig( [](#__codelineno-6-6)         process_iframes=True, [](#__codelineno-6-7)         remove_overlay_elements=True [](#__codelineno-6-8)     ) [](#__codelineno-6-9)     async with AsyncWebCrawler() as crawler: [](#__codelineno-6-10)         result = await crawler.arun( [](#__codelineno-6-11)             url="https://example.org/iframe-demo",  [](#__codelineno-6-12)             config=config [](#__codelineno-6-13)         ) [](#__codelineno-6-14)         print("Iframe-merged length:", len(result.cleaned_html)) [](#__codelineno-6-15) [](#__codelineno-6-16) if __name__ == "__main__": [](#__codelineno-6-17)     asyncio.run(main())`

* * *

4\. Structured Extraction Examples
----------------------------------

You can combine content selection with a more advanced extraction strategy. For instance, a **CSS-based** or **LLM-based** extraction strategy can run on the filtered HTML.

### 4.1 Pattern-Based with `JsonCssExtractionStrategy`

`[](#__codelineno-7-1) import asyncio [](#__codelineno-7-2) import json [](#__codelineno-7-3) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode [](#__codelineno-7-4) from crawl4ai.extraction_strategy import JsonCssExtractionStrategy [](#__codelineno-7-5) [](#__codelineno-7-6) async def main(): [](#__codelineno-7-7)     # Minimal schema for repeated items [](#__codelineno-7-8)     schema = { [](#__codelineno-7-9)         "name": "News Items", [](#__codelineno-7-10)         "baseSelector": "tr.athing", [](#__codelineno-7-11)         "fields": [ [](#__codelineno-7-12)             {"name": "title", "selector": "span.titleline a", "type": "text"}, [](#__codelineno-7-13)             { [](#__codelineno-7-14)                 "name": "link",  [](#__codelineno-7-15)                 "selector": "span.titleline a",  [](#__codelineno-7-16)                 "type": "attribute",  [](#__codelineno-7-17)                 "attribute": "href" [](#__codelineno-7-18)             } [](#__codelineno-7-19)         ] [](#__codelineno-7-20)     } [](#__codelineno-7-21) [](#__codelineno-7-22)     config = CrawlerRunConfig( [](#__codelineno-7-23)         # Content filtering [](#__codelineno-7-24)         excluded_tags=["form", "header"], [](#__codelineno-7-25)         exclude_domains=["adsite.com"], [](#__codelineno-7-26) [](#__codelineno-7-27)         # CSS selection or entire page [](#__codelineno-7-28)         css_selector="table.itemlist", [](#__codelineno-7-29) [](#__codelineno-7-30)         # No caching for demonstration [](#__codelineno-7-31)         cache_mode=CacheMode.BYPASS, [](#__codelineno-7-32) [](#__codelineno-7-33)         # Extraction strategy [](#__codelineno-7-34)         extraction_strategy=JsonCssExtractionStrategy(schema) [](#__codelineno-7-35)     ) [](#__codelineno-7-36) [](#__codelineno-7-37)     async with AsyncWebCrawler() as crawler: [](#__codelineno-7-38)         result = await crawler.arun( [](#__codelineno-7-39)             url="https://news.ycombinator.com/newest",  [](#__codelineno-7-40)             config=config [](#__codelineno-7-41)         ) [](#__codelineno-7-42)         data = json.loads(result.extracted_content) [](#__codelineno-7-43)         print("Sample extracted item:", data[:1])  # Show first item [](#__codelineno-7-44) [](#__codelineno-7-45) if __name__ == "__main__": [](#__codelineno-7-46)     asyncio.run(main())`

### 4.2 LLM-Based Extraction

`[](#__codelineno-8-1) import asyncio [](#__codelineno-8-2) import json [](#__codelineno-8-3) from pydantic import BaseModel, Field [](#__codelineno-8-4) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, LLMConfig [](#__codelineno-8-5) from crawl4ai.extraction_strategy import LLMExtractionStrategy [](#__codelineno-8-6) [](#__codelineno-8-7) class ArticleData(BaseModel): [](#__codelineno-8-8)     headline: str [](#__codelineno-8-9)     summary: str [](#__codelineno-8-10) [](#__codelineno-8-11) async def main(): [](#__codelineno-8-12)     llm_strategy = LLMExtractionStrategy( [](#__codelineno-8-13)         llm_config = LLMConfig(provider="openai/gpt-4",api_token="sk-YOUR_API_KEY") [](#__codelineno-8-14)         schema=ArticleData.schema(), [](#__codelineno-8-15)         extraction_type="schema", [](#__codelineno-8-16)         instruction="Extract 'headline' and a short 'summary' from the content." [](#__codelineno-8-17)     ) [](#__codelineno-8-18) [](#__codelineno-8-19)     config = CrawlerRunConfig( [](#__codelineno-8-20)         exclude_external_links=True, [](#__codelineno-8-21)         word_count_threshold=20, [](#__codelineno-8-22)         extraction_strategy=llm_strategy [](#__codelineno-8-23)     ) [](#__codelineno-8-24) [](#__codelineno-8-25)     async with AsyncWebCrawler() as crawler: [](#__codelineno-8-26)         result = await crawler.arun(url="https://news.ycombinator.com", config=config) [](#__codelineno-8-27)         article = json.loads(result.extracted_content) [](#__codelineno-8-28)         print(article) [](#__codelineno-8-29) [](#__codelineno-8-30) if __name__ == "__main__": [](#__codelineno-8-31)     asyncio.run(main())`

Here, the crawler:

*   Filters out external links (`exclude_external_links=True`).
*   Ignores very short text blocks (`word_count_threshold=20`).
*   Passes the final HTML to your LLM strategy for an AI-driven parse.

* * *

5\. Comprehensive Example
-------------------------

Below is a short function that unifies **CSS selection**, **exclusion** logic, and a pattern-based extraction, demonstrating how you can fine-tune your final data:

`[](#__codelineno-9-1) import asyncio [](#__codelineno-9-2) import json [](#__codelineno-9-3) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode [](#__codelineno-9-4) from crawl4ai.extraction_strategy import JsonCssExtractionStrategy [](#__codelineno-9-5) [](#__codelineno-9-6) async def extract_main_articles(url: str): [](#__codelineno-9-7)     schema = { [](#__codelineno-9-8)         "name": "ArticleBlock", [](#__codelineno-9-9)         "baseSelector": "div.article-block", [](#__codelineno-9-10)         "fields": [ [](#__codelineno-9-11)             {"name": "headline", "selector": "h2", "type": "text"}, [](#__codelineno-9-12)             {"name": "summary", "selector": ".summary", "type": "text"}, [](#__codelineno-9-13)             { [](#__codelineno-9-14)                 "name": "metadata", [](#__codelineno-9-15)                 "type": "nested", [](#__codelineno-9-16)                 "fields": [ [](#__codelineno-9-17)                     {"name": "author", "selector": ".author", "type": "text"}, [](#__codelineno-9-18)                     {"name": "date", "selector": ".date", "type": "text"} [](#__codelineno-9-19)                 ] [](#__codelineno-9-20)             } [](#__codelineno-9-21)         ] [](#__codelineno-9-22)     } [](#__codelineno-9-23) [](#__codelineno-9-24)     config = CrawlerRunConfig( [](#__codelineno-9-25)         # Keep only #main-content [](#__codelineno-9-26)         css_selector="#main-content", [](#__codelineno-9-27) [](#__codelineno-9-28)         # Filtering [](#__codelineno-9-29)         word_count_threshold=10, [](#__codelineno-9-30)         excluded_tags=["nav", "footer"],   [](#__codelineno-9-31)         exclude_external_links=True, [](#__codelineno-9-32)         exclude_domains=["somebadsite.com"], [](#__codelineno-9-33)         exclude_external_images=True, [](#__codelineno-9-34) [](#__codelineno-9-35)         # Extraction [](#__codelineno-9-36)         extraction_strategy=JsonCssExtractionStrategy(schema), [](#__codelineno-9-37) [](#__codelineno-9-38)         cache_mode=CacheMode.BYPASS [](#__codelineno-9-39)     ) [](#__codelineno-9-40) [](#__codelineno-9-41)     async with AsyncWebCrawler() as crawler: [](#__codelineno-9-42)         result = await crawler.arun(url=url, config=config) [](#__codelineno-9-43)         if not result.success: [](#__codelineno-9-44)             print(f"Error: {result.error_message}") [](#__codelineno-9-45)             return None [](#__codelineno-9-46)         return json.loads(result.extracted_content) [](#__codelineno-9-47) [](#__codelineno-9-48) async def main(): [](#__codelineno-9-49)     articles = await extract_main_articles("https://news.ycombinator.com/newest") [](#__codelineno-9-50)     if articles: [](#__codelineno-9-51)         print("Extracted Articles:", articles[:2])  # Show first 2 [](#__codelineno-9-52) [](#__codelineno-9-53) if __name__ == "__main__": [](#__codelineno-9-54)     asyncio.run(main())`

**Why This Works**: - **CSS** scoping with `#main-content`.  
\- Multiple **exclude\_** parameters to remove domains, external images, etc.  
\- A **JsonCssExtractionStrategy** to parse repeated article blocks.

* * *

6\. Scraping Modes
------------------

Crawl4AI provides two different scraping strategies for HTML content processing: `WebScrapingStrategy` (BeautifulSoup-based, default) and `LXMLWebScrapingStrategy` (LXML-based). The LXML strategy offers significantly better performance, especially for large HTML documents.

`[](#__codelineno-10-1) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, LXMLWebScrapingStrategy [](#__codelineno-10-2) [](#__codelineno-10-3) async def main(): [](#__codelineno-10-4)     config = CrawlerRunConfig( [](#__codelineno-10-5)         scraping_strategy=LXMLWebScrapingStrategy()  # Faster alternative to default BeautifulSoup [](#__codelineno-10-6)     ) [](#__codelineno-10-7)     async with AsyncWebCrawler() as crawler: [](#__codelineno-10-8)         result = await crawler.arun( [](#__codelineno-10-9)             url="https://example.com",  [](#__codelineno-10-10)             config=config [](#__codelineno-10-11)         )`

You can also create your own custom scraping strategy by inheriting from `ContentScrapingStrategy`. The strategy must return a `ScrapingResult` object with the following structure:

`[](#__codelineno-11-1) from crawl4ai import ContentScrapingStrategy, ScrapingResult, MediaItem, Media, Link, Links [](#__codelineno-11-2) [](#__codelineno-11-3) class CustomScrapingStrategy(ContentScrapingStrategy): [](#__codelineno-11-4)     def scrap(self, url: str, html: str, **kwargs) -> ScrapingResult: [](#__codelineno-11-5)         # Implement your custom scraping logic here [](#__codelineno-11-6)         return ScrapingResult( [](#__codelineno-11-7)             cleaned_html="<html>...</html>",  # Cleaned HTML content [](#__codelineno-11-8)             success=True,                     # Whether scraping was successful [](#__codelineno-11-9)             media=Media( [](#__codelineno-11-10)                 images=[                      # List of images found [](#__codelineno-11-11)                     MediaItem( [](#__codelineno-11-12)                         src="https://example.com/image.jpg", [](#__codelineno-11-13)                         alt="Image description", [](#__codelineno-11-14)                         desc="Surrounding text", [](#__codelineno-11-15)                         score=1, [](#__codelineno-11-16)                         type="image", [](#__codelineno-11-17)                         group_id=1, [](#__codelineno-11-18)                         format="jpg", [](#__codelineno-11-19)                         width=800 [](#__codelineno-11-20)                     ) [](#__codelineno-11-21)                 ], [](#__codelineno-11-22)                 videos=[],                    # List of videos (same structure as images) [](#__codelineno-11-23)                 audios=[]                     # List of audio files (same structure as images) [](#__codelineno-11-24)             ), [](#__codelineno-11-25)             links=Links( [](#__codelineno-11-26)                 internal=[                    # List of internal links [](#__codelineno-11-27)                     Link( [](#__codelineno-11-28)                         href="https://example.com/page", [](#__codelineno-11-29)                         text="Link text", [](#__codelineno-11-30)                         title="Link title", [](#__codelineno-11-31)                         base_domain="example.com" [](#__codelineno-11-32)                     ) [](#__codelineno-11-33)                 ], [](#__codelineno-11-34)                 external=[]                   # List of external links (same structure) [](#__codelineno-11-35)             ), [](#__codelineno-11-36)             metadata={                        # Additional metadata [](#__codelineno-11-37)                 "title": "Page Title", [](#__codelineno-11-38)                 "description": "Page description" [](#__codelineno-11-39)             } [](#__codelineno-11-40)         ) [](#__codelineno-11-41) [](#__codelineno-11-42)     async def ascrap(self, url: str, html: str, **kwargs) -> ScrapingResult: [](#__codelineno-11-43)         # For simple cases, you can use the sync version [](#__codelineno-11-44)         return await asyncio.to_thread(self.scrap, url, html, **kwargs)`

### Performance Considerations

The LXML strategy can be up to 10-20x faster than BeautifulSoup strategy, particularly when processing large HTML documents. However, please note:

1.  LXML strategy is currently experimental
2.  In some edge cases, the parsing results might differ slightly from BeautifulSoup
3.  If you encounter any inconsistencies between LXML and BeautifulSoup results, please [raise an issue](https://github.com/codeium/crawl4ai/issues)
     with a reproducible example

Choose LXML strategy when: - Processing large HTML documents (recommended for >100KB) - Performance is critical - Working with well-formed HTML

Stick to BeautifulSoup strategy (default) when: - Maximum compatibility is needed - Working with malformed HTML - Exact parsing behavior is critical

* * *

7\. Combining CSS Selection Methods
-----------------------------------

You can combine `css_selector` and `target_elements` in powerful ways to achieve fine-grained control over your output:

`[](#__codelineno-12-1) import asyncio [](#__codelineno-12-2) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode [](#__codelineno-12-3) [](#__codelineno-12-4) async def main(): [](#__codelineno-12-5)     # Target specific content but preserve page context [](#__codelineno-12-6)     config = CrawlerRunConfig( [](#__codelineno-12-7)         # Focus markdown on main content and sidebar [](#__codelineno-12-8)         target_elements=["#main-content", ".sidebar"], [](#__codelineno-12-9) [](#__codelineno-12-10)         # Global filters applied to entire page [](#__codelineno-12-11)         excluded_tags=["nav", "footer", "header"], [](#__codelineno-12-12)         exclude_external_links=True, [](#__codelineno-12-13) [](#__codelineno-12-14)         # Use basic content thresholds [](#__codelineno-12-15)         word_count_threshold=15, [](#__codelineno-12-16) [](#__codelineno-12-17)         cache_mode=CacheMode.BYPASS [](#__codelineno-12-18)     ) [](#__codelineno-12-19) [](#__codelineno-12-20)     async with AsyncWebCrawler() as crawler: [](#__codelineno-12-21)         result = await crawler.arun( [](#__codelineno-12-22)             url="https://example.com/article", [](#__codelineno-12-23)             config=config [](#__codelineno-12-24)         ) [](#__codelineno-12-25) [](#__codelineno-12-26)         print(f"Content focuses on specific elements, but all links still analyzed") [](#__codelineno-12-27)         print(f"Internal links: {len(result.links.get('internal', []))}") [](#__codelineno-12-28)         print(f"External links: {len(result.links.get('external', []))}") [](#__codelineno-12-29) [](#__codelineno-12-30) if __name__ == "__main__": [](#__codelineno-12-31)     asyncio.run(main())`

This approach gives you the best of both worlds: - Markdown generation and content extraction focus on the elements you care about - Links, images and other page data still give you the full context of the page - Content filtering still applies globally

8\. Conclusion
--------------

By mixing **target\_elements** or **css\_selector** scoping, **content filtering** parameters, and advanced **extraction strategies**, you can precisely **choose** which data to keep. Key parameters in **`CrawlerRunConfig`** for content selection include:

1.  **`target_elements`** – Array of CSS selectors to focus markdown generation and data extraction, while preserving full page context for links and media.
2.  **`css_selector`** – Basic scoping to an element or region for all extraction processes.
3.  **`word_count_threshold`** – Skip short blocks.
4.  **`excluded_tags`** – Remove entire HTML tags.
5.  **`exclude_external_links`**, **`exclude_social_media_links`**, **`exclude_domains`** – Filter out unwanted links or domains.
6.  **`exclude_external_images`** – Remove images from external sources.
7.  **`process_iframes`** – Merge iframe content if needed.

Combine these with structured extraction (CSS, LLM-based, or others) to build powerful crawls that yield exactly the content you want, from raw or cleaned HTML up to sophisticated JSON structures. For more detail, see [Configuration Reference](../../api/parameters/)
. Enjoy curating your data to the max!

* * *

---

# Docker Deployment - Crawl4AI Documentation (v0.5.x)

Docker Deployment
=================

Crawl4AI provides official Docker images for easy deployment and scalability. This guide covers installation, configuration, and usage of Crawl4AI in Docker environments.

Quick Start 🚀
--------------

Pull and run the basic version:

`[](#__codelineno-0-1) # Basic run without security [](#__codelineno-0-2) docker pull unclecode/crawl4ai:basic [](#__codelineno-0-3) docker run -p 11235:11235 unclecode/crawl4ai:basic [](#__codelineno-0-4) [](#__codelineno-0-5) # Run with API security enabled [](#__codelineno-0-6) docker run -p 11235:11235 -e CRAWL4AI_API_TOKEN=your_secret_token unclecode/crawl4ai:basic`

Running with Docker Compose 🐳
------------------------------

### Use Docker Compose (From Local Dockerfile or Docker Hub)

Crawl4AI provides flexibility to use Docker Compose for managing your containerized services. You can either build the image locally from the provided `Dockerfile` or use the pre-built image from Docker Hub.

### **Option 1: Using Docker Compose to Build Locally**

If you want to build the image locally, use the provided `docker-compose.local.yml` file.

`[](#__codelineno-1-1) docker-compose -f docker-compose.local.yml up -d`

This will: 1. Build the Docker image from the provided `Dockerfile`. 2. Start the container and expose it on `http://localhost:11235`.

* * *

### **Option 2: Using Docker Compose with Pre-Built Image from Hub**

If you prefer using the pre-built image on Docker Hub, use the `docker-compose.hub.yml` file.

`[](#__codelineno-2-1) docker-compose -f docker-compose.hub.yml up -d`

This will: 1. Pull the pre-built image `unclecode/crawl4ai:basic` (or `all`, depending on your configuration). 2. Start the container and expose it on `http://localhost:11235`.

* * *

### **Stopping the Running Services**

To stop the services started via Docker Compose, you can use:

`[](#__codelineno-3-1) docker-compose -f docker-compose.local.yml down [](#__codelineno-3-2) # OR [](#__codelineno-3-3) docker-compose -f docker-compose.hub.yml down`

If the containers don’t stop and the application is still running, check the running containers:

`[](#__codelineno-4-1) docker ps`

Find the `CONTAINER ID` of the running service and stop it forcefully:

`[](#__codelineno-5-1) docker stop <CONTAINER_ID>`

* * *

### **Debugging with Docker Compose**

*   **Check Logs**: To view the container logs:
    
    `[](#__codelineno-6-1) docker-compose -f docker-compose.local.yml logs -f`
    
*   **Remove Orphaned Containers**: If the service is still running unexpectedly:
    
    `[](#__codelineno-7-1) docker-compose -f docker-compose.local.yml down --remove-orphans`
    
*   **Manually Remove Network**: If the network is still in use:
    
    `[](#__codelineno-8-1) docker network ls [](#__codelineno-8-2) docker network rm crawl4ai_default`
    

* * *

### Why Use Docker Compose?

Docker Compose is the recommended way to deploy Crawl4AI because: 1. It simplifies multi-container setups. 2. Allows you to define environment variables, resources, and ports in a single file. 3. Makes it easier to switch between local development and production-ready images.

For example, your `docker-compose.yml` could include API keys, token settings, and memory limits, making deployment quick and consistent.

API Security 🔒
---------------

### Understanding CRAWL4AI\_API\_TOKEN

The `CRAWL4AI_API_TOKEN` provides optional security for your Crawl4AI instance:

*   If `CRAWL4AI_API_TOKEN` is set: All API endpoints (except `/health`) require authentication
*   If `CRAWL4AI_API_TOKEN` is not set: The API is publicly accessible

`[](#__codelineno-9-1) # Secured Instance [](#__codelineno-9-2) docker run -p 11235:11235 -e CRAWL4AI_API_TOKEN=your_secret_token unclecode/crawl4ai:all [](#__codelineno-9-3) [](#__codelineno-9-4) # Unsecured Instance [](#__codelineno-9-5) docker run -p 11235:11235 unclecode/crawl4ai:all`

### Making API Calls

For secured instances, include the token in all requests:

`[](#__codelineno-10-1) import requests [](#__codelineno-10-2) [](#__codelineno-10-3) # Setup headers if token is being used [](#__codelineno-10-4) api_token = "your_secret_token"  # Same token set in CRAWL4AI_API_TOKEN [](#__codelineno-10-5) headers = {"Authorization": f"Bearer {api_token}"} if api_token else {} [](#__codelineno-10-6) [](#__codelineno-10-7) # Making authenticated requests [](#__codelineno-10-8) response = requests.post( [](#__codelineno-10-9)     "http://localhost:11235/crawl", [](#__codelineno-10-10)     headers=headers, [](#__codelineno-10-11)     json={ [](#__codelineno-10-12)         "urls": "https://example.com", [](#__codelineno-10-13)         "priority": 10 [](#__codelineno-10-14)     } [](#__codelineno-10-15) ) [](#__codelineno-10-16) [](#__codelineno-10-17) # Checking task status [](#__codelineno-10-18) task_id = response.json()["task_id"] [](#__codelineno-10-19) status = requests.get( [](#__codelineno-10-20)     f"http://localhost:11235/task/{task_id}", [](#__codelineno-10-21)     headers=headers [](#__codelineno-10-22) )`

### Using with Docker Compose

In your `docker-compose.yml`:

`[](#__codelineno-11-1) services: [](#__codelineno-11-2)   crawl4ai: [](#__codelineno-11-3)     image: unclecode/crawl4ai:all [](#__codelineno-11-4)     environment: [](#__codelineno-11-5)       - CRAWL4AI_API_TOKEN=${CRAWL4AI_API_TOKEN:-}  # Optional [](#__codelineno-11-6)     # ... other configuration`

Then either: 1. Set in `.env` file:

`[](#__codelineno-12-1) CRAWL4AI_API_TOKEN=your_secret_token`

1.  Or set via command line:
    
    `[](#__codelineno-13-1) CRAWL4AI_API_TOKEN=your_secret_token docker-compose up`
    

> **Security Note**: If you enable the API token, make sure to keep it secure and never commit it to version control. The token will be required for all API endpoints except the health check endpoint (`/health`).

Configuration Options 🔧
------------------------

### Environment Variables

You can configure the service using environment variables:

`[](#__codelineno-14-1) # Basic configuration [](#__codelineno-14-2) docker run -p 11235:11235 \ [](#__codelineno-14-3)     -e MAX_CONCURRENT_TASKS=5 \ [](#__codelineno-14-4)     unclecode/crawl4ai:all [](#__codelineno-14-5) [](#__codelineno-14-6) # With security and LLM support [](#__codelineno-14-7) docker run -p 11235:11235 \ [](#__codelineno-14-8)     -e CRAWL4AI_API_TOKEN=your_secret_token \ [](#__codelineno-14-9)     -e OPENAI_API_KEY=sk-... \ [](#__codelineno-14-10)     -e ANTHROPIC_API_KEY=sk-ant-... \ [](#__codelineno-14-11)     unclecode/crawl4ai:all`

### Using Docker Compose (Recommended) 🐳

Create a `docker-compose.yml`:

`[](#__codelineno-15-1) version: '3.8' [](#__codelineno-15-2) [](#__codelineno-15-3) services: [](#__codelineno-15-4)   crawl4ai: [](#__codelineno-15-5)     image: unclecode/crawl4ai:all [](#__codelineno-15-6)     ports: [](#__codelineno-15-7)       - "11235:11235" [](#__codelineno-15-8)     environment: [](#__codelineno-15-9)       - CRAWL4AI_API_TOKEN=${CRAWL4AI_API_TOKEN:-}  # Optional API security [](#__codelineno-15-10)       - MAX_CONCURRENT_TASKS=5 [](#__codelineno-15-11)       # LLM Provider Keys [](#__codelineno-15-12)       - OPENAI_API_KEY=${OPENAI_API_KEY:-} [](#__codelineno-15-13)       - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY:-} [](#__codelineno-15-14)     volumes: [](#__codelineno-15-15)       - /dev/shm:/dev/shm [](#__codelineno-15-16)     deploy: [](#__codelineno-15-17)       resources: [](#__codelineno-15-18)         limits: [](#__codelineno-15-19)           memory: 4G [](#__codelineno-15-20)         reservations: [](#__codelineno-15-21)           memory: 1G`

You can run it in two ways:

1.  Using environment variables directly:
    
    `[](#__codelineno-16-1) CRAWL4AI_API_TOKEN=secret123 OPENAI_API_KEY=sk-... docker-compose up`
    
2.  Using a `.env` file (recommended): Create a `.env` file in the same directory:
    
    `[](#__codelineno-17-1) # API Security (optional) [](#__codelineno-17-2) CRAWL4AI_API_TOKEN=your_secret_token [](#__codelineno-17-3) [](#__codelineno-17-4) # LLM Provider Keys [](#__codelineno-17-5) OPENAI_API_KEY=sk-... [](#__codelineno-17-6) ANTHROPIC_API_KEY=sk-ant-... [](#__codelineno-17-7) [](#__codelineno-17-8) # Other Configuration [](#__codelineno-17-9) MAX_CONCURRENT_TASKS=5`
    

Then simply run:

`[](#__codelineno-18-1) docker-compose up`

### Testing the Deployment 🧪

`[](#__codelineno-19-1) import requests [](#__codelineno-19-2) [](#__codelineno-19-3) # For unsecured instances [](#__codelineno-19-4) def test_unsecured(): [](#__codelineno-19-5)     # Health check [](#__codelineno-19-6)     health = requests.get("http://localhost:11235/health") [](#__codelineno-19-7)     print("Health check:", health.json()) [](#__codelineno-19-8) [](#__codelineno-19-9)     # Basic crawl [](#__codelineno-19-10)     response = requests.post( [](#__codelineno-19-11)         "http://localhost:11235/crawl", [](#__codelineno-19-12)         json={ [](#__codelineno-19-13)             "urls": "https://www.nbcnews.com/business", [](#__codelineno-19-14)             "priority": 10 [](#__codelineno-19-15)         } [](#__codelineno-19-16)     ) [](#__codelineno-19-17)     task_id = response.json()["task_id"] [](#__codelineno-19-18)     print("Task ID:", task_id) [](#__codelineno-19-19) [](#__codelineno-19-20) # For secured instances [](#__codelineno-19-21) def test_secured(api_token): [](#__codelineno-19-22)     headers = {"Authorization": f"Bearer {api_token}"} [](#__codelineno-19-23) [](#__codelineno-19-24)     # Basic crawl with authentication [](#__codelineno-19-25)     response = requests.post( [](#__codelineno-19-26)         "http://localhost:11235/crawl", [](#__codelineno-19-27)         headers=headers, [](#__codelineno-19-28)         json={ [](#__codelineno-19-29)             "urls": "https://www.nbcnews.com/business", [](#__codelineno-19-30)             "priority": 10 [](#__codelineno-19-31)         } [](#__codelineno-19-32)     ) [](#__codelineno-19-33)     task_id = response.json()["task_id"] [](#__codelineno-19-34)     print("Task ID:", task_id)`

### LLM Extraction Example 🤖

When you've configured your LLM provider keys (via environment variables or `.env`), you can use LLM extraction:

`[](#__codelineno-20-1) request = { [](#__codelineno-20-2)     "urls": "https://example.com", [](#__codelineno-20-3)     "extraction_config": { [](#__codelineno-20-4)         "type": "llm", [](#__codelineno-20-5)         "params": { [](#__codelineno-20-6)             "provider": "openai/gpt-4", [](#__codelineno-20-7)             "instruction": "Extract main topics from the page" [](#__codelineno-20-8)         } [](#__codelineno-20-9)     } [](#__codelineno-20-10) } [](#__codelineno-20-11) [](#__codelineno-20-12) # Make the request (add headers if using API security) [](#__codelineno-20-13) response = requests.post("http://localhost:11235/crawl", json=request)`

> **Note**: Remember to add `.env` to your `.gitignore` to keep your API keys secure!

Usage Examples 📝
-----------------

### Basic Crawling

`[](#__codelineno-21-1) request = { [](#__codelineno-21-2)     "urls": "https://www.nbcnews.com/business", [](#__codelineno-21-3)     "priority": 10 [](#__codelineno-21-4) } [](#__codelineno-21-5) [](#__codelineno-21-6) response = requests.post("http://localhost:11235/crawl", json=request) [](#__codelineno-21-7) task_id = response.json()["task_id"] [](#__codelineno-21-8) [](#__codelineno-21-9) # Get results [](#__codelineno-21-10) result = requests.get(f"http://localhost:11235/task/{task_id}")`

### Structured Data Extraction

`[](#__codelineno-22-1) schema = { [](#__codelineno-22-2)     "name": "Crypto Prices", [](#__codelineno-22-3)     "baseSelector": ".cds-tableRow-t45thuk", [](#__codelineno-22-4)     "fields": [ [](#__codelineno-22-5)         { [](#__codelineno-22-6)             "name": "crypto", [](#__codelineno-22-7)             "selector": "td:nth-child(1) h2", [](#__codelineno-22-8)             "type": "text", [](#__codelineno-22-9)         }, [](#__codelineno-22-10)         { [](#__codelineno-22-11)             "name": "price", [](#__codelineno-22-12)             "selector": "td:nth-child(2)", [](#__codelineno-22-13)             "type": "text", [](#__codelineno-22-14)         } [](#__codelineno-22-15)     ], [](#__codelineno-22-16) } [](#__codelineno-22-17) [](#__codelineno-22-18) request = { [](#__codelineno-22-19)     "urls": "https://www.coinbase.com/explore", [](#__codelineno-22-20)     "extraction_config": { [](#__codelineno-22-21)         "type": "json_css", [](#__codelineno-22-22)         "params": {"schema": schema} [](#__codelineno-22-23)     } [](#__codelineno-22-24) }`

### Dynamic Content Handling

`[](#__codelineno-23-1) request = { [](#__codelineno-23-2)     "urls": "https://www.nbcnews.com/business", [](#__codelineno-23-3)     "js_code": [ [](#__codelineno-23-4)         "const loadMoreButton = Array.from(document.querySelectorAll('button')).find(button => button.textContent.includes('Load More')); loadMoreButton && loadMoreButton.click();" [](#__codelineno-23-5)     ], [](#__codelineno-23-6)     "wait_for": "article.tease-card:nth-child(10)" [](#__codelineno-23-7) }`

### AI-Powered Extraction (Full Version)

`[](#__codelineno-24-1) request = { [](#__codelineno-24-2)     "urls": "https://www.nbcnews.com/business", [](#__codelineno-24-3)     "extraction_config": { [](#__codelineno-24-4)         "type": "cosine", [](#__codelineno-24-5)         "params": { [](#__codelineno-24-6)             "semantic_filter": "business finance economy", [](#__codelineno-24-7)             "word_count_threshold": 10, [](#__codelineno-24-8)             "max_dist": 0.2, [](#__codelineno-24-9)             "top_k": 3 [](#__codelineno-24-10)         } [](#__codelineno-24-11)     } [](#__codelineno-24-12) }`

Platform-Specific Instructions 💻
---------------------------------

### macOS

`[](#__codelineno-25-1) docker pull unclecode/crawl4ai:basic [](#__codelineno-25-2) docker run -p 11235:11235 unclecode/crawl4ai:basic`

### Ubuntu

`[](#__codelineno-26-1) # Basic version [](#__codelineno-26-2) docker pull unclecode/crawl4ai:basic [](#__codelineno-26-3) docker run -p 11235:11235 unclecode/crawl4ai:basic [](#__codelineno-26-4) [](#__codelineno-26-5) # With GPU support [](#__codelineno-26-6) docker pull unclecode/crawl4ai:gpu [](#__codelineno-26-7) docker run --gpus all -p 11235:11235 unclecode/crawl4ai:gpu`

### Windows (PowerShell)

`[](#__codelineno-27-1) docker pull unclecode/crawl4ai:basic [](#__codelineno-27-2) docker run -p 11235:11235 unclecode/crawl4ai:basic`

Testing 🧪
----------

Save this as `test_docker.py`:

`[](#__codelineno-28-1) import requests [](#__codelineno-28-2) import json [](#__codelineno-28-3) import time [](#__codelineno-28-4) import sys [](#__codelineno-28-5) [](#__codelineno-28-6) class Crawl4AiTester: [](#__codelineno-28-7)     def __init__(self, base_url: str = "http://localhost:11235"): [](#__codelineno-28-8)         self.base_url = base_url [](#__codelineno-28-9) [](#__codelineno-28-10)     def submit_and_wait(self, request_data: dict, timeout: int = 300) -> dict: [](#__codelineno-28-11)         # Submit crawl job [](#__codelineno-28-12)         response = requests.post(f"{self.base_url}/crawl", json=request_data) [](#__codelineno-28-13)         task_id = response.json()["task_id"] [](#__codelineno-28-14)         print(f"Task ID: {task_id}") [](#__codelineno-28-15) [](#__codelineno-28-16)         # Poll for result [](#__codelineno-28-17)         start_time = time.time() [](#__codelineno-28-18)         while True: [](#__codelineno-28-19)             if time.time() - start_time > timeout: [](#__codelineno-28-20)                 raise TimeoutError(f"Task {task_id} timeout") [](#__codelineno-28-21) [](#__codelineno-28-22)             result = requests.get(f"{self.base_url}/task/{task_id}") [](#__codelineno-28-23)             status = result.json() [](#__codelineno-28-24) [](#__codelineno-28-25)             if status["status"] == "completed": [](#__codelineno-28-26)                 return status [](#__codelineno-28-27) [](#__codelineno-28-28)             time.sleep(2) [](#__codelineno-28-29) [](#__codelineno-28-30) def test_deployment(): [](#__codelineno-28-31)     tester = Crawl4AiTester() [](#__codelineno-28-32) [](#__codelineno-28-33)     # Test basic crawl [](#__codelineno-28-34)     request = { [](#__codelineno-28-35)         "urls": "https://www.nbcnews.com/business", [](#__codelineno-28-36)         "priority": 10 [](#__codelineno-28-37)     } [](#__codelineno-28-38) [](#__codelineno-28-39)     result = tester.submit_and_wait(request) [](#__codelineno-28-40)     print("Basic crawl successful!") [](#__codelineno-28-41)     print(f"Content length: {len(result['result']['markdown'])}") [](#__codelineno-28-42) [](#__codelineno-28-43) if __name__ == "__main__": [](#__codelineno-28-44)     test_deployment()`

Advanced Configuration ⚙️
-------------------------

### Crawler Parameters

The `crawler_params` field allows you to configure the browser instance and crawling behavior. Here are key parameters you can use:

`[](#__codelineno-29-1) request = { [](#__codelineno-29-2)     "urls": "https://example.com", [](#__codelineno-29-3)     "crawler_params": { [](#__codelineno-29-4)         # Browser Configuration [](#__codelineno-29-5)         "headless": True,                    # Run in headless mode [](#__codelineno-29-6)         "browser_type": "chromium",          # chromium/firefox/webkit [](#__codelineno-29-7)         "user_agent": "custom-agent",        # Custom user agent [](#__codelineno-29-8)         "proxy": "http://proxy:8080",        # Proxy configuration [](#__codelineno-29-9) [](#__codelineno-29-10)         # Performance & Behavior [](#__codelineno-29-11)         "page_timeout": 30000,               # Page load timeout (ms) [](#__codelineno-29-12)         "verbose": True,                     # Enable detailed logging [](#__codelineno-29-13)         "semaphore_count": 5,               # Concurrent request limit [](#__codelineno-29-14) [](#__codelineno-29-15)         # Anti-Detection Features [](#__codelineno-29-16)         "simulate_user": True,               # Simulate human behavior [](#__codelineno-29-17)         "magic": True,                       # Advanced anti-detection [](#__codelineno-29-18)         "override_navigator": True,          # Override navigator properties [](#__codelineno-29-19) [](#__codelineno-29-20)         # Session Management [](#__codelineno-29-21)         "user_data_dir": "./browser-data",   # Browser profile location [](#__codelineno-29-22)         "use_managed_browser": True,         # Use persistent browser [](#__codelineno-29-23)     } [](#__codelineno-29-24) }`

### Extra Parameters

The `extra` field allows passing additional parameters directly to the crawler's `arun` function:

`[](#__codelineno-30-1) request = { [](#__codelineno-30-2)     "urls": "https://example.com", [](#__codelineno-30-3)     "extra": { [](#__codelineno-30-4)         "word_count_threshold": 10,          # Min words per block [](#__codelineno-30-5)         "only_text": True,                   # Extract only text [](#__codelineno-30-6)         "bypass_cache": True,                # Force fresh crawl [](#__codelineno-30-7)         "process_iframes": True,             # Include iframe content [](#__codelineno-30-8)     } [](#__codelineno-30-9) }`

### Complete Examples

1. **Advanced News Crawling**

`[](#__codelineno-31-1) request = { [](#__codelineno-31-2)     "urls": "https://www.nbcnews.com/business", [](#__codelineno-31-3)     "crawler_params": { [](#__codelineno-31-4)         "headless": True, [](#__codelineno-31-5)         "page_timeout": 30000, [](#__codelineno-31-6)         "remove_overlay_elements": True      # Remove popups [](#__codelineno-31-7)     }, [](#__codelineno-31-8)     "extra": { [](#__codelineno-31-9)         "word_count_threshold": 50,          # Longer content blocks [](#__codelineno-31-10)         "bypass_cache": True                 # Fresh content [](#__codelineno-31-11)     }, [](#__codelineno-31-12)     "css_selector": ".article-body" [](#__codelineno-31-13) }`

2. **Anti-Detection Configuration**

`[](#__codelineno-32-1) request = { [](#__codelineno-32-2)     "urls": "https://example.com", [](#__codelineno-32-3)     "crawler_params": { [](#__codelineno-32-4)         "simulate_user": True, [](#__codelineno-32-5)         "magic": True, [](#__codelineno-32-6)         "override_navigator": True, [](#__codelineno-32-7)         "user_agent": "Mozilla/5.0 ...", [](#__codelineno-32-8)         "headers": { [](#__codelineno-32-9)             "Accept-Language": "en-US,en;q=0.9" [](#__codelineno-32-10)         } [](#__codelineno-32-11)     } [](#__codelineno-32-12) }`

3. **LLM Extraction with Custom Parameters**

`[](#__codelineno-33-1) request = { [](#__codelineno-33-2)     "urls": "https://openai.com/pricing", [](#__codelineno-33-3)     "extraction_config": { [](#__codelineno-33-4)         "type": "llm", [](#__codelineno-33-5)         "params": { [](#__codelineno-33-6)             "provider": "openai/gpt-4", [](#__codelineno-33-7)             "schema": pricing_schema [](#__codelineno-33-8)         } [](#__codelineno-33-9)     }, [](#__codelineno-33-10)     "crawler_params": { [](#__codelineno-33-11)         "verbose": True, [](#__codelineno-33-12)         "page_timeout": 60000 [](#__codelineno-33-13)     }, [](#__codelineno-33-14)     "extra": { [](#__codelineno-33-15)         "word_count_threshold": 1, [](#__codelineno-33-16)         "only_text": True [](#__codelineno-33-17)     } [](#__codelineno-33-18) }`

4. **Session-Based Dynamic Content**

`[](#__codelineno-34-1) request = { [](#__codelineno-34-2)     "urls": "https://example.com", [](#__codelineno-34-3)     "crawler_params": { [](#__codelineno-34-4)         "session_id": "dynamic_session", [](#__codelineno-34-5)         "headless": False, [](#__codelineno-34-6)         "page_timeout": 60000 [](#__codelineno-34-7)     }, [](#__codelineno-34-8)     "js_code": ["window.scrollTo(0, document.body.scrollHeight);"], [](#__codelineno-34-9)     "wait_for": "js:() => document.querySelectorAll('.item').length > 10", [](#__codelineno-34-10)     "extra": { [](#__codelineno-34-11)         "delay_before_return_html": 2.0 [](#__codelineno-34-12)     } [](#__codelineno-34-13) }`

5. **Screenshot with Custom Timing**

`[](#__codelineno-35-1) request = { [](#__codelineno-35-2)     "urls": "https://example.com", [](#__codelineno-35-3)     "screenshot": True, [](#__codelineno-35-4)     "crawler_params": { [](#__codelineno-35-5)         "headless": True, [](#__codelineno-35-6)         "screenshot_wait_for": ".main-content" [](#__codelineno-35-7)     }, [](#__codelineno-35-8)     "extra": { [](#__codelineno-35-9)         "delay_before_return_html": 3.0 [](#__codelineno-35-10)     } [](#__codelineno-35-11) }`

### Parameter Reference Table

| Category       | Parameter                   | Type  | Description                  |
| -------------- | --------------------------- | ----- | ---------------------------- |
| Browser        | headless                    | bool  | Run browser in headless mode |
| Browser        | browser\_type               | str   | Browser engine selection     |
| Browser        | user\_agent                 | str   | Custom user agent string     |
| Network        | proxy                       | str   | Proxy server URL             |
| Network        | headers                     | dict  | Custom HTTP headers          |
| Timing         | page\_timeout               | int   | Page load timeout (ms)       |
| Timing         | delay\_before\_return\_html | float | Wait before capture          |
| Anti-Detection | simulate\_user              | bool  | Human behavior simulation    |
| Anti-Detection | magic                       | bool  | Advanced protection          |
| Session        | session\_id                 | str   | Browser session ID           |
| Session        | user\_data\_dir             | str   | Profile directory            |
| Content        | word\_count\_threshold      | int   | Minimum words per block      |
| Content        | only\_text                  | bool  | Text-only extraction         |
| Content        | process\_iframes            | bool  | Include iframe content       |
| Debug          | verbose                     | bool  | Detailed logging             |
| Debug          | log\_console                | bool  | Browser console logs         |

Troubleshooting 🔍
------------------

### Common Issues

1. **Connection Refused**

`[](#__codelineno-36-1) Error: Connection refused at localhost:11235`

Solution: Ensure the container is running and ports are properly mapped.

2. **Resource Limits**

`[](#__codelineno-37-1) Error: No available slots`

Solution: Increase MAX\_CONCURRENT\_TASKS or container resources.

3. **GPU Access**

`[](#__codelineno-38-1) Error: GPU not found`

Solution: Ensure proper NVIDIA drivers and use `--gpus all` flag.

### Debug Mode

Access container for debugging:

`[](#__codelineno-39-1) docker run -it --entrypoint /bin/bash unclecode/crawl4ai:all`

View container logs:

`[](#__codelineno-40-1) docker logs [container_id]`

Best Practices 🌟
-----------------

1. **Resource Management** - Set appropriate memory and CPU limits - Monitor resource usage via health endpoint - Use basic version for simple crawling tasks

2. **Scaling** - Use multiple containers for high load - Implement proper load balancing - Monitor performance metrics

3. **Security** - Use environment variables for sensitive data - Implement proper network isolation - Regular security updates

API Reference 📚
----------------

### Health Check

`[](#__codelineno-41-1) GET /health`

### Submit Crawl Task

`[](#__codelineno-42-1) POST /crawl [](#__codelineno-42-2) Content-Type: application/json [](#__codelineno-42-3) [](#__codelineno-42-4) { [](#__codelineno-42-5)     "urls": "string or array", [](#__codelineno-42-6)     "extraction_config": { [](#__codelineno-42-7)         "type": "basic|llm|cosine|json_css", [](#__codelineno-42-8)         "params": {} [](#__codelineno-42-9)     }, [](#__codelineno-42-10)     "priority": 1-10, [](#__codelineno-42-11)     "ttl": 3600 [](#__codelineno-42-12) }`

### Get Task Status

`[](#__codelineno-43-1) GET /task/{task_id}`

For more details, visit the [official documentation](https://docs.crawl4ai.com/)
.

* * *

---

# Installation - Crawl4AI Documentation (v0.5.x)

Installation & Setup (2023 Edition)
===================================

1\. Basic Installation
----------------------

`[](#__codelineno-0-1) pip install crawl4ai`

This installs the **core** Crawl4AI library along with essential dependencies. **No** advanced features (like transformers or PyTorch) are included yet.

2\. Initial Setup & Diagnostics
-------------------------------

### 2.1 Run the Setup Command

After installing, call:

`[](#__codelineno-1-1) crawl4ai-setup`

**What does it do?** - Installs or updates required Playwright browsers (Chromium, Firefox, etc.) - Performs OS-level checks (e.g., missing libs on Linux) - Confirms your environment is ready to crawl

### 2.2 Diagnostics

Optionally, you can run **diagnostics** to confirm everything is functioning:

`[](#__codelineno-2-1) crawl4ai-doctor`

This command attempts to: - Check Python version compatibility - Verify Playwright installation - Inspect environment variables or library conflicts

If any issues arise, follow its suggestions (e.g., installing additional system packages) and re-run `crawl4ai-setup`.

* * *

3\. Verifying Installation: A Simple Crawl (Skip this step if you already run `crawl4ai-doctor`)
------------------------------------------------------------------------------------------------

Below is a minimal Python script demonstrating a **basic** crawl. It uses our new **`BrowserConfig`** and **`CrawlerRunConfig`** for clarity, though no custom settings are passed in this example:

`[](#__codelineno-3-1) import asyncio [](#__codelineno-3-2) from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig [](#__codelineno-3-3) [](#__codelineno-3-4) async def main(): [](#__codelineno-3-5)     async with AsyncWebCrawler() as crawler: [](#__codelineno-3-6)         result = await crawler.arun( [](#__codelineno-3-7)             url="https://www.example.com", [](#__codelineno-3-8)         ) [](#__codelineno-3-9)         print(result.markdown[:300])  # Show the first 300 characters of extracted text [](#__codelineno-3-10) [](#__codelineno-3-11) if __name__ == "__main__": [](#__codelineno-3-12)     asyncio.run(main())`

**Expected** outcome: - A headless browser session loads `example.com` - Crawl4AI returns ~300 characters of markdown.  
If errors occur, rerun `crawl4ai-doctor` or manually ensure Playwright is installed correctly.

* * *

4\. Advanced Installation (Optional)
------------------------------------

**Warning**: Only install these **if you truly need them**. They bring in larger dependencies, including big models, which can increase disk usage and memory load significantly.

### 4.1 Torch, Transformers, or All

*   **Text Clustering (Torch)**  
    
    `[](#__codelineno-4-1) pip install crawl4ai[torch] [](#__codelineno-4-2) crawl4ai-setup`
    
    Installs PyTorch-based features (e.g., cosine similarity or advanced semantic chunking).
    
*   **Transformers**  
    
    `[](#__codelineno-5-1) pip install crawl4ai[transformer] [](#__codelineno-5-2) crawl4ai-setup`
    
    Adds Hugging Face-based summarization or generation strategies.
    
*   **All Features**  
    
    `[](#__codelineno-6-1) pip install crawl4ai[all] [](#__codelineno-6-2) crawl4ai-setup`
    

#### (Optional) Pre-Fetching Models

`[](#__codelineno-7-1) crawl4ai-download-models`

This step caches large models locally (if needed). **Only do this** if your workflow requires them.

* * *

5\. Docker (Experimental)
-------------------------

We provide a **temporary** Docker approach for testing. **It’s not stable and may break** with future releases. We plan a major Docker revamp in a future stable version, 2025 Q1. If you still want to try:

`[](#__codelineno-8-1) docker pull unclecode/crawl4ai:basic [](#__codelineno-8-2) docker run -p 11235:11235 unclecode/crawl4ai:basic`

You can then make POST requests to `http://localhost:11235/crawl` to perform crawls. **Production usage** is discouraged until our new Docker approach is ready (planned in Jan or Feb 2025).

* * *

6\. Local Server Mode (Legacy)
------------------------------

Some older docs mention running Crawl4AI as a local server. This approach has been **partially replaced** by the new Docker-based prototype and upcoming stable server release. You can experiment, but expect major changes. Official local server instructions will arrive once the new Docker architecture is finalized.

* * *

Summary
-------

1. **Install** with `pip install crawl4ai` and run `crawl4ai-setup`. 2. **Diagnose** with `crawl4ai-doctor` if you see errors. 3. **Verify** by crawling `example.com` with minimal `BrowserConfig` + `CrawlerRunConfig`. 4. **Advanced** features (Torch, Transformers) are **optional**—avoid them if you don’t need them (they significantly increase resource usage). 5. **Docker** is **experimental**—use at your own risk until the stable version is released. 6. **Local server** references in older docs are largely deprecated; a new solution is in progress.

**Got questions?** Check [GitHub issues](https://github.com/unclecode/crawl4ai/issues)
 for updates or ask the community!

* * *

---

# Fit Markdown - Crawl4AI Documentation (v0.5.x)

Fit Markdown with Pruning & BM25
================================

**Fit Markdown** is a specialized **filtered** version of your page’s markdown, focusing on the most relevant content. By default, Crawl4AI converts the entire HTML into a broad **raw\_markdown**. With fit markdown, we apply a **content filter** algorithm (e.g., **Pruning** or **BM25**) to remove or rank low-value sections—such as repetitive sidebars, shallow text blocks, or irrelevancies—leaving a concise textual “core.”

* * *

1\. How “Fit Markdown” Works
----------------------------

### 1.1 The `content_filter`

In **`CrawlerRunConfig`**, you can specify a **`content_filter`** to shape how content is pruned or ranked before final markdown generation. A filter’s logic is applied **before** or **during** the HTML→Markdown process, producing:

*   **`result.markdown.raw_markdown`** (unfiltered)
*   **`result.markdown.fit_markdown`** (filtered or “fit” version)
*   **`result.markdown.fit_html`** (the corresponding HTML snippet that produced `fit_markdown`)

### 1.2 Common Filters

1. **PruningContentFilter** – Scores each node by text density, link density, and tag importance, discarding those below a threshold.  
2. **BM25ContentFilter** – Focuses on textual relevance using BM25 ranking, especially useful if you have a specific user query (e.g., “machine learning” or “food nutrition”).

* * *

2\. PruningContentFilter
------------------------

**Pruning** discards less relevant nodes based on **text density, link density, and tag importance**. It’s a heuristic-based approach—if certain sections appear too “thin” or too “spammy,” they’re pruned.

### 2.1 Usage Example

`[](#__codelineno-0-1) import asyncio [](#__codelineno-0-2) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig [](#__codelineno-0-3) from crawl4ai.content_filter_strategy import PruningContentFilter [](#__codelineno-0-4) from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator [](#__codelineno-0-5) [](#__codelineno-0-6) async def main(): [](#__codelineno-0-7)     # Step 1: Create a pruning filter [](#__codelineno-0-8)     prune_filter = PruningContentFilter( [](#__codelineno-0-9)         # Lower → more content retained, higher → more content pruned [](#__codelineno-0-10)         threshold=0.45,            [](#__codelineno-0-11)         # "fixed" or "dynamic" [](#__codelineno-0-12)         threshold_type="dynamic",   [](#__codelineno-0-13)         # Ignore nodes with <5 words [](#__codelineno-0-14)         min_word_threshold=5       [](#__codelineno-0-15)     ) [](#__codelineno-0-16) [](#__codelineno-0-17)     # Step 2: Insert it into a Markdown Generator [](#__codelineno-0-18)     md_generator = DefaultMarkdownGenerator(content_filter=prune_filter) [](#__codelineno-0-19) [](#__codelineno-0-20)     # Step 3: Pass it to CrawlerRunConfig [](#__codelineno-0-21)     config = CrawlerRunConfig( [](#__codelineno-0-22)         markdown_generator=md_generator [](#__codelineno-0-23)     ) [](#__codelineno-0-24) [](#__codelineno-0-25)     async with AsyncWebCrawler() as crawler: [](#__codelineno-0-26)         result = await crawler.arun( [](#__codelineno-0-27)             url="https://news.ycombinator.com",  [](#__codelineno-0-28)             config=config [](#__codelineno-0-29)         ) [](#__codelineno-0-30) [](#__codelineno-0-31)         if result.success: [](#__codelineno-0-32)             # 'fit_markdown' is your pruned content, focusing on "denser" text [](#__codelineno-0-33)             print("Raw Markdown length:", len(result.markdown.raw_markdown)) [](#__codelineno-0-34)             print("Fit Markdown length:", len(result.markdown.fit_markdown)) [](#__codelineno-0-35)         else: [](#__codelineno-0-36)             print("Error:", result.error_message) [](#__codelineno-0-37) [](#__codelineno-0-38) if __name__ == "__main__": [](#__codelineno-0-39)     asyncio.run(main())`

### 2.2 Key Parameters

*   **`min_word_threshold`** (int): If a block has fewer words than this, it’s pruned.
*   **`threshold_type`** (str):
*   `"fixed"` → each node must exceed `threshold` (0–1).
*   `"dynamic"` → node scoring adjusts according to tag type, text/link density, etc.
*   **`threshold`** (float, default ~0.48): The base or “anchor” cutoff.

**Algorithmic Factors**:

*   **Text density** – Encourages blocks that have a higher ratio of text to overall content.
*   **Link density** – Penalizes sections that are mostly links.
*   **Tag importance** – e.g., an `<article>` or `<p>` might be more important than a `<div>`.
*   **Structural context** – If a node is deeply nested or in a suspected sidebar, it might be deprioritized.

* * *

3\. BM25ContentFilter
---------------------

**BM25** is a classical text ranking algorithm often used in search engines. If you have a **user query** or rely on page metadata to derive a query, BM25 can identify which text chunks best match that query.

### 3.1 Usage Example

`[](#__codelineno-1-1) import asyncio [](#__codelineno-1-2) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig [](#__codelineno-1-3) from crawl4ai.content_filter_strategy import BM25ContentFilter [](#__codelineno-1-4) from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator [](#__codelineno-1-5) [](#__codelineno-1-6) async def main(): [](#__codelineno-1-7)     # 1) A BM25 filter with a user query [](#__codelineno-1-8)     bm25_filter = BM25ContentFilter( [](#__codelineno-1-9)         user_query="startup fundraising tips", [](#__codelineno-1-10)         # Adjust for stricter or looser results [](#__codelineno-1-11)         bm25_threshold=1.2   [](#__codelineno-1-12)     ) [](#__codelineno-1-13) [](#__codelineno-1-14)     # 2) Insert into a Markdown Generator [](#__codelineno-1-15)     md_generator = DefaultMarkdownGenerator(content_filter=bm25_filter) [](#__codelineno-1-16) [](#__codelineno-1-17)     # 3) Pass to crawler config [](#__codelineno-1-18)     config = CrawlerRunConfig( [](#__codelineno-1-19)         markdown_generator=md_generator [](#__codelineno-1-20)     ) [](#__codelineno-1-21) [](#__codelineno-1-22)     async with AsyncWebCrawler() as crawler: [](#__codelineno-1-23)         result = await crawler.arun( [](#__codelineno-1-24)             url="https://news.ycombinator.com",  [](#__codelineno-1-25)             config=config [](#__codelineno-1-26)         ) [](#__codelineno-1-27)         if result.success: [](#__codelineno-1-28)             print("Fit Markdown (BM25 query-based):") [](#__codelineno-1-29)             print(result.markdown.fit_markdown) [](#__codelineno-1-30)         else: [](#__codelineno-1-31)             print("Error:", result.error_message) [](#__codelineno-1-32) [](#__codelineno-1-33) if __name__ == "__main__": [](#__codelineno-1-34)     asyncio.run(main())`

### 3.2 Parameters

*   **`user_query`** (str, optional): E.g. `"machine learning"`. If blank, the filter tries to glean a query from page metadata.
*   **`bm25_threshold`** (float, default 1.0):
*   Higher → fewer chunks but more relevant.
*   Lower → more inclusive.

> In more advanced scenarios, you might see parameters like `use_stemming`, `case_sensitive`, or `priority_tags` to refine how text is tokenized or weighted.

* * *

4\. Accessing the “Fit” Output
------------------------------

After the crawl, your “fit” content is found in **`result.markdown.fit_markdown`**.

`[](#__codelineno-2-1) fit_md = result.markdown.fit_markdown [](#__codelineno-2-2) fit_html = result.markdown.fit_html`

If the content filter is **BM25**, you might see additional logic or references in `fit_markdown` that highlight relevant segments. If it’s **Pruning**, the text is typically well-cleaned but not necessarily matched to a query.

* * *

5\. Code Patterns Recap
-----------------------

### 5.1 Pruning

`[](#__codelineno-3-1) prune_filter = PruningContentFilter( [](#__codelineno-3-2)     threshold=0.5, [](#__codelineno-3-3)     threshold_type="fixed", [](#__codelineno-3-4)     min_word_threshold=10 [](#__codelineno-3-5) ) [](#__codelineno-3-6) md_generator = DefaultMarkdownGenerator(content_filter=prune_filter) [](#__codelineno-3-7) config = CrawlerRunConfig(markdown_generator=md_generator)`

### 5.2 BM25

`[](#__codelineno-4-1) bm25_filter = BM25ContentFilter( [](#__codelineno-4-2)     user_query="health benefits fruit", [](#__codelineno-4-3)     bm25_threshold=1.2 [](#__codelineno-4-4) ) [](#__codelineno-4-5) md_generator = DefaultMarkdownGenerator(content_filter=bm25_filter) [](#__codelineno-4-6) config = CrawlerRunConfig(markdown_generator=md_generator)`

* * *

6\. Combining with “word\_count\_threshold” & Exclusions
--------------------------------------------------------

Remember you can also specify:

`[](#__codelineno-5-1) config = CrawlerRunConfig( [](#__codelineno-5-2)     word_count_threshold=10, [](#__codelineno-5-3)     excluded_tags=["nav", "footer", "header"], [](#__codelineno-5-4)     exclude_external_links=True, [](#__codelineno-5-5)     markdown_generator=DefaultMarkdownGenerator( [](#__codelineno-5-6)         content_filter=PruningContentFilter(threshold=0.5) [](#__codelineno-5-7)     ) [](#__codelineno-5-8) )`

Thus, **multi-level** filtering occurs:

1.  The crawler’s `excluded_tags` are removed from the HTML first.
2.  The content filter (Pruning, BM25, or custom) prunes or ranks the remaining text blocks.
3.  The final “fit” content is generated in `result.markdown.fit_markdown`.

* * *

7\. Custom Filters
------------------

If you need a different approach (like a specialized ML model or site-specific heuristics), you can create a new class inheriting from `RelevantContentFilter` and implement `filter_content(html)`. Then inject it into your **markdown generator**:

`[](#__codelineno-6-1) from crawl4ai.content_filter_strategy import RelevantContentFilter [](#__codelineno-6-2) [](#__codelineno-6-3) class MyCustomFilter(RelevantContentFilter): [](#__codelineno-6-4)     def filter_content(self, html, min_word_threshold=None): [](#__codelineno-6-5)         # parse HTML, implement custom logic [](#__codelineno-6-6)         return [block for block in ... if ... some condition...]`

**Steps**:

1.  Subclass `RelevantContentFilter`.
2.  Implement `filter_content(...)`.
3.  Use it in your `DefaultMarkdownGenerator(content_filter=MyCustomFilter(...))`.

* * *

8\. Final Thoughts
------------------

**Fit Markdown** is a crucial feature for:

*   **Summaries**: Quickly get the important text from a cluttered page.
*   **Search**: Combine with **BM25** to produce content relevant to a query.
*   **AI Pipelines**: Filter out boilerplate so LLM-based extraction or summarization runs on denser text.

**Key Points**: - **PruningContentFilter**: Great if you just want the “meatiest” text without a user query.  
\- **BM25ContentFilter**: Perfect for query-based extraction or searching.  
\- Combine with **`excluded_tags`, `exclude_external_links`, `word_count_threshold`** to refine your final “fit” text.  
\- Fit markdown ends up in **`result.markdown.fit_markdown`**; eventually **`result.markdown.fit_markdown`** in future versions.

With these tools, you can **zero in** on the text that truly matters, ignoring spammy or boilerplate content, and produce a concise, relevant “fit markdown” for your AI or data pipelines. Happy pruning and searching!

*   Last Updated: 2025-01-01

* * *

---

# Link & Media - Crawl4AI Documentation (v0.5.x)

Link & Media
============

In this tutorial, you’ll learn how to:

1.  Extract links (internal, external) from crawled pages
2.  Filter or exclude specific domains (e.g., social media or custom domains)
3.  Access and manage media data (especially images) in the crawl result
4.  Configure your crawler to exclude or prioritize certain images

> **Prerequisites**  
> \- You have completed or are familiar with the [AsyncWebCrawler Basics](../simple-crawling/)
>  tutorial.  
> \- You can run Crawl4AI in your environment (Playwright, Python, etc.).

* * *

Below is a revised version of the **Link Extraction** and **Media Extraction** sections that includes example data structures showing how links and media items are stored in `CrawlResult`. Feel free to adjust any field names or descriptions to match your actual output.

* * *

1\. Link Extraction
-------------------

### 1.1 `result.links`

When you call `arun()` or `arun_many()` on a URL, Crawl4AI automatically extracts links and stores them in the `links` field of `CrawlResult`. By default, the crawler tries to distinguish **internal** links (same domain) from **external** links (different domains).

**Basic Example**:

`[](#__codelineno-0-1) from crawl4ai import AsyncWebCrawler [](#__codelineno-0-2) [](#__codelineno-0-3) async with AsyncWebCrawler() as crawler: [](#__codelineno-0-4)     result = await crawler.arun("https://www.example.com") [](#__codelineno-0-5)     if result.success: [](#__codelineno-0-6)         internal_links = result.links.get("internal", []) [](#__codelineno-0-7)         external_links = result.links.get("external", []) [](#__codelineno-0-8)         print(f"Found {len(internal_links)} internal links.") [](#__codelineno-0-9)         print(f"Found {len(internal_links)} external links.") [](#__codelineno-0-10)         print(f"Found {len(result.media)} media items.") [](#__codelineno-0-11) [](#__codelineno-0-12)         # Each link is typically a dictionary with fields like: [](#__codelineno-0-13)         # { "href": "...", "text": "...", "title": "...", "base_domain": "..." } [](#__codelineno-0-14)         if internal_links: [](#__codelineno-0-15)             print("Sample Internal Link:", internal_links[0]) [](#__codelineno-0-16)     else: [](#__codelineno-0-17)         print("Crawl failed:", result.error_message)`

**Structure Example**:

`[](#__codelineno-1-1) result.links = { [](#__codelineno-1-2)   "internal": [ [](#__codelineno-1-3)     { [](#__codelineno-1-4)       "href": "https://kidocode.com/", [](#__codelineno-1-5)       "text": "", [](#__codelineno-1-6)       "title": "", [](#__codelineno-1-7)       "base_domain": "kidocode.com" [](#__codelineno-1-8)     }, [](#__codelineno-1-9)     { [](#__codelineno-1-10)       "href": "https://kidocode.com/degrees/technology", [](#__codelineno-1-11)       "text": "Technology Degree", [](#__codelineno-1-12)       "title": "KidoCode Tech Program", [](#__codelineno-1-13)       "base_domain": "kidocode.com" [](#__codelineno-1-14)     }, [](#__codelineno-1-15)     # ... [](#__codelineno-1-16)   ], [](#__codelineno-1-17)   "external": [ [](#__codelineno-1-18)     # possibly other links leading to third-party sites [](#__codelineno-1-19)   ] [](#__codelineno-1-20) }`

*   **`href`**: The raw hyperlink URL.
*   **`text`**: The link text (if any) within the `<a>` tag.
*   **`title`**: The `title` attribute of the link (if present).
*   **`base_domain`**: The domain extracted from `href`. Helpful for filtering or grouping by domain.

* * *

2\. Domain Filtering
--------------------

Some websites contain hundreds of third-party or affiliate links. You can filter out certain domains at **crawl time** by configuring the crawler. The most relevant parameters in `CrawlerRunConfig` are:

*   **`exclude_external_links`**: If `True`, discard any link pointing outside the root domain.
*   **`exclude_social_media_domains`**: Provide a list of social media platforms (e.g., `["facebook.com", "twitter.com"]`) to exclude from your crawl.
*   **`exclude_social_media_links`**: If `True`, automatically skip known social platforms.
*   **`exclude_domains`**: Provide a list of custom domains you want to exclude (e.g., `["spammyads.com", "tracker.net"]`).

### 2.1 Example: Excluding External & Social Media Links

`[](#__codelineno-2-1) import asyncio [](#__codelineno-2-2) from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig [](#__codelineno-2-3) [](#__codelineno-2-4) async def main(): [](#__codelineno-2-5)     crawler_cfg = CrawlerRunConfig( [](#__codelineno-2-6)         exclude_external_links=True,          # No links outside primary domain [](#__codelineno-2-7)         exclude_social_media_links=True       # Skip recognized social media domains [](#__codelineno-2-8)     ) [](#__codelineno-2-9) [](#__codelineno-2-10)     async with AsyncWebCrawler() as crawler: [](#__codelineno-2-11)         result = await crawler.arun( [](#__codelineno-2-12)             "https://www.example.com", [](#__codelineno-2-13)             config=crawler_cfg [](#__codelineno-2-14)         ) [](#__codelineno-2-15)         if result.success: [](#__codelineno-2-16)             print("[OK] Crawled:", result.url) [](#__codelineno-2-17)             print("Internal links count:", len(result.links.get("internal", []))) [](#__codelineno-2-18)             print("External links count:", len(result.links.get("external", [])))   [](#__codelineno-2-19)             # Likely zero external links in this scenario [](#__codelineno-2-20)         else: [](#__codelineno-2-21)             print("[ERROR]", result.error_message) [](#__codelineno-2-22) [](#__codelineno-2-23) if __name__ == "__main__": [](#__codelineno-2-24)     asyncio.run(main())`

### 2.2 Example: Excluding Specific Domains

If you want to let external links in, but specifically exclude a domain (e.g., `suspiciousads.com`), do this:

`[](#__codelineno-3-1) crawler_cfg = CrawlerRunConfig( [](#__codelineno-3-2)     exclude_domains=["suspiciousads.com"] [](#__codelineno-3-3) )`

This approach is handy when you still want external links but need to block certain sites you consider spammy.

* * *

3\. Media Extraction
--------------------

### 3.1 Accessing `result.media`

By default, Crawl4AI collects images, audio, video URLs, and data tables it finds on the page. These are stored in `result.media`, a dictionary keyed by media type (e.g., `images`, `videos`, `audio`, `tables`).

**Basic Example**:

`[](#__codelineno-4-1) if result.success: [](#__codelineno-4-2)     # Get images [](#__codelineno-4-3)     images_info = result.media.get("images", []) [](#__codelineno-4-4)     print(f"Found {len(images_info)} images in total.") [](#__codelineno-4-5)     for i, img in enumerate(images_info[:3]):  # Inspect just the first 3 [](#__codelineno-4-6)         print(f"[Image {i}] URL: {img['src']}") [](#__codelineno-4-7)         print(f"           Alt text: {img.get('alt', '')}") [](#__codelineno-4-8)         print(f"           Score: {img.get('score')}") [](#__codelineno-4-9)         print(f"           Description: {img.get('desc', '')}\n") [](#__codelineno-4-10) [](#__codelineno-4-11)     # Get tables [](#__codelineno-4-12)     tables = result.media.get("tables", []) [](#__codelineno-4-13)     print(f"Found {len(tables)} data tables in total.") [](#__codelineno-4-14)     for i, table in enumerate(tables): [](#__codelineno-4-15)         print(f"[Table {i}] Caption: {table.get('caption', 'No caption')}") [](#__codelineno-4-16)         print(f"           Columns: {len(table.get('headers', []))}") [](#__codelineno-4-17)         print(f"           Rows: {len(table.get('rows', []))}")`

**Structure Example**:

`[](#__codelineno-5-1) result.media = { [](#__codelineno-5-2)   "images": [ [](#__codelineno-5-3)     { [](#__codelineno-5-4)       "src": "https://cdn.prod.website-files.com/.../Group%2089.svg", [](#__codelineno-5-5)       "alt": "coding school for kids", [](#__codelineno-5-6)       "desc": "Trial Class Degrees degrees All Degrees AI Degree Technology ...", [](#__codelineno-5-7)       "score": 3, [](#__codelineno-5-8)       "type": "image", [](#__codelineno-5-9)       "group_id": 0, [](#__codelineno-5-10)       "format": None, [](#__codelineno-5-11)       "width": None, [](#__codelineno-5-12)       "height": None [](#__codelineno-5-13)     }, [](#__codelineno-5-14)     # ... [](#__codelineno-5-15)   ], [](#__codelineno-5-16)   "videos": [ [](#__codelineno-5-17)     # Similar structure but with video-specific fields [](#__codelineno-5-18)   ], [](#__codelineno-5-19)   "audio": [ [](#__codelineno-5-20)     # Similar structure but with audio-specific fields [](#__codelineno-5-21)   ], [](#__codelineno-5-22)   "tables": [ [](#__codelineno-5-23)     { [](#__codelineno-5-24)       "headers": ["Name", "Age", "Location"], [](#__codelineno-5-25)       "rows": [ [](#__codelineno-5-26)         ["John Doe", "34", "New York"], [](#__codelineno-5-27)         ["Jane Smith", "28", "San Francisco"], [](#__codelineno-5-28)         ["Alex Johnson", "42", "Chicago"] [](#__codelineno-5-29)       ], [](#__codelineno-5-30)       "caption": "Employee Directory", [](#__codelineno-5-31)       "summary": "Directory of company employees" [](#__codelineno-5-32)     }, [](#__codelineno-5-33)     # More tables if present [](#__codelineno-5-34)   ] [](#__codelineno-5-35) }`

Depending on your Crawl4AI version or scraping strategy, these dictionaries can include fields like:

*   **`src`**: The media URL (e.g., image source)
*   **`alt`**: The alt text for images (if present)
*   **`desc`**: A snippet of nearby text or a short description (optional)
*   **`score`**: A heuristic relevance score if you’re using content-scoring features
*   **`width`**, **`height`**: If the crawler detects dimensions for the image/video
*   **`type`**: Usually `"image"`, `"video"`, or `"audio"`
*   **`group_id`**: If you’re grouping related media items, the crawler might assign an ID

With these details, you can easily filter out or focus on certain images (for instance, ignoring images with very low scores or a different domain), or gather metadata for analytics.

### 3.2 Excluding External Images

If you’re dealing with heavy pages or want to skip third-party images (advertisements, for example), you can turn on:

`[](#__codelineno-6-1) crawler_cfg = CrawlerRunConfig( [](#__codelineno-6-2)     exclude_external_images=True [](#__codelineno-6-3) )`

This setting attempts to discard images from outside the primary domain, keeping only those from the site you’re crawling.

### 3.3 Working with Tables

Crawl4AI can detect and extract structured data from HTML tables. Tables are analyzed based on various criteria to determine if they are actual data tables (as opposed to layout tables), including:

*   Presence of thead and tbody sections
*   Use of th elements for headers
*   Column consistency
*   Text density
*   And other factors

Tables that score above the threshold (default: 7) are extracted and stored in `result.media.tables`.

**Accessing Table Data**:

`[](#__codelineno-7-1) if result.success: [](#__codelineno-7-2)     tables = result.media.get("tables", []) [](#__codelineno-7-3)     print(f"Found {len(tables)} data tables on the page") [](#__codelineno-7-4) [](#__codelineno-7-5)     if tables: [](#__codelineno-7-6)         # Access the first table [](#__codelineno-7-7)         first_table = tables[0] [](#__codelineno-7-8)         print(f"Table caption: {first_table.get('caption', 'No caption')}") [](#__codelineno-7-9)         print(f"Headers: {first_table.get('headers', [])}") [](#__codelineno-7-10) [](#__codelineno-7-11)         # Print the first 3 rows [](#__codelineno-7-12)         for i, row in enumerate(first_table.get('rows', [])[:3]): [](#__codelineno-7-13)             print(f"Row {i+1}: {row}")`

**Configuring Table Extraction**:

You can adjust the sensitivity of the table detection algorithm with:

`[](#__codelineno-8-1) crawler_cfg = CrawlerRunConfig( [](#__codelineno-8-2)     table_score_threshold=5  # Lower value = more tables detected (default: 7) [](#__codelineno-8-3) )`

Each extracted table contains: - `headers`: Column header names - `rows`: List of rows, each containing cell values - `caption`: Table caption text (if available) - `summary`: Table summary attribute (if specified)

### 3.4 Additional Media Config

*   **`screenshot`**: Set to `True` if you want a full-page screenshot stored as `base64` in `result.screenshot`.
*   **`pdf`**: Set to `True` if you want a PDF version of the page in `result.pdf`.
*   **`wait_for_images`**: If `True`, attempts to wait until images are fully loaded before final extraction.

* * *

4\. Putting It All Together: Link & Media Filtering
---------------------------------------------------

Here’s a combined example demonstrating how to filter out external links, skip certain domains, and exclude external images:

`[](#__codelineno-9-1) import asyncio [](#__codelineno-9-2) from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig [](#__codelineno-9-3) [](#__codelineno-9-4) async def main(): [](#__codelineno-9-5)     # Suppose we want to keep only internal links, remove certain domains,  [](#__codelineno-9-6)     # and discard external images from the final crawl data. [](#__codelineno-9-7)     crawler_cfg = CrawlerRunConfig( [](#__codelineno-9-8)         exclude_external_links=True, [](#__codelineno-9-9)         exclude_domains=["spammyads.com"], [](#__codelineno-9-10)         exclude_social_media_links=True,   # skip Twitter, Facebook, etc. [](#__codelineno-9-11)         exclude_external_images=True,      # keep only images from main domain [](#__codelineno-9-12)         wait_for_images=True,             # ensure images are loaded [](#__codelineno-9-13)         verbose=True [](#__codelineno-9-14)     ) [](#__codelineno-9-15) [](#__codelineno-9-16)     async with AsyncWebCrawler() as crawler: [](#__codelineno-9-17)         result = await crawler.arun("https://www.example.com", config=crawler_cfg) [](#__codelineno-9-18) [](#__codelineno-9-19)         if result.success: [](#__codelineno-9-20)             print("[OK] Crawled:", result.url) [](#__codelineno-9-21) [](#__codelineno-9-22)             # 1. Links [](#__codelineno-9-23)             in_links = result.links.get("internal", []) [](#__codelineno-9-24)             ext_links = result.links.get("external", []) [](#__codelineno-9-25)             print("Internal link count:", len(in_links)) [](#__codelineno-9-26)             print("External link count:", len(ext_links))  # should be zero with exclude_external_links=True [](#__codelineno-9-27) [](#__codelineno-9-28)             # 2. Images [](#__codelineno-9-29)             images = result.media.get("images", []) [](#__codelineno-9-30)             print("Images found:", len(images)) [](#__codelineno-9-31) [](#__codelineno-9-32)             # Let's see a snippet of these images [](#__codelineno-9-33)             for i, img in enumerate(images[:3]): [](#__codelineno-9-34)                 print(f"  - {img['src']} (alt={img.get('alt','')}, score={img.get('score','N/A')})") [](#__codelineno-9-35)         else: [](#__codelineno-9-36)             print("[ERROR] Failed to crawl. Reason:", result.error_message) [](#__codelineno-9-37) [](#__codelineno-9-38) if __name__ == "__main__": [](#__codelineno-9-39)     asyncio.run(main())`

* * *

5\. Common Pitfalls & Tips
--------------------------

1. **Conflicting Flags**:  
\- `exclude_external_links=True` but then also specifying `exclude_social_media_links=True` is typically fine, but understand that the first setting already discards _all_ external links. The second becomes somewhat redundant.  
\- `exclude_external_images=True` but want to keep some external images? Currently no partial domain-based setting for images, so you might need a custom approach or hook logic.

2. **Relevancy Scores**:  
\- If your version of Crawl4AI or your scraping strategy includes an `img["score"]`, it’s typically a heuristic based on size, position, or content analysis. Evaluate carefully if you rely on it.

3. **Performance**:  
\- Excluding certain domains or external images can speed up your crawl, especially for large, media-heavy pages.  
\- If you want a “full” link map, do _not_ exclude them. Instead, you can post-filter in your own code.

4. **Social Media Lists**:  
\- `exclude_social_media_links=True` typically references an internal list of known social domains like Facebook, Twitter, LinkedIn, etc. If you need to add or remove from that list, look for library settings or a local config file (depending on your version).

* * *

**That’s it for Link & Media Analysis!** You’re now equipped to filter out unwanted sites and zero in on the images and videos that matter for your project.

### Table Extraction Tips

*   Not all HTML tables are extracted - only those detected as "data tables" vs. layout tables.
*   Tables with inconsistent cell counts, nested tables, or those used purely for layout may be skipped.
*   If you're missing tables, try adjusting the `table_score_threshold` to a lower value (default is 7).

The table detection algorithm scores tables based on features like consistent columns, presence of headers, text density, and more. Tables scoring above the threshold are considered data tables worth extracting.

* * *

---

# Local Files & Raw HTML - Crawl4AI Documentation (v0.5.x)

Prefix-Based Input Handling in Crawl4AI
=======================================

This guide will walk you through using the Crawl4AI library to crawl web pages, local HTML files, and raw HTML strings. We'll demonstrate these capabilities using a Wikipedia page as an example.

Crawling a Web URL
------------------

To crawl a live web page, provide the URL starting with `http://` or `https://`, using a `CrawlerRunConfig` object:

`[](#__codelineno-0-1) import asyncio [](#__codelineno-0-2) from crawl4ai import AsyncWebCrawler [](#__codelineno-0-3) from crawl4ai.async_configs import CrawlerRunConfig [](#__codelineno-0-4) [](#__codelineno-0-5) async def crawl_web(): [](#__codelineno-0-6)     config = CrawlerRunConfig(bypass_cache=True) [](#__codelineno-0-7)     async with AsyncWebCrawler() as crawler: [](#__codelineno-0-8)         result = await crawler.arun( [](#__codelineno-0-9)             url="https://en.wikipedia.org/wiki/apple",  [](#__codelineno-0-10)             config=config [](#__codelineno-0-11)         ) [](#__codelineno-0-12)         if result.success: [](#__codelineno-0-13)             print("Markdown Content:") [](#__codelineno-0-14)             print(result.markdown) [](#__codelineno-0-15)         else: [](#__codelineno-0-16)             print(f"Failed to crawl: {result.error_message}") [](#__codelineno-0-17) [](#__codelineno-0-18) asyncio.run(crawl_web())`

Crawling a Local HTML File
--------------------------

To crawl a local HTML file, prefix the file path with `file://`.

`[](#__codelineno-1-1) import asyncio [](#__codelineno-1-2) from crawl4ai import AsyncWebCrawler [](#__codelineno-1-3) from crawl4ai.async_configs import CrawlerRunConfig [](#__codelineno-1-4) [](#__codelineno-1-5) async def crawl_local_file(): [](#__codelineno-1-6)     local_file_path = "/path/to/apple.html"  # Replace with your file path [](#__codelineno-1-7)     file_url = f"file://{local_file_path}" [](#__codelineno-1-8)     config = CrawlerRunConfig(bypass_cache=True) [](#__codelineno-1-9) [](#__codelineno-1-10)     async with AsyncWebCrawler() as crawler: [](#__codelineno-1-11)         result = await crawler.arun(url=file_url, config=config) [](#__codelineno-1-12)         if result.success: [](#__codelineno-1-13)             print("Markdown Content from Local File:") [](#__codelineno-1-14)             print(result.markdown) [](#__codelineno-1-15)         else: [](#__codelineno-1-16)             print(f"Failed to crawl local file: {result.error_message}") [](#__codelineno-1-17) [](#__codelineno-1-18) asyncio.run(crawl_local_file())`

Crawling Raw HTML Content
-------------------------

To crawl raw HTML content, prefix the HTML string with `raw:`.

`[](#__codelineno-2-1) import asyncio [](#__codelineno-2-2) from crawl4ai import AsyncWebCrawler [](#__codelineno-2-3) from crawl4ai.async_configs import CrawlerRunConfig [](#__codelineno-2-4) [](#__codelineno-2-5) async def crawl_raw_html(): [](#__codelineno-2-6)     raw_html = "<html><body><h1>Hello, World!</h1></body></html>" [](#__codelineno-2-7)     raw_html_url = f"raw:{raw_html}" [](#__codelineno-2-8)     config = CrawlerRunConfig(bypass_cache=True) [](#__codelineno-2-9) [](#__codelineno-2-10)     async with AsyncWebCrawler() as crawler: [](#__codelineno-2-11)         result = await crawler.arun(url=raw_html_url, config=config) [](#__codelineno-2-12)         if result.success: [](#__codelineno-2-13)             print("Markdown Content from Raw HTML:") [](#__codelineno-2-14)             print(result.markdown) [](#__codelineno-2-15)         else: [](#__codelineno-2-16)             print(f"Failed to crawl raw HTML: {result.error_message}") [](#__codelineno-2-17) [](#__codelineno-2-18) asyncio.run(crawl_raw_html())`

* * *

Complete Example
================

Below is a comprehensive script that:

1.  Crawls the Wikipedia page for "Apple."
2.  Saves the HTML content to a local file (`apple.html`).
3.  Crawls the local HTML file and verifies the markdown length matches the original crawl.
4.  Crawls the raw HTML content from the saved file and verifies consistency.

`[](#__codelineno-3-1) import os [](#__codelineno-3-2) import sys [](#__codelineno-3-3) import asyncio [](#__codelineno-3-4) from pathlib import Path [](#__codelineno-3-5) from crawl4ai import AsyncWebCrawler [](#__codelineno-3-6) from crawl4ai.async_configs import CrawlerRunConfig [](#__codelineno-3-7) [](#__codelineno-3-8) async def main(): [](#__codelineno-3-9)     wikipedia_url = "https://en.wikipedia.org/wiki/apple" [](#__codelineno-3-10)     script_dir = Path(__file__).parent [](#__codelineno-3-11)     html_file_path = script_dir / "apple.html" [](#__codelineno-3-12) [](#__codelineno-3-13)     async with AsyncWebCrawler() as crawler: [](#__codelineno-3-14)         # Step 1: Crawl the Web URL [](#__codelineno-3-15)         print("\n=== Step 1: Crawling the Wikipedia URL ===") [](#__codelineno-3-16)         web_config = CrawlerRunConfig(bypass_cache=True) [](#__codelineno-3-17)         result = await crawler.arun(url=wikipedia_url, config=web_config) [](#__codelineno-3-18) [](#__codelineno-3-19)         if not result.success: [](#__codelineno-3-20)             print(f"Failed to crawl {wikipedia_url}: {result.error_message}") [](#__codelineno-3-21)             return [](#__codelineno-3-22) [](#__codelineno-3-23)         with open(html_file_path, 'w', encoding='utf-8') as f: [](#__codelineno-3-24)             f.write(result.html) [](#__codelineno-3-25)         web_crawl_length = len(result.markdown) [](#__codelineno-3-26)         print(f"Length of markdown from web crawl: {web_crawl_length}\n") [](#__codelineno-3-27) [](#__codelineno-3-28)         # Step 2: Crawl from the Local HTML File [](#__codelineno-3-29)         print("=== Step 2: Crawling from the Local HTML File ===") [](#__codelineno-3-30)         file_url = f"file://{html_file_path.resolve()}" [](#__codelineno-3-31)         file_config = CrawlerRunConfig(bypass_cache=True) [](#__codelineno-3-32)         local_result = await crawler.arun(url=file_url, config=file_config) [](#__codelineno-3-33) [](#__codelineno-3-34)         if not local_result.success: [](#__codelineno-3-35)             print(f"Failed to crawl local file {file_url}: {local_result.error_message}") [](#__codelineno-3-36)             return [](#__codelineno-3-37) [](#__codelineno-3-38)         local_crawl_length = len(local_result.markdown) [](#__codelineno-3-39)         assert web_crawl_length == local_crawl_length, "Markdown length mismatch" [](#__codelineno-3-40)         print("✅ Markdown length matches between web and local file crawl.\n") [](#__codelineno-3-41) [](#__codelineno-3-42)         # Step 3: Crawl Using Raw HTML Content [](#__codelineno-3-43)         print("=== Step 3: Crawling Using Raw HTML Content ===") [](#__codelineno-3-44)         with open(html_file_path, 'r', encoding='utf-8') as f: [](#__codelineno-3-45)             raw_html_content = f.read() [](#__codelineno-3-46)         raw_html_url = f"raw:{raw_html_content}" [](#__codelineno-3-47)         raw_config = CrawlerRunConfig(bypass_cache=True) [](#__codelineno-3-48)         raw_result = await crawler.arun(url=raw_html_url, config=raw_config) [](#__codelineno-3-49) [](#__codelineno-3-50)         if not raw_result.success: [](#__codelineno-3-51)             print(f"Failed to crawl raw HTML content: {raw_result.error_message}") [](#__codelineno-3-52)             return [](#__codelineno-3-53) [](#__codelineno-3-54)         raw_crawl_length = len(raw_result.markdown) [](#__codelineno-3-55)         assert web_crawl_length == raw_crawl_length, "Markdown length mismatch" [](#__codelineno-3-56)         print("✅ Markdown length matches between web and raw HTML crawl.\n") [](#__codelineno-3-57) [](#__codelineno-3-58)         print("All tests passed successfully!") [](#__codelineno-3-59)     if html_file_path.exists(): [](#__codelineno-3-60)         os.remove(html_file_path) [](#__codelineno-3-61) [](#__codelineno-3-62) if __name__ == "__main__": [](#__codelineno-3-63)     asyncio.run(main())`

* * *

Conclusion
==========

With the unified `url` parameter and prefix-based handling in **Crawl4AI**, you can seamlessly handle web URLs, local HTML files, and raw HTML content. Use `CrawlerRunConfig` for flexible and consistent configuration in all scenarios.

* * *

---

# Markdown Generation - Crawl4AI Documentation (v0.5.x)

Markdown Generation Basics
==========================

One of Crawl4AI’s core features is generating **clean, structured markdown** from web pages. Originally built to solve the problem of extracting only the “actual” content and discarding boilerplate or noise, Crawl4AI’s markdown system remains one of its biggest draws for AI workflows.

In this tutorial, you’ll learn:

1.  How to configure the **Default Markdown Generator**
2.  How **content filters** (BM25 or Pruning) help you refine markdown and discard junk
3.  The difference between raw markdown (`result.markdown`) and filtered markdown (`fit_markdown`)

> **Prerequisites**  
> \- You’ve completed or read [AsyncWebCrawler Basics](../simple-crawling/)
>  to understand how to run a simple crawl.  
> \- You know how to configure `CrawlerRunConfig`.

* * *

1\. Quick Example
-----------------

Here’s a minimal code snippet that uses the **DefaultMarkdownGenerator** with no additional filtering:

`[](#__codelineno-0-1) import asyncio [](#__codelineno-0-2) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig [](#__codelineno-0-3) from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator [](#__codelineno-0-4) [](#__codelineno-0-5) async def main(): [](#__codelineno-0-6)     config = CrawlerRunConfig( [](#__codelineno-0-7)         markdown_generator=DefaultMarkdownGenerator() [](#__codelineno-0-8)     ) [](#__codelineno-0-9)     async with AsyncWebCrawler() as crawler: [](#__codelineno-0-10)         result = await crawler.arun("https://example.com", config=config) [](#__codelineno-0-11) [](#__codelineno-0-12)         if result.success: [](#__codelineno-0-13)             print("Raw Markdown Output:\n") [](#__codelineno-0-14)             print(result.markdown)  # The unfiltered markdown from the page [](#__codelineno-0-15)         else: [](#__codelineno-0-16)             print("Crawl failed:", result.error_message) [](#__codelineno-0-17) [](#__codelineno-0-18) if __name__ == "__main__": [](#__codelineno-0-19)     asyncio.run(main())`

**What’s happening?**  
\- `CrawlerRunConfig( markdown_generator = DefaultMarkdownGenerator() )` instructs Crawl4AI to convert the final HTML into markdown at the end of each crawl.  
\- The resulting markdown is accessible via `result.markdown`.

* * *

2\. How Markdown Generation Works
---------------------------------

### 2.1 HTML-to-Text Conversion (Forked & Modified)

Under the hood, **DefaultMarkdownGenerator** uses a specialized HTML-to-text approach that:

*   Preserves headings, code blocks, bullet points, etc.
*   Removes extraneous tags (scripts, styles) that don’t add meaningful content.
*   Can optionally generate references for links or skip them altogether.

A set of **options** (passed as a dict) allows you to customize precisely how HTML converts to markdown. These map to standard html2text-like configuration plus your own enhancements (e.g., ignoring internal links, preserving certain tags verbatim, or adjusting line widths).

### 2.2 Link Citations & References

By default, the generator can convert `<a href="...">` elements into `[text][1]` citations, then place the actual links at the bottom of the document. This is handy for research workflows that demand references in a structured manner.

### 2.3 Optional Content Filters

Before or after the HTML-to-Markdown step, you can apply a **content filter** (like BM25 or Pruning) to reduce noise and produce a “fit\_markdown”—a heavily pruned version focusing on the page’s main text. We’ll cover these filters shortly.

* * *

3\. Configuring the Default Markdown Generator
----------------------------------------------

You can tweak the output by passing an `options` dict to `DefaultMarkdownGenerator`. For example:

`[](#__codelineno-1-1) from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator [](#__codelineno-1-2) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig [](#__codelineno-1-3) [](#__codelineno-1-4) async def main(): [](#__codelineno-1-5)     # Example: ignore all links, don't escape HTML, and wrap text at 80 characters [](#__codelineno-1-6)     md_generator = DefaultMarkdownGenerator( [](#__codelineno-1-7)         options={ [](#__codelineno-1-8)             "ignore_links": True, [](#__codelineno-1-9)             "escape_html": False, [](#__codelineno-1-10)             "body_width": 80 [](#__codelineno-1-11)         } [](#__codelineno-1-12)     ) [](#__codelineno-1-13) [](#__codelineno-1-14)     config = CrawlerRunConfig( [](#__codelineno-1-15)         markdown_generator=md_generator [](#__codelineno-1-16)     ) [](#__codelineno-1-17) [](#__codelineno-1-18)     async with AsyncWebCrawler() as crawler: [](#__codelineno-1-19)         result = await crawler.arun("https://example.com/docs", config=config) [](#__codelineno-1-20)         if result.success: [](#__codelineno-1-21)             print("Markdown:\n", result.markdown[:500])  # Just a snippet [](#__codelineno-1-22)         else: [](#__codelineno-1-23)             print("Crawl failed:", result.error_message) [](#__codelineno-1-24) [](#__codelineno-1-25) if __name__ == "__main__": [](#__codelineno-1-26)     import asyncio [](#__codelineno-1-27)     asyncio.run(main())`

Some commonly used `options`:

*   **`ignore_links`** (bool): Whether to remove all hyperlinks in the final markdown.
*   **`ignore_images`** (bool): Remove all `![image]()` references.
*   **`escape_html`** (bool): Turn HTML entities into text (default is often `True`).
*   **`body_width`** (int): Wrap text at N characters. `0` or `None` means no wrapping.
*   **`skip_internal_links`** (bool): If `True`, omit `#localAnchors` or internal links referencing the same page.
*   **`include_sup_sub`** (bool): Attempt to handle `<sup>` / `<sub>` in a more readable way.

* * *

4\. Content Filters
-------------------

**Content filters** selectively remove or rank sections of text before turning them into Markdown. This is especially helpful if your page has ads, nav bars, or other clutter you don’t want.

### 4.1 BM25ContentFilter

If you have a **search query**, BM25 is a good choice:

`[](#__codelineno-2-1) from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator [](#__codelineno-2-2) from crawl4ai.content_filter_strategy import BM25ContentFilter [](#__codelineno-2-3) from crawl4ai import CrawlerRunConfig [](#__codelineno-2-4) [](#__codelineno-2-5) bm25_filter = BM25ContentFilter( [](#__codelineno-2-6)     user_query="machine learning", [](#__codelineno-2-7)     bm25_threshold=1.2, [](#__codelineno-2-8)     use_stemming=True [](#__codelineno-2-9) ) [](#__codelineno-2-10) [](#__codelineno-2-11) md_generator = DefaultMarkdownGenerator( [](#__codelineno-2-12)     content_filter=bm25_filter, [](#__codelineno-2-13)     options={"ignore_links": True} [](#__codelineno-2-14) ) [](#__codelineno-2-15) [](#__codelineno-2-16) config = CrawlerRunConfig(markdown_generator=md_generator)`

*   **`user_query`**: The term you want to focus on. BM25 tries to keep only content blocks relevant to that query.
*   **`bm25_threshold`**: Raise it to keep fewer blocks; lower it to keep more.
*   **`use_stemming`**: If `True`, variations of words match (e.g., “learn,” “learning,” “learnt”).

**No query provided?** BM25 tries to glean a context from page metadata, or you can simply treat it as a scorched-earth approach that discards text with low generic score. Realistically, you want to supply a query for best results.

### 4.2 PruningContentFilter

If you **don’t** have a specific query, or if you just want a robust “junk remover,” use `PruningContentFilter`. It analyzes text density, link density, HTML structure, and known patterns (like “nav,” “footer”) to systematically prune extraneous or repetitive sections.

`[](#__codelineno-3-1) from crawl4ai.content_filter_strategy import PruningContentFilter [](#__codelineno-3-2) [](#__codelineno-3-3) prune_filter = PruningContentFilter( [](#__codelineno-3-4)     threshold=0.5, [](#__codelineno-3-5)     threshold_type="fixed",  # or "dynamic" [](#__codelineno-3-6)     min_word_threshold=50 [](#__codelineno-3-7) )`

*   **`threshold`**: Score boundary. Blocks below this score get removed.
*   **`threshold_type`**:
    *   `"fixed"`: Straight comparison (`score >= threshold` keeps the block).
    *   `"dynamic"`: The filter adjusts threshold in a data-driven manner.
*   **`min_word_threshold`**: Discard blocks under N words as likely too short or unhelpful.

**When to Use PruningContentFilter**  
\- You want a broad cleanup without a user query.  
\- The page has lots of repeated sidebars, footers, or disclaimers that hamper text extraction.

### 4.3 LLMContentFilter

For intelligent content filtering and high-quality markdown generation, you can use the **LLMContentFilter**. This filter leverages LLMs to generate relevant markdown while preserving the original content's meaning and structure:

`[](#__codelineno-4-1) from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, LLMConfig [](#__codelineno-4-2) from crawl4ai.content_filter_strategy import LLMContentFilter [](#__codelineno-4-3) [](#__codelineno-4-4) async def main(): [](#__codelineno-4-5)     # Initialize LLM filter with specific instruction [](#__codelineno-4-6)     filter = LLMContentFilter( [](#__codelineno-4-7)         llm_config = LLMConfig(provider="openai/gpt-4o",api_token="your-api-token"), #or use environment variable [](#__codelineno-4-8)         instruction=""" [](#__codelineno-4-9)         Focus on extracting the core educational content. [](#__codelineno-4-10)         Include: [](#__codelineno-4-11)         - Key concepts and explanations [](#__codelineno-4-12)         - Important code examples [](#__codelineno-4-13)         - Essential technical details [](#__codelineno-4-14)         Exclude: [](#__codelineno-4-15)         - Navigation elements [](#__codelineno-4-16)         - Sidebars [](#__codelineno-4-17)         - Footer content [](#__codelineno-4-18)         Format the output as clean markdown with proper code blocks and headers. [](#__codelineno-4-19)         """, [](#__codelineno-4-20)         chunk_token_threshold=4096,  # Adjust based on your needs [](#__codelineno-4-21)         verbose=True [](#__codelineno-4-22)     ) [](#__codelineno-4-23) [](#__codelineno-4-24)     config = CrawlerRunConfig( [](#__codelineno-4-25)         content_filter=filter [](#__codelineno-4-26)     ) [](#__codelineno-4-27) [](#__codelineno-4-28)     async with AsyncWebCrawler() as crawler: [](#__codelineno-4-29)         result = await crawler.arun("https://example.com", config=config) [](#__codelineno-4-30)         print(result.markdown.fit_markdown)  # Filtered markdown content`

**Key Features:** - **Intelligent Filtering**: Uses LLMs to understand and extract relevant content while maintaining context - **Customizable Instructions**: Tailor the filtering process with specific instructions - **Chunk Processing**: Handles large documents by processing them in chunks (controlled by `chunk_token_threshold`) - **Parallel Processing**: For better performance, use smaller `chunk_token_threshold` (e.g., 2048 or 4096) to enable parallel processing of content chunks

**Two Common Use Cases:**

1.  **Exact Content Preservation**:
    
    `[](#__codelineno-5-1) filter = LLMContentFilter( [](#__codelineno-5-2)     instruction=""" [](#__codelineno-5-3)     Extract the main educational content while preserving its original wording and substance completely. [](#__codelineno-5-4)     1. Maintain the exact language and terminology [](#__codelineno-5-5)     2. Keep all technical explanations and examples intact [](#__codelineno-5-6)     3. Preserve the original flow and structure [](#__codelineno-5-7)     4. Remove only clearly irrelevant elements like navigation menus and ads [](#__codelineno-5-8)     """, [](#__codelineno-5-9)     chunk_token_threshold=4096 [](#__codelineno-5-10) )`
    
2.  **Focused Content Extraction**:
    
    `[](#__codelineno-6-1) filter = LLMContentFilter( [](#__codelineno-6-2)     instruction=""" [](#__codelineno-6-3)     Focus on extracting specific types of content: [](#__codelineno-6-4)     - Technical documentation [](#__codelineno-6-5)     - Code examples [](#__codelineno-6-6)     - API references [](#__codelineno-6-7)     Reformat the content into clear, well-structured markdown [](#__codelineno-6-8)     """, [](#__codelineno-6-9)     chunk_token_threshold=4096 [](#__codelineno-6-10) )`
    

> **Performance Tip**: Set a smaller `chunk_token_threshold` (e.g., 2048 or 4096) to enable parallel processing of content chunks. The default value is infinity, which processes the entire content as a single chunk.

* * *

5\. Using Fit Markdown
----------------------

When a content filter is active, the library produces two forms of markdown inside `result.markdown`:

1. **`raw_markdown`**: The full unfiltered markdown.  
2. **`fit_markdown`**: A “fit” version where the filter has removed or trimmed noisy segments.

`[](#__codelineno-7-1) import asyncio [](#__codelineno-7-2) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig [](#__codelineno-7-3) from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator [](#__codelineno-7-4) from crawl4ai.content_filter_strategy import PruningContentFilter [](#__codelineno-7-5) [](#__codelineno-7-6) async def main(): [](#__codelineno-7-7)     config = CrawlerRunConfig( [](#__codelineno-7-8)         markdown_generator=DefaultMarkdownGenerator( [](#__codelineno-7-9)             content_filter=PruningContentFilter(threshold=0.6), [](#__codelineno-7-10)             options={"ignore_links": True} [](#__codelineno-7-11)         ) [](#__codelineno-7-12)     ) [](#__codelineno-7-13)     async with AsyncWebCrawler() as crawler: [](#__codelineno-7-14)         result = await crawler.arun("https://news.example.com/tech", config=config) [](#__codelineno-7-15)         if result.success: [](#__codelineno-7-16)             print("Raw markdown:\n", result.markdown) [](#__codelineno-7-17) [](#__codelineno-7-18)             # If a filter is used, we also have .fit_markdown: [](#__codelineno-7-19)             md_object = result.markdown  # or your equivalent [](#__codelineno-7-20)             print("Filtered markdown:\n", md_object.fit_markdown) [](#__codelineno-7-21)         else: [](#__codelineno-7-22)             print("Crawl failed:", result.error_message) [](#__codelineno-7-23) [](#__codelineno-7-24) if __name__ == "__main__": [](#__codelineno-7-25)     asyncio.run(main())`

* * *

6\. The `MarkdownGenerationResult` Object
-----------------------------------------

If your library stores detailed markdown output in an object like `MarkdownGenerationResult`, you’ll see fields such as:

*   **`raw_markdown`**: The direct HTML-to-markdown transformation (no filtering).
*   **`markdown_with_citations`**: A version that moves links to reference-style footnotes.
*   **`references_markdown`**: A separate string or section containing the gathered references.
*   **`fit_markdown`**: The filtered markdown if you used a content filter.
*   **`fit_html`**: The corresponding HTML snippet used to generate `fit_markdown` (helpful for debugging or advanced usage).

**Example**:

`[](#__codelineno-8-1) md_obj = result.markdown  # your library’s naming may vary [](#__codelineno-8-2) print("RAW:\n", md_obj.raw_markdown) [](#__codelineno-8-3) print("CITED:\n", md_obj.markdown_with_citations) [](#__codelineno-8-4) print("REFERENCES:\n", md_obj.references_markdown) [](#__codelineno-8-5) print("FIT:\n", md_obj.fit_markdown)`

**Why Does This Matter?**  
\- You can supply `raw_markdown` to an LLM if you want the entire text.  
\- Or feed `fit_markdown` into a vector database to reduce token usage.  
\- `references_markdown` can help you keep track of link provenance.

* * *

Below is a **revised section** under “Combining Filters (BM25 + Pruning)” that demonstrates how you can run **two** passes of content filtering without re-crawling, by taking the HTML (or text) from a first pass and feeding it into the second filter. It uses real code patterns from the snippet you provided for **BM25ContentFilter**, which directly accepts **HTML** strings (and can also handle plain text with minimal adaptation).

* * *

7\. Combining Filters (BM25 + Pruning) in Two Passes
----------------------------------------------------

You might want to **prune out** noisy boilerplate first (with `PruningContentFilter`), and then **rank what’s left** against a user query (with `BM25ContentFilter`). You don’t have to crawl the page twice. Instead:

1. **First pass**: Apply `PruningContentFilter` directly to the raw HTML from `result.html` (the crawler’s downloaded HTML).  
2. **Second pass**: Take the pruned HTML (or text) from step 1, and feed it into `BM25ContentFilter`, focusing on a user query.

### Two-Pass Example

`[](#__codelineno-9-1) import asyncio [](#__codelineno-9-2) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig [](#__codelineno-9-3) from crawl4ai.content_filter_strategy import PruningContentFilter, BM25ContentFilter [](#__codelineno-9-4) from bs4 import BeautifulSoup [](#__codelineno-9-5) [](#__codelineno-9-6) async def main(): [](#__codelineno-9-7)     # 1. Crawl with minimal or no markdown generator, just get raw HTML [](#__codelineno-9-8)     config = CrawlerRunConfig( [](#__codelineno-9-9)         # If you only want raw HTML, you can skip passing a markdown_generator [](#__codelineno-9-10)         # or provide one but focus on .html in this example [](#__codelineno-9-11)     ) [](#__codelineno-9-12) [](#__codelineno-9-13)     async with AsyncWebCrawler() as crawler: [](#__codelineno-9-14)         result = await crawler.arun("https://example.com/tech-article", config=config) [](#__codelineno-9-15) [](#__codelineno-9-16)         if not result.success or not result.html: [](#__codelineno-9-17)             print("Crawl failed or no HTML content.") [](#__codelineno-9-18)             return [](#__codelineno-9-19) [](#__codelineno-9-20)         raw_html = result.html [](#__codelineno-9-21) [](#__codelineno-9-22)         # 2. First pass: PruningContentFilter on raw HTML [](#__codelineno-9-23)         pruning_filter = PruningContentFilter(threshold=0.5, min_word_threshold=50) [](#__codelineno-9-24) [](#__codelineno-9-25)         # filter_content returns a list of "text chunks" or cleaned HTML sections [](#__codelineno-9-26)         pruned_chunks = pruning_filter.filter_content(raw_html) [](#__codelineno-9-27)         # This list is basically pruned content blocks, presumably in HTML or text form [](#__codelineno-9-28) [](#__codelineno-9-29)         # For demonstration, let's combine these chunks back into a single HTML-like string [](#__codelineno-9-30)         # or you could do further processing. It's up to your pipeline design. [](#__codelineno-9-31)         pruned_html = "\n".join(pruned_chunks) [](#__codelineno-9-32) [](#__codelineno-9-33)         # 3. Second pass: BM25ContentFilter with a user query [](#__codelineno-9-34)         bm25_filter = BM25ContentFilter( [](#__codelineno-9-35)             user_query="machine learning", [](#__codelineno-9-36)             bm25_threshold=1.2, [](#__codelineno-9-37)             language="english" [](#__codelineno-9-38)         ) [](#__codelineno-9-39) [](#__codelineno-9-40)         # returns a list of text chunks [](#__codelineno-9-41)         bm25_chunks = bm25_filter.filter_content(pruned_html)   [](#__codelineno-9-42) [](#__codelineno-9-43)         if not bm25_chunks: [](#__codelineno-9-44)             print("Nothing matched the BM25 query after pruning.") [](#__codelineno-9-45)             return [](#__codelineno-9-46) [](#__codelineno-9-47)         # 4. Combine or display final results [](#__codelineno-9-48)         final_text = "\n---\n".join(bm25_chunks) [](#__codelineno-9-49) [](#__codelineno-9-50)         print("==== PRUNED OUTPUT (first pass) ====") [](#__codelineno-9-51)         print(pruned_html[:500], "... (truncated)")  # preview [](#__codelineno-9-52) [](#__codelineno-9-53)         print("\n==== BM25 OUTPUT (second pass) ====") [](#__codelineno-9-54)         print(final_text[:500], "... (truncated)") [](#__codelineno-9-55) [](#__codelineno-9-56) if __name__ == "__main__": [](#__codelineno-9-57)     asyncio.run(main())`

### What’s Happening?

1. **Raw HTML**: We crawl once and store the raw HTML in `result.html`.  
2. **PruningContentFilter**: Takes HTML + optional parameters. It extracts blocks of text or partial HTML, removing headings/sections deemed “noise.” It returns a **list of text chunks**.  
3. **Combine or Transform**: We join these pruned chunks back into a single HTML-like string. (Alternatively, you could store them in a list for further logic—whatever suits your pipeline.)  
4. **BM25ContentFilter**: We feed the pruned string into `BM25ContentFilter` with a user query. This second pass further narrows the content to chunks relevant to “machine learning.”

**No Re-Crawling**: We used `raw_html` from the first pass, so there’s no need to run `arun()` again—**no second network request**.

### Tips & Variations

*   **Plain Text vs. HTML**: If your pruned output is mostly text, BM25 can still handle it; just keep in mind it expects a valid string input. If you supply partial HTML (like `"<p>some text</p>"`), it will parse it as HTML.
*   **Chaining in a Single Pipeline**: If your code supports it, you can chain multiple filters automatically. Otherwise, manual two-pass filtering (as shown) is straightforward.
*   **Adjust Thresholds**: If you see too much or too little text in step one, tweak `threshold=0.5` or `min_word_threshold=50`. Similarly, `bm25_threshold=1.2` can be raised/lowered for more or fewer chunks in step two.

### One-Pass Combination?

If your codebase or pipeline design allows applying multiple filters in one pass, you could do so. But often it’s simpler—and more transparent—to run them sequentially, analyzing each step’s result.

**Bottom Line**: By **manually chaining** your filtering logic in two passes, you get powerful incremental control over the final content. First, remove “global” clutter with Pruning, then refine further with BM25-based query relevance—without incurring a second network crawl.

* * *

8\. Common Pitfalls & Tips
--------------------------

1. **No Markdown Output?**  
\- Make sure the crawler actually retrieved HTML. If the site is heavily JS-based, you may need to enable dynamic rendering or wait for elements.  
\- Check if your content filter is too aggressive. Lower thresholds or disable the filter to see if content reappears.

2. **Performance Considerations**  
\- Very large pages with multiple filters can be slower. Consider `cache_mode` to avoid re-downloading.  
\- If your final use case is LLM ingestion, consider summarizing further or chunking big texts.

3. **Take Advantage of `fit_markdown`**  
\- Great for RAG pipelines, semantic search, or any scenario where extraneous boilerplate is unwanted.  
\- Still verify the textual quality—some sites have crucial data in footers or sidebars.

4. **Adjusting `html2text` Options**  
\- If you see lots of raw HTML slipping into the text, turn on `escape_html`.  
\- If code blocks look messy, experiment with `mark_code` or `handle_code_in_pre`.

* * *

9\. Summary & Next Steps
------------------------

In this **Markdown Generation Basics** tutorial, you learned to:

*   Configure the **DefaultMarkdownGenerator** with HTML-to-text options.
*   Use **BM25ContentFilter** for query-specific extraction or **PruningContentFilter** for general noise removal.
*   Distinguish between raw and filtered markdown (`fit_markdown`).
*   Leverage the `MarkdownGenerationResult` object to handle different forms of output (citations, references, etc.).

Now you can produce high-quality Markdown from any website, focusing on exactly the content you need—an essential step for powering AI models, summarization pipelines, or knowledge-base queries.

**Last Updated**: 2025-01-01

* * *

---

# Chunking - Crawl4AI Documentation (v0.5.x)

Chunking Strategies
===================

Chunking strategies are critical for dividing large texts into manageable parts, enabling effective content processing and extraction. These strategies are foundational in cosine similarity-based extraction techniques, which allow users to retrieve only the most relevant chunks of content for a given query. Additionally, they facilitate direct integration into RAG (Retrieval-Augmented Generation) systems for structured and scalable workflows.

### Why Use Chunking?

1. **Cosine Similarity and Query Relevance**: Prepares chunks for semantic similarity analysis. 2. **RAG System Integration**: Seamlessly processes and stores chunks for retrieval. 3. **Structured Processing**: Allows for diverse segmentation methods, such as sentence-based, topic-based, or windowed approaches.

### Methods of Chunking

#### 1\. Regex-Based Chunking

Splits text based on regular expression patterns, useful for coarse segmentation.

**Code Example**:

`[](#__codelineno-0-1) class RegexChunking: [](#__codelineno-0-2)     def __init__(self, patterns=None): [](#__codelineno-0-3)         self.patterns = patterns or [r'\n\n']  # Default pattern for paragraphs [](#__codelineno-0-4) [](#__codelineno-0-5)     def chunk(self, text): [](#__codelineno-0-6)         paragraphs = [text] [](#__codelineno-0-7)         for pattern in self.patterns: [](#__codelineno-0-8)             paragraphs = [seg for p in paragraphs for seg in re.split(pattern, p)] [](#__codelineno-0-9)         return paragraphs [](#__codelineno-0-10) [](#__codelineno-0-11) # Example Usage [](#__codelineno-0-12) text = """This is the first paragraph. [](#__codelineno-0-13) [](#__codelineno-0-14) This is the second paragraph.""" [](#__codelineno-0-15) chunker = RegexChunking() [](#__codelineno-0-16) print(chunker.chunk(text))`

#### 2\. Sentence-Based Chunking

Divides text into sentences using NLP tools, ideal for extracting meaningful statements.

**Code Example**:

`[](#__codelineno-1-1) from nltk.tokenize import sent_tokenize [](#__codelineno-1-2) [](#__codelineno-1-3) class NlpSentenceChunking: [](#__codelineno-1-4)     def chunk(self, text): [](#__codelineno-1-5)         sentences = sent_tokenize(text) [](#__codelineno-1-6)         return [sentence.strip() for sentence in sentences] [](#__codelineno-1-7) [](#__codelineno-1-8) # Example Usage [](#__codelineno-1-9) text = "This is sentence one. This is sentence two." [](#__codelineno-1-10) chunker = NlpSentenceChunking() [](#__codelineno-1-11) print(chunker.chunk(text))`

#### 3\. Topic-Based Segmentation

Uses algorithms like TextTiling to create topic-coherent chunks.

**Code Example**:

`[](#__codelineno-2-1) from nltk.tokenize import TextTilingTokenizer [](#__codelineno-2-2) [](#__codelineno-2-3) class TopicSegmentationChunking: [](#__codelineno-2-4)     def __init__(self): [](#__codelineno-2-5)         self.tokenizer = TextTilingTokenizer() [](#__codelineno-2-6) [](#__codelineno-2-7)     def chunk(self, text): [](#__codelineno-2-8)         return self.tokenizer.tokenize(text) [](#__codelineno-2-9) [](#__codelineno-2-10) # Example Usage [](#__codelineno-2-11) text = """This is an introduction. [](#__codelineno-2-12) This is a detailed discussion on the topic.""" [](#__codelineno-2-13) chunker = TopicSegmentationChunking() [](#__codelineno-2-14) print(chunker.chunk(text))`

#### 4\. Fixed-Length Word Chunking

Segments text into chunks of a fixed word count.

**Code Example**:

`[](#__codelineno-3-1) class FixedLengthWordChunking: [](#__codelineno-3-2)     def __init__(self, chunk_size=100): [](#__codelineno-3-3)         self.chunk_size = chunk_size [](#__codelineno-3-4) [](#__codelineno-3-5)     def chunk(self, text): [](#__codelineno-3-6)         words = text.split() [](#__codelineno-3-7)         return [' '.join(words[i:i + self.chunk_size]) for i in range(0, len(words), self.chunk_size)] [](#__codelineno-3-8) [](#__codelineno-3-9) # Example Usage [](#__codelineno-3-10) text = "This is a long text with many words to be chunked into fixed sizes." [](#__codelineno-3-11) chunker = FixedLengthWordChunking(chunk_size=5) [](#__codelineno-3-12) print(chunker.chunk(text))`

#### 5\. Sliding Window Chunking

Generates overlapping chunks for better contextual coherence.

**Code Example**:

`[](#__codelineno-4-1) class SlidingWindowChunking: [](#__codelineno-4-2)     def __init__(self, window_size=100, step=50): [](#__codelineno-4-3)         self.window_size = window_size [](#__codelineno-4-4)         self.step = step [](#__codelineno-4-5) [](#__codelineno-4-6)     def chunk(self, text): [](#__codelineno-4-7)         words = text.split() [](#__codelineno-4-8)         chunks = [] [](#__codelineno-4-9)         for i in range(0, len(words) - self.window_size + 1, self.step): [](#__codelineno-4-10)             chunks.append(' '.join(words[i:i + self.window_size])) [](#__codelineno-4-11)         return chunks [](#__codelineno-4-12) [](#__codelineno-4-13) # Example Usage [](#__codelineno-4-14) text = "This is a long text to demonstrate sliding window chunking." [](#__codelineno-4-15) chunker = SlidingWindowChunking(window_size=5, step=2) [](#__codelineno-4-16) print(chunker.chunk(text))`

### Combining Chunking with Cosine Similarity

To enhance the relevance of extracted content, chunking strategies can be paired with cosine similarity techniques. Here’s an example workflow:

**Code Example**:

`[](#__codelineno-5-1) from sklearn.feature_extraction.text import TfidfVectorizer [](#__codelineno-5-2) from sklearn.metrics.pairwise import cosine_similarity [](#__codelineno-5-3) [](#__codelineno-5-4) class CosineSimilarityExtractor: [](#__codelineno-5-5)     def __init__(self, query): [](#__codelineno-5-6)         self.query = query [](#__codelineno-5-7)         self.vectorizer = TfidfVectorizer() [](#__codelineno-5-8) [](#__codelineno-5-9)     def find_relevant_chunks(self, chunks): [](#__codelineno-5-10)         vectors = self.vectorizer.fit_transform([self.query] + chunks) [](#__codelineno-5-11)         similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten() [](#__codelineno-5-12)         return [(chunks[i], similarities[i]) for i in range(len(chunks))] [](#__codelineno-5-13) [](#__codelineno-5-14) # Example Workflow [](#__codelineno-5-15) text = """This is a sample document. It has multiple sentences.  [](#__codelineno-5-16) We are testing chunking and similarity.""" [](#__codelineno-5-17) [](#__codelineno-5-18) chunker = SlidingWindowChunking(window_size=5, step=3) [](#__codelineno-5-19) chunks = chunker.chunk(text) [](#__codelineno-5-20) query = "testing chunking" [](#__codelineno-5-21) extractor = CosineSimilarityExtractor(query) [](#__codelineno-5-22) relevant_chunks = extractor.find_relevant_chunks(chunks) [](#__codelineno-5-23) [](#__codelineno-5-24) print(relevant_chunks)`

* * *

---

# Simple Crawling - Crawl4AI Documentation (v0.5.x)

Simple Crawling
===============

This guide covers the basics of web crawling with Crawl4AI. You'll learn how to set up a crawler, make your first request, and understand the response.

Basic Usage
-----------

Set up a simple crawl using `BrowserConfig` and `CrawlerRunConfig`:

`[](#__codelineno-0-1) import asyncio [](#__codelineno-0-2) from crawl4ai import AsyncWebCrawler [](#__codelineno-0-3) from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig [](#__codelineno-0-4) [](#__codelineno-0-5) async def main(): [](#__codelineno-0-6)     browser_config = BrowserConfig()  # Default browser configuration [](#__codelineno-0-7)     run_config = CrawlerRunConfig()   # Default crawl run configuration [](#__codelineno-0-8) [](#__codelineno-0-9)     async with AsyncWebCrawler(config=browser_config) as crawler: [](#__codelineno-0-10)         result = await crawler.arun( [](#__codelineno-0-11)             url="https://example.com", [](#__codelineno-0-12)             config=run_config [](#__codelineno-0-13)         ) [](#__codelineno-0-14)         print(result.markdown)  # Print clean markdown content [](#__codelineno-0-15) [](#__codelineno-0-16) if __name__ == "__main__": [](#__codelineno-0-17)     asyncio.run(main())`

Understanding the Response
--------------------------

The `arun()` method returns a `CrawlResult` object with several useful properties. Here's a quick overview (see [CrawlResult](../../api/crawl-result/)
 for complete details):

`[](#__codelineno-1-1) result = await crawler.arun( [](#__codelineno-1-2)     url="https://example.com", [](#__codelineno-1-3)     config=CrawlerRunConfig(fit_markdown=True) [](#__codelineno-1-4) ) [](#__codelineno-1-5) [](#__codelineno-1-6) # Different content formats [](#__codelineno-1-7) print(result.html)         # Raw HTML [](#__codelineno-1-8) print(result.cleaned_html) # Cleaned HTML [](#__codelineno-1-9) print(result.markdown.raw_markdown) # Raw markdown from cleaned html [](#__codelineno-1-10) print(result.markdown.fit_markdown) # Most relevant content in markdown [](#__codelineno-1-11) [](#__codelineno-1-12) # Check success status [](#__codelineno-1-13) print(result.success)      # True if crawl succeeded [](#__codelineno-1-14) print(result.status_code)  # HTTP status code (e.g., 200, 404) [](#__codelineno-1-15) [](#__codelineno-1-16) # Access extracted media and links [](#__codelineno-1-17) print(result.media)        # Dictionary of found media (images, videos, audio) [](#__codelineno-1-18) print(result.links)        # Dictionary of internal and external links`

Adding Basic Options
--------------------

Customize your crawl using `CrawlerRunConfig`:

`[](#__codelineno-2-1) run_config = CrawlerRunConfig( [](#__codelineno-2-2)     word_count_threshold=10,        # Minimum words per content block [](#__codelineno-2-3)     exclude_external_links=True,    # Remove external links [](#__codelineno-2-4)     remove_overlay_elements=True,   # Remove popups/modals [](#__codelineno-2-5)     process_iframes=True           # Process iframe content [](#__codelineno-2-6) ) [](#__codelineno-2-7) [](#__codelineno-2-8) result = await crawler.arun( [](#__codelineno-2-9)     url="https://example.com", [](#__codelineno-2-10)     config=run_config [](#__codelineno-2-11) )`

Handling Errors
---------------

Always check if the crawl was successful:

`[](#__codelineno-3-1) run_config = CrawlerRunConfig() [](#__codelineno-3-2) result = await crawler.arun(url="https://example.com", config=run_config) [](#__codelineno-3-3) [](#__codelineno-3-4) if not result.success: [](#__codelineno-3-5)     print(f"Crawl failed: {result.error_message}") [](#__codelineno-3-6)     print(f"Status code: {result.status_code}")`

Logging and Debugging
---------------------

Enable verbose logging in `BrowserConfig`:

`[](#__codelineno-4-1) browser_config = BrowserConfig(verbose=True) [](#__codelineno-4-2) [](#__codelineno-4-3) async with AsyncWebCrawler(config=browser_config) as crawler: [](#__codelineno-4-4)     run_config = CrawlerRunConfig() [](#__codelineno-4-5)     result = await crawler.arun(url="https://example.com", config=run_config)`

Complete Example
----------------

Here's a more comprehensive example demonstrating common usage patterns:

`[](#__codelineno-5-1) import asyncio [](#__codelineno-5-2) from crawl4ai import AsyncWebCrawler [](#__codelineno-5-3) from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig, CacheMode [](#__codelineno-5-4) [](#__codelineno-5-5) async def main(): [](#__codelineno-5-6)     browser_config = BrowserConfig(verbose=True) [](#__codelineno-5-7)     run_config = CrawlerRunConfig( [](#__codelineno-5-8)         # Content filtering [](#__codelineno-5-9)         word_count_threshold=10, [](#__codelineno-5-10)         excluded_tags=['form', 'header'], [](#__codelineno-5-11)         exclude_external_links=True, [](#__codelineno-5-12) [](#__codelineno-5-13)         # Content processing [](#__codelineno-5-14)         process_iframes=True, [](#__codelineno-5-15)         remove_overlay_elements=True, [](#__codelineno-5-16) [](#__codelineno-5-17)         # Cache control [](#__codelineno-5-18)         cache_mode=CacheMode.ENABLED  # Use cache if available [](#__codelineno-5-19)     ) [](#__codelineno-5-20) [](#__codelineno-5-21)     async with AsyncWebCrawler(config=browser_config) as crawler: [](#__codelineno-5-22)         result = await crawler.arun( [](#__codelineno-5-23)             url="https://example.com", [](#__codelineno-5-24)             config=run_config [](#__codelineno-5-25)         ) [](#__codelineno-5-26) [](#__codelineno-5-27)         if result.success: [](#__codelineno-5-28)             # Print clean content [](#__codelineno-5-29)             print("Content:", result.markdown[:500])  # First 500 chars [](#__codelineno-5-30) [](#__codelineno-5-31)             # Process images [](#__codelineno-5-32)             for image in result.media["images"]: [](#__codelineno-5-33)                 print(f"Found image: {image['src']}") [](#__codelineno-5-34) [](#__codelineno-5-35)             # Process links [](#__codelineno-5-36)             for link in result.links["internal"]: [](#__codelineno-5-37)                 print(f"Internal link: {link['href']}") [](#__codelineno-5-38) [](#__codelineno-5-39)         else: [](#__codelineno-5-40)             print(f"Crawl failed: {result.error_message}") [](#__codelineno-5-41) [](#__codelineno-5-42) if __name__ == "__main__": [](#__codelineno-5-43)     asyncio.run(main())`

* * *

---

# LLM Strategies - Crawl4AI Documentation (v0.5.x)

Extracting JSON (LLM)
=====================

In some cases, you need to extract **complex or unstructured** information from a webpage that a simple CSS/XPath schema cannot easily parse. Or you want **AI**\-driven insights, classification, or summarization. For these scenarios, Crawl4AI provides an **LLM-based extraction strategy** that:

1.  Works with **any** large language model supported by [LightLLM](https://github.com/LightLLM)
     (Ollama, OpenAI, Claude, and more).
2.  Automatically splits content into chunks (if desired) to handle token limits, then combines results.
3.  Lets you define a **schema** (like a Pydantic model) or a simpler “block” extraction approach.

**Important**: LLM-based extraction can be slower and costlier than schema-based approaches. If your page data is highly structured, consider using [`JsonCssExtractionStrategy`](../no-llm-strategies/)
 or [`JsonXPathExtractionStrategy`](../no-llm-strategies/)
 first. But if you need AI to interpret or reorganize content, read on!

* * *

1\. Why Use an LLM?
-------------------

*   **Complex Reasoning**: If the site’s data is unstructured, scattered, or full of natural language context.
*   **Semantic Extraction**: Summaries, knowledge graphs, or relational data that require comprehension.
*   **Flexible**: You can pass instructions to the model to do more advanced transformations or classification.

* * *

2\. Provider-Agnostic via LightLLM
----------------------------------

Crawl4AI uses a “provider string” (e.g., `"openai/gpt-4o"`, `"ollama/llama2.0"`, `"aws/titan"`) to identify your LLM. **Any** model that LightLLM supports is fair game. You just provide:

*   **`provider`**: The `<provider>/<model_name>` identifier (e.g., `"openai/gpt-4"`, `"ollama/llama2"`, `"huggingface/google-flan"`, etc.).
*   **`api_token`**: If needed (for OpenAI, HuggingFace, etc.); local models or Ollama might not require it.
*   **`api_base`** (optional): If your provider has a custom endpoint.

This means you **aren’t locked** into a single LLM vendor. Switch or experiment easily.

* * *

3\. How LLM Extraction Works
----------------------------

### 3.1 Flow

1. **Chunking** (optional): The HTML or markdown is split into smaller segments if it’s very long (based on `chunk_token_threshold`, overlap, etc.).  
2. **Prompt Construction**: For each chunk, the library forms a prompt that includes your **`instruction`** (and possibly schema or examples).  
3. **LLM Inference**: Each chunk is sent to the model in parallel or sequentially (depending on your concurrency).  
4. **Combining**: The results from each chunk are merged and parsed into JSON.

### 3.2 `extraction_type`

*   **`"schema"`**: The model tries to return JSON conforming to your Pydantic-based schema.
*   **`"block"`**: The model returns freeform text, or smaller JSON structures, which the library collects.

For structured data, `"schema"` is recommended. You provide `schema=YourPydanticModel.model_json_schema()`.

* * *

4\. Key Parameters
------------------

Below is an overview of important LLM extraction parameters. All are typically set inside `LLMExtractionStrategy(...)`. You then put that strategy in your `CrawlerRunConfig(..., extraction_strategy=...)`.

1. **`provider`** (str): e.g., `"openai/gpt-4"`, `"ollama/llama2"`.  
2. **`api_token`** (str): The API key or token for that model. May not be needed for local models.  
3. **`schema`** (dict): A JSON schema describing the fields you want. Usually generated by `YourModel.model_json_schema()`.  
4. **`extraction_type`** (str): `"schema"` or `"block"`.  
5. **`instruction`** (str): Prompt text telling the LLM what you want extracted. E.g., “Extract these fields as a JSON array.”  
6. **`chunk_token_threshold`** (int): Maximum tokens per chunk. If your content is huge, you can break it up for the LLM.  
7. **`overlap_rate`** (float): Overlap ratio between adjacent chunks. E.g., `0.1` means 10% of each chunk is repeated to preserve context continuity.  
8. **`apply_chunking`** (bool): Set `True` to chunk automatically. If you want a single pass, set `False`.  
9. **`input_format`** (str): Determines **which** crawler result is passed to the LLM. Options include:  
\- `"markdown"`: The raw markdown (default).  
\- `"fit_markdown"`: The filtered “fit” markdown if you used a content filter.  
\- `"html"`: The cleaned or raw HTML.  
10. **`extra_args`** (dict): Additional LLM parameters like `temperature`, `max_tokens`, `top_p`, etc.  
11. **`show_usage()`**: A method you can call to print out usage info (token usage per chunk, total cost if known).

**Example**:

`[](#__codelineno-0-1) extraction_strategy = LLMExtractionStrategy( [](#__codelineno-0-2)     llm_config = LLMConfig(provider="openai/gpt-4", api_token="YOUR_OPENAI_KEY"), [](#__codelineno-0-3)     schema=MyModel.model_json_schema(), [](#__codelineno-0-4)     extraction_type="schema", [](#__codelineno-0-5)     instruction="Extract a list of items from the text with 'name' and 'price' fields.", [](#__codelineno-0-6)     chunk_token_threshold=1200, [](#__codelineno-0-7)     overlap_rate=0.1, [](#__codelineno-0-8)     apply_chunking=True, [](#__codelineno-0-9)     input_format="html", [](#__codelineno-0-10)     extra_args={"temperature": 0.1, "max_tokens": 1000}, [](#__codelineno-0-11)     verbose=True [](#__codelineno-0-12) )`

* * *

5\. Putting It in `CrawlerRunConfig`
------------------------------------

**Important**: In Crawl4AI, all strategy definitions should go inside the `CrawlerRunConfig`, not directly as a param in `arun()`. Here’s a full example:

`[](#__codelineno-1-1) import os [](#__codelineno-1-2) import asyncio [](#__codelineno-1-3) import json [](#__codelineno-1-4) from pydantic import BaseModel, Field [](#__codelineno-1-5) from typing import List [](#__codelineno-1-6) from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode, LLMConfig [](#__codelineno-1-7) from crawl4ai.extraction_strategy import LLMExtractionStrategy [](#__codelineno-1-8) [](#__codelineno-1-9) class Product(BaseModel): [](#__codelineno-1-10)     name: str [](#__codelineno-1-11)     price: str [](#__codelineno-1-12) [](#__codelineno-1-13) async def main(): [](#__codelineno-1-14)     # 1. Define the LLM extraction strategy [](#__codelineno-1-15)     llm_strategy = LLMExtractionStrategy( [](#__codelineno-1-16)         llm_config = LLMConfig(provider="openai/gpt-4o-mini", api_token=os.getenv('OPENAI_API_KEY')), [](#__codelineno-1-17)         schema=Product.schema_json(), # Or use model_json_schema() [](#__codelineno-1-18)         extraction_type="schema", [](#__codelineno-1-19)         instruction="Extract all product objects with 'name' and 'price' from the content.", [](#__codelineno-1-20)         chunk_token_threshold=1000, [](#__codelineno-1-21)         overlap_rate=0.0, [](#__codelineno-1-22)         apply_chunking=True, [](#__codelineno-1-23)         input_format="markdown",   # or "html", "fit_markdown" [](#__codelineno-1-24)         extra_args={"temperature": 0.0, "max_tokens": 800} [](#__codelineno-1-25)     ) [](#__codelineno-1-26) [](#__codelineno-1-27)     # 2. Build the crawler config [](#__codelineno-1-28)     crawl_config = CrawlerRunConfig( [](#__codelineno-1-29)         extraction_strategy=llm_strategy, [](#__codelineno-1-30)         cache_mode=CacheMode.BYPASS [](#__codelineno-1-31)     ) [](#__codelineno-1-32) [](#__codelineno-1-33)     # 3. Create a browser config if needed [](#__codelineno-1-34)     browser_cfg = BrowserConfig(headless=True) [](#__codelineno-1-35) [](#__codelineno-1-36)     async with AsyncWebCrawler(config=browser_cfg) as crawler: [](#__codelineno-1-37)         # 4. Let's say we want to crawl a single page [](#__codelineno-1-38)         result = await crawler.arun( [](#__codelineno-1-39)             url="https://example.com/products", [](#__codelineno-1-40)             config=crawl_config [](#__codelineno-1-41)         ) [](#__codelineno-1-42) [](#__codelineno-1-43)         if result.success: [](#__codelineno-1-44)             # 5. The extracted content is presumably JSON [](#__codelineno-1-45)             data = json.loads(result.extracted_content) [](#__codelineno-1-46)             print("Extracted items:", data) [](#__codelineno-1-47) [](#__codelineno-1-48)             # 6. Show usage stats [](#__codelineno-1-49)             llm_strategy.show_usage()  # prints token usage [](#__codelineno-1-50)         else: [](#__codelineno-1-51)             print("Error:", result.error_message) [](#__codelineno-1-52) [](#__codelineno-1-53) if __name__ == "__main__": [](#__codelineno-1-54)     asyncio.run(main())`

* * *

6\. Chunking Details
--------------------

### 6.1 `chunk_token_threshold`

If your page is large, you might exceed your LLM’s context window. **`chunk_token_threshold`** sets the approximate max tokens per chunk. The library calculates word→token ratio using `word_token_rate` (often ~0.75 by default). If chunking is enabled (`apply_chunking=True`), the text is split into segments.

### 6.2 `overlap_rate`

To keep context continuous across chunks, we can overlap them. E.g., `overlap_rate=0.1` means each subsequent chunk includes 10% of the previous chunk’s text. This is helpful if your needed info might straddle chunk boundaries.

### 6.3 Performance & Parallelism

By chunking, you can potentially process multiple chunks in parallel (depending on your concurrency settings and the LLM provider). This reduces total time if the site is huge or has many sections.

* * *

7\. Input Format
----------------

By default, **LLMExtractionStrategy** uses `input_format="markdown"`, meaning the **crawler’s final markdown** is fed to the LLM. You can change to:

*   **`html`**: The cleaned HTML or raw HTML (depending on your crawler config) goes into the LLM.
*   **`fit_markdown`**: If you used, for instance, `PruningContentFilter`, the “fit” version of the markdown is used. This can drastically reduce tokens if you trust the filter.
*   **`markdown`**: Standard markdown output from the crawler’s `markdown_generator`.

This setting is crucial: if the LLM instructions rely on HTML tags, pick `"html"`. If you prefer a text-based approach, pick `"markdown"`.

`[](#__codelineno-2-1) LLMExtractionStrategy( [](#__codelineno-2-2)     # ... [](#__codelineno-2-3)     input_format="html",  # Instead of "markdown" or "fit_markdown" [](#__codelineno-2-4) )`

* * *

8\. Token Usage & Show Usage
----------------------------

To keep track of tokens and cost, each chunk is processed with an LLM call. We record usage in:

*   **`usages`** (list): token usage per chunk or call.
*   **`total_usage`**: sum of all chunk calls.
*   **`show_usage()`**: prints a usage report (if the provider returns usage data).

`[](#__codelineno-3-1) llm_strategy = LLMExtractionStrategy(...) [](#__codelineno-3-2) # ... [](#__codelineno-3-3) llm_strategy.show_usage() [](#__codelineno-3-4) # e.g. “Total usage: 1241 tokens across 2 chunk calls”`

If your model provider doesn’t return usage info, these fields might be partial or empty.

* * *

9\. Example: Building a Knowledge Graph
---------------------------------------

Below is a snippet combining **`LLMExtractionStrategy`** with a Pydantic schema for a knowledge graph. Notice how we pass an **`instruction`** telling the model what to parse.

`[](#__codelineno-4-1) import os [](#__codelineno-4-2) import json [](#__codelineno-4-3) import asyncio [](#__codelineno-4-4) from typing import List [](#__codelineno-4-5) from pydantic import BaseModel, Field [](#__codelineno-4-6) from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode [](#__codelineno-4-7) from crawl4ai.extraction_strategy import LLMExtractionStrategy [](#__codelineno-4-8) [](#__codelineno-4-9) class Entity(BaseModel): [](#__codelineno-4-10)     name: str [](#__codelineno-4-11)     description: str [](#__codelineno-4-12) [](#__codelineno-4-13) class Relationship(BaseModel): [](#__codelineno-4-14)     entity1: Entity [](#__codelineno-4-15)     entity2: Entity [](#__codelineno-4-16)     description: str [](#__codelineno-4-17)     relation_type: str [](#__codelineno-4-18) [](#__codelineno-4-19) class KnowledgeGraph(BaseModel): [](#__codelineno-4-20)     entities: List[Entity] [](#__codelineno-4-21)     relationships: List[Relationship] [](#__codelineno-4-22) [](#__codelineno-4-23) async def main(): [](#__codelineno-4-24)     # LLM extraction strategy [](#__codelineno-4-25)     llm_strat = LLMExtractionStrategy( [](#__codelineno-4-26)         provider="openai/gpt-4", [](#__codelineno-4-27)         api_token=os.getenv('OPENAI_API_KEY'), [](#__codelineno-4-28)         schema=KnowledgeGraph.schema_json(), [](#__codelineno-4-29)         extraction_type="schema", [](#__codelineno-4-30)         instruction="Extract entities and relationships from the content. Return valid JSON.", [](#__codelineno-4-31)         chunk_token_threshold=1400, [](#__codelineno-4-32)         apply_chunking=True, [](#__codelineno-4-33)         input_format="html", [](#__codelineno-4-34)         extra_args={"temperature": 0.1, "max_tokens": 1500} [](#__codelineno-4-35)     ) [](#__codelineno-4-36) [](#__codelineno-4-37)     crawl_config = CrawlerRunConfig( [](#__codelineno-4-38)         extraction_strategy=llm_strat, [](#__codelineno-4-39)         cache_mode=CacheMode.BYPASS [](#__codelineno-4-40)     ) [](#__codelineno-4-41) [](#__codelineno-4-42)     async with AsyncWebCrawler(config=BrowserConfig(headless=True)) as crawler: [](#__codelineno-4-43)         # Example page [](#__codelineno-4-44)         url = "https://www.nbcnews.com/business" [](#__codelineno-4-45)         result = await crawler.arun(url=url, config=crawl_config) [](#__codelineno-4-46) [](#__codelineno-4-47)         if result.success: [](#__codelineno-4-48)             with open("kb_result.json", "w", encoding="utf-8") as f: [](#__codelineno-4-49)                 f.write(result.extracted_content) [](#__codelineno-4-50)             llm_strat.show_usage() [](#__codelineno-4-51)         else: [](#__codelineno-4-52)             print("Crawl failed:", result.error_message) [](#__codelineno-4-53) [](#__codelineno-4-54) if __name__ == "__main__": [](#__codelineno-4-55)     asyncio.run(main())`

**Key Observations**:

*   **`extraction_type="schema"`** ensures we get JSON fitting our `KnowledgeGraph`.
*   **`input_format="html"`** means we feed HTML to the model.
*   **`instruction`** guides the model to output a structured knowledge graph.

* * *

10\. Best Practices & Caveats
-----------------------------

1. **Cost & Latency**: LLM calls can be slow or expensive. Consider chunking or smaller coverage if you only need partial data.  
2. **Model Token Limits**: If your page + instruction exceed the context window, chunking is essential.  
3. **Instruction Engineering**: Well-crafted instructions can drastically improve output reliability.  
4. **Schema Strictness**: `"schema"` extraction tries to parse the model output as JSON. If the model returns invalid JSON, partial extraction might happen, or you might get an error.  
5. **Parallel vs. Serial**: The library can process multiple chunks in parallel, but you must watch out for rate limits on certain providers.  
6. **Check Output**: Sometimes, an LLM might omit fields or produce extraneous text. You may want to post-validate with Pydantic or do additional cleanup.

* * *

11\. Conclusion
---------------

**LLM-based extraction** in Crawl4AI is **provider-agnostic**, letting you choose from hundreds of models via LightLLM. It’s perfect for **semantically complex** tasks or generating advanced structures like knowledge graphs. However, it’s **slower** and potentially costlier than schema-based approaches. Keep these tips in mind:

*   Put your LLM strategy **in `CrawlerRunConfig`**.
*   Use **`input_format`** to pick which form (markdown, HTML, fit\_markdown) the LLM sees.
*   Tweak **`chunk_token_threshold`**, **`overlap_rate`**, and **`apply_chunking`** to handle large content efficiently.
*   Monitor token usage with `show_usage()`.

If your site’s data is consistent or repetitive, consider [`JsonCssExtractionStrategy`](../no-llm-strategies/)
 first for speed and simplicity. But if you need an **AI-driven** approach, `LLMExtractionStrategy` offers a flexible, multi-provider solution for extracting structured JSON from any website.

**Next Steps**:

1. **Experiment with Different Providers**  
\- Try switching the `provider` (e.g., `"ollama/llama2"`, `"openai/gpt-4o"`, etc.) to see differences in speed, accuracy, or cost.  
\- Pass different `extra_args` like `temperature`, `top_p`, and `max_tokens` to fine-tune your results.

2. **Performance Tuning**  
\- If pages are large, tweak `chunk_token_threshold`, `overlap_rate`, or `apply_chunking` to optimize throughput.  
\- Check the usage logs with `show_usage()` to keep an eye on token consumption and identify potential bottlenecks.

3. **Validate Outputs**  
\- If using `extraction_type="schema"`, parse the LLM’s JSON with a Pydantic model for a final validation step.  
\- Log or handle any parse errors gracefully, especially if the model occasionally returns malformed JSON.

4. **Explore Hooks & Automation**  
\- Integrate LLM extraction with [hooks](../../advanced/hooks-auth/)
 for complex pre/post-processing.  
\- Use a multi-step pipeline: crawl, filter, LLM-extract, then store or index results for further analysis.

**Last Updated**: 2025-01-01

* * *

That’s it for **Extracting JSON (LLM)**—now you can harness AI to parse, classify, or reorganize data on the web. Happy crawling!

* * *

---

# 404 Not Found

404 Not Found
=============

* * *

nginx/1.24.0 (Ubuntu)

---

# Clustering Strategies - Crawl4AI Documentation (v0.5.x)

Cosine Strategy
===============

The Cosine Strategy in Crawl4AI uses similarity-based clustering to identify and extract relevant content sections from web pages. This strategy is particularly useful when you need to find and extract content based on semantic similarity rather than structural patterns.

How It Works
------------

The Cosine Strategy: 1. Breaks down page content into meaningful chunks 2. Converts text into vector representations 3. Calculates similarity between chunks 4. Clusters similar content together 5. Ranks and filters content based on relevance

Basic Usage
-----------

`[](#__codelineno-0-1) from crawl4ai.extraction_strategy import CosineStrategy [](#__codelineno-0-2) [](#__codelineno-0-3) strategy = CosineStrategy( [](#__codelineno-0-4)     semantic_filter="product reviews",    # Target content type [](#__codelineno-0-5)     word_count_threshold=10,             # Minimum words per cluster [](#__codelineno-0-6)     sim_threshold=0.3                    # Similarity threshold [](#__codelineno-0-7) ) [](#__codelineno-0-8) [](#__codelineno-0-9) async with AsyncWebCrawler() as crawler: [](#__codelineno-0-10)     result = await crawler.arun( [](#__codelineno-0-11)         url="https://example.com/reviews", [](#__codelineno-0-12)         extraction_strategy=strategy [](#__codelineno-0-13)     ) [](#__codelineno-0-14) [](#__codelineno-0-15)     content = result.extracted_content`

Configuration Options
---------------------

### Core Parameters

`[](#__codelineno-1-1) CosineStrategy( [](#__codelineno-1-2)     # Content Filtering [](#__codelineno-1-3)     semantic_filter: str = None,       # Keywords/topic for content filtering [](#__codelineno-1-4)     word_count_threshold: int = 10,    # Minimum words per cluster [](#__codelineno-1-5)     sim_threshold: float = 0.3,        # Similarity threshold (0.0 to 1.0) [](#__codelineno-1-6) [](#__codelineno-1-7)     # Clustering Parameters [](#__codelineno-1-8)     max_dist: float = 0.2,            # Maximum distance for clustering [](#__codelineno-1-9)     linkage_method: str = 'ward',      # Clustering linkage method [](#__codelineno-1-10)     top_k: int = 3,                   # Number of top categories to extract [](#__codelineno-1-11) [](#__codelineno-1-12)     # Model Configuration [](#__codelineno-1-13)     model_name: str = 'sentence-transformers/all-MiniLM-L6-v2',  # Embedding model [](#__codelineno-1-14) [](#__codelineno-1-15)     verbose: bool = False             # Enable logging [](#__codelineno-1-16) )`

### Parameter Details

1. **semantic\_filter** - Sets the target topic or content type - Use keywords relevant to your desired content - Example: "technical specifications", "user reviews", "pricing information"

2. **sim\_threshold** - Controls how similar content must be to be grouped together - Higher values (e.g., 0.8) mean stricter matching - Lower values (e.g., 0.3) allow more variation

`[](#__codelineno-2-1) # Strict matching [](#__codelineno-2-2) strategy = CosineStrategy(sim_threshold=0.8) [](#__codelineno-2-3) [](#__codelineno-2-4) # Loose matching [](#__codelineno-2-5) strategy = CosineStrategy(sim_threshold=0.3)`

3. **word\_count\_threshold** - Filters out short content blocks - Helps eliminate noise and irrelevant content

`[](#__codelineno-3-1) # Only consider substantial paragraphs [](#__codelineno-3-2) strategy = CosineStrategy(word_count_threshold=50)`

4. **top\_k** - Number of top content clusters to return - Higher values return more diverse content

`[](#__codelineno-4-1) # Get top 5 most relevant content clusters [](#__codelineno-4-2) strategy = CosineStrategy(top_k=5)`

Use Cases
---------

### 1\. Article Content Extraction

`[](#__codelineno-5-1) strategy = CosineStrategy( [](#__codelineno-5-2)     semantic_filter="main article content", [](#__codelineno-5-3)     word_count_threshold=100,  # Longer blocks for articles [](#__codelineno-5-4)     top_k=1                   # Usually want single main content [](#__codelineno-5-5) ) [](#__codelineno-5-6) [](#__codelineno-5-7) result = await crawler.arun( [](#__codelineno-5-8)     url="https://example.com/blog/post", [](#__codelineno-5-9)     extraction_strategy=strategy [](#__codelineno-5-10) )`

### 2\. Product Review Analysis

`[](#__codelineno-6-1) strategy = CosineStrategy( [](#__codelineno-6-2)     semantic_filter="customer reviews and ratings", [](#__codelineno-6-3)     word_count_threshold=20,   # Reviews can be shorter [](#__codelineno-6-4)     top_k=10,                 # Get multiple reviews [](#__codelineno-6-5)     sim_threshold=0.4         # Allow variety in review content [](#__codelineno-6-6) )`

### 3\. Technical Documentation

`[](#__codelineno-7-1) strategy = CosineStrategy( [](#__codelineno-7-2)     semantic_filter="technical specifications documentation", [](#__codelineno-7-3)     word_count_threshold=30, [](#__codelineno-7-4)     sim_threshold=0.6,        # Stricter matching for technical content [](#__codelineno-7-5)     max_dist=0.3             # Allow related technical sections [](#__codelineno-7-6) )`

Advanced Features
-----------------

### Custom Clustering

`[](#__codelineno-8-1) strategy = CosineStrategy( [](#__codelineno-8-2)     linkage_method='complete',  # Alternative clustering method [](#__codelineno-8-3)     max_dist=0.4,              # Larger clusters [](#__codelineno-8-4)     model_name='sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'  # Multilingual support [](#__codelineno-8-5) )`

### Content Filtering Pipeline

`[](#__codelineno-9-1) strategy = CosineStrategy( [](#__codelineno-9-2)     semantic_filter="pricing plans features", [](#__codelineno-9-3)     word_count_threshold=15, [](#__codelineno-9-4)     sim_threshold=0.5, [](#__codelineno-9-5)     top_k=3 [](#__codelineno-9-6) ) [](#__codelineno-9-7) [](#__codelineno-9-8) async def extract_pricing_features(url: str): [](#__codelineno-9-9)     async with AsyncWebCrawler() as crawler: [](#__codelineno-9-10)         result = await crawler.arun( [](#__codelineno-9-11)             url=url, [](#__codelineno-9-12)             extraction_strategy=strategy [](#__codelineno-9-13)         ) [](#__codelineno-9-14) [](#__codelineno-9-15)         if result.success: [](#__codelineno-9-16)             content = json.loads(result.extracted_content) [](#__codelineno-9-17)             return { [](#__codelineno-9-18)                 'pricing_features': content, [](#__codelineno-9-19)                 'clusters': len(content), [](#__codelineno-9-20)                 'similarity_scores': [item['score'] for item in content] [](#__codelineno-9-21)             }`

Best Practices
--------------

1. **Adjust Thresholds Iteratively** - Start with default values - Adjust based on results - Monitor clustering quality

2. **Choose Appropriate Word Count Thresholds** - Higher for articles (100+) - Lower for reviews/comments (20+) - Medium for product descriptions (50+)

3. **Optimize Performance**

`[](#__codelineno-10-1) strategy = CosineStrategy( [](#__codelineno-10-2)     word_count_threshold=10,  # Filter early [](#__codelineno-10-3)     top_k=5,                 # Limit results [](#__codelineno-10-4)     verbose=True             # Monitor performance [](#__codelineno-10-5) )`

4. **Handle Different Content Types**

`[](#__codelineno-11-1) # For mixed content pages [](#__codelineno-11-2) strategy = CosineStrategy( [](#__codelineno-11-3)     semantic_filter="product features", [](#__codelineno-11-4)     sim_threshold=0.4,      # More flexible matching [](#__codelineno-11-5)     max_dist=0.3,          # Larger clusters [](#__codelineno-11-6)     top_k=3                # Multiple relevant sections [](#__codelineno-11-7) )`

Error Handling
--------------

`[](#__codelineno-12-1) try: [](#__codelineno-12-2)     result = await crawler.arun( [](#__codelineno-12-3)         url="https://example.com", [](#__codelineno-12-4)         extraction_strategy=strategy [](#__codelineno-12-5)     ) [](#__codelineno-12-6) [](#__codelineno-12-7)     if result.success: [](#__codelineno-12-8)         content = json.loads(result.extracted_content) [](#__codelineno-12-9)         if not content: [](#__codelineno-12-10)             print("No relevant content found") [](#__codelineno-12-11)     else: [](#__codelineno-12-12)         print(f"Extraction failed: {result.error_message}") [](#__codelineno-12-13) [](#__codelineno-12-14) except Exception as e: [](#__codelineno-12-15)     print(f"Error during extraction: {str(e)}")`

The Cosine Strategy is particularly effective when: - Content structure is inconsistent - You need semantic understanding - You want to find similar content blocks - Structure-based extraction (CSS/XPath) isn't reliable

It works well with other strategies and can be used as a pre-processing step for LLM-based extraction.

* * *

---

# Page Interaction - Crawl4AI Documentation (v0.5.x)

Page Interaction
================

Crawl4AI provides powerful features for interacting with **dynamic** webpages, handling JavaScript execution, waiting for conditions, and managing multi-step flows. By combining **js\_code**, **wait\_for**, and certain **CrawlerRunConfig** parameters, you can:

1.  Click “Load More” buttons
2.  Fill forms and submit them
3.  Wait for elements or data to appear
4.  Reuse sessions across multiple steps

Below is a quick overview of how to do it.

* * *

1\. JavaScript Execution
------------------------

### Basic Execution

**`js_code`** in **`CrawlerRunConfig`** accepts either a single JS string or a list of JS snippets.  
**Example**: We’ll scroll to the bottom of the page, then optionally click a “Load More” button.

`[](#__codelineno-0-1) import asyncio [](#__codelineno-0-2) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig [](#__codelineno-0-3) [](#__codelineno-0-4) async def main(): [](#__codelineno-0-5)     # Single JS command [](#__codelineno-0-6)     config = CrawlerRunConfig( [](#__codelineno-0-7)         js_code="window.scrollTo(0, document.body.scrollHeight);" [](#__codelineno-0-8)     ) [](#__codelineno-0-9) [](#__codelineno-0-10)     async with AsyncWebCrawler() as crawler: [](#__codelineno-0-11)         result = await crawler.arun( [](#__codelineno-0-12)             url="https://news.ycombinator.com",  # Example site [](#__codelineno-0-13)             config=config [](#__codelineno-0-14)         ) [](#__codelineno-0-15)         print("Crawled length:", len(result.cleaned_html)) [](#__codelineno-0-16) [](#__codelineno-0-17)     # Multiple commands [](#__codelineno-0-18)     js_commands = [ [](#__codelineno-0-19)         "window.scrollTo(0, document.body.scrollHeight);", [](#__codelineno-0-20)         # 'More' link on Hacker News [](#__codelineno-0-21)         "document.querySelector('a.morelink')?.click();",   [](#__codelineno-0-22)     ] [](#__codelineno-0-23)     config = CrawlerRunConfig(js_code=js_commands) [](#__codelineno-0-24) [](#__codelineno-0-25)     async with AsyncWebCrawler() as crawler: [](#__codelineno-0-26)         result = await crawler.arun( [](#__codelineno-0-27)             url="https://news.ycombinator.com",  # Another pass [](#__codelineno-0-28)             config=config [](#__codelineno-0-29)         ) [](#__codelineno-0-30)         print("After scroll+click, length:", len(result.cleaned_html)) [](#__codelineno-0-31) [](#__codelineno-0-32) if __name__ == "__main__": [](#__codelineno-0-33)     asyncio.run(main())`

**Relevant `CrawlerRunConfig` params**: - **`js_code`**: A string or list of strings with JavaScript to run after the page loads. - **`js_only`**: If set to `True` on subsequent calls, indicates we’re continuing an existing session without a new full navigation.  
\- **`session_id`**: If you want to keep the same page across multiple calls, specify an ID.

* * *

2\. Wait Conditions
-------------------

### 2.1 CSS-Based Waiting

Sometimes, you just want to wait for a specific element to appear. For example:

`[](#__codelineno-1-1) import asyncio [](#__codelineno-1-2) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig [](#__codelineno-1-3) [](#__codelineno-1-4) async def main(): [](#__codelineno-1-5)     config = CrawlerRunConfig( [](#__codelineno-1-6)         # Wait for at least 30 items on Hacker News [](#__codelineno-1-7)         wait_for="css:.athing:nth-child(30)"   [](#__codelineno-1-8)     ) [](#__codelineno-1-9)     async with AsyncWebCrawler() as crawler: [](#__codelineno-1-10)         result = await crawler.arun( [](#__codelineno-1-11)             url="https://news.ycombinator.com", [](#__codelineno-1-12)             config=config [](#__codelineno-1-13)         ) [](#__codelineno-1-14)         print("We have at least 30 items loaded!") [](#__codelineno-1-15)         # Rough check [](#__codelineno-1-16)         print("Total items in HTML:", result.cleaned_html.count("athing"))   [](#__codelineno-1-17) [](#__codelineno-1-18) if __name__ == "__main__": [](#__codelineno-1-19)     asyncio.run(main())`

**Key param**: - **`wait_for="css:..."`**: Tells the crawler to wait until that CSS selector is present.

### 2.2 JavaScript-Based Waiting

For more complex conditions (e.g., waiting for content length to exceed a threshold), prefix `js:`:

`[](#__codelineno-2-1) wait_condition = """() => { [](#__codelineno-2-2)     const items = document.querySelectorAll('.athing'); [](#__codelineno-2-3)     return items.length > 50;  // Wait for at least 51 items [](#__codelineno-2-4) }""" [](#__codelineno-2-5) [](#__codelineno-2-6) config = CrawlerRunConfig(wait_for=f"js:{wait_condition}")`

**Behind the Scenes**: Crawl4AI keeps polling the JS function until it returns `true` or a timeout occurs.

* * *

3\. Handling Dynamic Content
----------------------------

Many modern sites require **multiple steps**: scrolling, clicking “Load More,” or updating via JavaScript. Below are typical patterns.

### 3.1 Load More Example (Hacker News “More” Link)

`[](#__codelineno-3-1) import asyncio [](#__codelineno-3-2) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig [](#__codelineno-3-3) [](#__codelineno-3-4) async def main(): [](#__codelineno-3-5)     # Step 1: Load initial Hacker News page [](#__codelineno-3-6)     config = CrawlerRunConfig( [](#__codelineno-3-7)         wait_for="css:.athing:nth-child(30)"  # Wait for 30 items [](#__codelineno-3-8)     ) [](#__codelineno-3-9)     async with AsyncWebCrawler() as crawler: [](#__codelineno-3-10)         result = await crawler.arun( [](#__codelineno-3-11)             url="https://news.ycombinator.com", [](#__codelineno-3-12)             config=config [](#__codelineno-3-13)         ) [](#__codelineno-3-14)         print("Initial items loaded.") [](#__codelineno-3-15) [](#__codelineno-3-16)         # Step 2: Let's scroll and click the "More" link [](#__codelineno-3-17)         load_more_js = [ [](#__codelineno-3-18)             "window.scrollTo(0, document.body.scrollHeight);", [](#__codelineno-3-19)             # The "More" link at page bottom [](#__codelineno-3-20)             "document.querySelector('a.morelink')?.click();"   [](#__codelineno-3-21)         ] [](#__codelineno-3-22) [](#__codelineno-3-23)         next_page_conf = CrawlerRunConfig( [](#__codelineno-3-24)             js_code=load_more_js, [](#__codelineno-3-25)             wait_for="""js:() => { [](#__codelineno-3-26)                 return document.querySelectorAll('.athing').length > 30; [](#__codelineno-3-27)             }""", [](#__codelineno-3-28)             # Mark that we do not re-navigate, but run JS in the same session: [](#__codelineno-3-29)             js_only=True, [](#__codelineno-3-30)             session_id="hn_session" [](#__codelineno-3-31)         ) [](#__codelineno-3-32) [](#__codelineno-3-33)         # Re-use the same crawler session [](#__codelineno-3-34)         result2 = await crawler.arun( [](#__codelineno-3-35)             url="https://news.ycombinator.com",  # same URL but continuing session [](#__codelineno-3-36)             config=next_page_conf [](#__codelineno-3-37)         ) [](#__codelineno-3-38)         total_items = result2.cleaned_html.count("athing") [](#__codelineno-3-39)         print("Items after load-more:", total_items) [](#__codelineno-3-40) [](#__codelineno-3-41) if __name__ == "__main__": [](#__codelineno-3-42)     asyncio.run(main())`

**Key params**: - **`session_id="hn_session"`**: Keep the same page across multiple calls to `arun()`. - **`js_only=True`**: We’re not performing a full reload, just applying JS in the existing page. - **`wait_for`** with `js:`: Wait for item count to grow beyond 30.

* * *

### 3.2 Form Interaction

If the site has a search or login form, you can fill fields and submit them with **`js_code`**. For instance, if GitHub had a local search form:

`[](#__codelineno-4-1) js_form_interaction = """ [](#__codelineno-4-2) document.querySelector('#your-search').value = 'TypeScript commits'; [](#__codelineno-4-3) document.querySelector('form').submit(); [](#__codelineno-4-4) """ [](#__codelineno-4-5) [](#__codelineno-4-6) config = CrawlerRunConfig( [](#__codelineno-4-7)     js_code=js_form_interaction, [](#__codelineno-4-8)     wait_for="css:.commit" [](#__codelineno-4-9) ) [](#__codelineno-4-10) result = await crawler.arun(url="https://github.com/search", config=config)`

**In reality**: Replace IDs or classes with the real site’s form selectors.

* * *

4\. Timing Control
------------------

1. **`page_timeout`** (ms): Overall page load or script execution time limit.  
2. **`delay_before_return_html`** (seconds): Wait an extra moment before capturing the final HTML.  
3. **`mean_delay`** & **`max_range`**: If you call `arun_many()` with multiple URLs, these add a random pause between each request.

**Example**:

`[](#__codelineno-5-1) config = CrawlerRunConfig( [](#__codelineno-5-2)     page_timeout=60000,  # 60s limit [](#__codelineno-5-3)     delay_before_return_html=2.5 [](#__codelineno-5-4) )`

* * *

5\. Multi-Step Interaction Example
----------------------------------

Below is a simplified script that does multiple “Load More” clicks on GitHub’s TypeScript commits page. It **re-uses** the same session to accumulate new commits each time. The code includes the relevant **`CrawlerRunConfig`** parameters you’d rely on.

`[](#__codelineno-6-1) import asyncio [](#__codelineno-6-2) from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode [](#__codelineno-6-3) [](#__codelineno-6-4) async def multi_page_commits(): [](#__codelineno-6-5)     browser_cfg = BrowserConfig( [](#__codelineno-6-6)         headless=False,  # Visible for demonstration [](#__codelineno-6-7)         verbose=True [](#__codelineno-6-8)     ) [](#__codelineno-6-9)     session_id = "github_ts_commits" [](#__codelineno-6-10) [](#__codelineno-6-11)     base_wait = """js:() => { [](#__codelineno-6-12)         const commits = document.querySelectorAll('li.Box-sc-g0xbh4-0 h4'); [](#__codelineno-6-13)         return commits.length > 0; [](#__codelineno-6-14)     }""" [](#__codelineno-6-15) [](#__codelineno-6-16)     # Step 1: Load initial commits [](#__codelineno-6-17)     config1 = CrawlerRunConfig( [](#__codelineno-6-18)         wait_for=base_wait, [](#__codelineno-6-19)         session_id=session_id, [](#__codelineno-6-20)         cache_mode=CacheMode.BYPASS, [](#__codelineno-6-21)         # Not using js_only yet since it's our first load [](#__codelineno-6-22)     ) [](#__codelineno-6-23) [](#__codelineno-6-24)     async with AsyncWebCrawler(config=browser_cfg) as crawler: [](#__codelineno-6-25)         result = await crawler.arun( [](#__codelineno-6-26)             url="https://github.com/microsoft/TypeScript/commits/main", [](#__codelineno-6-27)             config=config1 [](#__codelineno-6-28)         ) [](#__codelineno-6-29)         print("Initial commits loaded. Count:", result.cleaned_html.count("commit")) [](#__codelineno-6-30) [](#__codelineno-6-31)         # Step 2: For subsequent pages, we run JS to click 'Next Page' if it exists [](#__codelineno-6-32)         js_next_page = """ [](#__codelineno-6-33)         const selector = 'a[data-testid="pagination-next-button"]'; [](#__codelineno-6-34)         const button = document.querySelector(selector); [](#__codelineno-6-35)         if (button) button.click(); [](#__codelineno-6-36)         """ [](#__codelineno-6-37) [](#__codelineno-6-38)         # Wait until new commits appear [](#__codelineno-6-39)         wait_for_more = """js:() => { [](#__codelineno-6-40)             const commits = document.querySelectorAll('li.Box-sc-g0xbh4-0 h4'); [](#__codelineno-6-41)             if (!window.firstCommit && commits.length>0) { [](#__codelineno-6-42)                 window.firstCommit = commits[0].textContent; [](#__codelineno-6-43)                 return false; [](#__codelineno-6-44)             } [](#__codelineno-6-45)             // If top commit changes, we have new commits [](#__codelineno-6-46)             const topNow = commits[0]?.textContent.trim(); [](#__codelineno-6-47)             return topNow && topNow !== window.firstCommit; [](#__codelineno-6-48)         }""" [](#__codelineno-6-49) [](#__codelineno-6-50)         for page in range(2):  # let's do 2 more "Next" pages [](#__codelineno-6-51)             config_next = CrawlerRunConfig( [](#__codelineno-6-52)                 session_id=session_id, [](#__codelineno-6-53)                 js_code=js_next_page, [](#__codelineno-6-54)                 wait_for=wait_for_more, [](#__codelineno-6-55)                 js_only=True,       # We're continuing from the open tab [](#__codelineno-6-56)                 cache_mode=CacheMode.BYPASS [](#__codelineno-6-57)             ) [](#__codelineno-6-58)             result2 = await crawler.arun( [](#__codelineno-6-59)                 url="https://github.com/microsoft/TypeScript/commits/main", [](#__codelineno-6-60)                 config=config_next [](#__codelineno-6-61)             ) [](#__codelineno-6-62)             print(f"Page {page+2} commits count:", result2.cleaned_html.count("commit")) [](#__codelineno-6-63) [](#__codelineno-6-64)         # Optionally kill session [](#__codelineno-6-65)         await crawler.crawler_strategy.kill_session(session_id) [](#__codelineno-6-66) [](#__codelineno-6-67) async def main(): [](#__codelineno-6-68)     await multi_page_commits() [](#__codelineno-6-69) [](#__codelineno-6-70) if __name__ == "__main__": [](#__codelineno-6-71)     asyncio.run(main())`

**Key Points**:

*   **`session_id`**: Keep the same page open.
*   **`js_code`** + **`wait_for`** + **`js_only=True`**: We do partial refreshes, waiting for new commits to appear.
*   **`cache_mode=CacheMode.BYPASS`** ensures we always see fresh data each step.

* * *

6\. Combine Interaction with Extraction
---------------------------------------

Once dynamic content is loaded, you can attach an **`extraction_strategy`** (like `JsonCssExtractionStrategy` or `LLMExtractionStrategy`). For example:

`[](#__codelineno-7-1) from crawl4ai.extraction_strategy import JsonCssExtractionStrategy [](#__codelineno-7-2) [](#__codelineno-7-3) schema = { [](#__codelineno-7-4)     "name": "Commits", [](#__codelineno-7-5)     "baseSelector": "li.Box-sc-g0xbh4-0", [](#__codelineno-7-6)     "fields": [ [](#__codelineno-7-7)         {"name": "title", "selector": "h4.markdown-title", "type": "text"} [](#__codelineno-7-8)     ] [](#__codelineno-7-9) } [](#__codelineno-7-10) config = CrawlerRunConfig( [](#__codelineno-7-11)     session_id="ts_commits_session", [](#__codelineno-7-12)     js_code=js_next_page, [](#__codelineno-7-13)     wait_for=wait_for_more, [](#__codelineno-7-14)     extraction_strategy=JsonCssExtractionStrategy(schema) [](#__codelineno-7-15) )`

When done, check `result.extracted_content` for the JSON.

* * *

7\. Relevant `CrawlerRunConfig` Parameters
------------------------------------------

Below are the key interaction-related parameters in `CrawlerRunConfig`. For a full list, see [Configuration Parameters](../../api/parameters/)
.

*   **`js_code`**: JavaScript to run after initial load.
*   **`js_only`**: If `True`, no new page navigation—only JS in the existing session.
*   **`wait_for`**: CSS (`"css:..."`) or JS (`"js:..."`) expression to wait for.
*   **`session_id`**: Reuse the same page across calls.
*   **`cache_mode`**: Whether to read/write from the cache or bypass.
*   **`remove_overlay_elements`**: Remove certain popups automatically.
*   **`simulate_user`, `override_navigator`, `magic`**: Anti-bot or “human-like” interactions.

* * *

8\. Conclusion
--------------

Crawl4AI’s **page interaction** features let you:

1. **Execute JavaScript** for scrolling, clicks, or form filling.  
2. **Wait** for CSS or custom JS conditions before capturing data.  
3. **Handle** multi-step flows (like “Load More”) with partial reloads or persistent sessions.  
4\. Combine with **structured extraction** for dynamic sites.

With these tools, you can scrape modern, interactive webpages confidently. For advanced hooking, user simulation, or in-depth config, check the [API reference](../../api/parameters/)
 or related advanced docs. Happy scripting!

* * *

---

# Quick Start - Crawl4AI Documentation (v0.5.x)

Getting Started with Crawl4AI
=============================

Welcome to **Crawl4AI**, an open-source LLM-friendly Web Crawler & Scraper. In this tutorial, you’ll:

1.  Run your **first crawl** using minimal configuration.
2.  Generate **Markdown** output (and learn how it’s influenced by content filters).
3.  Experiment with a simple **CSS-based extraction** strategy.
4.  See a glimpse of **LLM-based extraction** (including open-source and closed-source model options).
5.  Crawl a **dynamic** page that loads content via JavaScript.

* * *

1\. Introduction
----------------

Crawl4AI provides:

*   An asynchronous crawler, **`AsyncWebCrawler`**.
*   Configurable browser and run settings via **`BrowserConfig`** and **`CrawlerRunConfig`**.
*   Automatic HTML-to-Markdown conversion via **`DefaultMarkdownGenerator`** (supports optional filters).
*   Multiple extraction strategies (LLM-based or “traditional” CSS/XPath-based).

By the end of this guide, you’ll have performed a basic crawl, generated Markdown, tried out two extraction strategies, and crawled a dynamic page that uses “Load More” buttons or JavaScript updates.

* * *

2\. Your First Crawl
--------------------

Here’s a minimal Python script that creates an **`AsyncWebCrawler`**, fetches a webpage, and prints the first 300 characters of its Markdown output:

`[](#__codelineno-0-1) import asyncio [](#__codelineno-0-2) from crawl4ai import AsyncWebCrawler [](#__codelineno-0-3) [](#__codelineno-0-4) async def main(): [](#__codelineno-0-5)     async with AsyncWebCrawler() as crawler: [](#__codelineno-0-6)         result = await crawler.arun("https://example.com") [](#__codelineno-0-7)         print(result.markdown[:300])  # Print first 300 chars [](#__codelineno-0-8) [](#__codelineno-0-9) if __name__ == "__main__": [](#__codelineno-0-10)     asyncio.run(main())`

**What’s happening?** - **`AsyncWebCrawler`** launches a headless browser (Chromium by default). - It fetches `https://example.com`. - Crawl4AI automatically converts the HTML into Markdown.

You now have a simple, working crawl!

* * *

3\. Basic Configuration (Light Introduction)
--------------------------------------------

Crawl4AI’s crawler can be heavily customized using two main classes:

1. **`BrowserConfig`**: Controls browser behavior (headless or full UI, user agent, JavaScript toggles, etc.).  
2. **`CrawlerRunConfig`**: Controls how each crawl runs (caching, extraction, timeouts, hooking, etc.).

Below is an example with minimal usage:

`[](#__codelineno-1-1) import asyncio [](#__codelineno-1-2) from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode [](#__codelineno-1-3) [](#__codelineno-1-4) async def main(): [](#__codelineno-1-5)     browser_conf = BrowserConfig(headless=True)  # or False to see the browser [](#__codelineno-1-6)     run_conf = CrawlerRunConfig( [](#__codelineno-1-7)         cache_mode=CacheMode.BYPASS [](#__codelineno-1-8)     ) [](#__codelineno-1-9) [](#__codelineno-1-10)     async with AsyncWebCrawler(config=browser_conf) as crawler: [](#__codelineno-1-11)         result = await crawler.arun( [](#__codelineno-1-12)             url="https://example.com", [](#__codelineno-1-13)             config=run_conf [](#__codelineno-1-14)         ) [](#__codelineno-1-15)         print(result.markdown) [](#__codelineno-1-16) [](#__codelineno-1-17) if __name__ == "__main__": [](#__codelineno-1-18)     asyncio.run(main())`

> IMPORTANT: By default cache mode is set to `CacheMode.ENABLED`. So to have fresh content, you need to set it to `CacheMode.BYPASS`

We’ll explore more advanced config in later tutorials (like enabling proxies, PDF output, multi-tab sessions, etc.). For now, just note how you pass these objects to manage crawling.

* * *

4\. Generating Markdown Output
------------------------------

By default, Crawl4AI automatically generates Markdown from each crawled page. However, the exact output depends on whether you specify a **markdown generator** or **content filter**.

*   **`result.markdown`**:  
    The direct HTML-to-Markdown conversion.
*   **`result.markdown.fit_markdown`**:  
    The same content after applying any configured **content filter** (e.g., `PruningContentFilter`).

### Example: Using a Filter with `DefaultMarkdownGenerator`

`[](#__codelineno-2-1) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig [](#__codelineno-2-2) from crawl4ai.content_filter_strategy import PruningContentFilter [](#__codelineno-2-3) from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator [](#__codelineno-2-4) [](#__codelineno-2-5) md_generator = DefaultMarkdownGenerator( [](#__codelineno-2-6)     content_filter=PruningContentFilter(threshold=0.4, threshold_type="fixed") [](#__codelineno-2-7) ) [](#__codelineno-2-8) [](#__codelineno-2-9) config = CrawlerRunConfig( [](#__codelineno-2-10)     cache_mode=CacheMode.BYPASS, [](#__codelineno-2-11)     markdown_generator=md_generator [](#__codelineno-2-12) ) [](#__codelineno-2-13) [](#__codelineno-2-14) async with AsyncWebCrawler() as crawler: [](#__codelineno-2-15)     result = await crawler.arun("https://news.ycombinator.com", config=config) [](#__codelineno-2-16)     print("Raw Markdown length:", len(result.markdown.raw_markdown)) [](#__codelineno-2-17)     print("Fit Markdown length:", len(result.markdown.fit_markdown))`

**Note**: If you do **not** specify a content filter or markdown generator, you’ll typically see only the raw Markdown. `PruningContentFilter` may adds around `50ms` in processing time. We’ll dive deeper into these strategies in a dedicated **Markdown Generation** tutorial.

* * *

5\. Simple Data Extraction (CSS-based)
--------------------------------------

Crawl4AI can also extract structured data (JSON) using CSS or XPath selectors. Below is a minimal CSS-based example:

> **New!** Crawl4AI now provides a powerful utility to automatically generate extraction schemas using LLM. This is a one-time cost that gives you a reusable schema for fast, LLM-free extractions:

`[](#__codelineno-3-1) from crawl4ai.extraction_strategy import JsonCssExtractionStrategy [](#__codelineno-3-2) from crawl4ai import LLMConfig [](#__codelineno-3-3) [](#__codelineno-3-4) # Generate a schema (one-time cost) [](#__codelineno-3-5) html = "<div class='product'><h2>Gaming Laptop</h2><span class='price'>$999.99</span></div>" [](#__codelineno-3-6) [](#__codelineno-3-7) # Using OpenAI (requires API token) [](#__codelineno-3-8) schema = JsonCssExtractionStrategy.generate_schema( [](#__codelineno-3-9)     html, [](#__codelineno-3-10)     llm_config = LLMConfig(provider="openai/gpt-4o",api_token="your-openai-token")  # Required for OpenAI [](#__codelineno-3-11) ) [](#__codelineno-3-12) [](#__codelineno-3-13) # Or using Ollama (open source, no token needed) [](#__codelineno-3-14) schema = JsonCssExtractionStrategy.generate_schema( [](#__codelineno-3-15)     html, [](#__codelineno-3-16)     llm_config = LLMConfig(provider="ollama/llama3.3", api_token=None)  # Not needed for Ollama [](#__codelineno-3-17) ) [](#__codelineno-3-18) [](#__codelineno-3-19) # Use the schema for fast, repeated extractions [](#__codelineno-3-20) strategy = JsonCssExtractionStrategy(schema)`

For a complete guide on schema generation and advanced usage, see [No-LLM Extraction Strategies](../../extraction/no-llm-strategies/)
.

Here's a basic extraction example:

`[](#__codelineno-4-1) import asyncio [](#__codelineno-4-2) import json [](#__codelineno-4-3) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode [](#__codelineno-4-4) from crawl4ai.extraction_strategy import JsonCssExtractionStrategy [](#__codelineno-4-5) [](#__codelineno-4-6) async def main(): [](#__codelineno-4-7)     schema = { [](#__codelineno-4-8)         "name": "Example Items", [](#__codelineno-4-9)         "baseSelector": "div.item", [](#__codelineno-4-10)         "fields": [ [](#__codelineno-4-11)             {"name": "title", "selector": "h2", "type": "text"}, [](#__codelineno-4-12)             {"name": "link", "selector": "a", "type": "attribute", "attribute": "href"} [](#__codelineno-4-13)         ] [](#__codelineno-4-14)     } [](#__codelineno-4-15) [](#__codelineno-4-16)     raw_html = "<div class='item'><h2>Item 1</h2><a href='https://example.com/item1'>Link 1</a></div>" [](#__codelineno-4-17) [](#__codelineno-4-18)     async with AsyncWebCrawler() as crawler: [](#__codelineno-4-19)         result = await crawler.arun( [](#__codelineno-4-20)             url="raw://" + raw_html, [](#__codelineno-4-21)             config=CrawlerRunConfig( [](#__codelineno-4-22)                 cache_mode=CacheMode.BYPASS, [](#__codelineno-4-23)                 extraction_strategy=JsonCssExtractionStrategy(schema) [](#__codelineno-4-24)             ) [](#__codelineno-4-25)         ) [](#__codelineno-4-26)         # The JSON output is stored in 'extracted_content' [](#__codelineno-4-27)         data = json.loads(result.extracted_content) [](#__codelineno-4-28)         print(data) [](#__codelineno-4-29) [](#__codelineno-4-30) if __name__ == "__main__": [](#__codelineno-4-31)     asyncio.run(main())`

**Why is this helpful?** - Great for repetitive page structures (e.g., item listings, articles). - No AI usage or costs. - The crawler returns a JSON string you can parse or store.

> Tips: You can pass raw HTML to the crawler instead of a URL. To do so, prefix the HTML with `raw://`.

* * *

6\. Simple Data Extraction (LLM-based)
--------------------------------------

For more complex or irregular pages, a language model can parse text intelligently into a structure you define. Crawl4AI supports **open-source** or **closed-source** providers:

*   **Open-Source Models** (e.g., `ollama/llama3.3`, `no_token`)
*   **OpenAI Models** (e.g., `openai/gpt-4`, requires `api_token`)
*   Or any provider supported by the underlying library

Below is an example using **open-source** style (no token) and closed-source:

`[](#__codelineno-5-1) import os [](#__codelineno-5-2) import json [](#__codelineno-5-3) import asyncio [](#__codelineno-5-4) from pydantic import BaseModel, Field [](#__codelineno-5-5) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, LLMConfig [](#__codelineno-5-6) from crawl4ai.extraction_strategy import LLMExtractionStrategy [](#__codelineno-5-7) [](#__codelineno-5-8) class OpenAIModelFee(BaseModel): [](#__codelineno-5-9)     model_name: str = Field(..., description="Name of the OpenAI model.") [](#__codelineno-5-10)     input_fee: str = Field(..., description="Fee for input token for the OpenAI model.") [](#__codelineno-5-11)     output_fee: str = Field( [](#__codelineno-5-12)         ..., description="Fee for output token for the OpenAI model." [](#__codelineno-5-13)     ) [](#__codelineno-5-14) [](#__codelineno-5-15) async def extract_structured_data_using_llm( [](#__codelineno-5-16)     provider: str, api_token: str = None, extra_headers: Dict[str, str] = None [](#__codelineno-5-17) ): [](#__codelineno-5-18)     print(f"\n--- Extracting Structured Data with {provider} ---") [](#__codelineno-5-19) [](#__codelineno-5-20)     if api_token is None and provider != "ollama": [](#__codelineno-5-21)         print(f"API token is required for {provider}. Skipping this example.") [](#__codelineno-5-22)         return [](#__codelineno-5-23) [](#__codelineno-5-24)     browser_config = BrowserConfig(headless=True) [](#__codelineno-5-25) [](#__codelineno-5-26)     extra_args = {"temperature": 0, "top_p": 0.9, "max_tokens": 2000} [](#__codelineno-5-27)     if extra_headers: [](#__codelineno-5-28)         extra_args["extra_headers"] = extra_headers [](#__codelineno-5-29) [](#__codelineno-5-30)     crawler_config = CrawlerRunConfig( [](#__codelineno-5-31)         cache_mode=CacheMode.BYPASS, [](#__codelineno-5-32)         word_count_threshold=1, [](#__codelineno-5-33)         page_timeout=80000, [](#__codelineno-5-34)         extraction_strategy=LLMExtractionStrategy( [](#__codelineno-5-35)             llm_config = LLMConfig(provider=provider,api_token=api_token), [](#__codelineno-5-36)             schema=OpenAIModelFee.model_json_schema(), [](#__codelineno-5-37)             extraction_type="schema", [](#__codelineno-5-38)             instruction="""From the crawled content, extract all mentioned model names along with their fees for input and output tokens.  [](#__codelineno-5-39)             Do not miss any models in the entire content.""", [](#__codelineno-5-40)             extra_args=extra_args, [](#__codelineno-5-41)         ), [](#__codelineno-5-42)     ) [](#__codelineno-5-43) [](#__codelineno-5-44)     async with AsyncWebCrawler(config=browser_config) as crawler: [](#__codelineno-5-45)         result = await crawler.arun( [](#__codelineno-5-46)             url="https://openai.com/api/pricing/", config=crawler_config [](#__codelineno-5-47)         ) [](#__codelineno-5-48)         print(result.extracted_content) [](#__codelineno-5-49) [](#__codelineno-5-50) if __name__ == "__main__": [](#__codelineno-5-51) [](#__codelineno-5-52)     asyncio.run( [](#__codelineno-5-53)         extract_structured_data_using_llm( [](#__codelineno-5-54)             provider="openai/gpt-4o", api_token=os.getenv("OPENAI_API_KEY") [](#__codelineno-5-55)         ) [](#__codelineno-5-56)     )`

**What’s happening?** - We define a Pydantic schema (`PricingInfo`) describing the fields we want. - The LLM extraction strategy uses that schema and your instructions to transform raw text into structured JSON. - Depending on the **provider** and **api\_token**, you can use local models or a remote API.

* * *

7\. Multi-URL Concurrency (Preview)
-----------------------------------

If you need to crawl multiple URLs in **parallel**, you can use `arun_many()`. By default, Crawl4AI employs a **MemoryAdaptiveDispatcher**, automatically adjusting concurrency based on system resources. Here’s a quick glimpse:

`[](#__codelineno-6-1) import asyncio [](#__codelineno-6-2) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode [](#__codelineno-6-3) [](#__codelineno-6-4) async def quick_parallel_example(): [](#__codelineno-6-5)     urls = [ [](#__codelineno-6-6)         "https://example.com/page1", [](#__codelineno-6-7)         "https://example.com/page2", [](#__codelineno-6-8)         "https://example.com/page3" [](#__codelineno-6-9)     ] [](#__codelineno-6-10) [](#__codelineno-6-11)     run_conf = CrawlerRunConfig( [](#__codelineno-6-12)         cache_mode=CacheMode.BYPASS, [](#__codelineno-6-13)         stream=True  # Enable streaming mode [](#__codelineno-6-14)     ) [](#__codelineno-6-15) [](#__codelineno-6-16)     async with AsyncWebCrawler() as crawler: [](#__codelineno-6-17)         # Stream results as they complete [](#__codelineno-6-18)         async for result in await crawler.arun_many(urls, config=run_conf): [](#__codelineno-6-19)             if result.success: [](#__codelineno-6-20)                 print(f"[OK] {result.url}, length: {len(result.markdown.raw_markdown)}") [](#__codelineno-6-21)             else: [](#__codelineno-6-22)                 print(f"[ERROR] {result.url} => {result.error_message}") [](#__codelineno-6-23) [](#__codelineno-6-24)         # Or get all results at once (default behavior) [](#__codelineno-6-25)         run_conf = run_conf.clone(stream=False) [](#__codelineno-6-26)         results = await crawler.arun_many(urls, config=run_conf) [](#__codelineno-6-27)         for res in results: [](#__codelineno-6-28)             if res.success: [](#__codelineno-6-29)                 print(f"[OK] {res.url}, length: {len(res.markdown.raw_markdown)}") [](#__codelineno-6-30)             else: [](#__codelineno-6-31)                 print(f"[ERROR] {res.url} => {res.error_message}") [](#__codelineno-6-32) [](#__codelineno-6-33) if __name__ == "__main__": [](#__codelineno-6-34)     asyncio.run(quick_parallel_example())`

The example above shows two ways to handle multiple URLs: 1. **Streaming mode** (`stream=True`): Process results as they become available using `async for` 2. **Batch mode** (`stream=False`): Wait for all results to complete

For more advanced concurrency (e.g., a **semaphore-based** approach, **adaptive memory usage throttling**, or customized rate limiting), see [Advanced Multi-URL Crawling](../../advanced/multi-url-crawling/)
.

* * *

8\. Dynamic Content Example
---------------------------

Some sites require multiple “page clicks” or dynamic JavaScript updates. Below is an example showing how to **click** a “Next Page” button and wait for new commits to load on GitHub, using **`BrowserConfig`** and **`CrawlerRunConfig`**:

`[](#__codelineno-7-1) import asyncio [](#__codelineno-7-2) from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode [](#__codelineno-7-3) from crawl4ai.extraction_strategy import JsonCssExtractionStrategy [](#__codelineno-7-4) [](#__codelineno-7-5) async def extract_structured_data_using_css_extractor(): [](#__codelineno-7-6)     print("\n--- Using JsonCssExtractionStrategy for Fast Structured Output ---") [](#__codelineno-7-7)     schema = { [](#__codelineno-7-8)         "name": "KidoCode Courses", [](#__codelineno-7-9)         "baseSelector": "section.charge-methodology .w-tab-content > div", [](#__codelineno-7-10)         "fields": [ [](#__codelineno-7-11)             { [](#__codelineno-7-12)                 "name": "section_title", [](#__codelineno-7-13)                 "selector": "h3.heading-50", [](#__codelineno-7-14)                 "type": "text", [](#__codelineno-7-15)             }, [](#__codelineno-7-16)             { [](#__codelineno-7-17)                 "name": "section_description", [](#__codelineno-7-18)                 "selector": ".charge-content", [](#__codelineno-7-19)                 "type": "text", [](#__codelineno-7-20)             }, [](#__codelineno-7-21)             { [](#__codelineno-7-22)                 "name": "course_name", [](#__codelineno-7-23)                 "selector": ".text-block-93", [](#__codelineno-7-24)                 "type": "text", [](#__codelineno-7-25)             }, [](#__codelineno-7-26)             { [](#__codelineno-7-27)                 "name": "course_description", [](#__codelineno-7-28)                 "selector": ".course-content-text", [](#__codelineno-7-29)                 "type": "text", [](#__codelineno-7-30)             }, [](#__codelineno-7-31)             { [](#__codelineno-7-32)                 "name": "course_icon", [](#__codelineno-7-33)                 "selector": ".image-92", [](#__codelineno-7-34)                 "type": "attribute", [](#__codelineno-7-35)                 "attribute": "src", [](#__codelineno-7-36)             }, [](#__codelineno-7-37)         ], [](#__codelineno-7-38)     } [](#__codelineno-7-39) [](#__codelineno-7-40)     browser_config = BrowserConfig(headless=True, java_script_enabled=True) [](#__codelineno-7-41) [](#__codelineno-7-42)     js_click_tabs = """ [](#__codelineno-7-43)     (async () => { [](#__codelineno-7-44)         const tabs = document.querySelectorAll("section.charge-methodology .tabs-menu-3 > div"); [](#__codelineno-7-45)         for(let tab of tabs) { [](#__codelineno-7-46)             tab.scrollIntoView(); [](#__codelineno-7-47)             tab.click(); [](#__codelineno-7-48)             await new Promise(r => setTimeout(r, 500)); [](#__codelineno-7-49)         } [](#__codelineno-7-50)     })(); [](#__codelineno-7-51)     """ [](#__codelineno-7-52) [](#__codelineno-7-53)     crawler_config = CrawlerRunConfig( [](#__codelineno-7-54)         cache_mode=CacheMode.BYPASS, [](#__codelineno-7-55)         extraction_strategy=JsonCssExtractionStrategy(schema), [](#__codelineno-7-56)         js_code=[js_click_tabs], [](#__codelineno-7-57)     ) [](#__codelineno-7-58) [](#__codelineno-7-59)     async with AsyncWebCrawler(config=browser_config) as crawler: [](#__codelineno-7-60)         result = await crawler.arun( [](#__codelineno-7-61)             url="https://www.kidocode.com/degrees/technology", config=crawler_config [](#__codelineno-7-62)         ) [](#__codelineno-7-63) [](#__codelineno-7-64)         companies = json.loads(result.extracted_content) [](#__codelineno-7-65)         print(f"Successfully extracted {len(companies)} companies") [](#__codelineno-7-66)         print(json.dumps(companies[0], indent=2)) [](#__codelineno-7-67) [](#__codelineno-7-68) async def main(): [](#__codelineno-7-69)     await extract_structured_data_using_css_extractor() [](#__codelineno-7-70) [](#__codelineno-7-71) if __name__ == "__main__": [](#__codelineno-7-72)     asyncio.run(main())`

**Key Points**:

*   **`BrowserConfig(headless=False)`**: We want to watch it click “Next Page.”
*   **`CrawlerRunConfig(...)`**: We specify the extraction strategy, pass `session_id` to reuse the same page.
*   **`js_code`** and **`wait_for`** are used for subsequent pages (`page > 0`) to click the “Next” button and wait for new commits to load.
*   **`js_only=True`** indicates we’re not re-navigating but continuing the existing session.
*   Finally, we call `kill_session()` to clean up the page and browser session.

* * *

9\. Next Steps
--------------

Congratulations! You have:

1.  Performed a basic crawl and printed Markdown.
2.  Used **content filters** with a markdown generator.
3.  Extracted JSON via **CSS** or **LLM** strategies.
4.  Handled **dynamic** pages with JavaScript triggers.

If you’re ready for more, check out:

*   **Installation**: A deeper dive into advanced installs, Docker usage (experimental), or optional dependencies.
*   **Hooks & Auth**: Learn how to run custom JavaScript or handle logins with cookies, local storage, etc.
*   **Deployment**: Explore ephemeral testing in Docker or plan for the upcoming stable Docker release.
*   **Browser Management**: Delve into user simulation, stealth modes, and concurrency best practices.

Crawl4AI is a powerful, flexible tool. Enjoy building out your scrapers, data pipelines, or AI-driven extraction flows. Happy crawling!

* * *

---

# LLM-Free Strategies - Crawl4AI Documentation (v0.5.x)

Extracting JSON (No LLM)
========================

One of Crawl4AI’s **most powerful** features is extracting **structured JSON** from websites **without** relying on large language models. By defining a **schema** with CSS or XPath selectors, you can extract data instantly—even from complex or nested HTML structures—without the cost, latency, or environmental impact of an LLM.

**Why avoid LLM for basic extractions?**

1. **Faster & Cheaper**: No API calls or GPU overhead.  
2. **Lower Carbon Footprint**: LLM inference can be energy-intensive. A well-defined schema is practically carbon-free.  
3. **Precise & Repeatable**: CSS/XPath selectors do exactly what you specify. LLM outputs can vary or hallucinate.  
4. **Scales Readily**: For thousands of pages, schema-based extraction runs quickly and in parallel.

Below, we’ll explore how to craft these schemas and use them with **JsonCssExtractionStrategy** (or **JsonXPathExtractionStrategy** if you prefer XPath). We’ll also highlight advanced features like **nested fields** and **base element attributes**.

* * *

1\. Intro to Schema-Based Extraction
------------------------------------

A schema defines:

1.  A **base selector** that identifies each “container” element on the page (e.g., a product row, a blog post card).  
    2. **Fields** describing which CSS/XPath selectors to use for each piece of data you want to capture (text, attribute, HTML block, etc.).  
    3. **Nested** or **list** types for repeated or hierarchical structures.

For example, if you have a list of products, each one might have a name, price, reviews, and “related products.” This approach is faster and more reliable than an LLM for consistent, structured pages.

* * *

2\. Simple Example: Crypto Prices
---------------------------------

Let’s begin with a **simple** schema-based extraction using the `JsonCssExtractionStrategy`. Below is a snippet that extracts cryptocurrency prices from a site (similar to the legacy Coinbase example). Notice we **don’t** call any LLM:

`[](#__codelineno-0-1) import json [](#__codelineno-0-2) import asyncio [](#__codelineno-0-3) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode [](#__codelineno-0-4) from crawl4ai.extraction_strategy import JsonCssExtractionStrategy [](#__codelineno-0-5) [](#__codelineno-0-6) async def extract_crypto_prices(): [](#__codelineno-0-7)     # 1. Define a simple extraction schema [](#__codelineno-0-8)     schema = { [](#__codelineno-0-9)         "name": "Crypto Prices", [](#__codelineno-0-10)         "baseSelector": "div.crypto-row",    # Repeated elements [](#__codelineno-0-11)         "fields": [ [](#__codelineno-0-12)             { [](#__codelineno-0-13)                 "name": "coin_name", [](#__codelineno-0-14)                 "selector": "h2.coin-name", [](#__codelineno-0-15)                 "type": "text" [](#__codelineno-0-16)             }, [](#__codelineno-0-17)             { [](#__codelineno-0-18)                 "name": "price", [](#__codelineno-0-19)                 "selector": "span.coin-price", [](#__codelineno-0-20)                 "type": "text" [](#__codelineno-0-21)             } [](#__codelineno-0-22)         ] [](#__codelineno-0-23)     } [](#__codelineno-0-24) [](#__codelineno-0-25)     # 2. Create the extraction strategy [](#__codelineno-0-26)     extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True) [](#__codelineno-0-27) [](#__codelineno-0-28)     # 3. Set up your crawler config (if needed) [](#__codelineno-0-29)     config = CrawlerRunConfig( [](#__codelineno-0-30)         # e.g., pass js_code or wait_for if the page is dynamic [](#__codelineno-0-31)         # wait_for="css:.crypto-row:nth-child(20)" [](#__codelineno-0-32)         cache_mode = CacheMode.BYPASS, [](#__codelineno-0-33)         extraction_strategy=extraction_strategy, [](#__codelineno-0-34)     ) [](#__codelineno-0-35) [](#__codelineno-0-36)     async with AsyncWebCrawler(verbose=True) as crawler: [](#__codelineno-0-37)         # 4. Run the crawl and extraction [](#__codelineno-0-38)         result = await crawler.arun( [](#__codelineno-0-39)             url="https://example.com/crypto-prices", [](#__codelineno-0-40) [](#__codelineno-0-41)             config=config [](#__codelineno-0-42)         ) [](#__codelineno-0-43) [](#__codelineno-0-44)         if not result.success: [](#__codelineno-0-45)             print("Crawl failed:", result.error_message) [](#__codelineno-0-46)             return [](#__codelineno-0-47) [](#__codelineno-0-48)         # 5. Parse the extracted JSON [](#__codelineno-0-49)         data = json.loads(result.extracted_content) [](#__codelineno-0-50)         print(f"Extracted {len(data)} coin entries") [](#__codelineno-0-51)         print(json.dumps(data[0], indent=2) if data else "No data found") [](#__codelineno-0-52) [](#__codelineno-0-53) asyncio.run(extract_crypto_prices())`

**Highlights**:

*   **`baseSelector`**: Tells us where each “item” (crypto row) is.
*   **`fields`**: Two fields (`coin_name`, `price`) using simple CSS selectors.
*   Each field defines a **`type`** (e.g., `text`, `attribute`, `html`, `regex`, etc.).

No LLM is needed, and the performance is **near-instant** for hundreds or thousands of items.

* * *

### **XPath Example with `raw://` HTML**

Below is a short example demonstrating **XPath** extraction plus the **`raw://`** scheme. We’ll pass a **dummy HTML** directly (no network request) and define the extraction strategy in `CrawlerRunConfig`.

`[](#__codelineno-1-1) import json [](#__codelineno-1-2) import asyncio [](#__codelineno-1-3) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig [](#__codelineno-1-4) from crawl4ai.extraction_strategy import JsonXPathExtractionStrategy [](#__codelineno-1-5) [](#__codelineno-1-6) async def extract_crypto_prices_xpath(): [](#__codelineno-1-7)     # 1. Minimal dummy HTML with some repeating rows [](#__codelineno-1-8)     dummy_html = """ [](#__codelineno-1-9)     <html> [](#__codelineno-1-10)       <body> [](#__codelineno-1-11)         <div class='crypto-row'> [](#__codelineno-1-12)           <h2 class='coin-name'>Bitcoin</h2> [](#__codelineno-1-13)           <span class='coin-price'>$28,000</span> [](#__codelineno-1-14)         </div> [](#__codelineno-1-15)         <div class='crypto-row'> [](#__codelineno-1-16)           <h2 class='coin-name'>Ethereum</h2> [](#__codelineno-1-17)           <span class='coin-price'>$1,800</span> [](#__codelineno-1-18)         </div> [](#__codelineno-1-19)       </body> [](#__codelineno-1-20)     </html> [](#__codelineno-1-21)     """ [](#__codelineno-1-22) [](#__codelineno-1-23)     # 2. Define the JSON schema (XPath version) [](#__codelineno-1-24)     schema = { [](#__codelineno-1-25)         "name": "Crypto Prices via XPath", [](#__codelineno-1-26)         "baseSelector": "//div[@class='crypto-row']", [](#__codelineno-1-27)         "fields": [ [](#__codelineno-1-28)             { [](#__codelineno-1-29)                 "name": "coin_name", [](#__codelineno-1-30)                 "selector": ".//h2[@class='coin-name']", [](#__codelineno-1-31)                 "type": "text" [](#__codelineno-1-32)             }, [](#__codelineno-1-33)             { [](#__codelineno-1-34)                 "name": "price", [](#__codelineno-1-35)                 "selector": ".//span[@class='coin-price']", [](#__codelineno-1-36)                 "type": "text" [](#__codelineno-1-37)             } [](#__codelineno-1-38)         ] [](#__codelineno-1-39)     } [](#__codelineno-1-40) [](#__codelineno-1-41)     # 3. Place the strategy in the CrawlerRunConfig [](#__codelineno-1-42)     config = CrawlerRunConfig( [](#__codelineno-1-43)         extraction_strategy=JsonXPathExtractionStrategy(schema, verbose=True) [](#__codelineno-1-44)     ) [](#__codelineno-1-45) [](#__codelineno-1-46)     # 4. Use raw:// scheme to pass dummy_html directly [](#__codelineno-1-47)     raw_url = f"raw://{dummy_html}" [](#__codelineno-1-48) [](#__codelineno-1-49)     async with AsyncWebCrawler(verbose=True) as crawler: [](#__codelineno-1-50)         result = await crawler.arun( [](#__codelineno-1-51)             url=raw_url, [](#__codelineno-1-52)             config=config [](#__codelineno-1-53)         ) [](#__codelineno-1-54) [](#__codelineno-1-55)         if not result.success: [](#__codelineno-1-56)             print("Crawl failed:", result.error_message) [](#__codelineno-1-57)             return [](#__codelineno-1-58) [](#__codelineno-1-59)         data = json.loads(result.extracted_content) [](#__codelineno-1-60)         print(f"Extracted {len(data)} coin rows") [](#__codelineno-1-61)         if data: [](#__codelineno-1-62)             print("First item:", data[0]) [](#__codelineno-1-63) [](#__codelineno-1-64) asyncio.run(extract_crypto_prices_xpath())`

**Key Points**:

1. **`JsonXPathExtractionStrategy`** is used instead of `JsonCssExtractionStrategy`.  
2. **`baseSelector`** and each field’s `"selector"` use **XPath** instead of CSS.  
3. **`raw://`** lets us pass `dummy_html` with no real network request—handy for local testing.  
4\. Everything (including the extraction strategy) is in **`CrawlerRunConfig`**.

That’s how you keep the config self-contained, illustrate **XPath** usage, and demonstrate the **raw** scheme for direct HTML input—all while avoiding the old approach of passing `extraction_strategy` directly to `arun()`.

* * *

3\. Advanced Schema & Nested Structures
---------------------------------------

Real sites often have **nested** or repeated data—like categories containing products, which themselves have a list of reviews or features. For that, we can define **nested** or **list** (and even **nested\_list**) fields.

### Sample E-Commerce HTML

We have a **sample e-commerce** HTML file on GitHub (example):

`[](#__codelineno-2-1) https://gist.githubusercontent.com/githubusercontent/2d7b8ba3cd8ab6cf3c8da771ddb36878/raw/1ae2f90c6861ce7dd84cc50d3df9920dee5e1fd2/sample_ecommerce.html`

This snippet includes categories, products, features, reviews, and related items. Let’s see how to define a schema that fully captures that structure **without LLM**.

`[](#__codelineno-3-1) schema = { [](#__codelineno-3-2)     "name": "E-commerce Product Catalog", [](#__codelineno-3-3)     "baseSelector": "div.category", [](#__codelineno-3-4)     # (1) We can define optional baseFields if we want to extract attributes  [](#__codelineno-3-5)     # from the category container [](#__codelineno-3-6)     "baseFields": [ [](#__codelineno-3-7)         {"name": "data_cat_id", "type": "attribute", "attribute": "data-cat-id"},  [](#__codelineno-3-8)     ], [](#__codelineno-3-9)     "fields": [ [](#__codelineno-3-10)         { [](#__codelineno-3-11)             "name": "category_name", [](#__codelineno-3-12)             "selector": "h2.category-name", [](#__codelineno-3-13)             "type": "text" [](#__codelineno-3-14)         }, [](#__codelineno-3-15)         { [](#__codelineno-3-16)             "name": "products", [](#__codelineno-3-17)             "selector": "div.product", [](#__codelineno-3-18)             "type": "nested_list",    # repeated sub-objects [](#__codelineno-3-19)             "fields": [ [](#__codelineno-3-20)                 { [](#__codelineno-3-21)                     "name": "name", [](#__codelineno-3-22)                     "selector": "h3.product-name", [](#__codelineno-3-23)                     "type": "text" [](#__codelineno-3-24)                 }, [](#__codelineno-3-25)                 { [](#__codelineno-3-26)                     "name": "price", [](#__codelineno-3-27)                     "selector": "p.product-price", [](#__codelineno-3-28)                     "type": "text" [](#__codelineno-3-29)                 }, [](#__codelineno-3-30)                 { [](#__codelineno-3-31)                     "name": "details", [](#__codelineno-3-32)                     "selector": "div.product-details", [](#__codelineno-3-33)                     "type": "nested",  # single sub-object [](#__codelineno-3-34)                     "fields": [ [](#__codelineno-3-35)                         { [](#__codelineno-3-36)                             "name": "brand", [](#__codelineno-3-37)                             "selector": "span.brand", [](#__codelineno-3-38)                             "type": "text" [](#__codelineno-3-39)                         }, [](#__codelineno-3-40)                         { [](#__codelineno-3-41)                             "name": "model", [](#__codelineno-3-42)                             "selector": "span.model", [](#__codelineno-3-43)                             "type": "text" [](#__codelineno-3-44)                         } [](#__codelineno-3-45)                     ] [](#__codelineno-3-46)                 }, [](#__codelineno-3-47)                 { [](#__codelineno-3-48)                     "name": "features", [](#__codelineno-3-49)                     "selector": "ul.product-features li", [](#__codelineno-3-50)                     "type": "list", [](#__codelineno-3-51)                     "fields": [ [](#__codelineno-3-52)                         {"name": "feature", "type": "text"}  [](#__codelineno-3-53)                     ] [](#__codelineno-3-54)                 }, [](#__codelineno-3-55)                 { [](#__codelineno-3-56)                     "name": "reviews", [](#__codelineno-3-57)                     "selector": "div.review", [](#__codelineno-3-58)                     "type": "nested_list", [](#__codelineno-3-59)                     "fields": [ [](#__codelineno-3-60)                         { [](#__codelineno-3-61)                             "name": "reviewer",  [](#__codelineno-3-62)                             "selector": "span.reviewer",  [](#__codelineno-3-63)                             "type": "text" [](#__codelineno-3-64)                         }, [](#__codelineno-3-65)                         { [](#__codelineno-3-66)                             "name": "rating",  [](#__codelineno-3-67)                             "selector": "span.rating",  [](#__codelineno-3-68)                             "type": "text" [](#__codelineno-3-69)                         }, [](#__codelineno-3-70)                         { [](#__codelineno-3-71)                             "name": "comment",  [](#__codelineno-3-72)                             "selector": "p.review-text",  [](#__codelineno-3-73)                             "type": "text" [](#__codelineno-3-74)                         } [](#__codelineno-3-75)                     ] [](#__codelineno-3-76)                 }, [](#__codelineno-3-77)                 { [](#__codelineno-3-78)                     "name": "related_products", [](#__codelineno-3-79)                     "selector": "ul.related-products li", [](#__codelineno-3-80)                     "type": "list", [](#__codelineno-3-81)                     "fields": [ [](#__codelineno-3-82)                         { [](#__codelineno-3-83)                             "name": "name",  [](#__codelineno-3-84)                             "selector": "span.related-name",  [](#__codelineno-3-85)                             "type": "text" [](#__codelineno-3-86)                         }, [](#__codelineno-3-87)                         { [](#__codelineno-3-88)                             "name": "price",  [](#__codelineno-3-89)                             "selector": "span.related-price",  [](#__codelineno-3-90)                             "type": "text" [](#__codelineno-3-91)                         } [](#__codelineno-3-92)                     ] [](#__codelineno-3-93)                 } [](#__codelineno-3-94)             ] [](#__codelineno-3-95)         } [](#__codelineno-3-96)     ] [](#__codelineno-3-97) }`

Key Takeaways:

*   **Nested vs. List**:
*   **`type: "nested"`** means a **single** sub-object (like `details`).
*   **`type: "list"`** means multiple items that are **simple** dictionaries or single text fields.
*   **`type: "nested_list"`** means repeated **complex** objects (like `products` or `reviews`).
*   **Base Fields**: We can extract **attributes** from the container element via `"baseFields"`. For instance, `"data_cat_id"` might be `data-cat-id="elect123"`.
*   **Transforms**: We can also define a `transform` if we want to lower/upper case, strip whitespace, or even run a custom function.

### Running the Extraction

`[](#__codelineno-4-1) import json [](#__codelineno-4-2) import asyncio [](#__codelineno-4-3) from crawl4ai import AsyncWebCrawler, CrawlerRunConfig [](#__codelineno-4-4) from crawl4ai.extraction_strategy import JsonCssExtractionStrategy [](#__codelineno-4-5) [](#__codelineno-4-6) ecommerce_schema = { [](#__codelineno-4-7)     # ... the advanced schema from above ... [](#__codelineno-4-8) } [](#__codelineno-4-9) [](#__codelineno-4-10) async def extract_ecommerce_data(): [](#__codelineno-4-11)     strategy = JsonCssExtractionStrategy(ecommerce_schema, verbose=True) [](#__codelineno-4-12) [](#__codelineno-4-13)     config = CrawlerRunConfig() [](#__codelineno-4-14) [](#__codelineno-4-15)     async with AsyncWebCrawler(verbose=True) as crawler: [](#__codelineno-4-16)         result = await crawler.arun( [](#__codelineno-4-17)             url="https://gist.githubusercontent.com/githubusercontent/2d7b8ba3cd8ab6cf3c8da771ddb36878/raw/1ae2f90c6861ce7dd84cc50d3df9920dee5e1fd2/sample_ecommerce.html", [](#__codelineno-4-18)             extraction_strategy=strategy, [](#__codelineno-4-19)             config=config [](#__codelineno-4-20)         ) [](#__codelineno-4-21) [](#__codelineno-4-22)         if not result.success: [](#__codelineno-4-23)             print("Crawl failed:", result.error_message) [](#__codelineno-4-24)             return [](#__codelineno-4-25) [](#__codelineno-4-26)         # Parse the JSON output [](#__codelineno-4-27)         data = json.loads(result.extracted_content) [](#__codelineno-4-28)         print(json.dumps(data, indent=2) if data else "No data found.") [](#__codelineno-4-29) [](#__codelineno-4-30) asyncio.run(extract_ecommerce_data())`

If all goes well, you get a **structured** JSON array with each “category,” containing an array of `products`. Each product includes `details`, `features`, `reviews`, etc. All of that **without** an LLM.

* * *

4\. Why “No LLM” Is Often Better
--------------------------------

1. **Zero Hallucination**: Schema-based extraction doesn’t guess text. It either finds it or not.  
2. **Guaranteed Structure**: The same schema yields consistent JSON across many pages, so your downstream pipeline can rely on stable keys.  
3. **Speed**: LLM-based extraction can be 10–1000x slower for large-scale crawling.  
4. **Scalable**: Adding or updating a field is a matter of adjusting the schema, not re-tuning a model.

**When might you consider an LLM?** Possibly if the site is extremely unstructured or you want AI summarization. But always try a schema approach first for repeated or consistent data patterns.

* * *

5\. Base Element Attributes & Additional Fields
-----------------------------------------------

It’s easy to **extract attributes** (like `href`, `src`, or `data-xxx`) from your base or nested elements using:

`[](#__codelineno-5-1) { [](#__codelineno-5-2)   "name": "href", [](#__codelineno-5-3)   "type": "attribute", [](#__codelineno-5-4)   "attribute": "href", [](#__codelineno-5-5)   "default": null [](#__codelineno-5-6) }`

You can define them in **`baseFields`** (extracted from the main container element) or in each field’s sub-lists. This is especially helpful if you need an item’s link or ID stored in the parent `<div>`.

* * *

6\. Putting It All Together: Larger Example
-------------------------------------------

Consider a blog site. We have a schema that extracts the **URL** from each post card (via `baseFields` with an `"attribute": "href"`), plus the title, date, summary, and author:

`[](#__codelineno-6-1) schema = { [](#__codelineno-6-2)   "name": "Blog Posts", [](#__codelineno-6-3)   "baseSelector": "a.blog-post-card", [](#__codelineno-6-4)   "baseFields": [ [](#__codelineno-6-5)     {"name": "post_url", "type": "attribute", "attribute": "href"} [](#__codelineno-6-6)   ], [](#__codelineno-6-7)   "fields": [ [](#__codelineno-6-8)     {"name": "title", "selector": "h2.post-title", "type": "text", "default": "No Title"}, [](#__codelineno-6-9)     {"name": "date", "selector": "time.post-date", "type": "text", "default": ""}, [](#__codelineno-6-10)     {"name": "summary", "selector": "p.post-summary", "type": "text", "default": ""}, [](#__codelineno-6-11)     {"name": "author", "selector": "span.post-author", "type": "text", "default": ""} [](#__codelineno-6-12)   ] [](#__codelineno-6-13) }`

Then run with `JsonCssExtractionStrategy(schema)` to get an array of blog post objects, each with `"post_url"`, `"title"`, `"date"`, `"summary"`, `"author"`.

* * *

7\. Tips & Best Practices
-------------------------

1. **Inspect the DOM** in Chrome DevTools or Firefox’s Inspector to find stable selectors.  
2. **Start Simple**: Verify you can extract a single field. Then add complexity like nested objects or lists.  
3. **Test** your schema on partial HTML or a test page before a big crawl.  
4. **Combine with JS Execution** if the site loads content dynamically. You can pass `js_code` or `wait_for` in `CrawlerRunConfig`.  
5. **Look at Logs** when `verbose=True`: if your selectors are off or your schema is malformed, it’ll often show warnings.  
6. **Use baseFields** if you need attributes from the container element (e.g., `href`, `data-id`), especially for the “parent” item.  
7. **Performance**: For large pages, make sure your selectors are as narrow as possible.

* * *

8\. Schema Generation Utility
-----------------------------

While manually crafting schemas is powerful and precise, Crawl4AI now offers a convenient utility to **automatically generate** extraction schemas using LLM. This is particularly useful when:

1.  You're dealing with a new website structure and want a quick starting point
2.  You need to extract complex nested data structures
3.  You want to avoid the learning curve of CSS/XPath selector syntax

### Using the Schema Generator

The schema generator is available as a static method on both `JsonCssExtractionStrategy` and `JsonXPathExtractionStrategy`. You can choose between OpenAI's GPT-4 or the open-source Ollama for schema generation:

`[](#__codelineno-7-1) from crawl4ai.extraction_strategy import JsonCssExtractionStrategy, JsonXPathExtractionStrategy [](#__codelineno-7-2) from crawl4ai import LLMConfig [](#__codelineno-7-3) [](#__codelineno-7-4) # Sample HTML with product information [](#__codelineno-7-5) html = """ [](#__codelineno-7-6) <div class="product-card"> [](#__codelineno-7-7)     <h2 class="title">Gaming Laptop</h2> [](#__codelineno-7-8)     <div class="price">$999.99</div> [](#__codelineno-7-9)     <div class="specs"> [](#__codelineno-7-10)         <ul> [](#__codelineno-7-11)             <li>16GB RAM</li> [](#__codelineno-7-12)             <li>1TB SSD</li> [](#__codelineno-7-13)         </ul> [](#__codelineno-7-14)     </div> [](#__codelineno-7-15) </div> [](#__codelineno-7-16) """ [](#__codelineno-7-17) [](#__codelineno-7-18) # Option 1: Using OpenAI (requires API token) [](#__codelineno-7-19) css_schema = JsonCssExtractionStrategy.generate_schema( [](#__codelineno-7-20)     html, [](#__codelineno-7-21)     schema_type="css",  [](#__codelineno-7-22)     llm_config = LLMConfig(provider="openai/gpt-4o",api_token="your-openai-token") [](#__codelineno-7-23) ) [](#__codelineno-7-24) [](#__codelineno-7-25) # Option 2: Using Ollama (open source, no token needed) [](#__codelineno-7-26) xpath_schema = JsonXPathExtractionStrategy.generate_schema( [](#__codelineno-7-27)     html, [](#__codelineno-7-28)     schema_type="xpath", [](#__codelineno-7-29)     llm_config = LLMConfig(provider="ollama/llama3.3", api_token=None)  # Not needed for Ollama [](#__codelineno-7-30) ) [](#__codelineno-7-31) [](#__codelineno-7-32) # Use the generated schema for fast, repeated extractions [](#__codelineno-7-33) strategy = JsonCssExtractionStrategy(css_schema)`

### LLM Provider Options

1.  **OpenAI GPT-4 (`openai/gpt4o`)**
2.  Default provider
3.  Requires an API token
4.  Generally provides more accurate schemas
5.  Set via environment variable: `OPENAI_API_KEY`
    
6.  **Ollama (`ollama/llama3.3`)**
    
7.  Open source alternative
8.  No API token required
9.  Self-hosted option
10.  Good for development and testing

### Benefits of Schema Generation

1.  **One-Time Cost**: While schema generation uses LLM, it's a one-time cost. The generated schema can be reused for unlimited extractions without further LLM calls.
2.  **Smart Pattern Recognition**: The LLM analyzes the HTML structure and identifies common patterns, often producing more robust selectors than manual attempts.
3.  **Automatic Nesting**: Complex nested structures are automatically detected and properly represented in the schema.
4.  **Learning Tool**: The generated schemas serve as excellent examples for learning how to write your own schemas.

### Best Practices

1.  **Review Generated Schemas**: While the generator is smart, always review and test the generated schema before using it in production.
2.  **Provide Representative HTML**: The better your sample HTML represents the overall structure, the more accurate the generated schema will be.
3.  **Consider Both CSS and XPath**: Try both schema types and choose the one that works best for your specific case.
4.  **Cache Generated Schemas**: Since generation uses LLM, save successful schemas for reuse.
5.  **API Token Security**: Never hardcode API tokens. Use environment variables or secure configuration management.
6.  **Choose Provider Wisely**:
7.  Use OpenAI for production-quality schemas
8.  Use Ollama for development, testing, or when you need a self-hosted solution

That's it for **Extracting JSON (No LLM)**! You've seen how schema-based approaches (either CSS or XPath) can handle everything from simple lists to deeply nested product catalogs—instantly, with minimal overhead. Enjoy building robust scrapers that produce consistent, structured JSON for your data pipelines!

* * *

9\. Conclusion
--------------

With **JsonCssExtractionStrategy** (or **JsonXPathExtractionStrategy**), you can build powerful, **LLM-free** pipelines that:

*   Scrape any consistent site for structured data.
*   Support nested objects, repeating lists, or advanced transformations.
*   Scale to thousands of pages quickly and reliably.

**Next Steps**:

*   Combine your extracted JSON with advanced filtering or summarization in a second pass if needed.
*   For dynamic pages, combine strategies with `js_code` or infinite scroll hooking to ensure all content is loaded.

**Remember**: For repeated, structured data, you don’t need to pay for or wait on an LLM. A well-crafted schema plus CSS or XPath gets you the data faster, cleaner, and cheaper—**the real power** of Crawl4AI.

**Last Updated**: 2025-01-01

* * *

That’s it for **Extracting JSON (No LLM)**! You’ve seen how schema-based approaches (either CSS or XPath) can handle everything from simple lists to deeply nested product catalogs—instantly, with minimal overhead. Enjoy building robust scrapers that produce consistent, structured JSON for your data pipelines!

* * *

---

