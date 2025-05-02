from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from ...models.db_config_models import WebsiteConfig, WebsiteInfo, DbWebsite
from ...models.db_models import DbWebsiteScrapeConfig
from sqlalchemy.orm import joinedload


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
            identifier: The unique identifier of the website.

        Returns:
            Optional[WebsiteConfig]: The parsed configuration if found and valid, None otherwise.
        """
        try:
            # Query the database for the configuration
            query = select(DbWebsiteScrapeConfig).where(
                DbWebsiteScrapeConfig.website_identifier == website_id,
                DbWebsiteScrapeConfig.is_enabled == True,
            )
            result = await self.session.execute(query)
            config_record = result.scalar_one_or_none()

            if not config_record:
                print(
                    f"No enabled configuration found for website identifier '{website_id}'"
                )
                return None

            # Get the website info
            website_query = select(DbWebsite).where(DbWebsite.id == website_id)
            website_result = await self.session.execute(website_query)
            website = website_result.scalar_one_or_none()

            if not website:
                print(f"Website with ID {website_id} not found")
                return None

            # Create the website_info object
            website_info = WebsiteInfo(
                id=website.id,
                name=website.name,
                base_url=website.base_url,
                is_active=website.is_active,
                description=getattr(website, "description", None),
            )

            # Parse and validate the JSON configuration
            try:
                # Add website_info to the config if not already present
                config_data = config_record.config_json
                if "website_info" not in config_data:
                    config_data["website_info"] = website_info.model_dump()

                return WebsiteConfig.model_validate(config_data)
            except Exception as e:
                print(f"Error parsing configuration for '{website_id}': {str(e)}")
                return None

        except Exception as e:
            print(
                f"Database error while retrieving configuration for '{website_id}': {str(e)}"
            )
            return None

    async def get_config_by_identifier_async(
        self, identifier: int
    ) -> Optional[WebsiteConfig]:
        """Retrieve and parse the configuration for a given website identifier.

        Args:
            identifier: The unique identifier of the website.

        Returns:
            Optional[WebsiteConfig]: The parsed configuration if found and valid, None otherwise.
        """
        try:
            # Query the database for the configuration
            query = select(DbWebsiteScrapeConfig).where(
                DbWebsiteScrapeConfig.website_identifier == identifier,
                DbWebsiteScrapeConfig.is_enabled == True,
            )
            result = await self.session.execute(query)
            config_record = result.scalar_one_or_none()

            if not config_record:
                print(
                    f"No enabled configuration found for website identifier '{identifier}'"
                )
                return None

            # Get the website info
            website_query = select(DbWebsite).where(DbWebsite.id == identifier)
            website_result = await self.session.execute(website_query)
            website = website_result.scalar_one_or_none()

            if not website:
                print(f"Website with ID {identifier} not found")
                return None

            # Create the website_info object
            website_info = WebsiteInfo(
                id=website.id,
                name=website.name,
                base_url=website.base_url,
                is_active=website.is_active,
                description=getattr(website, "description", None),
            )

            # Parse and validate the JSON configuration
            try:
                # Add website_info to the config if not already present
                config_data = config_record.config_json
                if "website_info" not in config_data:
                    config_data["website_info"] = website_info.model_dump()

                return WebsiteConfig.model_validate(config_data)
            except Exception as e:
                print(f"Error parsing configuration for '{identifier}': {str(e)}")
                return None

        except Exception as e:
            print(
                f"Database error while retrieving configuration for '{identifier}': {str(e)}"
            )
            return None

    async def save_config_async(self, config: WebsiteConfig) -> bool:
        """Save a new or update an existing website configuration.

        Args:
            config: The WebsiteConfig to save.

        Returns:
            bool: True if the save was successful, False otherwise.
        """
        try:
            website_id = config.website_info.id

            # Check if a configuration already exists
            query = select(DbWebsiteScrapeConfig).where(
                DbWebsiteScrapeConfig.website_identifier == website_id
            )
            result = await self.session.execute(query)
            existing_config = result.scalar_one_or_none()

            if existing_config:
                # Update existing configuration
                existing_config.config_json = config.model_dump()
                existing_config.version = (
                    existing_config.version + 1 if existing_config.version else 1
                )
            else:
                # Create new configuration
                new_config = DbWebsiteScrapeConfig(
                    website_identifier=website_id,
                    config_json=config.model_dump(),
                    version=1,
                )
                self.session.add(new_config)

            await self.session.commit()
            return True

        except Exception as e:
            print(f"Error saving configuration for website ID '{website_id}': {str(e)}")
            await self.session.rollback()
            return False
