"""Adding phone number for customer_details

Revision ID: f7ed07a72f23
Revises: dee0e3125fb8
Create Date: 2024-04-27 00:05:28.494763

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f7ed07a72f23'
down_revision: Union[str, None] = 'dee0e3125fb8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'phone_number',
        sa.Column('customer_id', sa.Integer, primary_key=True),
        sa.Column('phone_number', sa.String(50), nullable=False,unique=True),
        sa.ForeignKeyConstraint(['customer_id'], ['customer_login.id'],ondelete='CASCADE')
        
        
        )
    pass


def downgrade() -> None:
    op.drop_table('phone_number')
    pass
