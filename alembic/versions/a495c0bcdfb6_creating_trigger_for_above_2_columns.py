"""Creating trigger for above 2 columns

Revision ID: a495c0bcdfb6
Revises: b89512cccd97
Create Date: 2024-04-28 16:38:33.472651

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text


# revision identifiers, used by Alembic.
revision: str = 'a495c0bcdfb6'
down_revision: Union[str, None] = 'b89512cccd97'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('investment', sa.Column('duration', sa.DECIMAL(2,2), nullable=False))
    pass


def downgrade() -> None:
    pass
