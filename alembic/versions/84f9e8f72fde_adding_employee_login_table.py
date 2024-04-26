"""Adding employee_login table

Revision ID: 84f9e8f72fde
Revises: d533474852e3
Create Date: 2024-04-27 00:00:50.382591

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84f9e8f72fde'
down_revision: Union[str, None] = 'd533474852e3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'employee_login',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(50), nullable=False,unique=True),
        sa.Column('password', sa.String(250), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'),nullable=False),
        
        
        )
    pass


def downgrade() -> None:
    op.drop_table('employee_login')
    pass