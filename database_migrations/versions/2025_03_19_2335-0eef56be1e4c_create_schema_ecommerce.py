"""create schema ecommerce

Revision ID: 0eef56be1e4c
Revises: 
Create Date: 2025-03-19 23:35:41.586385

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0eef56be1e4c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute('CREATE SCHEMA IF NOT EXISTS steal_house;')
    


def downgrade() -> None:
    """Downgrade schema."""
    op.execute('DROP SCHEMA IF EXISTS steal_house CASCADE;')
