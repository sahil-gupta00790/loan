"""Changing pan card and aadhaar card column names in customer table

Revision ID: eb5848122b06
Revises: 4f2df112b47f
Create Date: 2024-04-27 12:45:28.013519

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eb5848122b06'
down_revision: Union[str, None] = '4f2df112b47f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('customer_information', 'pan card', new_column_name='pan_number')
    op.alter_column('customer_information', 'aadhar card', new_column_name='aadhaar_number')
    pass


def downgrade() -> None:
    pass
