"""Adding phone number for employee_details

Revision ID: 716d4325cffe
Revises: f7ed07a72f23
Create Date: 2024-04-27 00:06:14.765574

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '716d4325cffe'
down_revision: Union[str, None] = 'f7ed07a72f23'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'employee_details',
        sa.Column('phone_number',sa.NUMERIC(10,0),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('employee_details', 'phone_number')
    pass
