"""creating my first stored procedure-no idea what I'll do atm

Revision ID: fdbe1d164517
Revises: 3c55a160403c
Create Date: 2024-04-28 01:39:06.972247

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import text


# revision identifiers, used by Alembic.
revision: str = 'fdbe1d164517'
down_revision: Union[str, None] = '3c55a160403c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('loan', sa.Column('amount_to_be_paid_this_month', sa.Numeric(10, 2), nullable=True))
    op.alter_column('loan','Paid_last_one?',new_column_name='paid_last_one')
    pass

def downgrade() -> None:
    op.drop_column('loan', 'amount_to_be_paid_this_month')
    op.alter_column('loan', 'Paid_last_one?', new_column_name='paid_last_one')
    pass