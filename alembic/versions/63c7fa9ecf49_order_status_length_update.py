"""Order status length update

Revision ID: 63c7fa9ecf49
Revises: c5ec11af7230
Create Date: 2025-11-06 21:06:34.922145

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "63c7fa9ecf49"
down_revision: Union[str, Sequence[str], None] = "c5ec11af7230"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        "order",
        "status",
        existing_type=sa.String(15),
        type_=sa.String(100),
        existing_nullable=True,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "order",
        "status",
        existing_type=sa.String(length=100),
        type_=sa.String(length=15),
        existing_nullable=True,
    )
