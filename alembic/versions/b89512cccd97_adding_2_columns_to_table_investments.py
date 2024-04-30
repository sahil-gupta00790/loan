"""adding 2 columns to table investments

Revision ID: b89512cccd97
Revises: 5c8dfd81f98e
Create Date: 2024-04-28 16:36:18.300884

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b89512cccd97'
down_revision: Union[str, None] = '5c8dfd81f98e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('investment', sa.Column('amount_to_be_paid', sa.DECIMAL(10,2), nullable=True))
    op.add_column('investment', sa.Column('investment_date_end', sa.Date(), nullable=True))
    pass


def downgrade() -> None:
    pass
