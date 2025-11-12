from typing import Optional, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from crawler_job.models.db_models import DbWebsite, DbWebsiteScrapeConfig
from crawler_job.services.logger_service import setup_logger

from ...models.pydantic_models import (
    WebsiteConfig,
    WebsiteScrapeConfigJson,
)


logger = setup_logger(__name__)


class JsonConfigRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_config_by_website_name_async(
        self, website_name: str
    ) -> Optional[WebsiteScrapeConfigJson]:
        return await self._get_config_async(website_name=website_name)

    async def _get_config_async(
        self, website_name: Optional[str] = None
    ) -> Optional[WebsiteScrapeConfigJson]:
        if website_name is None:
            logger.error("Website name must be provided")
            return None

        try:
            website_query = select(DbWebsite).where(
                DbWebsite.name == website_name, DbWebsite.is_active
            )
            website_result = await self.session.execute(website_query)
            website = website_result.scalar_one_or_none()

            if not website:
                logger.error(f"Website with name '{website_name}' not found")
                return None

            query = select(DbWebsiteScrapeConfig).where(
                DbWebsiteScrapeConfig.website_identifier == website.id
            )
            result = await self.session.execute(query)
            config_record = result.scalar_one_or_none()

            if not config_record:
                print(f"No enabled configuration found for website '{website_name}'")
                return None

            website_info = WebsiteConfig(
                id=website.id,  # type: ignore
                name=str(website.name),
                base_url=str(website.base_url),
                is_active=bool(website.is_active),
            )

            try:
                config_data: Dict[str, Any] = config_record.config_json  # type: ignore

                if "website_info" not in config_data:
                    config_data["website_info"] = website_info.model_dump()  # type: ignore

                return WebsiteScrapeConfigJson.model_validate(config_data)
            except Exception as e:
                logger.error(
                    f"Error parsing configuration for '{website_name}': {str(e)}"
                )
                return None

        except Exception as e:
            logger.error(
                f"Database error while retrieving configuration for '{website_name}': {str(e)}"
            )
            return None
