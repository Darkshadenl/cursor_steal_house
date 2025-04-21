"""Combine initial house and config migrations

Revision ID: a1b2c3d4e5f6
Revises: c93f29304c50
Create Date: 2025-04-20 23:15:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Session


# revision identifiers, used by Alembic.
revision: str = "a1b2c3d4e5f6"
down_revision: Union[str, None] = None  # This is now the first migration in the chain
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema with combined initial migrations."""
    # Create the steal_house schema if it doesn't exist
    op.execute("CREATE SCHEMA IF NOT EXISTS steal_house")

    # --- Start: Content from 2025_04_05_0001-refactor_house_models.py ---

    # Create the new houses table
    op.create_table(
        "houses",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("address", sa.String(), nullable=False),
        sa.Column("city", sa.String(), nullable=False),
        sa.Column("postal_code", sa.String(), nullable=True),
        sa.Column("neighborhood", sa.String(), nullable=True),
        sa.Column("status", sa.String(), nullable=False),
        sa.Column("high_demand", sa.Boolean(), nullable=True),
        sa.Column("demand_message", sa.String(), nullable=True),
        sa.Column("detail_url", sa.String(), nullable=True),
        sa.Column("rental_price", sa.String(), nullable=True),
        sa.Column("service_costs", sa.String(), nullable=True),
        sa.Column("min_income_single", sa.String(), nullable=True),
        sa.Column("min_income_joint", sa.String(), nullable=True),
        sa.Column("read_more_url", sa.String(), nullable=True),
        sa.Column("square_meters", sa.Integer(), nullable=True),
        sa.Column("bedrooms", sa.Integer(), nullable=True),
        sa.Column("energy_label", sa.String(), nullable=True),
        sa.Column("available_from", sa.String(), nullable=True),
        sa.Column("complex", sa.String(), nullable=True),
        sa.Column("complex_name", sa.String(), nullable=True),
        sa.Column("complex_description", sa.Text(), nullable=True),
        sa.Column("year_of_construction", sa.Integer(), nullable=True),
        sa.Column("number_of_objects", sa.String(), nullable=True),
        sa.Column("number_of_floors", sa.String(), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("location_map_url", sa.String(), nullable=True),
        sa.Column("request_viewing_url", sa.String(), nullable=True),
        sa.Column("options", sa.Text(), nullable=True),
        sa.Column("image_url", sa.String(), nullable=True),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
        schema="steal_house",
    )

    # --- End: Content from 2025_04_05_0001-refactor_house_models.py ---

    # --- Start: Content from 2025_04_20_2313-d8f972818f92_simplify_and_add_config_tables.py ---

    # Create websites table
    op.create_table(
        "websites",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("base_url", sa.String(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
        schema="steal_house",
    )

    # Create login_configs table
    op.create_table(
        "login_configs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("website_id", sa.Integer(), nullable=False),
        sa.Column("login_url", sa.String(), nullable=False),
        sa.Column("username_selector", sa.String(), nullable=False),
        sa.Column("password_selector", sa.String(), nullable=False),
        sa.Column("submit_selector", sa.String(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["website_id"], ["steal_house.websites.id"], ondelete="CASCADE"
        ),
        schema="steal_house",
    )

    # Create navigation_configs table
    op.create_table(
        "navigation_configs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("website_id", sa.Integer(), nullable=False),
        sa.Column("listing_page_url", sa.String(), nullable=False),
        sa.Column("listing_selector", sa.String(), nullable=False),
        sa.Column("next_page_selector", sa.String(), nullable=True),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["website_id"], ["steal_house.websites.id"], ondelete="CASCADE"
        ),
        schema="steal_house",
    )

    # Create extraction_configs table
    op.create_table(
        "extraction_configs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("website_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("selector", sa.String(), nullable=False),
        sa.Column("extraction_type", sa.String(), nullable=False),
        sa.Column("attribute_name", sa.String(), nullable=True),
        sa.Column(
            "is_required", sa.Boolean(), nullable=False, server_default=sa.false()
        ),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["website_id"], ["steal_house.websites.id"], ondelete="CASCADE"
        ),
        schema="steal_house",
    )

    # Create field_mappings table
    op.create_table(
        "field_mappings",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("extraction_config_id", sa.Integer(), nullable=False),
        sa.Column("target_field", sa.String(), nullable=False),
        sa.Column("transformation_rule", sa.JSON(), nullable=True),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["extraction_config_id"],
            ["steal_house.extraction_configs.id"],
            ondelete="CASCADE",
        ),
        schema="steal_house",
    )

    # Remove the 'status' column from 'houses'
    op.drop_column("houses", "status", schema="steal_house")

    # --- End: Content from 2025_04_20_2313-d8f972818f92_simplify_and_add_config_tables.py ---


def downgrade() -> None:
    """Downgrade schema by reverting combined initial migrations."""

    # --- Start: Reverting 2025_04_20_2313-d8f972818f92_simplify_and_add_config_tables.py ---

    # Add the 'status' column back to 'houses'
    op.add_column(
        "houses",
        sa.Column("status", sa.String(), nullable=False, server_default="unknown"),
        schema="steal_house",
    )

    # Drop config tables in reverse order of creation
    op.drop_table("field_mappings", schema="steal_house")
    op.drop_table("extraction_configs", schema="steal_house")
    op.drop_table("navigation_configs", schema="steal_house")
    op.drop_table("login_configs", schema="steal_house")
    op.drop_table("websites", schema="steal_house")

    # --- End: Reverting 2025_04_20_2313-d8f972818f92_simplify_and_add_config_tables.py ---

    # --- Start: Reverting 2025_04_05_0001-refactor_house_models.py ---

    # Drop the unified houses table
    op.drop_table("houses", schema="steal_house")

    # --- End: Reverting 2025_04_05_0001-refactor_house_models.py ---

    # Drop the schema if empty (will fail if it still contains objects, which is a safety measure)
    op.execute("DROP SCHEMA IF EXISTS steal_house")
