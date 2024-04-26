"""Adding employee_details table

Revision ID: dee0e3125fb8
Revises: 68675f4caf06
Create Date: 2024-04-27 00:03:18.226083

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dee0e3125fb8'
down_revision: Union[str, None] = '68675f4caf06'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'employee_details',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('Name', sa.String(50), nullable=False),
        sa.Column('pan card', sa.String(12), nullable=False,unique=True),
        sa.Column('aadhar card', sa.NUMERIC(12,0), nullable=False,unique=True),
        sa.Column('address', sa.String(1000), nullable=False),
        sa.Column('Salary',sa.Numeric(10,0),nullable=False),
        sa.Column('start_date', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'),nullable=False),
        sa.Column('designation',sa.String(50),nullable=False),
        sa.ForeignKeyConstraint(['id'], ['employee_login.id'], ondelete='CASCADE'),
        )
        
    pass


def downgrade() -> None:
    op.drop_table('employee_details')
    pass
