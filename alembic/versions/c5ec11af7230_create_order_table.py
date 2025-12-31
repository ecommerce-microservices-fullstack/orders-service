"""Create Order table

Revision ID: c5ec11af7230
Revises:
Create Date: 2025-11-01 16:49:32.653126

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c5ec11af7230"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "order",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("item_id", sa.Integer, nullable=False),
        sa.Column("qty", sa.Integer, nullable=False),
        sa.Column("status", sa.String(15), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("order")
