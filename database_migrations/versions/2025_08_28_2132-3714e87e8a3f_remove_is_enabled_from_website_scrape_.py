"""remove_is_enabled_from_website_scrape_configs

Revision ID: 3714e87e8a3f
Revises: 6a0f80e2cff5
Create Date: 2025-08-28 21:30:46.172096

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3714e87e8a3f"
down_revision: Union[str, None] = "remove_manual_tables"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Remove the is_enabled column from website_scrape_configs table
    op.drop_column("website_scrape_configs", "is_enabled", schema="steal_house")


def downgrade() -> None:
    """Downgrade schema."""
    # Add the is_enabled column back to website_scrape_configs table
    op.add_column(
        "website_scrape_configs",
        sa.Column("is_enabled", sa.Boolean(), nullable=False, default=True),
        schema="steal_house",
    )
