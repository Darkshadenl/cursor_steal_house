#!/usr/bin/env python
"""
Script to insert Vesteda website configuration into the database.
Run this script after applying the database migrations.
"""
import asyncio
import os
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Database connection URL from environment variable
DB_URL = os.getenv("DATABASE_URL")
if not DB_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

# Convert to async URL if needed
if not DB_URL.startswith("postgresql+asyncpg://"):
    DB_URL = DB_URL.replace("postgresql://", "postgresql+asyncpg://")

# Create async engine and session
engine = create_async_engine(DB_URL)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def insert_vesteda_config():
    """Insert Vesteda website configuration into the database"""
    async with async_session() as session:
        async with session.begin():
            # Check if Vesteda already exists
            query = text("SELECT id FROM steal_house.websites WHERE name = 'Vesteda'")
            result = await session.execute(query)
            existing_id = result.scalar()

            if existing_id:
                logger.info(
                    f"Vesteda website configuration already exists with ID {existing_id}"
                )
                return existing_id

            # 1. Insert website
            logger.info("Inserting Vesteda website configuration")
            insert_website = text(
                """
                INSERT INTO steal_house.websites (name, base_url, is_active, description)
                VALUES ('Vesteda', 'https://hurenbij.vesteda.com', TRUE, 'Vesteda real estate website')
                RETURNING id
            """
            )
            result = await session.execute(insert_website)
            website_id = result.scalar()
            logger.info(f"Inserted Vesteda website with ID {website_id}")

            # 2. Insert login config
            logger.info("Inserting Vesteda login configuration")
            insert_login = text(
                """
                INSERT INTO steal_house.login_configs (
                    website_id, login_url_path, username_selector, password_selector, 
                    submit_selector, success_indicator_selector, needs_login, credential_source
                )
                VALUES (
                    :website_id, '/login', 'input[type="email"]', 'input[type="password"]',
                    'button[type="submit"]', '.profile-menu', TRUE, 'env:VESTEDA_EMAIL'
                )
            """
            )
            await session.execute(insert_login, {"website_id": website_id})

            # 3. Insert navigation config
            logger.info("Inserting Vesteda navigation configuration")
            # Navigation steps JSON
            nav_steps = [
                {"action": "click", "selector": "a[href='/aanbod']"},
                {"action": "wait", "selector": ".properties-listing", "wait_time": 3},
            ]

            insert_navigation = text(
                """
                INSERT INTO steal_house.navigation_configs (
                    website_id, gallery_url_path, steps, next_page_selector
                )
                VALUES (
                    :website_id, '/aanbod', :steps, '.pagination__item--next a'
                )
            """
            )
            await session.execute(
                insert_navigation,
                {"website_id": website_id, "steps": json.dumps(nav_steps)},
            )

            # 4. Insert extraction config for gallery
            logger.info("Inserting Vesteda gallery extraction configuration")
            insert_gallery_config = text(
                """
                INSERT INTO steal_house.extraction_configs (
                    website_id, scope, extraction_method, base_selector
                )
                VALUES (
                    :website_id, 'gallery', 'css', '.card-apartment'
                )
                RETURNING id
            """
            )
            result = await session.execute(
                insert_gallery_config, {"website_id": website_id}
            )
            gallery_config_id = result.scalar()

            # 5. Insert field mappings for gallery
            logger.info("Inserting Vesteda gallery field mappings")
            gallery_mappings = [
                # Basic information
                ("address", ".card-apartment__street", "css", "text", None, True, None),
                ("city", ".card-apartment__city", "css", "text", None, True, None),
                (
                    "status",
                    ".card-apartment__status",
                    "css",
                    "text",
                    None,
                    True,
                    "For rent",
                ),
                # Financial information
                (
                    "rental_price",
                    ".card-apartment__price",
                    "css",
                    "text",
                    None,
                    False,
                    None,
                ),
                # Features
                (
                    "square_meters",
                    ".card-apartment__m2",
                    "css",
                    "text",
                    None,
                    False,
                    None,
                ),
                (
                    "bedrooms",
                    ".card-apartment__rooms",
                    "css",
                    "text",
                    None,
                    False,
                    None,
                ),
                # Detail link
                (
                    "detail_url",
                    ".card-apartment",
                    "css",
                    "attribute",
                    "href",
                    True,
                    None,
                ),
                # High demand indicator
                (
                    "high_demand",
                    ".card-apartment__high-demand",
                    "css",
                    "text",
                    None,
                    False,
                    "False",
                ),
                (
                    "demand_message",
                    ".card-apartment__high-demand",
                    "css",
                    "text",
                    None,
                    False,
                    None,
                ),
            ]

            for mapping in gallery_mappings:
                (
                    field_name,
                    selector,
                    selector_type,
                    extraction_type,
                    attribute_name,
                    is_required,
                    default_value,
                ) = mapping

                insert_mapping = text(
                    """
                    INSERT INTO steal_house.field_mappings (
                        extraction_config_id, pydantic_field_name, selector, 
                        selector_type, extraction_type, attribute_name, 
                        is_required, default_value
                    )
                    VALUES (
                        :config_id, :field_name, :selector, 
                        :selector_type, :extraction_type, :attribute_name, 
                        :is_required, :default_value
                    )
                """
                )

                await session.execute(
                    insert_mapping,
                    {
                        "config_id": gallery_config_id,
                        "field_name": field_name,
                        "selector": selector,
                        "selector_type": selector_type,
                        "extraction_type": extraction_type,
                        "attribute_name": attribute_name,
                        "is_required": is_required,
                        "default_value": default_value,
                    },
                )

            # 6. Insert extraction config for details
            logger.info("Inserting Vesteda detail extraction configuration")
            insert_detail_config = text(
                """
                INSERT INTO steal_house.extraction_configs (
                    website_id, scope, extraction_method, llm_provider, llm_instruction
                )
                VALUES (
                    :website_id, 'detail', 'llm', 'gemini', 
                    'Extract detailed property information from this real estate listing page. The returned data should include all available details about the property such as: address, city, status, rental price, service costs, available from date, square meters, number of bedrooms, neighborhood, energy label, complex name/description and any other property features mentioned.'
                )
            """
            )
            await session.execute(insert_detail_config, {"website_id": website_id})

            logger.info("Successfully inserted Vesteda website configuration")
            return website_id


async def main():
    """Main function"""
    try:
        website_id = await insert_vesteda_config()
        logger.info(
            f"Configuration inserted successfully for Vesteda (ID: {website_id})"
        )
    except Exception as e:
        logger.error(f"Error inserting configuration: {str(e)}")
        raise


if __name__ == "__main__":
    asyncio.run(main())
