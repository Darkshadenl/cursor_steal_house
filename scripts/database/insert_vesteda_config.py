import asyncio
import logging
import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

# Make sure project root is in path to import models and services
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from crawler_job.services.db_connection import get_db_context, engine
from crawler_job.models.db_config_models import (
    DbWebsite,
    DbLoginConfig,
    DbNavigationConfig,
    DbExtractionConfig,
    DbFieldMapping,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Old flexible method.
async def insert_vesteda_config_async():
    """Inserts the default configuration for the Vesteda website if it doesn't exist."""
    # Use the async context manager to handle session creation and closing
    async with get_db_context() as session:
        try:
            # Check if Vesteda website already exists
            stmt = select(DbWebsite).where(DbWebsite.name == "Vesteda")
            result = await session.execute(stmt)
            existing_website = result.scalars().first()

            if existing_website:
                logger.info("Vesteda configuration already exists. Skipping insertion.")
                return

            logger.info("Inserting Vesteda configuration...")

            # 1. Create Website entry
            website = DbWebsite(
                name="Vesteda",
                base_url="https://hurenbij.vesteda.com",
                is_active=True,
            )
            session.add(website)
            await session.flush()  # Flush to get website.id

            # 2. Create Login Config
            login_config = DbLoginConfig(
                website_id=website.id,
                needs_login=True,
                login_url_path="/login",
                username_selector='input[type="email"]',
                password_selector='input[type="password"]',
                submit_selector='button[type="submit"]',
                success_check_url="/",  # Check if landing on base URL path
                credential_source="env:VESTEDA_EMAIL",
            )
            session.add(login_config)

            # 3. Create Navigation Config
            navigation_config = DbNavigationConfig(
                website_id=website.id, gallery_url_path="/zoekopdracht/", steps=None
            )
            session.add(navigation_config)

            # 4. Create Gallery Extraction Config
            gallery_extraction = DbExtractionConfig(
                website_id=website.id,
                extraction_method="css",
                base_selector="div.card.card-result-list",
            )
            session.add(gallery_extraction)
            await session.flush()  # Flush to get gallery_extraction.id

            # 5. Create Field Mappings for Gallery
            gallery_mappings_data = [
                {
                    "pydantic_field_name": "address",
                    "selector": "h5.card-title a",
                    "extraction_type": "text",
                },
                {
                    "pydantic_field_name": "city",
                    "selector": "div.card-text",
                    "extraction_type": "text",
                },
                {
                    "pydantic_field_name": "rental_price",
                    "selector": "div.object-price span.value",
                    "extraction_type": "text",
                },
                {
                    "pydantic_field_name": "bedrooms",
                    "selector": "div.object-rooms span.value",
                    "extraction_type": "text",
                },
                {
                    "pydantic_field_name": "square_meters",
                    "selector": "div.object-area span.value",
                    "extraction_type": "text",
                },
                {
                    "pydantic_field_name": "status",
                    "selector": "div.card-image-label span",
                    "extraction_type": "text",
                },
                {
                    "pydantic_field_name": "detail_url",
                    "selector": "h5.card-title a",
                    "extraction_type": "attribute",
                    "attribute_name": "href",
                },
            ]

            for mapping_data in gallery_mappings_data:
                mapping = DbFieldMapping(
                    extraction_config_id=gallery_extraction.id, **mapping_data
                )
                session.add(mapping)

            # 6. Create Detail Extraction Config
            detail_extraction = DbExtractionConfig(
                website_id=website.id,
                scope="detail",
                extraction_method="llm",
                llm_provider="GEMINI",  # Or LLMProvider.GEMINI.value if it's an Enum
                # No explicit llm_instruction needed as per current scraper logic
            )
            session.add(detail_extraction)

            await session.commit()
            logger.info("Successfully inserted Vesteda configuration.")

        except Exception as e:
            await session.rollback()
            logger.error(f"Error inserting Vesteda configuration: {e}")
            raise
        # No finally needed as context manager handles session closing


async def main():
    load_dotenv("../../.env")
    # # Ensure database URL is set in environment -- Removed Check as connection is built from POSTGRES_* vars
    # db_url = os.getenv("DATABASE_URL")
    # if not db_url:
    #     logger.error(
    #         "DATABASE_URL environment variable not set. Please configure it in your .env file."
    #     )
    #     return

    await insert_vesteda_config_async()
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
