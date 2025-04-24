"""create_website_scrape_configs_table

Revision ID: 8d90ad7a93d2
Revises: 6da2cb130ba5
Create Date: 2025-04-24 11:32:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8d90ad7a93d2"
down_revision: Union[str, None] = "6da2cb130ba5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "website_scrape_configs",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("website_identifier", sa.String(), nullable=False),
        sa.Column("config_json", sa.JSON(), nullable=False),
        sa.Column("version", sa.Integer(), nullable=True, default=1),
        sa.Column(
            "is_enabled", sa.Boolean(), nullable=False, server_default=sa.text("true")
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            server_default=sa.text("CURRENT_TIMESTAMP"),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            nullable=False,
            server_default=sa.text("CURRENT_TIMESTAMP"),
            onupdate=sa.text("CURRENT_TIMESTAMP"),
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("website_identifier"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("website_scrape_configs")
