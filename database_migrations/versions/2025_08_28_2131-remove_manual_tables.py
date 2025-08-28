"""remove_manual_tables

Revision ID: remove_manual_tables
Revises: 6a0f80e2cff5
Create Date: 2025-08-28 21:31:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "remove_manual_tables"
down_revision: Union[str, None] = "6a0f80e2cff5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Remove tables that were manually deleted
    # These tables no longer exist in the database, so we just drop them
    # to keep the migration history consistent
    # Drop in reverse dependency order (child tables first)
    op.drop_table("field_mappings", schema="steal_house")
    op.drop_table("extraction_configs", schema="steal_house")
    op.drop_table("navigation_configs", schema="steal_house")
    op.drop_table("login_configs", schema="steal_house")


def downgrade() -> None:
    """Downgrade schema."""
    # Recreate the tables that were manually deleted
    # Note: This will fail if the tables already exist

    # Recreate login_configs table
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

    # Recreate navigation_configs table
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

    # Recreate extraction_configs table
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

    # Recreate field_mappings table
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
