import functools
import logging

logger = logging.getLogger(__name__)


def requires_crawler_initialized(func):
    @functools.wraps(func)
    async def wrapper(self, *args, **kwargs):
        if not self.crawler:
            raise Exception("Crawler not initialized")
        return await func(self, *args, **kwargs)

    return wrapper


def requires_cookies_accepted(func):
    @functools.wraps(func)
    async def wrapper(self, *args, **kwargs):
        if not self.accepted_cookies:
            await self._accept_cookies(self.current_url or self.website_config.base_url)
            self.accepted_cookies = True
        return await func(self, *args, **kwargs)

    return wrapper


def requires_login_config(func):
    @functools.wraps(func)
    async def wrapper(self, *args, **kwargs):
        if not self.login_config:
            raise Exception("Login config not initialized")
        return await func(self, *args, **kwargs)

    return wrapper
