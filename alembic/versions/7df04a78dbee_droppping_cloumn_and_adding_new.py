"""droppping cloumn and adding new

Revision ID: 7df04a78dbee
Revises: 08e5576cb44a
Create Date: 2024-04-28 17:09:37.161925

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7df04a78dbee'
down_revision: Union[str, None] = '08e5576cb44a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('investment','investment_date_end')
    
    pass


def downgrade() -> None:
    pass
