"""updating 2 investment  2 columns

Revision ID: 031f2bfefc27
Revises: a495c0bcdfb6
Create Date: 2024-04-28 16:55:53.199498

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '031f2bfefc27'
down_revision: Union[str, None] = 'a495c0bcdfb6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('investment', 'interest_rate',type_=sa.Numeric(10,2))
    op.alter_column('investment', 'duration', type_=sa.Numeric(10, 2))
    pass


def downgrade() -> None:
    pass
