from typing import Optional, Union, Tuple
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from ...models.db_config_models import (
    DbWebsiteScrapeConfig,
    WebsiteConfig,
    WebsiteInfo,
    DbWebsite,
)


class JsonConfigRepository:
    """Repository for managing website scraping configurations in JSON format."""

    def __init__(self, session: AsyncSession):
        """Initialize the repository with a database session.

        Args:
            session: The SQLAlchemy async session to use for database operations.
        """
        self.session = session

    async def get_config_by_website_id_async(
        self, website_id: int
    ) -> Optional[WebsiteConfig]:
        """Retrieve and parse the configuration for a given website identifier.

        Args:
            website_id: The unique identifier of the website.

        Returns:
            Optional[WebsiteConfig]: The parsed configuration if found and valid, None otherwise.
        """
        return await self._get_config_async(website_id=website_id)

    async def get_config_by_website_name_async(
        self, website_name: str
    ) -> Optional[WebsiteConfig]:
        """Retrieve and parse the configuration for a given website name.

        Args:
            website_name: The name of the website.

        Returns:
            Optional[WebsiteConfig]: The parsed configuration if found and valid, None otherwise.
        """
        return await self._get_config_async(website_name=website_name)

    async def _get_config_async(
        self, website_id: Optional[int] = None, website_name: Optional[str] = None
    ) -> Optional[WebsiteConfig]:
        """Internal method to retrieve and parse configuration for a website by ID or name.

        Args:
            website_id: The unique identifier of the website.
            website_name: The name of the website.

        Returns:
            Optional[WebsiteConfig]: The parsed configuration if found and valid, None otherwise.
        """
        if website_id is None and website_name is None:
            print("Either website_id or website_name must be provided")
            return None

        try:
            # First, get the website by ID or name
            if website_id is not None:
                website_query = select(DbWebsite).where(DbWebsite.id == website_id)
                identifier = website_id
            else:
                website_query = select(DbWebsite).where(DbWebsite.name == website_name)
                identifier = website_name

            website_result = await self.session.execute(website_query)
            website = website_result.scalar_one_or_none()

            if not website:
                print(
                    f"Website with {'ID' if website_id else 'name'} '{identifier}' not found"
                )
                return None

            # Query the database for the configuration
            query = select(DbWebsiteScrapeConfig).where(
                DbWebsiteScrapeConfig.website_identifier == website.id,
                DbWebsiteScrapeConfig.is_enabled == True,
            )
            result = await self.session.execute(query)
            config_record = result.scalar_one_or_none()

            if not config_record:
                print(
                    f"No enabled configuration found for website {'ID' if website_id else 'name'} '{identifier}'"
                )
                return None

            # Create the website_info object
            website_info = WebsiteInfo(
                id=website.id,  # type: ignore
                name=str(website.name),
                base_url=str(website.base_url),
                is_active=bool(website.is_active),
                description=getattr(website, "description", None),
            )

            try:
                config_data = config_record.config_json
                if "website_info" not in config_data:
                    config_data["website_info"] = website_info.model_dump()  # type: ignore

                return WebsiteConfig.model_validate(config_data)
            except Exception as e:
                print(f"Error parsing configuration for '{identifier}': {str(e)}")
                return None

        except Exception as e:
            print(
                f"Database error while retrieving configuration for '{website_id or website_name}': {str(e)}"
            )
            return None
