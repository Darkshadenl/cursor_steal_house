from typing import Dict, List, Optional, Any, Tuple
import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import and_, select

from crawler_job.models.db_config_models import (
    DbWebsite,
    DbLoginConfig,
    DbNavigationConfig,
    DbExtractionConfig,
    DbFieldMapping,
    WebsiteConfig,
    WebsiteInfo,
    LoginConfig,
    NavigationConfig,
    ExtractionConfig,
    FieldMapping,
)


class WebsiteConfigRepository:
    """
    Repository for loading website configurations from the database.
    """

    def __init__(self, db_session: AsyncSession):
        """
        Initialize WebsiteConfigRepository with a database session.

        Args:
            db_session: SQLAlchemy session for database access
        """
        self.db_session = db_session
        self.logger = logging.getLogger(__name__)

    async def get_config_async(self, website_id: int) -> WebsiteConfig:
        """
        Load the complete configuration for a website by its ID.

        Args:
            website_id: ID of the website to load configuration for

        Returns:
            WebsiteConfig: Complete website configuration

        Raises:
            ValueError: If website with given ID doesn't exist
        """
        try:
            # Load website information
            db_website = (
                self.db_session.query(DbWebsite)
                .filter(DbWebsite.id == website_id)
                .first()
            )
            if not db_website:
                raise ValueError(f"Website with ID {website_id} not found")

            # Load login config
            db_login_config = (
                self.db_session.query(DbLoginConfig)
                .filter(DbLoginConfig.website_id == website_id)
                .first()
            )

            # Load navigation config
            db_navigation_config = (
                self.db_session.query(DbNavigationConfig)
                .filter(DbNavigationConfig.website_id == website_id)
                .first()
            )

            # Load extraction configs and their field mappings
            db_extraction_configs = (
                self.db_session.query(DbExtractionConfig)
                .filter(DbExtractionConfig.website_id == website_id)
                .all()
            )

            # Map to Pydantic models
            website_info = WebsiteInfo(
                id=db_website.id,
                name=db_website.name,
                base_url=db_website.base_url,
                is_active=db_website.is_active,
                description=db_website.description,
            )

            login_config = None
            if db_login_config:
                login_config = LoginConfig(
                    id=db_login_config.id,
                    website_id=db_login_config.website_id,
                    login_url_path=db_login_config.login_url_path,
                    username_selector=db_login_config.username_selector,
                    password_selector=db_login_config.password_selector,
                    submit_selector=db_login_config.submit_selector,
                    success_indicator_selector=db_login_config.success_indicator_selector,
                    needs_login=db_login_config.needs_login,
                    credential_source=db_login_config.credential_source,
                )

            navigation_config = None
            if db_navigation_config:
                navigation_config = NavigationConfig(
                    id=db_navigation_config.id,
                    website_id=db_navigation_config.website_id,
                    gallery_url_path=db_navigation_config.gallery_url_path,
                    steps=db_navigation_config.steps,
                    next_page_selector=db_navigation_config.next_page_selector,
                )

            gallery_extraction_config = None
            detail_extraction_config = None

            for db_extraction_config in db_extraction_configs:
                # Get all field mappings for this extraction config
                db_field_mappings = (
                    self.db_session.query(DbFieldMapping)
                    .filter(
                        DbFieldMapping.extraction_config_id == db_extraction_config.id
                    )
                    .all()
                )

                # Convert field mappings to Pydantic models
                field_mappings = []
                for db_field_mapping in db_field_mappings:
                    field_mappings.append(
                        FieldMapping(
                            id=db_field_mapping.id,
                            extraction_config_id=db_field_mapping.extraction_config_id,
                            pydantic_field_name=db_field_mapping.pydantic_field_name,
                            selector=db_field_mapping.selector,
                            selector_type=db_field_mapping.selector_type,
                            extraction_type=db_field_mapping.extraction_type,
                            attribute_name=db_field_mapping.attribute_name,
                            is_required=db_field_mapping.is_required,
                            default_value=db_field_mapping.default_value,
                        )
                    )

                # Convert extraction config to Pydantic model
                extraction_config = ExtractionConfig(
                    id=db_extraction_config.id,
                    website_id=db_extraction_config.website_id,
                    scope=db_extraction_config.scope,
                    extraction_method=db_extraction_config.extraction_method,
                    llm_provider=db_extraction_config.llm_provider,
                    llm_instruction=db_extraction_config.llm_instruction,
                    base_selector=db_extraction_config.base_selector,
                    field_mappings=field_mappings,
                )

                # Assign to the appropriate config based on scope
                if db_extraction_config.scope == "gallery":
                    gallery_extraction_config = extraction_config
                elif db_extraction_config.scope == "detail":
                    detail_extraction_config = extraction_config

            # Create complete WebsiteConfig
            return WebsiteConfig(
                website_info=website_info,
                login_config=login_config,
                navigation_config=navigation_config,
                gallery_extraction_config=gallery_extraction_config,
                detail_extraction_config=detail_extraction_config,
            )

        except SQLAlchemyError as e:
            self.logger.error(f"Database error while loading website config: {str(e)}")
            raise
        except Exception as e:
            self.logger.error(f"Error while loading website config: {str(e)}")
            raise

    async def get_website_id_by_name_async(self, website_name: str) -> int:
        """
        Get the ID of a website by its name.

        Args:
            website_name: Name of the website

        Returns:
            int: Website ID

        Raises:
            ValueError: If website with given name doesn't exist
        """
        try:
            stmt = select(DbWebsite).where(DbWebsite.name == website_name)
            result = await self.db_session.execute(stmt)
            website = result.scalars().first()

            if not website:
                raise ValueError(f"Website with name '{website_name}' not found")

            return website.id 

        except SQLAlchemyError as e:
            self.logger.error(f"Database error while getting website ID: {str(e)}")
            raise
        except Exception as e:
            self.logger.error(f"Error while getting website ID: {str(e)}")
            raise

    # Synchronous versions of the methods (for backward compatibility)

    def get_config(self, website_id: int) -> WebsiteConfig:
        """
        Synchronous version of get_config_async.
        """
        # Reuse async code since they share the same core logic
        import asyncio

        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(self.get_config_async(website_id))
        finally:
            loop.close()

    def get_website_id_by_name(self, website_name: str) -> int:
        """
        Synchronous version of get_website_id_by_name_async.
        """
        import asyncio

        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(
                self.get_website_id_by_name_async(website_name)
            )
        finally:
            loop.close()


__all__ = ["WebsiteConfigRepository"]
