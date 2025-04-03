"""add_cascade_delete_for_gallery_houses

Revision ID: c93f29304c50
Revises: 730732ab93c4
Create Date: 2025-04-03 16:15:12.926793

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c93f29304c50"
down_revision: Union[str, None] = "730732ab93c4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Drop existing foreign key constraints
    op.drop_constraint(
        "detail_houses_gallery_id_fkey",
        "detail_houses",
        schema="steal_house",
        type_="foreignkey",
    )
    op.drop_constraint(
        "floor_plans_house_id_fkey",
        "floor_plans",
        schema="steal_house",
        type_="foreignkey",
    )

    # Recreate foreign key constraints with ON DELETE CASCADE
    op.create_foreign_key(
        "detail_houses_gallery_id_fkey",
        "detail_houses",
        "gallery_houses",
        ["gallery_id"],
        ["id"],
        source_schema="steal_house",
        referent_schema="steal_house",
        ondelete="CASCADE",
    )

    op.create_foreign_key(
        "floor_plans_house_id_fkey",
        "floor_plans",
        "detail_houses",
        ["house_id"],
        ["id"],
        source_schema="steal_house",
        referent_schema="steal_house",
        ondelete="CASCADE",
    )


def downgrade() -> None:
    """Downgrade schema."""
    # Drop cascade foreign key constraints
    op.drop_constraint(
        "detail_houses_gallery_id_fkey",
        "detail_houses",
        schema="steal_house",
        type_="foreignkey",
    )
    op.drop_constraint(
        "floor_plans_house_id_fkey",
        "floor_plans",
        schema="steal_house",
        type_="foreignkey",
    )

    # Recreate original foreign key constraints without CASCADE
    op.create_foreign_key(
        "detail_houses_gallery_id_fkey",
        "detail_houses",
        "gallery_houses",
        ["gallery_id"],
        ["id"],
        source_schema="steal_house",
        referent_schema="steal_house",
    )

    op.create_foreign_key(
        "floor_plans_house_id_fkey",
        "floor_plans",
        "detail_houses",
        ["house_id"],
        ["id"],
        source_schema="steal_house",
        referent_schema="steal_house",
    )
