"""Changing pan card and aadhaar card column names in employee table

Revision ID: 4f2df112b47f
Revises: a2fc7ef3d2da
Create Date: 2024-04-27 02:05:44.896203

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4f2df112b47f'
down_revision: Union[str, None] = 'a2fc7ef3d2da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('employee_details', 'pan card', new_column_name='pan_number')
    op.alter_column('employee_details', 'aadhar card', new_column_name='aadhaar_number')
    pass


def downgrade() -> None:
    pass
