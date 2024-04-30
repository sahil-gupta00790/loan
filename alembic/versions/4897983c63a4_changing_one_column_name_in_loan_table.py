"""changing one column name in loan table

Revision ID: 4897983c63a4
Revises: 1905ef5c1be6
Create Date: 2024-04-28 21:25:42.425834

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4897983c63a4'
down_revision: Union[str, None] = '1905ef5c1be6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('loan','status',new_column_name='approvval_status')
    op.alter_column('loan','approval_status',new_column_name='status_running')
    
    pass


def downgrade() -> None:
    pass
