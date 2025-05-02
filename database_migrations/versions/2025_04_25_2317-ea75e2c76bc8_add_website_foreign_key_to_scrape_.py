"""add_website_foreign_key_to_scrape_configs

Revision ID: ea75e2c76bc8
Revises: 8d90ad7a93d2
Create Date: 2025-04-25 23:17:39.679997

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ea75e2c76bc8"
down_revision: Union[str, None] = "8d90ad7a93d2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Change website_identifier to integer and add foreign key."""
    # Add new integer column
    op.add_column(
        "website_scrape_configs",
        sa.Column("website_id", sa.Integer(), nullable=True),
        schema="steal_house",
    )

    # Drop the old column and its unique constraint
    op.drop_constraint(
        "website_scrape_configs_website_identifier_key",
        "website_scrape_configs",
        schema="steal_house",
    )
    op.drop_column("website_scrape_configs", "website_identifier", schema="steal_house")

    # Rename new column to website_identifier
    op.alter_column(
        "website_scrape_configs",
        "website_id",
        new_column_name="website_identifier",
        schema="steal_house",
    )

    # Add unique constraint back
    op.create_unique_constraint(
        "website_scrape_configs_website_identifier_key",
        "website_scrape_configs",
        ["website_identifier"],
        schema="steal_house",
    )

    # Add foreign key
    op.create_foreign_key(
        "fk_website_scrape_configs_website",
        "website_scrape_configs",
        "websites",
        ["website_identifier"],
        ["id"],
        source_schema="steal_house",
        referent_schema="steal_house",
    )


def downgrade() -> None:
    """Revert website_identifier to varchar and remove foreign key."""
    # Drop foreign key
    op.drop_constraint(
        "fk_website_scrape_configs_website",
        "website_scrape_configs",
        schema="steal_house",
        type_="foreignkey",
    )

    # Drop unique constraint
    op.drop_constraint(
        "website_scrape_configs_website_identifier_key",
        "website_scrape_configs",
        schema="steal_house",
    )

    # Add temporary column
    op.add_column(
        "website_scrape_configs",
        sa.Column("website_identifier_old", sa.String(), nullable=True),
        schema="steal_house",
    )

    # Drop integer column
    op.drop_column("website_scrape_configs", "website_identifier", schema="steal_house")

    # Rename varchar column back
    op.alter_column(
        "website_scrape_configs",
        "website_identifier_old",
        new_column_name="website_identifier",
        schema="steal_house",
    )

    # Add unique constraint back
    op.create_unique_constraint(
        "website_scrape_configs_website_identifier_key",
        "website_scrape_configs",
        ["website_identifier"],
        schema="steal_house",
    )
