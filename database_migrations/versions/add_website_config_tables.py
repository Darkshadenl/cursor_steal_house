"""add website config tables

Revision ID: add_website_config_tables
Revises: refactor_house_models
Create Date: 2023-11-01T00:00:00.000000

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "add_website_config_tables"
down_revision = "refactor_house_models"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create websites table
    op.create_table(
        "websites",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("base_url", sa.String(length=255), nullable=False),
        sa.Column("is_active", sa.Boolean(), server_default="true", nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
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
        sa.Column("login_url_path", sa.String(length=255), nullable=True),
        sa.Column("username_selector", sa.String(length=255), nullable=False),
        sa.Column("password_selector", sa.String(length=255), nullable=False),
        sa.Column("submit_selector", sa.String(length=255), nullable=False),
        sa.Column("success_indicator_selector", sa.String(length=255), nullable=True),
        sa.Column("needs_login", sa.Boolean(), server_default="true", nullable=True),
        sa.Column("credential_source", sa.String(length=100), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["website_id"], ["steal_house.websites.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
        schema="steal_house",
    )

    # Create navigation_configs table
    op.create_table(
        "navigation_configs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("website_id", sa.Integer(), nullable=False),
        sa.Column("gallery_url_path", sa.String(length=255), nullable=False),
        sa.Column("steps", postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column("next_page_selector", sa.String(length=255), nullable=True),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["website_id"], ["steal_house.websites.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
        schema="steal_house",
    )

    # Create extraction_configs table
    op.create_table(
        "extraction_configs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("website_id", sa.Integer(), nullable=False),
        sa.Column("scope", sa.String(length=50), nullable=False),
        sa.Column(
            "extraction_method",
            sa.String(length=20),
            server_default="css",
            nullable=True,
        ),
        sa.Column("llm_provider", sa.String(length=50), nullable=True),
        sa.Column("llm_instruction", sa.Text(), nullable=True),
        sa.Column("base_selector", sa.String(length=255), nullable=True),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["website_id"], ["steal_house.websites.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "website_id", "scope", name="uix_extraction_config_website_scope"
        ),
        schema="steal_house",
    )

    # Create field_mappings table
    op.create_table(
        "field_mappings",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("extraction_config_id", sa.Integer(), nullable=False),
        sa.Column("pydantic_field_name", sa.String(length=100), nullable=False),
        sa.Column("selector", sa.String(length=255), nullable=False),
        sa.Column(
            "selector_type", sa.String(length=10), server_default="css", nullable=True
        ),
        sa.Column(
            "extraction_type",
            sa.String(length=20),
            server_default="text",
            nullable=True,
        ),
        sa.Column("attribute_name", sa.String(length=50), nullable=True),
        sa.Column("is_required", sa.Boolean(), server_default="false", nullable=True),
        sa.Column("default_value", sa.String(length=255), nullable=True),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["extraction_config_id"],
            ["steal_house.extraction_configs.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
        schema="steal_house",
    )

    # Add triggers for updated_at columns
    op.execute(
        """
    CREATE OR REPLACE FUNCTION steal_house.update_modified_column()
    RETURNS TRIGGER AS $$
    BEGIN
        NEW.updated_at = NOW();
        RETURN NEW;
    END;
    $$ language 'plpgsql';
    """
    )

    # Add update trigger for each table
    for table in [
        "websites",
        "login_configs",
        "navigation_configs",
        "extraction_configs",
        "field_mappings",
    ]:
        op.execute(
            f"""
        CREATE TRIGGER update_{table}_updated_at
        BEFORE UPDATE ON steal_house.{table}
        FOR EACH ROW
        EXECUTE FUNCTION steal_house.update_modified_column();
        """
        )


def downgrade() -> None:
    # Drop triggers first
    for table in [
        "field_mappings",
        "extraction_configs",
        "navigation_configs",
        "login_configs",
        "websites",
    ]:
        op.execute(
            f"DROP TRIGGER IF EXISTS update_{table}_updated_at ON steal_house.{table};"
        )

    # Drop function
    op.execute("DROP FUNCTION IF EXISTS steal_house.update_modified_column();")

    # Drop tables in reverse order
    op.drop_table("field_mappings", schema="steal_house")
    op.drop_table("extraction_configs", schema="steal_house")
    op.drop_table("navigation_configs", schema="steal_house")
    op.drop_table("login_configs", schema="steal_house")
    op.drop_table("websites", schema="steal_house")
