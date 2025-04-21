"""add_status_column_to_houses

Revision ID: 6da2cb130ba5
Revises: a1b2c3d4e5f6
Create Date: 2025-04-20 23:44:03.899531

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6da2cb130ba5"
down_revision: Union[str, None] = "a1b2c3d4e5f6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Add status column to houses table
    op.add_column(
        "houses",
        sa.Column("status", sa.String(), nullable=False, server_default="unknown"),
        schema="steal_house",
    )


def downgrade() -> None:
    """Downgrade schema."""
    # Remove status column from houses table
    op.drop_column("houses", "status", schema="steal_house")
