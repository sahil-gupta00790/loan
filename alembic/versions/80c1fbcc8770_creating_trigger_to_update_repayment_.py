"""Creating trigger to update repayment_date column

Revision ID: 80c1fbcc8770
Revises: e4226c3f4579
Create Date: 2024-04-27 22:00:36.346546

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '80c1fbcc8770'
down_revision: Union[str, None] = 'e4226c3f4579'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('loan', 'amount_to_be_paid')
    op.add_column('loan',sa.Column('amount_to_be_paid',sa.Numeric(10,2),nullable=True))
    op.add_column('loan', sa.Column('total_amount_paid', sa.Numeric(10,2), default=0))
    pass


def downgrade() -> None:
    pass
